var express = require('express')
var app = express()
var path = require ('path')
var mysql = require ('mysql')
var bodyParser = require ('body-parser')

//read from body


//configure database conection
var pool = mysql.createPool({
	host     : 'localhost',
  	user     : 'root',
  	password : 'duls3data'
})

//directori to load the files
app.use(express.static(path.join(__dirname,'content')))

//allow Body Objects to json
app.use(bodyParser());

//call DB
app.post("/dbsearch", function(req,res){
	var svc = req.body;
	var svc = svc.test

  pool.getConnection(function(err, connection) {
  	connection.query("SELECT name FROM Shitpeople.Name WHERE name like '%"+svc+"%';",function(err, rows, fields){
  		if (err) throw err;
      res.json(rows);
      connection.release();
	 });
  });
});
//DB Reconection afther time-out


//listen in the host
app.listen(80, function (){
	console.log('ready in local host')
});


