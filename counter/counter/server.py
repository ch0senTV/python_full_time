from flask import Flask, render_template, session, redirect, request, make_response

app = Flask(__name__)
app.secret_key = 'super_secret_key'  #generating secure secret key

@app.route('/')
def index():
    visit_count = session.get('visit_count', 0) + 1
    session['visit_count'] = visit_count

    counter = session.get('counter', 0)

    #added visits from cookies, thanks youtube :)
    actual_visits = request.cookies.get('actual_visits', 0)

    response = make_response(render_template('index.html', counter=counter, visit_count=visit_count, actual_visits=int(actual_visits) + 1))
    response.set_cookie('actual_visits', str(int(actual_visits) + 1))
    return response

@app.route('/destroy_session')
def destroy_session():
    #clearing cookie session
    session.clear()
    #redirecting route
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    #incrementing counter
    increment_value = int(request.form.get('increment_value', 1))
    session['counter'] = session.get('counter', 0) + increment_value
    return redirect('/')

@app.route('/increment_by_two')
def increment_by_two():
    #x2 for increments
    session['counter'] = session.get('counter', 0) + 2
    return redirect('/')

@app.route('/reset')
def reset():
    #reset increments in counter
    session['counter'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
