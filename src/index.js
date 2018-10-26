var express = require('express');
var router = express.Router();
var appRoot = require('app-root-path');
var path = require('path');

/* GET home page. */
router.post('/predict', function (req, res, next) {
  cords = req.body.data;
  const { spawn } = require('child_process');
  console.log(path.join(appRoot.path,'src','data_retriever.py'));
    const pyProg = spawn('python', [path.join(appRoot,'data_retriever.py'), '--lat', cords.lat, '--long', cords.lng, '--input', path.join(appRoot,'lat_long.npy')]);
    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.json({
          result: data
        });
    });
    pyProg.stderr.on('data', function (data) {
      console.log('stderr: ' + data.toString());
    });
    pyProg.on('exit', function (code) {
      console.log('child process exited with code ' + code.toString());
    });
});

router.get('/', function (req, res, next) {
  res.render('index.pug');
});

module.exports = router;