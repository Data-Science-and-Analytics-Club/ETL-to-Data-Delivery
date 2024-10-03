import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import cmudict
import joblib

nltk.download('cmudict')
d = cmudict.dict()

# Helper function to count syllables
def syllable_count(word):
    if isinstance(word, str):  
        try:
            return max([len([y for y in x if y[-1].isdigit()]) for x in d[word.lower()]])
        except KeyError:
            return len([char for char in word if char in 'aeiou'])  
    else:
        return 0 



train_data = pd.read_csv("modeltraining/train_data.csv")
test_data = pd.read_csv("modeltraining/test_data.csv")

# Ensure 'word' column is treated as strings and handle NaN values
train_data['word'] = train_data['Word'].astype(str)
test_data['word'] = test_data['Word'].astype(str)

# Feature extraction
def extract_features(df):
    """
    Extract features from the given DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing the 'Word' column.

    Returns:
    pd.DataFrame: DataFrame with extracted features, including word length and syllable count.
    """
    # TODO: Implement the function to fill the word_length and syllable_count features.
    pass

train_data = extract_features(train_data)
test_data = extract_features(test_data)


clf = RandomForestClassifier(random_state=42)
X_train = train_data[['word_length', 'syllable_count', 'Frequency']]
y_train = train_data['diff_level'].fillna(0).astype(int)
clf.fit(X_train, y_train)


y_test = test_data['diff_level'].fillna(0).astype(int)
X_test = test_data[['word_length', 'syllable_count', 'Frequency']]


y_pred = clf.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")

#You can unedit this line if you want to save the model
#joblib.dump(clf, 'word_difficulty_model.pkl')

print("Model training complete and saved!")