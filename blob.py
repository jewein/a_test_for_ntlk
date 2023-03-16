from textblob import TextBlob

# 创建一个TextBlob对象
blob = TextBlob("Hello, this is a test sentence.")

# 打印情感极性和主观性
print("Sentiment Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)
