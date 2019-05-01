file = open('foo.txt', 'r')
n = 0
for line in file:
    n += 1

print("Le fichier fait ", n, "lignes")