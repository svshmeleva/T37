import spacy

nlp = spacy.load("en_core_web_sm")

sentence_one = "The girl told the story cried."
sentence_two = "The horse raced past the barn fell."
sentence_three = "Mary gave the child the dog bit a Band-Aid."
sentence_four = "The cotton clothing is made of grows in Mississippi."
sentence_five = "The old man the boat."

gardenpathSentences = [sentence_one, sentence_two, sentence_three, sentence_four, sentence_five]

i = 1
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print(f"sentence {i}: {sentence}")
    print("Tolkenisation:")
    print([token.orth_ for token in nlp_sentence if not token.is_punct | token.is_space])
    print("Part of speech:")
    print([(token.text, token.pos_, token.dep_) for token in nlp_sentence])
    print("Entity recognition:")
    print([(token, token.label_, token.label) for token in nlp_sentence.ents])
    print("Lemmatisation:")
    print([token.lemma_ for token in nlp_sentence])
    print("\n")
    i += 1


print("=======================================")