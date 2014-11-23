var express = require('express')
var app = express();
var path = require ('path')

//configure app
app.set('view engine','ejs')
app.set('views',path.join(__dirname,'views'))

//use middleware
app.use(express.static(path.join(__dirname,'foundation')))

//define routes

app.get('/', function(req,res){
	res.render('index.ejs');

});

app.listen(80, function (){
	console.log('ready in local host')
})


