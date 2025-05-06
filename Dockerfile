FROM python:3.11-slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py .

USER 100:100
#CMD [ "python", "main.py"]
CMD [ "python", "-m", "flask", "--app", "main", "run", "--host=0.0.0.0", "--debug" ]
