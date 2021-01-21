from collections import Counter

#file = open('tepor.txt', 'r')
file = open('aoc8.txt', 'r')

lista = []

for line in file:
	lista.append(line.strip())

posjeceni = []
for k in range(len(lista)):
	posjeceni.append(0)

counter = 0
index = 0
for k in range(len(lista)):
	line = lista[index]

	#wrong one
	if posjeceni[index] == 1:
		break

	posjeceni[index] = 1

	naredba = line[:3]
	number = line[4:]

	if naredba == 'acc':
		counter += int(number)
		index += 1

	elif naredba == 'nop':
		index += 1

	elif naredba == 'jmp':
		index += int(number)

	if line == 'end':
		break

print(f'Accumulator value before breakign - {counter}')


#temp array to find all nop and jmp
liss = []
for k in range(len(lista)):
	line = lista[k]
	naredba = line[:3]
	liss.append(naredba)

z = Counter(liss)

#counting number of jmp and nop to check each permutation
kant = z['jmp']
kant += z['nop']

nova = []
aj = 0
for k in range(len(lista)):
	line = lista[k]
	if 'nop' in line or 'jmp' in line:
		nova.append(aj) 

	aj += 1


izbacilo = False

for ja in range(kant):

	templista = lista.copy()
	search = nova[ja]
	line = lista[search]
	if 'nop' in line:
		templista[search] = line.replace('nop', 'jmp')

	elif 'jmp' in line:
		templista[search] = line.replace('jmp', 'nop')
	
	posjeceni = []
	for k in range(len(lista)):
		posjeceni.append(0)

	counter = 0
	index = 0

	for k in range(len(lista)):

		line = templista[index]

		#wrong one
		if posjeceni[index] == 1:
			break

		posjeceni[index] = 1

		naredba = line[:3]

		number = line[4:]
		
		if naredba == 'acc':
			counter += int(number)
			index += 1

		elif naredba == 'nop':
			index += 1

		elif naredba == 'jmp':
			index += int(number)

		#reached end of the file
		if line == 'end':
			izbacilo = True
			break

	if(izbacilo):
		break

print(f'Accumulator value after fixing - {counter}')