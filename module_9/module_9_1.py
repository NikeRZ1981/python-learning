s = input()
for i in range(10):
    if str(i) in s:
        print('Цифра')
        s = ''
        break
if s:
    print('Цифр нет')
