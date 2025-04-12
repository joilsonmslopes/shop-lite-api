from sqlmodel import SQLModel, create_engine, Session

# Caminho do banco (SQLite file)
sqlite_file_name = "shoplite.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Criação da Engine
engine = create_engine(sqlite_url, echo=True)

# Função para criar todas as tabelas
def create_db_and_tables():
  SQLModel.metadata.create_all(engine)

# Fornece uma sessão para interagir com o banco
def get_session():
  with Session(engine) as session:
    yield session