# Optical Character Recognition (OCR) Image Processing

This code is an example of using Optical Character Recognition (OCR) to extract text from images. It uses the Tesseract library for OCR and the Python Imaging Library (PIL) for image processing.

## Prerequisites
- Python 3.x
- Tesseract OCR
- pytesseract library
- PIL library

## Installation
1. Install Tesseract OCR by following the instructions specific to your operating system. You can find the installation guide at [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
2. Install the required Python libraries by running the following command:

    ```pip install -r requirements.txt```


## Usage
1. Place the images you want to process in the same directory as the script.
2. Open the script file and locate the following line:

```python
file = "image 1 "+"("+str(x)+")"+'.jpg'
```
Modify "image 1 " to match the name of your image file. If your image file name follows a different pattern, make sure to adjust it accordingly.

3. Run the script and enter the total number of images you want to process.
4. The script will iterate through each image, extract the text using OCR, and store the extracted text in a data.txt file.
5. The progress of the OCR process will be displayed as a percentage.
6. Once the script completes, the extracted text will be available in the data.txt file.

7. Press Enter to exit the script.

## Additional Information

    You can modify the script to change the image file format or the output file name by modifying the relevant parts of the code.

The Tesseract OCR library is a powerful tool for extracting text from images but may not always produce perfect results. Adjustments or preprocessing of the images may be 

required to improve the accuracy of the OCR.

For more information on how to use Tesseract OCR with Python, refer to the pytesseract documentation.

Feel free to customize the code according to your specific requirements and use it as a starting point for your own OCR image processing projects.