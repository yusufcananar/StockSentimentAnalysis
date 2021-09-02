import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#Read the raw data -->  https://www.kaggle.com/aaron7sun/stocknews
df = pd.read_csv('Resources/Combined_News_DJIA.csv', encoding='UTF-8')
print(df.tail())

#Split the data
train = df[df['Date'] < '2014-01-01']
test = df[df['Date'] >= '2014-01-01']
print("test : ", len(test), "\ntrain : ", len(train))
print("{:.2f}% test and {:.2f}% train".format(100*len(test)/len(df), 100*len(train)/len(df)))

#Removing Punctuations
data = train.iloc[:, 2:27]
data.replace("[^a-zA-Z]", " ", regex=True, inplace=True)
print(data.head())

#Renaming column names for ease of access
list1 = [i for i in range(len(data.iloc[0]))]
new_index = [str(i) for i in list1]
data.columns = new_index
print(data.head())

#Converting headlines to lowercase
for index in new_index:
    data[index] = data[index].str.lower()
print(data.head())

print(data.index)
headlines = []
for row in range(0, len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row, 0:25]))
print(headlines[0])

#implement BAG of Words
countVec = CountVectorizer(ngram_range=(2, 2))
trainingSet = countVec.fit_transform(headlines)

#implement RandomForest Classifier
randomClassifier = RandomForestClassifier(n_estimators=200, criterion='entropy')
randomClassifier.fit(trainingSet, train['Label'])

#Predict for the Test Dataset
test_transform = []
for row in range(0, len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
testSet = countVec.transform(test_transform)
predictions = randomClassifier.predict(testSet)

#check accuracy
matrix = confusion_matrix(test['Label'], predictions)
print(matrix)
score = accuracy_score(test['Label'], predictions)
print(score)
report = classification_report(test['Label'], predictions)
print(report)

