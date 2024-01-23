from flask import Flask, render_template, request, redirect, url_for

app = Flask('dojos_and_ninjas_3')

dojos_data = [
    {'dojo_id': 1, 'names': 'Dojo 1', 'created_at': '', 'updated_at': ''},
    {'dojo_id': 2, 'names': 'Dojo 2', 'created_at': '', 'updated_at': ''},
]

ninjas_data = {
    1: [
        {'ninjas_id': 1, 'first_name': 'Ninja 1', 'last_name': 'Ninja 1','created_at': '', 'updated_at': '' },
        {'ninjas_id': 1, 'first_name': 'Ninja 1', 'last_name': 'Ninja 1','created_at': '', 'updated_at': '' },
    ],
    2: [
        {'ninjas_id': 1, 'first_name': 'Ninja 1', 'last_name': 'Ninja 1','created_at': '', 'updated_at': '' },
        {'ninjas_id': 1, 'first_name': 'Ninja 1', 'last_name': 'Ninja 1','created_at': '', 'updated_at': '' },
    ],
}

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos=dojos_data)

@app.route('/dojo/<int:dojo_id>')
def dojo_show(dojo_id):
    dojo_data = {'id': dojo_id, 'name': f'Dojo {dojo_id}'}
    ninjas_for_dojo = ninjas_data.get(dojo_id, [])
    return render_template('dojo_show.html', dojo=dojo_data, ninjas=ninjas_for_dojo)
@app.route('/ninjas')
def ninjas():
    return render_template('add_ninja.html', dojos=dojos_data)

@app.route('/ninjas/add', methods=['POST'])
def add_ninja():
    ninja_name = request.form.get('name')
    dojo_id = int(request.form.get('dojo'))

    if not ninja_name or dojo_id not in ninjas_data:
        return redirect(url_for('ninjas'))

    new_ninja = {'id': len(ninjas_data[dojo_id]) + 1, 'name': ninja_name}
    ninjas_data[dojo_id].append(new_ninja)

    return redirect(url_for('dojo_show', dojo_id=dojo_id))


@app.route('/dojos/add', methods=['GET', 'POST'])
def add_dojo():
    if request.method == 'POST':
        new_dojo_name = request.form.get('name')
        new_dojo_id = len(dojos_data) + 1
        new_dojo = {'id': new_dojo_id, 'name': new_dojo_name}
        dojos_data.append(new_dojo)
        return redirect(url_for('dojos'))
    return render_template('add_dojo.html')
