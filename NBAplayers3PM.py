import pandas as pd

nbaData = pd.read_csv('./datasets/NBAStats.csv')
pd.set_option('display.max_columns', None)

newDataNba = nbaData[['FULL NAME', '3PA', '3P%']].dropna(subset=['3PA', '3P%'])
newDataNba['3P%'] = newDataNba['3P%'] * 100
threePointsMade = newDataNba.assign(threePoints = (round((newDataNba['3PA'] * newDataNba['3P%']) / 100)))
threePointsMade['threePoints'] = threePointsMade['threePoints'].astype(int)
threePointsMade.rename(columns = {'threePoints':'3PM'}, inplace = True)
bestThrees = threePointsMade.sort_values(by='3PM', ascending=False)
print(bestThrees.head(50))