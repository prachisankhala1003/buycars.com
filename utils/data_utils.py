"""
Data utilities for car database and search
"""
import pandas as pd
import os


def get_sample_cars_data():
    """
    Returns sample car listing data.
    In production, this would query a real database.
    """
    sample_data = {
        "id": [1, 2, 3, 4, 5, 6, 7, 8],
        "year": [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015],
        "make": ["Honda", "Toyota", "Ford", "Honda", "Toyota", "Ford", "Honda", "Toyota"],
        "model": ["Civic", "Camry", "F-150", "Accord", "Corolla", "Mustang", "CR-V", "RAV4"],
        "mileage": [15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000],
        "condition": ["Excellent", "Excellent", "Good", "Good", "Good", "Fair", "Fair", "Fair"],
        "price": [21000, 19500, 28000, 24000, 16000, 22000, 18500, 14999],
        "color": ["Silver", "White", "Black", "Blue", "Red", "Red", "Gray", "Silver"],
    }
    return pd.DataFrame(sample_data)


def search_cars(year_range, make, model, max_price, condition):
    """
    Search cars by various criteria
    
    Args:
        year_range: tuple (min_year, max_year)
        make: str or None
        model: str or None
        max_price: int
        condition: str or None
    
    Returns:
        DataFrame with matching cars
    """
    df = get_sample_cars_data()
    
    # Apply filters
    df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    
    if make and make != "Any":
        df = df[df['make'] == make]
    
    if model and model != "Any":
        df = df[df['model'] == model]
    
    df = df[df['price'] <= max_price]
    
    if condition and condition != "Any":
        df = df[df['condition'] == condition]
    
    return df


def get_unique_makes():
    """Get list of unique car makes"""
    df = get_sample_cars_data()
    makes = ["Any"] + sorted(df['make'].unique().tolist())
    return makes


def get_unique_models(make=None):
    """Get list of unique models, optionally filtered by make"""
    df = get_sample_cars_data()
    
    if make and make != "Any":
        df = df[df['make'] == make]
    
    models = ["Any"] + sorted(df['model'].unique().tolist())
    return models
