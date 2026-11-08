# MODEL TRAINING AND EVALUATION

## 1. Introduction

This project uses the Multinomial Naive Bayes algorithm to classify SMS messages as ham or spam.

## 2. Text Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency) was used to convert SMS text into numerical features.

Configuration:
- Vectorizer: TfidfVectorizer
- Stop words: English
- Maximum features: 3,000

The vectorizer was fitted using training messages only. The same fitted vectorizer was used to transform testing messages.

## 3. Machine Learning Algorithm

Algorithm: Multinomial Naive Bayes

The algorithm is suitable for text classification tasks and works with numerical text features.

## 4. Model Training

The model was trained using:
- Training records: 4,135
- Input features: TF-IDF
- Target: Encoded message labels

## 5. Model Evaluation

The model was evaluated using the testing dataset.

Accuracy: 97.39%

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Ham | 0.97 | 1.00 | 0.99 | 903 |
| Spam | 1.00 | 0.79 | 0.89 | 131 |

Overall accuracy: 97.39%

### Confusion Matrix

| Actual / Predicted | Ham | Spam |
|---|---:|---:|
| Ham | 903 | 0 |
| Spam | 27 | 104 |

## 6. Results Interpretation

- 903 normal messages were correctly classified.
- 104 spam messages were correctly detected.
- 27 spam messages were incorrectly classified as normal.
- No normal messages were incorrectly classified as spam.

The model achieved good overall accuracy, but its spam recall of 79% indicates that some spam messages were missed.

## 7. Conclusion

The Multinomial Naive Bayes model achieved 97.39% accuracy on the test dataset. It successfully classifies many SMS messages, although further improvement is needed to reduce missed spam messages.