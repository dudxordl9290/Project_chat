FROM django:onbuild

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3.8", "manage.py", "runserver", "0.0.0.0:8000"]