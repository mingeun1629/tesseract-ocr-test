# OCR 사용법

## 1. Tesseract 설치
[Tesseract 공식 설치 가이드](https://github.com/UB-Mannheim/tesseract/wiki)를 참고하여 다운로드 및 설치합니다.

## 2. 환경변수 설정
Tesseract 실행 경로를 `PATH` 환경변수에 추가합니다.
예시 (Windows 기준):
```
C:\Program Files\Tesseract-OCR
```

## 3. 필수 라이브러리 설치
아래 명령어를 실행하여 `pytesseract` 및 `Pillow`를 설치합니다.
```sh
pip install pytesseract pillow
```

## 4. 샘플 이미지 준비
OCR 테스트를 위한 이미지를 프로젝트 루트 디렉토리에 저장합니다.
예시: `test.png`

## 5. 실행
아래 명령어로 OCR을 실행합니다.
```sh
python main.py
```