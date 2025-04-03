import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_image(image_path):
    """이미지 파일에서 텍스트 추출"""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang="eng+kor")

    pytesseract.pdf
    return text

def extract_text_from_pdf(pdf_path):
    """PDF 파일에서 텍스트 추출"""
    pages = convert_from_path(pdf_path, dpi=300, poppler_path="C:/poppler-24.08.0/Library/bin")
    text = ""
    for page_number, page in enumerate(pages, start=1):
        page_text = pytesseract.image_to_string(page, lang="eng+kor")
        text += f"[페이지 {page_number}]\n{page_text}\n"
    return text

def extract_text(file_path):
    """파일 유형에 따라 텍스트 추출"""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']:
        print(f"파일명: {file_path}")
        return extract_text_from_image(file_path)
    elif ext == '.pdf':
        print(f"파일명: {file_path}")
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("지원하지 않는 파일 형식입니다.")

# 파일 경로 설정
file_path = "test.png"  # 이미지 또는 PDF 경로

try:
    text = extract_text(file_path)
    print(text)
except Exception as e:
    print(f"오류 발생: {e}")