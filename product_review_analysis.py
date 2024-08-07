#Task 1:
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
rating = ['good', 'bad', 'excellent', 'poor', 'average']

for review in reviews:
    buzzwords = []
    index = review.find('.')
    for words in review.split():
        word = words.strip('.')
        if word.lower() == 'good':
            buzzwords.append('GOOD')
        elif word.lower() == 'bad':
            buzzwords.append('BAD')
        elif word.lower() == 'poor':
            buzzwords.append('POOR')
        elif word.lower() == 'excellent':
            buzzwords.append('EXCELLENT')
        elif word.lower() == 'average':
            buzzwords.append('AVERAGE')
        else:
            buzzwords.append(word)
        
    review_no_period = ' '.join(buzzwords)
    analyzed_reviews = review_no_period[:index] + "." + review_no_period[index:]
    individual_reviews = '--' + analyzed_reviews[0:]
    print(individual_reviews)

#Task 2:
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(positive, negative):
    for review in reviews:
        index = reviews.index(review)
        for words in positive_words:
            if words in review:
                positive_total = review.count(words)
                print(f"Positive word total in review number {index+1}: {positive_total}")
        for words in negative_words:
            if words in review:
                negative_total = review.count(words)
                print(f"Negative word total in review number {index+1}: {negative_total}")

sentiment_tally(positive_words, negative_words)

#Task 3:

for review in reviews:
    if review[:30].endswith(" "):
        summary = review[:30] + "..."
        print(f"Summary: {summary}")
    elif review[:31].endswith(" "):
        summary = review[:31] + "..."
        print(f"Summary: {summary}")
    elif review[:32].endswith(" "):
        summary = review[:32] + "..."
        print(f"Summary: {summary}")
    elif review[:33].endswith(" "):
        summary = review[:33] + "..."
        print(f"Summary: {summary}")
    else:
        break