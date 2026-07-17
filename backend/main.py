from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Inicializa a aplicação FastAPI
app = FastAPI()

# 1. Configure o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Defina caminhos absolutos para a pasta de imagens usando:
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Crie uma lista chamada `figurinhas` com as 30 figurinhas,
# cada uma com: id, nome, categoria, imagem_url
# O imagem_url deve apontar para "/figurinhas/{id}/imagem"
# Comente as figurinhas que ainda não estão disponíveis (ex: ids 3, 4, 5...)
# Deixe ativas apenas as figurinhas cujas imagens existem na pasta figurinhas/
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Sam Altman", "categoria": "IA", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Geoffrey Hinton", "categoria": "IA", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Yann LeCun", "categoria": "IA", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Guido van Rossum", "categoria": "PYTHON", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Tim Peters", "categoria": "PYTHON", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Raymondo Hettinger", "categoria": "PYTHON", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Travis Oliphant", "categoria": "PYTHON", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes McKinney", "categoria": "PYTHON", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar F. Codd", "categoria": "BANCO DE DADOS", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry Ellison", "categoria": "BANCO DE DADOS", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael Widenius", "categoria": "BANCO DE DADOS", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore Sanfilippo", "categoria": "BANCO DE DADOS", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot Horowitz", "categoria": "BANCO DE DADOS", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus Torvalds", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis Ritchie", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard Stallman", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill Gates", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve Jobs", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo Silveira", "categoria": "BRASIL", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme Silveira", "categoria": "BRASIL", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gustavo Guanabara", "categoria": "BRASIL", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mauricio Aniche", "categoria": "BRASIL", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre David", "categoria": "BRASIL", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme Lima", "categoria": "BRASIL", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi Space Coding", "categoria": "BRASIL", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius Neves", "categoria": "BRASIL", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafaela Ballerini", "categoria": "BRASIL", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Lucas Toledo", "categoria": "BRASIL", "imagem_url": "/figurinhas/30/imagem"},
]

# 4. Crie o endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# 5. Crie o endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Retorna 404 se não encontrar
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna FileResponse com o arquivo encontrado
    return FileResponse(arquivos[0])

# Mapeia requisições HTTP GET na rota "/total" para retornar as estatísticas do álbum
@app.get("/total")
def estatisticas_album():
    # O total de figurinhas no álbum é fixado em 30
    total_album = 30
    # O número de figurinhas coladas é o total de itens na lista ativa de figurinhas
    coladas = len(figurinhas)
    # As figurinhas que faltam são a diferença entre o total do álbum e as já coladas
    faltam = total_album - coladas
    
    return {
        "total_album": total_album,
        "coladas": coladas,
        "faltam": faltam
    }

# Mapeia requisições HTTP GET na rota "/figurinhas/{id}" para buscar uma figurinha por ID
@app.get("/figurinhas/{figurinha_id}")
def obter_figurinha(figurinha_id: int):
    # Busca a figurinha correspondente ao id informado
    for figurinha in figurinhas:
        if figurinha["id"] == figurinha_id:
            return figurinha
    # Se não encontrar, lança um erro HTTP 404 (Not Found)
    raise HTTPException(status_code=404, detail="Figurinha não encontrada")
