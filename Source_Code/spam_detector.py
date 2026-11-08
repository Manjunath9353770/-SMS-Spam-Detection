# SMS Spam Detection Program

import pickle
from pathlib import Path

# Find the saved model files
folder = Path(__file__).resolve().parent

with open(folder / "spam_model.pkl", "rb") as file:
    model = pickle.load(file)

with open(folder / "tfidf_vectorizer.pkl", "rb") as file:
    tfidf = pickle.load(file)

print("=" * 45)
print("       SMS SPAM DETECTION SYSTEM")
print("=" * 45)

while True:
    message = input("\nEnter an SMS message (or type exit): ")

    if message.lower() == "exit":
        print("Program closed.")
        break

    if not message.strip():
        print("Please enter a message.")
        continue

    message_features = tfidf.transform([message])
    prediction = model.predict(message_features)[0]

    if prediction == 1:
        print("Result: SPAM MESSAGE")
    else:
        print("Result: HAM (NOT SPAM)")