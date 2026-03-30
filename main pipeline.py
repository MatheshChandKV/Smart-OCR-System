import joblib
from open_cv import preprocess_image
mapping = {i: chr(i + 97) for i in range(26)}
model = joblib.load('emnist_model.pkl')
result = ""
img_path = 'image.png'
characters = preprocess_image(img_path)
corrections = {'i': 'I','l': 'I','o': 'O','0': 'O','z': 'Z','s': 'S','b': 'B','g': 'G','q': 'O','a': 'A'}
for char in characters:
    pred = model.predict(char)[0]
    if pred in mapping:
        result += mapping[pred]
    else:
        result += ' '
cleaned = ""

for ch in result:
    if ch in corrections:
        cleaned += corrections[ch]
    else:
        cleaned += ch

print("Corrected Text:", cleaned)
import difflib

words = ["PROTOTYPE", "BASIC", "MODEL", "TEXT"]

closest = difflib.get_close_matches(cleaned, words, n=1)

if closest:
    cleaned = closest[0]

print("Final Text:", cleaned)