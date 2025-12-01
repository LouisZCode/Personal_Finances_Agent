
from functions import read_csvs_in_folder
from agents import financial_agent

year = 2025
data = read_csvs_in_folder(year)
#print(data)


while True:
    message = input(f"Your message:\n")

    response = financial_agent.invoke(
        {"role" : "user", "messages" : f"{message}"},
        {"configurable" : {"thread_id" : "memo_001"}}
        )

    for i, msg in enumerate(response["messages"]):
        msg.pretty_print()