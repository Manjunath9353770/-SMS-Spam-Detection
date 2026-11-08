# VISUALIZATION AND RESULTS

## 1. Introduction

Data visualization helps understand the SMS dataset and evaluate the performance of the machine learning model.

Three graphs were generated for this project.

## 2. Class Distribution Graph

File: class_distribution.png

This bar chart displays the number of ham and spam messages in the cleaned dataset.

- Ham messages: 4,516
- Spam messages: 653

It shows that the dataset contains more normal messages than spam messages.

## 3. Confusion Matrix

File: confusion_matrix.png

The confusion matrix displays the actual and predicted classifications.

| Actual / Predicted | Ham | Spam |
|---|---:|---:|
| Ham | 903 | 0 |
| Spam | 27 | 104 |

The model correctly classified 903 ham messages and 104 spam messages.

## 4. Message Length Distribution

File: message_length_distribution.png

This histogram compares the character lengths of ham and spam messages.

It helps examine differences in message length between the two categories.

## 5. Model Performance

- Algorithm: Multinomial Naive Bayes
- Feature extraction: TF-IDF
- Accuracy: 97.39%
- Test records: 1,034

The model correctly classified 1,007 out of 1,034 test messages.

## 6. Conclusion

The visualizations provide an overview of dataset distribution, message length, and classification performance. They help explain the model's results and identify areas for improvement.