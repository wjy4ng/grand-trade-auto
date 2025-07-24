![header](https://capsule-render.vercel.app/api?type=rect&color=gradient&height=100&section=header&text=Grand-Trade-Auto&fontSize=45&fontAlign=80&fontAlignY=52)   
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## 🚗 프로젝트 소개 (Project Overview)

**Grand-Trade-Auto**는 중고차 가격을 예측하는 웹 애플리케이션입니다. 사용자는 차량의 다양한 옵션(제조사, 모델, 연식, 주행거리 등)을 입력하고, AI 모델이 예측한 합리적인 중고차 가격을 확인할 수 있습니다.

## ✨ 주요 기능 (Features)

*   **데이터 수집**: 웹 크롤러를 이용해 중고차 매물 데이터를 수집합니다.
*   **가격 예측 모델**: 수집된 데이터를 기반으로 XGBoost 머신러닝 모델을 학습하여 중고차 가격을 예측합니다.
*   **웹 인터페이스**: 사용자가 쉽게 차량 정보를 입력하고 예측 결과를 확인할 수 있는 React 기반의 프론트엔드를 제공합니다.
*   **API 서버**: Django를 사용하여 예측 모델을 서빙하는 백엔드 API를 구축했습니다.
*   **자동 배포**: GitHub Actions를 통해 AWS에 자동으로 배포됩니다.

## 🛠️ 기술 스택 (Tech Stack)

*   **Frontend**: React, TypeScript, Vite, Tailwind CSS
*   **Backend**: Django, Django REST Framework
*   **ML/Data**: Python, Pandas, Scikit-learn, XGBoost, Selenium
*   **Deployment**: AWS, GitHub Actions

## ⚙️ 작동 방식 (How it Works)
1. 데이터 불러오기
    - 데이터 형식 포맷
    - 데이터 결측치 제거
    - 데이터 타입 변환
2. 모델링
    - 벡터화
    - 학습/테스트 데이터셋 분리
    - XGBoost 모델 학습
    - 테스트 데이터셋으로 모델 검증
3. 새로운 데이터 예측

## 📊 데이터 출처 (Data Source)

*   **[Encar](https://car.encar.com/)**: 모델 학습을 위한 중고차 데이터는 엔카 홈페이지에서 수집되었습니다.
