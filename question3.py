import re

def analyze_blog_sentiments(blog_file):
    try:
        with open(blog_file, 'r') as file:
            text = file.read()
            positive_words = ['amazing', 'enjoy', 'beautiful', 'wonderful', 'fantastic']
            negative_words = ['disappointing', 'poor', 'lackluster', 'scarce']

            positive_count = sum(1 for word in positive_words if re.search(r'\b' + word + r'\b', text, flags=re.IGNORECASE))
            negative_count = sum(1 for word in negative_words if re.search(r'\b' + word + r'\b', text, flags=re.IGNORECASE))

            return positive_count, negative_count
    except FileNotFoundError:
        print(f"Error: File '{blog_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{blog_file}'.")
def analyze_weather_data(*weather_files):
    try:
        yearly_temperatures = {}

        for file_name in weather_files:
            year = re.search(r'\d{4}', file_name).group() 
            with open(file_name, 'r') as file:
                temperatures = [int(entry.split(',')[1].strip('°C')) for entry in file.read().split()]
                yearly_temperatures[year] = sum(temperatures) / len(temperatures)

        max_year = max(yearly_temperatures, key=yearly_temperatures.get)
        max_average_temp = yearly_temperatures[max_year]

        return yearly_temperatures, max_year, max_average_temp
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
        return {}, None, None
    except PermissionError as e:
        print(f"Error: Permission denied while accessing {e.filename}.")
        return {}, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}, None, None


positive, negative = analyze_blog_sentiments("travel_blogs.txt")

print("Sentiment Analysis Results:")
print(f"Positive words: {positive}")
print(f"Negative words: {negative}")

yearly_temperatures, max_year, max_average_temp = analyze_weather_data("weather_2020.txt", "weather_2021.txt", "weather_2022.txt")

print("\nWeather Analysis Results:")
for year, avg_temp in yearly_temperatures.items():
    print(f"Average temperature in {year}: {avg_temp:.2f}°C")

if max_year is not None and max_average_temp is not None:
    print(f"The year with the highest average temperature is {max_year} with an average temperature of {max_average_temp:.2f}°C.")
else:
    print("Error: Unable to determine the year with the highest average temperature.")
