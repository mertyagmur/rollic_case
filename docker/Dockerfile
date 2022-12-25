FROM python:3.9.13

WORKDIR /usr/src/rollic_api

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./rollic_api .

ENV FLASK_APP=rollic_api.py
ENV FLASK_DEBUG=true

CMD ["sh", "-c", "sleep 5 \ 
    && python -m flask run --host=0.0.0.0"]