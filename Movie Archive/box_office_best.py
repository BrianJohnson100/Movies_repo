import pandas as pd
import datetime
import openpyxl


def main():
    print("Start: " + str(datetime.datetime.now().strftime("%I:%m %p")))

    year = input("What year do you want to query on? ")

    week = input("What week do you want to query on? ")

    timeperiod = year + 'W' + week
    print(f'This is the timeperiod {timeperiod}')

    url: str = "https://www.boxofficemojo.com/weekend/" + timeperiod + "/"

    # I should put a for loop here that does a range between the starting week and the ending week of the dataset. Wto the prior data set from the prior week.
        #Create a range variable.
        #

    print(f'This is the name of the:  {url}')

    movie_dollars: pd.DataFrame = pd.read_html(url)[0]

    # returns current date and time
    # dt_now = datetime.datetime.now()
    # movie_dollars['Datestamp'] = dt_now

    print(movie_dollars.columns)
    input()
    print(movie_dollars.values)
    input()
    print(movie_dollars.items)
    input()
    print(movie_dollars.shape)
    input()

    print(movie_dollars[['Rank', 'Release']].head(5))

    location_for_file_export1 = r'C:\Users\Brian\OneDrive\Desktop\Box_Office1.xlsx'
    movie_dollars.to_excel(location_for_file_export1, index=False, engine="openpyxl")

    print("End: " + str(datetime.datetime.now().strftime("%I:%m %p")))


if __name__ == "__main__":
    main()
