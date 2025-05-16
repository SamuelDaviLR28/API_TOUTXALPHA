from app.database import engine, Base

def create_database():
    Base.metadata.create_all(bind=engine)
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    create_database()
