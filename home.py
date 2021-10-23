from flask import Flask, redirect, render_template, request
from app.SavingAccount import SavingAccount
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/deposit',  methods=['POST', 'GET'])
def deposit():
    if request.method == "GET":
        result = request.form['deposit']
        print(result)
        final_amount = SavingAccount.caculateOneYearWithoutWithdrawal(int(result))
        print(final_amount)

if __name__ == "__main__":
    app.run()