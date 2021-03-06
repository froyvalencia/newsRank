from nytimesarticle import articleAPI
api = articleAPI('77cb4690bfcc410aa646217a1502e601')

'''
The q (for query) parameter searches the article's body, headline and byline for a particular term. In this case, we are looking for the search term ‘Obama’. The fq (for filter query) parameter filters search results by various dimensions. For instance, ‘headline’:’Obama’ will filter search results to those with ‘Obama’ in the headline. 'source':['Reuters','The New York Times'] will filter by source (Reuters, New York Times, and AP are available through the API.) The begin_date parameter (in YYYYMMDD format) limits the date range of the search.
'''
#articles = api.search( q = 'Obama', fq = {'headline':'Obama', 'source':['Reuters','AP', 'The New York Times'], begin_date =20111231)



def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parss
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.append(dic)
    return(news) 

def get_articles(date,query):
    '''
    This function accepts a year in string format (e.g.'1980')
    and a query (e.g.'Amnesty International') and it will 
    return a list of parsed articles (in dictionaries)
    for that year.
    '''
    all_articles = []
    for i in range(0,100): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        articles = api.search(q = query,
               fq = {'source':['Reuters','AP', 'The New York Times']},
               #begin_date = date + '0101',
               #end_date = date + '1231',
               #sort='oldest',
               #page = str(i))
                              )
        print(articles)
        articles = parse_articles(articles)
        print(articles)
        all_articles = all_articles + articles
    return(all_articles)

#articles = api.search(q = 'Obama',fq = {'headline':'Obama', 'source':['Reuters','AP', 'The New York Times']},begin_date = 2011123)
#articles = api.search( q ="Obama", fq = {"headline":"Obama", "source":["Reuters","AP", "The New York Times"] } )

#for a in articles:
#   print(a)

ar =get_articles('2016','Trump')
for a in ar:
    print(a)

#for n in parse_articles(articles):
 #   print(n)


