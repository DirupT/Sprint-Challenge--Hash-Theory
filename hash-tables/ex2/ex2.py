def reconstruct_trip(tickets):
    hash_table = {}
    for key, value in tickets:
        hash_table[key] = value

    tickets = []
    start = hash_table[None]
    for key, value in hash_table.items():
        if start is not None:
            tickets.append(start)
            try:
                start = hash_table[start]
            except KeyError:
                return []

    return tickets


if __name__ == '__main__':
    incorrect_set = [
        ('LHD', 'DAB'),
        (None, 'HVN'),
        ('MSO', 'SFO'),
        ('RDU', 'ABQ'),
        ('ACY', None),
    ]
    print(reconstruct_trip(incorrect_set))
