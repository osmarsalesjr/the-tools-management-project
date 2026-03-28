import sqlite3
import json

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
    motivos_reprovacao  TEXT DEFAULT '[]', -- JSON array serializado

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

        con = sqlite3.connect("bd.db")
        con.row_factory = sqlite3.Row
        criar_banco_de_dados()

    except sqlite3.DatabaseError as e:
        print(f"Erro ao conectar ou inicializar o banco de dados: {e}")
        
        if con:
            con.close()
        raise


def criar_banco_de_dados() -> None:
    global cursor, con

    try:

        cursor = con.cursor()
        cursor.executescript(SCRIPT)

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

        if caixa_id is not None:
            verificar_status_caixa(caixa_id)
        
        peca["id"] = cursor.lastrowid
        return peca

    except sqlite3.DatabaseError as e:
        print(f"Erro ao salvar peça: {e}")
        con.rollback()
        raise


def verificar_status_caixa(caixa_id: int) -> None:

    try:
        quantidade_pecas = contar_pecas_por_caixa(caixa_id)

        if quantidade_pecas >= 10:
            atualizar_status_caixa(caixa_id, int(True))
            print(f"Caixa {caixa_id} atualizada para fechado.")
        else:
            atualizar_status_caixa(caixa_id, int(False))
            print(f"Caixa {caixa_id} atualizada para aberta.")

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


def atualizar_status_caixa(caixa_id: int, status: int) -> None:
    global cursor, con

    try:
        cursor.execute("""
            UPDATE caixa SET esta_fechada = ? WHERE caixa_id = ?
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
        caixa = recuperar_caixa_por_id(caixa_id)

        if (caixa is not None and caixa["esta_fechada"]):
            atualizar_status_caixa(caixa_id, int(False))
            

    except sqlite3.DatabaseError as e:
        print(f"Erro ao atualizar status caixa: {e}")
        con.rollback()
        raise


def recuperar_todas_as_caixas() -> list[dict]:
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
                "caixa_id": row["id"],
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
            "caixa_id": row["id"],
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


if __name__ == "__main__":
    main()
