FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "$PYTHONPATH:/code/src/spam_reports_project/spam_reports_project"
RUN mkdir /code
WORKDIR /code
COPY . /code/
ADD requirements.txt /code/
RUN pip install -r requirements.txt
CMD ["runserver.sh"]
