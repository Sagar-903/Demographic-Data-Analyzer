import pandas as pd

def calculate_demographic_data():
    # Load data
    df = pd.read_csv('adult.data.csv')  # Replace with your dataset path

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4 & 5. Percentage of people with advanced education making >50K
    advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
    high_edu = df[df['education'].isin(advanced_edu)]
    low_edu = df[~df['education'].isin(advanced_edu)]

    higher_edu_rich = round((high_edu[high_edu['salary'] == '>50K'].shape[0] / high_edu.shape[0]) * 100, 1)
    lower_edu_rich = round((low_edu[low_edu['salary'] == '>50K'].shape[0] / low_edu.shape[0]) * 100, 1)

    # 6. Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people working minimum hours who earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

    # 8. Country with highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = round((country_rich_counts / country_counts * 100).max(), 1)
    highest_earning_country = (country_rich_counts / country_counts * 100).idxmax()

    # 9. Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Return all values as dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_edu_rich': higher_edu_rich,
        'lower_edu_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
