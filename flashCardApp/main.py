from tkinter import *
import random


class FlashcardApp:
    def __init__(self, window):
        self.window = window

        # Ikkunan asetukset
        self.window.title("English-Finnish Flashcards")
        self.window.geometry("500x450")
        self.window.configure(bg="lightblue")

        # Sanat
        self.words = self.load_words()

        # Nykyinen sana
        self.current_english = ""
        self.current_finnish = ""

        # Onko vastaus näkyvissä?
        self.answer_visible = False

        # Pisteet
        self.correct = 0
        self.wrong = 0

        # Käännössuunta
        self.direction = IntVar(value=1)

        self.setup()

        # Ensimmäinen sana
        self.next_word()

    def setup(self):
        # Otsikko
        title = Label(
            self.window,
            text="English-Finnish Flashcards",
            font=("Arial", 20, "bold"),
            bg="lightblue"
        )
        title.pack(pady=20)

        # Käännössuunta
        direction_label = Label(
            self.window,
            text="Translation direction:",
            font=("Arial", 11),
            bg="lightblue"
        )
        direction_label.pack()

        self.radiobutton1 = Radiobutton(
            self.window,
            text="English → Finnish",
            variable=self.direction,
            value=1,
            font=("Arial", 10),
            bg="lightblue",
            command=self.next_word
        )
        self.radiobutton1.pack()

        self.radiobutton2 = Radiobutton(
            self.window,
            text="Finnish → English",
            variable=self.direction,
            value=2,
            font=("Arial", 10),
            bg="lightblue",
            command=self.next_word
        )
        self.radiobutton2.pack()

        # Sana
        self.word_label = Label(
            self.window,
            text="aydaguwhdaoj",
            font=("Arial", 18, "bold"),
            bg="lightblue"
        )
        self.word_label.pack(pady=30)

        # Vastaus
        self.answer_label = Label(
            self.window,
            text="",
            font=("Arial", 20),
            bg="lightblue"
        )
        self.answer_label.pack(pady=5)

        # Show answer -nappi
        self.answer_button = Button(
            self.window,
            text="Show answer",
            font=("Arial", 11),
            width=15,
            command=self.show_answer
        )
        self.answer_button.pack(pady=10)

        # Oikein / väärin -napit
        self.correct_button = Button(
            self.window,
            text="Correct",
            font=("Arial", 10),
            width=10,
            command=self.mark_correct,
            state=DISABLED
        )
        self.correct_button.pack(side=LEFT, padx=(130, 5))

        self.wrong_button = Button(
            self.window,
            text="Wrong",
            font=("Arial", 10),
            width=10,
            command=self.mark_wrong,
            state=DISABLED
        )
        self.wrong_button.pack(side=LEFT, padx=5)

        # Seuraava sana
        self.next_button = Button(
            self.window,
            text="Next word",
            font=("Arial", 11),
            width=15,
            command=self.next_word
        )
        self.next_button.pack(pady=15)

        # Pisteet
        self.score_label = Label(
            self.window,
            text="Correct: 0    Wrong: 0",
            font=("Arial", 10),
            bg="lightblue"
        )
        self.score_label.pack()

        # Enter = seuraava sana
        self.window.bind("<Return>", lambda event: self.next_word())

    def load_words(self):
        words = {}

        try:
            with open(
                "ENASanasto/sanasto.txt",
                "r",
                encoding="utf-8"
            ) as file:

                for line in file:
                    line = line.strip()

                    if not line:
                        continue

                    try:
                        english, finnish = line.split(" - ", 1)
                        words[english] = finnish

                    except ValueError:
                        print("Virheellinen rivi:", line)

        except FileNotFoundError:
            self.word_label = None

            print("Tiedostoa ENASanasto/sanasto.txt ei löytynyt.")

        return words

    def next_word(self):
        if not self.words:
            self.word_label.config(text="No words found")
            return

        # Arvotaan uusi sana
        english_word = random.choice(list(self.words.keys()))
        finnish_word = self.words[english_word]

        self.current_english = english_word
        self.current_finnish = finnish_word

        # Vastaus piiloon
        self.answer_visible = False

        self.answer_label.config(text="")

        # Näytetään kysymys
        if self.direction.get() == 1:
            self.word_label.config(text=self.current_english)

        else:
            self.word_label.config(text=self.current_finnish)

        # Painikkeiden tilat
        self.answer_button.config(state=NORMAL)
        self.correct_button.config(state=DISABLED)
        self.wrong_button.config(state=DISABLED)

    def show_answer(self):
        if self.answer_visible:
            return

        self.answer_visible = True

        if self.direction.get() == 1:
            self.answer_label.config(text=self.current_finnish)

        else:
            self.answer_label.config(text=self.current_english)

        # Kun vastaus on näkyvissä, käyttäjä voi arvioida itsensä
        self.correct_button.config(state=NORMAL)
        self.wrong_button.config(state=NORMAL)

        self.answer_button.config(state=DISABLED)

    def mark_correct(self):
        self.correct += 1
        self.update_score()
        self.next_word()

    def mark_wrong(self):
        self.wrong += 1
        self.update_score()
        self.next_word()

    def update_score(self):
        self.score_label.config(
            text=f"Correct: {self.correct}    Wrong: {self.wrong}"
        )


if __name__ == "__main__":
    window = Tk()

    app = FlashcardApp(window)

    window.mainloop()
