from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'dojo_survey_secret_key'


@app.route('/')
def index() -> str:
    session.clear();
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def show_responses() -> str:
    return render_template('result.html', results_dict=session)



if __name__ == '__main__':
    app.run(debug=True)
