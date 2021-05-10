# set base image (host OS)
FROM python:3.7

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# set the working directory in the container
WORKDIR /code

# install dependencies
COPY . .
RUN pip install -r ./requirements.txt

# command to run on container start
EXPOSE 8501
CMD [ "streamlit", "run", "http-app.py" ]