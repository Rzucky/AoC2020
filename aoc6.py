#file = open('tepor.txt', 'r')
file = open('aoc6.txt', 'r')

counter = 0

lista = []
lista1 = ''
for lines in file:
	if lines == '\n':
		#print(lista)
		#print(len(lista))
		counter += len(lista)
		lista = []
		#lista1 = ''

	lista1 += lines.strip()

	for i in lista1:
		if i not in lista:
			lista.append(i)
	lista1 = ''

print(counter)
file.close()

file = open('aoc6.txt', 'r')

sett = set()
new_group = True
counter = 0
for lines in file:
	if lines == '\n':
		counter += len(sett)
		sett.clear()
		new_group = True
	else:
		if new_group:
			sett.update((c for c in lines.strip()))
			new_group = False
		else:
			sett.intersection_update((c for c in lines.strip()))
if lines.strip() != '': counter += len(sett)
print(counter)