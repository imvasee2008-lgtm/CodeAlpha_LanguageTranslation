from googletrans import Translator

translator = Translator()

text = input("Enter text to translate: ")

translated = translator.translate(text, dest='ta')

print("Translated Text:")
print(translated.text)