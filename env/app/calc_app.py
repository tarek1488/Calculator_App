from flask import Flask,render_template , redirect


app =  Flask(__name__)

@app.route('/')
def home():
    return "hello from home page" 
if __name__ == "__main__":
    app.run()