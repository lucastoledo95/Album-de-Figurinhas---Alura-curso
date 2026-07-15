# 📖 Alura Album - Copa do Mundo Tech

Álbum de Figurinhas Digital Interativo com a temática **"Copa do Mundo Tech"**. O projeto é um tributo interativo à história e evolução do desenvolvimento de software, reunindo mentes nacionais e internacionais que moldam o futuro da tecnologia.

O álbum simula um livro físico com animação realista de virada de páginas (3D), efeitos sonoros sintetizados via **Web Audio API** e integração dinâmica com uma **API FastAPI** para carregamento das figurinhas.

---

## 🎯 Objetivo

Construir uma interface web moderna, fluida e interativa de um álbum de figurinhas. O projeto demonstra a integração entre um **frontend** (manipulação de DOM, bibliotecas de terceiros para efeitos visuais e síntese sonora) e um **backend** que disponibiliza dinamicamente os dados das figurinhas que preenchem os slots do álbum.

---

## 📁 Estrutura do Projeto

```
.
├── backend/                 # API FastAPI (servidor de dados)
│   ├── main.py              # Aplicação FastAPI com rotas de figurinhas
│   ├── __pycache__/         # Cache de bytecode Python
│   └── .venv/               # Ambiente virtual (FastAPI, Uvicorn, etc.)
├── frontend/                # Interface estática do álbum
│   ├── index.html           # Estrutura semântica e conteúdo do álbum
│   ├── style.css            # Estilização, tema visual e animações
│   └── app.js               # Lógica, interações, áudio e integração com a API
└── README.md
```

As dependências do backend (FastAPI, Uvicorn, Starlette, Pydantic) estão instaladas no ambiente virtual `.venv`.

---

## 🧩 Funcionalidade dos Arquivos

### 1. 📄 `frontend/index.html`
Define a estrutura e o conteúdo semântico do álbum.
- **Capa e Contracapa:** Páginas especiais com selos, títulos com efeito *glitch* e código de barras simulado.
- **Páginas internas:** Agrupadas por categorias, com 5 slots numerados (`#01` a `#30`):
  - **Pág. 1 — IA:** Alan Turing, John McCarthy, Sam Altman, Geoffrey Hinton, Yann LeCun.
  - **Pág. 2 — Python:** Guido van Rossum, Tim Peters, Raymond Hettinger, Travis Oliphant, Wes McKinney.
  - **Pág. 3 — Banco de Dados:** Edgar F. Codd, Larry Ellison, Michael Widenius, Salvatore Sanfilippo, Eliot Horowitz.
  - **Pág. 4 — Sistemas Operacionais:** Linus Torvalds, Dennis Ritchie, Richard Stallman, Bill Gates, Steve Jobs.
  - **Pág. 5 & 6 — Brasil (Vol. 1 & 2):** Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Andre David, Guilherme Lima, Gi Space Coding, Vinicius Neves, Rafaela Ballerini e "Você" (slot interativo).
- **Controles:** Botões de navegação lateral (anterior/próxima) e botão de alternar áudio.
- **Integrações:** Google Fonts (`Inter`, `Outfit`) e biblioteca `PageFlip` via CDN.

### 2. 🎨 `frontend/style.css`
Responsável por toda a identidade visual, layout e animações.
- **Identidade visual:** Paleta tecnológica com variáveis CSS (azul espacial, azul profundo, branco neve, preto novo) e detalhes neon.
- **Realismo:** Sombras na lombada central (`.page-content::after`) para dar profundidade de livro aberto.
- **Layout responsivo:** Grids e Flexbox; cursores `grab`/`grabbing` indicando que a página pode ser arrastada.
- **Micro-interações:** Hover nos botões, brilho nos slots especiais, glitch na capa e animação de "colar" figurinha (`.sticker-aparecer`).
- **Responsividade:** Breakpoints em `1200px` e `768px` para adaptação a tablets e mobile.

### 3. ⚡ `frontend/app.js`
Controla o comportamento dinâmico, interações e áudio.
- **Integração com a API:** Requisições assíncronas (`fetch`) para `http://localhost:8000/figurinhas`, montando um `Map` de `id → figurinha` e preenchendo os slots correspondentes (`#01` a `#30`) com imagens dinâmicas quando disponíveis.
- **Inicialização do PageFlip:** Configura `St.PageFlip` (dimensões, sombras, suporte mobile e tempo de transição de `800ms`).
- **Arraste customizado:** Substitui o clique/arraste padrão da biblioteca por um algoritmo que exige um limiar de movimento (evitando viradas acidentais).
- **Síntese sonora (Web Audio API):** Gera proceduralmente o som de "papel virando" em tempo real (ruído branco + filtros *bandpass* e *lowpass*), sem arquivos de áudio externos.
- **Controles:** Botões de navegação, mute/unmute e suporte a setas do teclado (←/→).

### 4. 🐍 `backend/main.py`
API FastAPI que simula um banco de dados em memória.
- `GET /` → Mensagem de boas-vindas (`{"mensagem": "Olá, mundo! 🌍"}`).
- `GET /figurinhas` → Lista completa de figurinhas (id, nome, categoria).
- `GET /figurinhas/{figurinha_id}` → Busca por id; retorna `404` se não encontrada.

O frontend consome essa API para preencher os slots do álbum dinamicamente.

---

## 🛠️ Tecnologias Utilizadas

- **HTML5** — Estrutura semântica de páginas e slots.
- **CSS3** — CSS Vanilla com variáveis e animações.
- **JavaScript (ES6+)** — Lógica interativa do álbum.
- **PageFlip (St.PageFlip)** — Motor de animação 3D de páginas de livro (via CDN).
- **Web Audio API** — Síntese de som digital em tempo real.
- **FastAPI / Python** — Backend de dados (porta `8000`).

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10+ (o `.venv` atual foi gerado com Python 3.14).
- Navegador moderno (Chrome, Edge, Firefox).

### 1. Frontend Estático (modo offline)
Basta abrir `frontend/index.html` no navegador ou usar uma extensão de servidor local (ex.: *Live Server* do VS Code). Nesse modo, o álbum exibe os slots com os nomes dos desenvolvedores.

### 2. Backend (API FastAPI)
Em um terminal, ative o ambiente virtual e inicie o servidor:

```bash
cd backend
.\.venv\Scripts\Activate.ps1   # Windows (PowerShell)
# source .venv/bin/activate    # Linux/macOS

uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`. Documentação interativa automática em `http://localhost:8000/docs`.

### 3. Frontend + Backend (modo completo)
Com o backend rodando na porta `8000`, abra o `frontend/index.html`. O `app.js` buscará `http://localhost:8000/figurinhas` e preencherá os slots automaticamente.

---

## 📄 Licença

Projeto desenvolvido como material de estudo da **Imersão Alura** (Julho/2026). Uso educacional.
