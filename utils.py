from intertools import permutations

def ler_mundo(arquivo: str) -> list:
	"""
	Lê um arquivo contendo as coordenadas dos pontos de entrega de comida e do ponto de retorno do drone.

	O conteúdo do arquivo segue este formato matricial:

	i j
	a11 a12 ... a1j
	a21 a22 ... a2j
	... ... ... ...
	ai1 ai2 ... aij

	i e j são, respectivamente, os números de linhas e colunas da matriz;
	axy, em que 1 <= x <= i e 1 <= y <= j, deve assumir um dos seguintes valores:
		- 0, que é um ponto padrão
		- R, que é o ponto de retorno do drone
		- A, B, C, D, E, F... (menos o R), que são os pontos de entrega

	Parâmetros:
		arquivo: caminho do arquivo no computador.

	Retorno:
		Uma lista de tuplas que representam pontos e que seguem o formato (nome, x, y), 
		em que nome indica o rótulo do ponto, seja ele de retorno (R) ou de entrega (A, B, C, D, E, F... menos o R), 
		x é o valor inteiro da coordenada horizontal do ponto e y o da coordenada vertical.

		E, em caso de erro na leitura do arquivo, uma lista vazia.
	"""

	pass

def obter_percurso(mundo: list) -> str:
    try:
        origem = None
        entregas = []

        for ponto in mundo:
            nome, x, y = ponto

            if nome == "R":
                origem = ponto
            else:
                entregas.append(ponto)

        if origem is None:
            return ""

        if len(entregas) == 0:
            return ""

        menor_distancia = float("inf")
        melhor_percurso = None

        for percurso in permutations(entregas):

            distancia_total = 0
            ponto_atual = origem

            for ponto in percurso:
                distancia_total += (
                    abs(ponto_atual[1] - ponto[1])
                    + abs(ponto_atual[2] - ponto[2])
                )

                ponto_atual = ponto

            distancia_total += (
                abs(ponto_atual[1] - origem[1])
                + abs(ponto_atual[2] - origem[2])
            )

            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                melhor_percurso = percurso

        return " ".join(ponto[0] for ponto in melhor_percurso)

    except Exception:
        return ""