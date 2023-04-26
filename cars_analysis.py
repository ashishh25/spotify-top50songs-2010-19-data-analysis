import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('cars.csv')

# display the DataFrame
print(df.head(10))
print(df.describe())

# Create a pandas dataframe from the Cars list
cars_df = pd.DataFrame(df)

# Print the mean selling price
print("Mean selling price: ", cars_df['selling_price'].mean())

# Print the total number of units sold
print("Total units sold: ", cars_df['units_sold'].sum())

# Print the average units sold per month
print("Average units sold per month: ", cars_df['units_sold'].mean())

# Print the highest selling car
print("Highest selling car: ", cars_df.loc[cars_df['units_sold'].idxmax()]['name'])

# Print the number of cars sold by brand
print("Number of cars sold by brand: \n", cars_df.groupby(['Brand'])['units_sold'].sum())

#Most car sold in Jan
# Filter data to include only sales in January
jan_sales = cars_df.loc[cars_df['month'] == 'January']

# Find the car with the highest number of units sold in January
most_sold_car = jan_sales.loc[jan_sales['units_sold'].idxmax()]

# Print the result
print("The most sold car in January is: ", most_sold_car['name'], "with", most_sold_car['units_sold'], "units sold.")

#Top 3 Brands
# Group the sales data by brand and sum up the units sold for each brand
brand_sales = cars_df.groupby('Brand').sum()['units_sold']

# Sort the data by the number of units sold and select the top 3 brands
top_brands = brand_sales.sort_values(ascending=False)[:3]

# Create a bar chart to visualize the data
plt.bar(top_brands.index, top_brands.values,  color=['darkorchid', 'Saddlebrown', 'orange'])
plt.title('Top 3 Car Brands by Most Sold Cars')
plt.xlabel('Brand')
plt.ylabel('Units Sold')
plt.show()

# Count the number of cars sold by each brand
brand_counts = cars_df['Brand'].value_counts()

#Percentage of Brands
# Calculate the percentage of cars sold by each brand
brand_percentages = 100 * brand_counts / brand_counts.sum()

# Create a pie chart to visualize the data
plt.pie(brand_percentages.values, labels=brand_percentages.index, autopct='%1.1f%%')
plt.title('Percentage of Cars Sold by Brand')
plt.axis('equal')
plt.show()

#Relational Graph
# Create a scatter plot to visualize the data
cars_df.plot.scatter(x='selling_price', y='units_sold', color='blue')
plt.title('Relationship between Selling Price and Units Sold')
plt.xlabel('Selling Price')
plt.ylabel('Units Sold')
plt.show()
