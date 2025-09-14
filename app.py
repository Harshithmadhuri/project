from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_name():
   return 'Hello this is Harshith Bharadwaj'

@app.route('/app')
def return_name():
   return 'welcome to k8'

if __name__ == '__main__':
   app.run(host="0.0.0.0",port="8085")
