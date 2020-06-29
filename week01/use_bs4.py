import requests
from bs4 import BeautifulSoup as bs
import pandas

def get_movie_list(myurl):
    movie_list = []
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    Cookie = '__mta=216432553.1593157179116.1593416250543.1593441366227.14; uuid_n_v=v1; uuid=2F36D140B78011EA9C0AF732B1940F47CB9E98D7B7E14F578159BC42D9CEDBC0; _csrf=3debe017b62478ae6b1a85d7465506f89cf28d66168f9cbbb49125206967b1be; mojo-uuid=fd02fa8f958d67809ea388260fe358d4; _lxsdk_cuid=172ef9156acc8-057a88abf7e114-4353760-144000-172ef9156acc8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593261116,1593309214,1593396795,1593396814; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172ff02177127e-045e3d6eaf2535-5437971-304704-172ff021772499%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172ff02177127e-045e3d6eaf2535-5437971-304704-172ff021772499%22%7D; _lxsdk=2F36D140B78011EA9C0AF732B1940F47CB9E98D7B7E14F578159BC42D9CEDBC0; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593442077; __mta=216432553.1593157179116.1593441366227.1593442077207.15; _lxsdk_s=17300ce7ca2-d4f-a1a-fe%7C%7C1'
    header = {'user-agent':user_agent, 'Cookie':Cookie}

    response = requests.get(myurl, headers = header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class':'movie-hover-info'}, limit = 10):
        atag = tags.find_all('div', attrs = {'class':'movie-hover-title'})
        movie_name = tags.find('span', attrs = {'class':'name'}).text.strip()
        movie_kind = atag[1].text.strip()
        movie_uptime = atag[3].text.strip()
        movie_list.append({'name':movie_name, 'kind':movie_kind, 'uptime':movie_uptime})
        # print(f'{movie_name}, {movie_kind}, {movie_uptime}')
    return movie_list


myurl = 'https://maoyan.com/films?showType=3'

print(get_movie_list(myurl))
movie = pandas.DataFrame(get_movie_list(myurl))
movie.to_csv('./movie.csv',index=False, encoding='utf_8_sig')

