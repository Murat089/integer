k = int(input('Обхват по бьюсту:'))

if (k >= 80) and (k < 90):
	print('5 баллов')

m = int(input('По бедрам:'))
if (m >= 80) and (m < 90):
	print('5 баллов')

n = int(input('По талии:'))
if (n >= 60) and (n < 70):
	print('5 баллов')

t = int(input('Рост:'))
if (t >= 170) and (t < 200):
	print('5 баллов')

p = int(input('Вес:'))
if (p >= 60) and (p < 80):
	print('5 баллов')
l = ((k + m + t)/(n*2 + p))
print(l)
