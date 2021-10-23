from flask import Flask, redirect, render_template, request
from app.SavingAccount import SavingAccount
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/deposit',methods = ['POST', 'GET'])
def deposit():
    if request.method == "POST":
        result = request.form['deposit']
        final_amount = SavingAccount.isOneYearWithoutWithdrawal(int(result))
        print(final_amount)
        render_template("deposit.html")
    else:
        print("Error Webpage")
if __name__ == "__main__":
    app.run()