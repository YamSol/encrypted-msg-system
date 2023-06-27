def msg_encrypt(mensagem, pub_key):

    ## TODO: Converter para (base64/hexadecimal/binario)
  
    # transformar mensagem em numero
    int_msgs = []
    for char in mensagem:
        int_msgs.append(ord(char))

    # encriptar cada numero da mensagem
    e_int_msg = []
    for msg in int_msgs:
        e_int_msg.append(int_encrypt(msg, pub_key))

    return e_int_msg


def msg_decrypt(e_mensagem, priv_key):

    ## TODO: Reconverter para array de inteiros

    # descriptografa cada numero da e_mensagem
    d_int_msg = []
    for num in e_mensagem:
        d_int_msg.append(int_decrypt(num, priv_key))

    # transformar numeros na mensagem
    msg = ""
    for num in d_int_msg:
        msg += chr(num)

    return  msg

def int_encrypt(msg, pub_key):
    return pow(msg,pub_key['e'],pub_key['n'])

def int_decrypt(msg, priv_key):
    return pow(msg,priv_key['d'], priv_key['n'])

if(__name__ == "__main__"):
    __msg = "MSG"
    __pub_key = {'e':769,'n':2047}
    __priv_key = {'d':1649,'n':2047}

    print("The message is: ", __msg)

    __encrypted_message = msg_encrypt(__msg, __pub_key)
    print("Encrypted msg: ", __encrypted_message)

    __decrypted_message = msg_decrypt(__encrypted_message, __priv_key)
    print("The message is: ", __decrypted_message)