import re
with open ("prepoinsulin-seq.txt", "r") as arquivo:
    conteudo = arquivo.read()

insulina = re.sub(r"[^a-z]","",conteudo)

print(insulina)

tamanho = len(insulina)
print(tamanho)