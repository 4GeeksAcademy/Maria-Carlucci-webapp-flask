
# your code here
from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/tree_classifier_crit-entro_maxdepth-5_minleaf-2_minsplit5_42.sav", "rb"))
class_dict = {
    "0": "No Diabetes",
    "1": "Diabetes"
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        val4 = float(request.form["val4"])
        val5 = float(request.form["val5"])
        val6 = float(request.form["val6"])
        val7 = float(request.form["val7"])
        val8 = float(request.form["val8"])
        
        data = [[val1, val2, val3, val4, val5, val6, val7, val8]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)