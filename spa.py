import spacy

# 加载英文预训练模型
nlp = spacy.load("en_core_web_sm")

# 示例文本
text = "SpaCy is a popular NLP library."

# 对文本进行处理
doc = nlp(text)

# 打印分词和词性标注结果
for token in doc:
    print(token.text, token.pos_, token.tag_)
