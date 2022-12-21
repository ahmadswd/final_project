def say_hello():
    print("Hello, Ahmad.")

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self, x, y):
        return self.x * self.y

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

if __name__ == "__main__":
    say_hello()
    calc = Calculator(x, y)
    print(f"The result is {calc.add()}")
