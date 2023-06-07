blockchain = [[0]]

def add_value(amount):
    blockchain.append([blockchain[-1], amount])
    print(blockchain)

add_value(1.4)
add_value(2.2)
add_value(3.7)
add_value(4.1)
add_value(5.3)
