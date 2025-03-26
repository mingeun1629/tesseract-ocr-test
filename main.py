import pytesseract
from PIL import Image

### 한글+영어 텍스트 추출
image_path = "test.png"  # 이미지 경로
img = Image.open(image_path)
text = pytesseract.image_to_string(img, lang="eng+kor")
print("한글 추출된 텍스트:")
print(text)