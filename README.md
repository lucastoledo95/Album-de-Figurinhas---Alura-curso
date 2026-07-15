# 📖 Alura Album - Copa do Mundo Tech

Este projeto é um **Álbum de Figurinhas Digital Interativo** com a temática "Copa do Mundo Tech". Ele serve como um tributo interativo à história e evolução do desenvolvimento de software, apresentando mentes brilhantes nacionais e internacionais que moldam o futuro da tecnologia. 

O design do álbum simula um livro físico com animação realista de virada de páginas, efeitos sonoros sintetizados via Web Audio API e integração dinâmica para carregamento de figurinhas.

---

## 🎯 Objetivo do Projeto

O objetivo principal é construir uma interface web moderna, fluida e interativa de um álbum de figurinhas. O projeto foi estruturado para demonstrar a integração entre um frontend robusto (com manipulação de DOM, bibliotecas de terceiros para efeitos visuais, síntese sonora) e uma API de backend para recuperar de forma dinâmica as imagens e informações das figurinhas que preenchem os slots do álbum.

---

## 📂 Funcionalidade dos Arquivos

O projeto é construído em cima de três arquivos principais no frontend, com foco em simplicidade e performance:

### 1. 📄 [`index.html`](file:///e:/projetos%20DESENVOLVIMENTOS/Album-de-Figurinhas---Alura-curso/Album-de-Figurinhas---Alura-curso/index.html)
Define toda a estrutura e conteúdo semântico do álbum de figurinhas.
*   **Capa e Contracapa:** Páginas especiais com efeitos estéticos e estruturais (contendo selos, títulos de destaque e código de barras simulado).
*   **Páginas Internas:** Divididas por categorias de tecnologia com 5 slots numerados por página:
    *   **Pág. 1: IA (Inteligência Artificial)** - Alan Turing, John McCarthy, Sam Altman, Geoffrey Hinton, Yann LeCun.
    *   **Pág. 2: Python** - Guido van Rossum, Tim Peters, Raymond Hettinger, Travis Oliphant, Wes McKinney.
    *   **Pág. 3: Banco de Dados** - Edgar F. Codd, Larry Ellison, Michael Widenius, Salvatore Sanfilippo, Eliot Horowitz.
    *   **Pág. 4: Sistemas Operacionais** - Linus Torvalds, Dennis Ritchie, Richard Stallman, Bill Gates, Steve Jobs.
    *   **Pág. 5 & 6: Brasil (Celebridades Tech Vol. 1 & 2)** - Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Andre David, Guilherme Lima, Gi Space Coding, Vinicius Neves, Rafaela Ballerini e "Você" (slot interativo).
*   **Controles do Usuário:** Botões de navegação lateral (Anterior/Próxima) e botão de alternar áudio (Mute/Unmute).
*   **Integrações:** Importação das fontes (`Inter` e `Outfit` do Google Fonts) e importação via CDN da biblioteca de animação de livros `PageFlip`.

### 2. 🎨 [`style.css`](file:///e:/projetos%20DESENVOLVIMENTOS/Album-de-Figurinhas---Alura-curso/Album-de-Figurinhas---Alura-curso/style.css)
Responsável por toda a estilização, design visual premium e animações.
*   **Identidade Visual:** Paleta de cores moderna inspirada em tecnologia e ficção científica, utilizando variáveis CSS com tons escuros e luzes neon (azul espacial, azul profundo, branco neve, preto novo).
*   **Efeitos de Realismo:** Sombras graduais na lombada central do álbum (`.page-content::after`) para criar a percepção de profundidade de um livro aberto físico.
*   **Responsividade e Layout:** Uso de Grids e Flexbox para alinhar os slots das figurinhas de forma responsiva, com cursores customizados (`grab`/`grabbing`) para indicar que a página pode ser arrastada.
*   **Micro-interações:** Efeitos de hover nos botões de som e navegação, animações de brilho para os slots especiais de figurinhas, e efeito glitch futurista nos títulos da capa.

### 3. ⚡ [`app.js`](file:///e:/projetos%20DESENVOLVIMENTOS/Album-de-Figurinhas---Alura-curso/Album-de-Figurinhas---Alura-curso/app.js)
Controla o comportamento dinâmico, interações e áudio do projeto.
*   **Integração com Backend (API):** Faz requisições assíncronas (`fetch`) para a API do FastAPI (em `http://localhost:8000/figurinhas`) para obter os dados das figurinhas. Se conectada com sucesso, renderiza as imagens dinamicamente nos slots corretos com base no número (`#01` a `#30`).
*   **Inicialização do PageFlip:** Configura e controla a biblioteca externa `St.PageFlip` (largura, altura, margens, suporte mobile e tempos de transição rápida de 800ms).
*   **Arraste Customizado:** Substitui o comportamento padrão de clique/arraste da biblioteca por um algoritmo personalizado que detecta a intenção de arraste a partir de um limite de movimentação (evitando viradas de página acidentais ao tentar apenas clicar em botões).
*   **Síntese Sonora (Web Audio API):** Gera proceduralmente em tempo real o som físico de "papel virando" ao alternar as páginas. Isso é feito gerando ruído branco (White Noise) atenuado por filtros passa-faixa (Bandpass Filter) dinâmicos e filtros passa-baixa (Lowpass Filter), eliminando arquivos pesados de áudio e garantindo carregamento instantâneo.
*   **Controles de Entrada:** Gerencia os botões de navegação na tela, controle de mute/unmute do som de papel, e suporte a comandos de teclado (setas esquerda e direita).

---

## 🛠️ Tecnologias Utilizadas

*   **HTML5** - Estruturação semântica de páginas e slots.
*   **CSS3** - CSS Vanilla estruturado com variáveis e animações.
*   **JavaScript (ES6+)** - Lógica interativa do álbum.
*   **PageFlip Library (St.PageFlip)** - Motor de animação tridimensional e interativa de páginas de livro.
*   **Web Audio API** - Síntese de som digital em tempo real para os efeitos sonoros.
*   **FastAPI / Python** (Backend) - Servidor de dados das figurinhas (opcional, rodando na porta `8000`).

---

## 🚀 Como Executar o Projeto

1.  **Frontend Estático:**
    *   Basta abrir o arquivo [`index.html`](file:///e:/projetos%20DESENVOLVIMENTOS/Album-de-Figurinhas---Alura-curso/Album-de-Figurinhas---Alura-curso/index.html) diretamente no navegador de sua preferência ou usar uma extensão de servidor local (como *Live Server* do VS Code).
    *   *Nota:* Nesse modo, o álbum exibirá apenas os slots cinzas vazios com os nomes dos desenvolvedores (modo offline).

2.  **Com o Servidor Backend (Opcional - Dia 3):**
    *   Para visualizar o álbum completo com as fotos das figurinhas coladas, certifique-se de que o backend em Python está rodando.
    *   Abra o terminal, navegue até a pasta do backend e inicie o servidor:
        ```bash
        cd backend/dia-3
        uvicorn main:app --reload
        ```
    *   Atualize o frontend para que o arquivo [`app.js`](file:///e:/projetos%20DESENVOLVIMENTOS/Album-de-Figurinhas---Alura-curso/Album-de-Figurinhas---Alura-curso/app.js) consiga ler a rota de imagens no endereço `http://localhost:8000`.
