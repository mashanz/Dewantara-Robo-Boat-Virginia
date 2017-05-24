# max X = 800px
# max Y = 600px
# width = w (min 25)
# height = h (min 25)

# area dibagi menjadi 10 kolom

def area(conn):
    while(1):
        x = conn.recv()
        x = x.__getitem__(0)
        if x >=0 and x < 160:
            print("area 1")
        elif x >=160 and x < 320:
            print("area 2")
        elif x >=320 and x < 480:
            print("area 3")
        elif x >=480 and x < 640:
            print("area 4")
        elif x >=640 and x < 800:
            print("area 5")
        else:
            print("area unknown")
