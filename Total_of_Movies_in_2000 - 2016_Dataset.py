import pandas as pd
import pygal
import time
start_time = time.time()

#banner
print("|>>> Total of Movies in 2000 - 2016 Dataset <<<|")

def treemap_graph():
    """ Create treemap_graph of total of movies 2000 - 2016 """
    # start display
    print(">> [status] Creat Graph Starting!")

    graph = pygal.Bar(x_title="Year", y_title="Total", legend_at_bottom=True, print_values=True)
    graph.title = "Total of Movies in 2000 - 2016 Dataset"
    for i in range(2000, 2017):
        graph.add(str(i), dataload(i))
    graph.render_to_file("Graph_Export/Total_of_Movies_2000-2016.svg")

    # end display
    print(">> [status] Created Graph Successful!")

    # Used time
    print(">> [status] Completed : Used time = %s seconds" % (time.time() - start_time))

def dataload(year):
    """ Load Dataset """
    dataset = pd.read_csv("Data_Export/%i.csv" % (year))
    total = len(dataset["title"].tolist())
    return total

treemap_graph()
