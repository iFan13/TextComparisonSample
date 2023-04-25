
import nltk 
from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# define the two descriptions to compare
description1 = "The quick brown fox jumped over the lazy dog."
description2 = "The lazy dog was jumped over by the quick brown fox."

# convert descriptions to lowercase and tokenize into words
description1_words = word_tokenize(description1.lower())
description2_words = word_tokenize(description2.lower())

# remove stopwords from the words
stop_words = set(stopwords.words('english'))
description1_words = [word for word in description1_words if word not in stop_words]
description2_words = [word for word in description2_words if word not in stop_words]

# Get the synonyms of each token from both descriptions
desc1_syns = [] 
desc2_syns = [] 

for word in description1_words: 
	for syn in wordnet.synsets(word): 
		for l in syn.lemmas(): 
			desc1_syns.append(l.name()) 

for word in description2_words: 
	for syn in wordnet.synsets(word): 
		for l in syn.lemmas(): 
			desc2_syns.append(l.name())


# calculate the percentage match
common_words = set(desc1_syns) & set(desc2_syns)
percentage_match = (len(common_words) / len(set(desc1_syns + desc2_syns))) * 100

# print the percentage match
print("Percentage match: ", percentage_match, "%")

