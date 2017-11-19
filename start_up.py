
def test(collect):
    print(collect)


collection = []
for i in range(1,10):
    global collection
    collection.append(i)
test(collection)