import tkinter as tk  # Importa a biblioteca Tkinter e chama de tk pra facilitar
from tkinter import messagebox # Importa a messagebox pra mostrar avisos

class ToDoListApp:
    def __init__(self, root):
        # Inicializa a janela principal
        self.root = root
        self.root.title("Minha Lista de Tarefas") # Define o título da janela

        # Cria uma lista vazia pra guardar as tarefas
        self.tasks = []

        # Cria os componentes da interface

        # Campo de texto pra digitar a tarefa
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)  # Adiciona um espaço em cima e embaixo

        # Botão pra adicionar a tarefa
        self.add_button = tk.Button(root, text="Adicionar", command=self.add_task)
        self.add_button.pack()

        # Listbox pra mostrar as tarefas
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        # Botão pra marcar como concluída
        self.complete_button = tk.Button(root, text="Concluir", command=self.complete_task)
        self.complete_button.pack()

        # Botão pra remover a tarefa
        self.delete_button = tk.Button(root, text="Remover", command=self.delete_task)
        self.delete_button.pack()


    def add_task(self):
        # Pega o texto do campo de texto
        task = self.task_entry.get()

        # Verifica se o campo não está vazio
        if task != "":  # Jeito mais "estudante" de verificar
            # Adiciona a tarefa na lista
            self.tasks.append({"task": task, "completed": False})

            # Atualiza a listbox pra mostrar a nova tarefa
            self.update_listbox()

            # Limpa o campo de texto
            self.task_entry.delete(0, tk.END)
        else:
            # Mostra um aviso se o campo estiver vazio
            messagebox.showwarning("Aviso!", "Por favor, digite uma tarefa!")


    def complete_task(self):
        # Tenta pegar o índice da tarefa selecionada
        try:
            selected_index = self.task_listbox.curselection()[0]  # Pega o primeiro item selecionado

            # Marca a tarefa como concluída
            self.tasks[selected_index]["completed"] = True

            # Atualiza a listbox
            self.update_listbox()

        except IndexError:
            # Mostra um aviso se nada estiver selecionado
            messagebox.showwarning("Aviso!", "Selecione uma tarefa!")


    def delete_task(self):
        # Tenta pegar o índice da tarefa selecionada
        try:
            selected_index = self.task_listbox.curselection()[0]

            # Remove a tarefa da lista
            del self.tasks[selected_index]

            # Atualiza a listbox
            self.update_listbox()

        except IndexError:
            # Mostra um aviso se nada estiver selecionado
            messagebox.showwarning("Aviso!", "Selecione uma tarefa!")


    def update_listbox(self):
        # Limpa a listbox
        self.task_listbox.delete(0, tk.END)

        # Adiciona as tarefas da lista na listbox
        for i, task_data in enumerate(self.tasks):
            task = task_data["task"]
            completed = task_data["completed"]

            # Se a tarefa estiver concluída, coloca "(Concluída)" no final
            if completed:
                task = task + " (Concluída)" # Concatenando string desse jeito

            self.task_listbox.insert(tk.END, task)

            # Coloca a cor da tarefa em cinza se estiver concluída
            if completed:
                self.task_listbox.itemconfig(i, fg="gray")


# Inicializa a janela e roda o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()