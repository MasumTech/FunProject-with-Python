cvrt_rates = {'USD':80.00, 'CAD':65.66, 'GBP': 55.34, 'CHF':33.54, 'AUD':11.45, 'INR':78.90}

crny_name = input('Please enter your currency name: ')
crny_amnt = int(input('Please enter your amount: '))
f = int(0)

if crny_name == 'USD':
    conv_cur = crny_amnt * cvrt_rates['USD']
elif crny_name == 'CAD':
    conv_cur = crny_amnt * cvrt_rates['CAD']
elif crny_name == 'GBP':
    conv_cur = crny_amnt * cvrt_rates['GBP']
elif crny_name == 'CHF':
    conv_cur = crny_amnt * cvrt_rates['CHF']
elif crny_name == 'AUD':
    conv_cur = crny_amnt * cvrt_rates['AUD']
elif crny_name == 'INR':
    conv_cur = crny_amnt * cvrt_rates['INR']
else:
    f = int(1)
    print('Opps! Unknown currency')

if f==0:
    print(f'Successfully converted! For {crny_amnt} {crny_name} you will get {conv_cur} BDT')
