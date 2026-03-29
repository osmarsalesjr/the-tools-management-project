
from operacoes.validacoes_pecas import (
    STATUS_APROVADO,
    STATUS_REPROVADO,
    MOTIVO_REPROVADO_POR_PESO,
    MOTIVO_REPROVADO_POR_COR,
    MOTIVO_REPROVADO_POR_COMPRIMENTO,
)

lista_de_pecas = [
    # ======================
    # 43 APROVADAS
    # ======================
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "VERDE", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor": "AZUL", "comprimento": 12, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor": "VERDE", "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 95, "cor": "AZUL", "comprimento": 10, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 105, "cor": "VERDE", "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor": "AZUL", "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor": "VERDE", "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor": "VERDE", "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 103, "cor": "AZUL", "comprimento": 19, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 96, "cor": "VERDE", "comprimento": 11, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 104, "cor": "VERDE", "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 95, "cor": "AZUL", "comprimento": 12, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 105, "cor": "VERDE", "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor": "AZUL", "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor": "VERDE", "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor": "VERDE", "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor": "AZUL", "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor": "VERDE", "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 103, "cor": "VERDE", "comprimento": 19, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 96, "cor": "AZUL", "comprimento": 11, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 104, "cor": "VERDE", "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor": "AZUL", "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor": "VERDE", "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor": "VERDE", "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor": "AZUL", "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor": "VERDE", "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 103, "cor": "VERDE", "comprimento": 19, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 96, "cor": "AZUL", "comprimento": 11, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 104, "cor": "VERDE", "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor": "AZUL", "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor": "VERDE", "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor": "VERDE", "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor": "AZUL", "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor": "VERDE", "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor": "AZUL", "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    # ======================
    # 35 REPROVADAS
    # ======================
    # Peso inválido
    {"peso": 80, "cor": "AZUL", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 80, "cor": "VERDE", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 110, "cor": "AZUL", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 110, "cor": "VERDE", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 70, "cor": "AZUL", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 70, "cor": "VERDE", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 120, "cor": "AZUL", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 120, "cor": "VERDE", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 90, "cor": "AZUL", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 90, "cor": "VERDE", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    # Cor inválida
    {"peso": 100, "cor": "VERMELHO", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "PRETO", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "BRANCO", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "AMARELO", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "ROXO", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "LARANJA", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "ROSA", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "CINZA", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "MARROM", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor": "ROXO", "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    # Comprimento inválido
    {"peso": 100, "cor": "AZUL", "comprimento": 5, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "VERDE", "comprimento": 5, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "AZUL", "comprimento": 25, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "VERDE", "comprimento": 25, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "AZUL", "comprimento": 30, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "VERDE", "comprimento": 30, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "AZUL", "comprimento": 2, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "VERDE", "comprimento": 2, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "AZUL", "comprimento": 50, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor": "VERDE", "comprimento": 50, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    # Múltiplos erros
    {"peso": 50, "cor": "ROXO", "comprimento": 30, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO, MOTIVO_REPROVADO_POR_COR, MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 120, "cor": "PRETO", "comprimento": 5, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO, MOTIVO_REPROVADO_POR_COR, MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 80, "cor": "BRANCO", "comprimento": 25, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO, MOTIVO_REPROVADO_POR_COR, MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 130, "cor": "AMARELO", "comprimento": 1, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO, MOTIVO_REPROVADO_POR_COR, MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 60, "cor": "ROSA", "comprimento": 40, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO, MOTIVO_REPROVADO_POR_COR, MOTIVO_REPROVADO_POR_COMPRIMENTO]},
]

def main() -> None:
    pass


def pegar_lista_pecas() -> list[dict]:
    global lista_de_pecas

    return lista_de_pecas


if __name__ == "__main__":
    main()
