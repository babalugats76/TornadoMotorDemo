#Grab the latest alpine image
FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./src /opt/app/src
ADD ./demo.py /opt/app/demo.py
WORKDIR /opt/app

# Run the image as a non-root user
RUN adduser -D user
USER user

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD python3 demo.py --port=$PORT --processes=$PROCESSES
