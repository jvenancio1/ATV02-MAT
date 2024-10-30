def calcular_bissetriz(a, b, c, tipo):
    """
    Calcula a divisão do lado oposto pela bissetriz interna ou externa.
    
    Parâmetros:
    a, b, c - Lados do triângulo (a e b são os lados adjacentes ao ângulo bissetado)
    tipo - Tipo da bissetriz ("interna" ou "externa")
    
    Retorna:
    A divisão do lado oposto em segmentos d e e.
    """
    try:
        if tipo == "interna":
            # Cálculo da divisão pela bissetriz interna
            d = (a * c) / (a + b)
            e = (b * c) / (a + b)
            print(f"A bissetriz interna divide o lado oposto em segmentos: {d:.2f} e {e:.2f}")
        elif tipo == "externa":
            # Cálculo da divisão pela bissetriz externa
            d = (a * c) / (b - a)
            e = (b * c) / (b - a)
            print(f"A bissetriz externa divide o lado oposto em segmentos: {d:.2f} e {e:.2f}")
        else:
            print("Tipo de bissetriz inválido. Escolha 'interna' ou 'externa'.")
    except ZeroDivisionError:
        print("Erro: a bissetriz externa não intercepta o lado oposto para esses valores.")

# Exemplo de uso
a = float(input("Digite o lado a do triângulo: "))
b = float(input("Digite o lado b do triângulo: "))
c = float(input("Digite o lado c (lado oposto ao ângulo): "))
tipo = input("Digite o tipo de bissetriz ('interna' ou 'externa'): ").lower()

calcular_bissetriz(a, b, c, tipo)
