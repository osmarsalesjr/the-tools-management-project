
import sqlite3
import json

from flask import g
from sqlite3 import Connection

from operacoes.massa_dados_testes import pegar_lista_pecas


STATUS_APROVADO = "APROVADO"

SCRIPT = """
CREATE TABLE IF NOT EXISTS caixa (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    esta_fechada INTEGER NOT NULL DEFAULT 0 CHECK (esta_fechada IN (0, 1))
);

CREATE TABLE IF NOT EXISTS peca (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    caixa_id            INTEGER,
    peso                INTEGER NOT NULL,
    cor                 TEXT NOT NULL,
    comprimento         INTEGER NOT NULL,
    status              TEXT NOT NULL DEFAULT 'REPROVADO' CHECK (status IN ('APROVADO', 'REPROVADO')),
    motivos_reprovacao  TEXT DEFAULT '[]',

    FOREIGN KEY (caixa_id) REFERENCES caixa(id)
);
"""
cursor = None
con = None


def main() -> None:
    pass


def conectar_banco_de_dados() -> None:
    global con
    
    try:
        if "db" not in g:
            g.db = sqlite3.connect("bd.db")
            g.db.row_factory = sqlite3.Row
            con = g.db

            ### Cria tabelas
            criar_banco_de_dados()
    except sqlite3.DatabaseError as e:
        print(f"Erro ao conectar o banco de dados: {e}")
        raise e


def desconectar_banco_de_dados() -> None:
    global con
    
    try:
        con = g.pop('db', None)
        if con is not None:
            con.close()
    except sqlite3.DatabaseError as e:
        con.close()
        print(f"Erro ao desconectar o banco de dados: {e}")
        raise e


def criar_banco_de_dados() -> None:
    global cursor, con

    try:

        cursor = con.cursor()
        cursor.executescript(SCRIPT)

        popular_banco_de_dados_com_massa_de_testes()

    except sqlite3.DatabaseError as e:

        print(f"Erro ao criar as tabelas: {e}")
        con.rollback()
        raise


def salvar_peca(peca: dict) -> dict:
    global con, cursor
    
    peso = peca["peso"]
    cor = peca["cor"]
    comprimento = peca["comprimento"]
    status = peca["status"]
    motivos_reprovacao = json.dumps(peca["motivos_reprovacao"])
    caixa_id = peca.get("caixa_id")

    try:
        cursor.execute("""
            INSERT INTO peca (caixa_id, peso, cor, comprimento, status, motivos_reprovacao)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (caixa_id, peso, cor, comprimento, status, motivos_reprovacao))

        con.commit()
        peca["id"] = cursor.lastrowid

        if caixa_id is not None:
            verificar_status_caixa(caixa_id)
        
        return peca

    except sqlite3.DatabaseError as e:
        print(f"Erro ao salvar peça: {e}")
        con.rollback()
        raise


def verificar_status_caixa(caixa_id: int) -> None:

    try:
        quantidade_pecas = contar_pecas_por_caixa(caixa_id)

        if quantidade_pecas >= 10:
            atualizar_caixa(caixa_id, int(True))
            print(f"Caixa {caixa_id} atualizada para fechada.")

    except Exception as e:
        print(f"Erro ao verificar status da caixa ID {caixa_id}: {e}")
        raise


def contar_pecas_por_caixa(caixa_id: int) -> int:
    global cursor

    try:
        cursor.execute("""
            SELECT COUNT(*) FROM peca WHERE caixa_id = ?
        """, (caixa_id,))

        return cursor.fetchone()[0]

    except sqlite3.DatabaseError as e:
        print(f"Erro ao contar peças da caixa {caixa_id}: {e}")
        raise


def atualizar_caixa(caixa_id: int, status: int) -> None:
    global cursor, con

    try:
        cursor.execute("""
            UPDATE caixa SET esta_fechada = ? WHERE id = ?
        """, (status, caixa_id,))

        con.commit()

    except sqlite3.DatabaseError as e:
        print(f"Erro ao atualizar status caixa: {e}")
        con.rollback()
        raise


def remover_peca(peca: dict) -> None:
    global cursor, con

    try:
        cursor.execute("""
            DELETE FROM peca WHERE id = ?
        """, (peca["id"],))

        con.commit()
        print("Peça foi removida com sucesso.")

        caixa_id = peca.get("caixa_id")

        if caixa_id is None:
            return
        
        caixa = recuperar_caixa_por_id(caixa_id)

        if (caixa is not None and caixa["esta_fechada"]):
            atualizar_caixa(caixa_id, int(False))
            print(f"Caixa ID {caixa_id} foi atualizada para ABERTA.")
            

    except sqlite3.DatabaseError as e:
        print(f"Erro ao atualizar status caixa: {e}")
        con.rollback()
        raise


def recuperar_pecas_por_caixa_id(caixa_id: int) -> int:
    global cursor

    try:
        cursor.execute("""
            SELECT * FROM peca WHERE caixa_id = ?
        """, (caixa_id,))
        rows = cursor.fetchall()

        return [
            {
                "id": row["id"],
                "caixa_id": row["caixa_id"],
                "peso": row["peso"],
                "cor": row["cor"],
                "comprimento": row["comprimento"],
                "status": row["status"],
                "motivos_reprovacao": json.loads(row["motivos_reprovacao"])
            }
            for row in rows
        ]

    except sqlite3.DatabaseError as e:
        print(f"Erro ao contar peças da caixa {caixa_id}: {e}")
        raise


def recuperar_caixas() -> list[dict]:
    global cursor

    try:
        cursor.execute("SELECT * FROM caixa")
        rows = cursor.fetchall()

        return [
            {
                "id": row["id"],
                "esta_fechada": bool(row["esta_fechada"])
            }
            for row in rows
        ]

    except sqlite3.DatabaseError as e:
        print(f"Erro ao buscar caixas: {e}")
        raise


def recuperar_caixas_com_pecas() -> list[dict]:
    global cursor

    try:
        cursor.execute("SELECT * FROM caixa")
        rows = cursor.fetchall()

        return [
            {
                "id": row["id"],
                "esta_fechada": bool(row["esta_fechada"]),
                "pecas": recuperar_pecas_por_caixa_id(row["id"])
            }
            for row in rows
        ]

    except sqlite3.DatabaseError as e:
        print(f"Erro ao buscar caixas: {e}")
        raise


def criar_caixa() -> dict:
    global cursor, con

    try:
        cursor.execute("INSERT INTO caixa DEFAULT VALUES")

        con.commit()

        return {
            "id": cursor.lastrowid,
            "esta_fechada": False
        }

    except sqlite3.DatabaseError as e:
        print(f"Erro ao salvar caixa: {e}")
        con.rollback()
        raise


def recuperar_todas_as_pecas() -> list[dict]:
    global cursor

    try:
        cursor.execute("SELECT * FROM peca")
        rows = cursor.fetchall()

        return [
            {
                "id": row["id"],
                "caixa_id": row["caixa_id"],
                "peso": row["peso"],
                "cor": row["cor"],
                "comprimento": row["comprimento"],
                "status": row["status"],
                "motivos_reprovacao": json.loads(row["motivos_reprovacao"])
            }
            for row in rows
        ]

    except sqlite3.DatabaseError as e:
        print(f"Erro ao buscar peças: {e}")
        raise


def recuperar_peca_por_id(peca_id: int) -> dict:
    global cursor

    try:
        cursor.execute("SELECT * FROM peca WHERE id = ?", (peca_id,))
        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row["id"],
            "caixa_id": row["caixa_id"],
            "peso": row["peso"],
            "cor": row["cor"],
            "comprimento": row["comprimento"],
            "status": row["status"],
            "motivos_reprovacao": json.loads(row["motivos_reprovacao"])
        }
    except sqlite3.DatabaseError as e:
        print(f"Erro ao buscar peça {peca_id}: {e}")
        raise


def recuperar_caixa_por_id(caixa_id: int) -> dict:
    global cursor

    try:
        cursor.execute("SELECT * FROM caixa WHERE id = ?", (caixa_id,))
        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row["id"],
            "esta_fechada": row["esta_fechada"]
        }
    except sqlite3.DatabaseError as e:
        print(f"Erro ao buscar peça {caixa_id}: {e}")
        raise


def buscar_caixa_para_nova_peca() -> dict | None:
    
    caixas = recuperar_caixas()

    if len(caixas) == 0:
        return criar_caixa()

    caixa_para_nova_peca_encontrada = False

    for caixa in caixas:
        esta_fechada = caixa["esta_fechada"]

        if esta_fechada is True:
            continue

        caixa_para_nova_peca_encontrada = True
        return caixa

    if caixa_para_nova_peca_encontrada is False:
        return criar_caixa()


def popular_banco_de_dados_com_massa_de_testes() -> None:

    pecas_existentes = recuperar_todas_as_pecas()

    if len(pecas_existentes) > 0:
        return

    pecas = pegar_lista_pecas()

    for peca in pecas:
        if peca["status"].casefold() == STATUS_APROVADO.casefold():
            caixa = buscar_caixa_para_nova_peca()
            caixa_id = caixa.get("id")
            peca["caixa_id"] = caixa_id
        peca_salva = salvar_peca(peca)
        print(f"Peça cadastrada com sucesso com ID: {peca_salva["id"]}.")


def resetar_banco_de_dados() -> None:
    global cursor, con

    try:
        cursor.executescript("""
            DELETE FROM peca;
            DELETE FROM caixa;
            DELETE FROM sqlite_sequence WHERE name = 'peca';
            DELETE FROM sqlite_sequence WHERE name = 'caixa';
        """)

        con.commit()
        print("Banco de dados resetado com sucesso.")

    except sqlite3.DatabaseError as e:
        print(f"Erro ao resetar banco de dados: {e}")
        con.rollback()
        raise


if __name__ == "__main__":
    main()
