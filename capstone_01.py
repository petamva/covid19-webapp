from flask import Flask, url_for, redirect, render_template, session
from datetime import datetime
import tensorflow as tf
import numpy as np
import joblib
from infoform import InfoForm

app = Flask(__name__)
# Set up your imports and your flask app.
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = InfoForm()

    if form.validate_on_submit():
        session['country'] = form.country.data
        session['date'] = form.date.data
        return redirect(url_for("report"))

    return render_template('my_home.html', form=form)


@app.route('/report')
def report():
    n = (datetime.strptime(session['date'], '%Y-%m-%d')-datetime(2021, 6, 16)).days
    # path01 = rf'./models/{session["country"].lower()}.h5'
    # path02 = rf'./batches/{session["country"].lower()}.npy'
    # path03 = rf'./scalers/{session["country"].lower()}.pkl'
    path01 = rf'./models/{session["country"]}.h5'
    path02 = rf'./batches/{session["country"]}.npy'
    path03 = rf'./scalers/{session["country"]}.pkl'
    new_model = tf.keras.models.load_model(path01)
    first_eval_batch = np.load(path02)
    new_scaler = joblib.load(path03)
    test_predictions = []
    current_batch = first_eval_batch[np.newaxis, ...]
    for i in range(n):
        current_pred = new_model.predict(current_batch)[0]
        test_predictions.append(current_pred)
        current_batch = np.append(current_batch[:,1:,:],[[current_pred]], axis=1)
    true_predictions = new_scaler.inverse_transform(test_predictions)
    predicted_cases = true_predictions[:, 0]
    cases = int(predicted_cases[-1])
    if cases < 0:
        cases = 0 
    return render_template('myreport.html', cases=cases)


if __name__ == '__main__':
    app.run(debug=True)
