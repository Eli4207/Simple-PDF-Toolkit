from pypdf import PdfWriter
from time import sleep

def merge_pdf():
    merger = PdfWriter()

    print("** PDF-Merger (Version 0.0.1) **")
    print("!!Erster Hinweis: Die Dateien werden in der Reihenfolge zusammengefuegt, in der Sie sie im Folgenden angeben!!")
    print("!!Zweiter Hinweis: Die einzulesenden Dateien sollten sich im gleichen Verzeichnis, wie dieses Programm befinden!!")

    o_name = input("Wie soll die fertige Datei heissen? ")

    x = True
    while x:
        name = input("Bitte geben Sie den Namen einer einzulesenden Datei an: ")
        pages = input("Bitte geben Sie die zu verwendenen Seiten an (z. B. '3-7' oder 'a' fuer alles): ")
        try:
            data = open(name + ".pdf", "rb")

            if pages == "a":
                merger.append(data)
            else:
                b_e_pages = pages.split("-")
                b_page = int(b_e_pages[0]) - 1
                e_page = int(b_e_pages[1])
                merger.append(fileobj=data, pages=(b_page, e_page))

            add = input("Möchten Sie weitere Dateien hinzufuegen? (y oder n): ")
            if add == "n":
                x = False
        except:
            print("Diese Datei kann nicht gefunden werden bzw. die Seitenzahlen sind falsch! Bitte wiederholen Sie ihre Eingabe!")

    output = open(o_name + ".pdf", "wb")
    merger.write(output)

    merger.close()
    output.close()

    print(o_name + ".pdf ist fertig!")
    sleep(2)