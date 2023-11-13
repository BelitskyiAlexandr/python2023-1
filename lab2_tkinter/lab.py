import tkinter as tk
from tkinter import messagebox

class StudentInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторна робота 2")

        # Додати елементи до вікна
        self.label_student_info = tk.Label(root, text="Беліцький Олександр КП-01\nПЗКС \nКПІ")
        self.label_student_info.pack()

        # Змінні для збереження стилів
        self.default_style = {'background': 'lightgray', 'foreground': 'black'}
        self.alt_style = {'background': 'black', 'foreground': 'white'}

        # Кнопка-перемикач для зміни кольорового рішення
        self.style_button = tk.Button(root, text="Змінити стиль", command=self.toggle_style)
        self.style_button.pack()


        self.label_task1 = tk.Label(root, text="\nЗавдання 1\nОднакові слова в рядках")
        self.label_task1.pack()

        self.label_sentence1 = tk.Label(root, text="Речення 1:")
        self.label_sentence1.pack()

        self.entry_sentence1 = tk.Entry(root, width=50)
        self.entry_sentence1.pack()

        self.label_sentence2 = tk.Label(root, text="Речення 2:")
        self.label_sentence2.pack()

        self.entry_sentence2 = tk.Entry(root, width=50)
        self.entry_sentence2.pack()

        self.button_count = tk.Button(root, text="Лічильник слів", command=self.count_matching_words)
        self.button_count.pack(pady=10)


        self.label_task2 = tk.Label(root, text="\nЗавдання 2")
        self.label_task2.pack()

        self.label_sequences = tk.Label(root, text="Округлення до сотих в послідовності символів")
        self.label_sequences.pack()

        self.entry_sequences = tk.Entry(root, width=50)
        self.entry_sequences.pack()

        self.button_trim_numbers = tk.Button(root, text="Обрізати числа", command=self.trim_numbers)
        self.button_trim_numbers.pack(pady=10)


        self.label_task3 = tk.Label(root, text="\nЗавдання 3")
        self.label_task3.pack()

        self.label_sentence3 = tk.Label(root, text="Добуток двох натуральних чисел всередині рядка")
        self.label_sentence3.pack()

        self.entry_sentence3 = tk.Entry(self.root, width=40)
        self.entry_sentence3.pack()

        self.button_process = tk.Button(self.root, text="Обробити рядок", command=self.process_string)
        self.button_process.pack(pady=10)


    def count_matching_words(self):
        # Отримати речення від користувача
        sentence1 = self.entry_sentence1.get()
        sentence2 = self.entry_sentence2.get()

        # Розділити речення на слова
        words1 = set(sentence1.split())
        words2 = set(sentence2.split())

        # Знайти спільні слова
        matching_words = words1.intersection(words2)

        # Показати результат в спливаючому вікні
        messagebox.showinfo("Результат", f"Кількість спільних слів: {len(matching_words)}")


    def trim_numbers(self):
        input_string = self.entry_sequences.get()

        # Розділити рядок на слова
        words = input_string.split()

        # Обробити кожне слово
        for i in range(len(words)):
            word = words[i]
            # Спробувати конвертувати слово в число
            try:
                num = float(word)
                # Якщо це число, обрізати його до двох значущих цифр після коми
                words[i] = "{:.2f}".format(num)
            except ValueError:
                # Якщо не вдалося конвертувати в число, залишити як є
                pass

       # Скласти змінений рядок
        trimmed_string = ' '.join(words)
        messagebox.showinfo("Результат", f"Обрізані числа: {trimmed_string}")

    
    def process_string(self):
        input_string = self.entry_sentence1.get()
        result_string = self.replace_products(input_string)
        messagebox.showinfo("Результат", f"Результат обробки: {result_string}")

    def replace_products(self, input_string):
        words = list(input_string)

        i = 0
        while i <= len(words) - 2:
            if words[i + 1] == '*' and words[i].isdigit() and words[i + 2].isdigit():
                product_result = str(int(words[i]) * int(words[i + 2]))
                words[i] = product_result
                words.pop(i + 1)
                words.pop(i + 1)
            else:
                i += 1
        #Вивід через цикл, бо інакше з'являться непотрібні пробіли
        result_string = ''.join(str(i) for i in words)
        return result_string


    def toggle_style(self):
        # Зміна стилю елементів при натисканні кнопки
        current_style = self.alt_style if self.style_button['text'] == 'Змінити стиль' else self.default_style
        self.root.configure(background=current_style['background'])
        self.label_student_info.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_task1.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_task2.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_task3.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_sentence1.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_sentence2.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_sequences.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.label_sentence3.configure(background=current_style['background'], foreground=current_style['foreground'])
        self.style_button['text'] = 'Змінити стиль' if current_style == self.default_style else 'Скинути стиль'

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentInfoApp(root)
    root.mainloop()
