# Звіт до роботи Lab5

## Тема: Тестування

---

### Виконання роботи:

### Перевірка assert

- Я зробив простеньку програмку з тестами assert:

```py
year = input('Введіть свій рік народження -> ')
assert year.isdigit(), f'Ви впевнені що це "{year}" число ?)'
age = 2022 - int(year)

pib = input(
    'Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> ')

list = pib.split()
for item in list:
    assert item.istitle(), f'Схоже ви допустились помилки у слові "{item}"'

print(f'Вітаю {pib}, цього року вам буде (або вже є) {age} рочків )))')
```

Ось що буде виводитись, якщо написати все правильно:

```
Введіть свій рік народження -> 2003
Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> Лапін Юрій Андрійович
Вітаю Лапін Юрій Андрійович, цього року вам буде (або вже є) 19 рочків )))
```

Якщо ввести не число (типу int) то перша перевірка видасть таку помилку:

```
Введіть свій рік народження -> текст)
AssertionError: Ви впевнені що це "текст)" число ?)
```

Якщо ввести правильно число, але ввести слово з маленької літери:

```
Введіть свій рік народження -> 1991
Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> україна
AssertionError: Схоже ви допустились помилки у слові "україна"
```

<span style='color: rgba(255, 255, 255, 0.2)'>Україна пишеться з великої<span>

- Я ввів код з прикладу і трошки його модифікував, для того щоб гарний вивід був. Ну і запхав це все в блоки трай/ексцепт, бо без цього прграма зупиняє роботу при ініціалізації деяких об'єктів, а я хотів красивий вивід )

```
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник",
                        "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"

        self.type = type
        self.length = length

    def print_figure(self):
        return f'Фігура {self.type} з cтороною {self.length}'


try:
    figure1 = Figure("квадрат", 2)
    print(f'Фігура 1 - {figure1.print_figure()}')
except AssertionError as err:
    print(f'Фігура 1 - {err}')

try:
    figure2 = Figure("прямокутник", 0)
    print(f'Фігура 2 - {figure2.print_figure()}')
except AssertionError as err:
    print(f'Фігура 2 - {err}')

try:
    figure3 = Figure("трикутник", -42)
    print(f'Фігура 3 - {figure3.print_figure()}')
except AssertionError as err:
    print(f'Фігура 3 - {err}')

try:
    figure4 = Figure("трикутник", 15)
    print(f'Фігура 4 - {figure4.print_figure()}')
except AssertionError as err:
    print(f'Фігура 4 - {err}')

try:
    figure5 = Figure("трапеція", 100)
    print(f'Фігура 5 - {figure5.print_figure()}')
except AssertionError as err:
    print(f'Фігура 5 - {err}')

```

Ось що виводитья:

```
Фігура 1 - Фігура квадрат з cтороною 2
Фігура 2 - Довжина має бути більшою за 0!
Фігура 3 - Довжина має бути більшою за 0!
Фігура 4 - Фігура трикутник з cтороною 15
Фігура 5 - Дозволені фігури: квадрат, прямокутник, трикутник
```

- Тут я вже не зробив гарний вивід, але най буде)

```
class Name:
    def __init__(self, name, hobby='') -> None:
        if name not in ["Богдан", "Юрій", "Анонім"]:
            raise ValueError("Дозволені імена: Богдан, Анонім")
        if hobby == '':
            raise ValueError("Хобі не може бути пустим")

        self.name = name
        self.hobby = hobby


a = Name("Юрій", "Їсти, спати, писати код, дивитись аніме")
b = Name("Юрій")
```

тут видно що при ініціалізації `а` все норм, але при анаціалізації `b` видає помилку, бо хобі не вказане

```
Traceback (most recent call last):
  File "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\testing3.py", line 13, in <module>
    b = Name("Юрій")
  File "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\testing3.py", line 6, in __init__
    raise ValueError("Хобі не може бути пустим")
ValueError: Хобі не може бути пустим
```

## Юніт тести

- Я ввів код і запустив, поки не дуже зрозуміло як це все працює, але ось що получилось:

```
======================================================================
ERROR: setUpClass (__main__.TestFigure)
----------------------------------------------------------------------
TypeError: TestFigure.setUpClass() missing 1 required positional argument: 'cls'

----------------------------------------------------------------------
Ran 0 tests in 0.000s

FAILED (errors=1)
```

- Окей, я розібрався чому помилка була, я просто забрав параметр cls з методу setUpClass і все запрацювало )

app.py

```py
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    COLORS = ["red", "green", "blue"]

    def __init__(self, type, length, color='0') -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        assert color in self.COLORS, "Дозволені кольори: red, green, blue"
        self.type = type
        self.length = length
        self.color = color

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type  # робимо помилку

    @property
    def get_figure_color(self):
        return self.color
```

Test_app.py

```py
import unittest
from random import choice, randint

from app import Figure  # назва файлу з нашим класом повинна бути app.py


class TestFigure(unittest.TestCase):
    def setUpClass():
        """Виконається лише раз на початку тестів
        """
        pass

    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.color = choice(Figure.COLORS)
        self.obj = Figure(self.figure, self.length, self.color)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(
            f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type,
                         "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")

    def test_figure_color(self):
        self.assertEqual(self.color, self.obj.get_figure_color,
                         "Властивість get_figure_length повертає непривильний колір!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError
            Figure("коло", 1)


if __name__ == '__main__':
    # unittest.main(verbosity=2) щоб був більш детальний вивід
    unittest.main(verbosity=2)

```

І ось що вивелось у консоль при запуску тестів:

```
test_figure_color (__main__.TestFigure) ... ok
test_figure_lengh (__main__.TestFigure) ... FAIL
test_figure_type (__main__.TestFigure) ... Тестуємо вивід, має бути: прямокутник == прямокутник
ok
test_obj (__main__.TestFigure) ... ok

======================================================================
FAIL: test_figure_lengh (__main__.TestFigure)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\Test_app.py", line 33, in test_figure_lengh
    self.assertEqual(self.length, self.obj.get_figure_length,
AssertionError: 5 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```

## Юніт тести з використання бібліотеки PyTest

- Я створив віртуальне середовище та інсталював туди бібліотеку `PyTest`
  До арр.ру додав таку функцію:

```py
def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    len = 4
    col = 'blue'

    triangle = Figure(fig, len, col)
    assert triangle.type == fig, f"Фігура має бути {fig}"
```

Ось що вивів `PyTest`:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: D:\Labs\Labs 3.1\ООП\github\OOP\Lab5
collected 1 item

app.py .              [100%]

================== 1 passed in 0.02s ==================
```

А це вивід вісля запуску `Test_app.py`:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: D:\Labs\Labs 3.1\ООП\github\OOP\Lab5
collected 4 items

Test_app.py .F..   [100%]

================== FAILURES ==================
__________________ TestFigure.test_figure_lengh __________________

self = <Test_app.TestFigure testMethod=test_figure_lengh>

    def test_figure_lengh(self):
>       self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")
E       AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!

Test_app.py:33: AssertionError
================== short test summary info ==================
FAILED Test_app.py::TestFigure::test_figure_lengh - AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!
================== 1 failed, 3 passed in 0.10s ==================
```

## Візуалізація результатів та покриття коду Coverage (pytest-cov)

- Я встановив плагін `PyTest-Cov` та `Coverage`, щоб потестити який з тестів краще тестить )
  Вивід трошки гарніший. В таблиці гарно виглядає, але щось мало інформації про помилку.

```
Name     Stmts   Miss  Cover
----------------------------
app.py      25      5    80%
----------------------------
TOTAL       25      5    80%
```

- Я ввів команду `pipenv run python -m coverage html` і згенерувався крутий сайтик з такою самою таблицею, але виглядає гарніше )

### Висновок:

- :question: Що зроблено в роботі; :wavy_dash: Я навчився проводити тести
- :question: Чи досягнуто мети роботи; :wavy_dash: ну простенькі тести навчився робити, думаю досягнуто
- :question: Які нові знання отримано; :wavy_dash: Отримано знання про тести )
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; :wavy_dash: так )
- :question: Чи вдалося виконати всі завдання; :wavy_dash: думаю так
- :question: Чи виникли складності у виконанні завдання; :wavy_dash: повітряні тривоги
- :question: Чи подобається такий формат здачі роботи (Feedback); :wavy_dash: :sunglasses::+1:
- :question: Побажання для покращення (Suggestions); :wavy_dash: впринцині всьо норм )
