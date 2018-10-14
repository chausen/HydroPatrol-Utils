var nano = require('nano')('http://localhost:5984');

nano.db.list(function(err, body) {
  body.forEach(function(db) {
     nano.db.destroy(db);
  });
});
