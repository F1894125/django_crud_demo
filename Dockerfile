FROM python:3.12-slim

WORKDIR /django_crud_demo

COPY . .

RUN pip install django==5.2.12

RUN chmod +x start.sh

EXPOSE 8000

CMD ["./start.sh"]