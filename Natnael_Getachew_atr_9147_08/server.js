// import all the relevant modules here
let express = require("express");


// instantiate the app
let app = express();


// disable caching to avoid 304 responses
app.disable('etag');






app.get('/', function (request, response) {

    response.header('Content-Type', 'text/html');
   
    // reander the home page
    let home = 
    `<html>
      <body>
        <p style="font-size:140px">
          I am unattackable lol
        </p>
      </body>
    </html>`;
    for (let i = 0; i < 10000; i++) {
        let sq = i+i;
        console.log(sq);
    };
    // send the combined html to the user
    response.send(home);

});

// tell express to listen to the specified port
app.listen(8000);
