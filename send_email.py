import smtplib
from email.message import EmailMessage as em
import os
import imghdr
import recipients_list
import imghdr

sendermail= os.environ['sendermail']
senderpass = os.environ['apppass']


def fun_send_email():
    msg = em()
    msg['subject'] = "Editable Text"
    msg['from'] = sendermail
    msg['to'] = recipients_list.sender_email
    htmlfile= open('msg_format.html').read()
    msg.add_alternative(htmlfile, subtype= 'html')


    for i in recipients_list.attachment_files:
        with open(i , 'rb') as afiles:
            afname=afiles.name
            aftype = imghdr.what(afname)
            afread= afiles.read()
        msg.add_attachment(afread, maintype = 'image', subtype = aftype, filename = afname) #for attaching pdf just edit maintype parameter with "application" and subtype as "octet-stream"


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sendermail, senderpass)
        smtp.send_message(msg)


fun_send_email()

