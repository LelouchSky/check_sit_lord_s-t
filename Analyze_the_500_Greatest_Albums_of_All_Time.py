import csv
with open('C:\\Users\\skyti\\python\\code1\\Mod 1 Code & Data Files\\albumlist.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    print(type(reader))
    print(reader.fieldnames)

    # for row in reader:
    #     print(row)

    # rows = 101
    # for row in reader:
    #     rows -= 1
    #     if (rows > 0):
    #         print(row)
    #     else:
    #         break

    albums = []
    for row in reader:
        albums.append(row)

    print("number albums: ", len(albums))

    albums_1974 = [row for row in albums if row["Year"] == '1974']
    print("number of album in 1974: ", len(albums_1974))

    for album in albums_1974:
        print(album["Album"], "by", album["Artist"] )

    print([row for row in albums if album["Year"] == "1974"][:10])

    rock_albums = [row for row in albums if(row["Genre"] == "Rock" 
                    and ("Pop Rock" in row["Subgenre"] or "Fusion" in row["Subgenre"]))
                  ]

    for album in rock_albums:
        print("Album name: ", album["Album"], "Artist name: ", album["Artist"], "Genre: ", album["Genre"], "Subgenre: ", album["Subgenre"])

