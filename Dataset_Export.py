""" Read Dataset and Create CSV File """
import csv
import pandas as pd
dataset = pd.read_csv("Dataset/tmdb_5000_movies.csv")

def data_load():
    """ Load Dataset """
    # start display
    print("Export Dataset Starting !!!")
    # load dataset
    title = dataset["title"].tolist()
    rate = dataset["vote_average"].tolist()
    budget = dataset["budget"].tolist()
    revenue = dataset["revenue"].tolist()
    runtime = dataset["runtime"].tolist()
    year = dataset["release_date"].tolist()
    # data to export
    data_2000 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2001 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2002 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2003 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2004 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2005 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2006 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2007 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2008 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2009 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2010 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2011 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2012 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2013 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2014 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2015 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    data_2016 = [
            ["title", "rate", "budget", "revenue", "runtime", "year"]
    ]
    # add value to data classified by year
    for i in range(len(title)):
        if str(year[i])[:4] == "2000":
            data_2000.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2001":
            data_2001.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2002":
            data_2002.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2003":
            data_2003.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2004":
            data_2004.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2005":
            data_2005.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2006":
            data_2006.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2007":
            data_2007.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2008":
            data_2008.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2009":
            data_2009.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2010":
            data_2010.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2011":
            data_2011.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2012":
            data_2012.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2013":
            data_2013.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2014":
            data_2014.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2015":
            data_2015.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
        elif str(year[i])[:4] == "2016":
            data_2016.append([title[i], rate[i], budget[i], revenue[i], runtime[i], str(year[i])[:4]])
    # export file
    export_file(data_2000, 2000)
    export_file(data_2001, 2001)
    export_file(data_2002, 2002)
    export_file(data_2003, 2003)
    export_file(data_2004, 2004)
    export_file(data_2005, 2005)
    export_file(data_2006, 2006)
    export_file(data_2007, 2007)
    export_file(data_2008, 2008)
    export_file(data_2009, 2009)
    export_file(data_2010, 2010)
    export_file(data_2011, 2011)
    export_file(data_2012, 2012)
    export_file(data_2013, 2013)
    export_file(data_2014, 2014)
    export_file(data_2015, 2015)
    export_file(data_2016, 2016)
    # end display
    print("Exported Dataset Successful !!!")

def export_file(data, year):
    """ Export CSV File Sort By Year """
    file_name = "Data_Export/" + str(year) + ".csv"
    with open(file_name, "w", newline="") as export_file:
        file_ = csv.writer(export_file, delimiter=",")
        file_.writerows(data)

data_load()
