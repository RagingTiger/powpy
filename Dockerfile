# get a slime python3 base image
FROM python:3.8.2-alpine3.10

# set workdir
ARG SRC_DIR=/usr/local/share/powpy
WORKDIR $SRC_DIR

# grab src
COPY src/requirements.txt .

# get requirements
RUN pip3 install -r requirements.txt

# get remaining src
COPY src/ .

# link src
RUN ln ${SRC_DIR}/pow.py /usr/bin/pow.py

# set the command
ENTRYPOINT ["python", "/usr/bin/pow.py"]
CMD ["example"]
