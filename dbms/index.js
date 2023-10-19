
const express = require('express');
const routes = require(__dirname + '/routes');

const PORT = 4000;

const app = express();

app.use(express.json());
app.use(express.text());

app.use('/', routes);

app.all('*', (req, res) => {
  res.status(400).send('unknown endpoint');
});

app.use((error, req, res, next) => {
  console.error(error.message);
  res.status(400).json({error: error.message});
});

app.listen(PORT, () => {
  console.log('dbms is listening on port', PORT);
});

