# Основи програамування на Python

## Тема: Основні конструкції в Python

### Мета: Навчитись працювати з основними типами даних та функціями в Пайтон 3

---

### Виконання роботи

- Я трошки Попракитикуйтесь з простими змінними, списками `list`, наборами `set` та словниками `dict`:

```python
String = 'text'
Integer = 1
List = ['a', 1, 1.25, 'Слово']
Dict = {'a': 'Слово', 'b': 1}
Set = ('a', 'c', 'b',)

print(f' це рядок \t->\t {String}')
print(f' це ціле число \t->\t {Integer}')
print(f' це список \t->\t {List}')
print(f' це словник \t->\t {Dict}')
print(f' це сет \t->\t {Set}')
```

```
 це рядок   ->	 text
 це ціле число 	->	 1
 це список 	->	 ['a', 1, 1.25, 'Слово']
 це словник 	->	 {'a': 'Слово', 'b': 1}
 це сет 	->	 ('a', 'c', 'b')
```

- Тут я просто вивів дельлька вбудованих констант:

```python
print(True)
print(False)
print(None)
print(NotImplemented)
```

```
True
False
None
NotImplemented
```

- Експерименти з вбудованими і не тільки функціями:

```python
# print(globals())

import base64
print(base64.b64decode('cHJpbnQoJ3Rlc3RpbmcgZW5jcnlwdGVkIGNvZGUnKQ=='))
exec(base64.b64decode('cHJpbnQoJ3Rlc3RpbmcgZW5jcnlwdGVkIGNvZGUnKQ=='))

print(hash('LOL'))

dict1 = [1, 2, 3]
dict2 = ['ван', 'ту', 'срі']
print(zip(dict1, dict2))
for item in zip(dict1, dict2):
    print(item)
```

```
b"print('testing encrypted code')"
testing encrypted code
-2974910610774903325
<zip object at 0x000001A3FF1F2740>
(1, 'ван')
(2, 'ту')
(3, 'срі')
```

- З циклами я трошки знайомий тому я зробив простеньку програмку яка від 1000 віднімає 7 поки не дійде до 0:

```python
# 1000 - 7

num = 1000
while num > 0:
    print(f'{num} - 7 = {num-7}')
    num-=7
```

```
1000 - 7 = 993
993 - 7 = 986
986 - 7 = 979
979 - 7 = 972
972 - 7 = 965
965 - 7 = 958
958 - 7 = 951
951 - 7 = 944
944 - 7 = 937
937 - 7 = 930
930 - 7 = 923
923 - 7 = 916
916 - 7 = 909
909 - 7 = 902
902 - 7 = 895
895 - 7 = 888
888 - 7 = 881
881 - 7 = 874
874 - 7 = 867
867 - 7 = 860
860 - 7 = 853
853 - 7 = 846
846 - 7 = 839
839 - 7 = 832
832 - 7 = 825
...
27 - 7 = 20
20 - 7 = 13
13 - 7 = 6
6 - 7 = -1
```

- Я спробував зробити розгалуження за новою конструкцією match-case:

```py
A = True
print("Значить А=True" if A else "Значить А=False ")

choise = input(">>> ")
match choise:
    case '1':
        print('ви вибрали 1')

    case 'test':
        print('ви вибрали test')

    case _:
        print('ви нічого не вибрали')
```

```
Значить А=True
ви вибрали test
```

- Я пробував зловити помилку, але помилка зловила мене

```py
try:
    def true():
        return False
    def false():
        return True

    print(f'Це тру - {true()}')
    print(f'Це фолс - {false()}')

except:
    print('еррор')
finally:
    print('нема еррора')
```

```
Це тру - False
Це фолс - True
нема еррора
```

- Написав свій код з контекст-менеджером. Він виводить по 1 рядочку з файлу TEST.md у консоль:

```py
with open("TEST.md", "r") as f:
    for line in f:
        print(line)
```

```
test line 1

test line 2

line 3
```

- Познайомився з lambda-функціями. VS Code постійно виправляв мою лямбда функцію на просту :grin:

```py
sqrt = lambda x: x**0.5

print("Це просто функція:", sqrt)
print(f'квадратний корінь числа 25 = {sqrt(25)}')
```

```
Це просто функція: <function <lambda> at 0x000001A381135000>
квадратний корінь числа 25 = 5.0
```

### Висновок:

## Я навчився працювати з основними типами даних та функціями в Пайтон 3. трішки дослідив роботу основних конструкцій в Python.
