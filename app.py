
# -------------- compte le nombre de lignes -------------- #
ligne = open('foo.txt', 'r')
ligne_deux = open('stud2.txt', 'r')

n = 0
m = 0
for line in ligne:
    n += 1
for line in ligne_deux:
    m += 1

if m == n:
    print("ATTENTION : Les deux fichiers ont le même nombre de lignes")
else:
    print("Les deux fichiers n'ont pas le même nombre de lignes")

# -------------- compte le nombre de mots -------------- #

with open('foo.txt', 'r') as file:
    data = file.read()
with open('stud2.txt', 'r') as file:
    data2 = file.read()

print("Les fichiers comprennent respectivement {} et {} mots".format(len(data.split()), len(data2.split())))

# -------------- Comparaison -------------- #

