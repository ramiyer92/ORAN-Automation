# ORAN-Automation
The repository is been build for  M &amp; S Plane optimisation in the Fronthual Interface

**Introduction**

The complete Automation is built using ncclient is a Python library for supporting NETCONF protocol. It aims to offer an intuitive API that sensibly maps the XML-encoded nature of NETCONF. 
It will help to run the O-RAN WG4 M Plane and S Plane Conformance Test Cases. Below are the requirements before executing the test case. This will run only Linux Base Environment.

**Requirements**
- Python >=3.7
- setuptools 0.6+
- libxml2
- Libxslt
- ncclient >=0.6.12
- fpdf>=1.7.2
- fpdf2>=2.5.5
- lxml==4.8.0
- ifcfg>=0.22
- maskpass>=0.3.6
- paramiko>=2.11.0
- pytest>=7.0.1
- requests>=2.27.1
- tabulate>=0.8.10
- xmltodict>=0.13.0
    
**Installation**

  pip install -r requirements.txt




**# Setup Diagram:**

**Flow Chart:**


M-Plane

S-Plane





**Usage**
- Go to the test cases directory and run the following:
- Edit the Config.py file according to requirements of RU configuration.
- Config.py contains 

details = 

{ 
 'SUPER_USER': 'Enter Super User',
 
 'SUPER_USER_PASS' : 'Enter Super User Password',
 
 'SUDO_USER' : 'Enter Sudo User',
 
 'SUDO_PASS' : 'Enter Sudo User Password',
 
 'NMS_USER' : 'Enter NMS User',
 
 'NMS_PASS' : 'Enter NMS User Password',
 
 'FM_PM_USER' : 'Enter FM-PM User',
 
 'FM_PM_PASS' : 'Enter FM-PM User Password',
 
 'IPADDR_PARAGON' : 'Enter Paragon Neo IP',
 
 'PORT' : 'Enter Paragon Neo Port To enable PTP/SYNCE',
 
 'DU_PASS' : 'Enter DU Password',
 
 'DU_MAC' : 'Enter DU MAC',
 
 'remote_path' : 'sftp://whoami@IP_address:22/path/to/the/software/file',
 
 'Corrupt_File': 'sftp://whoami@IP_address:22/path/to/the/software/currupt/file',
 
 'SYSLOG_PATH' : 'System log path of RU',
 
 'syslog_name' : 'System log name',
 
 'uplane_xml'  : 'path/userplane/xml/file',
 
 'TC_27_xml'  : 'path/to/the/uaerplane/xml/with/same/eaxcid/file'
 
}


- python M_CTC_ID_{Test Case ID}.py

**Note: In the linux env all the required libraries should be installed.**







