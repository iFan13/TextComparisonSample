
import nltk 
from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

# define the two descriptions to compare
description1 = "The quick brown fox jumped over the lazy dog."
description2 = "The apathetic pup was leapt by the fast brown vixen."

# convert descriptions to lowercase and tokenize into words
description1_words = word_tokenize(description1.lower())
description2_words = word_tokenize(description2.lower())

# remove stopwords from the words
stop_words = set(stopwords.words('english'))
description1_words = [word for word in description1_words if word not in stop_words]
description2_words = [word for word in description2_words if word not in stop_words]

# stem words
desc1_stem = [stemmer.stem(word) for word in description1_words]
desc2_stem = [stemmer.stem(word) for word in description2_words]

# Get the synonyms of each token from both descriptions
desc1_syns = [] 
desc2_syns = [] 

for word in desc1_stem: 
	for syn in wordnet.synsets(word): 
		for l in syn.lemmas(): 
			desc1_syns.append(l.name()) 

for word in desc2_stem: 
	for syn in wordnet.synsets(word): 
		for l in syn.lemmas(): 
			desc2_syns.append(l.name())

# print sample
print(set(desc1_syns))
print(set(desc2_syns))


# calculate the percentage match
common_words = set(desc1_syns) & set(desc2_syns)
percentage_match = (len(common_words) / len(set(desc1_syns + desc2_syns))) * 100

# print the percentage match
print("Percentage match: ", percentage_match, "%")
