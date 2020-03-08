import requests

url = 'https://api.exchangeratesapi.io/latest'

data = requests.get(url)

# info = data.content
# print(info)

exchange_api = data.json()
rates = exchange_api['rates']

usr_crny_amnt = int(input('Please enter your amount: '))
usr_crny_name = input('Please enter your currency name: ').upper()

if usr_crny_name in rates.keys():
   cnvrt_cncy = usr_crny_amnt * rates[f'{usr_crny_name}']
   print(f'For {usr_crny_amnt} Euro you will get {cnvrt_cncy} {usr_crny_name}')
else:
    print(f'{usr_crny_name} Does not exist')