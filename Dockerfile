# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /src
ENV FLASK_APP=dockercomposeexample.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install .
EXPOSE 5000
CMD ["flask", "run", "--debug"]
