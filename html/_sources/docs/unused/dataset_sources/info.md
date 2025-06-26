# Dataset Sources
These are the original dataset files.
The sources are:

**Dataset 1:**  <br>
*Original*  <br>
Name	Vital Food Costs: A Five-Nation Analysis 2018-2022 <br>
Source	[https://www.kaggle.com/datasets/sumangoda/food-prices](https://www.kaggle.com/datasets/sumangoda/food-prices) <br>
Records	1200 <br>
Variables	10 <br>
*Filtered*  <br>
/filtered/Food_Prices_Sweden.csv - 240 records; 9 variables <br>
/filtered/Food_Prices_Sweden_2018-2021.csv - 190 records; 9 variables <br>
```
df_food_pricees_sweden = df_food_prices[df_food_prices['Country '] == 'Sweden'].drop('Country ', axis=1)
df_food_prices_sweden_years = df_food_prices_sweden[df_food_prices_sweden['Year '] <= 2021]
```
**Description**<br>
Deze dataset bevat de maandelijkse prijzen van vier essentiële voedingsmiddelen (melk, eieren, brood en aardappelen) in vijf landen (Australië, Japan, Canada, Zuid-Afrika en Zweden) van 2018 tot 2022. Elk record bevat het land, de datum, het artikel, de prijs in lokale valuta, de prijs in dollars, de beschikbaarheid en de kwaliteit van het product. Deze dataset kan helpen bij het beoordelen van de betaalbaarheid van voedsel, de kosten van levensonderhoud en de gevolgen van inflatie. Wij focussen hierbij specifiek op de data van Zweden.<br>

**Dataset 2:**  <br>
*Original*  <br>
Name 	WDI: Education, Health & Employment (2011 - 2021) <br>
Source 	[https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021](https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021) <br>
Records 	209 <br>
Variables 	95 <br>
**Filtered** <br>
/filtered/WDI_Indicators_Sweden.csv - 11 records; 93 variables; <br>
/filtered/WDI_Indicators_Sweden_2018-2021.csv - 4 records; 93 variables;<br>
```
df_wdi_indicators_sweden = df_wdi_indicators[df_wdi_indicators['Country Name'] == 'Sweden'].drop('Country Name', axis=1).drop('Country Code', axis=1)
df_wdi_indicators_sweden_years = df_wdi_indicators_sweden[df_wdi_indicators_sweden['Time'] >= 2018]
```
**Description** <br>
Deze dataset bevat wereldwijde sociaaleconomische indicatoren zoals onderwijs, gezondheid en werkgelegenheid, tussen 2011 en 2021 van 19 geavanceerde economieën. Het biedt statistieken per land per jaar, zoals het werkloosheidspercentage, het gemiddelde inkomen, het opleidingsniveau en gezondheidsindicatoren. Hiermee is het mogelijk om de 19 landen te vergelijken op basis van onderwijs, werkgelegenheid, gezondheidszorg en het geeft demografie om trends en verschillen te identificeren. Wij zullen hierbij focussen op Zweden.<br>

**Dataset 3:**  <br>
*Original*  <br>
estat_earn_nt_net_en.csv (Not uploaded to github due to file size) <br>
https://ec.europa.eu/eurostat/databrowser/view/earn_nt_net__custom_17081659/default/table?lang=en  <br>
df_annual_net_earnings  <br>
*Filtered*  <br>
5742 entries, 10 columns  <br>
/filtered/Annual_Net_Earnings_Sweden.csv - 5742 records; 10 variables; <br>
/filtered/Annual_Net_Earnings_Sweden_2018-2021.csv - 936 records; 10 variables; <br>
```
df_annual_net_earnings_sweden = df_annual_net_earnings[df_annual_net_earnings['geo'] == 'Sweden'].drop('geo', axis=1)
df_annual_net_earnings_sweden_years = df_annual_net_earnings_sweden[(df_annual_net_earnings_sweden['TIME_PERIOD'] >= 2018) & (df_annual_net_earnings_sweden['TIME_PERIOD'] <= 2021)]
```
**Description** <br>
Deze dataset is een subset van de Annual net earnings, een subset met alleen Zweden. 
De originele dataset bevat netto inkomsten die reflecterend zijn voor verschillende soorten gezinnen in de EU en landen die economisch sterk verbonden zijn met de EU, door de jaren heen (2000 - 2024), per land. Waar het netto inkomen uit is opgebouwd (bruto inkomen / belastingen / financiële ondersteuning van de overheid, etc.) worden benoemd. De data komen van een Model, dat op zichzelf is gebaseerd op data die verschillende landen zelf hebben gedeeld.<br>
