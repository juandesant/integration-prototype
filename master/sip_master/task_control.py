""" Functions for comanding a slave controller to load and unload tasks
"""

import rpyc

from sip_master import config

def load(name, cfg, status):
    """ Command the slave controller to load a task
    """

    # Scan the task parameter list for entries with values starting with a #
    # character and replace with an allocated resource.
    task_cfg = cfg['task']
    for k,v in enumerate(task_cfg):
        if v[0] == '#':
            task_cfg[k] = str(config.resource.allocate_resource(name, v[1:]))
    conn = rpyc.connect(status['address'], status['rpc_port'])
    conn.root.load(task_cfg)
    status['state']= 'loading'

def unload(cfg, status):
    """ Command the slave controller to unload the task
    """
    conn = rpyc.connect(status['address'], status['rpc_port'])
    conn.root.unload(cfg['task'])
