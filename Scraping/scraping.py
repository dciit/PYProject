# import pytesseract
# import cv2
# import re
# import os 
# def cut_after_numbers(text):
#   pattern = r"\d+"  # รูปแบบสำหรับจับคู่ชุดตัวเลข
#   match = re.search(r'\d+', text[::-1])
#   if match:
#       return text[len(text) - match.end():len(text)]
  
# # อ่านภาพ
# img = cv2.imread('image.jpg')

# # แปลงเป็น grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # ทำ OCR
# text = pytesseract.image_to_string(gray, lang='tha')  # กำหนดภาษาเป็นไทย

# lines = text.splitlines()
# texts = ''
# # Loop through each line and process it as needed
# for index,line in enumerate(lines):
#     # Remove leading and trailing whitespace
#     line = line.strip()
    
#     # Check if the line is empty or contains only whitespace
#     if not line:
#         continue  # Skip empty lines

#     # Process the line here (e.g., print, store in a list, analyze)
#     if index >= 3:
#         if cut_after_numbers(line) != None and len(cut_after_numbers(line)) > 1:
#             print(line)
#             texts += cut_after_numbers(line) + '\n'



# # file_name = "sample.txt"
# # file_path = os.path.join(os.getcwd(), file_name)  # Save in the current working directory

# # # Write the text to the file
# # with open(file_path, "w") as file:
# #     file.write(texts)

# # # Open the file with Notepad
# # os.system(f"notepad {file_path}")

from PIL import Image
import pytesseract

# กำหนดเส้นทางไปยัง tesseract.exe หากยังไม่ได้เพิ่มลงใน PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# เปิดรูปภาพที่ต้องการอ่าน
image = Image.open('image.jpg')  # แทนที่ด้วยชื่อไฟล์รูปภาพจริง

# กำหนดให้ pytesseract อ่านข้อความเป็นภาษาไทย
thai_text = pytesseract.image_to_string(image, lang='tha')

# พิมพ์ผลลัพธ์ที่ได้
print("ข้อความที่ได้จากภาพ:", thai_text)

# กรองเฉพาะตัวเลขไทยจากข้อความที่ได้
thai_numbers = ''.join([ch for ch in thai_text if ch in '๑๒๓๔๕๖๗๘๙๐'])

print("ตัวเลขไทยที่พบ:", thai_numbers)