from flask import Flask, request ,render_template, jsonify
import numpy as np
import pickle
from logging import FileHandler, WARNING

app= Flask(__name__ ,template_folder = 'template')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
with open("logic.pkl", "rb") as file:
    lgr = pickle.load(file)


@app.route('/')
def about():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/pred',methods=['POST'])
def pred():
    EnterGREScore =request.form['fname']
    EnterTOEFLScore =request.form['lname']
    SelectUniversityno =request.form['univer']
    EnterSOP =request.form['sop']
    Enterlor =request.form['lor']
    EnterCGPA =request.form['cgpa']
    Research =request.form['resear']
    variables =[[int(EnterGREScore),int(EnterTOEFLScore),int(SelectUniversityno),float(EnterSOP),float(Enterlor), float(EnterCGPA),int(Research)]]
    print(variables)
    prediction=lgr.predict(variables)
    print(prediction)
    output=prediction[0]
    if output == True:
        return render_template('submit.html',prediction_text="You Have Chance")
    else:
        return render_template('submit.html', prediction_text="You Have No Chance")





if __name__ == '__main__':
    app.run(debug=True)





