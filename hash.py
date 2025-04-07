import hashlib

mensagem = input("Digite a mensagem para gerar o hash: ")

hash_sha256 = hashlib.sha256(mensagem.encode()).hexdigest()
hash_md5 = hashlib.md5(mensagem.encode()).hexdigest()

print("\n SHA-256:", hash_sha256)
print("MD5:", hash_md5)
