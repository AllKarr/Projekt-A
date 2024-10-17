from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/artist')
def artist():
    return render_template('artist.html')

@app.route('/listener')
def listener():
    return render_template('listener.html')

@app.route('/producer')
def producer():
    return render_template('producer.html')

if __name__ == '__main__':
    app.run(debug=True)
