#  Smart-OCR-System

An advanced Optical Character Recognition (OCR) system that combines image processing, computer vision, and machine learning techniques to accurately extract text from noisy and real-world images.

---

##  Overview

This project implements a complete OCR pipeline that transforms raw images into clean, machine-readable text. Unlike basic OCR tools, this system focuses on improving accuracy through preprocessing and structured processing stages.

---

##  Features

*  Image preprocessing (grayscale, noise removal, thresholding)
*  Deskewing and image enhancement
*  Text extraction using OCR engine
*  Improved accuracy on noisy and real-world images
*  Before vs After comparison (enhanced vs raw input)
*  Modular pipeline (easy to extend with deep learning models)

---

##  Pipeline

```
Input Image
   ↓
Preprocessing (OpenCV)
   ↓
Text Detection / Extraction
   ↓
Post-processing
   ↓
Final Text Output
```

---

##  Tech Stack

* Python
* OpenCV
* Tesseract OCR
* NumPy

###  Optional 

* EasyOCR
* TensorFlow / PyTorch

---

##  Project Structure

```
Smart-OCR-System/
│
├── images/                # Input images
├── output/                # Processed images & results
├── src/
│   ├── preprocessing.py   # Image cleaning
│   ├── ocr_engine.py      # OCR extraction
│   ├── utils.py           # Helper functions
│
├── main.py                # Entry point
├── requirements.txt
└── README.md
```

---

##  Installation

```bash
git clone https://github.com/your-username/Smart-OCR-System.git
cd Smart-OCR-System
pip install -r requirements.txt
```

---

##  Usage

```bash
python main.py
```

---

##  Results

| Input Image | Processed Image | Extracted Text |
| ----------- | --------------- | -------------- |
| Raw Image   | Clean Image     | OCR Output     |

(Add screenshots here)

---

##  Future Improvements

*  Deep Learning-based OCR (CNN + LSTM)
*  Handwritten text recognition
*  Streamlit web interface
*  Multi-language support

---

##  Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

Mathesh Chand

---

##  Final Note

This project demonstrates how combining preprocessing, computer vision, and machine learning significantly improves OCR performance compared to basic implementations.
