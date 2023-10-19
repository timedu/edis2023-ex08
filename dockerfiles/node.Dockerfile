FROM node:18-slim
WORKDIR /home/dbms
RUN npm install --location=global express@4.18
