import smtplib
from email.message import EmailMessage as em
import os
import imghdr
import recipients_list
import imghdr


"""
Add your gmail id and your password in your enviroment variable and give the variable name below in place of 'sendermail' and 'apppass'.
N.B. If your gmail account is protected by 2 step verification then create an app password and add that app password to the env varibale and replace
'apppass' with that password.

"""
sendermail= os.environ['sendermail']
senderpass = os.environ['apppass']


def fun_send_email():
    msg = em()
    msg['subject'] = "Editable Text"
    msg['from'] = sendermail
    msg['to'] = recipients_list.to_email                #Edit the recipients_list.py to_email list to send to all the recipients
    htmlfile= open('msg_format.html').read()            #Edit the msg_format.html file for desired format of the message
    msg.add_alternative(htmlfile, subtype= 'html')      

    #Add the attachment names in attachment_files in recipients_list.py and keep the attachments in the same directory

    for i in recipients_list.attachment_files:
        with open(i , 'rb') as afiles:
            afname=afiles.name
            aftype = imghdr.what(afname)
            afread= afiles.read()
        msg.add_attachment(afread, maintype = 'image', subtype = aftype, filename = afname) 
        #for attaching pdf just edit maintype parameter with "application" and subtype as "octet-stream"


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sendermail, senderpass)
        smtp.send_message(msg)


fun_send_email()

