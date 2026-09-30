# Python version: 3.x
# Coding: utf-8

import re
with open ("prepoinsulin-seq.txt", "r") as arquivo:
    conteudo = arquivo.read()

preproInsulin = re.sub(r"[^a-z]","",conteudo)

print(preproInsulin)

tamanho = len(preproInsulin)
print(tamanho)

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcghlvealylvcgergffytpktr"
cInsulin = "reaedlqvgqvelgggpgagslqplalegslqkr"
aInsulin = "giveqcctsicslyqlenycn"

insulin = bInsulin + aInsulin
print(insulin)


print("A Seguir será apresentada a sequencia da pro-insulina humana: "+preproInsulin)

#passo 4 concatenação com +
print('A cadeia A da insulina é '+aInsulin)

#passo 5 concatenação com virgula
print("A cadeia B da insulina é",bInsulin)