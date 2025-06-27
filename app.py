import dash
from dash import dcc, html, Input, State, Output
import plotly.graph_objects as go
import pandas as pd

df_earnings = pd.read_csv('docs/processed_data/Annual_Net_Earnings_Sweden_2014-2024.csv')
df_earnings = df_earnings[df_earnings['currency'] == 'National currency']

labels = {'One-earner couple with two children earning 100% of the average earning': '👱(💶)👱(-) 🧒🧒 Gezin 2 ouders, 2 kinderen, 1 ouder heeft gemiddeld inkomen',
 'Two-earner couple with two children, both earning 100% of the average earning': '👱(💶)👱(💶) 🧒🧒 Gezin 2 ouders, 2 kinderen, 2 ouders hebben allebij gmiddeld inkomen',
 'Two-earner couple with two children, one earning 100% and the other 33% of the average earning': '👱(💶)👱(🪙) 🧒🧒 Gezin 2 ouders, 2 kinderen, 1 ouder gemiddeld inkomen, 1 ouder 33% van gemiddeld',
 'Two-earner couple with two children, one earning 100% and the other 67% of the average earning': '👱(💶)👱(🪙🪙) 🧒🧒 Gezin 2 ouders, 2 kinderen, 1 ouder gemiddeld inkomen, 1 ouder 67% van gemiddeld',
 'Two-earner couple without children, both earning 100% of the average earning': '👱(💶)👱(💶) Gezin 2 volwassennen, 2 hebben allebij gemiddeld inkomen',
 'Two-earner couple without children, one earning 100% and the other 33% of the average earning': '👱(💶)👱(🪙) Gezin 2 volwassennen, 1 gemiddeld inkomen, 1 33% van gemiddeld inkomen',
 'Single person with two children earning 67% of the average earning': '👱(🪙🪙) 🧒🧒 Gezin 1 ouder, 2 kinderen, ouder 67% van gemiddeld inkomen',
 'Single person without children earning 67% of the average earning': '👱(🪙🪙) Gezin 1 volwassenne, met 67% van gemiddeld inkomen',
 'Single person without children earning 100% of the average earning': '👱(💶) Gezin 1 volwassenne, met gemiddeld inkomen',
 'Single person without children earning 125% of the average earning': '👱(💶🪙) Gezin 1 volwassenne, met 125% van gemiddeld inkomen',
 'Single person without children earning 167% of the average earning': '👱(💶🪙🪙) Gezin 1 volwassenne, met 167% van gemiddeld inkomen'}

estructs = ['Family allowances','Social Security','Taxes','Net earning']
marker_colors = {'Family allowances':"#F5B700", 'Social Security':"#DC0073", 'Taxes':"#371E30", 'Net earning':"#00C49A"}

app = dash.Dash(__name__)
app.title = "Inkomstenbronnen van gezinnen"
server = app.server

app.layout = html.Div([
    html.H2("Inkomstenbronnen van gezinnen"),
    dcc.Dropdown(
        id='group-dropdown',
        options=[{'label':labels[l], 'value':l} for l in labels],
        value='One-earner couple with two children earning 100% of the average earning'
    ),
    dcc.Graph(id='main-graph'),
    dcc.Store(id='current-mode', data={'mode': 'bar', 'group': 'One-earner couple with two children earning 100% of the average earning', 'year': None})
])

def create_stacked_bar(group):
    fig = go.Figure()
    for struct in estructs:
        subset = df_earnings[(df_earnings["estruct"] == struct) & (df_earnings["ecase"] == group)]
        fig.add_trace(go.Bar(
            x=subset["TIME_PERIOD"],
            y=subset["OBS_VALUE"],
            name=struct,
            marker_color = marker_colors[struct]
        ))
    fig.update_layout(barmode='stack', title=f'Inkomstenbronnen {labels[group]}')
    return fig

def create_donut(year, group):
    subset = df_earnings[(df_earnings["estruct"] == 'Family allowances') | (df_earnings["estruct"] == 'Net earning') | (df_earnings["estruct"] == 'Social Security')| (df_earnings["estruct"] =='Taxes')]
    subset = subset[(subset["TIME_PERIOD"] == year) & (subset["ecase"] == group)]
    fig = go.Figure(data=[go.Pie(
        labels=subset["estruct"],
        values=subset["OBS_VALUE"],
        marker_colors=["#F5B700","#00C49A", "#DC0073","#371E30"],
        hole=0.5
    )])
    fig.update_layout(title=f"Inkomstenbronnen {labels[group]} {year}")
    return fig

@app.callback(
    Output('main-graph', 'figure'),
    Output('current-mode', 'data'),
    Input('main-graph', 'clickData'),
    Input('group-dropdown', 'value'),
    State('current-mode', 'data')
)

def toggle_donut_bar(clickData, selected_group, stored_data):
    if selected_group == stored_data['group']:
        if stored_data['mode'] == 'bar':
            if clickData:
                clicked_year = clickData["points"][0]["x"]
                return create_donut(clicked_year, stored_data["group"]), {'mode': 'donut', 'group':stored_data['group'], 'year':clicked_year}
            return create_stacked_bar(stored_data['group']), stored_data
        else:
            return create_stacked_bar(stored_data['group']), {'mode': 'bar', 'group': stored_data['group'], 'year':None}
    else:
        if stored_data['mode'] == 'donut':
            return create_donut(stored_data['year'], selected_group), {'mode':stored_data['mode'], 'group': selected_group, 'year':stored_data['year']}
        else:
            return create_stacked_bar(selected_group), {'mode':stored_data['mode'], 'group': selected_group, 'year':stored_data['year']}

if __name__ == '__main__':
    app.run(debug=False)
