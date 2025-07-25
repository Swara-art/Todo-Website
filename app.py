from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name") # Get frorm details here
        
@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
    
