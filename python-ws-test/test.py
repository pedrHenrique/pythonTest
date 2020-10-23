import os

def main():
    LINGUAGENS = os.environ.get('LANG')
    CONTATOS = os.environ.get('CONTACTS').split(',')

    print("Olá Mundo")
    print("As linguagens que estão sendo procuradas são:", LINGUAGENS)
    print("Os contatos quais a mensagem será enviada são: ")
    #print(type(CONTATOS))
    print(len(CONTATOS))
    
    for c in CONTATOS:
        print("Contato:", c)
    
    if len(CONTATOS) <= 1:
        print('A lista não foi construída do jeito que devia')
        exit(1)
    else:
        print('A lista foi construída do jeito que deveria :D')
        exit(0)
    return LINGUAGENS

if __name__ == '__main__':
    main()