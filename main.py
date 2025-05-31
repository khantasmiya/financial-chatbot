import pandas as pd

# Sample financial data
data = {
    'Company': ['Apple', 'Apple', 'Apple', 'Samsung', 'Samsung', 'Samsung'],
    'Year': [2021, 2022, 2023, 2021, 2022, 2023],
    'Total Revenue': [300000, 320000, 340000, 280000, 290000, 310000],
    'Net Income': [50000, 52000, 55000, 46000, 47000, 49000]
}

# Create a DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by=['Company', 'Year'])

# Chatbot logic
def simple_chatbot(user_query):
    if user_query == "What is the total revenue for Apple in 2023?":
        return f"The total revenue for Apple in 2023 was ${df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Total Revenue'].values[0]:,}."

    elif user_query == "What is the total revenue for Samsung in 2023?":
        return f"Samsung's total revenue in 2023 was ${df[(df['Company'] == 'Samsung') & (df['Year'] == 2023)]['Total Revenue'].values[0]:,}."

    elif user_query == "How has Apple’s net income changed from 2022 to 2023?":
        income_2022 = df[(df['Company'] == 'Apple') & (df['Year'] == 2022)]['Net Income'].values[0]
        income_2023 = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Net Income'].values[0]
        diff = income_2023 - income_2022
        return f"Apple's net income increased by ${diff} from 2022 to 2023."

    elif user_query == "How has Samsung’s net income changed from 2022 to 2023?":
        income_2022 = df[(df['Company'] == 'Samsung') & (df['Year'] == 2022)]['Net Income'].values[0]
        income_2023 = df[(df['Company'] == 'Samsung') & (df['Year'] == 2023)]['Net Income'].values[0]
        diff = income_2023 - income_2022
        return f"Samsung's net income increased by ${diff} from 2022 to 2023."

    elif user_query == "What’s the overall revenue growth of Apple?":
        revenue_2021 = df[(df['Company'] == 'Apple') & (df['Year'] == 2021)]['Total Revenue'].values[0]
        revenue_2023 = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Total Revenue'].values[0]
        growth = ((revenue_2023 - revenue_2021) / revenue_2021) * 100
        return f"Apple's overall revenue growth from 2021 to 2023 was {growth:.2f}%."

    else:
        return "Sorry, I can only respond to predefined financial queries."

# Chat loop
print("Welcome to the Financial Chatbot! Ask me about Apple or Samsung.\n")
print("Try: 'What is the total revenue for Apple in 2023?' or type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break
    response = simple_chatbot(user_input)
    print("Bot:", response)
