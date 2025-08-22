from demographic_data_analyzer import calculate_demographic_data

result = calculate_demographic_data()
for key, value in result.items():
    print(f"{key}: {value}")
