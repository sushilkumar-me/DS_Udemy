from flask import Flask 
'''
It creates an instance of the Flask class, 
which will be the WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome(): 
    return "Welcome to this flask application. This should be an amazing "

@app.route("/index")
def index(): 
    return "This is the index application"

# from this part execution is start
if __name__ == "__main__": 
    app.run(debug=True)
