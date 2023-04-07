from pdf_merger import merge_pdf
from pdf_transformer import transform_pdf

print("Simple PDF Toolkit (SPT) wurde gestartet")
x = True
while x:
    app = input("Welches Programm moechten Sie nutzen? (pdf_merger [1] oder transformer [2]) ")
    if app == "1":
        print("")
        merge_pdf()
        x = False
    elif app == "2":
        print("")
        transform_pdf()
        x = False
    else:
        print("Bitte wiederholen Sie ihre Eingabe")