from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bluelink')
def bluelink():
    return jsonify({"message": "Server is running!"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
