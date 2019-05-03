file = open('foo.txt', 'r')
second = open('stud2.txt', 'r')

n = 0
m = 0
for line in file:
    n += 1
for line in second:
    m += 1

if m == n:
    print("ATTENTION : Les deux fichiers ont le même nombre de lignes")
else:
    print("Les deux fichiers n'ont pas le même nombre de lignes")

str_file = str(file)
str_second = str(second)

count1 = 0
count2 = 0
for word in str_file:
    count1 += 1
for word in str_second:
    count1 += 1
diff = count2 - count1
print("Les fichiers ont", diff, "mots de différence.")


packed_file = str_file.replace(' ', '')
packed_second = str_second.replace(' ', '')

