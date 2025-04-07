from cryptography.fernet import Fernet

# Geração da chave
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Entrada do usuário
mensagem = input("Digite a mensagem a ser criptografada: ")

# Criptografando
criptografada = fernet.encrypt(mensagem.encode())
descriptografada = fernet.decrypt(criptografada).decode()

print("\n🔑 Chave:", chave.decode())
print("🔒 Mensagem Criptografada:", criptografada)
print("🔓 Mensagem Descriptografada:", descriptografada)