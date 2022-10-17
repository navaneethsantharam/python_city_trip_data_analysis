import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday","all")
months = ("january","february","march","april","may","june","july","august","september","october","november","december","all")
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("Enter a city name (chicago/new york city/washington)-").lower()
        if city in CITY_DATA.keys():
            break
        print("Enter a valid city name among above three cities!!!")
    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("Enter a month (all for all months, else specific month name)-").lower()
        if month in months:
            break
        print("Enter a valid month!!!")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter a day of week (all for all days, else specific day name(monday,tuesday,etc)-").lower()
        if day in days:
            break
        print("Enter a valid day!!!")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    path="D:\\Python\\projects\\pandas_miniproject\\files\\"
    file_for_city=CITY_DATA.get(city)
    df=pd.read_csv(path+file_for_city,index_col=[0])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    df["Start Time"]=pd.to_datetime(df["Start Time"],infer_datetime_format=True)
    df["month"]=df["Start Time"].dt.month_name()
    print("Most common month:",df["month"].value_counts().index[0])
    # display the most common day of week
    df["day of week"]=df["Start Time"].dt.day_name()
    print("Most common day:",df["day of week"].value_counts().index[0])
    # display the most common start hour
    df["start hour"]=df["Start Time"].dt.hour
    print("Most common hour:",df["start hour"].value_counts().index[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print("Most common start station:",df["Start Station"].value_counts().index[0])
    # display most commonly used end station
    print("Most common end station:",df["End Station"].value_counts().index[0])
    # display most frequent combination of start station and end station trip
    print("Most common end station:",df[["Start Station","End Station"]].value_counts().index[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df["End Time"]=pd.to_datetime(df["End Time"],infer_datetime_format=True)
    # display total travel time
    print("Total travel time:",np.sum(df["End Time"]-df["Start Time"]))
    # display mean travel time
    print("Mean travel time:",np.mean(df["End Time"]-df["Start Time"]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print("\nUser type counts:\n",df["User Type"].value_counts())

    # Display counts of gender
    try:
        print("\nGender counts:\n",df["Gender"].value_counts())
    except KeyError:
        print("Gender column does not exist in file, Hence skipping gender analysis!!!")
    # Display earliest, most recent, and most common year of birth
    #df["Birth Year"]=df["Birth Year"].fillna(1900).astype("int")
    try:
        print("\nRecent year of birth:",df["Birth Year"].max())
        print("\nEarliest year of birth:",df["Birth Year"].min())
        print("\nMost common year of birth:",df["Birth Year"].value_counts().index[0])
    except KeyError:
        print("Birth Year column does not exist in file, Hence skipping gender analysis!!!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        start_index=0
        df_size=df.shape[0]
        while True:
            see_dataframe=input("\nWould you like to see the dataframe(5 rows)yes/no-")
            if see_dataframe.lower()!="yes":
                break
            end_index=start_index+5
            end_index=min(end_index,df_size)
            if start_index>=end_index:
                break
            print(df.iloc[start_index:end_index].to_markdown())
            start_index+=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
