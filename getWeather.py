from weatherapi_class import weatherApi as weather
import argparse

#apikey
apiKey = "xxx"

#argparser
parser = argparse.ArgumentParser()
parser.add_argument("--current", help="Use this flag if you want to get current weather", dest="current", action="store_true")
parser.add_argument("--forecast", help="Use this flag if you want to get forecast weather", dest="forecast", action="store_true")
parser.add_argument("--city", type=str, help="City", dest="city")
parser.add_argument("--aqi", help="Get air quality index", action="store_true")
parser.add_argument("--days", type=int, help="Get weather forecast for x days", dest="days")
parser.add_argument("--alerts", help="Get weather alerts", action="store_true")
args = parser.parse_args()

if not args.city:
    print("Please specify at least one city")
    exit(1)

if not args.current and not args.forecast:
    print("Please specify if you need current weather or forecast with appropiate flags.")
    exit(1)
elif args.current and args.forecast:
    print("Please specify one of current or forecast with appropiate flags.")
    exit(1)

if args.current:
    #getting response if current flag is defined
    _weather = weather.getCurrent(apiKey, args.city, args.aqi)
    print(_weather)

if args.forecast:
    if args.days is not None:
        if args.days > 10 or args.days < 1:
            print("Days must be a number between 1 and 10")
            exit(1)

    elif args.days is None:
        print("Please specify days with appropiate flag. Must be an int between 1 and 10")
        exit(1)

    _weather = weather.getForecast(apiKey, args.city, args.aqi, args.days, args.alerts)
    print(_weather)
