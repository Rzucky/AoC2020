from collections import Counter

file = open('tepor.txt', 'r')
#file = open('aoc8.txt', 'r')

lista = []

for line in file:
	lista.append(line.strip())


#print(lista)

posjeceni = []
for k in range(len(lista)):
	posjeceni.append(0)

counter = 0
index = 0
for k in range(len(lista)):
	line = lista[index]

	if posjeceni[index] == 1:
		print('ponovilo se')
		break

	posjeceni[index] = 1

	naredba = line[:3]
	#print(naredba)
	number = line[4:]
	#print(number)

	if naredba == 'acc':
		counter += int(number)
		index += 1

	elif naredba == 'nop':
		index += 1

	elif naredba == 'jmp':
		index += int(number)


	#print(index)
print(f'accumulator in a broken one is {counter}')



posjeceni = []
for k in range(len(lista)):
	posjeceni.append(0)


counter = 0
index = 0
kant = 0
# kant = lista.count('nop')
# print(kant)
# kant += lista.count('jmp')
#print(kant)
liss = []
for k in range(len(lista)):
	line = lista[k]
	naredba = line[:3]
	liss.append(naredba)

z = Counter(liss)
print(z)


nova = []
aj = 0
for k in range(len(lista)):
	line = lista[k]
	if 'nop' in line or 'jmp' in line:
		nova.append(aj) 

	aj += 1

izbacilo = False

for ja in range(kant):
	
	search = nova[ja]
	line = lista[search]
	if 'nop' in line:
		line = line.replace('nop', 'jmp')

	elif 'jmp' in line:
		line = line.replace('jmp', 'nop')
	

	for k in range(len(lista)):
		line = lista[index]

		if posjeceni[index] == 1:
			print('ponovilo se')
			izbacilo = True
			break

		posjeceni[index] = 1

		naredba = line[:3]
		#print(naredba)
		number = line[4:]
		#print(number)

		if naredba == 'acc':
			counter += int(number)
			index += 1

		elif naredba == 'nop':
			index += 1

		elif naredba == 'jmp':
			index += int(number)

	if(not izbacilo):
		print(counter)