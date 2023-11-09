from django import forms
from .forms import OneOnOneForm
from bs4 import BeautifulSoup
from django.shortcuts import render 
form = OneOnOneForm()
import pandas as pd
import requests


def batsq(t):
  # t = int(input("team A : "))

  url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=runs;season=2023%2F24;team={t};template=results;trophy=12;type=batting"

  sq = pd.read_html(url)
  df = sq[2]
  df = df.iloc[:, :-1]
#   df = df.replace('-', 0)
#   df['HS'] = df['HS'].str.replace('*', '', regex=False)
#   df = df.dropna()
  return df

def ballsq(t):
  # t = int(input("team A : "))
  url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=runs;season=2023%2F24;team={t};template=results;trophy=12;type=bowling"

  sq = pd.read_html(url)
  df = sq[2]
  df = df.iloc[:, :-1]
#   df = df.replace('-', 0)
#   df = df.dropna()

#   y = df["BBI"]

#   hw = []
#   lr = []

#   for i in y :
#     if i == 0:
#       continue
#     else:
#       x = i.split('/')
#       w = x[0]
#       r = x[1]
#       hw.append(w)
#       lr.append(r)

#   df = df[df['BBI'] != 0]
#   df['hw'] = hw
#   df['lr'] = lr

  return df

# Create your views here.
def getsquad(request):
  team_id = None
  result = None
  if request.method == 'POST':
        team_id = int(request.POST.get('team'))

  urlsq = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=runs;season=2023%2F24;team={team_id};template=results;trophy=12;type=allround"

  sq = pd.read_html(urlsq)
  df = sq[2]
  result = df.iloc[:, :-1]
  result = result.to_html(classes='table table-striped')

  bat = batsq(team_id)
  bat = bat.to_html(classes='table table-striped')

  ball = ballsq(team_id)
  ball = ball.to_html(classes='table table-striped')

  return render(request,'squad.html', {'form': form, 'result': result, 'bat':bat,'ball':ball})

