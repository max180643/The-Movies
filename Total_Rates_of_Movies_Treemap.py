import pandas as pd
import pygal
import time
start_time = time.time()

#Banner
print("|>>> Total Rates of Movies in year 2000-2016 Dataset <<<|")

def rate_movies():
    """ Create treemap_graph of total of movies in year 2000-2016 and Load Dataset title and rate"""
    for year in range(2000, 2017):
        print(">> Year : %i" % year)

        # Start display
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Data_Export/%i.csv" % (year))
        title = dataset["title"].tolist() #Title Movies
        rate = dataset["rate"].tolist() #Rate
        graph = pygal.Treemap(x_title="Movie", y_title="Rate")
        graph.title = "Total Rates of Movies in %i Dataset" % year
        for i in range(len(title)):
            graph.add(title[i], rate[i])
        graph.render_to_file("Graph_Export/Rates_Year/Treemap/Total_Rates_of_Movies_%i.svg" % year)

        # End display
        print(">> [status] Created Graph Successful!")
        print()

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

rate_movies()
