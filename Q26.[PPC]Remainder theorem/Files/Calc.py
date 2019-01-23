a = 32134
b = 193127

n = 1584891
m = 3438478

for i in range(m):
	x = n * i + a
	if x % m == b:
		print(x)