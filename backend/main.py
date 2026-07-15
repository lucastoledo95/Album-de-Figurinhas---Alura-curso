# Importa a classe FastAPI e a exceção HTTPException necessárias para criar a aplicação e tratar erros
from fastapi import FastAPI, HTTPException

# Inicializa a instância principal da aplicação FastAPI
app = FastAPI()

# Lista de figurinhas em memória (simulando um banco de dados)
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA"}
]

# Mapeia requisições HTTP GET na rota raiz ("/") para a função correspondente
@app.get("/")
def hello_world():
    # Retorna o dicionário Python, que o FastAPI converte automaticamente em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}

# Mapeia requisições HTTP GET na rota "/figurinhas" para a função correspondente
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas
    return figurinhas

# Mapeia requisições HTTP GET na rota "/figurinhas/{id}" para buscar uma figurinha por ID
@app.get("/figurinhas/{figurinha_id}")
def obter_figurinha(figurinha_id: int):
    # Busca a figurinha correspondente ao id informado
    for figurinha in figurinhas:
        if figurinha["id"] == figurinha_id:
            return figurinha
    # Se não encontrar, lança um erro HTTP 404 (Not Found)
    raise HTTPException(status_code=404, detail="Figurinha não encontrada")

