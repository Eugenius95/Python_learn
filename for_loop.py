from flask import Flask, render_template, request, redirect, flash
import requests, base64

app = Flask(__name__)
app.secret_key = 'secret-key'

GOOGLE_SHEET_WEBHOOK_URL = 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec'

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = {
            "branch": request.form.get("branch"),
            "role": request.form.get("role"),
            "signatory": request.form.get("signatory"),
            "date": request.form.get("date"),
            "timeIn": request.form.get("timeIn"),
            "timeOut": request.form.get("timeOut"),
            "initials": request.form.get("initials"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "signature": request.form.get("signature")
        }

        try:
            res = requests.post(GOOGLE_SHEET_WEBHOOK_URL, json=form_data)
            if res.status_code == 200:
                flash("Form submitted successfully!", "success")
            else:
                flash("Error submitting form.", "error")
        except Exception as e:
            flash(str(e), "error")

        return redirect('/')
    return render_template('form.html')
