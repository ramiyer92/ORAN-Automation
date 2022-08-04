from asyncio import FastChildWatcher, streams
import sys
from ncclient import manager
from ncclient.xml_ import to_ele
import xmltodict
import socket
import xml.dom.minidom
import paramiko
import STARTUP
from scp import SCPException
from paramiko import SSHClient
from scp import SCPClient

pdf = STARTUP.PDF_CAP()

def kill_ssn(host, port, user, password,sid):
    with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
        m.kill_session(sid)

def session_login(host, port, user, password):
    try:
        with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
            STARTUP.STORE_DATA('Step 1 Connect to the NETCONF Server',Format = True,PDF = pdf)
            STARTUP.STORE_DATA(f'''> connect --ssh --host {host} --port 830 --login {user}
                    Interactive SSH Authentication
                    Type your password:
                    Password: 
                    > status
                    Current NETCONF session:
                    ID          : {m.session_id}
                    Host        : {host}
                    Port        : {port}
                    Transport   : SSH
                    Capabilities:
                    ''',Format = False,PDF = pdf)
            for i in m.server_capabilities:
                STARTUP.STORE_DATA(i,Format = False,PDF = pdf)

            cap = m.create_subscription()

            STARTUP.STORE_DATA('>subscribe',Format = True,PDF = pdf)
            dict_data = xmltodict.parse(str(cap))
            if dict_data['nc:rpc-reply']['nc:ok']== None:
                STARTUP.STORE_DATA('Ok',Format = False,PDF = pdf)
            pdf.add_page()
            STARTUP.STORE_DATA('Step 2 Freerun State of O-RU in Startup Condition',Format = True,PDF = pdf)
            SYNC = '''<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <sync xmlns="urn:o-ran:sync:1.0">
            </sync>
            </filter>
            '''
        
            data1  = m.get(SYNC).data_xml
            x = xml.dom.minidom.parseString(data1)
            

            xml_pretty_str = x.toprettyxml()
            STARTUP.STORE_DATA('Expected Result',Format = True,PDF = pdf)
            STARTUP.STORE_DATA(xml_pretty_str,Format = "XML",PDF= pdf)
    
    except Exception as e:
        STARTUP.STORE_DATA(f"{e}",Format = "TEST_STEP",PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format = "TEST_STEP",PDF = pdf)

def Result_Decleration(host, port, user, password):
    try:
        with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
            pdf.add_page()
            STARTUP.STORE_DATA('RESULTS',Format =True,PDF = pdf)
            SYNC = '''
                <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <sync xmlns="urn:o-ran:sync:1.0">
                </sync>
                </filter>
                '''
       
            value_SYNC = m.get(SYNC).data_xml
 
            dict_Sync = xmltodict.parse(str(value_SYNC))
            Sync_state=dict_Sync['data']['sync']['sync-status']['sync-state']

            STARTUP.STORE_DATA(f"{'Sync_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if Sync_state == "FREERUN" else f"{'Sync_state STATUS' : <50}{'=' : ^20}{'FAIL' : ^20}",Format = FastChildWatcher,PDF = pdf)
            
            Ptp_lock_state=dict_Sync['data']['sync']['ptp-status']['lock-state']
            STARTUP.STORE_DATA(f"{'Ptp_lock_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if Ptp_lock_state == "UNLOCKED" else f"{'Ptp_lock_state STATUS' : <50}{'=' : ^20}{'FAIL' : ^20}",Format = False,PDF = pdf)
            
            Ptp_state=dict_Sync['data']['sync']['ptp-status']['sources']['state']
            STARTUP.STORE_DATA(f"{'Ptp_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if Ptp_state == "DISABLED" else f"{'Ptp_state STATUS' : <50}{'=' : ^20}{'FAIL' : ^20}",Format = False,PDF = pdf)
            
            SyncE_lock_state=dict_Sync['data']['sync']['synce-status']['lock-state']
            STARTUP.STORE_DATA(f"{'SyncE_lock_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if SyncE_lock_state == "UNLOCKED" else f"{'SyncE_lock_state STATUS' : <50}{'=' : ^20}{'FAIL' : ^20}",Format = False,PDF = pdf)

            SyncE_state=dict_Sync['data']['sync']['synce-status']['sources']['state']
            STARTUP.STORE_DATA(f"{'SyncE_State STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if SyncE_state == "DISABLED" else f"{'SyncE_state STATUS' : <50}{'=' : ^20}{'FAIL' : ^20}",Format = False,PDF = pdf)
    except Exception as e:
        STARTUP.STORE_DATA(f"{e}",Format = "TEST_STEP",PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format = False,PDF = pdf)

def CREATE_LOGS(PDF,name):
    name1 = str(path) + "/" +str(name) + ".pdf"
    PDF.output(name1)

if __name__ == '__main__':
    try:
        print('Provide the credentials for SSH')
        usr = input("Enter the username: ")
        pss = input("Enter the Password: ")
        m = manager.call_home(host = '', port=4334, hostkey_verify=False,username =usr, password =pss)

        li = m._session._transport.sock.getpeername()
        sid = m.session_id
        kill_ssn(li[0],830,usr,pss,sid)
        res = session_login(li[0],830,usr,pss)
        pdf.add_page()
        STARTUP.STORE_DATA('SYSTEM LOGS',Format = True,PDF = pdf)
        command = "cd /media/sd-mmcblk0p4; cat garuda.log | grep SYNCMNGR;"
        command1 = "cd /media/sd-mmcblk0p4; rm -rf garuda.log;"
        # STARTUP.STORE_DATA("Result Decleration",Format =True,PDF = pdf)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=li[0],username='root',password='garuda')

        stdin, stdout, stderr = ssh_client.exec_command(command)
        lines = stdout.readlines()
        for i in lines:
            STARTUP.STORE_DATA(i,Format ="XML",PDF = pdf)
        stdin, stdout, stderr = ssh_client.exec_command(command1)
        Result_Decleration(li[0],830,usr,pss)
        path = input('Enter the path to save SI LAB logs and PDF')
        Remote_path= path + "/TC1.log"
        ssh_ob = SSHClient()
        ssh_ob.load_system_host_keys()
        ssh_ob.connect(hostname=li[0],username=usr,password="root")
        scp = SCPClient(ssh_ob.get_transport())
        scp.get('/var/log/synctimingptp2.log',Remote_path)
        scp.close()
        CREATE_LOGS(pdf,name = "S_CTC_ID_001")
   
    except SCPException as e:
        STARTUP.STORE_DATA("File Not found in RU",Format = False,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format =False,PDF = pdf)

    except UnicodeError as e:
        STARTUP.STORE_DATA(f"{e}","Please give correct Ip address",Format =False,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format = False,PDF = pdf)

    except paramiko.ssh_exception.AuthenticationException as e:
        STARTUP.STORE_DATA(f"{e}","Please give correct username or password",Format =False,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format = False,PDF = pdf)

    except socket.timeout as e:
        STARTUP.STORE_DATA(f'{e}',Format = False,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format = False,PDF = pdf)
    
    except Exception as e:
        STARTUP.STORE_DATA(f'{e}',Format = "TEST_STEP",PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',f'{exc_tb.tb_lineno}',Format = False,PDF = pdf)
