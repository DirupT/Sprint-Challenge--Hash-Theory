def get_indices_of_item_weights(weights, limit):
    hash_table = {}
    for index, key in enumerate(weights):
        hash_table[key] = index

    for i, weight in enumerate(hash_table):
        try:
            return (hash_table[limit - weight], i)
        except KeyError:
            print("error")

    return ()


if __name__ == '__main__':
        # You can write code here to test your implementation using the Python repl
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))
