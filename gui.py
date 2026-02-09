import tkinter as tk
from tkinter import messagebox, simpledialog
from Database import Database
from Todo import Todo

db = Database()
invoer_titel = None
todo_lijst = None
status_tekst = None

def vernieuw_lijst():
    """Laat alle todos opnieuw zien in de lijst."""
    todo_lijst.delete(0, tk.END)

    todos = db.get_todos()
    for todo_id in sorted(todos):
        todo = todos[todo_id]
        klaar = "ja" if todo.completed else "nee"
        regel = f"{todo_id}: {todo.title} (klaar: {klaar})"
        todo_lijst.insert(tk.END, regel)


def geselecteerde_id():
    """Pak het ID van de geselecteerde regel in de lijst."""
    selectie = todo_lijst.curselection()
    if not selectie:
        messagebox.showinfo("Info", "Kies eerst een todo in de lijst.")
        return None

    regel_index = selectie[0]
    regel_tekst = todo_lijst.get(regel_index)
    id_tekst = regel_tekst.split(":")[0]
    return int(id_tekst)


def voeg_todo_toe():
    titel = invoer_titel.get().strip()
    if titel == "":
        messagebox.showinfo("Info", "Vul eerst een titel in.")
        return

    todo = Todo(titel)
    nieuw_id = db.add_todo(todo)

    invoer_titel.delete(0, tk.END)
    vernieuw_lijst()
    status_tekst.config(text=f"Toegevoegd: {nieuw_id}")


def voeg_todo_toe_via_enter(event):
    voeg_todo_toe()


def markeer_als_klaar():
    todo_id = geselecteerde_id()
    if todo_id is None:
        return

    todo = db.get_todo(todo_id)
    if todo is None:
        messagebox.showinfo("Info", "Deze todo bestaat niet meer.")
        vernieuw_lijst()
        return

    todo.completed = True
    vernieuw_lijst()
    status_tekst.config(text=f"Afgerond: {todo_id}")


def wijzig_titel():
    todo_id = geselecteerde_id()
    if todo_id is None:
        return

    todo = db.get_todo(todo_id)
    if todo is None:
        messagebox.showinfo("Info", "Deze todo bestaat niet meer.")
        vernieuw_lijst()
        return

    nieuwe_titel = simpledialog.askstring("Titel wijzigen", "Nieuwe titel:")
    if nieuwe_titel is None:
        return

    nieuwe_titel = nieuwe_titel.strip()
    if nieuwe_titel == "":
        messagebox.showinfo("Info", "Titel mag niet leeg zijn.")
        return

    todo.title = nieuwe_titel
    vernieuw_lijst()
    status_tekst.config(text=f"Aangepast: {todo_id}")


def verwijder_todo():
    todo_id = geselecteerde_id()
    if todo_id is None:
        return

    gelukt = db.remove_todo(todo_id)
    if not gelukt:
        messagebox.showinfo("Info", "Deze todo bestaat niet meer.")

    vernieuw_lijst()
    if gelukt:
        status_tekst.config(text=f"Verwijderd: {todo_id}")


def start_gui():
    global invoer_titel, todo_lijst, status_tekst

    venster = tk.Tk()
    venster.title("Simpele Todo Lijst")
    venster.geometry("500x400")

    boven = tk.Frame(venster)
    boven.pack(fill="x", padx=10, pady=10)

    invoer_titel = tk.Entry(boven)
    invoer_titel.pack(side="left", fill="x", expand=True)
    invoer_titel.bind("<Return>", voeg_todo_toe_via_enter)

    knop_toevoegen = tk.Button(boven, text="Toevoegen", command=voeg_todo_toe)
    knop_toevoegen.pack(side="left", padx=8)

    todo_lijst = tk.Listbox(venster, height=12)
    todo_lijst.pack(fill="both", expand=True, padx=10)

    onder = tk.Frame(venster)
    onder.pack(fill="x", padx=10, pady=10)

    knop_klaar = tk.Button(onder, text="Klaar", command=markeer_als_klaar)
    knop_klaar.pack(side="left")

    knop_wijzigen = tk.Button(onder, text="Wijzigen", command=wijzig_titel)
    knop_wijzigen.pack(side="left", padx=8)

    knop_verwijderen = tk.Button(onder, text="Verwijderen", command=verwijder_todo)
    knop_verwijderen.pack(side="left")

    status_tekst = tk.Label(venster, text="Klaar")
    status_tekst.pack(fill="x", padx=10, pady=(0, 10))

    vernieuw_lijst()
    venster.mainloop()


if __name__ == "__main__":
    start_gui()
