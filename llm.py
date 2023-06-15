# insert this part into settings.py
# initialize openai
import os
import openai

# load api key from file
with open(os.getcwd() + "/openai.key", "r") as f:
    api_key = f.read()

OPENAI_API_KEY = api_key

# initialize openai
SCHEMA = "CreditCardTransactions:{TransactionID,Date,Time,Customer:{CustomerID,Name,Email,Address},Merchant:{MerchantID,Name,Location},Amount,Currency,Card:{CardNumber,ExpiryDate,CVV},TransactionType,Status},CostumerSegmentation:{CustomerID,Age,Gender,MaritalStatus,Education,Income,CreditScore,TransactionHistory:[{TransactionID,Date,Time,MerchantID,Amount,Currency,TransactionType}]}"

# add openAI key to initialize openai
openai.api_key = OPENAI_API_KEY

# functions to be called from views.py to convert user's natural langauge to query into sqlite query
def convert_to_sql(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Schema: {SCHEMA} \n Code generation: \n {query}\n SQLite Query: \n",
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response)
    return response.choices[0].text

# # fetch settings value django
# from django.conf import settings

# # fetch settings value
# OPENAI_API_KEY = settings.OPENAI_API_KEY
