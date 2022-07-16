import json
import requests
import pymysql
import pandas as pd
import sqlalchemy # install if needed
from sqlalchemy import create_engine

def lambda_handler(event, context):
 #for connection to AWS instance
    
    cnx = pymysql.connect(
    user='****',
    password='****',
    host='**yourhostname**.eu-central-1.rds.amazonaws.com',
    database='gans')
    
#for cities data
    schema = "gans"
    host = "wbs-project3-db.czigfki0oepk.eu-central-1.rds.amazonaws.com"
    user = "Shruti_Gujar"
    password ="Ivg&13De?Bak"
    port = 3306
    con = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}"
    
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}', echo=False)
    cities_df = pd.read_sql_table("cities", con=engine)
    
    cities = cities_df["city"].to_list()
    
     
#creating function for weather 
     
    def get_weather_data(cities):
        weather_list = []
        url = f"http://api.openweathermap.org/data/2.5/forecast?q=Boston&appid={'32e589382a5ef64b4041baebd1e6cbe6'}&units=metric"
        test = requests.get(url)
        if test.status_code >= 200 and test.status_code <= 299:
            for city in cities:
                url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={'32e589382a5ef64b4041baebd1e6cbe6'}&units=metric"
                weather = requests.get(url)
                weather_df = pd.json_normalize(weather.json()["list"])
                weather_df["city"] = city
                weather_list.append(weather_df)
        else:
            return -1
        weather_combined = pd.concat(weather_list, ignore_index = True)
        return weather_combined
    
 #rename the tables names

    weather_data = get_weather_data(cities)


    weather_data = weather_data[["pop", "dt_txt", "main.temp", "main.feels_like", "main.humidity", "clouds.all", 
                             "wind.speed", "wind.gust", "city"]]
                             
   
    weather_data.rename(columns = {"pop": "precip_prob", 
                                "dt_txt": "forecast_time", 
                                "main.temp": "temperature",
                                "main.feels_like": "feels_like",
                                "main.humidity": "humidity", 
                                "clouds.all": "cloudiness", 
                                "wind.speed": "wind_speed", 
                                "wind.gust": "wind_gust",}, 
                                 inplace = True)
                    
    weather_data = weather_data.merge(cities_df[["city_id", "city"]], how = "left", on = "city")
    weather_data["forecast_time"] = pd.to_datetime(weather_data["forecast_time"])

    weather_data.to_sql("weathers", if_exists = "append", con = engine, index = False)
   
     
    # commit changes & close connection
    cursor = cnx.cursor()
    cnx.commit()
    cursor.close()
    cnx.close()
    
    
