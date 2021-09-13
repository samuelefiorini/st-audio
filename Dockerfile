FROM python:3.9
COPY ./requirements.txt /tmp/requirements.txt
RUN apt update && \
    apt install -y build-essential && \
    apt install -y libsndfile1
RUN pip install -r /tmp/requirements.txt
EXPOSE 8501
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]