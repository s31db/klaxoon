import tkinter as tk
from tkinter import messagebox
import os


class TokenInputDialog:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Configuration du jeton d'API Klaxoon")

        self.label = tk.Label(master, text="Entrez votre jeton d'API Klaxoon :")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.save_button = tk.Button(
            master, text="Enregistrer", command=self.save_token
        )
        self.save_button.pack()

    def save_token(self) -> None:
        api_token = self.entry.get()
        if not api_token:
            messagebox.showerror("Erreur", "Veuillez entrer un jeton d'API")
        else:
            try:
                os.makedirs(os.path.expanduser("~/.api_klaxoon"))
            except FileExistsError:
                pass
            with open(os.path.expanduser("~/.api_klaxoon/.token"), "w") as f:
                f.write(api_token)
            messagebox.showinfo(
                "Succès", "Le jeton d'API a été enregistré avec succès."
            )
            self.master.destroy()


def configure_api_token() -> None:
    root = tk.Tk()
    token_input_dialog = TokenInputDialog(root)
    root.mainloop()


if __name__ == "__main__":
    configure_api_token()
