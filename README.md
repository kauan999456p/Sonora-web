# Sonora — música, descoberta e Creator Lab

**Player web independente, em português, pronto para GitHub Pages.** O Sonora reúne músicas locais, descoberta de faixas com licença indicada pela fonte, recomendações pessoais e uma oficina de projetos curtos inacabados.

![Sonora](assets/sonora-icon.svg)

## Recursos

### Player musical
- Biblioteca local com importação por botão ou arrastar e soltar.
- Reconhecimento básico de tags ID3 em MP3.
- Player com fila, aleatório, repetir, volume e progresso.
- Favoritos, histórico e playlists.
- Busca online no Jamendo e consulta do ccMixter, com separação entre biblioteca local e resultados online.
- Download de faixas Jamendo somente quando a API informa que o download é permitido.
- Recomendações que usam reproduções, artistas, estilos e favoritos registrados localmente.

### Sonora Creator Lab — Reels inacabados
- 100 rascunhos iniciais e editáveis (não são vídeos prontos nem publicações).
- Criação de novos projetos, pesquisa, filtros por estado e indicador de progresso.
- Campos para título, ideia/legenda e etapa do projeto.
- Anexo e pré-visualização de um vídeo por rascunho.
- **Limite de seleção: 1 GB (1.000.000.000 bytes) por vídeo.**
- Vídeos criptografados em blocos AES-GCM de 8 MiB, sem carregar o arquivo inteiro na memória durante a gravação.
- Barra de progresso durante a criptografia e verificação aproximada do espaço disponível.

> O limite de 1 GB é o máximo aceito pelo Sonora, não uma garantia de que todo navegador terá espaço para armazenar esse tamanho. Cotas do IndexedDB, espaço livre e memória variam por dispositivo. A pré-visualização de vídeos muito grandes pode exigir bastante memória porque o navegador precisa remontar os blocos descriptografados para reproduzir.

### Experiência e privacidade
- Tutorial animado com o mascote Lumi para quem está começando.
- Conta local no navegador com derivação de chave PBKDF2-SHA-256 e cofre AES-GCM.
- IndexedDB para guardar preferências, biblioteca e mídias cifradas.
- PWA com cache dos arquivos estáticos para reabrir a interface offline.
- Layout responsivo para computador, tablet e celular.

## Publicar no GitHub Pages

1. Crie um repositório no GitHub, por exemplo `sonora`.
2. Extraia este projeto e envie **o conteúdo desta pasta para a raiz** do repositório (o `index.html` precisa ficar na raiz).
3. Faça push para a branch `main`.
4. Abra **Settings → Pages**.
5. Em **Build and deployment**, selecione **GitHub Actions**.
6. O workflow `.github/workflows/pages.yml` publica o site automaticamente após o push.

O site é estático: não precisa de Node.js, banco de dados ou servidor próprio para publicar.

## Executar localmente no Windows

1. Instale Python 3, caso ainda não esteja instalado: https://www.python.org/downloads/
2. Extraia o projeto.
3. Dê dois cliques em `iniciar.bat`.
4. O Sonora abrirá em `http://127.0.0.1:8765` (ou outra porta livre próxima).
5. Deixe a janela do terminal aberta enquanto usa o app. Pressione `Ctrl+C` nela para encerrar.

Também é possível usar uma extensão de servidor local no VS Code.

## Segurança e limites conhecidos

- A conta é local ao navegador. Não existe login compartilhado entre dispositivos, sincronização online, recuperação de senha ou painel de administração.
- A senha não é guardada em texto puro. Se esquecer a senha, os dados criptografados não poderão ser recuperados.
- A criptografia local não protege contra malware, extensões maliciosas ou acesso ao navegador já desbloqueado.
- Os arquivos importados permanecem no dispositivo; não são enviados ao GitHub.
- Não publique chaves privadas, tokens ou segredos neste repositório.
- O Jamendo vem com um identificador público de demonstração (`709fa152`). Para uso contínuo, configure seu próprio `client_id` nas Preferências e confira as regras atuais da API.
- A consulta ao ccMixter pode depender de CORS e abre a página original para reprodução e conferência da licença.
- O player não extrai áudio ou vídeo do YouTube nem do Spotify.
- O Creator Lab ainda não oferece timeline multipista, corte, transições, legendas automáticas ou exportação final de Reels.

## Estrutura

```text
SonoraPlayer_Web/
├── .github/workflows/pages.yml
├── assets/sonora-icon.svg
├── docs/SECURITY.md
├── docs/ROADMAP.md
├── index.html
├── app.js
├── styles.css
├── reels.css
├── manifest.webmanifest
├── service-worker.js
├── local_server.py
└── iniciar.bat
```

## Desenvolvimento

- HTML, CSS e JavaScript puro; sem etapa de build.
- Para verificar sintaxe do JavaScript: `node --check app.js`.
- Para testar no navegador, execute `iniciar.bat` e acesse o endereço local.
- Pull requests são bem-vindos. Consulte `CONTRIBUTING.md`.

## Licença

Projeto distribuído sob a licença MIT. Catálogos, marcas e conteúdos externos continuam sujeitos às licenças e aos termos de seus respectivos titulares.


## Versão local

O banner no topo do site oferece o download da edição local em `downloads/Sonora_Local_v1.1.0.zip`. Ela roda no computador com Python 3, sem depender do GitHub Pages. Recursos de catálogo online continuam precisando de conexão com a internet.
