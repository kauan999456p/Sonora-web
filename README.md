# Sonora v1.0 — Player musical online

O Sonora v1.0 é um player web para descobrir, organizar e ouvir músicas online. O projeto é publicado no GitHub Pages e não possui edição desktop/local separada nesta versão.

## Catálogo online

O catálogo usa a API oficial do **Audius** para carregar faixas em alta, pesquisar por música/artista/estilo e reproduzir áudio pelo endpoint oficial de streaming. A aplicação tenta os endpoints públicos oficiais do Audius e mantém a origem da faixa visível.

- Catálogo em alta e pesquisa.
- Categorias musicais para descoberta.
- Reprodução no player integrado, sem baixar/re-hospedar o áudio.
- Link para a página original do artista.
- O app não promete que todas as faixas sejam livres de direitos autorais. Os direitos pertencem aos criadores; reutilização fora do streaming deve seguir a licença/permissões informadas pelo artista.
- As consultas de leitura do Audius normalmente funcionam sem credencial de desenvolvedor; limites podem se aplicar. Uma chave pode ser usada futuramente para elevar a cota, sem colocá-la no código público.

Documentação: https://docs.audius.co/api/

## Recursos do Sonora

- Player com play/pause, faixa anterior/próxima, volume, repetição e aleatório.
- Busca e catálogo online Audius.
- Biblioteca de arquivos que o usuário seleciona no próprio navegador (opcional).
- Arrastar e soltar arquivos de áudio.
- Playlists, favoritos e histórico.
- Recomendações locais baseadas nas reproduções e favoritos.
- Conta local do navegador com senha derivada por PBKDF2 e dados do cofre protegidos por AES-GCM.
- Tutorial interativo com Lumi.
- Área de rascunhos de Reels, com vídeos guardados no armazenamento do navegador.

## Publicar no GitHub Pages

1. Abra **Settings → Pages** no repositório.
2. Em **Build and deployment**, escolha **Deploy from a branch**.
3. Selecione a branch `main` e a pasta `/(root)`.
4. Salve e aguarde a publicação.

O arquivo `index.html` fica na raiz do repositório. O workflow em `.github/workflows/pages.yml`, se presente, pode ser usado para automatizar a publicação.

## Privacidade e armazenamento

O login do Sonora nesta versão é local ao navegador; não é uma conta sincronizada entre dispositivos. Músicas importadas pelo usuário, playlists e preferências não são enviadas ao GitHub. O áudio do catálogo é transmitido diretamente pelo Audius.

## Limitações conhecidas

- A disponibilidade de faixas depende do catálogo e das regras de streaming do Audius.
- Algumas faixas podem deixar de estar disponíveis, ser removidas ou ter restrição regional.
- O navegador precisa de internet para carregar o catálogo e transmitir as músicas.
- O armazenamento de arquivos locais depende da cota que o navegador permite.

## Licença

Consulte o arquivo LICENSE deste repositório para a licença do código. Essa licença não concede direitos sobre as músicas de terceiros disponibilizadas pelo Audius.
