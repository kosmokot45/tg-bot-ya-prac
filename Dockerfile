FROM python:3.11

RUN apt-get update && apt-get install ffmpeg

# create the app user
RUN addgroup --system app && adduser --system --group app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# test/debug mode
# ENTRYPOINT ["tail", "-f", "/dev/null"]

CMD [ "python", "app.py" ]