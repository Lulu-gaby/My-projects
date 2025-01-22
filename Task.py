#Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task ():
    def __init__(self,task_description, deadline):
        self.task_description = task_description
        self.deadline = deadline
        self.task_completed = False

    def mark_task(self):
        self.task_completed = True


def task_list():
    tasks = []

    tasks.append(Task("Помыть машину", "25.01.2025"))
    tasks.append(Task("Купить продукты", "23.01.2025"))
    tasks.append(Task("Купить подарок маме", "23.01.2025"))
    tasks.append(Task("Отдать вещи в химчистку", "27.01.2025"))

    tasks[0].mark_task()
    tasks[2].mark_task()

    print("Список задач:")
    for i, task in enumerate(tasks):
        print(f" {i}. {task.task_description} - {'Выполнено' if task.task_completed else 'Не выполнено'}")

    print("Невыполненные задачи:")
    for task in tasks:
        if not task.task_completed:
            print(f"{task.task_description} - {task.deadline}")

task_list()











