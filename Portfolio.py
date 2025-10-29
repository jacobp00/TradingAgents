
import json
from datetime import date
today = str(date.today())
print("Hello, welcome to your portfolio management system!")

print("Do you want to manage for todays date, [yes/no]?c Date:",today)
boolean=str(input())
if boolean=='no':
    Date=input('What date do you want to manage? format [yyyy-mm-dd]  ')
else:
    Date=today



aktier=["Google", "NVDA", "JPM", "XOM", "LLY"]




print('What stock did you manage today?')
for i in range(len(aktier)):
    print(f"({i+1}) {aktier[i]}")

print("-" * 30)  # Snygg linje

index = int(input("Select stock: "))
stock = aktier[index - 1]

print("\nYou chose:", stock)




action=input("Did you buy sell hold the stock? (buy/sell/hold) ")
entry={
    "date":Date,
    "action":action,
    "stock":stock,
}
if action in ("buy", "sell"):
    quantity=int(1)
    price=float(input("What was the price per share? "))
    entry.update({
        "quantity": quantity,
        "price": price

    })

elif action=="hold":
    note=str("Hold position today")
    entry["note"] = note

    
with open(f"{stock}.json", "a", encoding="utf-8") as f:
    json.dump(entry, f, ensure_ascii=False)
    f.write("\n")  # Gör en rad per entry

