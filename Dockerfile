FROM python:3.8

RUN mkdir app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3" , "app.py"]