#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None]*length

    hash_map = {}

    for i in range(length):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination

        elif tickets[i].destination == "NONE":
            route[length-1] = tickets[i].source
        else:
            hash_map[tickets[i].source] = tickets[i].destination

    index = 1
    for source, destination in hash_map.items():
        if index == length - 1:
            break

        route[index] = hash_map[route[index-1]]
        index += 1
        pass

    route[length - 1] = "NONE"

    return route


def test_long_case():
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
               ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
                "SLC", "PIT", "ORD", "NONE"]

    print(reconstruct_trip(tickets, 10))


test_long_case()
