movies = ["The Holy Grail",1975,
          "The Life of Brain", 1979,
          "The Meaning of Life",1983]

for each_flick in movies:
    print(each_flick)

print("===============================")
count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1

print("===============================")
movies2 = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam",91,
           ["Graham Chapman", ["Michael Palin","John Cleese",
                "Terry Gilliam","Eric Idle", "Terry Jones"]]]

for each_item in movies2:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
