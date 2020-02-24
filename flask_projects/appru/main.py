from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_message', methods=['POST', 'GET'])
def submit_message():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
	return redirect("/thanks.html")

def write_to_csv(data):
	with open('database.csv', mode="a") as f:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = f.write(f"{name},{email},{subject},{message}\n")

if __name__ == '__main__':
    app.run(debug = True)
