from flask import Flask,render_template,request
app = Flask(__name__,static_folder="uploads")


from predict_api import get_init_model,predict

model = get_init_model()

@app.route('/')
def index():
	return render_template("index.html")

from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save('uploads/' + secure_filename(f.filename))

		text = predict('uploads/' + secure_filename(f.filename),model)
	
		return get_response_ui(result={	"url"   :   "uploads/" + secure_filename(f.filename),
										"text"  :   text})


def get_response_ui(result):
	return f"""
			<div class='row'>
				<div class='col s12 center-align'>
					<img class='z-depth-4' src='{result["url"]}'>
				</div>
			</div>
			
			<div class='container'>
				<div class='center-align'>
					<div class='card'>
					<div class='card-image'>
						<button title='caption' class='btn-floating btn-large halfway-fab waves-effect waves-light red' href='#'><i id='icon_btn' class='material-icons'>short_text</i></button>
					</div>
					<div class='card-content'>
					<br>
					<h2>{result["text"]}</h2>
					</div>
					</div>
				</div>
			</div>
		"""

if __name__ == '__main__':
	app.run()
