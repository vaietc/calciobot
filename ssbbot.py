#HockeyBotS v1.1.0 by /u/TeroTheTerror
## -- coding: utf-8 --

import requests
import json
import mwparserfromhell
import urllib.parse
import urllib.request
import re
import datetime
import time
from html.parser import HTMLParser
import praw
import sys
import collections
from bs4 import BeautifulSoup

import configparser
Config = configparser.ConfigParser()
Config.read("config.ini")

class Soccer(object):

    def __init__(self):
        #Define divisions in a list
        self.username = Config.get("userinfo", "username")
        self.password = Config.get("userinfo", "password")
        if len(sys.argv) > 1:
            self.subreddit = sys.argv[1]
        else:
            self.subreddit = Config.get("userinfo", "subreddit")
     
        self.userAgent = Config.get("userinfo", "userAgent")
        self.mashapeKey = Config.get("userinfo", "mashapekey")
        self.fix = 'y'



    # Get page from Wikipedia
    def get_page(self, title):
            api_url = "https://en.wikipedia.org/w/api.php"
            data = {"action": "query", "prop": "revisions", "rvlimit": 1,"rvprop": "content", "format": "json", "titles": title}
            response = urllib.request.urlopen(api_url, urllib.parse.urlencode(data).encode()).read()
            jsonresponse = json.loads(response.decode("utf-8") )
            return mwparserfromhell.parse(list(jsonresponse["query"]["pages"].values())[0]["revisions"][0]['*'])
                
    def get_team_link(self,team_name):
            link_title=None
            trim=10
            link = "[%s](%s)"

            teams = {}
            teams.update({'Atalanta':['http://atalanta.it']})
            teams.update({'Bologna':['http://bolognafc.it']})
            teams.update({'Cagliari':['http://cagliaricalcio.net']})
            teams.update({'Catania':['http://ilcalciocatania.it']})
            teams.update({'Chievo':['http://chievoverona.it']})
            teams.update({'Fiorentina':['http://violachannel.tv']})
            teams.update({'Genoa':['http://genoacfc.it/']})
            teams.update({'Internazionale':['/r/FCInterMilan','Inter']})
            teams.update({'Juventus':['/r/juve']})
            teams.update({'Juventus Primavera':['/r/juve']})
            teams.update({'Lazio':['/r/Lazio']})
            teams.update({'Livorno':['http://livornocalcio.it']})
            teams.update({'Milan':['/r/ACMilan']})
            teams.update({'Napoli':['/r/SSCNapoli']})
            teams.update({'Parma':['http://fcparma.com']})
            teams.update({'Roma':['/r/ASRoma']})
            teams.update({'Sampdoria':['http://sampdoria.it']})
            teams.update({'Sassuolo':['http://sassuolocalcio.it']})
            teams.update({'Torino':['http://torinofc.it']})
            teams.update({'Udinese':['/r/Udinese']})
            teams.update({'Hellas Verona':['http://hellasverona.it','Verona']})

            if team_name in teams:
                t = teams.get(team_name)[1] if len(teams.get(team_name)) == 2 else team_name
                t = t[:trim] + "." if len(t) > trim else t
                link = link % (t, teams.get(team_name)[0]) if len(teams.get(team_name)) == 2 else link % (t, teams.get(team_name)[0])
                
                link_title = team_name if len(teams.get(team_name)) == 2 and link_title is None else link_title
            else:
                t = team_name[:trim] + "." if len(team_name) > trim else team_name
                link = link % (t, "##")

            if link_title is not None:
                link = link[:-1] + " '" + link_title + "'" + link[-1:]

            return link

    def parse_table (self, wikitable):
        i = 1
        table_markdown = ""
        for template in wikitable.filter_templates():
            if "Sports table" in template.name:
                if len(table_markdown) > 0:
                    table_markdown += "\n"
                table_markdown +=  "| P | Team | P | W | D | L | GD | Pts |\n"
                table_markdown += "|:-:|:--|:--:|:--:|:--:|:--:|:--:|:--:|\n"

                while template.has("team" + str(i)):
                        team_code = str(template.get("team" + str(i)).value).split()[0].strip()
                        team_name = template.get("name_" + team_code).value.strip_code().strip()
                        team_wins = int(template.get("win_" + team_code).value.split()[0])
                        team_draws = int(template.get("draw_" + team_code).value.split()[0])
                        team_losses = int(template.get("loss_" + team_code).value.split()[0])
                        team_gf = int(template.get("gf_" + team_code).value.split()[0])
                        team_ga = int(re.search(r'\d+', str(template.get("ga_" + team_code).value)).group()) #The RE here is because people keep not putting a space between the Goals Against and any HTML comments.                    team_points = (team_wins * 3) + team_draws
                        team_played = team_wins + team_draws + team_losses
                        team_gd  = team_gf - team_ga
                        team_position = i
                        team_points = (team_wins*3) + team_draws
                        team_result = str(template.get("result"+str(i)).value).split()[0].upper() if template.has("result" + str(i)) else ""
                
                        table_markdown += "| {} | {} | {} | {} | {} | {} | {} | {} |\n".format( team_position, sb.get_team_link(team_name), team_played, team_wins, team_draws, team_losses, team_gd, team_points )
                        
                        i += 1
            i = 1

        return table_markdown
    
    def fix_standings(self, text):
        #Use dictionary to replace team names with sub names
        team_names = {
          'Juventus': 'Juventus',
          'Sampdoria': 'Sampdoria',
          'Genoa': 'Genoa',
          'Inter Milan': 'Inter',
          'AC Milan': 'AC Milan',
          'Milan': 'AC Milan',
          'Udinese': 'Udinese',
          'Hellas Verona': 'Hellas Verona',
          'Fiorentina': 'Fiorentina',
          'Palermo': 'Palermo',
          'Sassuolo': 'Sassuolo',
          'Torino': 'Torino',
          'Cagliari': 'Cagliari',
          'Empoli': 'Empoli',
          'Atalanta': 'Atalanta',
          'ChievoVerona': 'Chievo Verona',
          'Chievo Verona': 'ChievoVerona',
          'Cesena': 'Cesena',
          'Parma': 'Parma',
          'Lazio Roma': 'Lazio',
          'Lazio': 'Lazio',
          'Lazio AS Roma': 'Lazio',
          'Lazio': 'Lazio',
          'SSC Napoli': 'Napoli',
          'SSC Napoli': 'Napoli',
          'Inter': 'Inter',
          'AS Roma': 'Roma',
          'Null' : ''}

        team_subreddits = {
          'Juventus': '[Juventus](/r/Juve)',
          'Sampdoria': '[Sampdoria](/r/Sampdoria)',
          'AC Milan': '[AC Milan](/r/ACMilan)',
          'Udinese': '[Udinese](/r/Udinese)',
          'Fiorentina': '[Fiorentina](/r/Fiorentina)',
          'Palermo': '[Palermo](/r/Palermo)',
          'Cagliari': '[Cagliari](/r/Casteddu)',
          'Lazio': '[Lazio](/r/Lazio)',
          'Napoli': '[Napoli](/r/SSCNapoli)',
          'Inter': '[Inter](/r/FCInterMilan)',
          'Roma': '[Roma](/r/ASRoma)',
          'Parma': '[Parma](/r/parmafc)',
          'Hellas Verona': '[Hellas Verona](/r/HellasVerona)',
          'Chievo Verona': '[Chievo Verona](/r/ChievoVerona)',
          'Genoa': '[Genoa](/r/GenoaCFC)',
          'Torino': '[Torino](/r/IlToro)',
          'Atalanta': '[Atalanta](/r/Atalanta)',
          'Null' : ''}

        if self.fix == 'y':
            for i, j in team_names.items():
                text = text.replace(i, j)
            for i, j in team_subreddits.items():
                text = text.replace(i, j)
            return text
        else:
            return text

    def scrape_top_scorer(self): 
        api = 'https://sportsop-soccer-sports-open-data-v1.p.mashape.com/v1/leagues/serie-a/seasons/16-17/topscorers'
        headers = { 'X-Mashape-Key' : self.mashapeKey, 'Accept' : 'application/json' }
        response = requests.get(api, headers=headers)
        raw_data = response.json()
        data = {}
        data['topscorers'] = []
        data['source'] = 'https://market.mashape.com/sportsop/soccer-sports-open-data'
        if (raw_data['data']['statusCode'] == '200'):
            topscorers = raw_data['data']['topscorers']
            for i in range(0, min(len(topscorers), 10)): # Grab up to 10 top scorers.
                data['topscorers'].append({ 'player' : topscorers[i]['fullname'], 'team': topscorers[i]['team'], 'goals': topscorers[i]['goals'], 'penalties': topscorers[i]['penalties'] })
        else:
            raise RuntimeError("Failed to fetch top scorers from mashape " + str(raw_data))
        return data
 
    def generate_top_scorer_tables(self, data_hash):
        body = "\n|Player|Team|Goals(Penalties)"
        body += "\n|:--|:--|:--|\n"
        for i in range(0, len(data_hash['topscorers'])):
            body += "|" + str(data_hash['topscorers'][i]['player'].replace('\n', ' ').replace('\r', '')) + " | " + str(data_hash['topscorers'][i]['team'].replace('\n', ' ').replace('\r', '')) + " | " + str(data_hash['topscorers'][i]['goals'].replace('\n', ' ').replace('\r', '')) + " ( " + str(data_hash['topscorers'][i]['penalties'].replace('\n', ' ').replace('\r', '')) +  " ) \n"
        body += "\n\n[Source](%s)" % data_hash['source']
        return body
 
    def create_sidebar(self):
        updated = datetime.datetime.now().strftime('%b %d, %Y at %I:%M%p')
        #To fix character glitch when grabbing the sidebar
        h = HTMLParser()
        #Initialize PRAW and login
        r = praw.Reddit(user_agent='Soccer_Bot_S/v1.1.0 by ' + Config.get("userinfo", "username"))
        r.login(self.username,self.password)
        #Grab the sidebar template from the wiki
        sidebar = r.get_subreddit(self.subreddit).get_wiki_page('edit_sidebar').content_md
        #Create list from sidebar by splitting at ***
        sidebar_list = sidebar.split('***')
        #Sidebar with updated tables - +lucky_guess+sidebar_list[6]
        sidebar = (sidebar_list[0]+sidebar_list[1]+str(serie_a_md))
        sidebar += (sidebar_list[2]+sidebar_list[3]+str(serie_b_md))
        sidebar += (sidebar_list[4]+fix_goalscorers)
        #sidebar += (sidebar_list[7]+sidebar_list[8]+sidebar_list[9])
        sidebar += "\nLast Updated: " + updated + "\n\n"
        #Fix characters in sidebar
        sidebar = h.unescape(sidebar)
        return sidebar

    def update_reddit(self):
        #Initialize PRAW and login
        r = praw.Reddit(user_agent='Soccer_Bot_S/v1.1.0 by ' + Config.get("userinfo", "username"))
        r.login(self.username,self.password)
        #Grab the current settings
        settings = r.get_subreddit(self.subreddit).get_settings()
        #Update the sidebar
        settings['description'] = sidebar
        settings = r.get_subreddit(self.subreddit).update_settings(description=settings['description'])

sb = Soccer()

print('Scraping Standings for Serie A...')
serie_a_table = sb.get_page('Template:2016–17_Serie_A_table')
print('Scraping Standings for Serie B...')
serie_b_table = sb.get_page('2016–17_Serie_B')
print('Generating Table...')
serie_a_md = sb.parse_table (serie_a_table)
serie_b_md = sb.parse_table (serie_b_table)
print('Fixing Table...')
print('Scraping Goalscorer Stats...')
top_scorer_list = sb.scrape_top_scorer()
print('Generating Top Scorer Table...')
top_scorer_table = sb.generate_top_scorer_tables(top_scorer_list)
print('Fixing Table...')
fix_goalscorers = sb.fix_standings(top_scorer_table)
print(fix_goalscorers)
print('Grabbing Sidebar Template...')
sidebar = sb.create_sidebar()
print('Updating Sidebar...')
sb.update_reddit()
print('Sidebar Updated: '+datetime.datetime.now().strftime('%b %d, %Y at %I:%M%p'))
