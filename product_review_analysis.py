#Task 1:


def review_analysis(review_list):
    joined_reviews = " ".join(review_list)
    caps_words = []
    for review in review_list:
        for word in review:
            if word == "good":
                caps_words.append("GOOD")
            elif word == "bad":
                caps_words.append("BAD")
            elif word == "poor":
                caps_words.append("POOR")
            elif word == "excellent":
                caps_words.append("EXCELLENT") 
            elif word == "average":
                caps_words.append("AVERAGE")
            else:
                caps_words.append(word)
    return ''.join(caps_words)

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

print(review_analysis(reviews))
    
#Task 2:

#Task 3:

