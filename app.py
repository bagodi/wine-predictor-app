import joblib
import os

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    Alcohol = FloatField('Alcohol: ', validators=[DataRequired()])
    Malic_acid = FloatField('Malic_acid: ', validators=[DataRequired()])
    Ash = FloatField('Ash: ', validators=[DataRequired()])
    Alcalinity_of_ash = FloatField('Alcalinity_of_ash: ', validators=[DataRequired()])
    Magnesium = FloatField('Magnesium: ', validators=[DataRequired()])
    Total_phenols = FloatField('Total_phenols: ', validators=[DataRequired()])
    Flavanoids = FloatField('Flavanoids: ', validators=[DataRequired()])
    Nonflavanoid_phenols = FloatField('Nonflavanoid_phenols: ', validators=[DataRequired()])
    Proanthocyanins = FloatField('Proanthocyanins: ', validators=[DataRequired()])
    Color_intensity = FloatField('Color_intensity: ', validators=[DataRequired()])
    Hue = FloatField('Hue: ', validators=[DataRequired()])
    HOD280_OD315_of_diluted_wines = FloatField('OD280/OD315_of_diluted_wines: ', validators=[DataRequired()])
    Proline = FloatField('Proline: ', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    specie = 'No-Image'
    if form.validate_on_submit():
        x = [[form.Alcohol.data, form.Malic_acid.data, form.Ash.data, form.Alcalinity_of_ash.data, form.Magnesium.data,
              form.Total_phenols.data, form.Flavanoids.data, form.Nonflavanoid_phenols.data, form.Proanthocyanins.data,
              form.Color_intensity.data, form.Hue.data, form.HOD280_OD315_of_diluted_wines.data, form.Proline.data]]
        specie = 'cultivars'+str(make_prediction(x))
    return render_template('index.html', form=form, specie=specie)

def make_prediction(x):
    filename = os.path.join('model','finalized_model.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]