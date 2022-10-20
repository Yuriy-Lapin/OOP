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
