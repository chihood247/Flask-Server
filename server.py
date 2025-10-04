from flask import Flask, request, redirect, url_for

#passphrase
#keyphrase

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('server'))

@app.route('/submit', methods = ["GET", "POST"])
def server():
    if request.method == 'GET':
        return 'Server Page'
    
    else:
        pass_phrase = request.form.get('passphrase')

        key_phrase = request.form.get('keyphrase')

        return f'<p>{pass_phrase}</p><p>{key_phrase}</p>'

if __name__ == '__main__':
    app.run(debug = True)