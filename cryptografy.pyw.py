import hashlib
from tkinter import *

#Opção de cadastro de usuário:
def cadastrar():
    '''Foi colocado uma opção de cadastro caso o usuário não tivesse o login, pois tinha como foco acompanhar
    o comportamento de login e cadastro. Primeiro, ocorre a separação dos caracteres digitados no campo password.
    Após separação, ocorre a criptografia de cada caracter com hash md5 e junta-se todos os hashs de caracteres e
    converte em um hash único, assim salvando no banco de dados ou, como nesse caso, arquivo de texto.'''
    b = ''
    for valor in senha.get():
        resultado = hashlib.md5(valor.encode('utf-8'))
        a = resultado.hexdigest()
        print(f'O Hash de {valor} é {a}')
        b += a

    complet = hashlib.md5(b.encode('utf-8'))
    cripto = complet.hexdigest()
    print(b)
    print(cripto)
    open('save.txt', 'w').write(cripto)
#Opção que verifica se o login e senha estão coerentes, como padrão o login é login.
def constatar():
    b = ''
    for valor in senha.get():
        resultado = hashlib.md5(valor.encode('utf-8'))
        a = resultado.hexdigest()
        print(f'O Hash de {valor} é {a}')
        b += a

    complet = hashlib.md5(b.encode('utf-8'))
    cripto = complet.hexdigest()
    print(b)
    print(cripto)

    comparar = open('save.txt', 'r').read()

    if login.get() == 'login' and comparar == cripto:
        print('\033[32mPassword is True')

        root.destroy()
        novatela = Tk()
        novatela.config(background='blue')
        novatela.mainloop()

    else:
        print("\033[34mError! Password isn't True")

root = Tk()
senha = StringVar()
login = StringVar()
root.title('teste_de_cryptografia')
root.config(bd=30, background='lightblue')


label = Label(root, text='Login: ')
label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
label.config(background = 'lightblue')


login = Entry(root,)
login.grid(row=0,column=1, padx=5, pady=5)
login.config(justify='right',state='normal')

label2 = Label(root, text='Password: ')
label2.grid(row=1, column=0, sticky='e', padx=5, pady=5)
label2.config(background='lightblue')

senha = Entry(root,)
senha.grid(row=1, column=1, sticky='e', padx=5, pady=5)
senha.config(justify='right', state='normal', show='*')

button = Button(root, text='Entrar', command=constatar)
button.grid(row=2,column=1)
cadbutton = Button(root, text='Cadastrar', command=cadastrar)
cadbutton.grid(row=3,column=1)
root.mainloop()