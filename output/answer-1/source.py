import pandas as pd

url = 'https://raw.githubusercontent.com/Priyadharshan134/internship-test2/master/input/question-1/main.csv'
crime = pd.read_csv(url,sep=',')
crime.Year = pd.to_datetime(crime.Year,format='%Y')
crime.Year
crime = crime.set_index('Year',drop=True)


del crime['Total']
crime.head()


crimes = crime.resample('10AS').sum()

population = crimes['Population'].resample('10AS').max()
print(population)
crimes['Population'] = population
crimes

