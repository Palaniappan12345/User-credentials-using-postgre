FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt 
EXPOSE 5090
ENTRYPOINT [ "python" ] 
CMD [ "application.py" ] 