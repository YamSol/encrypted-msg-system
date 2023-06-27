from key_generation.gerar_par_de_chaves import gerar_keys
from key_generation.MsgHandler import msg_encrypt, msg_decrypt

# Titulo
print('*'*15, "Sistema de Mensagens", '*'*15)

# Gerando chaves
a, b = gerar_keys()
pub_key = {'e': a[0], 'n': a[1]}
priv_key = {'d': b[0], 'n': b[1]}

# Recebendo mensagem
message = input("Digite sua mensagem: ")

# Encriptando mensagem
encrypted_menssage = msg_encrypt(message,pub_key)
print(encrypted_menssage)

# Desencriptando mensagem
decrypted_menssage = msg_decrypt(encrypted_menssage,priv_key)
print(decrypted_menssage)
