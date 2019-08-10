import time
a=['3-MAIOR','2-MEDIO','1-MENOR']
b=[]
c=[]
move = []
def info():
    print('-------------------------------------------------------------')
    print(' II  II     III     III     II IIIIIIIII IIIIIIII')
    print(' II  II    II II    II II   II II     II    II')
    print(' IIIIII   II   II   II  II  II II     II    II')
    print(' II  II  IIIIIIIII  II   II II II     II    II')
    print(' II  II II       II II     III IIIIIIIII IIIIIIII\n-------------------------------------------------------------')
    print(' Este é um jogo Torre de Hanói em Python. É composto por\n três pinos e três discos. O objetivo é mover os três\n discos do pino esquerdo para o direito, ou no terminal,\n de cima (pino 1) para baixo (pino 3) em ordem de tamanho,\n ou seja, não pode colocar um disco maior em cima de um menor.                                     * BOM JOGO! *')
def jogando():
    print('--------------------------------------------------------')
    print(' Pino 1 =',' | '.join(map(str, a)))
    print(' Pino 2 =',' | '.join(map(str, b)))
    print(' Pino 3 =',' | '.join(map(str, c)))
    print('\n Abortar =','(9)')
    print('--------------------------------------------------------')
def base():
    mov = 0
    while True:
        ganhar()
        jogando()
        x = int(input(' Mover de Pino: '))
        if x == 1 and len(a) != 0:
            y = int(input(' Para Pino: '))
            if y == 2:
                s = a.pop()
                if len(b) == 0 or b[0] > s:
                    b.append(s)
                    mov += 1
                else:
                    a.append(s)
            elif y == 3:
                s = a.pop()
                if len(c) == 0 or c[0] > s:
                    c.append(s)
                    mov += 1
                else:
                    a.append(s)
            else:
                print('--------------------------------------------------------')
                print('Pino inexistente, tente novamente!')
                time.sleep(2)
        elif x == 2 and len(b) != 0:
            y = int(input(' Para Pino: '))
            if y == 1:
                s = b.pop()
                if len(a) == 0 or a[0] > s:
                    a.append(s)
                    mov += 1
                else:
                    b.append(s)
            elif y == 3:
                s = b.pop()
                if len(c) == 0 or c[0] > s:
                    c.append(s)
                    mov += 1
                else:
                    b.append(s)
            else:
                print('--------------------------------------------------------')
                print('Pino inexistente, tente novamente!')
                time.sleep(2)
        elif x == 3 and len(c) != 0:
            y = int(input(' Para Pino: '))
            if y == 1:
                s = c.pop()
                if len(a) == 0 or a[0] > s:
                    a.append(s)
                    mov += 1
                else:
                    c.append(s)
            elif y == 2:
                s = c.pop()
                if len(b) == 0 or b[0] > s:
                    b.append(s)
                    mov += 1
                else:
                    c.append(s)
            else:
                print('--------------------------------------------------------')
                print('Pino inexistente, tente novamente!')
                time.sleep(2)
        elif x == 9:
            JOGO()
        else:
            print('--------------------------------------------------------')
            print('Pino vazio ou inexistente, tente novamente!')
            time.sleep(2)
        move.append(mov)
def ganhar():
    if len(c) == 3:
        if move[-1] == 7:
            print('--------------------------------------------------------')            
            print('--------------------------------------------------------')
            print('             VOCÊ GANHOU PERFEITAMENTE!!!')
            print(' Movimentos mínimos: 7       Numero de movimentos:',move[-1])
            print('--------------------------------------------------------')
            while True:
                p = str(input('Jogar novamente?(S/N): '))
                if p.lower() == 's':
                    reset()
                    JOGO()
                elif p.lower() == 'n':
                    exit()
                else:
                    print('Opção inválida, tente novamente!')     
        else:
            print('--------------------------------------------------------')
            print('--------------------------------------------------------')
            print('              VOCÊ GANHOU MAS DEMOROU!!!')
            print(' Movimentos mínimos: 7       Numero de movimentos:',move[-1])
            print('--------------------------------------------------------')
            while True:
                p = str(input('Jogar novamente?(S/N): '))
                if p.lower() == 's':
                    reset()
                    JOGO()
                elif p.lower() == 'n':
                    exit()
                else:
                    print('Opção inválida, tente novamente!')
def reset():
    a.clear(); a.append('3-MAIOR'); a.append('2-MEDIO'); a.append('1-MENOR')
    b.clear()
    c.clear()
    move.clear()
def menu():
    print('--------------------------------------------------------------')
    print(' Jogar ou continuar --- (1)                          ')
    print(' Resetar pinos      --- (2)')
    print(' Sair do jogo       --- (9)                          ')
    print('--------------------------------------------------------')
    h = int(input(' O que deseja fazer: '))
    if h == 1:
        base()
    elif h == 2:
        reset()
        JOGO()
    elif h == 9:
        exit()
    else:
        print('--------------------------------------------------------')
        print(' Opção inválida')
        time.sleep(2)
        JOGO()
def JOGO():
    info()
    menu()
JOGO()
