# Datasets

## Dataset 1: Consumer Price Index
TODO Nieuwe dataset gebruiken https://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__PR__PR0101__PR0101S/SnabbStatPR0101/table/tableViewLayout1/ <br>
**Original**
<table><tr>
<td>Name</td><td>Vital Food Costs: A Five-Nation Analysis 2018-2022 </td></tr><tr>
<td>Source</td><td> [https://www.kaggle.com/datasets/sumangoda/food-prices](https://www.kaggle.com/datasets/sumangoda/food-prices) </td></tr><tr>
<td>Records</td><td>1200 </td></tr><tr>
<td>Variables</td><td>10 </td></tr></table>

*Filtered**<br>
```
df_food_pricees_sweden = df_food_prices[df_food_prices['Country '] == 'Sweden'].drop('Country ', axis=1)
df_food_prices_sweden_years = df_food_prices_sweden[df_food_prices_sweden['Year '] <= 2021]
```

<table>
<thead><tr><td></td><td>Sweden </td><td>Sweden 2018 - 2021 </td></tr></thead><tbody>
<tr>
<td>Records</td><td>240</td><td>190 </td></tr><tr>
<td>Variables</td><td>9 </td><td>9</td></tr></tbody></table>

**Description**<br>
Deze dataset bevat de maandelijkse prijzen van vier essentiële voedingsmiddelen (melk, eieren, brood en aardappelen) in vijf landen (Australië, Japan, Canada, Zuid-Afrika en Zweden) van 2018 tot 2022. Elk record bevat het land, de datum, het artikel, de prijs in lokale valuta, de prijs in dollars, de beschikbaarheid en de kwaliteit van het product. Deze dataset kan helpen bij het beoordelen van de betaalbaarheid van voedsel, de kosten van levensonderhoud en de gevolgen van inflatie. Wij focussen hierbij specifiek op de data van Zweden.

## Dataset 2: WDI: Education, Health & Emplyment

**Original**
<table><tr>
<td>Name </td><td>WDI: Education, Health & Employment (2011 - 2021) </td></tr><tr>
<td>Source </td><td> [https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021](https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021) </td></tr><tr>
<td>Records </td><td>209 </td></tr><tr>
<td>Variables </td><td>95 </td></tr></table>

**Filtered**<br>
```
df_wdi_indicators_sweden = df_wdi_indicators[df_wdi_indicators['Country Name'] == 'Sweden'].drop('Country Name', axis=1).drop('Country Code', axis=1)
df_wdi_indicators_sweden_years = df_wdi_indicators_sweden[df_wdi_indicators_sweden['Time'] >= 2018]
```
<table>
<thead><tr><td></td><td>Sweden </td><td>Sweden 2018 - 2021 </td></tr></thead><tbody>
<tr>
<td>Records </td><td>11</td><td>4</td></tr><tr>
<td>Variables </td><td>93</td><td>93</td></tr></tbody></table>

**Description** <br>
Deze dataset bevat wereldwijde sociaaleconomische indicatoren zoals onderwijs, gezondheid en werkgelegenheid, tussen 2011 en 2021 van 19 geavanceerde economieën. Het biedt statistieken per land per jaar, zoals het werkloosheidspercentage, het gemiddelde inkomen, het opleidingsniveau en gezondheidsindicatoren. Hiermee is het mogelijk om de 19 landen te vergelijken op basis van onderwijs, werkgelegenheid, gezondheidszorg en het geeft demografie om trends en verschillen te identificeren. Wij zullen hierbij focussen op Zweden.

## Dataset 3: Annual net earnings
**Original**
<table><tr>
<td>Name </td><td>Annual net earnings </td></tr><tr>
<td>Source </td><td> [https://ec.europa.eu/eurostat/databrowser/bookmark/6adafcb6-297e-4d27-b687-9b7c189c264c?lang=en](https://ec.europa.eu/eurostat/databrowser/bookmark/6adafcb6-297e-4d27-b687-9b7c189c264c?lang=en) </td></tr><tr>
<td>Records </td><td>193548 </td></tr><tr>
<td>Variables </td><td>11 </td></tr><tr></table>

**Filtered**<br>
```
df_annual_net_earnings_sweden = df_annual_net_earnings[df_annual_net_earnings['geo'] == 'Sweden'].drop('geo', axis=1)
df_annual_net_earnings_sweden_years = df_annual_net_earnings_sweden[(df_annual_net_earnings_sweden['TIME_PERIOD'] >= 2018) & (df_annual_net_earnings_sweden['TIME_PERIOD'] <= 2021)]
```
<table>
<thead><tr><td></td><td>Sweden </td><td>Sweden 2018 - 2021 </td></tr></thead><tbody>
<tr>
<td>Records </td><td>5742 </td><td>936</td></tr><tr>
<td>Variables </td><td>10 </td><td>10</td></tr></tbody></table>

**Description** <br>
Deze dataset is een subset van de Annual net earnings, een subset met alleen Zweden. 
De originele dataset bevat netto inkomsten die reflecterend zijn voor verschillende soorten gezinnen in de EU en landen die economisch sterk verbonden zijn met de EU, door de jaren heen (2000 - 2024), per land. Waar het netto inkomen uit is opgebouwd (bruto inkomen / belastingen / financiële ondersteuning van de overheid, etc.) worden benoemd. De data komen van een Model, dat op zichzelf is gebaseerd op data die verschillende landen zelf hebben gedeeld.<br>
