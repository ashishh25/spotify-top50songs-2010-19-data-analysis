import pandas as pd

Cars = [
    {"name": "BMW X5", "model": "SUV", "selling_price": 4000000, "units_sold": 12, "Brand": "BMW", "month": "January"},
    {"name": "Fortuner", "model": "Sedan", "selling_price": 750000, "units_sold": 23, "Brand": "TOYOTA", "month": "January"},
    {"name": "Verna", "model": "Sedan", "selling_price": 1800000, "units_sold": 24, "Brand": "Hyundai", "month": "February"},
    {"name": "Alto", "model": "SUV", "selling_price": 400000, "units_sold": 134, "Brand": "Maruti Suzuki", "month": "February"},
    {"name": "Seltos", "model": "SUV", "selling_price": 750000, "units_sold": 90, "Brand": "Kia", "month": "March"},
    {"name": "Brezza", "model": "SUV", "selling_price": 900000, "units_sold": 60, "Brand": "Maruti Suzuki", "month": "March"},
    {"name": "Land Rover", "model": "SUV", "selling_price": 120000, "units_sold": 80, "Brand": "Land Rover", "month": "April"},
    {"name": "Swift", "model": "SUV", "selling_price": 850000, "units_sold": 73, "Brand": "Maruti Suzuki", "month": "April"},
    {"name": "Creta", "model": "SUV", "selling_price": 1850000, "units_sold": 54, "Brand": "Hyundai", "month": "April"},
    {"name": "XUV 300", "model": "SUV", "selling_price": 1150000, "units_sold": 61, "Brand": "Mahindra", "month": "March"},
    {"name": "NEXON", "model": "SUV", "selling_price": 850000, "units_sold": 82, "Brand": "TATA", "month": "January"},
    {"name": "PUNCH", "model": "SUV", "selling_price": 1050000, "units_sold": 82, "Brand": "TATA", "month": "January"}
]

df = pd.DataFrame(Cars)
df.to_csv('cars.csv', index=False)