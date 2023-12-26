import tkinter as tk
from tkinter.ttk import Combobox
from openpyxl import Workbook
import pathlib

root = tk.Tk()
root.title('Cadastro de Clientes')
root.geometry("600x400")
root.configure(bg='black')  # Alterando a cor de fundo da interface

# Criação dos campos de entrada
labels = []
entries = []
label_texts = ['Nome Completo:', 'Idade:', 'Telefone:', 'Email:', 'Endereço:', 'Sexo:', 'Nacionalidade:']
for i, label_text in enumerate(label_texts):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, sticky='w')
    label.config(fg='black')  # Alterando a cor do texto dos labels para branco
    labels.append(label)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=10, ipadx=80)
    entry.config(width=50, bg='green', fg='white')  # Alterando a cor de fundo e texto das entradas para branco e preto
    entries.append(entry)

    if label_text == 'Sexo:':
        combo_sexo = Combobox(root, values=['Masculino', 'Feminino', 'Outro'])
        combo_sexo.grid(row=i, column=1, padx=10, pady=10, ipadx=165)
        combo_sexo.config(width=18, background='white', foreground='black')  # Alterando a cor de fundo e texto do Combobox para branco e preto
        entries[-1] = combo_sexo

    if label_text == 'Nacionalidade:':
        entry.insert(tk.END, 'Brasileiro')  # Exemplo de entrada padrão para Nacionalidade

    if label_text == 'Idade:':
        entry.insert(tk.END, '0')  # Exemplo de entrada padrão para Idade

    labels[-1] = label

# Atribuir as variáveis globais
entry_nome, entry_idade, entry_telefone, entry_email, entry_endereco, combo_sexo, entry_nacionalidade = entries

# Restante do código (funções, botões, etc.)
def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    sexo = combo_sexo.get()
    nacionalidade = entry_nacionalidade.get()

    # Restante do código de cadastro...

def mudar_cor():
    root.configure(bg='black')
    for label in labels:
        label.config(fg='black')
    for entry in entries:
        entry.config(bg='green', fg='white')
    button_cadastrar.config(bg='green')

button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
button_cadastrar.grid(row=len(label_texts), columnspan=2, padx=10, pady=10)
button_cadastrar.config(bg='green', fg='white')
button_mudar_cor = tk.Button(root, text="Mudar Cor", command=mudar_cor)
button_mudar_cor.grid(row=len(label_texts) + 1, columnspan=2, padx=10, pady=10)

# Configuração da planilha Excel
ficheiro_path = pathlib.Path("Clientes.xlsx")
    
# Configuração da planilha Excel
workbook = Workbook()
planilha = workbook.active
planilha.append(['Nome', 'Idade', 'Telefone', 'Email', 'Endereço', 'Sexo', 'Nacionalidade'])
workbook.save('cadastros.xlsx')

root.mainloop()