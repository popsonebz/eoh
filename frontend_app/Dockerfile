FROM node:11.9.0

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY ./address-book/package.json /usr/src/app/package.json
RUN npm install
RUN npm install -g @angular/cli@6.1.4

COPY ./address-book /usr/src/app

EXPOSE 4200

CMD ng serve --host 0.0.0.0
