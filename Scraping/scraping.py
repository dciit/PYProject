import pytesseract
import cv2
import re
def cut_after_numbers(text):
  pattern = r"\d+"  # รูปแบบสำหรับจับคู่ชุดตัวเลข
  match = re.search(r'\d+', text[::-1])
  if match:
      return text[len(text) - match.end():len(text)]
  
# อ่านภาพ
img = cv2.imread('image.jpg')

# แปลงเป็น grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ทำ OCR
text = pytesseract.image_to_string(gray, lang='tha')  # กำหนดภาษาเป็นไทย

lines = text.splitlines()

# Loop through each line and process it as needed
for index,line in enumerate(lines):
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Check if the line is empty or contains only whitespace
    if not line:
        continue  # Skip empty lines

    # Process the line here (e.g., print, store in a list, analyze)
    if index >= 3:
        if cut_after_numbers(line) != None and len(cut_after_numbers(line)) > 1:
            # print(line)
            print(cut_after_numbers(line))


