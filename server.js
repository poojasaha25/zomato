var express = require ('express');
var app = express();
var bodyparser = require('body-parser');
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({
extended:true
}))
app.get("/",function(request,response)
{
  response.send('Hello from Express')
});
app.get("/message",function(request,response)
{
  response.send('Hello from message')
})
app.get("/product/:a/:b",function(request,response)
{
  let result = Number(request.params.a) * Number(request.params.b);
  response.send(''+result);
})
app.get("/add",function(request,response)
{
  let result = Number(request.query.num1) + Number(request.query.num2);
  response.send(''+result);
})
app.get("/data",function(request,response)
{
  let obj={'name':'Amit','age':'26','location':'Bangalore'};

  response.send(obj);
})
app.get("/data/js",function(request,response)
{
  let js={'product':'Mobile','price':'12000'};
  response.send(js);
})
app.post('/calculate/add', function(request, res) {
  //  var dataReceived = request.body;
    var num1= Number(request.body.num1);
    var num2 = Number(request.body.num2);
    var result = num1 + num2;

    res.send(''+result);
});
app.get('/:location',(req,res)=>{
res.redirect('https://developers.zomato.com/api/v2.1/locations?query='+req.params.location+'&apikey=fec96315ec6902cf4ee11a192eacc614');
})

app.listen(8080);
