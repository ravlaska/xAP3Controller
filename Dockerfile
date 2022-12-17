FROM python:3.10.6-alpine
ADD main.py .
RUN apk update
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install python-miio
CMD ["python", "./main.py"]
