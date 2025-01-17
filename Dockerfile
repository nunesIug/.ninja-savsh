FROM python:3.11-alpine

WORKDIR /api/svsh/

COPY requirements.txt /api/svsh/
COPY . . 

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]