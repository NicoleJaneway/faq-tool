# set base image (host OS)
FROM python:3.7

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# set the working directory in the container
WORKDIR /code

# install dependencies
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# copy the dependencies file to the working directory
COPY app.py bert.py heroku.yml Procfile setup.sh ./

# copy the data (move this higher if the data doesn't change much)
COPY data ./data

# command to run on container start
EXPOSE 8501
CMD [ "python", "./app.py" ]
