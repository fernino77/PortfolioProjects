#import the necessary package!
import requests

#input the city name
city = input('Input the name of the city: ')
print(city)


#Display the message!
print('Displaying Weather Report For: ' + city)

#fetch the weather details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text)
