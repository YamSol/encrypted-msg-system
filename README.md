# encrypted-msg-system
Sistema de envio e recebimento de mensagens criptografadas. Sistema de criptografia RSA implementado manualmente.


## No terminal
Para executar o comando via terminal:
1. abra a pasta /key_generation
2. Execute o comando:
    - Para Criptografar:
        ```
       python -c "import MsgHandler; print(MsgHandler.msg_encrypt('<SUA MENSAGEM>',{'e':769,'n':2047}))"
        ```
    - Para Descriptografar:
        ```
       python -c "import MsgHandler; print(MsgHandler.msg_decrypt('<SUA MENSAGEM>',{'e':1649,'n':2047}))"
        ``` 
