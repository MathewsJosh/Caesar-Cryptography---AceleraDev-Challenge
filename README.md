# Caesar-Cryptography---AceleraDev-Challenge
O código faz tudo o que o enunciado solicita.

Está separado em 4 arquivos:

index.py: define as variáveis iniciais e realiza as chamadas de funções
runRequest.py: faz a request GET para receber os dados a serem tratados e salvá-los no arquivo 'answer.json'
runDecrypt.py: recebe a mensagem e número de casas definidos para decriptar a mensagem
runPost.py: insere a mensagem decriptografada e o resumo Sha1 no arquivo 'answer.json' e realiza o envio da mensagem através do "POST";
O resultado será mostrado no console, após a execução correra to programa: Resultado do Programa

Para que o programa rode por completo, é necessário setar o token na linha 7 do arquivo index.py:

token =  'valor_do_token'
** Não esqueça que para rodar o programa, é necessário adicionar a biblioteca 'requests' **
