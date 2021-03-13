FROM python:3.9.2
RUN mkdir -p /moya_programma/
COPY . /moya_programma/
WORKDIR /moya_programma/

CMD ["python3", "main.py"]
