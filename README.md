# MeetGPT – Transcrição de Reuniões 🎙️
[English version](README.en.md)

Aplicação Web em Python para capturar áudio de reuniões em tempo real, transcrever com Whisper e gerar resumos inteligentes com GPT. Ideal para registrar decisões, facilitar revisões e servir como base para assistentes virtuais e soluções de acessibilidade.

## Sumário
- [Visão geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Como funciona](#como-funciona)
- [Arquitetura e estrutura de pastas](#arquitetura-e-estrutura-de-pastas)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Uso](#uso)
- [Personalização](#personalização)
- [Boas práticas e segurança](#boas-práticas-e-segurança)
- [Solução de problemas](#solução-de-problemas)
- [Roadmap](#roadmap)
- [Contribuição](#contribuição)
- [Autor](#autor)
- [Licença](#licença)

---

## Visão geral
O MeetGPT é um Web App construído com Streamlit que:
- Captura áudio do microfone via WebRTC.
- Transcreve o áudio em tempo real com Whisper (OpenAI).
- Gera resumos objetivos com pontos de acordos utilizando modelos GPT.
- Armazena e organiza o histórico de reuniões localmente.

Ao final, você terá um projeto robusto que integra captura de áudio, processamento com IA e apresentação amigável.

---

## Funcionalidades 
- Gravação de áudio direto do navegador (microfone).
- Transcrição incremental a cada ~5 segundos.
- Geração automática de resumo com:
  - Texto corrido (até 300 caracteres).
  - Lista de acordos/combinações em bullet points.
- Organização de reuniões por data/hora com título.
- Visualização do resumo e da transcrição completa.

---

## Como funciona
Fluxo principal do `app.py`:
1. Captura de áudio com `streamlit-webrtc` (modo SENDONLY).
2. Agregação dos frames de áudio com `pydub`:
   - `audio.mp3` (acumulado da reunião)
   - `audio_temp.mp3` (janela incremental)
3. A cada ~5 segundos, envia `audio_temp.mp3` para transcrição:
   - `OpenAI Whisper (model="whisper-1")`
   - Idioma padrão: `pt`
4. Concatena a transcrição incremental e exibe em tela, salvando em `transcricao.txt`.
5. Na aba de reuniões salvas:
   - Permite adicionar um título.
   - Gera e exibe o resumo com `chat.completions` (modelo padrão `gpt-3.5-turbo-1106`) usando um prompt estruturado.
   - Salva o resumo em `resumo.txt`.

---

## Arquitetura e estrutura de pastas
- Interface: Streamlit (duas abas)
  - Gravar Reunião
  - Ver transcrições salvas
- Persistência local: pasta `arquivos/` na raiz do projeto.

Estrutura de saída por reunião:
```
arquivos/
└── YYYY_MM_DD_HH_MM_SS/
    ├── audio.mp3          # áudio completo acumulado
    ├── audio_temp.mp3     # áudio da janela de ~5s (sobrescrito durante a gravação)
    ├── transcricao.txt    # transcrição completa
    ├── resumo.txt         # resumo gerado por GPT
    └── titulo.txt         # título definido pelo usuário
```

---

## Tecnologias 
- Python
- Streamlit
- streamlit-webrtc (WebRTC no navegador)
- pydub (manipulação de áudio) + FFmpeg
- OpenAI API (Whisper + GPT)
- python-dotenv (carregamento de variáveis do .env)

---

## Pré-requisitos
- Python 3.9+ (recomendado)
- FFmpeg instalado e disponível no PATH (necessário para o pydub)
- Chave de API da OpenAI

Instalação do FFmpeg:
- macOS (Homebrew): `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt-get update && sudo apt-get install -y ffmpeg`
- Windows (Chocolatey): `choco install ffmpeg`

---

## Instalação 
1. Clone o repositório:
   ```
   git clone https://github.com/<owner>/<repo>.git
   cd <repo>
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   - macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
   Caso não exista um `requirements.txt`, instale manualmente:
   ```
   pip install streamlit streamlit-webrtc pydub openai python-dotenv
   ```

---

## Configuração
Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

O projeto utiliza `python-dotenv` para carregar automaticamente essa variável no runtime.

---

## Execução
Inicie a aplicação Streamlit:
```
streamlit run app.py
```

Acesse no navegador (geralmente):
```
http://localhost:8501
```

Permita o uso do microfone quando solicitado.

---

## Uso
1. Aba “Gravar Reunião”
   - Clique em “Permitir” quando o navegador solicitar acesso ao microfone.
   - Comece a falar. A cada ~5 segundos a transcrição é atualizada e salva.
   - Ao encerrar a fala/abaixar a guia, a sessão é finalizada e os arquivos são salvos em `arquivos/`.

2. Aba “Ver transcrições salvas”
   - Selecione uma reunião pelo timestamp/título.
   - Se não houver título, digite e clique em “Salvar”.
   - O resumo será gerado automaticamente (se ainda não existir) e exibido junto com a transcrição completa.

---

## Personalização
- Idioma da transcrição:
  - Função `transcreve_audio(caminho_audio, language='pt', ...)` — altere `language`.
- Janela de transcrição:
  - Intervalo determinado por `if agora - ultima_trancricao > 5:` — ajuste para mais/menos segundos.
- Modelos OpenAI:
  - Transcrição: `model='whisper-1'`.
  - Resumo (chat): `modelo='gpt-3.5-turbo-1106'` em `chat_openai`.
- Prompt de resumo:
  - Variável `PROMPT` no topo do arquivo — edite regras (limite de caracteres, formato, etc).
- Armazenamento:
  - Pasta base `PASTA_ARQUIVOS` — ajuste o caminho conforme necessidade.

Exemplo de `requirements.txt` sugerido:
```
streamlit>=1.33
streamlit-webrtc>=0.47
pydub>=0.25
openai>=1.0
python-dotenv>=1.0
```

---

## Boas práticas e segurança
- Nunca commit sua chave `OPENAI_API_KEY`.
- Use o arquivo `.env` local e adicione `.env` ao `.gitignore`.
- Se for lidar com dados sensíveis, considere:
  - Criptografia em repouso (por exemplo, transcrições/resumos).
  - Termos e consentimento dos participantes.
  - Políticas de retenção e exclusão de dados.
- Custos: o uso da API da OpenAI é pago por volume (tokens/áudio). Monitore e defina limites.

---

## Solução de problemas
- Microfone não funciona:
  - Verifique permissões do navegador/OS para o site `localhost:8501`.
  - Use HTTPS em produção para WebRTC. Em localhost, HTTP normalmente funciona.
- Erro com pydub/FFmpeg:
  - Certifique-se de que o `ffmpeg` está instalado e acessível no PATH.
- Resumo não é gerado:
  - Verifique se `OPENAI_API_KEY` está definido e válido.
  - Cheque eventuais limites de taxa (rate limit) da OpenAI.
- Latência alta ou transcrição irregular:
  - Reduza o intervalo de chunk (atual > 5s) ou melhore a rede/CPU.
- “arquivos/” não aparece:
  - A pasta é criada automaticamente no primeiro uso. Verifique permissões de escrita no diretório do projeto.

---

## Roadmap
- Exportar resumo/transcrição em PDF/Markdown.
- Marcação de speakers (diarização) e timestamps.
- Marcar ações (to-dos) automaticamente com base no resumo.
- Suporte a idiomas multilíngues com detecção automática.
- Configuração de STUN/TURN customizados para WebRTC em produção.
- Integração com banco de dados (SQLite/PostgreSQL) para histórico persistente.
- Autenticação de usuários.

---

## Contribuição
Contribuições são bem-vindas!
- Abra uma issue descrevendo a melhoria/bug.
- Faça um fork, crie uma branch e envie um PR com uma descrição clara.

Padrão sugerido de branch:
- `feat/<descrição>`
- `fix/<descrição>`
- `chore/<descrição>`

---

## Autor
- @yagosamu
