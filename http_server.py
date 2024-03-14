from flask import Flask, request, url_for, jsonify, render_template, redirect

app = Flask(__name__)


# GET request
@app.route('/api/history', methods=['GET'])
def api():
    data = request.get_json()
    return jsonify(data)

# POST request
@app.route('/calculate')
def calc(data = None):
    if request.method == 'POST':
        data = request.get_json()
    else:
        data = None
    return render_template('templates/calculate.html', data=data)


# GET request
@app.route('/', methods=['GET'])
def index():
    return redirect("/calculate")




if __name__ == '__main__':
    app.run(debug=True)
