def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média de três notas.

    Args:
        nota1 (float|int): A primeira nota.
        nota2 (float|int): A segunda nota.
        nota3 (float|int): A terceira nota.

    Returns:
        float: A média das notas.

    Raises:
        ValueError: Se as notas não forem números ou se não houver exatamente três notas.
    """
    # Verifica se todas as notas são números
    if not all(isinstance(nota, (int, float)) for nota in [nota1, nota2, nota3]):
        raise ValueError("Todas as notas devem ser números inteiros ou decimais")

    # Calcula e retorna a média
    return (nota1 + nota2 + nota3) / 3
