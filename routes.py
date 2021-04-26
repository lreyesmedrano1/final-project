# Flask Imports:
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, length
import math

#Function Imports:
from distance import lat_long, travel, saved, distance_calc

app = Flask(__name__)


SECRET_KEY = "efgh"
app.config['SECRET_KEY'] = SECRET_KEY


class MyForm(FlaskForm):
    """Contact/Location form."""
    start = StringField(
        'Start Destination',
        [DataRequired()]
    )
    
    end = TextField(
        'End destination',
        [
            DataRequired()
        ]
    )
    
    method = TextField(
        'Transportation',
        [
            DataRequired()
        ]
    )
    c_travel_type = SelectField('Car type', choices =[(' '),('Gas'), ('Electric'),('Plugin'),('Hybrid')])
    t_travel_type = SelectField('Train type',choices = [(' '),('Electric'), ('Fossil Fuel')])
    p_travel_type= SelectField('Plane type', choices=[(' '),('domestic'), ('long haul')] )

    people = SelectField("If in a car, How many people were there?", choices=[(' '),('1'),('2'),('3'),('4')])
    
    submit_1 = SubmitField('Distance')
    submit_2 = SubmitField('CO2 Emission')
    
    



@app.route('/', methods = ['POST', 'GET'])
def homepage():
    "this function is reading the html page to allow the user to fill out the form for a designated location"
    form = MyForm() 
    # transportation = ["Train", "Bus", "Plane", "Car" ]
    
    return render_template('signin.html', form=form) 


@app.route('/distance', methods = ['POST'])
def dis_data():
    """ Based on the location given in the form, the data will go to PArt1 and get the closest stop and if it is wheelchair accessible"""
    location1 = request.form['start']
    location2 = request.form['end']
    result = lat_long(location1, location2)

    return render_template("data_presentation.html", result=result, location1=location1,location2=location2)

@app.route('/co2_emission', methods =['POST'])
def co2_data():
    """Based on the data inputed and pressing CO2 Emission will convert the information to what was asked in 
    the last two functions. It will render the results in  to appear"""
    em=0
    location1 = request.form['start']
    location2 = request.form['end']
    train_type = request.form['t_travel_type']
    car_type =request.form['c_travel_type']
    car_type = str(car_type)
    plane_type =request.form['p_travel_type']
    plane_type = str(plane_type)
    a_people = request.form['people']
    a_people = str(a_people)
    distance = lat_long(location1, location2)
    typer = request.form['method']
    typer = str(typer)
    outcome, em_round = travel(typer,distance)
    extra_percent= saved(typer,distance,em)
    
    return render_template('co2_data.html', outcome=outcome, em_round=em_round,extra_percent=extra_percent )











if __name__ == "__main__":
    app.run(debug=True)
