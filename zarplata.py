z = 20000
x = 20000
c = int(input('Дни в месяц:'))
v = int(input('Рабочие дни:'))
b = int(input('Премии:'))
n = 13
m = int(input('Удержания:'))
zp = (z/x * c + b) * ((100 - n)/100) - m

print(zp)
