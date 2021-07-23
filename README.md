# Login e senha: 
## Criando um processo de login e senha em python e analisando tipos de hash.

###Foi colocado uma opção de cadastro caso o usuário não tivesse o login, pois tinha como foco acompanhar o comportamento de login e cadastro. Primeiro, ocorre a separação dos caracteres digitados no campo password. Após separação, ocorre a criptografia de cada caracter com hash md5 e junta-se todos os hashs de caracteres e converte em um hash único, assim salvando no banco de dados ou, como nesse caso, arquivo de texto.