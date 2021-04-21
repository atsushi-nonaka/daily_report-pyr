FROM alpine:latest

RUN apk --update add python3 python3-dev py3-pip \
    gcc \
    musl-dev \
    linux-headers \
    build-base \
    libffi-dev \
    bash

COPY . /app

WORKDIR /app

RUN rm -rf env && \
    python3 -m venv env 

RUN env/bin/pip install --upgrade pip
RUN env/bin/pip install -e .
# --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org

CMD ["env/bin/uwsgi", "--ini-paste", "development.ini"]