from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Entrada da mensagem
mensagem = input("Digite a mensagem a ser criptografada: ").encode()

# Geração das chaves
chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
chave_publica = chave_privada.public_key()

# Criptografando com a chave pública
criptografada = chave_publica.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Descriptografando com a chave privada
descriptografada = chave_privada.decrypt(
    criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\n🔒 Mensagem Criptografada:", criptografada)
print("🔓 Mensagem Descriptografada:", descriptografada.decode())
