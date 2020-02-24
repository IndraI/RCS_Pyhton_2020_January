from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<page_name>')
def page(page_name):
	data = read_db()
	print(data)
	return render_template(page_name, data=data)

@app.route('/submit_message', methods=['POST', 'GET'])
def submit_message():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
	return redirect("/single-product.html")

def write_to_csv(data):
	with open('database.csv', mode="a") as f:
		name = data["name"]
		email = data["email"]
		number = data["number"]
		message = data["message"]
		csv_writer = f.write(f"{name},{email},{number},{message}\n")

def read_db():
	data = pd.read_csv("database.csv", header=None)
	data.columns = ["name", "email", "number", "review"]
	return data.to_dict('records')

if __name__ == '__main__':
    app.run(debug = True)
