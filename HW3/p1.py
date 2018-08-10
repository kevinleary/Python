import csv

 #function to read imdb-top-rated
def read_top_rated(top_rated_file, top_rated_dict):

    """Read the imdb_top_rated.csv to create a dictionary
        with the tuple key (title, year):imdb_rating """

    data_reader = csv.reader(top_rated_file)


    for row in data_reader:
        # ignore header rows: elements begin with a number since sorted by rank
        #row increments in for and col is the index i.e. [0]
        if row[0].isdigit():  
            #rank = row[0]
            title = row[1]
            year = row[2]
            imdb_rating = row[3]

            top_rated_dict[(title, year)] = imdb_rating
    #print(top_rated_dict) #-- looks good!



 #function to read imdb-top-grossing
def read_top_grossing(top_grossing_file, top_grossing_dict):

    """Read the imdb_top_grossing.csv to create a dictionary
        with the tuple key (title, year):box_office """

    data_reader = csv.reader(top_grossing_file)

    for row in data_reader:
        # ignore header rows: elements begin with a number
        if row[0].isdigit():  
            title = row[1]
            year = row[2]
            box_office = row[3]
            #top_grossing_dict = {(title, year):box_office}
            #print(top_grossing_dict)
            top_grossing_dict[(title, year)] = box_office


#function to read imdb-top-casts
def read_top_casts(top_casts_file, top_casts_dict):

    """Read the imdb_top_casts.csv to create a dictionary
        with the tuple key (title, year): 
        --- this one is a little less straight foward"""

    data_reader = csv.reader(top_casts_file)

    for row in data_reader:
        # ignore header rows: elements begin with a number
        #if row[0].isdigit():  #---not needed because no headers for this csv
        title = row[0]
        year = row[1]
        director = row[2]
        cast = row[3:8]
        #top_casts_dict = {(title, year):(director, cast)}
        top_casts_dict[(title, year)] = (director, cast)
        #top_casts_dict = {(title, year):director}
        #print(top_casts_dict)


#top_rated_dict = {('movie', 'year'):[rating]}

#Read the files 
top_rated_file = open(r'E:\A FAU\COP4045 - Python\HW\HW3\imdb-top-rated.csv')
top_grossing_file = open(r'E:\A FAU\COP4045 - Python\HW\HW3\imdb-top-grossing.csv')
top_casts_file = open(r'E:\A FAU\COP4045 - Python\HW\HW3\imdb-top-casts.csv', encoding='utf8')      #pain in the ass

#create dictionaries
top_rated_dict = {}
read_top_rated(top_rated_file, top_rated_dict)

top_grossing_dict = {}
read_top_grossing(top_grossing_file, top_grossing_dict)

top_casts_dict = {}
read_top_casts(top_casts_file, top_casts_dict)



#1a) print the directors with the most movies in the    top rated list 
dir_count = {}
i = 0

#query values and put them in a new dict with a count
for key, value in top_casts_dict.items():
    if key in top_rated_dict:
        valnew = top_casts_dict[key][0]
        dir_count[valnew] = dir_count.get(valnew, 0) + 1
    
#reverse sort the values
dir_sorted = sorted(dir_count.items(), key=lambda kv:kv[1], reverse=True)

#print values
print("Directors with most movies in the top rated\n")
while(i < 5):
    print(dir_sorted[i][0])
    i+= 1
    


#1b) directors with most movies in the top grossing

dir_gross_count = {}
i = 0

#query values and put them in a new dict with a count
for key, value in top_casts_dict.items():
    if key in top_grossing_dict:
        valnew = top_casts_dict[key][0]
        dir_gross_count[valnew] = dir_gross_count.get(valnew, 0) + 1
    
#reverse sort the values
dir_gross_sorted = sorted(dir_gross_count.items(), key=lambda kv:kv[1], reverse=True)

#print values
print("\n\nDirectors with most highest grossing movies\n")
while(i < 5):
    print(dir_gross_sorted[i][0])
    i+= 1


#1c) displays a ranking of the actors with the most movie credits in top rated

actor_count = {}
i=0

for key, value in top_casts_dict.items():
    if key in top_rated_dict:
        for name in top_casts_dict[key][1]:   
            actor_count[name] = actor_count.get(name, 0) + 1

actor_count_sorted = sorted(actor_count.items(), key=lambda kv:kv[1], reverse=True)

#print values
print("\n\nMost credited actors in top rated\n")
while(i < 5):
    print(actor_count_sorted[i][0])
    i+= 1

#1d) Displays a ranking (descending) with the actors who brought in the most box office money, 
# based onthe top grossing movie list. For a movie with gross ticket sales amount s, 
# the 5 actors on the cast list will split amount s in the following way: 


actor_gross_count = {}
i=0

for key, value in top_casts_dict.items():
    if key in top_grossing_dict:
        for name in top_casts_dict[key][1]:   
            #for the splits 
            #would have to convert the money 
                actor_gross_count[name] = top_grossing_dict

actor_count_sorted = sorted(actor_count.items(), key=lambda kv:kv[1], reverse=True)

#print values
print("\n\nMost credited actors in top rated\n")
while(i < 5):
    print(actor_count_sorted[i][0])
    i+= 1
