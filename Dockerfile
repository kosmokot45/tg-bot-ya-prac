FROM jrottenberg/ffmpeg:4.0-alpine

WORKDIR /app

COPY --from=0 / /

FROM python:3.11.1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]