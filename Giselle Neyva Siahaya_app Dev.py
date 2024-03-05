import random
import tkinter as tk
from tkinter import messagebox

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tebak Kata Game")

        # Set ukuran jendela utama
        self.master.geometry("800x600")

        self.words_to_guess = []
        self.word_to_guess = ""
        self.guessed_word = []
        self.attempts = 0

        self.label = tk.Label(master, text="Masukkan 5 kata yang berbeda:", font=("Arial", 18))
        self.label.pack(pady=10)

        for i in range(5):
            entry = tk.Entry(master, font=("Arial", 14))
            entry.pack(pady=5)
            self.words_to_guess.append(entry)

        self.start_button = tk.Button(master, text="Mulai", command=self.start_game, font=("Arial", 16))
        self.start_button.pack(pady=10)

    def start_game(self):
        user_inputs = [entry.get().lower() for entry in self.words_to_guess]

        if len(set(user_inputs)) != 5:
            messagebox.showwarning("Peringatan", "Masukkan 5 kata yang berbeda.")
            return

        self.word_to_guess = random.choice(user_inputs)
        self.guessed_word = ["_"] * len(self.word_to_guess)

        self.label.config(text="Selamat datang di permainan tebak kata!", font=("Arial", 18))
        for entry in self.words_to_guess:
            entry.pack_forget()
        self.start_button.pack_forget()

        self.show_word_to_guess()
        self.create_guessing_elements()

    def create_guessing_elements(self):
        self.guess_label = tk.Label(self.master, text="Tebak Kata:", font=("Arial", 18))
        self.guess_label.pack()

        self.guess_display = tk.Label(self.master, text=" ".join(["_" for _ in self.word_to_guess]), font=("Arial", 24))
        self.guess_display.pack()

        self.keyboard_frame = tk.Frame(self.master)
        self.create_keyboard()

    def create_keyboard(self):
        keys = "qwertyuiopasdfghjklzxcvbnm"
        
        for row in range(4):
            for col in range(7):
                index = row * 7 + col
                if index < len(keys):
                    key = keys[index]
                    button = tk.Button(self.keyboard_frame, text=key, command=lambda k=key: self.check_and_update(k), font=("Arial", 14))
                    button.grid(row=row, column=col, padx=5, pady=5)

        self.keyboard_frame.pack(pady=20)

    def show_word_to_guess(self):
        self.show_word_to_guess_label = tk.Label(self.master, text=f" {self.word_to_guess}", font=("Arial", 16))
        self.show_word_to_guess_label.pack(pady=10)

    def check_and_update(self, guess):
        if guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.guessed_word[i] = guess

            self.update_guess_display()

            if "_" not in self.guessed_word:
                self.game_over_message("Selamat! Kamu berhasil menebak kata.")
        else:
            self.attempts += 1
            messagebox.showinfo("Info", "Huruf tersebut tidak ada dalam kata yang harus ditebak. Coba lagi.")

    def update_guess_display(self):
        guess_display_text = " ".join(self.guessed_word)
        self.guess_display.config(text=guess_display_text)

    def game_over_message(self, message):
        messagebox.showinfo("Game Over", f"{message}\nJumlah percobaan: {self.attempts}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)	
    root.mainloop()
