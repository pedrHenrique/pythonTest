import os

def main():
    LINGUAGENS = os.environ.get('LANG')
    CONTATOS = [os.environ.get('CONTACTS')]

    print("Olá Mundo")
    print("As linguagens que estão sendo procuradas são:", LINGUAGENS)
    print("Os contatos quais a mensagem será enviada são: ", CONTATOS)
    print(type(CONTATOS))

    return LINGUAGENS

if __name__ == '__main__':
    main()