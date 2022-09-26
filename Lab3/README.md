# Звіт до роботи Lab3

## Тема: Знайомство з ООП

### Мета: Навчитись працювати з класама та об'єктами

---

### Виконання роботи:

- Я запустив програму з класом:

<details><summary> >>>>>> Python Code <<<<<< </summary>
### Перша програма на ООП

```python

class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self):
        """Class property
        return: повертаємо імя
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"


print("Let's Start!")

names = ("Bohdan", "Marta", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me}
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()}
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

```

</details>

ось що вона вивела мені у консольку:

```
Let's Start!
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000002025595B8E0>
This is object attribute: Bohdan / 1
This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
This is <class 'method'> call: Bohdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000002025595ADD0>
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x0000020255959D20>
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We create 4 names! ??? Why 4?
```

- Відповіді на запитання:

1. Чому коли передаємо значення None створюється обєкт з іменем Anonymous?

   - бо в класі є метод який повертає Anonymous якщо ім'я = none

   ```py
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
   ```

2. Як змінити текст привітання при виклику методу say_hello()? Допишіть цю частину коду.

   - me.say_hello("aaaaaaa") <- можна написати текст у виклик функції. Якщо робити виклик без параметрів то метод поверне "Hello to everyone!"

3. Допишіть функцію в класі яка порахує кількість букв в імені (підказка: використайте функцію len());

   - це було просто:

   ```py
   def name_lenght(self):
        return len(self.name)
   ```

4. Порахуйте кількість імен у списку names та порівняйте із виведеним результатом. Дайте відповідь чому маємо різну кількість імен?

   - Через тиждень пошуків я все ж таки знайшов те 5-е ім'я.<br>
     ![alt text](https://github.com/Yuriy-Lapin/OOP/raw/main/Lab3/pictures/1.png "F")<br>
     У мене є така теорія:<br>
     1. Створюється екземпляр класу з ім'ям `None`
     1. Тоді спрацьовує `MyName.total_names += 1`
     1. Після чого викликається метод `anonymous_user()` який повертає таку підозрілу штуку `cls("Anonymous")`
     1. І тоді вже створюється екземпляр з ім'ям `Anonymous` і його :id: на одиницю білше ніж повинно бути

### Висновок:

- :question: Що зроблено в роботі; :wavy_dash: Трошки розібрались з ООП
- :question: Чи досягнуто мети роботи; :wavy_dash:
- :question: Які нові знання отримано; :wavy_dash: Отримано знання про ООП, класи, методи, `магічні` функцфї, декоратори.
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; :wavy_dash: Вдалось, навіть на 4 запитання знайшлось логічне пояснення
- :question: Чи вдалося виконати всі завдання; :wavy_dash: Взагалі без проблем )
- :question: Чи виникли складності у виконанні завдання; :wavy_dash: Окей, проблеми були, але тільки в 4 запитанні )
- :question: Чи подобається такий формат здачі роботи (Feedback); :wavy_dash: :sunglasses::+1:
- :question: Побажання для покращення (Suggestions); :wavy_dash:

---
