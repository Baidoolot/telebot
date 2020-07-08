FROM python:3.7

ENV PYTHONDONTWRIEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /usr/src/parlament
WORKDIR /usr/src/parlament

COPY . /usr/src/parlament
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "app/main.py" ]



