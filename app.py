# Importing essential libraries
from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np

app = Flask(__name__, template_folder= r'C:\Users\sarth\py4e\Restaurant Review Sentiment Analysis\client')

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = r'C:\Users\sarth\py4e\Restaurant Review Sentiment Analysis\model\Restaurant_Review_model.pickle'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open(r'C:\Users\sarth\py4e\Restaurant Review Sentiment Analysis\model\cv-transform.pkl','rb'))



@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)