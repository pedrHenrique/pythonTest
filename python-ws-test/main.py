import test
import test_mail

if __name__ == '__main__':
    mensagem = test.main()
    test_mail.envia_email(mensagem)