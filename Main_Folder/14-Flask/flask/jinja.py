### Building Url Dynimically 
## variable rules 
### Jinja 2 Template Engine 

# Jinja 2 Template
'''
{{ }} exprassions to print output in html
{%...%} conditional,for loop
{#...#} this is for comment
'''

from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/")
def welcome(): 
    return "Welcome to the home page"

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/form",methods=['GET','POST'])
def form():
    # if request.method =="POST":
    #     name=request.form['name']
    #     return f"Hello  {name}!"
    return render_template("form.html")

@app.route("/submit", methods=['POST','GET'])
def submit(): 
    if request.method == "POST":
        name = request.form['name']
        return f"Hello {name}" 
    return render_template("form.html")

#Variable rule
@app.route("/suc/<int:sc>")
def suc(sc):
    return f"The score is {sc}"

# Jinja 2 Template
@app.route("/sucess/<int:score>")
def sucess(score): 
    res = ""
    if score> 50:
        res = "PASSED"
    else: 
        res = "FAILED"
    return render_template("result.html",results=res)

@app.route("/sucess1/<int:score>")
def sucess1(score): 
    res = ""
    if score> 50:
        res = "PASSED"
    else: 
        res = "FAILED"
    exp = {"score":score,"res":res}
    return render_template("result1.html",results=exp)



if __name__ == "__main__": 
    app.run(debug=True)