from flask import Flask, request, url_for, jsonify, render_template, redirect
import datetime

app = Flask(__name__, template_folder='templates')


# GET request
@app.route('/api/history', methods=['GET'])
def api():
    data = "History data from file here..."
    return jsonify(data)

# GET request
@app.route('/history', methods=['GET'])
def history():
    data = request.get_json()
    return render_template('/history.html', data=data)

# POST request
@app.route('/calculate', methods=['GET', 'POST'])
def calc(data = None):
    if request.method == 'POST':
        history = request.form['expr']
        print("HistoryP: ", history)
        return redirect(url_for('calc'))
    else:
        history = None
        print("HistoryG: ", history)
        return render_template('/calculate.html', history=history)


# GET request
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', utc_date=datetime.datetime.utcnow())



if __name__ == '__main__':
    app.run(debug=True)
