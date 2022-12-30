FROM python:3.10.7
USER root

WORKDIR /app
COPY . /app

RUN pip install --upgrade -r /app/requirements.txt # python�̃��C�u������requirements.txt�ɋL�q���܂��B

RUN apt-get update # ffmpeg���r���h�ς݃o�C�i����install���܂��B
RUN apt-get install -y ffmpeg

CMD ["python", "main.py"]