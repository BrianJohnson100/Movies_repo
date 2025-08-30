import pandas as pd
import datetime
import openpyxl
#import pysnooper

DIR = r'C:\Users\Brian\projects\movie$'

# @pysnooper.snoop("snoop.txt")
def main():
    print("Start: " + str(datetime.datetime.now().strftime("%I:%m %p")))
    while True:
        download = input("w for weekly, y for yearly: ")
        if download.lower() in "wy":
            break
        print("You must enter a w or a y.")

    movie_dollars = []

    if download == "w":
        year = input("What year do you want to query on? ")

        start_week = input("What week do you want to start on? ")
        start_week = str(int(start_week) + 100)[1:]

        end_week = input("What week do you want to end on? ")
        end_week = str(int(end_week) + 100)[1:]


        date_range_w = range(int(year + start_week), int(year + end_week) + 1)
        timeperiod_w = year + 'W' + end_week
        url = f"https://www.boxofficemojo.com/weekend/{timeperiod_w}"
        for date_time_variable in date_range_w:
            timeperiod_w = str(date_time_variable)[:4] + 'W' + str(
                date_time_variable)[4:]
            # print(timeperiod_w)
            # print(f'This is the Time Period: {timeperiod_w}')
            # print(f'This is the start of week number: {start_week}')
            # input("This is where the w stops")

    else:
        from_year = str("1977")
        to_year = datetime.datetime.now()
        to_year = f"{int(to_year.strftime('%Y'))-1}"

        date_range_y = range(int(from_year), int(to_year))
        timeperiod_y = date_range_y

        url = f"https://www.boxofficemojo.com/year/world/{timeperiod_y})/"

        for date_time_variable in date_range_y:
            # timeperiod_y = str(date_time_variable)[:4] + 'W' + str(
            # date_time_variable)[4:]
            print(timeperiod_y)
            print(f'This is the name of the url:  {url}')

    movie_dollar: pd.DataFrame = pd.read_html(url)[0]
    movie_dollar['Weekend #'] = timeperiod_w
    movie_dollar['Year #'] = from_year
    movie_dollars.append(movie_dollar)

    movies = movie_dollars[0]
    for movie_dollar in movie_dollars[1:]:
        movies = pd.concat([movies, movie_dollar], ignore_index=True)

    exit()

    print(movies)
    print(movies.shape)
    if download == "w":
        location_for_file_export1 = fr'{DIR}\Box_Officew.xlsx'
    elif download == "y":
        location_for_file_export1 = fr'{DIR}\Box_Officey.xlsx'
    movies.to_excel(location_for_file_export1, index=False, engine="openpyxl")
    print("End: " + str(datetime.datetime.now().strftime("%I:%m %p")))

if __name__ == "__main__":
    main()
