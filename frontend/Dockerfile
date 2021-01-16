# Pull latest node image
FROM node:latest

EXPOSE 3000
EXPOSE 35729

# RUN mkdir /app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
# ADD package-lock.json /app/package-lock.json

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get upgrade \
    && apt-get update \
    && apt-get install

# RUN npm install --no-cache

# Install app dependencies
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
RUN npm install -g react-router-dom
RUN npm install

# Add React app to working directory
ADD . /app

# Start the React app
CMD ["npm", "start"]