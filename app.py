import sklearn.linear_model as lin
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Load a dataset.
mygraphdata = pd.read_csv('powerproduction.csv')

#https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/models.ipynb
#https://stackoverflow.com/questions/30336324/seaborn-load-dataset
#https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/




#https://stackoverflow.com/questions/32244753/how-to-save-a-seaborn-plot-into-a-file
sns_plot = sns.pairplot(mygraphdata)
sns_plot.savefig('static/images/plot.png')


def predict_energy_from_wind_speed(text):

    text = text
    


    def do_linear_regression(data,text):

        # Load a dataset.

        powerproduction = data
        def f(speed, p):
            return p[0] + speed * p[1]

        def predict_power_output(speed):
            return round(f(speed, p),2)

        speed = powerproduction["speed"].to_numpy()
        y = powerproduction["power"].to_numpy()

        speed = speed.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(speed, y)
        r = model.score(speed, y)
        p = [model.intercept_, model.coef_[0]]

        print(predict_power_output(int(text)))

    # Load a dataset.
    df = pd.read_csv('powerproduction.csv')

    # We are removing the non zero values
    cleansed_data_2 = df.loc[df['power'] > 0 ]

    # filtering between values see https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
    zero_to_five = cleansed_data_2.loc[(cleansed_data_2['speed'] > 0) & (cleansed_data_2['speed']< 5)]
    greater_than_five_to_ten = cleansed_data_2.loc[(cleansed_data_2['speed'] > 5) & (cleansed_data_2['speed']< 10)]
    greater_than_ten_to_fifteen = cleansed_data_2.loc[(cleansed_data_2['speed'] > 10) & (cleansed_data_2['speed']< 15)]
    greater_than_fifteen_to_twenty = cleansed_data_2.loc[(cleansed_data_2['speed'] > 15) & (cleansed_data_2['speed']< 20)]
    greater_than_twenty_to_twenty_five = cleansed_data_2.loc[(cleansed_data_2['speed'] > 20) & (cleansed_data_2['speed']< 25)]

    def return_zero():
        return 0

    # If a user types wind speeds lower than 0.275 or equal higher than 24.499, it will be handled with an if statement and return 0

    if text <= 0.275:
        return_zero()

    if text >= 24.499:
        return_zero()


    #if a user inputs a wind speed between 0 - 5 mph, they will get a linear prediction from wind speed data betwween 0 and 5 mph.

    if text > 0 and text < 5:
        #Load a dataset.
        do_linear_regression(zero_to_five,text)


    #if a user inputs a wind speed between 5 - 10 mph, they will get a linear prediction from wind speed data betwween 5 and 10 mph.

    if text > 5 and text < 10:
        #Load a dataset.
        do_linear_regression(greater_than_five_to_ten,text)


    #if a user inputs a wind speed between 10 - 15 mph, they will get a linear prediction from wind speed data betwween 10 and 15 mph.
      
    if text > 10 and text < 15:
        #Load a dataset.
        do_linear_regression(greater_than_ten_to_fifteen,text)

    #if a user inputs a wind speed between 15 - 20 mph, they will get a linear prediction from wind speed data betwween 15 and 20 mph.

    if text > 15 and text < 20:
        #Load a dataset.
        do_linear_regression(greater_than_fifteen_to_twenty,text)

    #if a user inputs a wind speed between 20 - 25 mph, they will get a linear prediction from wind speed data betwween 20 and 25 mph.

    if text > 20 and text < 25:
        #Load a dataset
        do_linear_regression(greater_than_twenty_to_twenty_five,text)







from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return """ 
    <style>
    table.blueTable {
  border: 1px solid #1C6EA4;
  background-color: #EEEEEE;
  width: 100%;
  text-align: left;
  border-collapse: collapse;
}
table.blueTable td, table.blueTable th {
  border: 1px solid #AAAAAA;
  padding: 3px 2px;
}
table.blueTable tbody td {
  font-size: 13px;
}
table.blueTable tr:nth-child(even) {
  background: #D0E4F5;
}
table.blueTable thead {
  background: #1C6EA4;
  background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  border-bottom: 2px solid #444444;
}
table.blueTable thead th {
  font-size: 15px;
  font-weight: bold;
  color: #FFFFFF;
  border-left: 2px solid #D0E4F5;
}
table.blueTable thead th:first-child {
  border-left: none;
}

table.blueTable tfoot {
  font-size: 14px;
  font-weight: bold;
  color: #FFFFFF;
  background: #D0E4F5;
  background: -moz-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: -webkit-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: linear-gradient(to bottom, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  border-top: 2px solid #444444;
}
table.blueTable tfoot td {
  font-size: 14px;
}
table.blueTable tfoot .links {
  text-align: right;
}
table.blueTable tfoot .links a{
  display: inline-block;
  background: #1C6EA4;
  color: #FFFFFF;
  padding: 2px 8px;
  border-radius: 5px;
}
</style>   
    
    <img src="static/images/Wind_turbine_Holderness.jpg" alt="https://commons.wikimedia.org/wiki/File:Wind_turbine_Holderness.jpg">
    <table class="blueTable"><thead><tr><th><centre>Predict Energy Output From Wind Speed of """ + text + """ mph</centre></th></tr></thead><tbody><tr><td>""" + predict_energy_from_wind_speed(int(text)) + """ </td></tr></tbody></tr></table>
    <img src="static/images/plot.png" alt="A Matplotlibplot">
    <button onclick="goBack()">Go Back</button>

<script>
function goBack() {
  window.history.back();
}
</script>
    """ 
