# Dataset Sources
These are the original dataset files.
The sources are:

**Dataset 1:**  <br>
*Original*  <br>
Food Prices.csv (Renamed to Food_Prices.csv from here on out, to avoid problems with the source string.)  <br>
https://www.kaggle.com/datasets/sumangoda/food-prices  <br>
df_food_prices  <br>
*Filtered*  <br>
240 entries, 9 columns  <br>
`df_food_pricees_sweden = df_food_prices[df_food_prices['Country '] == 'Sweden'].drop('Country ', axis=1)`  <br>
df_food_prices_sweden  <br>

**Dataset 2:**  <br>
*Original*  <br>
WDI_Indicators_MainData.csv  <br>
https://www.kaggle.com/datasets/parsabahramsari/wdi-education-health-and-employment-2011-2021  <br>
df_wdi_indicators  <br>
*Filtered*  <br>
11 entries, 93 columns  <br>
/sweden/WDI_Indicators_Sweden.csv  <br>
`df_wdi_indicators[df_wdi_indicators['Country Name'] == 'Sweden'].drop('Country Name', axis=1).drop('Country Code', axis=1)`  <br>
df_wdi_indicators_sweden  <br>

**Dataset 3:**  <br>
*Original*  <br>
estat_earn_nt_net_en.csv  <br>
https://ec.europa.eu/eurostat/databrowser/view/earn_nt_net__custom_17081659/default/table?lang=en  <br>
df_annual_net_earnings  <br>
*Filtered*  <br>
5742 entries, 10 columns  <br>
/sweden/Annual_Net_Earnings_Sweden.csv  <br>
`df_annual_net_earnings_sweden = df_annual_net_earnings[df_annual_net_earnings['geo'] == 'Sweden'].drop('geo', axis=1)`  <br>
df_annual_net_earnings_sweden  <br>
