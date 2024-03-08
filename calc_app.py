from flask import Flask,render_template , redirect ,request



app =  Flask(__name__)



@app.route('/')
def home():
    return render_template('homepage.html') 

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['screen']
    try:
        result = eval(expression)
        print(result)
        return render_template('homepage.html' ,result = result , expr = expression)
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return redirect('/')

    

if __name__ == "__main__":
    app.run(debug=True,port=9000)