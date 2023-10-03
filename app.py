import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit.components.v1 import html
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

st.title("From Doubters to Believers:")
st.header("The Evolution of Liverpool FC Under Jürgen Klopp")

st.image("https://media.giphy.com/media/l3q2zCKVADRJtZCP6/giphy.gif", caption='Source: giphy.com', use_column_width=True)

st.markdown("### A Storied Club in a Period of Flux")

st.markdown("Liverpool Football Club, founded in 1892, is one of the most successful football clubs in the history of the English game. \
            With 19 English league titles, 6 European Cups, and numerous other domestic and international trophies, the club has a rich legacy that is the envy of many. \
            However, every tale of glory has its chapters of struggle, and for Liverpool, this period of inconsistency was notably evident in the years leading up to 2015."
)

st.markdown("### The Pre-Klopp Era: A Statistical Overview")

st.markdown("Before the arrival of Liverpool FC's new manager Jürgen Klopp in October 2015, the club was in a state of flux, both on and off the pitch. \
            The club had not won a league title since the 1989-1990 season, and their performances in other competitions were equally inconsistent. \
            For this statistical overview, we will be analyzing the six seasons before Jürgen Klopp's appointment.\
            \n \
            \n To set the stage, let's delve into some key data points:"
)

# Win Loss Records
st.markdown("##### Win-Loss-Draw Results")
st.markdown("Between the 2009-2010 and 2014-2015 seasons, Liverpool's win percentage in the Premier League fluctuated between 36.8% and 68.4%. \
            The club's best season during this time was 2013-2014, when they finished 2nd in the league only 2 points behind Manchester City. \
            Other than this standout season, Liverpool's performances could be described as mediocre at best. \
")
            
df_liv_results = pd.read_csv('results_with_without_klopp.csv')
df_liv_seasons = pd.read_csv('season_results_without_klopp.csv')
df_liv_standings = pd.read_csv('standings_without_klopp.csv')

# remoeve last column
df_liv_results = df_liv_results.iloc[:, :-1]

# pie chart
fig_pie_liv_results = px.pie(df_liv_results, values='Without Klopp', names='Result')
fig_pie_liv_results.update_layout(
    title = 'Liverpool FC Results before Jürgen Klopp',
    legend_title = '',

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: kaggle.com | Premier League Matches 1993-2023",
            xref="paper",
            yref="paper"
        )
    ]
)

# create a diagram to show the win-loss-draw results grouped by season
fig_bar_liv_results = px.bar(df_liv_seasons, x='Season_End_Year', y='Count', color='Liverpool_Result', barmode='group')
fig_bar_liv_results.update_layout(
    title = 'Liverpool FC Results before Jürgen Klopp',
    legend_title = '',
    xaxis_title = 'Season End Year',
    yaxis_title = 'Percentage of Matches',

    # stacked bar chart
    barmode = 'stack',

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: kaggle.com | Premier League Matches 1993-2023",
            xref="paper",
            yref="paper"
        ),
    ]
)

tab1, tab2 = st.tabs(["Seasons Combined", "Seasons Separated"])
with tab1:
    st.plotly_chart(fig_pie_liv_results, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig_bar_liv_results, theme="streamlit", use_container_width=False)


# League Positions
st.markdown("##### League Positions")
st.markdown("In the five seasons before Klopp's arrival, Liverpool's league finishes were as follows: \
            7th (2009-10), 6th (2010-11), 8th (2011-12), 7th (2012-13), 2nd (2013-14), and 6th (2014-15). \
            The 2013-14 season was a high point, but it was sandwiched between years of disappointment. \
            Hover over the line chart below to see the exact league positions and points totals for each season. \
")
            
# Create subplots
fig_liv_standings = go.Figure()

# Add traces
fig_liv_standings.add_trace(go.Scatter(x=df_liv_standings['Season_End_Year'], y=df_liv_standings['Rk'], mode='lines', hovertext=df_liv_standings['Pts']))


#fig_line_liv_standings = px.line(df_liv_standings, x='Season_End_Year', y='Rk', hovertext='Pts')
fig_liv_standings.update_layout(
    title = 'Liverpool FC League Positions before Jürgen Klopp',
    legend_title = '',
    xaxis_title = 'Season End Year',
    yaxis_title = 'League Position',

    yaxis = dict(
        autorange = False,
        range = [20,1],
        dtick = 1
    ),

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: kaggle.com | Premier League Standings 1993-2023",
            xref="paper",
            yref="paper"
        ),
    ]
)

st.plotly_chart(fig_liv_standings, theme="streamlit", use_container_width=True)

# Trophies Won
st.markdown("##### Trophies")
st.markdown("The club managed to win the League Cup in the 2011-2012 season but failed to secure any other major domestic or international trophies. Their European campaigns were equally lackluster, with exits in the early knockout stages or failure to qualify altogether.")


st.markdown("This period was marked by managerial changes, tactical indecisiveness, and a lack of a coherent long-term vision. \
            Fans were growing restless, and there was a palpable need for change - a change that would eventually come in the form of Jürgen Klopp. \
")
            
st.markdown("Let's take a look on how he transformed the club. \
            But before we do that; \
            **Who is Jürgen Klopp? And why did Liverpool hire him?** \
")
            
st.markdown("### The Manager")

st.image("https://media.giphy.com/media/WV3if1rJykgbku0zq1/giphy.gif", caption='Source: giphy.com', use_column_width=True)

st.markdown("Jürgen Klopp is a German football manager well known for his tactical genius and team-building skills. \
            He is also known for his charismatic personality, tactical acumen, and ability to build strong team cohesion. \
            Klopp is credited with implementing a high-intensity style of play called 'Gegenpressing', which aims to win back the ball as quickly as possible after losing possession.\
")
            
st.markdown("###### Career Highlights")
st.markdown("Before joining Liverpool, Klopp had a successful managerial stint at Borussia Dortmund in Germany. \
            Under his leadership, Dortmund won two Bundesliga titles, a DFB-Pokal, and reached the UEFA Champions League final in 2013. \
            His success at Dortmund made him one of the most sought-after managers in European football. \
")


# ------------------ MITTELTEIL ---------------------

st.markdown("### The Transformation")
st.markdown("##### Formations")

st.markdown("We can see that before Jürgen Klopp was appointed, that Liverpool FC used so many different formations. \
            This is a sign of a team that is struggling to find it's identity. \
            Under Jürgen Klopp, Liverpool FC has primarily employed a high-pressing 4-3-3 formation. \
            However, we can see that in the beginning that Klopp experimented with many different formations, \
            trying to find the right fit for his squad. \
            The increase in games under Jürgen Klopp is due to the fact that they were a lot more successful, resulting in playing in more torunaments. \
")

df_liv_formations = pd.read_csv('liverpool_formations.csv')

fig_liv_formations = px.line(df_liv_formations, x='Season_End_Year', y='Count', color='Formation')
fig_liv_formations.update_layout(
    title='Liverpool FC Formations',
    xaxis_title='Season End Year',
    yaxis_title='Games Played',

    # add line at x = 2015 -> Klopp's first season
    shapes=[
        dict(
            type= 'line',
            xref= 'x',
            yref= 'y',
            x0= 2016,
            y0= 0,
            x1= 2016,
            y1= 60,
            line=dict(
                color="black",
                width=2,
                dash="dashdot"
            )
        )
    ],
 
    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: footballcritic.com | Liverpool FC Formations",
            xref="paper",
            yref="paper"
        ),

        dict(
            x=2016,
            y=40,
            showarrow=True,
            arrowhead=7,
            ax=-75,
            text="Klopp's Arrival",
        ),
    ]
)

st.plotly_chart(fig_liv_formations, theme="streamlit", use_container_width=True)

st.markdown("##### Pressing Intensity")

st.markdown("The 4-3-3 formation is a very flexible formation that can be used to play a variety of styles. \
            Klopp's Liverpool has primarily used this formation to play a high-pressing, counter-attacking style of football. \
            The team presses high up the pitch, forcing the opposition to make mistakes and then capitalizing on those mistakes \
            to score goals. This style of play is very physically demanding, and it requires a high level of fitness from the players.\
")
            
st.image('liverpool_pressing.png', width = 500, caption='Source: anfieldindex.com | Liverpool FC Pressing')

# st.markdown("##### Case Studies: Tactical Brilliance in Key Matches")

# st.markdown("###### Liverpool 4-0 Barcelona (4-3 agg.) - 2018-19 Champions League Semi-Final Second Leg")

# st.markdown("In the second leg of the 2018-19 Champions League Semi-Final, Liverpool were trailing 3-0 on aggregate \
#             after a disappointing performance in the first leg at the Camp Nou. The odds were stacked against them. \
#             However, Klopp's tactical brilliance and the players' determination to win the match \
#             allowed them to pull off one of the greatest comebacks in Champions League history. \
#             Let's take a look at how they did it.")

# st.image('https://e0.365dm.com/19/05/1600x900/skysports-liverpool-goal-origi_4662066.jpg?20190507214604', use_column_width=True, caption='Source: skysports.com | Liverpool FC vs Barcelona')

# Player Development

st.markdown("##### Liverpool vs. Biggest Rivals")

st.markdown("Liverpool FC has a long history of rivalries with other clubs, including Manchester United and Everton. \
            The Reds have also developed a rivalry with Manchester City in recent years, as both teams have been competing for the Premier League title. \
            Arsenal, Tottenham and Chelsea have also been added to the list of Liverpool's rivals, as they are all in the so-called 'Big Six' of the Premier League. \
            \n \
            In this section, we will look at Liverpool's results against these rivals since 2009. \
")

df_rivals_results = pd.read_csv('df_liv_rivals.csv')

fig_liv_rivals_results = px.bar(df_rivals_results, x='Season_End_Year', y='Count', color='Liverpool_Result', barmode='group')
fig_liv_rivals_results.update_layout(
    title = 'Liverpool FC Win-Loss-Draw Results Against Rivals',
    legend_title = '',
    xaxis_title = 'Season End Year',
    yaxis_title = 'Percentage of Matches',

    # stacked bar chart
    barmode='stack',

    # show all ticks
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1
    ),
    
    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: kaggle.com | Premier League Matches 1993-2023",
            xref="paper",
            yref="paper"
        )
    ]
)

st.plotly_chart(fig_liv_rivals_results, theme="streamlit", use_container_width=True)

st.markdown("As we can see, Jürgen Klopp and his squad have had a lot of success in the big games, drastically reducing their defeats. \
            In seasons 2017 and 2022, Liverpool did not lose a single match against their rivals. \
")
            
# League Positions
st.markdown("##### League Positions Under Klopp")
st.markdown("In this section, we will look at Liverpool's league positions under Jürgen Klopp. \
            We can see that the Reds have consistently finished in the top 4 since Klopp's arrival. \
            In the 2019-20 season, they won the Premier League title for the first time in 30 years.")
  
df_liv_standings_klopp = pd.read_csv('standings_with_klopp.csv')

# Create subplots
fig_df_liv_standings_klopp = go.Figure()

# Add traces
fig_df_liv_standings_klopp.add_trace(go.Scatter(x=df_liv_standings_klopp['Season_End_Year'], y=df_liv_standings_klopp['Rk'], mode='lines', hovertext=df_liv_standings_klopp['Pts']))


#fig_line_liv_standings = px.line(df_liv_standings, x='Season_End_Year', y='Rk', hovertext='Pts')
fig_df_liv_standings_klopp.update_layout(
    title = 'Liverpool FC League Positions under Jürgen Klopp',
    legend_title = '',
    xaxis_title = 'Season End Year',
    yaxis_title = 'League Position',

    yaxis = dict(
        autorange = False,
        range = [20,1],
        dtick = 1
    ),

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: kaggle.com | Premier League Standings 1993-2023",
            xref="paper",
            yref="paper"
        ),
    ]
)

st.plotly_chart(fig_df_liv_standings_klopp, theme="streamlit", use_container_width=True)

st.markdown("#### Most Influential Players Under Klopp")

df_salah = pd.read_excel('salah_stats.xlsx', sheet_name='salah_stats')
df_alisson = pd.read_excel('salah_stats.xlsx', sheet_name='alisson_stats')
df_mignolet = pd.read_excel('salah_stats.xlsx', sheet_name='mignolet_stats')
df_trent= pd.read_excel('salah_stats.xlsx', sheet_name='trent_stats')


col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Mohamed Salah")
    st.image('https://backend.liverpoolfc.com/sites/default/files/styles/xs/public/2023-07/pp-23-24-mens-home-body-salah.webp?itok=usRCmKmb', caption='Source: liverpoolfc.com | Mohamed Salah', width=250)


st.markdown("In 2017, Mohamed Salah signed with Liverpool for a then-club record transfer fee of £36.9 million. \
            He has since become a highly successful forward for Liverpool FC, winning numerous medals in competitions such as the Premier League, Champions League, FA Cup, and Carabao Cup. \
            He has achieved impressive milestones for Liverpool, including passing the 250-appearance and 150-goal marks, entering the top 10 of the club's all-time leading scorers list, and becoming the club's all-time top Premier League goalscorer. \
            Salah's consistency and remarkable performances have earned him many individual awards, including the PFA Players' Player of the Year and Football Writers' Association Footballer of the Year awards. \
            He has recently signed a new long-term contract with Liverpool and is eager to win more trophies with the club.")

st.markdown('"I feel great and [I am] excited to win trophies with the club… I have enjoyed my football here at the club and hopefully I will continue to enjoy it and win many trophies," he said.')

st.markdown("Let's take a look at some of his statistics.")

fig_salah = go.Figure()

fig_salah.add_trace(go.Scatter(x=df_salah['Season_End_Year'], y=df_salah['Goals'], mode='lines', name='Goals', hovertext=df_salah['Squad']))
fig_salah.add_trace(go.Scatter(x=df_salah['Season_End_Year'], y=df_salah['Assists'], mode='lines', name='Assists', hovertext=df_salah['Squad']))

fig_salah.update_layout(
    title='Mohamed Salah Statistics',
    xaxis_title='Season End Year',
    yaxis_title='Count',

    # show every tick
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=1
    ),

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: fbref.com | Mohamed Salah Statistics",
            xref="paper",
            yref="paper"
        ),
    ]
)

# Create subplots
fig_salah_2 = go.Figure()

# Add traces
fig_salah_2.add_trace(go.Scatter(x=df_salah['Season_End_Year'], y=df_salah['MP'], mode='lines', name='Matches Played', hovertext=df_salah['Squad']))
fig_salah_2.add_trace(go.Scatter(x=df_salah['Season_End_Year'], y=df_salah['Starts'], mode='lines', name='Matches Started', hovertext=df_salah['Squad']))

# Update layout
fig_salah_2.update_layout(
    title='Mohamed Salah Statistics',
    xaxis_title='Season End Year',
    yaxis_title='Count', 

    # show every tick
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=1
    ), 

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: fbref.com | Mohamed Salah Statistics",
            xref="paper",
            yref="paper"
        ),
    ]
)

tab3, tab4 = st.tabs(["Goals & Assists", "Matches Played & Started"])
with tab3:
    st.plotly_chart(fig_salah, theme="streamlit", use_container_width=True)
with tab4:
    st.plotly_chart(fig_salah_2, theme="streamlit", use_container_width=True)

st.markdown("As we can see from the graph above, Salah has been a prolific goalscorer for Liverpool, improving drastically compared to his previous seasons at Roma and Fiorentina. \
            He even broke the Premier League record for most goals scored in a 38-game season with 32 goals in his first season, exceeding all expectations. \
            Salah has also been a creative force for Liverpool, providing many assists for his teammates. \
            Another impressive stat is the amount of matches played and started, arguably being one of the most consistent players in the team by starting most games. \
            All this together makes him one of the most important players Jürgen Klopp has signed for Liverpool. \
")


col3, col4 = st.columns(2)

with col3:
    st.markdown("##### Alisson Becker")
    st.image('https://backend.liverpoolfc.com/sites/default/files/styles/lg/public/2023-07/pp-23-24-mens-home-body-becker.webp?itok=Ikgbv2my', caption='Source: liverpoolfc.com | Alisson Becker', width=250)

# alison description
st.markdown("Alisson Becker has been a formidable goalkeeper for Liverpool FC since joining in 2018 for a then-world record fee of £66.8 million for a goalkeeper, helping the team win the Champions League and Premier League in 2019 and 2020, respectively. \
            He played every minute of the Reds' 2018-2019 domestic campaign, becoming the club's first goalkeeper to win the Premier League Golden Glove award in over a decade. \
            Alisson's crucial late save against Napoli on matchday six helped Liverpool secure a spot in the Champions League knockout stages that season. \
            He scored a stoppage-time winner against West Bromwich Albion in the 2020-21 campaign, securing Champions League qualification for the Reds. \
            Alisson also won the FA Cup and League Cup with Liverpool that season, and earned the Men's Player of the Season award for his excellent form across a difficult 2022-2023 campaign.\
")
            
st.markdown("To demonstrate his immense importance to the team, here is a comparison of Liverpool's defensive statistics with and without Alisson in the Premier League since he joined the club.")

def goalkeeper_fig(y_val, title):
    fig = px.bar(df_alisson, x='Season_End_Year', y=y_val, color='Name', barmode='group')

    # Update layout
    fig.update_layout(
        title=title + ' by Goalkeeper',
        xaxis_title='Season End Year',
        yaxis_title='Count', 
        legend_title="Liverpool Goalkeeper",

        # show every tick
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1
        ),

        annotations=[
            dict(
                x=0.5,
                y=-0.25,
                showarrow=False,
                text="Source: fbref.com | Liverpool FC Goalkeeper Statistics",
                xref="paper",
                yref="paper"
            ),
        ]
    )

    return fig

fig_alisson_ga = goalkeeper_fig('GA90', 'Goals Against Per Game')
fig_alisson_saves = goalkeeper_fig('Save%', 'Save Percentage')
fig_alisson_cs = goalkeeper_fig('CS%', 'Clean Sheet Percentage')
fig_alisson_wins = goalkeeper_fig('W', 'Wins')

tab5, tab6, tab7, tab8 = st.tabs(["Goals Against Per Game", "Save Percentage", "Clean Sheet Percentage", "Wins"])
with tab5:
    st.plotly_chart(fig_alisson_ga, theme="streamlit", use_container_width=True)
with tab6:
    st.plotly_chart(fig_alisson_saves, theme="streamlit", use_container_width=True)
with tab7:
    st.plotly_chart(fig_alisson_cs, theme="streamlit", use_container_width=True)
with tab8:
    st.plotly_chart(fig_alisson_wins, theme="streamlit", use_container_width=True)


st.markdown("These two signings are an example of the many other great players Jürgen Klopp convinced to join Liverpool. \
         The German manager has been a key factor in Liverpool's recent success, and his ability to attract top talent to the club has been a major reason for the Reds' recent dominance. \
")
            
st.markdown("Klopp has also been able to develop players who were already at the club, such as Trent Alexander-Arnold, into world-class players.")


col5, col6 = st.columns(2)

with col5:
    st.markdown("##### Trent Alexander-Arnold")
    st.image('https://backend.liverpoolfc.com/sites/default/files/styles/lg/public/2023-09/pp-23-24-mens-home-body-trent-hair.webp?itok=980rZGFU', caption='Source: liverpoolfc.com | Trent Alexander-Arnold', width=250)

# trent description
st.markdown("Trent Alexander-Arnold is a product of Liverpool's youth academy, and has been a key player for the Reds since making his debut in 2016. \
            He has won the Champions League and Premier League with the club, and has been named in the PFA Team of the Year twice. \
            Alexander-Arnold has also been named in the UEFA Champions League Squad of the Season twice, and was named in the FIFA FIFPro World11 in 2020. \
            He has been a creative force for Liverpool, providing many assists for his teammates. \
            Alexander-Arnold has become a consistent performer for the Reds since his debut at just 18 years old. \
            He has also recently been a leader on the pitch, captaining the team on several occasions. \
            Simply a great development under Jürgen Klopp. \
")
            
# Create subplots
fig_trent = go.Figure()

# Add traces
fig_trent.add_trace(go.Scatter(x=df_trent['Season_End_Year'], y=df_trent['Goals'], mode='lines', name='Goals'))
fig_trent.add_trace(go.Scatter(x=df_trent['Season_End_Year'], y=df_trent['Assists'], mode='lines', name='Assists'))

# Update layout
fig_trent.update_layout(
    title='Trent Alexander-Arnold Statistics',
    xaxis_title='Season End Year',
    yaxis_title='Count',

    # show every tick
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=1
    ),

    annotations=[
        dict(
            x=0.5,
            y=-0.3,
            showarrow=False,
            text="Source: fbref.com | Trent Alexander-Arnold Statistics",
            xref="paper",
            yref="paper"
        ),
    ]
)

# Create subplots
fig_trent_2 = go.Figure()

# Add traces
fig_trent_2.add_trace(go.Scatter(x=df_trent['Season_End_Year'], y=df_trent['MP'], mode='lines', name='Matches Played'))
fig_trent_2.add_trace(go.Scatter(x=df_trent['Season_End_Year'], y=df_trent['Starts'], mode='lines', name='Matches Started'))

# Update layout
fig_trent_2.update_layout(
    title='Trent Alexander-Arnold Statistics',
    xaxis_title='Season End Year',
    yaxis_title='Count', 

    # show every tick
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=1
    ), 

    annotations=[
        dict(
            x=0.5,
            y=-0.25,
            showarrow=False,
            text="Source: fbref.com | Trent Alexander-Arnold Statistics",
            xref="paper",
            yref="paper"
        ),
    ]
)

tab9, tab10 = st.tabs(["Goals & Assists", "Matches Played & Started"])
with tab9:
    st.plotly_chart(fig_trent, theme="streamlit", use_container_width=True)
with tab10:
    st.plotly_chart(fig_trent_2, theme="streamlit", use_container_width=True)


st.markdown("These numbers for a defender are just incredible. \
            Let's compare his statistics to the alltime highest assisting defenders in the Premier League. \
")
            
st.markdown("In the following scatter plot, the size of the bubble represents the number of games played by the player. \
            Trent Alexander-Arnold is represented by the red bubble. \
            As we can see, he is already one of the best attacking defenders in Premier League history, and he still has many games and years infront of him to become the best. \
")

# Trent vs top assist defenders 
df_defenders = pd.read_excel("defender_assists.xlsx")

# Create scatter plot
fig_defenders = go.Figure()

# Add data for each player
for i in range(len(df_defenders["Name"])):
    if df_defenders["Name"][i] == "Trent Alexander-Arnold":
        fig_defenders.add_trace(go.Scatter(x=[df_defenders["Assists"][i]], y=[df_defenders["Goals"][i]], mode='markers', name=df_defenders["Name"][i], 
                                 marker=dict(size=[df_defenders["Games"][i]/10], color='red', sizemode='diameter', opacity=0.6, line=dict(color='Black', width=1)),
                                 text=df_defenders["Name"][i]))
    else:
        fig_defenders.add_trace(go.Scatter(x=[df_defenders["Assists"][i]], y=[df_defenders["Goals"][i]], mode='markers', name=df_defenders["Name"][i],
                                 marker=dict(size=[df_defenders["Games"][i]/10], color='#1f77b4', sizemode='diameter', opacity=0.6, line=dict(color='Black', width=1)),
                                 text=df_defenders["Name"][i]))

# Update layout for better visualization
fig_defenders.update_layout(
    title="Alltime Top 15 Assisting Defenders",
    xaxis_title="Assists",
    yaxis_title="Goals",
    legend_title="Players",
    showlegend=False,

    annotations=[
        dict(
            x=0.85,
            y=0.9,
            text="Ashley Young has played 427 games and is 38 years old",
            xref="paper",
            yref="paper",
            showarrow=True,
            arrowhead=2,
            ax=-50,
            ay=-60
        ),
        dict(
            x=0.5,
            y=-0.3,
            showarrow=False,
            text="Source: premierleague.com | Stats Center",
            xref="paper",
            yref="paper"
        ),
    ]
)

st.plotly_chart(fig_defenders, theme="streamlit", use_container_width=True)

st.markdown("### Financial Prudence")

st.markdown("Another key factor in Liverpool's recent success has been the club's financial prudence. \
            Liverpool's owners, Fenway Sports Group (FSG), have been very careful with the club's finances, and have not spent money recklessly. \
            This has allowed the club to be in a strong financial position, and has allowed the club to spend money on top players when necessary, which we touched on in the previous chapter. \
")   
st.markdown("Let's compare Liverpool's net spend and trophies to that of their rivals in the Premier League.")

df_net_spend = pd.read_excel("net_spend.xlsx")

# Create figure
fig_spend = go.Figure()

# Add bar chart for net spend
fig_spend.add_trace(go.Bar(x=df_net_spend["Club"], y=df_net_spend["Net spend (mil. eur)"], name='Net Spend (mil. eur)', marker_color='#1f77b4'))

# Add line chart for trophies
fig_spend.add_trace(go.Scatter(x=df_net_spend["Club"], y=df_net_spend["Trophies"], mode='lines+markers', name='Trophies', yaxis='y2', line=dict(color='red', width=2)))

# Add bar chart for net spend per trophy
fig_spend.add_trace(go.Bar(x=df_net_spend["Club"], y=df_net_spend["Net spend per trophy (mil. eur)"], name='Net Spend per Trophy (mil. eur)', marker_color='#17becf'))

# Update layout for dual axis
fig_spend.update_layout(
    title="Club's Net Spend & Trophies (2013 - 2023)",
    xaxis_title="Club",
    yaxis_title="Net Spend (mil. eur)",
    yaxis2=dict(title='Trophies', overlaying='y', side='right'),
    barmode='group',

    width=850,

    annotations=[
        dict(
            x=0.5,
            y=-0.3,
            showarrow=False,
            text="Source: planetfootball.com",
            xref="paper",
            yref="paper"
        ),
    ]
)
st.plotly_chart(fig_spend, theme="streamlit")

st.markdown("Considering Liverpool has a much smaller net spend than most of their big rivals, yet are right up there with the amount of trophies won is a testament of the financial prudence and success Jürgen Klopp has brought to the club.")

st.markdown("### Conclusion")

st.markdown("##### The Klopp Effect: Tactical Adaptability and Transformation")

st.markdown("As we have looked at the data, one thing becomes very clear: Jürgen Klopp has been the key to Liverpool FC's transformation. \
            Whether it's the aggressive style of play, improving players, or outsmarting opponents in important matches, Klopp has brought a level of energy that was greatly needed before 2015. \
            His skill as a manager has not only made the team work better together but has also brought back the winning mentality that Liverpool FC is known for. \
")

st.markdown("##### A Tale of Triumph")

st.markdown("In conclusion, the story of Liverpool FC under Jürgen Klopp is a tale of change. \
            This change was brought about through clever strategies, developing players and managing finances wisely.\
            The numbers clearly show that Klopp has not only made Liverpool better, but he has also set new standards for the club. \
            Based on these statistics, it is evident that this is just the start of an exciting and successful era in the club's impressive history.\
")
