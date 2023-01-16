FROM python:3.10.6

WORKDIR /previdencia

COPY . /previdencia

RUN chmod +x ./install.sh

RUN ./install.sh

CMD ["uvicorn", "main:app"]