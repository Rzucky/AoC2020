import linecache

#file = open('tepor.txt', 'r')
file = open('aoc9.txt', 'r')

trenutni = []
lista = []
for lines in file:
	lista.append(lines.strip())

#loading preamble
for i in range(1,26):
	line = linecache.getline('aoc9.txt', i)
	trenutni.append(line.strip())

#print(trenutni)

#the rest of the files
for i in range(25,len(lista)):
	k = int(lista[i].strip())
	
	valid = False
	find = False
	for i in range(25):
		for j in range(25):
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
	cnt = 0
	index = i+1
	a = 0
	#for each index, filling up trap array until it hits either the right number or goes over
	#if it goes over, it tries again with the new starting index
	while(cnt < k):
		cnt += trap[a]
		a += 1
		if cnt == k:
			find = True
			break

		trap.append(int(lista[index]))
		index += 1
	if find:
		break

#print(f'trap tocan za {k}: {trap}')
rez = min(trap) + max(trap)
print(f'Sum of smallest and largest:{rez}')
