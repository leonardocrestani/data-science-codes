import pandas as pd

#-----------------------------Coleta dos dados-----------------------------

file = './datasets/flights.csv'
flights = pd.read_csv(file)
pd.set_option('display.max_columns', None)

#-----------------------------Analise dos dados-----------------------------

# 5 primeiros voos
firstFiveFlights = flights.head(5)
# 5 ultimos voos
lastFiveFlights = flights.tail(5)

# voos com atraso maior que 2 horas
flightsWithDelay = flights.query("arr_delay > 2.0")

# voos com destino IAH e HOU (cidade de Houston)
flightsDestinyHouston = flights[(flights["dest"] == "IAH") | (flights["dest"] == "HOU")]

# voos pela empresa DL no dia 21
DLFlights = flights[(flights["day"] == 21) & (flights['month'] == 12) & (flights["carrier"] == "DL")]

# voos entre 00 (24) e 6 da manha
midnightFlights = flights.query("dep_time < 24  & dep_time > 6")

# dataset ordenado por data
flightsByDate = flights.sort_values(['time_hour'])

# voos mais rapidos
flightsSpeed = flights.assign(speed = flights.distance / flights.air_time)
fasterFlights = flightsSpeed.sort_values(by='speed', ascending=False)

# voo mais curto e mais longo
# tirar linhas da coluna air time que possuem o valor NaN
data = flights.dropna(subset=["air_time"])
flightsTime = data.sort_values(by='air_time', ascending=False)
fasterFlight = flightsTime.head(1)
slowerFlight = flightsTime.tail(1)

# novo dataframe apenas com as colunas 'dep_time', 'dep_delay', 'arr_time', 'arr_delay'
newDataFlights = flights[['dep_time', 'dep_delay', 'arr_time', 'arr_delay']].dropna(subset=['dep_time', 'dep_delay', 'arr_time', 'arr_delay'])

# dataframe somente com os voos nao cancelados
notCancelledFlights = flights[(flights["dep_delay"] != 'NA') | (flights["arr_delay"] != 'NA')].dropna(subset=["dep_delay", "arr_delay"])

# agrupar pelo destino e contar o numero de voos por destino utilizando o novo dataframe de nao cancelados
flightsByDestiny = notCancelled.groupby(["dest"])['dest'].count()

# dataframe qual mostra as empresas aéreas que mais atrasam voos na média
delayMeanByCarrier = flights.groupby(["carrier"]).agg({
  "arr_delay" : "mean"
}).sort_values(by = 'arr_delay', ascending=False)
