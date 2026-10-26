from pathlib import Path
from typing import TextIO

# Ćwiczenia praktyczne dzień 2 - eksperymenty z kontekstem

"""Utwórz klasę Logger, która:
• przy wejściu do kontekstu (__enter__) wypisuje „Start sekcji logowania”,
• przy wyjściu (__exit__) wypisuje „Koniec sekcji logowania”.
• Użyj jej w bloku with, wypisując coś w środku"""

class Logger:
    def __enter__(self):
        print("Start sekcji logowania")

    def __exit__(self, exc_type, exc, tb):
        print("Koniec sekcji logowania")

"""Napisz klasę FileWriter, która:
• w __init__ przyjmuje ścieżkę do pliku,
• w __enter__ otwiera plik do zapisu i zwraca uchwyt (file handle),
• w __exit__ zamyka plik niezależnie od tego, czy wystąpił wyjątek.
• Przetestuj zapis tekstu do pliku w bloku with."""

class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()

def main():
    print("Początek logowania")

    with Logger():
        print("Logowane działanie")
        with FileWriter("wynik.txt") as file:
            file.write("Linia tekstu")

    print(f"Czy plik jest zamkniety: {file.closed}")

    print("Koniec logowania")


if __name__ == "__main__":
    main()
