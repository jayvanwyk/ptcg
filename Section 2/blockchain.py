#Initializing our blockchain list
blockchain = [0]


def get_last_blockchain_value():
    """Returns the last value o f the current blockchain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
    """Append a new, and the last value of the blockchain, to the blockchain
    
       Arguments:
            :transaction_amount: The amount that should be added.
            :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """Returns the input of the user (a new transaction amount) as a float."""
    return float(input("Your transaction amount please: "))


add_value(get_user_input(), get_last_blockchain_value())
add_value(get_user_input(), get_last_blockchain_value())
add_value(get_user_input(), get_last_blockchain_value())

print(blockchain)