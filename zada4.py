# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
from googletrans import Translator  # устанавливаем через pip install googletrans в терминале

with open('perevod.txt', 'w', encoding='utf-8') as f:
    with open('perevod_f.txt', 'r', encoding='utf-8') as f1:
                text = f1.read()
    f.write(Translator().translate(text, src='en', dest='ru').text)
