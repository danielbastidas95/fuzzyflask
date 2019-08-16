/*
var sqlite3 = require('sqlite3').verbose()
var db = new sqlite3.Database('abcd2')
db.serialize(function(){
    db.run("CREATE TABLE user (id INT, dt TEXT)");

    var stmt = db.prepare("INSERT INTO user VALUES (?,?)");
    for (var i = 0; i<10; i++){
        var d = new Date();
        var n = d.toLocaleTimeString();
        stmt.run(i,n);
    }
    stmt.finalize();

    db.each("SELECT id, dt FROM user", function(err, row){
        console.log("user id: " + row.id, row.dt);
    });

});
*/

var sqlite3 = require('sqlite3').verbose()
var db = new sqlite3.Database('')
db.serialize(function(){
    db.run("CREATE TABLE user (id INT, dt TEXT)");

    var stmt = db.prepare("INSERT INTO user VALUES (?,?)");
    for (var i = 0; i<10; i++){
        var d = new Date();
        var n = d.toLocaleTimeString();
        stmt.run(i,n);
    }
    stmt.finalize();

    db.each("SELECT id, dt FROM user", function(err, row){
        console.log("user id: " + row.id, row.dt);
    });

});

/*
function fetchDataFromSQLiteDB() {
    //used http://sqlitebrowser.org/ for creating database
    var conn = SQL.connect( { Driver: "SQLite",
    Database: "C:\\Users\\Tesis\\fuzzyflask\\database.db"} );
    var result = conn.query("SELECT id, title, iniciativa_11, iniciativa_12, FROM objetivo1;");
    console.log(result);
    if(result.isValid == false) {
        test.log("Result is not valid, maybe no entries in database?")
    } else {
        while (result.isValid) {
            // do something with the result
            var id = result.value(0)
            var title = result.value(1)
            var iniciativa_11 = result.value(2)
            var iniciativa_12 = result.value(3)
            //test.log(id + forename + surname + email + phone)
            addEntry(title, iniciativa_11, iniciativa_12)
            console.log(iniciativa_11, iniciativa_12);
            result.toNext();
        }
    test.log("added " + id + " entries in the addressbook application")
    console.log(iniciativa_11, iniciativa_12);
 }
 console.log(result);
}
*/