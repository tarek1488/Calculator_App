from flask import Flask,render_template , redirect
from calc_class import Calculator


app =  Flask(__name__)

calculator = Calculator()

@app.route('/')
def home():
    return render_template('homepage.html') 

@app.route('/calculate',methods = ['POST'] )
def calculate():
    pass
    




if __name__ == "__main__":
    app.run(debug=True,port=9000)