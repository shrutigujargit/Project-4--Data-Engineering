# Project-4--Data-Engineering
>## _Gans_ - an ecommerce company:

Gans is a startup developing an e-scooter-sharing system. It aspires to operate in the most populous cities all around the world. In each city, it will have hundreds of e-scooters parked in the streets and allows users to rent them by the minute.

Gans has seen that its operational success depends on having their scooters parked where users need them. Ideally, scooters get rearranged organically by having certain users moving from point A to point B, and then an even number of users moving from point B to point A. There are some elements that create asymmetries. Here are some of them:

In hilly cities, users tend to use scooters to go uphill and then walk downhill. In the morning, there is a general movement from residential neighbourhoods towards the city centre. Whenever it starts raining, e-scooter usage decreases drastically. Whenever airplanes with back-pack young tourists lands, a lot of scooters are needed close to the airport. for this things we need Data(cities, weather, airports, flights).

>### Summary of work done so far:


* Data Collection
  - Scrape data from the wikipedia.(Python library used: beautifulsoup).
   - Collect data with the help of APIs.
 
* Data Storage
     - Create a database model.
     - Store data on a local MySQL instance.

* AWS
    - Set up a cloud database(Amazon Web Services (AWS), to set up MySQL database)
     - Move scripts to Lambda.

* Automate the pipeline
     - Used CloudWatch Events / EventBridge


>### API's

   * Weather data (https://openweathermap.org/api)

   * Airports data (https://rapidapi.com/hub)

   * Flights data (https://rapidapi.com/hub) 
