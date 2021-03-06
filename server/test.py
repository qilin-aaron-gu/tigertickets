import pymongo

client = pymongo.MongoClient('mongodb+srv://thomaslin:Tiger7252@tiger-tickets-n3wt7.mongodb.net/tigertickets?retryWrites=true&w=majority')
db = client.tigertickets
# seat = {
#     "A": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, -1, -1, -1, -1, -1,
#           -1, -1, -1, -1, -1, -1],
#     "B": [-1, -1, -1, 23, 22, 21, 20, -1, -1, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, -2, -1, -1, 4, 3,
#           2, 1, -1, -1, -1, -1],
#     "C": [-1, 27, 26, 25, 24, 23, 22, -1, -1, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -2, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "D": [30, 29, 28, 27, 26, 25, 24, -1, -1, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, -1, -1, 7,
#           6, 5, 4, 3, 2, 1, -1],
#     "E": [-1, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
#          -1, -1, -1, -1, -1, -1, -1],
#     "F": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, -1, -1,
#           -1, -1, -1, -1, -1, -1, -1],
#     "G": [-1, 26, 25, 24, 23, 22, 21, -1, -1, -1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "H": [29, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, -2, -1, -1, 7,
#           6, 5, 4, 3, 2, 1, -1],
#     "I": [29, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, -2, -1, -1, 7,
#           6, 5, 4, 3, 2, 1, -1],
#     "J": [-1, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "K": [-1, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "L": [-1, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "M": [-1, 28, 27, 26, 25, 24, 23, -1, -1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, -1, -1, 6, 5,
#           4, 3, 2, 1, -1, -1],
#     "N": [-1, 28, 27, 26, 25, 24, 23, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6,
#           5, 4, 3, 2, 1, -1, -1]
# }
# seat = {'seats': [{"row": i, 'column': seat[i]} for i in seat]}
# print(seat)
# print(db.seatmap.insert_one(seat))
import time

t1 = time.time()
string = ''
result = db.events.aggregate([
    {
        '$match': {
            'main_events.sessions.seats.person.qr_string': string
        }
    }, {
        '$project': {
            'main_events.name': 1,
            'main_events.sessions.session_date': 1,
            'main_events.sessions.week': 1,
            'main_events.sessions.seats': 1
        }
    }, {
        '$unwind': {
            'path': '$main_events'
        }
    }, {
        '$unwind': {
            'path': '$main_events.sessions'
        }
    }, {
        '$match': {
            'main_events.sessions.seats.person.qr_string': string
        }
    }, {
        '$unwind': {
            'path': '$main_events.sessions.seats'
        }
    }, {
        '$match': {
            'main_events.sessions.seats.person.qr_string': string
        }
    }
])
# result = db.events.find_one({'main_events.sessions.seats.person.qr_string': 'Hello'})
print(time.time() - t1)
print([i for i in result])
