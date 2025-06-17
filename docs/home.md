# Informatie Visualisatie G1 (24)

- Amora van Deursen 15759601 [github](https://github.com/moratje111)
- Emilie Rosier 15838366 [github](https://github.com/emilierosier)
- May Bardet 13160974 [gibhub](https://github.com/MayBardet)
- Sabih Syed 15611175 [github](https://github.com/prox05/)

*Temporary Title*
# Verhouding tussen voedselprijzen, inkomen en werkgelegenheid in Zweden

## Table of Contents
- [Introductie](#int)
- [Dataset en Preprocessing](#dap)
- [Visualisatie](#vis)

<a name="int"></a>
## Introductie


*Topic description in your own words* <br>
De kosten van leefbaarheid zijn een belangrijk onderwerp in Zweden. Zo is te zien dat de prijs van voedsel in de afgelopen jaren is gestegen. Veel burgers vinden het te duur geworden voor hun inkomen. Tegelijkertijd zien we dat het jaarlijkse netto-inkomen ook is gestegen en dat de werkgelegenheid redelijk stabiel is gebleven. Is deze inkomensstijging genoeg om de kosten van leefbaarheid te betalen? Met de gevonden datasets onderzoeken wij de verschillende perspectieven. <br><br>

*First Perspective* <br>
De prijzen van het voedsel in Zweden zijn de afgelopen jaren gestegen. Hierdoor zijn er veel huishoudens die het niet meer kunnen betalen om comfortabel te leven. <br><br>

*Second Perspective* <br>
De werkgelegenheid in Zweden is de afgelopen jaren stabiel gebleven en het nettoloon is zelfs gestegen. Hierdoor zouden de inwoners van Zweden in principe de gestegen kosten van het voedsel moeten kunnen betalen. <br><br>

<a name="dap"></a>
## Dataset en Preprocessing


### Dataset 1
**Original**
<table><tr>
<td>Name</td><td>Vital Food Costs: A Five-Nation Analysis 2018-2022 </td></tr><tr>
<td>Source</td><td>[https://www.kaggle.com/datasets/sumangoda/food-prices](https://www.kaggle.com/datasets/sumangoda/food-prices) </td></tr><tr>
<td>Records</td><td>1200 </td></tr><tr>
<td>Variables</td><td>10 </td></tr></table>

**Filtered**<br>
Filter (Sweden): `df_food_pricees_sweden = df_food_prices[df_food_prices['Country '] == 'Sweden'].drop('Country ', axis=1)`
<table><tr>
<td>Records</td><td>240 </td></tr><tr>
<td>Variables</td><td>9 </td></tr></table>

**Description**<br>
Deze dataset bevat de maandelijkse prijzen van vier essentiële voedingsmiddelen (melk, eieren, brood en aardappelen) in vijf landen (Australië, Japan, Canada, Zuid-Afrika en Zweden) van 2018 tot 2022. Elk record bevat het land, de datum, het artikel, de prijs in lokale valuta, de prijs in dollars, de beschikbaarheid en de kwaliteit van het product. Deze dataset kan helpen bij het beoordelen van de betaalbaarheid van voedsel, de kosten van levensonderhoud en de gevolgen van inflatie. Wij focussen hierbij specifiek op de data van Zweden.

### Dataset 2
**Original**
<table><tr>
<td>Name</td><td>WDI: Education, Health & Employment (2011 - 2021) </td></tr><tr>
<td>Source</td><td>[https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021](https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021) </td></tr><tr>
<td>Records</td><td>209 </td></tr><tr>
<td>Variables</td><td>95 </td></tr></table>

**Filtered**<br>
Filter (Sweden): `df_wdi_indicators[df_wdi_indicators['Country Name'] == 'Sweden'].drop('Country Name', axis=1).drop('Country Code', axis=1)`
<table><tr>
<td>Records</td><td>11 </td></tr><tr>
<td>Variables</td><td>93 </td></tr></table>

**Description**
Deze dataset bevat wereldwijde sociaaleconomische indicatoren zoals onderwijs, gezondheid en werkgelegenheid, tussen 2011 en 2021 van 19 geavanceerde economieën. Het biedt statistieken per land per jaar, zoals het werkloosheidspercentage, het gemiddelde inkomen, het opleidingsniveau en gezondheidsindicatoren. Hiermee is het mogelijk om de 19 landen te vergelijken op basis van onderwijs, werkgelegenheid, gezondheidszorg en het geeft demografie om trends en verschillen te identificeren. Wij zullen hierbij focussen op Zweden.

### Dataset 3
**Original**
<table><tr>
<td>Name</td><td>Annual net earnings </td></tr><tr>
<td>Source</td><td>[https://ec.europa.eu/eurostat/databrowser/bookmark/6adafcb6-297e-4d27-b687-9b7c189c264c?lang=en](https://ec.europa.eu/eurostat/databrowser/bookmark/6adafcb6-297e-4d27-b687-9b7c189c264c?lang=en) </td></tr><tr>
<td>Records</td><td>193548 </td></tr><tr>
<td>Variables</td><td>11 </td></tr><tr></table>

**Filtered**<br>
Filter (Sweden): `df_annual_net_earnings_sweden = df_annual_net_earnings[df_annual_net_earnings['geo'] == 'Sweden'].drop('geo', axis=1)`
<table><tr>
<td>Records</td><td>5742 </td></tr><tr>
<td>Variables</td><td>10 </td></tr></table>

**Description**
Deze dataset is een subset van de Annual net earnings, een subset met alleen Zweden. 
De originele dataset bevat netto inkomsten die reflecterend zijn voor verschillende soorten gezinnen in de EU en landen die economisch sterk verbonden zijn met de EU, door de jaren heen (2000 - 2024), per land. Waar het netto inkomen uit is opgebouwd (bruto inkomen / belastingen / financiële ondersteuning van de overheid, etc.) worden benoemd. De data komen van een Model, dat op zichzelf is gebaseerd op data die verschillende landen zelf hebben gedeeld.

<a name="vis"></a>
## Visualisatie

