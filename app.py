file = open('foo.txt', 'r')
second = open('stud2.txt', 'r')

n = 0
for line in file:
    n += 1

m = 0
for line in second:
    m += 1

if m == n:
    print("ATTENTION : Les deux fichiers ont le même nombre de lignes")
else:
    print("Les deux fichiers n'ont pas le même nombre de lignes")