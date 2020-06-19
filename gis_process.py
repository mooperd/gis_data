import csv
with open('gis.csv') as csvfile:
    gisreader = csv.DictReader(csvfile, delimiter=';')
    output_list = []
    for row in gisreader:
        if float(row["total_route_time"]) > 125:
            output_list.append(row)
    
    print(output_list)
        # print("the from_id is {0}. the fromid_toid is {1}".format(row["from_id"], row["fromid_toid"]))

    

