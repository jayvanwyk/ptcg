blockchain = [[0]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(amount):
    blockchain.append([get_last_blockchain_value(), amount])
    print(blockchain)

add_value(1.4)
add_value(2.2)
add_value(3.7)
add_value(4.1)
add_value(5.3)
