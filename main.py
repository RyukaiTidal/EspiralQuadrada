def imprimirAnimacao(n,x,y):
    if n == 0:
        pass
    else:
        for l in range(1, n + 1):
            for c in range(1, n + 1):
                if l == y and c == x:
                    print("X", end="")
                else:
                    print("O", end="")
            print("", end="\n")
        print("@")

#Função pra definir linhas e colunas NxN
n = int(input())
#Y = Linha Inicial, X = Coluna Inicial
x = round((n/2)+0.1)

if n % 2 == 0:
    y = round((n/2)+0.1)+1
else:
    y = round((n/2)+0.1)

#1 = Direita, 2 = Cima, 3 = Esquerda, 4 = Baixo
rotation = 1


imprimirAnimacao(n,x,y)
xatual = x
yatual = y
exp = 1
mr = exp
for move in range(n*n,1,-1):
    match rotation:
        case 1:
            xatual += 1
        case 2:
            yatual -= 1
        case 3:
            xatual -= 1
        case 4:
            yatual +=1
    imprimirAnimacao(n, xatual, yatual)
    mr -= 1
    if mr == 0:
        mr = exp
        rotation += 1
        if rotation == 5:
            rotation = 1
        if rotation == 2 or rotation == 4:
            exp += 1