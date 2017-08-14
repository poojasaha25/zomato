const should = require("chai").should(),
assert = require ("chai").assert,
supertest = require("supertest"),
app = require("../express-boilerplate/server/server1");
var url = supertest("http://localhost:8080");
describe.only("sending null value", function(err){
  it("1", function(done){
    url
        .put("/update")
        .send()
        .expect(200)
        .end(function(err,res){
          should.not.exist(err);
           (res.text).should.equal('Enter valid id');
          done();
        });
          });
  it("2", function(done){
    url
        .put("/update")
        .send({})
        .expect(200)
        .end(function(err,res){
          should.not.exist(err);
           (res.text).should.equal('Enter valid id');
          done();
        });
          });
          it("3", function(done){
                    url
                        .put("/update")
                        .send({id:""})
                        .expect(200)
                        .end(function(err,res){
                          should.not.exist(err);
                          (res.text).should.equal('Enter the correct id');
                          done();
                        });
                          });

      it("4", function(done){
                url
                    .put("/update")
                    .send({id:"100"})
                    .expect(200)
                    .end(function(err,res){
                      should.not.exist(err);
                      (res.text).should.equal('Resturant updated');
                      done();
                    });
                      });

 });
