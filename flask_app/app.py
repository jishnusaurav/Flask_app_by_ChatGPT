from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SurveyForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        return redirect('/thanks')
    return render_template('index.html', form=form)

@app.route('/thanks')
def thanks():
    return 'Thank you for taking our survey!'

if __name__ == '__main__':
    app.run(debug=True)
