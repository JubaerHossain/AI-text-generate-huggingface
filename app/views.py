import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import AutoModelWithLMHead, AutoTokenizer, pipeline, set_seed

# Load pre-trained GPT-2 tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelWithLMHead.from_pretrained("gpt2")

# Define a pipeline for generating text
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Set seed for reproducibility
set_seed(102)

@api_view(['POST'])
def prompt_data(request):
    prompt = request.data.get('prompt')
    generated_text = text_generator(prompt, max_length=50, do_sample=True)[0]['generated_text']

    return JsonResponse({
        'answer': generated_text,        
    }, status=status.HTTP_200_OK)
    
