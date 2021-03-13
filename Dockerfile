from python3.9
RUN mkdir -p /moya_programma/
COPY . /moya_programma/
WORKDIR /moya_programma/

CMD ["python3", "main.py"]
