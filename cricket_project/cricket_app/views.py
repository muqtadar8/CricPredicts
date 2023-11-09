
# Create your views here.
from django import forms
from .forms import OneOnOneForm
from bs4 import BeautifulSoup
from django.shortcuts import render 
form = OneOnOneForm()
import pandas as pd
import requests
import plotly.express as px

def home(request):
    return render(request, 'index.html')


# https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;innings_number=1;innings_number=2;opposition=1;orderby=start;team=6;template=results;trophy=12;type=team;view=innings


#Creating a function to see the stats when two teams have played(historical data)
def one_stats(t,o):
  data = {1: 'England',
    2: 'Australia',
    3: 'South Africa',
    4: 'West Indies',
    5: 'New Zealand',
    6: 'India',
    7: 'Pakistan',
    8: 'Sri Lanka',
    9: 'Zimbabwe',
    11: 'United States of America',
    12: 'Bermuda',
    14: 'East Africa',
    15: 'Netherlands',
    17: 'Canada',
    19: 'Hong Kong',
    20: 'Papua New Guinea',
    25: 'Bangladesh',
    26: 'Kenya',
    27: 'United Arab Emirates',
    28: 'Namibia',
    29: 'Ireland',
    30: 'Scotland',
    32: 'Nepal'}
  # print(data)
  dfs = []
  # t =int( input("enter a team id "))

  # o =int( input("enter a oponent team id "))

  if t == o :
    print("haula hai tu")
    return 
  elif (t not in data.keys() ) or (o not in data.keys()):
    print("marja")

  # Loop through the 'id' values from 0 to 19
  # for id in range(1, 35):
  url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;innings_number=1;innings_number=2;opposition={o};orderby=start;team={t};template=results;trophy=12;type=team;view=innings"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")

  # Find the Primary team and Opposition team information
  opposition_team = soup.find("b", string="Opposition team")
  # print(opposition_team,"message")

  if opposition_team:
      ptn = opposition_team.next_sibling.strip()
  else :
    print("no ptn")
  # print("ptn")

  # Read the HTML tables from the URL
  team_vs_team = pd.read_html(url)


  # Assuming you want to use the third table (team_vs_team[2]) from each URL
  # if len(team_vs_team) > 2:
  data = team_vs_team[2]
  # dfs.append(data)

  df1 = pd.DataFrame({'opposition': [ptn]})
  # print(df1)
  df1.columns = ["opposition"]

  # result_df = pd.concat([df1, data], axis = 1, ignore_index=False)
  data = data.drop(["Unnamed: 6"],axis = 1 )
  data = data.iloc[:,:-1]

  result_counts = data['Result'].value_counts()
  fig = px.pie(result_counts, values=result_counts, names=result_counts.index)
  fig1 = px.bar(data, x='Start Date', y='Score', color='Result')

  data = data.to_html(classes='table table-striped')

#   result_counts = ['Result'].value_counts()
#   fig = px.pie(result_counts, values=result_counts, names=result_counts.index, title='India Vs Australia Match Results')

    # Convert the Plotly figure to an HTML div
  div = fig.to_html(full_html=False)
  div1 = fig1.to_html(full_html=False)

  return data , div ,div1






def oneonone(request):
    result = None
    result1 = None
    a = None
    b = None
    plot_div = None
    plot_div1 = None
    teams = {1: 'England',
    2: 'Australia',
    3: 'South Africa',
    4: 'West Indies',
    5: 'New Zealand',
    6: 'India',
    7: 'Pakistan',
    8: 'Sri Lanka',
    9: 'Zimbabwe',
    11: 'United States of America',
    12: 'Bermuda',
    14: 'East Africa',
    15: 'Netherlands',
    17: 'Canada',
    19: 'Hong Kong',
    20: 'Papua New Guinea',
    25: 'Bangladesh',
    26: 'Kenya',
    27: 'United Arab Emirates',
    28: 'Namibia',
    29: 'Ireland',
    30: 'Scotland',
    32: 'Nepal'}
    
    team_range = [1,2,3,4,5,6,7,8,9,11,12,14,15,17,19,20,25,26,27,28,29,30,32]

    if request.method == 'POST':
        team_id = int(request.POST.get('team'))
        opponent_id = int(request.POST.get('opponent'))

#         for i in team_range :
#   # print(i.values())
#             if (teams[i] == team_id):
#                 team_id = i
#             elif (teams[i] == opponent_id):
#                 opponent_id = i



        # Implement your one-on-one function here
        if team_id == opponent_id:
            result = "Haula hai tu."
        else:
            result = "No compromise, only fight"

        url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;opposition={opponent_id};team={team_id};orderby=runs;template=results;trophy=12;type=team"
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        # Find the Primary team and Opposition team information
        opposition_team = soup.find("b", string="Opposition team")

        if opposition_team:
            ptn = opposition_team.next_sibling.strip()
        else :
            print("no ptn")

        # print("ptn")
        a = teams[team_id]
        b = teams[opponent_id]
        # Read the HTML tables from the URL
        team_vs_team = pd.read_html(url)


        # Assuming you want to use the third table (team_vs_team[2]) from each URL
        data = team_vs_team[2]
        df1 = pd.DataFrame({'Opposition': [ptn]})
        df1.columns = ["Opposition"]
        # print(df1)
        data = data.iloc[:,:-1]
        result = pd.concat([data, df1], axis = 1, ignore_index=False)
        
        result = result.to_html(classes='table table-striped')
        result1,plot_div,plot_div1= one_stats(team_id,opponent_id)
    return render(request, 'oneonone.html', {'form': form, 'result': result,'result1':result1,'a':a,'b':b,'plot_div': plot_div,'plot_div1': plot_div1 })

def oneone(team_id,opponent_id):
    result = None

    teams = {1: 'England',
        2: 'Australia',
        3: 'South Africa',
        4: 'West Indies',
        5: 'New Zealand',
        6: 'India',
        7: 'Pakistan',
        8: 'Sri Lanka',
        9: 'Zimbabwe',
        11: 'United States of America',
        12: 'Bermuda',
        14: 'East Africa',
        15: 'Netherlands',
        17: 'Canada',
        19: 'Hong Kong',
        20: 'Papua New Guinea',
        25: 'Bangladesh',
        26: 'Kenya',
        27: 'United Arab Emirates',
        28: 'Namibia',
        29: 'Ireland',
        30: 'Scotland',
        32: 'Nepal'}
    
    if team_id == opponent_id:
        result = "Haula hai tu."
    else:
        result = "No compromise, only fight"

    url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;opposition={opponent_id};team={team_id};orderby=runs;template=results;trophy=12;type=team"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # Find the Primary team and Opposition team information
    opposition_team = soup.find("b", string="Opposition team")

    if opposition_team:
        ptn = opposition_team.next_sibling.strip()
    else :
        print("no ptn")
    # print("ptn")
    
    # Read the HTML tables from the URL
    team_vs_team = pd.read_html(url)


    # Assuming you want to use the third table (team_vs_team[2]) from each URL
    data = team_vs_team[2]
    df1 = pd.DataFrame({'Opposition': [ptn]})
    df1.columns = ["Opposition"]
    # print(df1)
    data = data.iloc[:,:-1]
    result = pd.concat([data, df1], axis = 1, ignore_index=False)
    
    # result = result.to_html(classes='table table-striped')

    return result


def onevsall(request):
    id = None
    a = None
    if request.method == 'POST':
            id = int(request.POST.get('team'))
    
    teams = {1: 'England',
        2: 'Australia',
        3: 'South Africa',
        4: 'West Indies',
        5: 'New Zealand',
        6: 'India',
        7: 'Pakistan',
        8: 'Sri Lanka',
        9: 'Zimbabwe',
        11: 'United States of America',
        12: 'Bermuda',
        14: 'East Africa',
        15: 'Netherlands',
        17: 'Canada',
        19: 'Hong Kong',
        20: 'Papua New Guinea',
        25: 'Bangladesh',
        26: 'Kenya',
        27: 'United Arab Emirates',
        28: 'Namibia',
        29: 'Ireland',
        30: 'Scotland',
        32: 'Nepal'
        }
    # a = teams[id]
    result = pd.DataFrame()

    for i in teams.keys():
        if i == id :
            continue
        else :
            x = oneone(id,i)
            result = pd.concat([result, x], ignore_index=False)
            
    result = result.to_html(classes='table table-striped')

    return render(request,'onevsall.html',{'form': form, 'result': result})

