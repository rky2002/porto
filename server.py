from flask import Flask,render_template,request
import csv
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/<string:page>')
def pager(page):
    return render_template(page)


def writes(data):
	with open("database.csv",newline='',mode="a") as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file =csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		file.writerow([email,subject,message])

@app.route('/submit',methods=['POST','GET'])
def submit():
	if request.method=='POST':
		data=request.form.to_dict()
		writes(data)
		return "form submitted"
	else:	
		return "something went wrong try again"
	