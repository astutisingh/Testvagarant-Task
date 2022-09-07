"""
@Author:
Name: Astuti
College: Lovely Professional University
Year of Passing: 2023
Phone Number: 9905076230
Email: astutisingh982@gmail.com


A program for Shopping Cart

Basket:
    Product         Unit Price  GST%    Quantity
1   Leather Wallet  1100        18      1 
2   Umbrella        900         12      2
3   Cigarette       200         28      3
4   Honey           100         0       4

Task:
To calculate total amount and find the product on which there is maximum GST
"""

def maxGST(GST_Dict):
    current_max = ["", 0]
    keys = GST_Dict.keys()
    for key in keys:
        value = GST_Dict[key]
        if value > current_max[1]: 
            current_max[0] = key
            current_max[1] = value
    return current_max


def calculate_amount(Basket):
    GST_Dict = {}
    TotalAmount = 0
    for dic in Basket:
        unit_price = dic["Unit_Price"]
        
        GST = (unit_price*(dic["GST"]/100))
        GST_Dict[dic["Product"]] = GST
        # print(GST_Dict)
        amount = (dic["Unit_Price"]+GST)*dic["Quantity"]
        print(amount)
        if unit_price > 500:
            amount = amount - 0.05*amount
        TotalAmount+=amount

    max_GST = maxGST(GST_Dict)
    print("Customer had pay maximum GST on: ",max_GST[0])
    return TotalAmount
            


if __name__ == '__main__':
    Basket = [
        {"Product":"Leather Wallet", "Unit_Price": 1100, "GST":18, "Quantity": 1},
        {"Product":"Umbrella", "Unit_Price": 900, "GST":12, "Quantity":2},
        {"Product":"Cigarette", "Unit_Price": 200, "GST":28, "Quantity":3},
        {"Product":"Honey", "Unit_Price": 100, "GST":0, "Quantity":4},
    ]

    print("Total amount: Rs.", calculate_amount(Basket))
