import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Filtering city, month, day
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city_input = input("city : ").lower()
    city = city_input.replace(' ', '_')
    city_i = 1
    
    while(city_i > 0):
        city_i -= 1
        if city in CITY_DATA != True:
           break
        else:
           print("This is invaild input. Please input correct ones.")
           city_input = input("city : ").lower()
           city = city_input.replace(' ', '_')
           city_i += 1
            
    months = ["all", "january", "february", "march", "april", "may", "june"]
    
    month = input("month : ").lower()
    month_i = 1
 
    while(month_i > 0):
        month_i -= 1
        if month in months != True:
           break
        else:
           print("This is invaild input. Please input correct ones.")
           month = input("month : ").lower()
           month_i += 1

    day_of_weeks = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    day = input("day of week : ").lower()
    day_i = 1

    while(day_i > 0):
        day_i -= 1
        if day in day_of_weeks != True:
           break
        else:
           print("This is invaild input. Please input correct ones.")
           day = input("day of week : ").lower()
           day_i += 1

    print('-'*40)
    return city, month, day

#Loading datas
def load_data(city, month, day):
    df = pd.read_csv("{}.csv".format(city))
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday

    if month != "all":
        month_list = ["january", "feburary", "march", "april", "may", "june"]
        month = month_list.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != "all":
        df = df[df['day of week'] == day.title()]

    return df

#Carculating frequent month, week and hour
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()
    
    print('Common Month :', common_month)

    df['day of week'] = df['Start Time'].dt.weekday
    common_week = df['day of week'].mode()
    
    print('Common Week :', common_week)

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()
    
    print('Common Hour :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Calculating popular stations
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()
    
    print('Common Start Station:', common_start_station)

    common_end_station = df['End Station'].mode()
    
    print('Common End Station:', common_end_station)

    frequent_combination = df.groupby(['Start Station', 'End Station']).idmax()
                                       
    print('Frequent Combination Stations :', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Carculating travel time
def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
                                       
    print('Total Travel Time :', total_time)

    mean_time = total_time.mean()
    
    print('Mean Travel Time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Calculate user stats(gender, birth year)
def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_count()
    
    print('User Type :', user_type)

    if 'Gender' in df:
        gender_count = df['Gender'].value_count()
        print('Gender Count :', gender_count)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    
    if 'Birth Year' in df:
       gender_earlist = df['Birth Year'].max()
       gender_recent = df['Birth Year'].min()
       gender_common = df['Birth Year'].mode()
                                       
       print('Earlist Gender :', gender_earlist)
       print('Recent Gender :', gender_recent)
       print('Common Gender :', gender_common)

    else:
        print('Gender stats cannot be calculated because Birth Year does not appear in the dataframe')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Displaying datas
def display_data(df):
    pd.set_option('display.max_columns',200)
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    end_loc = 4
    if view_data == "yes":
        while (1):
            print(df.loc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            view_display = input("Do you wish to continue? Enter yes or no\n").lower()
        
            if view_display == "no":
                break
    else:
        return None

#Running  all functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
