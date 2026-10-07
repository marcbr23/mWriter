from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QPlainTextEdit, QPushButton, QFileDialog, QLabel
import os
import sys
import webbrowser



class mWriter(QtWidgets.QWidget):

    def nerdfonts(self):
        webbrowser.open_new(r"https://www.nerdfonts.com/cheat-sheet")

    def saveas(self):
        filepath, _ = QFileDialog.getSaveFileName(
            self, 
            "Save file as...", 
            "", 
            "Archivos de texto (*.txt);; All files (*)"
        )
        
        if filepath:
            
            if not filepath.endswith(".txt"):
                filepath += ".txt"

            contenido = self.input.toPlainText()
            f = open(filepath, "w", encoding="utf-8") 
            f.write(contenido)
            f.close()
    
    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self, 
            "Open file", 
            "", 
            "Archivos de texto (*.txt);; All files (*)"
        )

        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                self.input.setPlainText(content)

    def wordcount(self):
            text_content = self.input.toPlainText()
            wordnumber = len(text_content.replace("'", " ").replace("-", " ").split())
            self.number_of_words.setText(f"{wordnumber} words")

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.input = QPlainTextEdit(self)
        self.input.setStyleSheet("border: none; font-family: 'Iosevka Term'; font-size: 16pt")
        self.save = QPushButton("", self)
        self.save.setStyleSheet("border: none;")
        self.nf = QPushButton("󰛖", self)
        self.nf.setStyleSheet("border: none;")
        self.openfile = QPushButton("", self)
        self.openfile.setStyleSheet("border: none;")
        self.number_of_words = QLabel("0 words")
        self.number_of_words.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number_of_words.setStyleSheet("border: none; font-family: 'Iosevka Term'; font-size: 10pt")

        self.layout.addWidget(self.input, 1, 3)
        self.layout.addWidget(self.openfile, 2, 0)
        self.layout.addWidget(self.save, 2, 1)
        self.layout.addWidget(self.nf, 2, 2)
        self.layout.addWidget(self.number_of_words, 2, 4)


        self.save.clicked.connect(self.saveas)
        self.save.setShortcut("Ctrl+S")

        self.nf.clicked.connect(self.nerdfonts)
        self.nf.setShortcut("Shift+Ctrl+N")

        self.openfile.clicked.connect(self.open_file)
        self.openfile.setShortcut("Ctrl+O")

        self.input.textChanged.connect(self.wordcount)

        self.layout.setRowStretch(0, 10)
        self.layout.setRowStretch(1, 80)
        self.layout.setRowStretch(2, 10)

        self.layout.setColumnStretch(0, 5)
        self.layout.setColumnStretch(1, 5)
        self.layout.setColumnStretch(2, 5)
        self.layout.setColumnStretch(3, 70)
        self.layout.setColumnStretch(4, 15)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = mWriter()
    widget.show()

    sys.exit(app.exec())
