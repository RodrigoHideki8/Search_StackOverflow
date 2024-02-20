import tkinter as tk
from tkinter import scrolledtext
from search_stackoverflow import search_stackoverflow

def buscar_resposta():
    mensagem_erro = entry.get()
    resumo_resposta = search_stackoverflow(mensagem_erro)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, resumo_resposta)

root = tk.Tk()
root.title("Busca no Stack Overflow")

label = tk.Label(root, text="Informe a mensagem de erro:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Buscar", command=buscar_resposta)
button.pack()

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
text_area.pack()

root.mainloop()