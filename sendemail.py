#SMTP simple Message Transfer Protocol
import smtplib
## getpass use to gett password from user
import getpass
##MIMEtext sharing information between two party
from email.mime.text import MIMEText

def send_email():
    senders_address='ssshanker2001@gmail.com'
    password=getpass.getpass()
    subject='''IMPORTANT!!'''
    msg='''
       Learn Inspire Grow
    '''
    
    #server initalisation
    server=smtplib.SMTP('smtp.gmail.com',587)
    ##tls is a kind of handhake which will allow the connection
    server.starttls()
    server.login(senders_address,password)
    
    ##draft my message body
    mag=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=senders_address
    msg['To']='ssshanker2001@gmail.com'
    msg.set_param('importance','high value')
    recipients='ssshanker2001@gmail.com'
    
    server.sendmail(senders_address, recipients,msg.as_string())

send_email()