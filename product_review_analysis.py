#Task 1:
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

def review_analysis(review_list):
    split_reviews = review_list.split()
    caps_words = []
    for word in review_list:
        if word == "good":
            caps_words.append(f"{word.upper()}")
        elif word == "bad":
            caps_words.append(f"{word.upper()}")
        elif word == "poor":
            caps_words.append(f"{word.upper()}")
        elif word == "excellent":
            caps_words.append(f"{word.upper()}") 
        elif word == "average":
            caps_words.append(f"{word.upper()}")
        else:
            caps_words.append(word)
    return ''.join(caps_words)

analyzed_reviews = review_analysis(reviews)

print(analyzed_reviews)
    
#Task 2:

#Task 3:

