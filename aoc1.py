file = open('aoc.txt', 'r')
num = file.readlines()

for i in range(len(num)):
	for j in range(len(num)):
		if (int(num[i].strip()) + int(num[j].strip()))==2020:
			print(int(num[i].strip())*int(num[j].strip()))


for i in range(len(num)):
	for j in range(len(num)):
		for k in range(len(num)):
			if (int(num[i].strip()) + int(num[j].strip())+int(num[k].strip()))==2020:
				print(int(num[i].strip())*int(num[j].strip())*int(num[k].strip()))
				raise KeyboardInterrupt


