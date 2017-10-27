# coding: utf-8
"""This module provides Python logging handlers (and formatters) to be used
with SIP logging functions.

Example:

.. code-block:: python

    l = logging.getLogger('my.logger')
    l.addHandler(ZmqHandler.bind('cap:ingest:vis', port=5555)
    l.setLevel('DEBUG')
    l.info('A message')

.. moduleauthor:: Benjamin Mort <benjamin.mort@oerc.ox.ac.uk>
"""
import logging
import logging.handlers
import time

import simplejson as json
import zmq


class ZmqLogFormatter(logging.Formatter):
    """Formats log messages for the ZmqLogHandler."""

    def format(self, record):
        """Returns a JSON string which encodes the log record.

        Args:
            record (logging.LogRecord): Log record object.

        Returns:
            string, JSON formatted SIP Log record.
        """
        return json.dumps(record._raw.copy(), sort_keys=True)


class ZmqLogHandler(logging.Handler):
    """Publishes log messages to a ZMQ PUB socket."""

    @classmethod
    def to(cls, channel, host='127.0.0.1',
           port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
           level=logging.NOTSET):
        """Convenience class method to create a ZmqLoghandler and
        connect to a ZMQ subscriber.

        Args:
            channel (string): Logging channel name. This is used to build a
                              ZMQ topic.
            host (string): Hostname / ip address of the subscriber to publish
                           to.
            port (int, string): Port on which to publish messages.
            level (int): Logging level
        """
        print(port)
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        address = 'tcp://{}:{}'.format(host, port)
        publisher.connect(address)
        time.sleep(0.1)  # This sleep hopefully fixes the silent joiner problem.
        return cls(channel, publisher, level=level)

    def __init__(self, channel, zmq_publisher, level=logging.NOTSET):
        """Constructor.
        Create a new log handler from given channel and ZMQ pub. socket.

        Args:
            channel (string): Logging channel name. This is used to build a
                              ZMQ topic.
            zmq_publisher: Connected ZMQ PUB socket object.
            level (int) Logging level.
        """
        logging.Handler.__init__(self, level)
        self.channel = channel
        self.zmq_publisher = zmq_publisher
        self.formatter = ZmqLogFormatter()

    @staticmethod
    def _to_bytes(s):
            """Convert unicode argument s to bytes

            Args:
                s: Unicode string to convert.

            Returns:
                Input string encoded as a utf8 byte array.
            """
            if isinstance(s, bytes):
                return s
            elif isinstance(s, str):
                return s.encode(encoding='utf8', errors='strict')
            else:
                raise TypeError("Expected unicode or bytes, got %r" % s)

    def emit(self, record: logging.LogRecord):
        """Publish log message over ZMQ

        Writes a JSONified LogRecord to the ZMQ PUB socket. The record is
        converted to JSON by the attached ZmqLogFormatter class.

        Args:
            record: LogRecord object.
        """
        b_chan = self._to_bytes(self.channel)
        b_level = self._to_bytes(record.levelname)
        b_chan = b':'.join([b_level, b_chan])
        b_msg = self._to_bytes(self.format(record))
        self.zmq_publisher.send_multipart([b_chan, b_msg])


