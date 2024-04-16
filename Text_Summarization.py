# import torch
# import re
# from transformers import AutoTokenizer
# from transformers import AutoModelForSeq2SeqLM

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print(device)
# tokenizer = AutoTokenizer.from_pretrained("vishnun0027/Text_Summarization_model_15042024")
# model = AutoModelForSeq2SeqLM.from_pretrained("vishnun0027/Text_Summarization_model_15042024")


# def Summarise_text(text):
#     text = re.sub('\s+', ' ', text)
#     # Tokenize the text
#     inputs = tokenizer(text, return_tensors="pt").input_ids 
#     print(inputs)
#     outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)   
#     # Get the predicted
#     predicted = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     return predicted


from transformers import pipeline
import re

summarizer = pipeline("summarization", model="vishnun0027/Text_Summarization_model_15042024")

def Summarise_text(text):
    text = re.sub('\s+', ' ', text)
    prediction =summarizer(text)
    prediction = prediction[0]['summary_text']
    return prediction