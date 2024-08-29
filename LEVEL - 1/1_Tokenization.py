import nltk

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
            
sentences = nltk.sent_tokenize(paragraph)
print(sentences)
print(len(sentences))

words = nltk.word_tokenize(paragraph)
print(words)
print(len(words))

# sent_tokenizor
# word_tokenizor
# wordpunct_tokenizor
# TreebankWordTokenizer
