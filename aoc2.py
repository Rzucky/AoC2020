file = open('aoc2.txt', 'r')
num = file.readlines()

counter = 0
for line in num:
	lines = line.split(' ')
	key = lines[0].split('-')
	n = int(key[0])
	m = int(key[1])
	key = lines[1].strip(':')	
	stri = lines[2].strip()
	temp = 0
	for i in range(len(stri)):
		if key == stri[i]:
			temp += 1

	if temp >= n and temp <= m:
		counter += 1

print(counter)

counter = 0
for line in num:
	lines = line.split(' ')
	key = lines[0].split('-')
	n = int(key[0]) - 1
	m = int(key[1]) - 1
	key = lines[1].strip(':')	
	stri = lines[2].strip()
	temp = 0

	if stri[n] == key:
		temp += 1
	if stri[m] == key:
		temp += 1

	if temp == 1:
		counter += 1

print(counter)

	
