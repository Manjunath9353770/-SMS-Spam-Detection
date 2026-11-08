
# SMS Spam Detection Using Machine Learning

## Project Overview

This project uses machine learning and Natural Language Processing (NLP) techniques to classify SMS messages into two categories:

- **Ham:** Normal and legitimate SMS messages.
- **Spam:** Unwanted or suspicious SMS messages.

The system uses TF-IDF for text feature extraction and the Multinomial Naive Bayes algorithm for classification.

## Objectives

- Analyse and preprocess SMS messages.
- Convert text into numerical features using TF-IDF.
- Train a machine learning classification model.
- Evaluate model performance.
- Predict whether a new SMS message is spam or ham.

## Dataset

**Dataset:** SMS Spam Collection  
**Source:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/228/sms+spam+collection

| Description | Count |
|---|---:|
| Original records | 5,572 |
| Duplicate records removed | 403 |
| Cleaned records | 5,169 |
| Ham messages | 4,516 |
| Spam messages | 653 |

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Jupyter Notebook
- Visual Studio Code

## Machine Learning Workflow

1. Dataset loading
2. Data inspection
3. Duplicate removal
4. Label encoding
5. Train-test splitting
6. TF-IDF feature extraction
7. Model training
8. Model evaluation
9. SMS prediction

## Model Performance

**Algorithm:** Multinomial Naive Bayes  
**Feature extraction:** TF-IDF  
**Accuracy:** 97.39%

| Metric | Ham | Spam |
|---|---:|---:|
| Precision | 0.97 | 1.00 |
| Recall | 1.00 | 0.79 |
| F1-score | 0.99 | 0.89 |

The model correctly classified 1,007 out of 1,034 test messages. It missed 27 spam messages, so further improvement in spam detection is possible.

## Project Structure

```text
Project_2_SMS_Spam_Detection/
│
├── Dataset/
│   └── SMSSpamCollection
│
├── Notebooks/
│   └── SMS_Spam_Detection.ipynb
│
├── Source_Code/
│   ├── spam_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── spam_detector.py
│
├── Graphs/
│   ├── class_distribution.png
│   ├── confusion_matrix.png
│   └── message_length_distribution.png
│
├── Documentation/
│   ├── DATASET_INFORMATION.md
│   ├── DATASET_PREPROCESSING.md
│   ├── MODEL_TRAINING_AND_EVALUATION.md
│   ├── VISUALIZATION_AND_RESULTS.md
│   └── PROJECT_SETUP_AND_CONCLUSION.md
│
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## How to Run

Open the project folder in Visual Studio Code.

Run the prediction program from the project root:

```bash
python Source_Code/spam_detector.py
```

Enter an SMS message when prompted.

Type `exit` to close the program.

## Sample Predictions

| SMS Message | Expected Classification |
|---|---|
| Hi, are you coming to college tomorrow? | HAM |
| URGENT! Claim your free reward now! | SPAM |

## Graphs and Results

The project generates three visualizations:

1. Class distribution graph
2. Confusion matrix
3. Message length distribution graph

These graphs are available in the `Graphs` folder.

## Limitations

- Some spam messages may be incorrectly classified as ham.
- Performance depends on the training dataset.
- New spam patterns may not be recognized.

## Future Enhancements

- Improve spam detection recall.
- Experiment with other classification algorithms.
- Develop a web-based SMS detection application.
- Train with larger and more recent datasets.

## Conclusion

This project demonstrates the practical use of machine learning and NLP for SMS spam detection. The trained model achieved 97.39% accuracy on the test dataset.

## Author

**Manjunath R**

Diploma – Artificial Intelligence and Machine Learning
