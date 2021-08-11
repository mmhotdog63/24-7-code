from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return "24/7 Script"

app.run(host='0.0.0.0', port=8080)