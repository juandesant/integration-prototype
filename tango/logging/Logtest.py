#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        Logtest.py
#
#  Project :     Test Log Consumer
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      brian.mcilwrath$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["Logtest", "LogtestClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(Logtest.additionnal_import) ENABLED START -----#
import datetime

#----- PROTECTED REGION END -----#	//	Logtest.additionnal_import

# Device States Description
# No states for this device


class Logtest (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(Logtest.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Logtest.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        self.get_logger().set_level(3)
        Logtest.init_device(self)
        #----- PROTECTED REGION ID(Logtest.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Logtest.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(Logtest.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Logtest.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        #----- PROTECTED REGION ID(Logtest.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Logtest.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(Logtest.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Logtest.always_executed_hook

    # -------------------------------------------------------------------------
    #    Logtest read/write attribute methods
    # -------------------------------------------------------------------------
    
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(Logtest.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Logtest.read_attr_hardware


    # -------------------------------------------------------------------------
    #    Logtest command methods
    # -------------------------------------------------------------------------
    
    def log(self, argin):
        """ 
        :param argin: 
        :type argin: PyTango.DevVarStringArray
        """
        self.debug_stream("In log()")
        #----- PROTECTED REGION ID(Logtest.log) ENABLED START -----#
        # Tango Manual Appendix 9 gives the format
        # argin[0] = millisecond Unix timestamp
        # argin[1] = log level
        # argin[2] = the source log device name
        # argin[3] = the log message
        # argin[4] = Not used - reserved
        # argin[5] = thread identifier of originating message
        t = datetime.datetime.fromtimestamp(float(argin[0])/1000.)
        fmt = "%Y-%m-%d %H:%M:%S"
        self.info_stream("{} - {} {} {}".format(t.strftime(fmt),argin[1],
             argin[2], argin[3]))
        #----- PROTECTED REGION END -----#	//	Logtest.log
        

    #----- PROTECTED REGION ID(Logtest.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Logtest.programmer_methods

class LogtestClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(Logtest.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Logtest.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        'log':
            [[PyTango.DevVarStringArray, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(LogtestClass, Logtest, 'Logtest')
        #----- PROTECTED REGION ID(Logtest.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Logtest.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
