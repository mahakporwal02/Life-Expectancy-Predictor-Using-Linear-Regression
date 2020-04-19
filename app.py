
from flask import Flask, redirect, url_for, request,render_template
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle 

app = Flask(__name__) 

@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 
  
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        AM = float(request.form['c1'])
        ID = float(request.form['c2'])
        AL = float(request.form['c3'])
        PE = float(request.form['c4'])
        HEPB = float(request.form['c5'])
        MEAS = float(request.form['c6'])
        BMI = float(request.form['c7'])
        U5D = float(request.form['c8'])
        PO = float(request.form['c9'])
        TE = float(request.form['c10'])
        DIF = float(request.form['c11'])
        HIV = float(request.form['c12'])
        GDP = float(request.form['c13'])
        POP = float(request.form['c14'])
        THIN = float(request.form['c15'])
        THIN2 = float(request.form['c16'])
        ICOR = float(request.form['c17'])
        SCH = float(request.form['c18'])
        x=[[AM,ID,AL,PE,HEPB,MEAS,BMI,U5D,PO,TE,DIF,HIV,GDP,POP,THIN,THIN2,ICOR,SCH]]
        le=pickle.load(open('life expectancy.sav','rb'))
        y=le.predict(x)
        return 'answer is %f' %y
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)