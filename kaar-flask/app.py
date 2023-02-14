import os
import pandas as pd
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from pred import forecast
import csv
import json
import matplotlib.pyplot as plt

ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'

CORS(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_message(message, data = None):

    if data:

        return jsonify({'message': message, 'data': data})

    return jsonify({'message': message})


@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        file = request.files['file']

        filename = secure_filename(file.filename)
        
        if file and allowed_file(filename):

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            formdata = request.form
            
            data = handle_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename),int(formdata['days']))
            
            return send_message('File uploaded successfully', data=data)

        return send_message('File not allowed')

    return send_message('Send a file')


def handle_csv(file_name, step):
    
    print(step)

    df = pd.read_csv(file_name)    

    df.reset_index(inplace=True)

    df.fillna(0, inplace=True)

    
    try:
        df['date'] = pd.to_datetime(df['date'],dayfirst=True,format="%d-%m-%Y")
    except:
        pass
    try:
        df['date'] = pd.to_datetime(df['date'],dayfirst=True,format="%d.%m.%Y")
    except:
        pass

    df.to_csv(file_name, index=False)
    print(file_name[10:])
    
    forecast_data = forecast(
        file_name= file_name,
        time_col_name='date',
        steps = step)

    
    
    # with open("filename.csv",'w') as file:
    #     writer=csv.writer(file)
    #     writer.writerow(forecast_data)

    # df2=pd.read_csv("filename.csv")
    
    # print(df2)
    
    # ax=plt.gca()
    # plt.figure(12,12)
    # x=
    # df.plot(,color='blue',ax=ax)

    count=0
    with open("prediction/filename.csv",'w') as file:
        csv_writer=csv.writer(file)        
        for col in forecast_data:
            if count==0:
                header=col.keys()
                csv_writer.writerow(header)
                count+=1
            csv_writer.writerow(col.values())
    
    df2=pd.read_csv("prediction/filename.csv")
    print(df2)
    plt.figure(figsize=(10,10))
    
    df2['date']=pd.to_datetime(df2['date'])
    x1=df['date']
    y1=df['price']
    x2=df2['date']
    y2=df2['prediction']

    plt.plot(x1,y1,'r')
    plt.plot(x2,y2,'g')
    plt.gcf().autofmt_xdate()
    plt.xlim()
    plt.xlabel('Date')
    plt.ylabel('Prediction')
    plt.xticks(rotation=45)
    plt.legend(["past","Prediction"],loc="upper right")
    # plt.show()
    plt.savefig('../kaar-angular/src/assets/img/plot.png')
    print("********************************************************************************************")
    return forecast_data

    
if __name__ == '__main__':
    app.run()
