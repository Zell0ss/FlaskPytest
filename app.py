from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'})

@app.route('/health/')
def health():
    return jsonify({'health': 'Good, doctor!'})

@app.route('/listall')
def listall():
    return jsonify({'/': 'hello world', '/list': 'list endpoints', '/health/':'app health'})



if __name__ == '__main__':
    app.run(debug=True)
