1.
J�nes = '''
   (\_/)
   (o o)
   / | \\
'''

n = int(input("Sisestage j�neste arv (1 kuni 9): "))

if 1 <= n <= 9:
   
    for i in range(n):
        print(J�nes, end=' ')
else:
    print("Vigane sisestus. Sisestage arv vahemikus 1 kuni 9.")

3.
import random

print("Arva �ra arv vahemikus 0 kuni 100. Sul on 10 katset.")

number = random.randint(0, 100)

for i in range(10):
    arvan = int(input("Sisestage oma oletus: "))
   
    if arvan < number:
        print("Peidetud arv on suurem.")
    elif arvan > number:
        print("Peidetud arv on v�iksem.")
    else:
        print(f"Palju �nne, arvasite numbri �ra! See oli number {number}.")
        break
else:
    print(f"Kahjuks kaotasite. Arvati numbrit {number}.")
4.

number = int(input("Sisestage number: "))
tagurpidi_number = 0

while number > 0:
    digit = number % 10
    tagurpidi_number = tagurpidi_number * 10 + number
    number = number // 10

print(vastupidine_number)

5.
number = int(input("Sisestage t�isarv: "))
summa_numbrid = 0
toote_numbrid = 1

while number != 0:
    numbriline = number % 10
    summa_numbrid += number
    toote_numbrid *= number
    number //= 10

print("summa numbrid:", summa_numbrid)
print("Numbrite korrutis:", toote_numbrid)
