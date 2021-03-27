FROM python:3.9.2

ENV TARGET_DIR /game_isp/

RUN mkdir -p "${TARGET_DIR}"

COPY . "${TARGET_DIR}"

WORKDIR "${TARGET_DIR}"

CMD ["python3", "main.py"]
