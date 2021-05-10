FROM tensorflow/tensorflow:1.12.0-py3
RUN pip install bert-serving-server[http]
RUN mkdir -p /app
COPY . /app
WORKDIR /app
EXPOSE 5555:5555 
EXPOSE 5556:5556
EXPOSE 8000:8125
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []
HEALTHCHECK --timeout=5s CMD curl -f http://localhost:8125/status/server || exit 1