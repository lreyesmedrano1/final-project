# Flask Imports:
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, length

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
        'Transportation Type',
        [
            DataRequired()
        ]
    )
    
    submit_1 = SubmitField('Distance')
    submit_2 = SubmitField('CO2 Emission')
    
    



@app.route('/', methods = ['POST', 'GET'])
def homepage():
    "this function is reading the html page to allow the user to fill out the form for a designated location"
    form = MyForm() 
    transportation = ["Train", "Bus", "Plane", "Car" ]
    
    return render_template('signin.html', form=form) 


@app.route('/distance', methods = ['POST'])
def dis_data():
    """ Based on the location given in the form, the data will go to PArt1 and get the closest stop and if it is wheelchair accessible"""
    location1 = request.form['start']
    location1 = str(location1)
    location2 = request.form['end']
    location2 = str(location2)
    result = lat_long(location1, location2)

    return render_template("data_presentation.html", result=result, location1=location1,location2=location2)

@app.route('/co2_emission', methods =['POST'])
def co2_data():
    """Based on the data inputed and pressing a certain button will convert the information to what was asked in 
    the last two functions. It will render the results in  to appear"""
# def diff_distance():
#     """run program from distance.lat_long--will print the distance between two points"""
#     location1 = Location_1
#     location2 = location_2
#     return lat_long(location1,location2), render_template('data_presentation.html', form = form)
# def saved_distance():
#     """ run program from sitance.distance_calc-- will calculate what was traveled and saved. 
#     Essentially combining the travel and saved functions from distance.py """
#     return distance_calc(), render_template('data_presentation.html', form=form)










if __name__ == "__main__":
    app.run(debug=True)
