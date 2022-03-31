# Restaurant-Review-Sentiment-Analysis
It is a NLP based project on Sentiment Analysis. The objective of the project is to predict whether a particular review is positive or negative. I have used a text csv file which consists of reviews of different restaurants. Positive review is labelled as 1 while negative review is marked as 0. The data was preprocessed first using Tokenization and Stemming. Then, I have created vectors using Bag of Words Technique. A Naive Bayes model is created with these vectors where I achieved a precision of 0.79 on training dataset while 0.76 on test dataset. Also tried other algorithms such as Random Forest and Logistic Regression using cross validation, but Naive Bayes provides better results.

The web app is deployed using flask on local host. Below are the snippets of the working of the app.
Start Page
<img width="479" alt="start page" src="https://user-images.githubusercontent.com/83235872/161115750-b501d139-3fc1-4088-a9ba-7ef3c377cad9.png">

Using a Positive Review and Result
<img width="443" alt="positive comm" src="https://user-images.githubusercontent.com/83235872/161115858-bfc05a51-280d-4205-9302-c52e71524655.png">
<img width="677" alt="positive pred" src="https://user-images.githubusercontent.com/83235872/161115876-ff0ded60-d1cb-417b-9630-9cebdcfd2619.png">

Using a Negative Review and Result
<img width="452" alt="neg comm" src="https://user-images.githubusercontent.com/83235872/161115987-0fe9efed-9fa6-48c9-bcb7-1f1f7b08d139.png">
<img width="635" alt="negative review" src="https://user-images.githubusercontent.com/83235872/161116008-94bbea9b-835c-44a9-948b-7cae2e02c0d5.png">
