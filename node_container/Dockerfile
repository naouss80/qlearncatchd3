FROM mhart/alpine-node:base-8

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

EXPOSE 80 2814
CMD [ "node", "viz_server.js" ]
