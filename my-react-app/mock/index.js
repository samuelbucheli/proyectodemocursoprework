const express = require('express');

const paths = require('./path');

const app = express();
const PORT = '8090';

/* demo */
app.get('/demo', function(req, res) {
    const json = require(paths.DEMO);
    res.json(json);
    res.end();
});

app.listen(PORT, function() {
    console.log(`mock server start at localhost: ${PORT}`);
});
