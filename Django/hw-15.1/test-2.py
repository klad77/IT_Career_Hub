import re
import unittest

# тесты показали, что предложенные функции обработки текста
# работают не правильно


class TextProcessor:

    def __init__(self, text):
        self.text = text
        self.cleaned_text = None

    def clean_text(self):
        # Удаляет все небуквенные символы и приводит текст к нижнему регистру
        self.cleaned_text = re.sub(r'[^a-zA-Z\s]', '', self.text).lower()

    def remove_stop_words(self, stop_words):
    # Удаляет стоп-слова из текста
        if self.cleaned_text is None:
            self.clean_text()
        words = self.cleaned_text.split()
        filtered_words = [word for word in words if word not in stop_words]
        self.cleaned_text = ' '.join(filtered_words)


class TestTextProcessor(unittest.TestCase):

    def test_remove_stop_words_works_when_no_stop_words_present(self):
        processor = TextProcessor("Hello World")
        stop_words = ([])
        processor.remove_stop_words(stop_words)
        self.assertEqual(processor.cleaned_text, "hello world")


    def test_clean_text_removes_non_alpha_characters(self):
        processor = TextProcessor("123 ABC!!!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "abc")

    def test_clean_text_converts_to_lowercase(self):
        processor = TextProcessor("HeLLo WoRLD")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "hello world")

    def test_clean_text_handles_empty_string(self):
        processor = TextProcessor("")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "")

    def test_remove_stop_words_removes_stop_words(self):
        processor = TextProcessor("this is a test")
        stop_words = ['this', 'is']
        processor.remove_stop_words(stop_words)
        self.assertEqual(processor.cleaned_text, "a test")




if __name__ == "__main__":
    unittest.main()
