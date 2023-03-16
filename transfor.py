from transformers import pipeline, BertTokenizer, BertModel
text_generator = pipeline("text-generation", model="gpt2")
generated_text = text_generator("Once upon a time")
print(generated_text[0]['generated_text'])
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
input_text = "Hello, how are you?"
inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)
embeddings = outputs.last_hidden_state
print(embeddings)
