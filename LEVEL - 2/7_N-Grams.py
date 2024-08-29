import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import re
import numpy

paragraph = '''I envision India as a global leader in 2047 in innovation and technology. 
            With a highly educated and skilled workforce, India will be at the forefront 
            of the Fourth Industrial Revolution, driving the development of cutting-edge 
            technologies and solutions.Additionally, I see India as a hub for international 
            trade and commerce, with a thriving business environment that attracts 
            investment from around the world. The country's diverse culture and rich history 
            will continue to be a major draw for tourists, making it a top destination for 
            cultural exchange and exploration. Overall, my vision for India in 2047 is 
            one of prosperity and progress, with a strong emphasis on sustainability and 
            social responsibility. By prioritising education, innovation, and international 
            cooperation, India has the potential to become a beacon of hope and motivation 
            for the world.'''

wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z0-9]',' ',sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating TF-IDF Model with NGrams
cv = CountVectorizer(ngram_range=(3,5))
X = cv.fit_transform(corpus).toarray()
print(X)
print(X.shape)