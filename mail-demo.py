from fileinput import filename
import os 
import smtplib
import pdfkit
from pdfkit.api import configuration


from email.message import EmailMessage

EMAIL_ADDRESS = "fashinaoluwaseun36@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Hello from MailBot'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'contact.seunfashina@gmail.com'
msg.set_content('Testing Pdf')


files = ['form_mail.html']
wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  #by using configuration you can add path value.


pdfkit.from_file(files, 'output.pdf', configuration = wkhtml_path)  
result = ['output.pdf']
for file in result:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name


msg.add_attachment(file_data, maintype='application', subtype='octet-stream' ,filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
