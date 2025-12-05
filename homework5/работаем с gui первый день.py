import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QComboBox
)
from PySide6.QtCore import Qt


class MiniTranslator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мини-переводчик")
        self.setMinimumSize(700, 300)

        self.en_ru_dict = {
            "hello": "привет",
            "hi": "привет",
            "world": "мир",
            "cat": "кот",
            "dog": "собака",
            "python": "питон",
            "student": "студент",
            "university": "университет",
            "coffee": "кофе",
            "book": "книга",
            "music": "музыка",
            "love": "любовь",
            "project": "проект",
            "homework": "домашка",
            "apple": "яблоко",
        }
        self.ru_en_dictionary = {
            "здравствуйте": "hello",
            "привет": "hi",
            "мир": "world",
            "кот": "cat",
            "собака": "dog",
            "студент": "student",
            "университет": "university",
            "кофе": "coffee",
            "книга": "book",
            "музыка": "music",
            "любовь": "love",
            "проект": "project",
            "домашняя работа": "homework",
            "яблоко": "apple",
        }

        #Ввод текста
        self.input_label = QLabel("Введите текст:")
        self.input_edit = QTextEdit()
        self.input_edit.setPlaceholderText("Введите слово или короткую фразу...")

        #Направление
        self.direction_label = QLabel("Направление:")
        self.direction_combo = QComboBox()
        self.direction_combo.addItems(["EN → RU", "RU → EN"])

        #Кнопка
        self.translate_button = QPushButton("Перевести")
        self.translate_button.clicked.connect(self.translate_text)

        #Вывод текста
        self.output_label = QLabel("Перевод:")
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)


        main_layout = QVBoxLayout()

        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_edit)

        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self.direction_label)
        controls_layout.addWidget(self.direction_combo)
        controls_layout.addStretch()
        controls_layout.addWidget(self.translate_button)

        main_layout.addLayout(controls_layout)

        main_layout.addWidget(self.output_label)
        main_layout.addWidget(self.output_edit)

        self.setLayout(main_layout)

    def translate_text(self:str) -> None:
        text = self.input_edit.toPlainText().strip()

        if not text:
            self.output_edit.setPlainText("Введите текст для перевода.")
            return

        direction = self.direction_combo.currentText()

        if direction == "EN → RU":
            result = self._translate_sentence(text, self.en_ru_dict)
        else:
            result = self._translate_sentence(text, self.ru_en_dict)

        self.output_edit.setPlainText(result)

    @staticmethod
    def _translate_sentence(sentence: str, dictionary: dict) -> str:
        words = sentence.split()
        translated_words = []

        for w in words:
            prefix = ""
            suffix = ""
            core = w

            while core and not core[0].isalnum():
                prefix += core[0]
                core = core[1:]
            while core and not core[-1].isalnum():
                suffix = core[-1] + suffix
                core = core[:-1]

            lower_core = core.lower()

            if not core:
                translated_words.append(w)
                continue

            if lower_core in dictionary:
                translated = dictionary[lower_core]
            else:
                translated = core + "[!]"

            translated_words.append(prefix + translated + suffix)

        return " ".join(translated_words)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MiniTranslator()
    window.show()

    sys.exit(app.exec())
