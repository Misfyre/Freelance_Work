__author__ = 'Nick Sarris (ngs5st)'

import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_individual(year, situation):

    final_data = []
    sessions = requests.session()
    url = 'http://stats.hockeyanalysis.com/ratings.php?db=' + year + \
          '&sit=' + situation + '&type=individual&teamid=0&pos=skaters' \
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

            list.append(final_data, player_data)

        except:
            continue

    columns = ['name','team','gp','toi','g','a','firsta','points','shots',
               'ifenwick','icorsi','shpct','g_60','a_60','firsta_60','points_60',
               'shots_60','ifenwick_60','icorsi_60','igp','iap','ipp']

    player_df = pd.DataFrame(final_data, columns=columns)
    player_df.to_csv('player_data_{}_{}_{}.csv'.format(year, situation, 'individual'), index=False)

def scrape_on_ice(year, situation, type):

    final_data = []
    sessions = requests.session()
    url = 'http://stats.hockeyanalysis.com/ratings.php?db=' + year + \
          '&sit=' + situation + '&type=' + type + '&teamid=0&pos=skaters' \
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
            gf_60 = str(data[8]).replace('<td><center>','')
            gf_60 = str(gf_60).replace('</center></td>','')
            gf_60 = str(gf_60).replace(' ','')
            ga_60 = str(data[10]).replace('<td><center>','')
            ga_60 = str(ga_60).replace('</center></td>','')
            ga_60 = str(ga_60).replace(' ','')
            gf_percent = str(data[12]).replace('<td><strong><center>','')
            gf_percent = str(gf_percent).replace('</center></strong></td>','')
            gf_percent = str(gf_percent).replace(' ','')
            sh_percent = str(data[14]).replace('<td><center>','')
            sh_percent = str(sh_percent).replace('</center></td>','')
            sh_percent = str(sh_percent).replace(' ','')
            sv_percent = str(data[16]).replace('<td><center>','')
            sv_percent = str(sv_percent).replace('</center></td>','')
            sv_percent = str(sv_percent).replace(' ','')
            pdo = str(data[18]).replace('<td><center>','')
            pdo = str(pdo).replace('</center></td>','')
            pdo = str(pdo).replace(' ','')
            tmgf_60 = str(data[20]).replace('<td><center>','')
            tmgf_60 = str(tmgf_60).replace('</center></td>','')
            tmgf_60 = str(tmgf_60).replace(' ','')
            tmga_60 = str(data[22]).replace('<td><center>','')
            tmga_60 = str(tmga_60).replace('</center></td>','')
            tmga_60 = str(tmga_60).replace(' ','')
            tmgf_percent = str(data[24]).replace('<td><center>','')
            tmgf_percent = str(tmgf_percent).replace('</center></td>','')
            tmgf_percent = str(tmgf_percent).replace(' ','')
            gf_60_reltm = str(data[26]).replace('<td><center>','')
            gf_60_reltm = str(gf_60_reltm).replace('</center></td>','')
            gf_60_reltm = str(gf_60_reltm).replace(' ','')
            ga_60_reltm = str(data[28]).replace('<td><center>','')
            ga_60_reltm = str(ga_60_reltm).replace('</center></td>','')
            ga_60_reltm = str(ga_60_reltm).replace(' ','')
            gf_percent_reltm = str(data[30]).replace('<td><center>','')
            gf_percent_reltm = str(gf_percent_reltm).replace('</center></td>','')
            gf_percent_reltm = str(gf_percent_reltm).replace(' ','')
            opp_gf_60 = str(data[32]).replace('<td><center>','')
            opp_gf_60 = str(opp_gf_60).replace('</center></td>','')
            opp_gf_60 = str(opp_gf_60).replace(' ','')
            opp_ga_60 = str(data[34]).replace('<td><center>','')
            opp_ga_60 = str(opp_ga_60).replace('</center></td>','')
            opp_ga_60 = str(opp_ga_60).replace(' ','')
            opp_gf_percent = str(data[36]).replace('<td><center>','')
            opp_gf_percent = str(opp_gf_percent).replace('</center></td>','')
            opp_gf_percent = str(opp_gf_percent).replace(' ','')
            ozfo = str(data[38]).replace('<td><center>','')
            ozfo = str(ozfo).replace('</center></td>','')
            ozfo = str(ozfo).replace(' ','')
            dzfo = str(data[40]).replace('<td><center>','')
            dzfo = str(dzfo).replace('</center></td>','')
            dzfo = str(dzfo).replace(' ','')
            nzfo = str(data[42]).replace('<td><center>','')
            nzfo = str(nzfo).replace('</center></td>','')
            nzfo = str(nzfo).replace(' ','')
            totfo = str(data[44]).replace('<td><center>','')
            totfo = str(totfo).replace('</center></td>','')
            totfo = str(totfo).replace(' ','')
            ozfo_percent = str(data[46]).replace('<td><center>','')
            ozfo_percent = str(ozfo_percent).replace('</center></td>','')
            ozfo_percent = str(ozfo_percent).replace(' ','')
            dzfo_percent = str(data[48]).replace('<td><center>','')
            dzfo_percent = str(dzfo_percent).replace('</center></td>','')
            dzfo_percent = str(dzfo_percent).replace(' ','')
            nzfo_percent = str(data[50]).replace('<td><center>','')
            nzfo_percent = str(nzfo_percent).replace('</center></td>','')
            nzfo_percent = str(nzfo_percent).replace(' ','')

            player_data = [name, team, gp, toi, gf_60, ga_60, gf_percent,
                           sh_percent, sv_percent, pdo, tmgf_60, tmga_60,
                           tmgf_percent, gf_60_reltm, ga_60_reltm, gf_percent_reltm,
                           opp_gf_60, opp_ga_60, opp_gf_percent, ozfo, dzfo, nzfo,
                           totfo, ozfo_percent, dzfo_percent, nzfo_percent]

            list.append(final_data, player_data)

        except:
            continue

    columns = ['name','team','gp','toi','gf_60','ga_60','gf_percent',
               'sh_percent','sv_percent','pdo','tmgf_60','tmga_60','tmgf_percent',
               'gf_60_reltm','ga_60_reltm','gf_percent_reltm','opp_gf_60',
               'opp_ga_60','opp_gf_percent','ozfo','dzfo','nzfo','totfo',
               'ozfo_percent','dzfo_percent','nzfo_percent']

    player_df = pd.DataFrame(final_data, columns=columns)
    player_df.to_csv('player_data_{}_{}_{}.csv'.format(year, situation, type), index=False)

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

    situation_list = ['5v5','5v5home','5v5road','5v5close','5v5close_home',
                      '5v5close_road','5v5tied','5v5tied_home','5v5tied_road',
                      '5v5leading','5v5leading_home','5v5leading_road',
                      '5v5trailing','5v5trailing_home','5v5trailing_road',
                      '5v5up1','5v5up2','4v4','5v5firstperiod','5v5secondperiod',
                      '5v5thirdperiod','5v4','4v5','PP','SH','f10','5v5home_f10',
                      '5v5road_f10','5v5close_f10','5v5tied_f10','5v5up1_f10',
                      '5v5up2_f10','5v5down1_f10','5v5down2_f10','5v5leading_f10',
                      '5v5trailing_f10']

    type_list = ['individual','goals','shots','fenwick','corsi']

    year = input("Which Year Do You Want to Scrape? (Enter 'All' for All of Them): ")
    situation = input("Which Situation Do You Want to Scrape? (Enter 'All' for All of Them): ")
    type = input("Which Type Do You Want to Scrape? (Enter 'All' for All of Them): ")

    if year == 'All':
        if situation == 'All':
            if type == 'All':
                print('')
                for year in year_list:
                    for situation in situation_list:
                        for type in type_list:
                            if type == 'individual':
                                print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                                scrape_individual(year, situation)
                            else:
                                print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                                scrape_on_ice(year, situation, type)
            else:
                print('')
                for year in year_list:
                    for situation in situation_list:
                        if type == 'individual':
                            print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                            scrape_individual(year, situation)
                        else:
                            print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                            scrape_on_ice(year, situation, type)
        else:
            if type == 'All':
                print('')
                for year in year_list:
                    for type in type_list:
                        if type == 'individual':
                            print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                            scrape_individual(year, situation)
                        else:
                            print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                            scrape_on_ice(year, situation, type)
            else:
                print('')
                for year in year_list:
                    if type == 'individual':
                        print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                        scrape_individual(year, situation)
                    else:
                        print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                        scrape_on_ice(year, situation, type)
    else:
        if situation == 'All':
            if type == 'All':
                print('')
                for situation in situation_list:
                    for type in type_list:
                        if type == 'individual':
                            print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                            scrape_individual(year, situation)
                        else:
                            print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                            scrape_on_ice(year, situation, type)
            else:
                print('')
                for situation in situation_list:
                    if type == 'individual':
                        print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                        scrape_individual(year, situation)
                    else:
                        print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                        scrape_on_ice(year, situation, type)
        else:
            if type == 'All':
                print('')
                for type in type_list:
                    if type == 'individual':
                        print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                        scrape_individual(year, situation)
                    else:
                        print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                        scrape_on_ice(year, situation, type)
            else:
                print('')
                if type == 'individual':
                    print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                    scrape_individual(year, situation)
                else:
                    print('Scraping Year | Situation | Type: {} | {} | {}'.format(year, situation, type))
                    scrape_on_ice(year, situation, type)


if __name__ == '__main__':
    main()