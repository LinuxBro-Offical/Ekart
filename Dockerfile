FROM python:3.8

WORKDIR /app

COPY ekart/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ekart/ .

EXPOSE 8000

# Run migrations before starting the Django app
RUN python manage.py migrate

# Define the command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
