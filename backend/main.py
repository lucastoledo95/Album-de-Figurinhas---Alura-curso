# Importa o FastAPI para criar a API, o StaticFiles para servir arquivos estáticos e o módulo os para gerenciar caminhos
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import os

# Inicializa a aplicação FastAPI
app = FastAPI()

# Define o caminho absoluto da pasta contendo as imagens das figurinhas.
# PASTA_BASE obtém o diretório do arquivo main.py atual, garantindo que o caminho
# funcione de forma consistente independente do diretório de onde o servidor for executado.
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura o FastAPI para servir arquivos estáticos.
# A pasta PASTA_IMAGENS é montada na rota "/imgs", com o nome identificador "imgs".
# Com isso, o arquivo "figurinhas/01-alan-turing.jpg" fica acessível em "/imgs/01-alan-turing.jpg".
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista em memória com os dados das figurinhas cadastradas
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/imgs/01-alan-turing.jpg"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/imgs/02-john-mccarthy.jpg"},
   # {"id": 3, "nome": "Sam Altman", "categoria": "IA", "imagem_url": "/imgs/03-sam.jpg"},
   # {"id": 4, "nome": "Geoffrey Hinton", "categoria": "IA", "imagem_url": "/imgs/04-Geoffrey.jpg"},
   # {"id": 5, "nome": "Yann LeCun", "categoria": "IA", "imagem_url": "/imgs/05-Yann.jpeg"},
   # {"id": 6, "nome": "Guido van Rossum", "categoria": "PYTHON", "imagem_url": "/imgs/06-Guido.jpg"},
   # {"id": 7, "nome": "Tim Peters", "categoria": "PYTHON", "imagem_url": "/imgs/07-Tim.jpeg"},
   # {"id": 8, "nome": "Raymondo Hettinger", "categoria": "PYTHON", "imagem_url": "/imgs/08-Ray.jpeg"},
   # {"id": 9, "nome": "Travis Oliphant", "categoria": "PYTHON", "imagem_url": "/imgs/09-Travis.jpg"},
   # {"id": 10, "nome": "Wes McKinney", "categoria": "PYTHON", "imagem_url": "/imgs/10-Wes.jpg"},
   # {"id": 11, "nome": "Edgar F. Codd", "categoria": "BANCO DE DADOS", "imagem_url": "/imgs/11-Edgar.jpeg"},
   # {"id": 12, "nome": "Larry Ellison", "categoria": "BANCO DE DADOS", "imagem_url": "/imgs/12-Larry.jpg"},
   # {"id": 13, "nome": "Michael Widenius", "categoria": "BANCO DE DADOS", "imagem_url": "/imgs/13-Michael.webp"},
   # {"id": 14, "nome": "Salvatore Sanfilippo", "categoria": "BANCO DE DADOS", "imagem_url": "/imgs/14-Salvatore.png"},
   # {"id": 15, "nome": "Eliot Horowitz", "categoria": "BANCO DE DADOS", "imagem_url": "/imgs/15-Eliot.png"},
   # {"id": 16, "nome": "Linus Torvalds", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/imgs/16-Linus.jpg"},
   # {"id": 17, "nome": "Dennis Ritchie", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/imgs/17-Dennis.png"},
   # {"id": 18, "nome": "Richard Stallman", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/imgs/18-Richard.jpg"},
   # {"id": 19, "nome": "Bill Gates", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/imgs/19-bill.jpg"},
   # {"id": 20, "nome": "Steve Jobs", "categoria": "SISTEMAS OPERACIONAIS", "imagem_url": "/imgs/20-Steve.webp"},
   # {"id": 21, "nome": "Paulo Silveira", "categoria": "BRASIL", "imagem_url": "/imgs/21-Paulo.avif"},
   # {"id": 22, "nome": "Guilherme Silveira", "categoria": "BRASIL", "imagem_url": "/imgs/22-Guilherme.jpeg"},
   # {"id": 23, "nome": "Gustavo Guanabara", "categoria": "BRASIL", "imagem_url": "/imgs/23-Gus.png"},
   # {"id": 24, "nome": "Mauricio Aniche", "categoria": "BRASIL", "imagem_url": "/imgs/24-Mauricio.jpeg"},
   # {"id": 25, "nome": "Andre David", "categoria": "BRASIL", "imagem_url": "/imgs/25-Andre.jpeg"},
   # {"id": 26, "nome": "Guilherme Lima", "categoria": "BRASIL", "imagem_url": "/imgs/26-Guilherme.jpeg"},
   # {"id": 27, "nome": "Gi Space Coding", "categoria": "BRASIL", "imagem_url": "/imgs/27-Gi.jpeg"},
   # {"id": 28, "nome": "Vinicius Neves", "categoria": "BRASIL", "imagem_url": "/imgs/28-Vinicius.png"},
   # {"id": 29, "nome": "Rafaela Ballerini", "categoria": "BRASIL", "imagem_url": "/imgs/29-Rafa.jpeg"},
   # {"id": 30, "nome": "Lucas Toledo", "categoria": "BRASIL", "imagem_url": ""}
]

# Define o único endpoint GET "/figurinhas" que retorna a lista de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas que será convertida em JSON pelo FastAPI
    return figurinhas

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

