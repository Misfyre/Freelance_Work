__author__ = 'Nick Sarris (ngs5st)'

import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_data(year):

    final_data = []
    sessions = requests.session()
    url = 'http://stats.hockeyanalysis.com/ratings.php?db=' + year + \
          '&sit=5v5&type=individual&teamid=0&pos=skaters' \
          '&minutes=50&disp=1&sort=PCT&sortdir=DESC'
    response = sessions.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find_all('tr')[3:]

    for index in table:
        data = list(index)[3:]

        try:
            name = str(data[0]).replace('<td>','')
            name = str(name).replace('</a></td>','')
            name = str(name).split('>')[1]

            team = str(data[2]).replace('<td>','')
            team = str(team).replace('</td>','')
            gp = str(data[4]).replace('<td><center>','')
            gp = str(gp).replace('</center></td>','')
            gp = str(gp).replace(' ','')
            toi = str(data[6]).replace('<td><center>','')
            toi = str(toi).replace('</center></td>','')
            toi = str(toi).replace(' ','')

            g = str(data[8]).replace('<td><center>','')
            g = str(g).replace('</center></td>','')
            g = str(g).replace(' ','')
            a = str(data[10]).replace('<td><center>','')
            a = str(a).replace('</center></td>','')
            a = str(a).replace(' ','')

            firsta = str(data[12]).replace('<td><center>','')
            firsta = str(firsta).replace('</center></td>','')
            firsta = str(firsta).replace(' ','')
            points = str(data[14]).replace('<td><center>','')
            points = str(points).replace('</center></td>','')
            points = str(points).replace(' ','')
            shots = str(data[16]).replace('<td><center>','')
            shots = str(shots).replace('</center></td>','')
            shots = str(shots).replace(' ','')

            ifenwick = str(data[18]).replace('<td><center>','')
            ifenwick = str(ifenwick).replace('</center></td>','')
            ifenwick = str(ifenwick).replace(' ','')
            icorsi = str(data[20]).replace('<td><center>','')
            icorsi = str(icorsi).replace('</center></td>','')
            icorsi = str(icorsi).replace(' ','')
            shpct = str(data[22]).replace('<td><center>','')
            shpct = str(shpct).replace('</center></td>','')
            shpct = str(shpct).replace(' ','')

            g_60 = str(data[24]).replace('<td><center>','')
            g_60 = str(g_60).replace('</center></td>','')
            g_60 = str(g_60).replace(' ','')
            a_60 = str(data[26]).replace('<td><center>','')
            a_60 = str(a_60).replace('</center></td>','')
            a_60 = str(a_60).replace(' ','')

            firsta_60 = str(data[28]).replace('<td><center>','')
            firsta_60 = str(firsta_60).replace('</center></td>','')
            firsta_60 = str(firsta_60).replace(' ','')
            points_60 = str(data[30]).replace('<td><strong><center>','')
            points_60 = str(points_60).replace('</center></strong></td>','')
            points_60 = str(points_60).replace(' ','')
            shots_60 = str(data[32]).replace('<td><center>','')
            shots_60 = str(shots_60).replace('</center></td>','')
            shots_60 = str(shots_60).replace(' ','')

            ifenwick_60 = str(data[34]).replace('<td><center>','')
            ifenwick_60 = str(ifenwick_60).replace('</center></td>','')
            ifenwick_60 = str(ifenwick_60).replace(' ','')
            icorsi_60 = str(data[36]).replace('<td><center>','')
            icorsi_60 = str(icorsi_60).replace('</center></td>','')
            icorsi_60 = str(icorsi_60).replace(' ','')

            igp = str(data[38]).replace('<td><center>','')
            igp = str(igp).replace('</center></td>','')
            igp = str(igp).replace(' ','')
            iap = str(data[40]).replace('<td><center>','')
            iap = str(iap).replace('</center></td>','')
            iap = str(iap).replace(' ','')
            ipp = str(data[42]).replace('<td><center>','')
            ipp = str(ipp).replace('</center></td>','')
            ipp = str(ipp).replace(' ','')

            player_data = [name, team, gp, toi, g, a, firsta, points, shots,
                           ifenwick, icorsi, shpct, g_60, a_60, firsta_60, points_60,
                           shots_60, ifenwick_60, icorsi_60, igp, iap, ipp]

            #print('Scraping Data: {} | {} | {} | {} | {} | {} | {} | {} | {} |'
            #                    ' {} | {} | {} | {} | {} | {} | {} | {} | {} |'
            #                    ' {} | {} | {} | {}'.format(
            #    name, team, gp, toi, g, a, firsta, points, shots,
            #    ifenwick, icorsi, shpct, g_60, a_60, firsta_60, points_60,
            #    shots_60, ifenwick_60, icorsi_60, igp, iap, ipp))

            list.append(final_data, player_data)

        except:
            continue

    columns = ['name','team','gp','toi','g','a','firsta','points','shots',
               'ifenwick','icorsi','shpct','g_60','a_60','firsta_60','points_60',
               'shots_60','ifenwick_60','icorsi_60','igp','iap','ipp']

    player_df = pd.DataFrame(final_data, columns=columns)
    player_df.to_csv('player_data_{}.csv'.format(year), index=False)

def main():

    year_list = ['201617','201516','201415','201314','201213',
                 '201112','201011','200910','200809','200708',
                 '201517','201416','201315','201214','201113',
                 '201012','200911','200810','200709','201417',
                 '201316','201215','201114','201013','200912',
                 '200811','200710','201317','201216','201115',
                 '201014','200913','200812','200711','201116',
                 '201015','200914','200813','200712','201016',
                 '200915','200814','200713','200916','200815',
                 '200714','200816','200715','200716']

    manual_input = input("Which Year Do You Want to Scrape? (Enter 'All' for All of Them): ")

    if manual_input == 'All':
        print('')
        for year in year_list:
            print('Scraping Year: {}'.format(year))
            scrape_data(year)
    else:
        scrape_data(manual_input)


if __name__ == '__main__':
    main()