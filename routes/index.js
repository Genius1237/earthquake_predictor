var express = require('express');
var router = express.Router();
var appRoot = require('app-root-path');
var path = require('path');

/* GET home page. */
router.post('/predict', function (req, res, next) {
  cords = req.body.data;
  const { spawn } = require('child_process');
    const pyProg = spawn('python', [path.join(appRoot.path,'src','data_retriever.py'), '--lat', cords.lat, '--long', cords.lng, '--input', path.join(appRoot.path,'src','lat_long.npy')]);
    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.json({
          result: data.toString()
        });
    });
    pyProg.stderr.on('data', function (data) {
      console.log('stderr: ' + data.toString());
      res.json({
        result: false
      });
    });
});

router.get('/', function (req, res, next) {
  res.render('index.pug');
});

module.exports = router;