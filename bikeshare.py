import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input("Enter city name (chicago, new york city, washington): ").lower() 
        if city in CITY_DATA:
            break 
        else: 
             print("Invalid city. Please enter again.")
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all'] 
    while True:
        month = input("Enter month name (january, february, ..., june) or 'all': ").lower() 
        if month in months: 
            break 
        else:
            print("Invalid month. Please enter again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'] 
    while True: 
        day = input("Enter day of week (monday, tuesday, ..., sunday) or 'all': ").lower() 
        if day in days:
            break 
        else:
            print("Invalid day. Please enter again.") 
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
    # load data file into a dataframe 
    df = pd.read_csv(CITY_DATA[city]) 
    # convert the Start Time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    # extract month and day of week from Start Time to create new columns 
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name() 
    # filter by month if applicable 
    if month != 'all': 
        # use the index of the months list to get the corresponding int 
         months = ['january', 'february', 'march', 'april', 'may', 'june'] 
         month = months.index(month.lower()) + 1 
        # filter by month to create the new dataframe 
         df = df[df['month'] == month] 
    # filter by day of week if applicable 
    if day != 'all': 
        # filter by day of week to create the new dataframe 
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0] 
    print(f"Most common month: {most_common_month}")

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0] 
    print(f"Most common day of week: {most_common_day_of_week}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    most_common_start_hour = df['hour'].mode()[0] 
    print(f"Most common start hour: {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0] 
    print(f"Most common start station: {most_common_start_station}")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0] 
    print(f"Most common end station: {most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax() 
    print(f"Most common trip: {most_common_trip[0]} to {most_common_trip[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() 
    print(f"Total travel time: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() 
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts() 
    print(f"Counts of user types:\n{user_types}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: 
        gender_counts = df['Gender'].value_counts() 
        print(f"Counts of gender:\n{gender_counts}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: 
        earliest_birth_year = int(df['Birth Year'].min()) 
        most_recent_birth_year = int(df['Birth Year'].max()) 
        most_common_birth_year = int(df['Birth Year'].mode()[0]) 
        print(f"Earliest birth year: {earliest_birth_year}") 
        print(f"Most recent birth year: {most_recent_birth_year}") 
        print(f"Most common birth year: {most_common_birth_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Adding Raw Data Display Function    
def display_raw_data(df):
    start = 0
    while True:
        raw_data = input("Do you want to see 5 lines of raw data? (yes/no): ").lower()
        if raw_data == 'yes':
            print(df.iloc[start:start + 5])
            start += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
