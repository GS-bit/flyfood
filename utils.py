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
	"""
	Obtém o menor percurso que o drone deve realizar para entregar as comidas.

	Parâmetros:
		mundo: uma lista de tuplas que representam pontos e que seguem o formato (nome, x, y), 
		em que nome indica o rótulo do ponto, seja ele de retorno (R) ou de entrega (A, B, C, D, E, F... menos o R), 
		x é o valor inteiro da coordenada horizontal do ponto e y o da coordenada vertical.

	Retorno:
		Uma string (por exemplo, "A D C B") que indica a sequência de pontos a ser percorrida pelo drone.

		E, em caso de erro na execução da função, uma string vazia.
	"""

	pass
