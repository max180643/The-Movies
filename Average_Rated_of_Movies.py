import pandas as pd
import pygal
import time
start_time = time.time()

#Banner
print("|>>> Average Rated of Movies in year 2000-2016 Dataset <<<|")

def average_rates():
    """ Create Rated of Movies average_graph of movies in year 2000-2016 and Load Dataset rate"""
    graph = pygal.SolidGauge(inner_radius=0.70)
    graph.title = "Average Rated of Movies in year 2000-2016"
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    graph.value_formatter = percent_formatter

    for year in range(2000, 2017):
        print(">> Year : %i" % year)

        # Start display
        print(">> [status] Create Graph Starting!")

        dataset = pd.read_csv("Data_Export/%i.csv" % (year))
        rate = dataset["rate"].tolist() #Rate
        average = ((sum(rate)/len(rate))//0.01)/100
        graph.add(str(year), [{'value': average, 'max_value': 10}])

        # End display
        print(">> [status] Created Graph Successful!")
        print()

    graph.render_to_file("Graph_Export/Rated_Movies/Average/Average_Rated_of_Movies.svg")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

average_rates()
