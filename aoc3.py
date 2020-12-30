file = open('aoc3.txt', 'r')
#warning, does not work as it should but gives good answer
#watch at your own risk
counter = 0
i = 0
red = file.readline()

print(148*50*53*64*29)	

while(red != '\n'):
	i += 1

	red = file.readline().strip()
	red = file.readline().strip()
	
	if len(red) != 0:
		i = i % len(red)
	
	if(red != '\n'):
		if red[i] == '#':
			counter += 1
			print(counter)






