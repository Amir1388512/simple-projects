FROM python:3.12-slim

LABEL author="amir" version="1.0.0" description="This is my test-1 project"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "equation.py"]
