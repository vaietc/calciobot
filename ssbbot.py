#HockeyBotS v1.1.0 by /u/TeroTheTerror
#SoccerBotS forked from HockeyBotS
import datetime
import time
import urllib2
import HTMLParser
import praw
import sys
from bs4 import BeautifulSoup


import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

class Soccer(object):

    def __init__(self):
        #Define divisions in a list
        divisions = ['Atlantic', 'Metropolitan', 'Central', 'Pacific']
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
        link = 'http://www.livescore.com/soccer/italy/serie-a/'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
        for table in soup.findAll('table', { "class" : "league-wc table mtn" }):
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


    def generate_tables(self, data_hash):
        #Compiling the table
        body = "\n|Pos|Team|P|W|D|L|GD|Pts|"
        body += "\n|:--:|:--|:--:|:--:|:--:|:--:|:--:|:--:|"
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][1][1], data_hash['data'][1][2], data_hash['data'][1][3], data_hash['data'][1][4], data_hash['data'][1][5], data_hash['data'][1][6], data_hash['data'][1][9], data_hash['data'][1][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][2][1], data_hash['data'][2][2], data_hash['data'][2][3], data_hash['data'][2][4], data_hash['data'][2][5], data_hash['data'][2][6], data_hash['data'][2][9], data_hash['data'][2][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][3][1], data_hash['data'][3][2], data_hash['data'][3][3], data_hash['data'][3][4], data_hash['data'][3][5], data_hash['data'][3][6], data_hash['data'][3][9], data_hash['data'][3][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][4][1], data_hash['data'][4][2], data_hash['data'][4][3], data_hash['data'][4][4], data_hash['data'][4][5], data_hash['data'][4][6], data_hash['data'][4][9], data_hash['data'][4][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][5][1], data_hash['data'][5][2], data_hash['data'][5][3], data_hash['data'][5][4], data_hash['data'][5][5], data_hash['data'][5][6], data_hash['data'][5][9], data_hash['data'][5][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][6][1], data_hash['data'][6][2], data_hash['data'][6][3], data_hash['data'][6][4], data_hash['data'][6][5], data_hash['data'][6][6], data_hash['data'][6][9], data_hash['data'][6][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][7][1], data_hash['data'][7][2], data_hash['data'][7][3], data_hash['data'][7][4], data_hash['data'][7][5], data_hash['data'][7][6], data_hash['data'][7][9], data_hash['data'][7][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][8][1], data_hash['data'][8][2], data_hash['data'][8][3], data_hash['data'][8][4], data_hash['data'][8][5], data_hash['data'][8][6], data_hash['data'][8][9], data_hash['data'][8][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][9][1], data_hash['data'][9][2], data_hash['data'][9][3], data_hash['data'][9][4], data_hash['data'][9][5], data_hash['data'][9][6], data_hash['data'][9][9], data_hash['data'][9][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][10][1], data_hash['data'][10][2], data_hash['data'][10][3], data_hash['data'][10][4], data_hash['data'][10][5], data_hash['data'][10][6], data_hash['data'][10][9], data_hash['data'][10][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][11][1], data_hash['data'][11][2], data_hash['data'][11][3], data_hash['data'][11][4], data_hash['data'][11][5], data_hash['data'][11][6], data_hash['data'][11][9], data_hash['data'][11][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][12][1], data_hash['data'][12][2], data_hash['data'][12][3], data_hash['data'][12][4], data_hash['data'][12][5], data_hash['data'][12][6], data_hash['data'][12][9], data_hash['data'][12][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][13][1], data_hash['data'][13][2], data_hash['data'][13][3], data_hash['data'][13][4], data_hash['data'][13][5], data_hash['data'][13][6], data_hash['data'][13][9], data_hash['data'][13][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][14][1], data_hash['data'][14][2], data_hash['data'][14][3], data_hash['data'][14][4], data_hash['data'][14][5], data_hash['data'][14][6], data_hash['data'][14][9], data_hash['data'][14][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][15][1], data_hash['data'][15][2], data_hash['data'][15][3], data_hash['data'][15][4], data_hash['data'][15][5], data_hash['data'][15][6], data_hash['data'][15][9], data_hash['data'][15][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][16][1], data_hash['data'][16][2], data_hash['data'][16][3], data_hash['data'][16][4], data_hash['data'][16][5], data_hash['data'][16][6], data_hash['data'][16][9], data_hash['data'][16][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][17][1], data_hash['data'][17][2], data_hash['data'][17][3], data_hash['data'][17][4], data_hash['data'][17][5], data_hash['data'][17][6], data_hash['data'][17][9], data_hash['data'][17][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][18][1], data_hash['data'][18][2], data_hash['data'][18][3], data_hash['data'][18][4], data_hash['data'][18][5], data_hash['data'][18][6], data_hash['data'][18][9], data_hash['data'][18][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][19][1], data_hash['data'][19][2], data_hash['data'][19][3], data_hash['data'][19][4], data_hash['data'][19][5], data_hash['data'][19][6], data_hash['data'][19][9], data_hash['data'][19][10])
        body += "\n|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(data_hash['data'][20][1], data_hash['data'][20][2], data_hash['data'][20][3], data_hash['data'][20][4], data_hash['data'][20][5], data_hash['data'][20][6], data_hash['data'][20][9], data_hash['data'][20][10])
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
        link = 'http://www.livescore.com/soccer/euro/qualification-group-h/'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        #Find the division table
        for table in soup.findAll('table', { "class" : "league-wc table mtn" }):
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
        body += "\n|%s|%s|%s|%s|%s|" % (data_hash['data'][1][1], data_hash['data'][1][2], data_hash['data'][1][3], data_hash['data'][1][9], data_hash['data'][1][10])
        body += "\n|%s|%s|%s|%s|%s|" % (data_hash['data'][2][1], data_hash['data'][2][2], data_hash['data'][2][3], data_hash['data'][2][9], data_hash['data'][2][10])
        body += "\n|%s|%s|%s|%s|%s|" % (data_hash['data'][3][1], data_hash['data'][3][2], data_hash['data'][3][3], data_hash['data'][3][9], data_hash['data'][3][10])
        body += "\n|%s|%s|%s|%s|%s|" % (data_hash['data'][4][1], data_hash['data'][4][2], data_hash['data'][4][3], data_hash['data'][4][9], data_hash['data'][4][10])
        body += "\n|%s|%s|%s|%s|%s|" % (data_hash['data'][5][1], data_hash['data'][5][2], data_hash['data'][5][3], data_hash['data'][5][9], data_hash['data'][5][10])
        body += "\n|%s|%s|%s|%s|%s|" % (data_hash['data'][6][1], data_hash['data'][6][2], data_hash['data'][6][3], data_hash['data'][6][9], data_hash['data'][6][10])
        body += "\n\n[Source](%s)" % data_hash['source']
        return body

    def scrape_euro_fixtures(self):
        link = 'http://www.livescore.com/soccer/euro/qualification-group-h/fixtures/all/'
        w = urllib2.urlopen(link)
        soup = BeautifulSoup(w.read())

        for table in soup.findAll('table', { "class" : "league-table mtn" }):
            rawdata = table

        eflst_list = []
        eflst_date_list = []
        eflst_date_list1 = []
        eflst_date_list2 = []
        eflst_list1 = []
        eflst_list2 = []

        #Find the division table
        #Make list of cells within a list of rows
        rawdata_list = [tr.findAll('td') for tr in rawdata.findAll('tr')]
        datedata_list = [tr.findAll('span') for tr in rawdata.findAll('tr')]

        #Text only version of rawdata_list
        for row1 in rawdata_list:
            eflst_list.append([cell.text for cell in row1])
        for row2 in datedata_list:
            eflst_date_list.append([cell.text for cell in row2])
        #Get rid of problematic characters
        for edflst in eflst_date_list:
            eflst_date_list1.append([val.replace(u'\xa0', u' ') for val in edflst])

        for edflst in eflst_date_list1:
            eflst_date_list2.append([val.replace(u'\xa0', u' ') for val in edflst])

        for edflst in eflst_date_list1:
            eflst_date_list2.append([val.replace(u'\xf3', u'o') for val in edflst])

        for eflst in eflst_list:
            eflst_list1.append([val.replace(u'\xa0', u' ') for val in eflst])

        for eflst in eflst_list1:
            eflst_list2.append([val.replace(u'\xe9', u'e') for val in eflst])

        for eflst in eflst_list1:
            eflst_list2.append([val.replace(u'\xf3', u'o') for val in eflst])

        w.close()
        data = {}
        data['source'] = link
        data['dates'] = eflst_date_list2
        data['fixtures'] = eflst_list2
        return data

    def generate_euro_fixtures_tables(self, data_hash):
        #Time/Date stamp
        #Compiling the table
        body = "\n|%s|" % (str(data_hash['dates'][0][0]))
        body += "\n|:--|"
        body += "\n|%s - %s vs. %s |" % (data_hash['fixtures'][1][0], data_hash['fixtures'][1][1], data_hash['fixtures'][1][3])
        body += "\n|%s - %s vs. %s |" % (data_hash['fixtures'][2][0], data_hash['fixtures'][2][1], data_hash['fixtures'][2][3])
        body += "\n|%s - %s vs. %s |" % (data_hash['fixtures'][3][0], data_hash['fixtures'][3][1], data_hash['fixtures'][3][3])
        body += "\n\n[Source](%s)" % data_hash['source']
        return body

    def create_sidebar(self):
        updated = datetime.datetime.now().strftime('%b %d, %Y at %I:%M%p')
        #To fix character glitch when grabbing the sidebar
        h = HTMLParser.HTMLParser()
        #Initialize PRAW and login
        r = praw.Reddit(user_agent='Soccer_Bot_S/v1.1.0 by ubercl0ud')
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
        r = praw.Reddit(user_agent='Soccer_Bot_S/v1.1.0 by ubercl0ud')
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
