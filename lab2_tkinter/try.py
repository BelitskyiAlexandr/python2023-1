import tkinter as tk
from tkinter import messagebox

class StudentInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")
        self.root.geometry("400x200")

        self.label_student_info = tk.Label(self.root, text="Кафедра: КІТ, Університет: КПІ")
        self.label_student_info.pack(pady=10)

        self.entry_sentence1 = tk.Entry(self.root, width=40)
        self.entry_sentence1.pack(pady=10)

        self.btn_process = tk.Button(self.root, text="Обробити рядок", command=self.process_string)
        self.btn_process.pack(pady=10)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentInfoApp(root)
    root.mainloop()
