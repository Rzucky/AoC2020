#file = open('tepor.txt', 'r')
file = open('aoc4.txt', 'r')
counter = 0

lista = ''
for lines in file:
	if lines == '\n':
		lista = ''

	lista += lines
	
	if 'byr:' in lista and 'iyr:' in lista and 'eyr:' in lista and 'hgt:' in lista and 'hcl:' in lista and 'ecl:' in lista and 'pid:' in lista:
		tempo = 0
		i = lista.find('byr:') + 4
		tmp = int(lista[i:i+4])
		print(tmp)
		if tmp >= 1920 and tmp <= 2002:
			tempo += 1

		i = lista.find('iyr:') + 4
		tmp = int(lista[i:i+4])
		print(tmp)
		if tmp >= 2010 and tmp <= 2020:
			tempo += 1

		i = lista.find('eyr:') + 4
		tmp = int(lista[i:i+4])
		print(tmp)
		if tmp >= 2020 and tmp <= 2030:
			tempo += 1

		i = lista.find('hgt:') + 4
		tmp = lista[i:i+6]
		print(tmp)
		if tmp[3] == 'c' and tmp[4] == 'm':
			broj = int(tmp[:3])
			if broj >= 150 and broj <= 193:
				tempo += 1

		if tmp[2] == 'i' and tmp[3] == 'n':
			broj = int(tmp[:2])
			if broj >= 59 and broj <= 76:
				tempo += 1

		i = lista.find('hcl:') + 5
		tmp = lista[i:i+7]
		print(tmp)
		if lista[i-1] == '#':
			tempo2 = 0
			for i in tmp:
				if i >= 'a' and i <= 'f':
					tempo2 += 1
				elif i >= '0' and i <= '9':
					tempo2 += 1
		if tempo2 == 6:
			tempo += 1

		i = lista.find('ecl:') + 4
		tmp = lista[i:i+3]
		print(tmp)
		if tmp == 'amb' or tmp == 'blu' or tmp == 'brn' or  tmp == 'gry' or tmp == 'grn' or tmp == 'hzl' or tmp == 'oth':
			tempo += 1

		i = lista.find('pid:') + 4
		tmp = lista[i:i+10]
		tempo2 = 0
		print(tmp)
		for i in tmp:
			if i >= '0' and i <= '9':
				tempo2 += 1

		if tempo2 == 9:
			tempo += 1
		if 'cid:' in lista:
			lista = lista.replace('cid:', 'cid')

		if tempo == 7 and lista.count(':') == 7:
			counter += 1

		print(lista)
		lista = ''



print(counter)



# 	byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid
