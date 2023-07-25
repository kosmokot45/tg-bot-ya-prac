FROM python:3.11.1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get -y update -qq --fix-missing && \
    apt-get -y install --no-install-recommends \
    ffmpeg

COPY . .

CMD [ "python3", "app.py" ]