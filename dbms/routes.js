
const router = require('express').Router();
const { setTimeout } = require('timers/promises');

//
// db operations
//

const records = []; // {key, value, timestamp}

const compareTimestamps = (a, b) => (a.timestamp < b.timestamp) ? 1 : -1;

const saveRecord = newRecord => {
  records.unshift(newRecord);
  records.sort(compareTimestamps);
  return newRecord;
};

const getRecord = key => {
  const recordFound = records.find(record => record.key === key);
  return recordFound && recordFound.value !== 'tombstone'
    ? recordFound : undefined;
}

const getAllRecords = () => records;

const deleteAllRecords = () => {
  records.splice(0);
  return records;
};


//
// handle request
//

let delay = 0;
const pause = async () => {
  console.log('pause', delay/1000, 'seconds');
  await setTimeout(delay);
  delay = (delay < 1500) ? delay + 300 : 0;
};

router.post('*', async (req, res) => {

  // await setTimeout(500);

  console.log('request:', req.body);
  const { operation, key, timestamp } = req.body;

  switch (operation) {

    case 'set':
      await pause();
      res.json(saveRecord({
        key, timestamp,
        value: (new Date(timestamp)).toLocaleString('fi', { timeZone: 'Europe/Helsinki' })
      }));
      break;

    case 'get':
      await pause();
      res.json(getRecord(key));
      break;

    case 'del':
      await pause();
      res.json(saveRecord({
        key, timestamp,
        value: 'tombstone'
      }));
      break;

    case 'list':
      res.json(getAllRecords());
      break;

    case 'reset':
      delay = 0;
      res.json(deleteAllRecords());
      break;

    default: {
      res.json(req.body);
    }

  }

});

module.exports = router;
