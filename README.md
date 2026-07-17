# 📖 Alura Album - Copa do Mundo Tech

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)

Álbum de Figurinhas Digital Interativo com a temática **"Copa do Mundo Tech"**. Este projeto é um tributo interativo à história e evolução do desenvolvimento de software, reunindo mentes brilhantes nacionais e internacionais que moldam o futuro da tecnologia. 

Desenvolvido como um projeto **Full Stack**, o álbum simula a experiência física de folhear um livro com animação realista em 3D, efeitos sonoros sintetizados via **Web Audio API** e integração dinâmica com uma **API REST FastAPI** em Python.

---

## 💡 Diferenciais & Destaques Técnicos

Este projeto foi projetado com foco em boas práticas de arquitetura, otimização de performance e excelente experiência do usuário (UX/UI). Ele se destaca por:
*   **Arquitetura Clean e Desacoplada:** Separação clara de responsabilidades entre o Backend (API REST) e Frontend (Client Estático).
*   **Manipulação Avançada de DOM e Web APIs:** Uso de JavaScript Vanilla moderno sem frameworks pesados, demonstrando domínio das APIs nativas do navegador (Fetch API, Web Audio API, seletores, manipulação de classes dinâmicas).
*   **Física e Animações em CSS:** Criação de interfaces responsivas de altíssima fidelidade visual, com sombras realistas de lombada, transições Snappy, cursores de arrasto personalizados e efeitos de *glitch* em tempo real.
*   **Desenvolvimento de APIs Modernas:** Construção de rotas performáticas em Python utilizando FastAPI, validação estática de tipos, tratamento de erros HTTP e estruturação automática de documentação OpenAPI.
*   **Integração Assíncrona:** Gerenciamento eficiente de requisições paralelas e tratamento de estados (carregamento de imagem com sucesso vs falha de rede).

---

## 📁 Estrutura do Projeto

```text
.
├── backend/                   # Backend em Python (FastAPI)
│   ├── main.py                # Servidor API REST, middlewares CORS e endpoints
│   ├── figurinhas/            # Repositório de imagens das figurinhas (01-30)
│   └── .venv/                 # Ambiente virtual contendo as dependências
├── frontend/                  # Frontend Estático (Client)
│   ├── index.html             # Estrutura semântica do álbum e slots
│   ├── style.css              # Design System (variáveis), animações e responsividade
│   └── app.js                 # Lógica de negócio, síntese de áudio e fetch à API
└── README.md                  # Documentação do projeto
```

---

## ⚙️ Backend (Python + FastAPI)

O backend é construído em **FastAPI**, um framework Python moderno, de alta performance (baseado em Starlette e Pydantic) e com tipagem estática que facilita o desenvolvimento rápido de APIs seguras.

### Principais Características do Backend:
1.  **Segurança e CORS Habilitado (Cross-Origin Resource Sharing):**
    O backend possui configuração explícita de políticas de CORS por meio do middleware `CORSMiddleware` do FastAPI. Isso é indispensável em uma arquitetura Full Stack desacoplada, garantindo que o frontend (rodando em servidores de desenvolvimento locais como Live Server, ou servidores HTTP nativos como `http://localhost:3000`, e até mesmo via protocolo local `file://`) possa se comunicar e fazer requisições assíncronas à API (rodando em `http://localhost:8000`) sem sofrer bloqueios pelas políticas restritivas de mesma origem (*Same-Origin Policy*) impostas pelos navegadores.
    *   **Configuração de Segurança:** Foram liberadas todas as origens (`["*"]`), métodos HTTP (`["*"]`) e cabeçalhos customizados (`["*"]`) para facilitar a testabilidade local e integrações rápidas do ecossistema.
2.  **Resolução Dinâmica de Arquivos:** Uso de `glob` e manipulação de caminhos absolutos do sistema de arquivos para encontrar imagens com base no padrão numérico de ID (ex: `01-alan-turing.jpg`), permitindo compatibilidade imediata com extensões diversas (`.jpg`, `.jpeg`, `.png`, `.webp`, `.avif`).
3.  **Entrega Eficiente de Mídia:** Uso de `FileResponse` da Starlette para realizar streaming otimizado dos arquivos de imagem diretamente ao cliente.

### Endpoints Disponíveis:
*   `GET /` — Endpoint de integridade física da API (Health Check / Boas-vindas).
*   `GET /figurinhas` — Retorna uma lista em formato JSON com todas as 30 figurinhas catalogadas, contendo: `id`, `nome`, `categoria` e o `imagem_url`.
*   `GET /figurinhas/{id}` — Busca os detalhes técnicos de uma única figurinha pelo seu ID correspondente (retorna `404` se o ID for inválido).
*   `GET /figurinhas/{id}/imagem` — Busca a imagem física da figurinha no sistema de arquivos do servidor.
*   `GET /total` — Retorna estatísticas em tempo real sobre o progresso do álbum: total de slots, figurinhas coladas (existentes) e quantidade restante para completar.

### 🌐 Documentação Interativa Automática (`/docs`)

Uma das maiores vantagens em utilizar o FastAPI é a geração automática de especificações OpenAPI. Ao rodar o backend, duas rotas de documentação são expostas nativamente:

*   **Swagger UI (`/docs`):** Permite visualizar de forma gráfica e interativa todos os endpoints da API. A partir dela, **qualquer pessoa pode testar os endpoints diretamente no navegador**, clicando no botão **"Try it out"** e inspecionando os payloads de resposta em tempo real, sem necessidade de ferramentas externas como Postman ou Insomnia.
*   **ReDoc (`/redoc`):** Uma visualização alternativa focada em documentação legível e detalhada de schemas, excelente para integração de times.

---

## 🎨 Frontend (HTML5, CSS Vanilla, JavaScript)

O frontend foi desenvolvido utilizando tecnologias nativas da Web para demonstrar forte domínio em engenharia de client-side.

### Principais Funcionalidades do Frontend:
1.  **Visual Premium & Design System:** Interface customizada baseada em variáveis CSS com temática neon espacial (`--color-blue-universe`, `--color-dev-blue`, etc.), fontes modernas carregadas via Google Fonts (`Outfit` e `Inter`) e sombras realistas para lombada central que mudam de acordo com o lado da página aberta.
2.  **Animação 3D com PageFlip:** Utilização da biblioteca `St.PageFlip` de alto desempenho para transições realistas de dobras de página.
3.  **Preenchimento Dinâmico via API:** Conexão assíncrona inteligente. O script `app.js` realiza o `fetch` para `/figurinhas`, processa os dados usando a estrutura de dados `Map` para otimização de busca $O(1)$ e popula automaticamente os slots dinâmicos `#01` a `#30` no DOM.
4.  **Colagem Suave (UX):** As figurinhas coladas são reveladas através de uma animação suave de fade-in e scale (`@keyframes sticker-aparecer`), simulando a aplicação da figurinha física ao papel.
5.  **Física de Gestos Aperfeiçoada:** Implementação de um manipulador de eventos personalizado para os gestos de arrasto (com mouse ou touch), exigindo um limite de movimento de pelo menos `10px` para iniciar a virada da página, eliminando disparos acidentais comuns de cliques estáticos.
6.  **Síntese Sonora Procedural (Web Audio API):**
    *   **Inovação Técnica:** O som realista de papel sendo folheado é gerado **100% via código e matemática**, sem carregar arquivos MP3 ou WAV pesados.
    *   **Como funciona:** Um oscilador gera ruído branco em tempo real, que passa por um filtro passabanda (`bandpass`) com sweep dinâmico de frequência que cai de `1500Hz` a `350Hz` (simulando a acústica da página se movimentando no ar) e por um filtro passabaixas (`lowpass`) para atenuar ruídos estridentes artificiais.

---

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
*   **Python 3.10+** instalado em sua máquina.
*   Um navegador web moderno com suporte a Web Audio API.

### Passo 1: Executando o Backend (API)
Abra o seu terminal na pasta raiz do projeto e execute os seguintes comandos:

```bash
# Navegar até a pasta backend
cd backend

# Criar um ambiente virtual (caso não exista)
python -m venv .venv

# Ativar o ambiente virtual
# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# No Linux/macOS:
source .venv/bin/activate

# Instalar as dependências do projeto
pip install fastapi uvicorn

# Iniciar o servidor de desenvolvimento
uvicorn main:app --reload
```

O backend iniciará na porta padrão `http://localhost:8000`.

*   Para acessar a documentação interativa da API, vá para: **`http://localhost:8000/docs`**

### Passo 2: Executando o Frontend
Com o backend rodando ativamente na porta `8000`, basta abrir o arquivo `frontend/index.html` em qualquer navegador.
*   **Recomendação:** Para evitar problemas de CORS em alguns navegadores rígidos ao abrir arquivos locais via protocolo `file://`, execute o frontend utilizando um servidor local simples, como a extensão **Live Server** do VS Code ou usando o utilitário nativo de Python em um novo terminal:

```bash
# Executar a partir da pasta frontend
cd frontend
python -m http.server 3000
```
Acesse no navegador: `http://localhost:3000`

---

## 📚 Categorias do Álbum
*   **IA (Pág. 1):** Slot `#01` ao `#05` (Alan Turing, John McCarthy, Sam Altman, Geoffrey Hinton, Yann LeCun).
*   **Python (Pág. 2):** Slot `#06` ao `#10` (Guido van Rossum, Tim Peters, Raymond Hettinger, Travis Oliphant, Wes McKinney).
*   **Banco de Dados (Pág. 3):** Slot `#11` ao `#15` (Edgar F. Codd, Larry Ellison, Michael Widenius, Salvatore Sanfilippo, Eliot Horowitz).
*   **Sistemas Operacionais (Pág. 4):** Slot `#16` ao `#20` (Linus Torvalds, Dennis Ritchie, Richard Stallman, Bill Gates, Steve Jobs).
*   **Brasil - Vol. 1 & 2 (Pág. 5 & 6):** Slot `#21` ao `#30` (Lideranças e educadores tech do país: Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Andre David, Guilherme Lima, Gi Space Coding, Vinicius Neves, Rafaela Ballerini, e uma surpresa no slot `#30`).

---

Desenvolvido para fins didáticos e demonstração de engenharia de software Full Stack. Sinta-se à vontade para explorar os códigos ou testar a API!
