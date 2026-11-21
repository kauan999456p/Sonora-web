# Segurança e privacidade

- A conta do Sonora existe apenas no navegador/dispositivo em que foi criada.
- A senha é usada para derivar uma chave via PBKDF2-SHA-256 (310.000 iterações); não é armazenada em texto puro.
- O cofre e os vídeos anexados aos rascunhos são cifrados com AES-GCM antes de serem gravados no IndexedDB.
- Vídeos do Creator Lab são divididos em blocos de 8 MiB; cada bloco recebe um IV aleatório e dados adicionais autenticados que vinculam o bloco ao projeto e à sua posição.
- O limite de 1 GB é um limite de entrada do app, não uma promessa de espaço disponível. A cota efetiva depende do navegador e do dispositivo.
- A cifragem local não protege contra malware, extensões maliciosas, acesso ao perfil do navegador desbloqueado ou perda da senha.
- Não há sincronização remota nem recuperação de senha.
- Não inclua tokens, senhas ou credenciais privadas no repositório público.
- A API do Jamendo usa um identificador público de demonstração. Configure seu próprio identificador e confira as regras atuais do serviço.
