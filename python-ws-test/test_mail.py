import os
import time
import smtplib
from email.message import EmailMessage

ENDERECO_EMAIL = os.environ.get('USR_MAIL')
SENHA_EMAIL = os.environ.get('PAS_MAIL')

def envia_email(mensagem):

    print('Iniciando teste de email básico a partir do Jenkins')
    print('Sleep para suspense')
    time.sleep(3.5)

    msg = EmailMessage()
    msg['Subject'] = 'Email com variáveis de ambiente ocultas'
    msg['From'] = ENDERECO_EMAIL
    msg['To'] = ENDERECO_EMAIL
    msg.set_content('Este email foi enviado com variáveis de ambiente ocultas e fornecidas pelo próprio jenkins\n' +
    'Se conseguirmos ver as linguagens que estão sendo informadas aqui abaixo.\n\n', mensagem, '\n\nEntão o teste foi um sucesso :)')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ENDERECO_EMAIL, SENHA_EMAIL)
        smtp.send_message(msg)

    print('Email enviado com sucesso')

if __name__ == '__main__':
    envia_email('mensagem genêrica de teste')