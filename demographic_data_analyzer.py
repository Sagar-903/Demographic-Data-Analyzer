import os
import pandas as pd

def calculate_demographic_data():
    # --- Step 1: Load dataset ---
    file_path = r"C:\Users\sagar\Desktop\Demographic Data Analyzer\adult.data.csv"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The dataset file does not exist at: {file_path}")
    
    # Column names for Adult dataset
    columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education_num',
        'marital_status', 'occupation', 'relationship', 'race',
        'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
        'native_country', 'income'
    ]
    
    # Read CSV with proper delimiter handling
    df = pd.read_csv(file_path, header=None, names=columns, sep=',\s*', engine='python')
    
    # --- Step 2: Clean data ---
    # Strip spaces, lowercase, replace dashes
    df.columns = df.columns.str.strip().str.lower().str.replace('-', '_')
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Convert numeric columns safely
    numeric_cols = ['age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # invalid strings -> NaN

    # --- Step 3: Calculate demographic statistics ---
    
    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Income >50K by education
    higher_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu_df = df[df['education'].isin(higher_education)]
    lower_edu_df = df[~df['education'].isin(higher_education)]

    higher_edu_rich = round((higher_edu_df['income'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((lower_edu_df['income'] == '>50K').mean() * 100, 1)

    # 5. Minimum hours worked per week
    min_work_hours = df['hours_per_week'].min()
    num_min_workers = df[df['hours_per_week'] == min_work_hours]

    rich_percentage_min_workers = 0
    if not num_min_workers.empty:
        rich_percentage_min_workers = round((num_min_workers['income'] == '>50K').mean() * 100, 1)

    # 6. Country with highest percentage of rich people
    country_counts = df['native_country'].value_counts()
    country_rich_counts = df[df['income'] == '>50K']['native_country'].value_counts()

    country_percentage = (country_rich_counts / country_counts * 100).dropna()
    if not country_percentage.empty:
        highest_earning_country = country_percentage.idxmax()
        highest_earning_country_percentage = round(country_percentage.max(), 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = None

    # 7. Top occupation in India for >50K income
    india_high_salary = df[(df['native_country'] == 'India') & (df['income'] == '>50K')]
    if not india_high_salary.empty:
        top_IN_occupation = india_high_salary['occupation'].mode()[0]
    else:
        top_IN_occupation = None

    # --- Step 4: Return all results in a dictionary ---
    result = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    return result

# --- For testing ---
if __name__ == "__main__":
    data = calculate_demographic_data()
    for key, value in data.items():
        print(f"{key}: {value}")
