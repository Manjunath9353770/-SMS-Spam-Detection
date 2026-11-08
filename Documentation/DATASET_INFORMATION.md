# DATASET INFORMATION

## 1. Project Overview

Project Name: SMS Spam Detection

This project uses machine learning to classify SMS messages into two categories:
- Ham: Normal, legitimate messages.
- Spam: Unwanted or fraudulent messages.

## 2. Dataset Source

Dataset Name: SMS Spam Collection

Source: UCI Machine Learning Repository

URL: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

## 3. Dataset Description

The dataset contains SMS messages labelled as ham or spam.

It contains two columns:
- label: Message category (ham or spam).
- message: Actual SMS text.

## 4. Dataset Statistics

| Description | Count |
|---|---:|
| Original records | 5,572 |
| Original columns | 2 |
| Missing values | 0 |
| Duplicate records removed | 403 |
| Cleaned records | 5,169 |
| Ham messages after cleaning | 4,516 |
| Spam messages after cleaning | 653 |

## 5. Dataset Preprocessing

The following preprocessing operations were performed:

1. Loaded the tab-separated dataset using Pandas.
2. Assigned column names.
3. Checked missing values.
4. Identified and removed duplicate records.
5. Converted ham labels to 0.
6. Converted spam labels to 1.

## 6. Dataset Conclusion

The cleaned dataset contains 5,169 SMS messages. It is used to train and evaluate a machine learning classification model.
