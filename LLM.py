from config import HF_API_KEY
import requests

DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(ModelName):
    return f"https://router.huggingface.co/hf-inference/models/{ModelName}"
def query(payload,ModelName = DEFAULT_MODEL):
    ApiUrl=build_api_url(ModelName)
    headers = {"Authorization":f"Bearer {HF_API_KEY}"}
    response = requests.post(ApiUrl,headers=headers,json=payload)
    return response.json()
def SummarizeText(text,MinLength,MaxLength,ModelName = DEFAULT_MODEL):
    payload={
        "inputs":text,
        "parameters":{"MinLength":MinLength, "MaxLength":MaxLength}
    }
    print(f"AI summarization using model: {ModelName}")
    result = query(payload,ModelName=ModelName)
    if isinstance(result,list) and result and "SummaryText" in result[0]:
        return result[0]["SummaryText"]
    else:
        print("Error", result)
        return None
if __name__=="__main__":
    user_name = input("your name").strip()
    if not user_name:
        user_name = "user"
    print(f"Welcome {user_name}, enter text to see an ai response.")
    user_text = input("Please enter text you want to see the ai summarize.")
    if not user_text:
        print("Please enter text")
    else:
        ModelChoice = input("Enter the model name, ex: facebook/bart-large-cnn").strip()
        if not ModelChoice:
            ModelChoice = DEFAULT_MODEL
        StyleChoice = input("Choose your style \n 1. standard (quick and concise) 2. enchanced (detailed)")
        if StyleChoice == "2":
            MinLength = 80
            MaxLength = 200
            print("Enchanced Summarization...")
        else:
            MinLength = 50
            MaxLength = 150
            print("Using Standard Summary...")
        Summary = SummarizeText(user_text,MinLength,MaxLength,ModelName=ModelChoice)

        if Summary:
            print(f"AI summarized {user_name}'s text.")
            print (Summary)
        else:
            print("AI failed to summarize your text")
