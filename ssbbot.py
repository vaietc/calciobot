#HockeyBotS v1.1.0 by /u/TeroTheTerror
#SoccerBotS forked from HockeyBotS
import datetime
import time
import urllib2
import HTMLParser
import praw
import sys
import re
import collections
from bs4 import BeautifulSoup


import ConfigParser
Config = ConfigParser.ConfigParser()
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
	
	print self.subreddit
        self.userAgent = Config.get("userinfo", "userAgent")
        self.fix = 'y'

    def scrape_standings(self):
        #link = 'http://www.whatsthescore.com/football/italy/serie-a/table.html'
        link = 'http://www.livescore.com/soccer/italy/serie-a/'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
	rawdata = []
        for t in soup.findAll('div', { "class" : "ltable table" }):
	    live_table = []
            for table in t.findAll(attrs={'class': re.compile(r"row-gray\b.*")}):
                result = {}
                rawdata.append(table)
                result['team'] = table.findAll('div')[1].text
                result['played'] = table.findAll('div')[2].text
                result['wins'] = table.findAll('div')[3].text
                result['draws'] = table.findAll('div')[4].text
                result['loss'] = table.findAll('div')[5].text
                result['gd'] = table.findAll('div')[8].text
                result['pts'] = table.findAll('div')[9].text
#                print "%s %s %s %s %s %s %s" % (result['team'], result['played'], result['wins'], result['draws'], result['loss'], result['gd'], result['pts'])
                live_table.append(result)


        vlist = []
        vlist1 = []
        vlist2 = []

        w.close()
        data = {}
        data['source'] = link
        data['data'] = live_table
        return data


    def generate_tables(self, data_hash):
        #Compiling the table
        body = "\n|Pos|Team|P|W|D|L|GD|Pts|"
        body += "\n|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|"
        body += "\n|1|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][1]['team'], data_hash['data'][1]['played'], data_hash['data'][1]['wins'], data_hash['data'][1]['draws'], data_hash['data'][1]['loss'], data_hash['data'][1]['gd'], data_hash['data'][1]['pts'])
        body += "\n|2|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][2]['team'], data_hash['data'][2]['played'], data_hash['data'][2]['wins'], data_hash['data'][2]['draws'], data_hash['data'][2]['loss'], data_hash['data'][2]['gd'], data_hash['data'][2]['pts'])
        body += "\n|3|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][3]['team'], data_hash['data'][3]['played'], data_hash['data'][3]['wins'], data_hash['data'][3]['draws'], data_hash['data'][3]['loss'], data_hash['data'][3]['gd'], data_hash['data'][3]['pts'])
        body += "\n|4|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][4]['team'], data_hash['data'][4]['played'], data_hash['data'][4]['wins'], data_hash['data'][4]['draws'], data_hash['data'][4]['loss'], data_hash['data'][4]['gd'], data_hash['data'][4]['pts'])
        body += "\n|5|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][5]['team'], data_hash['data'][5]['played'], data_hash['data'][5]['wins'], data_hash['data'][5]['draws'], data_hash['data'][5]['loss'], data_hash['data'][5]['gd'], data_hash['data'][5]['pts'])
        body += "\n|6|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][6]['team'], data_hash['data'][6]['played'], data_hash['data'][6]['wins'], data_hash['data'][6]['draws'], data_hash['data'][6]['loss'], data_hash['data'][6]['gd'], data_hash['data'][6]['pts'])
        body += "\n|7|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][7]['team'], data_hash['data'][7]['played'], data_hash['data'][7]['wins'], data_hash['data'][7]['draws'], data_hash['data'][7]['loss'], data_hash['data'][7]['gd'], data_hash['data'][7]['pts'])
        body += "\n|8|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][8]['team'], data_hash['data'][8]['played'], data_hash['data'][8]['wins'], data_hash['data'][8]['draws'], data_hash['data'][8]['loss'], data_hash['data'][8]['gd'], data_hash['data'][8]['pts'])
        body += "\n|9|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][9]['team'], data_hash['data'][9]['played'], data_hash['data'][9]['wins'], data_hash['data'][9]['draws'], data_hash['data'][9]['loss'], data_hash['data'][9]['gd'], data_hash['data'][9]['pts'])
        body += "\n|10|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][10]['team'], data_hash['data'][10]['played'], data_hash['data'][10]['wins'], data_hash['data'][10]['draws'], data_hash['data'][10]['loss'], data_hash['data'][10]['gd'], data_hash['data'][10]['pts'])
        body += "\n|11|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][11]['team'], data_hash['data'][11]['played'], data_hash['data'][11]['wins'], data_hash['data'][11]['draws'], data_hash['data'][11]['loss'], data_hash['data'][11]['gd'], data_hash['data'][11]['pts'])
        body += "\n|12|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][12]['team'], data_hash['data'][12]['played'], data_hash['data'][12]['wins'], data_hash['data'][12]['draws'], data_hash['data'][12]['loss'], data_hash['data'][12]['gd'], data_hash['data'][12]['pts'])
        body += "\n|13|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][13]['team'], data_hash['data'][13]['played'], data_hash['data'][13]['wins'], data_hash['data'][13]['draws'], data_hash['data'][13]['loss'], data_hash['data'][13]['gd'], data_hash['data'][13]['pts'])
        body += "\n|14|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][14]['team'], data_hash['data'][14]['played'], data_hash['data'][14]['wins'], data_hash['data'][14]['draws'], data_hash['data'][14]['loss'], data_hash['data'][14]['gd'], data_hash['data'][14]['pts'])
        body += "\n|15|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][15]['team'], data_hash['data'][15]['played'], data_hash['data'][15]['wins'], data_hash['data'][15]['draws'], data_hash['data'][15]['loss'], data_hash['data'][15]['gd'], data_hash['data'][15]['pts'])
        body += "\n|16|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][16]['team'], data_hash['data'][16]['played'], data_hash['data'][16]['wins'], data_hash['data'][16]['draws'], data_hash['data'][16]['loss'], data_hash['data'][16]['gd'], data_hash['data'][16]['pts'])
        body += "\n|17|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][17]['team'], data_hash['data'][17]['played'], data_hash['data'][17]['wins'], data_hash['data'][17]['draws'], data_hash['data'][17]['loss'], data_hash['data'][17]['gd'], data_hash['data'][17]['pts'])
        body += "\n|18|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][18]['team'], data_hash['data'][18]['played'], data_hash['data'][18]['wins'], data_hash['data'][18]['draws'], data_hash['data'][18]['loss'], data_hash['data'][18]['gd'], data_hash['data'][18]['pts'])
        body += "\n|19|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][19]['team'], data_hash['data'][19]['played'], data_hash['data'][19]['wins'], data_hash['data'][19]['draws'], data_hash['data'][19]['loss'], data_hash['data'][19]['gd'], data_hash['data'][19]['pts'])
        body += "\n|20|{0}|{1}|{2}|{3}|{4}|{5}|{6}|".format(data_hash['data'][20]['team'], data_hash['data'][20]['played'], data_hash['data'][20]['wins'], data_hash['data'][20]['draws'], data_hash['data'][20]['loss'], data_hash['data'][20]['gd'], data_hash['data'][20]['pts'])
        body += "\n\n[Source](%s)" % data_hash['source']
        return body

    def fix_standings(self, text):
        #Use dictionary to replace team names with sub names
        team_names = {
          'Juventus': 'Juventus',
          'Sampdoria': 'Sampdoria',
          'Genoa': 'Genoa',
          'Inter Milan': 'Inter',
          'AC Milan': 'AC Milan',
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
          'Roma': 'AS Roma',
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
          'Napoli': '[SSC Napoli](/r/SSCNapoli)',
          'Inter': '[Inter](/r/FCInterMilan)',
          'AS Roma': '[AS Roma](/r/ASRoma)',
          'Parma': '[Parma](/r/parmafc)',
          'Hellas Verona': '[Hellas Verona](/r/HellasVerona)',
          'Chievo Verona': '[Chievo Verona](/r/ChievoVerona)',
          'Genoa': '[Genoa](/r/GenoaCFC)',
          'Torino': '[Torino](/r/IlToro)',
          'Atalanta': '[Atalanta](/r/Atalanta)',
          'Null' : ''}

        if self.fix == 'y':
            for i, j in team_names.iteritems():
                text = text.replace(i, j)
            for i, j in team_subreddits.iteritems():
                text = text.replace(i, j)
            return text
        else:
            return text

    def scrape_top_scorer(self):
        global rawdata
        rawdata = []
        link = 'http://www.soccerstats.com/scorers.asp?league=italy'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
        for table in soup.findAll('table', { "class" : "sortable" }):
            rawdata = table

        vlist = []
        vlist1 = []
        vlist2 = []

        #Make list of cells within a list of rows
        rawdata_list = [tr.findAll('td') for tr in rawdata.findAll('tr')]

        #Text only version of rawdata_list
        for row in rawdata_list:
            vlist.append([cell.text for cell in row])
        #Get rid of problematic characters
        for i in vlist:
            vlist1.append([val.replace(u'\xa0', u' ') for val in i])

        for i in vlist1:
            vlist2.append([val.replace(u'\xe9', u'e') for val in i])

        for i in vlist1:
            vlist2.append([val.replace(u'\xf3', u'o') for val in i])

        w.close()
        data = {}
        data['source'] = link
        data['data'] = vlist2
        return data

    def generate_top_scorer_tables(self, data_hash):
        #Time/Date stamp
        #Compiling the table
        body = "\n|Player|Team|Goals(Penalties)"
        body += "\n|:--|:--|:--:|"
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][1][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][1][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][1][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][1][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][2][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][2][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][2][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][2][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][3][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][3][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][3][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][3][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][4][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][4][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][4][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][4][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][5][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][5][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][5][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][5][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][6][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][6][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][6][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][6][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][7][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][7][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][7][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][7][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][8][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][8][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][8][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][8][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][9][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][9][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][9][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][9][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n|{0}|{1}|{2}({3})".format(data_hash['data'][10][0].encode('utf-8').replace('\n', ' ').replace('\r', ''), data_hash['data'][10][1].replace('\n', ' ').replace('\r', ''), data_hash['data'][10][3].replace('\n', ' ').replace('\r', ''), data_hash['data'][10][4].replace('\n', ' ').replace('\r', '')).decode('utf-8')
        body += "\n\n[Source](%s)" % data_hash['source']
        return body

    def scrape_euro_standings(self):
        link = 'http://www.uefa.com/uefaeuro/season=2016/standings/round=2000446/group=2002435/index.html'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
        #for table in soup.findAll('table', { "class" : "league-wc table mtn" }):
        for table in soup.findAll('table', { "class" : "tb_stand grp_2002435 vis_grtable" }):
            rawdata = table

        vlist = []
        vlist1 = []
        vlist2 = []

        #Make list of cells within a list of rows
        rawdata_list = [tr.findAll('td') for tr in rawdata.findAll('tr')]
        #Text only version of rawdata_list
        for row in rawdata_list:
            vlist.append([cell.text for cell in row])
        #Get rid of problematic characters
        for i in vlist:
            vlist1.append([val.replace(u'\xa0', u' ') for val in i])

        for i in vlist1:
            vlist2.append([val.replace(u'\xe9', u'e') for val in i])

        for i in vlist1:
            vlist2.append([val.replace(u'\xf3', u'o') for val in i])

        w.close()
        data = {}
        data['source'] = link
        data['data'] = vlist2
        return data

    def generate_euro_standings_tables(self, data_hash):
        #Time/Date stamp
        #Compiling the table
        body = "\n|Pos|Team|GP|GD|Pts|"
        body += "\n|:--:|:--|:--:|:--:|:--:|"
        body += "\n|1|%s|%s|%s|%s|" % (data_hash['data'][2][0], data_hash['data'][2][1], data_hash['data'][2][13], data_hash['data'][2][14])
        body += "\n|2|%s|%s|%s|%s|" % (data_hash['data'][3][0], data_hash['data'][3][1], data_hash['data'][3][13], data_hash['data'][3][14])
        body += "\n|3|%s|%s|%s|%s|" % (data_hash['data'][4][0], data_hash['data'][4][1], data_hash['data'][4][13], data_hash['data'][4][14])
        body += "\n|4|%s|%s|%s|%s|" % (data_hash['data'][5][0], data_hash['data'][5][1], data_hash['data'][5][13], data_hash['data'][5][14])
	body += "\n|5|%s|%s|%s|%s|" % (data_hash['data'][6][0], data_hash['data'][6][1], data_hash['data'][6][13], data_hash['data'][6][14])
        body += "\n|6|%s|%s|%s|%s|" % (data_hash['data'][7][0], data_hash['data'][7][1], data_hash['data'][7][13], data_hash['data'][7][14])
        body += "\n\n[Source](%s)" % data_hash['source']
        return body

    def scrape_euro_fixtures(self):
        link = 'http://www.livescore.com/soccer/euro/qualification-group-h/fixtures/all/'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

	rawdata = []
	match_date = []
        matches = []

        for table in soup.findAll(attrs={'class': 'tright fs11'}):
            match_date.append(table)

	counter = collections.Counter()
        for table in soup.findAll(attrs={'class': re.compile(r".*\brow-gray\b.*")}):
	    match = {}
            rawdata.append(table)
            time = table.findAll('div', attrs={ "class" : "min"})
            team_l = table.findAll('div', attrs={ "class" : "ply tright name"})
            team_r = table.findAll('div', attrs={ "class" : "ply name"})
        #    print "%s %s %s" % (time[0].text, team_l[0].text, team_r[0].text)
    	    match['date'] = match_date[0].text
            match['time'] = time[0].text
            match['team_l'] = team_l[0].text
            match['team_r'] = team_r[0].text
        #    print match
            matches.append(match)

        eflst_list = []
        eflst_date_list = []
        eflst_date_list1 = []
        eflst_date_list2 = []
        eflst_list1 = []
        eflst_list2 = []

        #Find the division table
        #Make list of cells within a list of rows

        w.close()
        data = {}
        data['source'] = link
        data['fixtures'] = matches
        return data

    def generate_euro_fixtures_tables(self, data_hash):
        #Time/Date stamp
        #Compiling the table
        body = "\n|%s|" % (str(data_hash['fixtures'][0]['date']))
        body += "\n|:--|"
        body += "\n|%s (UTC) - %s vs. %s |" % (data_hash['fixtures'][0]['time'], data_hash['fixtures'][0]['team_l'], data_hash['fixtures'][0]['team_r'])
        body += "\n|%s (UTC) - %s vs. %s |" % (data_hash['fixtures'][1]['time'], data_hash['fixtures'][1]['team_l'], data_hash['fixtures'][1]['team_r'])
        body += "\n|%s (UTC) - %s vs. %s |" % (data_hash['fixtures'][2]['time'], data_hash['fixtures'][2]['team_l'], data_hash['fixtures'][2]['team_r'])
        body += "\n\n[Source](%s)" % data_hash['source']
        return body

    def create_sidebar(self):
        updated = datetime.datetime.now().strftime('%b %d, %Y at %I:%M%p')
        #To fix character glitch when grabbing the sidebar
        h = HTMLParser.HTMLParser()
        #Initialize PRAW and login
        r = praw.Reddit(user_agent='Soccer_Bot_S/v1.1.0 by ' + Config.get("userinfo", "username"))
        r.login(self.username,self.password)
        #Grab the sidebar template from the wiki
        sidebar = r.get_subreddit(self.subreddit).get_wiki_page('edit_sidebar').content_md
        #Create list from sidebar by splitting at ***
        sidebar_list = sidebar.split('***')
        #Sidebar with updated tables - +lucky_guess+sidebar_list[6]
        sidebar = (sidebar_list[0]+standings_a+sidebar_list[2])
        sidebar += (sidebar_list[3]+fix_goalscorers)
        # sidebar += (sidebar_list[4]+euro_standings_table)
        # sidebar += (sidebar_list[6]+euro_fixtures_table)
        sidebar += (sidebar_list[7]+sidebar_list[8]+sidebar_list[9])
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

print 'Scraping Standings...'
final_list = sb.scrape_standings()
print 'Generating Table...'
standings_b = sb.generate_tables(final_list)
print 'Fixing Table...'
standings_a = sb.fix_standings(standings_b)
print 'Scraping Stats...'
top_scorer_list = sb.scrape_top_scorer()
print 'Generating Top Scorer Table...'
top_scorer_table = sb.generate_top_scorer_tables(top_scorer_list)
print 'Fixing Table...'
fix_goalscorers = sb.fix_standings(top_scorer_table)
# print 'Scraping Euro Stats...'
# euro_standings_list = sb.scrape_euro_standings()
# print 'Generating Euro Standings Table...'
# euro_standings_table = sb.generate_euro_standings_tables(euro_standings_list)
# print 'Scraping Euro Fixtures...'
# euro_fixtures_list = sb.scrape_euro_fixtures()
# print 'Generating Euro Fixtures Table...'
# euro_fixtures_table = sb.generate_euro_fixtures_tables(euro_fixtures_list)
print 'Grabbing Sidebar Template...'
sidebar = sb.create_sidebar()
print 'Updating Sidebar...'
sb.update_reddit()
print 'Sidebar Updated: '+datetime.datetime.now().strftime('%b %d, %Y at %I:%M%p')
