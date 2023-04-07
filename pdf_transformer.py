from pypdf import PdfWriter, PdfReader
from time import sleep

def transform_pdf():
    print("** PDF-Transformer (Version 0.0.1) **")
    print("!!Hinweis: Die einzulesenden Dateien sollten sich im gleichen Verzeichnis, wie dieses Programm befinden!!")

    x = True
    while x:
        o_name = input("Wie soll die fertige Datei heissen? ")
        name = input("Bitte geben Sie den Namen der einzulesenden Datei an: ")
        pages = input("Welche Seiten sollen gedreht werden? (z. B. 1,2,4,7) ")
        pages.replace(" ", "")
        pages_l = pages.split(",")
        try:
            reader = PdfReader(name + ".pdf")
            writer = PdfWriter()

            for page in range(0, len(reader.pages), 1):
                writer.add_page(reader.pages[page])
                if str(page + 1) in pages_l:
                    writer.pages[page].rotate(180)

            with open(o_name + ".pdf", "wb") as output:
                writer.write(output)

            print(o_name + ".pdf ist fertig!")
            c = input("Wollen Sie die Seiten weiterer Dateien drehen? (y oder n) ")
            if c == "n":
                x = False
            sleep(2)

        except:
            print("Bitte überprüfen Sie ihre Eingaben")