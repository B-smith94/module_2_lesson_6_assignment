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
    
    for words in review.split():
        index = words.find('.')
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
    print(review_no_period)

#Task 2:
def sentiment_tally():
    pass
#Task 3:

