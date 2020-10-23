import os

def main():
    LINGUAGENS = os.environ.get('LANG')

    print("Olá Mundo")
    print("As linguagens que estão sendo procuradas são:", LINGUAGENS)

    return LINGUAGENS

if __name__ == '__main__':
    main()