from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import socket
import sys
import json
from ncclient import manager
import xmltodict
import xml.dom.minidom
import time
import paramiko
from scp import SCPException
from paramiko import SSHClient
from scp import SCPClient
import STARTUP
from calnexRest import calnexInit, calnexGet, calnexSet, calnexCreate, calnexDel
pdf = STARTUP.PDF_CAP()


def kill_ssn(host, port, user, password,sid):
    with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
        m.kill_session(sid)

def session_login(host, port, user, password):
    try:
        with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:

            STARTUP.STORE_DATA('********** Connect to the NETCONF Server ***********',STARTUP = True,PDF = pdf)

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
                    ''',STARTUP = False,PDF = pdf)
            for i in m.server_capabilities:
                STARTUP.STORE_DATA(i,STARTUP = False,PDF = pdf)

            rpc=m.create_subscription()


            STARTUP.STORE_DATA('>subscribe',STARTUP = True,PDF = pdf)

            dict_data = xmltodict.parse(str(rpc))
            if dict_data['nc:rpc-reply']['nc:ok']== None:
                STARTUP.STORE_DATA('Ok',STARTUP = False,PDF = pdf)

            STARTUP.STORE_DATA("Initial configuratin of o-ru before synchronization",STARTUP = True,PDF = pdf)

            SYNC = '''<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <sync xmlns="urn:o-ran:sync:1.0">
            </sync>
            </filter>
            '''


            data1  = m.get(SYNC).data_xml
            x = xml.dom.minidom.parseString(data1)
            

            xml_pretty_str = x.toprettyxml()
            STARTUP.STORE_DATA(xml_pretty_str,STARTUP = "XML",PDF = pdf)
            calnexSet("app/mse/master/Master1/start")
            time.sleep(10)
            time.sleep(10)
            driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_linux641/chromedriver')
            driver.get("http://172.17.80.2/#/testMeasurement/playlist")
            time.sleep(5)
            driver.minimize_window()

            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='trackContainerTracksNode']/track-master-slave-emulation/div/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[4]/div[3]/div/div[1]/div"))).get_attribute("class")
            if element == "detected":
    
                STARTUP.STORE_DATA('Enable ptp and syncE and capturing notifications for ptp , synce and ru-sync states',STARTUP = True,PDF = pdf)
    
                calnexSet("app/generation/synce/esmc/Port1/start")

                while True:
                        n = m.take_notification()
                        notify=n.notification_xml
                        dict_notify = xmltodict.parse(str(notify))
                        input_dict =  dict_notify
                        output_dict = json.loads(json.dumps(input_dict)) 
                        def recursive_items(dictionary):
                            for key, value in dictionary.items():
                                if type(value) is dict:
                                    yield from recursive_items(value)
                                else:
                                    yield (key, value)
                        for key, value in recursive_items(output_dict):
                            NF1 = key
                        if NF1=='synce-state':
                            s = xml.dom.minidom.parseString(notify)
                            xml_pretty_str = s.toprettyxml()
                            STARTUP.STORE_DATA(xml_pretty_str,STARTUP = False,PDF = pdf)
                            break
                while True:
                        n = m.take_notification()
                        notify=n.notification_xml
                        dict_notify = xmltodict.parse(str(notify))
                        input_dict =  dict_notify
                        output_dict = json.loads(json.dumps(input_dict)) 
                        def recursive_items(dictionary):
                            for key, value in dictionary.items():
                                if type(value) is dict:
                                    yield from recursive_items(value)
                                else:
                                    yield (key, value)
                        for key, value in recursive_items(output_dict):
                            NF1 = key
                        
                        if NF1=='ptp-state':
                            s = xml.dom.minidom.parseString(notify)
                            

                            xml_pretty_str = s.toprettyxml()

                            STARTUP.STORE_DATA(xml_pretty_str,STARTUP = False,PDF = pdf)
                            break
                while True:
                        n = m.take_notification()
                        notify=n.notification_xml
                        dict_notify = xmltodict.parse(str(notify))
                        input_dict =  dict_notify
                        output_dict = json.loads(json.dumps(input_dict))  
                        def recursive_items(dictionary):
                            for key, value in dictionary.items():
                                if type(value) is dict:
                                    yield from recursive_items(value)
                                else:
                                    yield (key, value)
                        for key, value in recursive_items(output_dict):
                            NF1 = key
                        if NF1=='sync-state':
                            s = xml.dom.minidom.parseString(notify)
                            

                            xml_pretty_str = s.toprettyxml()

                            STARTUP.STORE_DATA(xml_pretty_str,STARTUP = False,PDF = pdf)
                            break
                pdf.add_page()
                STARTUP.STORE_DATA("Retrieving SYNCE Locked State",STARTUP = True,PDF = pdf)
    
                SYNC = '''<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <sync xmlns="urn:o-ran:sync:1.0">
                </sync>
                </filter>
                '''
                
                data1  = m.get(SYNC).data_xml
                x = xml.dom.minidom.parseString(data1)
                

                xml_pretty_str = x.toprettyxml()
                STARTUP.STORE_DATA(xml_pretty_str,STARTUP = "XML",PDF = pdf)        
                calnexSet("app/generation/synce/esmc/Port1/ssm", "SsmValue", 'QL-DNU')
                STARTUP.STORE_DATA("Changing QL_SSM to DNU",STARTUP = True,PDF = pdf)
                while True:
                    n = m.take_notification()
                    notify=n.notification_xml
                    dict_notify = xmltodict.parse(str(notify))
                    input_dict =  dict_notify
                    output_dict = json.loads(json.dumps(input_dict))  
                    def recursive_items(dictionary):
                        for key, value in dictionary.items():
                            if type(value) is dict:
                                yield from recursive_items(value)
                            else:
                                yield (key, value)
                    for key, value in recursive_items(output_dict):
                        NF1 = key
                    if NF1=='synce-state':
                        s = xml.dom.minidom.parseString(notify)
                        

                        xml_pretty_str = s.toprettyxml()

                        STARTUP.STORE_DATA(xml_pretty_str,STARTUP = False,PDF = pdf)
                        break
        



    
                STARTUP.STORE_DATA('STEP 3 and 4 Expected Result',STARTUP = True,PDF = pdf)
    
                STARTUP.STORE_DATA("\t\t\tRetriving  and PTP ,SyncE and SYNC state ")
    
                SYNC = '''<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <sync xmlns="urn:o-ran:sync:1.0">
                </sync>
                </filter>
                '''
                
                data1  = m.get(SYNC).data_xml
                x = xml.dom.minidom.parseString(data1)
                

                xml_pretty_str = x.toprettyxml()
                STARTUP.STORE_DATA(xml_pretty_str,STARTUP = "XML",PDF = pdf)
    
                time.sleep(20)
            else:
                STARTUP.STORE_DATA('Device Not Detected',STARTUP = True,PDF = pdf)
    except Exception as e:
        STARTUP.STORE_DATA(e,STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)

def Result_Decleration(host, port, user, password):
    try:
        with manager.connect(host=host, port=port, username=user, hostkey_verify=False, password=password) as m:
            STARTUP.STORE_DATA('RESULTS',STARTUP = True,PDF = pdf)
            SYNC = '''
                <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <sync xmlns="urn:o-ran:sync:1.0">
                </sync>
                </filter>
                '''
            
            value_SYNC = m.get(SYNC).data_xml

            
            dict_Sync = xmltodict.parse(str(value_SYNC))
            Sync_state=dict_Sync['data']['sync']['sync-status']['sync-state']

            STARTUP.STORE_DATA(f"{'Sync_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if Sync_state == "LOCKED" else f"\t\tTest Case Fail\nReason : Sync state is {Sync_state}",STARTUP = True,PDF = pdf)
            
            Ptp_lock_state=dict_Sync['data']['sync']['ptp-status']['lock-state']
            STARTUP.STORE_DATA(f"{'Ptp_lock_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if Ptp_lock_state == "LOCKED" else f"\t\tTest Case Fail\nReason : Ptp lock state state is {Ptp_lock_state}",STARTUP = True,PDF = pdf)

            Ptp_state=dict_Sync['data']['sync']['ptp-status']['sources']['state']
            STARTUP.STORE_DATA(f"{'Ptp_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if Ptp_state == "PARENT" else f"\t\t Test Case Fail \nReason : Ptp state state is {Ptp_state}",STARTUP = True,PDF = pdf)

            SyncE_lock_state=dict_Sync['data']['sync']['synce-status']['lock-state']
            STARTUP.STORE_DATA(f"{'SyncE_lock_state STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if SyncE_lock_state == "UNLOCKED" else f"\t\tTest Case Fail\nReason : SyncE lock state is {SyncE_lock_state}",STARTUP = True,PDF = pdf)

            SyncE_state=dict_Sync['data']['sync']['synce-status']['sources']['state']
            STARTUP.STORE_DATA(f"{'SyncE_State STATUS' : <50}{'=' : ^20}{'PASS' : ^20}" if SyncE_state == "NOK" else f"\t\tTest Case Fail\nReason : SyncE state state is {SyncE_state}",STARTUP = True,PDF = pdf)
    except Exception as e:
        STARTUP.STORE_DATA(e,STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)

def CREATE_LOGS(PDF,name):
    name1 = str(path) + "/" +str(name) + ".pdf"
    PDF.output(name1)

if __name__ == '__main__':
    calnexInit("172.17.80.2")
    try:
        STARTUP.STORE_DATA('Provide the credentials for SSH',STARTUP = True,PDF = pdf)
        usr = input("Enter the username: ")
        pss = input("Enter the Password: ")
        m = manager.call_home(host = '', port=4334, hostkey_verify=False,username =usr, password =pss)

        li = m._session._transport.sock.getpeername()
        sid = m.session_id
        kill_ssn(li[0],830,usr,pss,sid)
        
        
        res = session_login(li[0],830,usr,pss)
        STARTUP.STORE_DATA('SYSTEM LOGS',STARTUP = True,PDF = pdf)
        command = "cd /media/sd-mmcblk0p4; cat garuda.log | grep SYNCMNGR;"
        command1 = "cd /media/sd-mmcblk0p4; rm -rf garuda.log;"


        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=li[0],username='root',password='garuda')

        stdin, stdout, stderr = ssh_client.exec_command(command)
        lines = stdout.readlines()
        for i in lines:
            STARTUP.STORE_DATA(i,end="",STARTUP = "XML",PDF = pdf)
        stdin, stdout, stderr = ssh_client.exec_command(command1)
        Result_Decleration(li[0],830,usr,pss)
        path = input('Enter the path to save SI LAB logs  ')
        Remote_path= path + "/TC8.log"
        ssh_ob = SSHClient()
        ssh_ob.load_system_host_keys()
        ssh_ob.connect(hostname=li[0],username=usr,password=pss)
        scp = SCPClient(ssh_ob.get_transport())
        scp.get('/var/log/synctimingptp2.log',Remote_path)
        scp.close()
        CREATE_LOGS(pdf,name = "S_CTC_ID_008")
    except SCPException as e:
        STARTUP.STORE_DATA("File Not found in RU",STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)

    except UnicodeError as e:
        STARTUP.STORE_DATA(e,"Please give correct Ip address",STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)

    except paramiko.ssh_exception.AuthenticationException as e:
        STARTUP.STORE_DATA(e,"Please give correct username or password",STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)

    except socket.timeout as e:
        STARTUP.STORE_DATA(e,"Call Home could not complete",STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)
    
    except Exception as e:
        STARTUP.STORE_DATA(e,STARTUP = True,PDF = pdf)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        STARTUP.STORE_DATA('Error Line Number:',{exc_tb.tb_lineno},STARTUP = True,PDF = pdf)


    calnexSet("app/mse/master/Master1/clockclass", "ClockClass", 6)
    calnexSet("app/mse/applypending")

    calnexSet("app/generation/synce/esmc/Port1/ssm", "SsmValue", 'QL-PRC')
    calnexSet("app/mse/master/Master1/stop")
    calnexSet("app/generation/synce/esmc/Port1/stop")
