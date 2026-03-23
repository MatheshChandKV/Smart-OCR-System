#OCR with tesseract

import pytesseract as pt
from PIL import Image
a=pt.image_to_string(Image.open('test_image1.png'))
print(a)
