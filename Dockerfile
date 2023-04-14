FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update -y && apt-get upgrade -y 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /Bikash/
WORKDIR /Bikash/
RUN pip3 install --no-cache-dir --upgrade --requirement Installer
CMD python3 -m Bikash.py
