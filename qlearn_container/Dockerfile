FROM frolvlad/alpine-miniconda3

# Dockerfile author / maintainer 
MAINTAINER naouss80 naouss80@gmail.com

ENV TENSORFLOW_VERSION=1.3.0

RUN apk --no-cache add libstdc++
RUN pip install wheel
# Install TensorFlow
RUN pip install --ignore-installed --upgrade "tensorflow == ${TENSORFLOW_VERSION}"

# Clean up
RUN find / -depth -type d -name tests -exec rm -rf {} \;
RUN find / -depth -type d -name test -exec rm -rf {} \;
RUN find / -depth -type d -name \__pycache__ -exec rm -rf {} \;
RUN rm -rf /root/.cache

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

# Install the right pip version
RUN pip install tensorflow==1.3.0
RUN  pip install keras==1.2.2

# Install qlearncatchd3
RUN python setup.py install


# Set the default command
# ENTRYPOINT ["/usr/src/app"]