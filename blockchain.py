blockchain = [0]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)

add_value(1.4,[1])
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=1.34)
add_value(3.7)
add_value(4.1)
add_value(5.3)
