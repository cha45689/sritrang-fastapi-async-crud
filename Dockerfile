FROM python:3.11-slim as compile-image

RUN apt-get update -y && \
    apt-get install -y --fix-missing \
    build-essential
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt 


# WORKDIR /src

FROM python:3.11-slim as build-image
COPY --from=compile-image /opt/venv /opt/venv

COPY ./app /app

ENV PYTHONPATH="/src:/opt/venv"
ENV PATH="/opt/venv/bin/:$PATH"
ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "fastapi" ]
CMD ["run", "app/application/main.py", "--port", "80", "--workers", "3"] 
