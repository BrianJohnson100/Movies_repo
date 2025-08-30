import pandas as pd
import datetime
import openpyxl
import pysnooper


# @pysnooper.snoop("snoop.txt")
def main():
    print("Start: " + str(datetime.datetime.now().strftime("%I:%m %p")))

    year = input("What year do you want to query on? ")

    start_week = input("What week do you want to start on? ")
    start_week = str(int(start_week) + 100)[1:]

    end_week = input("What week do you want to end on? ")
    end_week = str(int(end_week) + 100)[1:]

    date_range = range(int(year + start_week), int(year + end_week) + 1)

    movie_dollars = []

    for date_time_variable in date_range:
        timeperiod = str(date_time_variable)[:4] + 'W' + str(date_time_variable)[4:]
        print(timeperiod)

        print(f'This is the Time Period: {timeperiod}')
        print(f'This is the start of week number: {start_week}')
        # input()

        urls = [([],f"https://www.boxofficemojo.com/weekend/{timeperiod}"),
                ([],f"https://www.boxofficemojo.com/year/world/{timeperiod[:4]}")]

        for position, data in enumerate(urls):
            container, url = data

            print(f'This is the name of the url:  {url}')
            movie_dollar: pd.DataFrame = pd.read_html(url)[0]
            movie_dollar['Weekend #'] = timeperiod
            container.append(movie_dollar)

        print(container)
        print(container[0])

        container = container[0]
        for movie_dataframe in container[1:]:
            container = pd.concat([container, movie_dataframe])

       # print(movie_dollars[['Rank', 'Release', 'Datestamp']].head(5))
    print(container)
    exit()
    '''print(movies.shape)
    print(movies.head(3))
    input("")
    
    print(movie_dollars.columns)
    input()
    print(movie_dollars.values)
    input()
    print(movie_dollars.items)
    input()
    print(movie_dollars.shape)
    input()
    '''
    # exit()
    # print(movie_dollars[['Rank', 'Release']].head(5))

    location_for_file_export1 = r'C:\Users\Brian\projects\movie$\Box_Office1.xlsx'
    movies.to_excel(location_for_file_export1, index=False, engine="openpyxl")

    print("End: " + str(datetime.datetime.now().strftime("%I:%m %p")))


if __name__ == "__main__":
    main()
