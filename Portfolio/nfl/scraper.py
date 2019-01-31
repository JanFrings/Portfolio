import requests
from bs4 import BeautifulSoup

def scraper(player_name):
        # This part is creating a requests that looks like a browser and not like a request.get object but we need to
        # put a uptodate header within the currly brackets
        # session = requests.Session()
        # session.headers = {}

        first_name = (player_name.split())[0]
        last_name = (player_name.split())[1]

        last_name_first_letter = last_name[0]
        last_name_first_four = last_name[0:4]
        first_name_first_two = first_name[0:2]

        # grabs the players webpage with the whole site content
        page = requests.get('https://www.pro-football-reference.com/players/{}/{}{}00.htm'.format(last_name_first_letter,
                                                                                                    last_name_first_four,
                                                                                                    first_name_first_two,))
        # with the .content call we get out a <!DOCTYPE>. file                                                                                            first_name_first_two))
        content = page.content
        # the bs4's html.parser extracts the data
        soup = BeautifulSoup(content, 'html.parser')

        # finds within the html the right table for the choosen week
        week_number = 251
        stats = soup.find("tr", {"id": "stats.{}".format(week_number)})

        stats_relevant = ['pass_yds', 'pass_td', 'rush_yds']
        stat_list = []

        # The following function works as shown:
        #1: stats_pass_yds = stats.find("td", {"data-stat": "{}".format('pass_yds')})
        # grabs the pass_yds table with its information
        #2: pass_yds = list(stats_pass_yds.children)[0]
        # .children is a list generator so we call list() to actually generate a list
        #  and we grab the 0'th element to get the string out of the list
        #3. stat_list = [  int(pass_yds),]
        # to get an integer we collect the data in a list with the int() call

        for stat in stats_relevant:
            stat_list.append(int(list(stats.find("td", {"data-stat": "{}".format(stat)}).children)[0]))

        print(stat_list)
        # x = Player(passing_yards = stat_list[0])
        # x.save()
scraper('Drew Brees')
