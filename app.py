from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Simple App</title></head>
    <body>
        <h1>Welcome to Flask App</h1>
        <form action="/submit" method="post">
            <label for="data">Enter some data:</label><br>
            <input type="text" id="data" name="data"><br><br>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('data')
    return f"You submitted: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
