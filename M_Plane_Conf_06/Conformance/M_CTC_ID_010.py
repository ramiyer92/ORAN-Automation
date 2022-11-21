###############################################################################
##@ FILE NAME:      M_CTC_ID_010
##@ TEST SCOPE:     M PLANE O-RAN CONFORMANCE
##@ Version:        V_1.0.0
##@ Support:        @Ramiyer, @VaibhavDhiman, @PriyaSharma
###############################################################################

###############################################################################
## Package Imports 
###############################################################################


import socket, sys, os, warnings, time, xmltodict, xml.dom.minidom, paramiko, lxml.etree
from ncclient import manager
from ncclient.operations.rpc import RPC, RPCError
from ncclient.transport import errors
from paramiko.ssh_exception import NoValidConnectionsError
from ncclient.operations.errors import TimeoutExpiredError
from ncclient.transport.errors import SessionCloseError
from configparser import ConfigParser
from scapy.all import *

###############################################################################
## Directory Path
###############################################################################
dir_name = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(dir_name)
# print(parent)
sys.path.append(parent)

########################################################################
## For reading data from .ini file
########################################################################
configur = ConfigParser()
configur.read('{}/inputs.ini'.format(dir_name))

###############################################################################
## Related Imports
###############################################################################
from require import STARTUP, Config
from require.Vlan_Creation import *


###############################################################################
## Initiate PDF
###############################################################################
pdf = STARTUP.PDF_CAP()


class M_CTC_ID_010(vlan_Creation):

    # init method or constructor
    def __init__(self) -> None:
        super().__init__()
        self.interface_name = ''
        self.hostname, self.call_home_port = '',''
        self.USER_N = ''
        self.PSWRD = ''
        self.session = ''

    ###############################################################################
    ## SFP Link Detection
    ###############################################################################
    def sfp_Linked(self):
        ## Check Point 1
        Check1 = True
        self.interface_name = self.linked_detected()
        if self.interface_name:
            pass
        else:
            Check1 = False
        return Check1

    ###############################################################################
    ## Test Execution and Procedure
    ###############################################################################
    def test_procedure(self):
        STARTUP.STORE_DATA('\n\n\t\t********** Connect to the NETCONF Server ***********\n\n',Format='TEST_STEP',PDF = pdf)
        STATUS = STARTUP.STATUS(self.hostname,self.USER_N,self.session.session_id,830)
        STARTUP.STORE_DATA(STATUS,Format=False,PDF = pdf)


        ###############################################################################
        ## Server Capabilities
        ###############################################################################
        for cap in self.session.server_capabilities:
            STARTUP.STORE_DATA("\t{}".format(cap),Format=False,PDF = pdf)
            
        ###############################################################################
        ## Create_subscription
        ###############################################################################
        cap=self.session.create_subscription()
        STARTUP.STORE_DATA('> subscribe', Format=True, PDF=pdf)
        dict_data = xmltodict.parse(str(cap))
        if dict_data['nc:rpc-reply']['nc:ok'] == None:
            STARTUP.STORE_DATA('\nOk\n', Format=False, PDF=pdf)
           

        pdf.add_page()
        ###############################################################################
        ## Test Procedure 1
        ###############################################################################
        Test_Step1 = '\t\t Step 1 The TER NETCONF Client triggers <rpc><get> towards the O-RU NETCONF Server.'
        STARTUP.STORE_DATA('{}'.format(Test_Step1),Format = 'TEST_STEP',PDF=pdf)
        STARTUP.STORE_DATA('{}'.format('> get'), Format = True,PDF=pdf)
        
        ###############################################################################
        ## Test Procedure 2
        ###############################################################################
        Test_Step2 = '\t\t Step 2 The O-RU NETCONF Server responds with <rpc-reply><data> where <data> contains all information elements that the O-RU NETCONF Server is able to expose'
        STARTUP.STORE_DATA(
            '{}'.format(Test_Step2), Format = 'TEST_STEP',PDF=pdf)


        ###############################################################################
        ## Get the RU details without filter
        ###############################################################################
        Data = self.session.get(filter=None, with_defaults=None).data_xml
        x = xml.dom.minidom.parseString(Data)
        xml_pretty_str = x.toprettyxml()
        STARTUP.STORE_DATA(xml_pretty_str, Format = 'XML',PDF=pdf)
        return True



    ###############################################################################
    ## Main Function
    ###############################################################################
    def test_Main_010(self):
        Check1 = self.sfp_Linked()
        
        print(self.hostname)
        ###############################################################################
        ## Read User Name and password from Config.INI of Config.py
        ###############################################################################
        self.USER_N = configur.get('INFO','sudo_user')
        self.PSWRD = configur.get('INFO','sudo_pass')
        if Check1 == False or Check1 == None:
            return Check1

        sniff(iface = self.interface, stop_filter = self.check_tcp_ip, timeout = 100)
        try:
            STARTUP.delete_system_log(host= self.hostname)
            time.sleep(2)
            ###############################################################################
            ## Perform call home to get ip_details
            ###############################################################################
            self.session = STARTUP.call_home(host = '0.0.0.0', port=4334, hostkey_verify=False,username = self.USER_N, password = self.PSWRD,timeout = 60,allow_agent = False , look_for_keys = False)
            self.hostname, self.call_home_port = self.session._session._transport.sock.getpeername()   #['ip_address', 'TCP_Port']
            
            if self.session:
                RU_Details = STARTUP.demo(session = self.session,host= self.hostname, port= 830)

                for key, val in RU_Details[1].items():
                    if val[0] == 'true' and val[1] == 'true':

                        ###############################################################################
                        ## Test Description
                        ###############################################################################
                        Test_Desc = 'Test Description : This scenario validates that the O-RU NETCONF Server properly executes a general get command.'
                        CONFIDENTIAL = STARTUP.ADD_CONFIDENTIAL(
                            '10', SW_R=val[2])
                        STARTUP.STORE_DATA(CONFIDENTIAL, Format = 'CONF',PDF=pdf)
                        STARTUP.STORE_DATA(Test_Desc,Format = 'DESC',PDF= pdf)
                        pdf.add_page()
                time.sleep(5)
                result = self.test_procedure()
                # self.session.close_session()
                if result == True:
                    return True
                else:
                    return result


        ###############################################################################
        ## Exception
        ###############################################################################
        except socket.timeout as e:
            Error = '{} : Call Home is not initiated, SSH Socket connection lost....'.format(
                e)
            STARTUP.STORE_DATA(Error, Format=True,PDF=pdf)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            STARTUP.STORE_DATA(
                f"Error occured in line number {exc_tb.tb_lineno}", Format=False,PDF=pdf)
            return Error

        except RPCError as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            STARTUP.STORE_DATA(
                f"Error occured in line number {exc_tb.tb_lineno}", Format=False,PDF=pdf)
            # self.session.close_session()
            return [e.type, e.tag, e.severity, e.path, e.message, exc_tb.tb_lineno]

        except Exception as e:
            STARTUP.STORE_DATA('{}'.format(e), Format=True,PDF=pdf)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            STARTUP.STORE_DATA(
                f"Error occured in line number {exc_tb.tb_lineno}", Format=False,PDF=pdf)
            # self.session.close_session()
            return e
            
        finally:
            try:
                self.session.close_session()
            except Exception as e:
                print(e)

        

    

def test_m_ctc_id_010():
    tc010_obj = M_CTC_ID_010()
    Check = tc010_obj.test_Main_010()
    if Check == False:
        STARTUP.STORE_DATA('{0} FAIL_REASON {0}'.format('*'*20),Format=True,PDF= pdf)
        STARTUP.STORE_DATA('{}'.format('SFP Link not detected..'),Format=False,PDF= pdf)
        STARTUP.ACT_RES(f"{'Retrieval without Filter Applied' : <50}{'=' : ^20}{'FAIL' : ^20}",PDF= pdf,COL=(235, 52, 52))
        return False

    ###############################################################################
    ## Expected/Actual Result and System Logs
    ###############################################################################
    STARTUP.GET_SYSTEM_LOGS(tc010_obj.hostname,tc010_obj.USER_N,tc010_obj.PSWRD,pdf)
    Exp_Result = 'Expected Result : The O-RU NETCONF Server responds with <rpc-reply><data> where <data> contains all information elements that the O-RU NETCONF Server is able to expose'
    STARTUP.STORE_DATA(Exp_Result,Format = 'DESC',PDF= pdf)

    STARTUP.STORE_DATA('\t\t{}'.format('****************** Actual Result ******************'),Format = True,PDF= pdf)
    try:
        if Check == True:
            STARTUP.ACT_RES(f"{'Retrieval without Filter Applied' : <50}{'=' : ^20}{'SUCCESS' : ^20}",PDF= pdf,COL=(105, 224, 113))
            return True
            
        elif type(Check) == list:
            STARTUP.STORE_DATA('{0} FAIL_REASON {0}'.format('*'*20),Format=True,PDF= pdf)
            Error_Info = '''\terror-tag \t: \t{}\n\terror-type \t: \t{}\n\terror-severity \t: \t{}\n\tDescription' \t: \t{}'''.format(*map(str,Check))
            STARTUP.STORE_DATA(Error_Info,Format=False,PDF= pdf)
            STARTUP.ACT_RES(f"{'Retrieval without Filter Applied' : <50}{'=' : ^20}{'FAIL' : ^20}",PDF= pdf,COL=(235, 52, 52))
            return False
        else:
            STARTUP.STORE_DATA('{0} FAIL_REASON {0}'.format('*'*20),Format=True,PDF= pdf)
            STARTUP.STORE_DATA('{}'.format(Check),Format=False,PDF= pdf)
            STARTUP.ACT_RES(f"{'Retrieval without Filter Applied' : <50}{'=' : ^20}{'FAIL' : ^20}",PDF= pdf,COL=(235, 52, 52))
            return False


    except Exception as e:
            STARTUP.STORE_DATA('{}'.format(e), Format=True,PDF=pdf)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            STARTUP.STORE_DATA(
                f"Error occured in line number {exc_tb.tb_lineno}", Format=False,PDF=pdf)
            return False


    ###############################################################################
    ## For Capturing the logs
    ###############################################################################
    finally:
        STARTUP.CREATE_LOGS('M_CTC_ID_010',PDF=pdf)

if __name__ == "__main__":
    test_m_ctc_id_010()
