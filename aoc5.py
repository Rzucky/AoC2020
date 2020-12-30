#file = open('tepor.txt', 'r')
file = open('aoc5.txt', 'r')

highest = -1
kiki = []
ha = 0

for lines in file:

	lines = lines.strip()
	red = lines[:7]
	seat = lines[7:]

	red = red.replace('B', '1').replace('F', '0')
	seat = seat.replace('R', '1').replace('L', '0')

	decimal = 0
	for digit in red:
		decimal = decimal*2 + int(digit)
	decimal2 = 0
	for digit in seat:
		decimal2 = decimal2*2 + int(digit)

	k = decimal*8+decimal2

	highest = max(k,highest)
	kiki.append(k)

for num in range(40, highest-40):
	if num-1 in kiki and num+1 in kiki and not(num in kiki):
		ha = num
		

print(highest)
print(ha)




