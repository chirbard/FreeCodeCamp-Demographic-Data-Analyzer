import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    boolean_array = df['sex'] == 'Male'
    # print(boolean_array)
    average_age_men = df['age'][boolean_array].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    boolean_array = df['education'] == 'Bachelors'
    bachelors_count = df[boolean_array].shape[0]
    row_count = df.shape[0]
    percentage_bachelors = round(100 * (bachelors_count / row_count), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    b = df['education'] == 'Bachelors'
    m = df['education'] == 'Masters'
    d = df['education'] == 'Doctorate'
    higher_education = b | m | d
    lower_education = ~higher_education

    # percentage with salary >50K
    rich = df['salary'] == '>50K'
    higher_education_rich_count = df[rich & higher_education].shape[0]
    higher_education_count = df[higher_education].shape[0]
    lower_education_rich_count = df[rich & lower_education].shape[0]
    lower_education_count = row_count - higher_education_count
    higher_education_rich =  100 * (higher_education_rich_count / higher_education_count)
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich =  100 * (lower_education_rich_count / lower_education_count)
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours_mask = df['hours-per-week'] == min_work_hours
    min_hours_rich_count = df[rich & min_work_hours_mask].shape[0]
    rmin_work_hours_count = df[min_work_hours_mask].shape[0]
    rich_percentage = round(100 * (min_hours_rich_count / rmin_work_hours_count), 1)

    # What country has the highest percentage of people that earn >50K?
    country_value_counts = df['native-country'].value_counts()
    rich_in_countries = df[rich]['native-country'].value_counts()
    highest_earning_country_percentage = 0
    highest_earning_country = rich_in_countries.iloc[0]
    for country in rich_in_countries.index:
        percentage = 100 * (rich_in_countries[country] / country_value_counts[country])
        if percentage > highest_earning_country_percentage:
            highest_earning_country_percentage = round(percentage, 1)
            highest_earning_country = country

    # Identify the most popular occupation for those who earn >50K in India.
    in_india = df['native-country'] == 'India'
    rich_in_india = in_india & rich
    rich_in_india_occupation_value_count = df[rich_in_india]['occupation'].value_counts()
    # print(rich_in_india_occupation_value_count)
    top_IN_occupation = rich_in_india_occupation_value_count.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
