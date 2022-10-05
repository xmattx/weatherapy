import requests, urllib3

#Disabling insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class weatherApi:

    def __init__(self, apiKey, city, aqi) -> None:
        self.city = city
        self.aqi = aqi
        self.apiKey = apiKey


    def getCurrent(apiKey: str, city: str, aqi: bool):    
        if not isinstance(apiKey, str) or not isinstance(city, str) or not isinstance(aqi, bool):
            print("ERROR - apiKey and city must be string and aqi must be bool")
            exit(1)

        aqi = "yes" if aqi else "no"
        req = requests.get("http://api.weatherapi.com/v1/current.json?key={0}&q={1}&aqi={2}".format(apiKey, city, aqi))
        return req.json()


    def getForecast(apiKey: str, city: str, aqi: bool, days: int, alerts: bool):     
        if not isinstance(apiKey, str) or not isinstance(city, str) or not isinstance(aqi, bool) or not isinstance(alerts, bool):
            print("ERROR - apiKey and city must be string, aqi and alerts must be bool")
            exit(1)

        aqi = "yes" if aqi else "no"
        alerts = "yes" if alerts else "no"
        req = requests.get("http://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days={2}&aqi={3}&alerts={4}".format(apiKey, city, days, aqi, alerts))
        return req.json()