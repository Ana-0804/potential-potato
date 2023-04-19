from flask import Flask, request

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.form['input_str']
    input_str = data
    return {'output_str': input_str[::-1]}

if __name__ == '__main__':
    app.run(debug=True)
