from flask import Flask, redirect ,request,render_template

app = Flask(__name__)

@app.route("/check", methods=['POST'])
def check():
    name = request.form["name"]
    age = int(request.form["age"])
    email = request.form["email"]
    agree = request.form["agree"]
    if agree == "on":
        agree = True
    else:
        agree = False
    detail = request.form["detail"]
    print(agree)
    return render_template(
        'check.html',
        name=name,
        age=age,
        email=email,
        agree=agree,
        detail=detail)

@app.route('/register', methods=['POST'])
def register():
    return redirect("/finish")

@app.route('/finish')
def finish():
    return render_template('finish.html')

@app.route('/')
def index():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)