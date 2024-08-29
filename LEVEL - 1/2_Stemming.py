import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords

# PorterStemmer

paragraph = '''I envision history India as a global leader in 2047 in innovation and technology. 
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
            
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)

print(sentences)

# LancasterStemmer

paragraph = '''I envision history India as a global leader in 2047 in innovation and technology. 
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

sentences = nltk.sent_tokenize(paragraph)

lancaster = LancasterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lancaster.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)

print('\n\n')
print(sentences)

# RegexStemmer

from nltk.stem import RegexpStemmer

paragraph = '''I envision history India as a global leader in 2047 in innovation and technology. 
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
            
regex = RegexpStemmer("ing$|s$|e$|able$", min=4)
sentence = nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [regex.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)
    
print('\n')
print(sentence)


# Snowboll stemmer

from nltk.stem import SnowballStemmer

p = '''I envision history India as a global leader in 2047 in innovation and technology. 
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
            
snowball = SnowballStemmer('english', ignore_stopwords=True)
s = nltk.sent_tokenize(p)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [snowball.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)
print('\n\n')
print(paragraph)