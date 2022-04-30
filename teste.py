# 1) Linha desenhada da esquerda pra direita
# 2) x1 < x2 e y1 < y2
# 3) inclinação entre 0 e 1.


# gera a linha

def bresenham(x1, y1, x2, y2):

	novo_ponto = 2 * (y2 - y1)
	erro_inclinacao = novo_ponto - (x2 - x1)

	y = y1
	for x in range(x1, x2+1):

		print("(", x, ",", y, ")\n")

		# adiciona inclinação para aumentar o angulo
		erro_inclinacao = erro_inclinacao + novo_ponto

		# O erro de inclinação atingiu o limite
        # incrementa y e atualiza o erro de inclinação.
		if (erro_inclinacao >= 0):
			y = y+1
			erro_inclinacao = erro_inclinacao - 2 * (x2 - x1)


# main
def main():
    x0 = int(input("Entre com o posição inicial de x: "))
    y0 = int(input("Entre com o posição incial de y: "))
    x1 = int(input("Entre com o posição final de x: "))
    y1 = int(input("Entre com o posição final de y: "))
    bresenham(x0,y0,x1,y1)

if __name__=='__main__':
    main()