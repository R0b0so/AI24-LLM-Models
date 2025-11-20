from config import HF_API_KEY
import requests

DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):
    return f"https://router.huggingface.co/hf-inference/models/{model_name
}"
def query(payload,model_name = DEFAULT_MODEL):
    ApiUrl=build_api_url(model_name
)
    headers = {"Authorization":f"Bearer {HF_API_KEY}"}
    response = requests.post(ApiUrl,headers=headers,json=payload)
    return response.json()
def SummarizeText(text,min_length,max_length,model_name = DEFAULT_MODEL):
    payload={
        "inputs":text,
        "parameters":{"min_length":min_length, "max_length":max_length}
    }
    print(f"AI summarization using model: {model_name}")
    result = query(payload,model_name
=model_name
)
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
            min_length = 80
            max_length = 200
            print("Enchanced Summarization...")
        else:
            min_length = 50
            max_length = 150
            print("Using Standard Summary...")
        Summary = SummarizeText(user_text,min_length,max_length,model_name
    =ModelChoice)

        if Summary:
            print(f"AI summarized {user_name}'s text.")
            print (Summary)
        else:
            print("AI failed to summarize your text")
