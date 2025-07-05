This project builds two types of Machine Learning Algorithms which are logistic regression and Support Vector Machine (Classifier) 



#Project Goal

- Preprocesses raw text data (cleaning, tokenization, stemming, etc.)
- Converts text into numerical features using CountVectorizer - TF-IDF (CountVectorization worked better than TF-IDF for the reviews)
- Trains and compares multiple ML models (Logistic Regression, SVM)
- Evaluates model performance with real metrics
- Accepts custom user input for predictions




# What I learned from the project:

- How to clean and preprocess raw text data
- The differences between CountVectorizer and TfidfVectorizer
- How to handle class imbalance with `class_weight='balanced'` as training data were 3k for positive versus 1k for negative which makes the model biased towards positive reviews than treating them equally
- How to interpret a confusion matrix, Accuracy score
- The Importance of proper evaluation beyond just accuracy an example for that was even though the accuracy score for TF-IDF was 70% it the matrix showed no true negatives or false negatives which means the model was biased toward positive reviews.
