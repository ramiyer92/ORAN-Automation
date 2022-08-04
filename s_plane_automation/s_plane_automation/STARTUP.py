from os import name, path
from fpdf import FPDF
from requests import head

def STORE_DATA(*datas,Format,PDF):
     for data in datas:
        # OUTPUT_LIST.append(*data)
        # print(''.join([*data])
          if Format == True:
               print('='*100)
               print(data)
               print('='*100)
               HEADING(PDF,data)

          elif Format == 'XML':
               print(data)
               XML_FORMAT(PDF,data)

          elif Format == 'CONF':
               print('='*100)
               print(data)
               print('='*100)
               CONFDENTIAL(PDF,data)
          
          elif Format == 'DESC':
               print('='*100)
               print(data)
               print('='*100)
               Test_desc(PDF,data)
          
          elif Format == 'TEST_STEP':
               print('='*100)
               print(data)
               print('='*100)
               Test_Step(PDF,data)
          
          # elif Format == False:
          #      # print('='*100)
          #      print(data)
          #      # print('='*100)
          #      Test_Step(PDF,data)

          else:
               print(data)
               PDF.write(h=5,txt=data)
               PDF.ln()

def CREATE_LOGS(PDF):
    # STORE_DATA(OUTPUT_LIST,OUTPUT_LIST)
    PDF.output(f"{path}.pdf")
    PDF.output(f"{path+name}.pdf")



def ADD_CONFIDENTIAL(TC,SW_R):

    CONF = '''**    
     {2}
     * @file    M_CTC_ID_0{0}_.txt                                                           
     * @brief    M PLANE O-RAN  Conformance
     * @credits Created based on Software Release for GIRU_revC-- v{1}                          
     {2}'''.format(TC,SW_R,'*'*70)
    return CONF


def Test_desc(PDF,data):
     PDF.set_font("Times",style = 'B', size=13)
     PDF.set_text_color(17, 64, 37)
     PDF.write(5, '\n{}\n'.format('='*71))
     PDF.multi_cell(w =180,h = 10,txt='Test Description : {}'.format(data),border=1,align='L')
     PDF.write(5, '\n{}\n'.format('='*71))
     PDF.set_font("Times",style = '',size = 9)
     PDF.set_text_color(0, 0, 0)
     # PDF.ln(80)
     pass



def STATUS(host,user,session_id,port):
    STATUS = f'''> connect --ssh --host {host} --port 830 --login {user}
                        Interactive SSH Authentication
                        Type your password:
                        Password: 
                        > status
                        Current NETCONF session:
                        ID          : {session_id}
                        Host        : {host}
                        Port        : {port}
                        Transport   : SSH
                        Capabilities:
                        '''
    return STATUS



def PDF_CAP():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=9)
    y = int(pdf.epw)
    pdf.image(name='Front_Page.png', x = None, y = None, w = y, h = 0, type = '', link = '')
    pdf.ln(10)
    return pdf


def HEADING(PDF,data,*args):
    PDF.set_font("Times",style = 'B', size=9)
    PDF.write(5, '\n{}\n'.format('='*75))
    PDF.write(5,data)
    PDF.write(5, '\n{}\n'.format('='*75))
    PDF.set_font("Times",style = '',size = 9)



def XML_FORMAT(PDF,data):
    PDF.set_text_color(199, 48, 83)
    PDF.write(5,data)
    PDF.set_text_color(0, 0, 0)

def CONFDENTIAL(PDF,data):
     PDF.set_font("Times",style = 'B', size=15)
     PDF.set_text_color(10, 32, 71)
     PDF.write(5, '\n{}\n'.format('='*62))
     PDF.multi_cell(w =180,txt=data,border=1,align='L',h = 5)
     PDF.write(5, '\n{}\n'.format('='*62))
     PDF.set_font("Times",style = '',size = 9)
     PDF.set_text_color(0, 0, 0)
     PDF.ln(30)
     pass

def Test_Step(PDF,data):
    PDF.set_font("Times",style = 'B', size=11)
    PDF.set_text_color(125, 93, 65)
    PDF.write(5, '\n{}\n'.format('='*80))
    PDF.write(5,data)
    PDF.write(5, '\n{}\n'.format('='*80))
    PDF.set_font("Times",style = '',size = 9)
    PDF.set_text_color(0,0,0)

# pdf = PDF_CAP()
# CONF = ADD_CONFIDENTIAL('10',SW_R='4.0.9')
# STORE_DATA(CONF,Heading='CONF',PDF=pdf)
# Test_Desc = 'This scenario validates that the O-RU NETCONF Server properly executes a get command with a filter applied.'
# STORE_DATA(Test_Desc,Heading='DESC',PDF=pdf)
# pdf.set_auto_page_break(auto=True,margin=20)
# STORE_DATA('\t\t********** Connect to the NETCONF Server ***********','This scenario validates that the O-RU NETCONF Server',Heading='TEST_STEP',PDF=pdf)
# STATUSS = STATUS('192.168.4.59','operator','3',830)
# STORE_DATA(STATUSS,Heading=False,PDF=pdf)
# STORE_DATA('\t\t***********step 1 and 2 Retrival of ru information with filter **********',Heading='TEST_STEP',PDF=pdf)
# STORE_DATA("get --filter-xpath /o-ran-usermgmt:users/user",Heading=True,PDF=pdf)
# u_name = '''
#           <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
#           <users xmlns="urn:o-ran:user-mgmt:1.0">	
#                <user>                                                                                    
#                </user>
#           </users>
#           </filter>
#                 '''
# STORE_DATA(u_name,Heading='XML',PDF=pdf)
# STORE_DATA('\t\t***********step 1 and 2 Retrival of ru information with filter **********',Heading=True,PDF=pdf)
# CREATE_LOGS(pdf)


















