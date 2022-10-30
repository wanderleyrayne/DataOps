#Importação das libs
import sqlite3
# Criar BD
Conexao = sqlite3.connect('Banco_Dados.db')
Cursor = Conexao.cursor()

# Criar uma tabela

Query = '''

CREATE TABLE Tabela_Processamento(
    Routine_Id, TEXT
    Routine_Name TEXT,
    User TEXT,
    User_Machine TEXT,
    User_Operation_System TEXT,
    StartDate TEXT,
    StartHours TEXT,
    Internet_Connection TEXT,
    User_local_IP TEXT,
    FinishedDate TEXT,
    FinishedHours TEXT,
    Execution_Time TEXT,
    Erro TEXT
)

'''

Cursor.execute(Query)
Conexao.commit()

Conexao.close()