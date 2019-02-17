FROM python:3.7.2
COPY requirements.txt /opt/app/
RUN pip install -r /opt/app/requirements.txt
RUN apt-get -y update && apt-get -y install postgresql-client
COPY run.py manage.py script.sh /opt/app/
RUN chmod +x /opt/app/script.sh
COPY ./src /opt/app/src/
WORKDIR /opt/app/
EXPOSE 5000
CMD ["./script.sh", "address_book_database:5432"]
