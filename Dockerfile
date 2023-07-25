FROM python:3.11.1

# FROM jrottenberg/ffmpeg:4.3-alpine

# WORKDIR /app
RUN apt-get -y update && apt-get -y install ffmpeg

# create the app user
# RUN addgroup --system app && adduser --system --group app

# SET environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY --from=1 / /
# COPY . .

# test/debug mode
# ENTRYPOINT ["tail", "-f", "/dev/null"]

CMD [ "python", "app.py" ]