FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip pip-tools


RUN mkdir /notebooks
WORKDIR /notebooks

COPY requirements.txt /notebooks/
RUN pip-compile --output-file requirements.output requirements.txt
RUN pip install -r requirements.txt

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root

