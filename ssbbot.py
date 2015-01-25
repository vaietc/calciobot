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
        link = 'http://www.whatsthescore.com/football/italy/serie-a/table.html'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
        for table in soup.findAll('table', { "class" : "base-listing standing-listing standing-points-live opened with-standing-points-diff" }):
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
	print data
        return data


    def generate_tables(self, data_hash):
        #Compiling the table
        body = "\n|Pos|Team|P|W|D|L|GD|Pts|"
        body += "\n|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|"
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][3][0], data_hash['data'][3][4], data_hash['data'][3][7], data_hash['data'][3][8], data_hash['data'][3][9], data_hash['data'][3][10], data_hash['data'][3][13], data_hash['data'][3][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][4][0], data_hash['data'][4][4], data_hash['data'][4][7], data_hash['data'][4][8], data_hash['data'][4][9], data_hash['data'][4][10], data_hash['data'][4][13], data_hash['data'][4][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][5][0], data_hash['data'][5][4], data_hash['data'][5][7], data_hash['data'][5][8], data_hash['data'][5][9], data_hash['data'][5][10], data_hash['data'][5][13], data_hash['data'][5][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][6][0], data_hash['data'][6][4], data_hash['data'][6][7], data_hash['data'][6][8], data_hash['data'][6][9], data_hash['data'][6][10], data_hash['data'][6][13], data_hash['data'][6][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][7][0], data_hash['data'][7][4], data_hash['data'][7][7], data_hash['data'][7][8], data_hash['data'][7][9], data_hash['data'][7][10], data_hash['data'][7][13], data_hash['data'][7][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][8][0], data_hash['data'][8][4], data_hash['data'][8][7], data_hash['data'][8][8], data_hash['data'][8][9], data_hash['data'][8][10], data_hash['data'][8][13], data_hash['data'][8][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][9][0], data_hash['data'][9][4], data_hash['data'][9][7], data_hash['data'][9][8], data_hash['data'][9][9], data_hash['data'][9][10], data_hash['data'][9][13], data_hash['data'][9][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][10][0], data_hash['data'][10][4], data_hash['data'][10][7], data_hash['data'][10][8], data_hash['data'][10][9], data_hash['data'][10][10], data_hash['data'][10][13], data_hash['data'][10][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][11][0], data_hash['data'][11][4], data_hash['data'][11][7], data_hash['data'][11][8], data_hash['data'][11][9], data_hash['data'][11][10], data_hash['data'][11][13], data_hash['data'][11][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][12][0], data_hash['data'][12][4], data_hash['data'][12][7], data_hash['data'][12][8], data_hash['data'][12][9], data_hash['data'][12][10], data_hash['data'][12][13], data_hash['data'][12][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][13][0], data_hash['data'][13][4], data_hash['data'][13][7], data_hash['data'][13][8], data_hash['data'][13][9], data_hash['data'][13][10], data_hash['data'][13][13], data_hash['data'][13][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][14][0], data_hash['data'][14][4], data_hash['data'][14][7], data_hash['data'][14][8], data_hash['data'][14][9], data_hash['data'][14][10], data_hash['data'][14][13], data_hash['data'][14][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][15][0], data_hash['data'][15][4], data_hash['data'][15][7], data_hash['data'][15][8], data_hash['data'][15][9], data_hash['data'][15][10], data_hash['data'][15][13], data_hash['data'][15][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][16][0], data_hash['data'][16][4], data_hash['data'][16][7], data_hash['data'][16][8], data_hash['data'][16][9], data_hash['data'][16][10], data_hash['data'][16][13], data_hash['data'][16][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][17][0], data_hash['data'][17][4], data_hash['data'][17][7], data_hash['data'][17][8], data_hash['data'][17][9], data_hash['data'][17][10], data_hash['data'][17][13], data_hash['data'][17][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][18][0], data_hash['data'][18][4], data_hash['data'][18][7], data_hash['data'][18][8], data_hash['data'][18][9], data_hash['data'][18][10], data_hash['data'][18][13], data_hash['data'][18][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][19][0], data_hash['data'][19][4], data_hash['data'][19][7], data_hash['data'][19][8], data_hash['data'][19][9], data_hash['data'][19][10], data_hash['data'][19][13], data_hash['data'][19][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][20][0], data_hash['data'][20][4], data_hash['data'][20][7], data_hash['data'][20][8], data_hash['data'][20][9], data_hash['data'][20][10], data_hash['data'][20][13], data_hash['data'][20][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][21][0], data_hash['data'][21][4], data_hash['data'][21][7], data_hash['data'][21][8], data_hash['data'][21][9], data_hash['data'][21][10], data_hash['data'][21][13], data_hash['data'][21][6])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][22][0], data_hash['data'][22][4], data_hash['data'][22][7], data_hash['data'][22][8], data_hash['data'][22][9], data_hash['data'][22][10], data_hash['data'][22][13], data_hash['data'][22][6])

        body += "\n\n[Source](%s)" % data_hash['source']
	print body
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
        link = 'http://www.soccerstats.com/scorers.asp?league=italy'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
        for table in soup.findAll('table', { "id" : "btable" }):
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
        print body
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
        sidebar += (sidebar_list[4]+euro_standings_table)
        sidebar += (sidebar_list[6]+euro_fixtures_table)
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
print 'Scraping Euro Stats...'
euro_standings_list = sb.scrape_euro_standings()
print 'Generating Euro Standings Table...'
euro_standings_table = sb.generate_euro_standings_tables(euro_standings_list)
print 'Scraping Euro Fixtures...'
euro_fixtures_list = sb.scrape_euro_fixtures()
print 'Generating Euro Fixtures Table...'
euro_fixtures_table = sb.generate_euro_fixtures_tables(euro_fixtures_list)
print 'Grabbing Sidebar Template...'
sidebar = sb.create_sidebar()
print 'Updating Sidebar...'
sb.update_reddit()
print 'Sidebar Updated: '+datetime.datetime.now().strftime('%b %d, %Y at %I:%M%p')
