
from nltk.corpus import wordnet

def calculate_avg_sentence_length_org(file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()

    # Clean and split each sentence into words
    sentence_lengths = [len(sentence.split()) for sentence in sentences]
    sentence_count = len(sentence_lengths)

    # Calculate the average length
    if len(sentence_lengths) == 0:
        return 0
    average_length = sum(sentence_lengths) / len(sentence_lengths)

    return average_length, sentence_count

def calculate_avg_sentence_length(file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()

    # Clean and split each sentence into words
    sentences_words_splitted = [sentence.split() for sentence in sentences]
    sentence_lengths = []
    for sentence in sentences_words_splitted:
        word_count = 0
        for word in sentence:
            if not(wordnet.synsets(word)):
                pass
            else:
                word_count += 1
        sentence_lengths.append(word_count)
    
    sentence_count = len(sentence_lengths)

    # Calculate the average length
    if len(sentence_lengths) == 0:
        return 0
    average_length = sum(sentence_lengths) / len(sentence_lengths)

    return average_length, sentence_count

def calculate_type_token_ratio(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text by splitting on whitespace
    tokens = text.split()

    # Convert tokens to lower case and calculate unique types
    types = set(token.lower() for token in tokens)

    # Calculate type/token ratio
    if len(tokens) == 0:
        return 0
    ttr = len(types) / len(tokens)

    return ttr

file_path = f"raw_data/supreme_org_test.txt"
avg_length, sentence_count = calculate_avg_sentence_length_org(file_path)
print(f"Average sentence length of original legal sentences: {avg_length:.2f} words")
print(f"Sentence count of original legal sentences: {sentence_count:.2f} sentences")
avg_word_count, _ = calculate_avg_sentence_length(file_path)
#print(f"Average word count per sentence original legal sentences: {avg_word_count:.2f} words")

#ttr = calculate_type_token_ratio(file_path)
#print(f"Type/Token Ratio: {ttr:.4f}")

file_path = f"raw_data/supreme_org_test_splitted.txt"
avg_length, sentence_count = calculate_avg_sentence_length_org(file_path)
print(f"Average sentence length of original legal sentences after splitting: {avg_length:.2f} words")
print(f"Sentence count of original legal sentences after splitting: {sentence_count:.2f} sentences")
avg_word_count, _ = calculate_avg_sentence_length(file_path)
#print(f"Average word count per sentence original legal sentences: {avg_word_count:.2f} words")

#ttr = calculate_type_token_ratio(file_path)
#print(f"Type/Token Ratio: {ttr:.4f}")

#file_path = f"raw_data/supreme_test_labels1.txt"
file_path = f"raw_data/supreme_test_labels1_splitted.txt"
avg_length, sentence_count = calculate_avg_sentence_length_org(file_path)
print(f"Average sentence length of Reference 1: {avg_length:.2f} words")
print(f"Sentence count after splitting for Reference 1: {sentence_count:.2f} sentences")
avg_word_count, _ = calculate_avg_sentence_length(file_path)
#print(f"Average word count per sentence for Reference 1: {avg_word_count:.2f} words")

#ttr = calculate_type_token_ratio(file_path)
#print(f"Type/Token Ratio: {ttr:.4f}")

#file_path = f"raw_data/supreme_test_labels2.txt"
file_path = f"raw_data/supreme_test_labels2_splitted.txt"
avg_length, sentence_count = calculate_avg_sentence_length_org(file_path)
print(f"Average sentence length of Reference 2: {avg_length:.2f} words")
print(f"Sentence count after splitting for Reference 2: {sentence_count:.2f} sentences")
avg_word_count, _ = calculate_avg_sentence_length(file_path)
#print(f"Average word count per sentence for Reference 2: {avg_word_count:.2f} words")

#ttr = calculate_type_token_ratio(file_path)
#print(f"Type/Token Ratio: {ttr:.4f}")

#file_path = f"raw_data/supreme_test_labels3.txt"
file_path = f"raw_data/supreme_test_labels3_splitted.txt"
avg_length, sentence_count = calculate_avg_sentence_length_org(file_path)
print(f"Average sentence length of Reference 3: {avg_length:.2f} words")
print(f"Sentence count after splitting for Reference 3: {sentence_count:.2f} sentences")
avg_word_count, _ = calculate_avg_sentence_length(file_path)
#print(f"Average word count per sentence for Reference 3: {avg_word_count:.2f} words")

#ttr = calculate_type_token_ratio(file_path)
#print(f"Type/Token Ratio: {ttr:.4f}")

"""
file_path = f"raw_data/supreme_org_test.txt"
avg_length = calculate_avg_sentence_length(file_path)
print(f"Average sentence length of original legal sentences: {avg_length:.2f} words")
ttr = calculate_type_token_ratio(file_path)
print(f"Type/Token Ratio: {ttr:.4f}")

file_path = f"raw_data/supreme_test_labels2.txt"
avg_length = calculate_avg_sentence_length(file_path)
print(f"Average sentence length of Reference 2: {avg_length:.2f} words")
ttr = calculate_type_token_ratio(file_path)
print(f"Type/Token Ratio: {ttr:.4f}")

file_path = f"raw_data/supreme_test_labels3.txt"
avg_length = calculate_avg_sentence_length(file_path)
print(f"Average sentence length of Reference 3: {avg_length:.2f} words")
ttr = calculate_type_token_ratio(file_path)
print(f"Type/Token Ratio: {ttr:.4f}")
"""
