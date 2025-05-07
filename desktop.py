"""Модуль для """
import tkinter as tk
from logic import kv_ur


class Kvur(tk.Tk):
    """Класс для создания окна"""
    def __init__(self):
        """Инициилизация атрибутов"""
        super().__init__()
        self.title("Калькулятор для решения квадратного уравнения")
        self.geometry("500x500")
        self.init_input()
        self.button = tk.Button(self,
                                text="Рассчитать",
                                font=("Arial, 16"),
                                command=self.calculate)
        self.button.grid(row=4, column=2)

    def init_input(self):
        """Инициилизация атрибутов"""
        self.label_a = tk.Label(self, text="a", font=("Arial", 16))
        self.label_a.grid(row=0, column=0)

        self.input_a = tk.Entry(self)
        self.input_a.grid(row=0, column=1)

        self.label_b = tk.Label(self, text="b", font=("Arial", 16))
        self.label_b.grid(row=1, column=0)

        self.input_b = tk.Entry(self)
        self.input_b.grid(row=1, column=1)

        self.label_c = tk.Label(self, text="c", font=("Arial", 16))
        self.label_c.grid(row=2, column=0)

        self.input_c = tk.Entry(self)
        self.input_c.grid(row=2, column=1)

        self.label = tk.Label(self, text="Результат", font=("Arial", 16))
        self.label.grid(row=1, column=2)
        
        self.response = tk.Label(self, text="", font=("Arial", 16))
        self.response.grid(row=1, column=3)

    def calculate(self):
        """Метод для решения уравнения"""
        a = int(self.input_a.get())
        b = int(self.input_b.get())
        c = int(self.input_c.get())
        result = kv_ur(a, b, c)
        self.response.config(text=result)


if __name__ == "__main__":
    app = Kvur()
    app.mainloop()
