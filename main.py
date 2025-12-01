
from functions import read_csvs_in_folder
from agents import financial_agent

year = 2025
data = read_csvs_in_folder(year)
#print(data)


message = input(f"Your message:/n")

response = financial_agent.invoke({"role" : "user", "messages" : f"{message}"})

for i, msg in enumerate(response["messages"]):
    msg.pretty_print()