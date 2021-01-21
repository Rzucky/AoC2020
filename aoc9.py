import linecache

file = open('tepor.txt', 'r')
#file = open('aoc9.txt', 'r')

trenutni = []
lista = []
for lines in file:
	lista.append(lines.strip())

#loading preamble
for i in range(1,6):
	line = linecache.getline('tepor.txt', i)
	trenutni.append(line.strip())

print(trenutni)

#the rest of the files
for i in range(5,len(lista)):
	k = int(lista[i].strip())
	
	valid = False
	find = False
	for i in range(5):
		for j in range(5):
			if int(trenutni[i].strip()) + int(trenutni[j].strip()) == k and int(trenutni[i].strip()) != int(trenutni[j].strip()):
				valid = True
				find = True
				break
		if find:
			break

	if not valid:
		break

	trenutni.append(str(k))
	trenutni.pop(0)

print(f'Wrong one is {k}')

find = False
#indexi prvog koje pokusavamo
for i in range(len(lista)):
	trap = []
	trap.append(int(lista[i]))
	#count = int(lista[i])
	count = 0
	index = i+1
	kaj = 0
	while(count < k):
		count += trap[kaj]
		#print(f'count {count}')
		kaj += 1
		#print(kaj)
		#print(f'trap: {trap}')
		if count == k:
			#print(f'trap tocan: {trap}')
			find = True
			break

		trap.append(int(lista[index]))
		index += 1
	if find:
		break

	#print(f'nije uspio za i:  {i}')

print(f'trap tocan za {k}: {trap}')
rez = min(trap) + max(trap)
print(rez)
