from flask import Flask, request, url_for, jsonify, render_template, redirect
from datetime import datetime, timezone

app = Flask(__name__, template_folder='templates')

# file handling
def write_to_file(data):
    with open('history.txt', 'a') as file:
        file.write(data + '\n')


def read_from_file():
    with open('history.txt', 'r') as file:
        return file.readlines()
    
#error catching
@app.errorhandler(404)   
def not_found(e): 
  print("404 error NOT FOUND!")
  return render_template("404.html") 


# GET request for history api
@app.route('/api/history', methods=['GET'])
def api():
    print('Serving \'api/history\'')
    data = read_from_file()
    return jsonify(data)


# GET request to return calculation history
@app.route('/history', methods=['GET'])
def history():
    history = read_from_file()
    return render_template('/history.html', history=history)


# POST and GET request for calculator
@app.route('/calculate', methods=['GET', 'POST'])
def calc(data = None):
    if request.method == 'POST':
        expr = request.form['expr']
        try :
            result = eval(expr) # executes valid python code, irl this is a vulnerability
        except:
            result = "Invalid expression"
        write_to_file(expr + ' = ' + str(result))
        print("Serving History Post: ", history)
        return render_template('/calculate.html', expr=expr, result=result, utc_date=datetime.now(timezone.utc))
    else:
        print('Serving \'calculate.html\'')
        return render_template('/calculate.html', utc_date=datetime.now(timezone.utc))


# GET request
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('calc'))



if __name__ == '__main__':
    app.run(debug=True)
