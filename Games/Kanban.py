import tkinter as tk
from tkinter import messagebox

# Цветовая палитра
BG_COLOR = "#BFB8DA"  # Лавандовый фон доски
COLUMN_COLOR = "#E8B7D4"  # Новый цвет колонок
BUTTON_COLOR = "#A5678E"  # Фиолетовые кнопки
BUTTON_TEXT_COLOR = "white"

class KanbanBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban Board")
        self.root.configure(bg=BG_COLOR)

        # Колонки Kanban
        self.columns = ["В ожидании", "В разработке", "Тестирование", "Готово"]
        self.tasks = {col: [] for col in self.columns}

        # Фреймы для колонок
        self.frames = {}
        self.text_widgets = {}

        for i, col in enumerate(self.columns):
            frame = tk.Frame(root, bg=COLUMN_COLOR, bd=2, relief="ridge", padx=10, pady=10)
            frame.grid(row=0, column=i, padx=10, pady=10, sticky="n")

            label = tk.Label(frame, text=col, font=("Arial", 14, "bold"), fg="black", bg=COLUMN_COLOR)
            label.pack()

            # Добавляем Scrollbar
            scrollbar = tk.Scrollbar(frame, orient="vertical")
            # Используем Text вместо Listbox
            text_widget = tk.Text(frame, width=30, height=15, bg="white", fg="black", font=("Arial", 12), wrap=tk.WORD, yscrollcommand=scrollbar.set)
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=text_widget.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.frames[col] = frame
            self.text_widgets[col] = text_widget

        # Поле ввода
        self.task_entry = tk.Entry(root, width=70, font=("Arial", 12))
        self.task_entry.grid(row=1, column=0, columnspan=4, pady=10)

        # Кнопки
        self.button_frame = tk.Frame(root, bg=BG_COLOR)
        self.button_frame.grid(row=2, column=0, columnspan=4, pady=5)

        self.add_button = tk.Button(self.button_frame, text="Добавить задачу", command=self.add_task,
                                    width=20, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 12, "bold"))
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.move_button = tk.Button(self.button_frame, text="Переместить", command=self.move_task,
                                     width=20, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 12, "bold"))
        self.move_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Удалить", command=self.delete_task,
                                       width=20, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 12, "bold"))
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        """Добавляет задачу в колонку 'В ожидании'."""
        task = self.task_entry.get()
        if task:
            self.tasks["В ожидании"].append(task)
            self.text_widgets["В ожидании"].insert(tk.END, task + "\n")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Введите название задачи!")

    def move_task(self):
        """Перемещает выбранную задачу в следующую колонку."""
        for col_index in range(len(self.columns) - 1):
            col = self.columns[col_index]
            next_col = self.columns[col_index + 1]

            # Получаем индекс задачи, чтобы переместить ее
            selection_start = self.text_widgets[col].index("insert linestart")
            selection_end = self.text_widgets[col].index("insert lineend")

            if selection_start != selection_end:
                task = self.text_widgets[col].get(selection_start, selection_end)
                self.text_widgets[col].delete(selection_start, selection_end)

                self.tasks[col].remove(task)
                self.tasks[next_col].append(task)
                self.text_widgets[next_col].insert(tk.END, task + "\n")
                return

        messagebox.showwarning("Ошибка", "Выберите задачу для перемещения!")

    def delete_task(self):
        """Удаляет выбранную задачу."""
        for col in self.columns:
            selection_start = self.text_widgets[col].index("insert linestart")
            selection_end = self.text_widgets[col].index("insert lineend")

            if selection_start != selection_end:
                task = self.text_widgets[col].get(selection_start, selection_end)
                self.text_widgets[col].delete(selection_start, selection_end)
                self.tasks[col].remove(task)
                return

        messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KanbanBoard(root)
    root.mainloop()
