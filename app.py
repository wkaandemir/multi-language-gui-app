import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import gettext

def setup_translation(language):
    locale_dir = 'locale'
    translation = gettext.translation('messages', localedir=locale_dir, languages=[language])
    translation.install()
    global _
    _ = translation.gettext

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sample Application")
        self.setGeometry(100, 100, 300, 200)

        self.language_var = 'en'

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.create_widgets()

    def create_widgets(self):
        self.label = QLabel("Hello, world!")
        self.layout.addWidget(self.label)

        self.name_label = QLabel("Please enter your name:")
        self.layout.addWidget(self.name_label)
        
        self.name_entry = QLineEdit()
        self.layout.addWidget(self.name_entry)

        self.greet_button = QPushButton("Greet")
        self.greet_button.clicked.connect(self.greet)
        self.layout.addWidget(self.greet_button)

        self.language_menu = QComboBox()
        self.language_menu.addItems(['en', 'tr'])
        self.language_menu.currentTextChanged.connect(self.change_language)
        self.layout.addWidget(self.language_menu)

    def greet(self):
        name = self.name_entry.text()
        greeting = _("Hello, {}!").format(name)
        self.label.setText(greeting)

    def change_language(self, language):
        self.language_var = language
        setup_translation(language)
        self.update_ui()

    def update_ui(self):
        self.setWindowTitle(_("Sample Application"))
        self.label.setText(_("Hello, world!"))
        self.name_label.setText(_("Please enter your name:"))
        self.greet_button.setText(_("Greet"))


if __name__ == "__main__":
    setup_translation('en')
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
