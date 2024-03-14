from flask import Flask, request, url_for, jsonify

app = Flask(__name__)


# GET request
@app.route('/api/history', methods=['GET'])
def api():
    data = request.get_json()
    return jsonify(data)

# POST request
@app.route('/calculate', methods=['POST'])
def calc():
    data = request.get_json()
    return jsonify(data)

# GET request
@app.route('/', methods=['GET'])
def index():
    return 'Hello World'




if __name__ == '__main__':
    app.run(debug=True)
