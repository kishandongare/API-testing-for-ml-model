from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('pipe.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('Company')
    typename = request.form.get('TypeName')
    ram = request.form.get('Ram')
    weight= request.form.get('Weight')
    touchscreen = request.form.get('Touchscreen')
    ips = request.form.get('Ips')
    ppi = request.form.get('ppi')
    cpu = request.form.get('Cpu brand')
    hdd = request.form.get('HDD')
    ssd = request.form.get('SSD')
    gpu = request.form.get('Gpu brand')
    os = request.form.get('os')
    input_query = np.array([[company, typename, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]])

    result = np.exp(model.predict(input_query)[0]) #np.exp() basically price in log format

    return jsonify({'price':int(result)})
if __name__ == '__main__':
    app.run(debug=True)