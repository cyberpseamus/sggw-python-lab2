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
• Przetestuj zapis tekstu do pliku w bloku with. Zmodyfikuj FileWriter, tak by:
• gdy w środku bloku with wystąpi wyjątek, __exit__ wypisał komunikat: „Błąd podczas zapisu: <treść wyjątku>”.
• wyjątek nie był tłumiony (czyli dalej przerywał program)."""
class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            print(f"Błąd podczas zapisu: {exc}")
            self.file.close()
            return False
        self.file.close()


""" Napisz klasę SafeDivision, która:
• w __enter__ zwraca samą siebie.
• ma metodę divide(a, b) dzielącą liczby,
• w __exit__ tłumi wyjątki typu ZeroDivisionError, wypisując komunikat „Nie
można dzielić przez zero”."""
class SafeDivision:

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if (exc_type == ZeroDivisionError):
            print("Nie można dzielić przez zero")
            return True           

    def divide(self, a,b):
        return a/b


def main():
    print("Początek logowania")

    try:
        with Logger():
            print("Logowane działanie")

            print("Operacja dzielenia")
            with SafeDivision() as div:
                print(div.divide(10, 0))

            print("Operacja zapisu do pliku")    
            with FileWriter("wynik.txt") as file:
                file.write("Linia tekstu")
                raise ValueError("Treść wyjątku")

        print("Koniec logowania")

    except ValueError:
        print("Wystąpił ValueError przy zapisie.")           
        raise

    finally:
        print(f"Czy plik jest zamknięty: {file.closed}")

if __name__ == "__main__":
    main()
