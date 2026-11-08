# DATASET ANALYSIS AND PREPROCESSING

## 1. Introduction

Data preprocessing is an important step in machine learning. It prepares raw data for model training by identifying missing values, removing duplicate records, and converting text labels into numerical values.

## 2. Dataset Inspection

The SMS Spam Collection dataset was loaded using the Pandas library.

Original dataset:
- Total records: 5,572
- Total columns: 2
- Missing values: 0
- Duplicate records: 403

## 3. Duplicate Removal

Duplicate SMS records were identified and removed using the Pandas drop_duplicates() method.

After removing duplicates:
- Total records: 5,169
- Ham messages: 4,516
- Spam messages: 653

## 4. Label Encoding

The text labels were converted into numerical values:

| Original Label | Encoded Value |
|---|---:|
| Ham | 0 |
| Spam | 1 |

This conversion allows the classification algorithm to process the target labels.

## 5. Feature and Target Selection

- Input feature (X): SMS message text.
- Target variable (y): Encoded message label.

## 6. Train-Test Split

The cleaned dataset was divided into training and testing sets.

| Dataset | Records |
|---|---:|
| Training data | 4,135 |
| Testing data | 1,034 |
| Total | 5,169 |

The test size was 20%, with random_state=42 and stratified sampling.

## 7. Conclusion

The dataset was cleaned and prepared successfully. Duplicate records were removed, labels were encoded, and the data was divided into training and testing sets for machine learning.