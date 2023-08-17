FROM python:3-alpine

RUN apk update
# set a directory for the app
WORKDIR /usr/src/app
# copy all the files to the container
COPY requirements.txt .
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . .

#RUN chmod +x ./wait-for

ADD https://raw.githubusercontent.com/eficode/wait-for/master/wait-for .

EXPOSE 5000

CMD ["python", "./app.py"]
