if __name__ == '__main__':

    import time
    import pandas as pd
    import numpy as np

    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york': 'new_york_city.csv',
                 'washington': 'washington.csv'}

    CITIES = ['chicago', 'new york', 'washington']

    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


    def get_filters():
        """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
        print('Hello! Let\'s explore some US bikeshare data!')

        while True:
            city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
            if city in CITIES:
                break

        while True:
            month = input(
                'Which month to want to be analyzed e.g. january, ... or type "all" to apply no monthly filter. \n> ').lower()
            if month in MONTHS:
                break

        while True:
            day = input(
                'Which day of the week you want to be analyzed e.g. monday? You can type "all" again to apply no day filter. \n> ').lower()
            if day in DAYS:
                break

        print('-' * 40)
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

        df = pd.read_csv(CITY_DATA[city])

        df['Start Time'] = pd.to_datetime(df['Start Time'])

        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

            df = df[df['month'] == month]

        if day != 'all':
            df = df[df['day_of_week'] == day.title()]

        return df


    def time_stats(df):
        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        most_common_month = df['month'].value_counts().idxmax()
        print("The most common month is :", most_common_month)

        most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
        print("The most common day of week is :", most_common_day_of_week)

        most_common_start_hour = df['hour'].value_counts().idxmax()
        print("The most common start hour is :", most_common_start_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


    def station_stats(df):
        """Displays statistics on the most popular stations and trip."""

        print("Calculating The Most Popular Stations and Trip...")
        start_time = time.time()

        most_common_start_station = df['Start Station'].value_counts().idxmax()
        print("The most common start station is: ", most_common_start_station)

        most_common_end_station = df['End Station'].value_counts().idxmax()
        print("The most common end station is : ", most_common_end_station)

        df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
        most_common_start_end_station = df['Start End'].value_counts().idxmax()
        print("The most common start station and end station is : {}".format(most_common_start_end_station))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


    def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""

        print("Calculating Trip Duration...")
        start_time = time.time()

        total_travel = df['Trip Duration'].sum()
        print("Total travel time is: ", total_travel)

        mean_travel = df['Trip Duration'].mean()
        print("Mean travel time is: ", mean_travel)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


    def user_stats(df):
        """Displays statistics on bikeshare users."""
        # df = pd.read_csv(CITY_DATA[city]
        print("nCalculating User Stats...")
        start_time = time.time()

        print("Counts of user types:\n")
        user_counts = df['User Type'].value_counts()
        print(user_counts)

        print("Counts of user types:\n")
        print(df['Gender'].value_counts())

        print("earliest, most recent, and most common year of birth:\n")
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        print(df['Birth Year'].mode())

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


    def rawdata_show(df):
        """ show raw data of bikeshare project"""
        
        userinput = 'yes'

        while str(userinput) == 'yes':
            x = 0
            y = x+5
            print(df.iloc[x:y])
            userinput = input('\nWould you like to see the next 5 lines of raw data? Type yes\n')
            x += 5


    def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)

            if str(city) != 'washington':
                user_stats(df)
            else:
                print('no gender data for washington available')
            rawdata = input('\nWould you like to see some raw data? Enter yes\n')

            if rawdata.lower() == 'yes':
                rawdata_show(df)

            restart = input('\nWould you like to restart? Enter yes. Otherwise the programm will be closed\n')
            if restart.lower() != 'yes':
                break


    if __name__ == "__main__":
        main()
