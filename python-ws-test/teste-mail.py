import os
import time
import smtplib
from email.message import EmailMessage

ENDERECO_EMAIL = os.environ.get('USR_MAIL')
SENHA_EMAIL = os.environ.get('PAS_MAIL')

print('Iniciando teste de email básico a partir do Jenkins')
print('Sleep para suspense')
time.sleep(3.5)

msg = EmailMessage()
msg['Subject'] = 'Email com variáveis de ambiente ocultas'
msg['From'] = ENDERECO_EMAIL
msg['To'] = 'pedrleonardi@gmail.com'
msg.set_content('Este email foi enviado com variáveis de ambiente ocultas e fornecidas pelo próprio jenkins\n' +
'Se conseguirmos ver essa mensagem, o teste foi um sucesso :)')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(ENDERECO_EMAIL, SENHA_EMAIL)
    smtp.send_message(msg)

print('Email enviado com sucesso')
