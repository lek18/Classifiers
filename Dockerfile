FROM python:3.8-slim-buster

#RUN apt-get -y update && apt-get install -y libzbar-dev
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./churn/

#ENV PYTHONPATH "${PYTHONPATH}:/churn"

CMD ["python","/app/churn/main.py", "/app/churn/"]