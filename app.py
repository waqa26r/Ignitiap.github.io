from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    language = request.args.get('language')
    if language == 'English':
        return 'Hello world'
    elif language == 'French':
        return 'Bonjour le monde'
    elif language == 'Hindi':
        return 'Namastey sansar'
    else:
        return 'Language not supported'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)