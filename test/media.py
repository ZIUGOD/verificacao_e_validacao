def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média de três notas.

    Parâmetros:
    nota1 (int ou float): A primeira nota.
    nota2 (int ou float): A segunda nota.
    nota3 (int ou float): A terceira nota.

    Retorna:
    float: A média das três notas.

    Levanta:
    ValueError: Se alguma das notas não for um número ou se as notas estiverem fora do intervalo [-1e6, 1e6].
    """

    # Verifica se todas as notas são números (int ou float)
    if not all(isinstance(n, (int, float)) for n in [nota1, nota2, nota3]):
        raise ValueError("Todas as notas devem ser números inteiros ou decimais.")

    # Verifica se as notas estão dentro do intervalo válido [-1e6, 1e6]
    for nota in [nota1, nota2, nota3]:
        if nota < -1e6 or nota > 1e6:
            raise ValueError(
                f"Nota {nota} está fora do intervalo válido. As notas devem estar entre -1e6 e 1e6."
            )

    # Calcula a média
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media
