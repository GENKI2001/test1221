import random

class Initial:
    def __init__(self) -> None:
        self.value = random.random()

class Second(Initial):
    pass

initial = Initial()
second = Second()
print(initial.value)
print(second.value, "こんにちは")

print(initial.value)
print("はーいじゃないです")
