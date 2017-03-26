# Run a test server.
from flaskapp import app
from flaskapp import views
from flaskapp import models

app.run(host='127.0.0.1', port=8080, debug=True)
