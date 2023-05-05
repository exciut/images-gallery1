FROM node:20.0-alpine

WORKDIR /app

EXPOSE 3000

COPY package-lock.json ./
COPY package.json ./

RUN npm install --silent

COPY . ./

CMD ["npm", "start"]