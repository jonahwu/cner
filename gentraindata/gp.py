import pprint
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch


def GSearch(query, page):
    #search_args = ('preaching to the choir', 1)
    try:
        gsearch = GoogleSearch()
        #ysearch = YahooSearch()
        #bsearch = BingSearch()
        #search_args = ('王建明', 1)
        #gresults = gsearch.search(*search_args)
        maxNum=20
        #gresults = gsearch.search(query='hello world', page=1,num=5, start=1, country_code="tw")
        #gresults = gsearch.search(query='hello world', page=2, country_code="tw")
        gresults = gsearch.search(query=query, page=page, country_code="tw")
        #gresults = gsearch.search(query=query, page=page)
        #yresults = ysearch.search(*search_args)
        #bresults = bsearch.search(*search_args)
        a = {
          "Google": gresults,
          }

        # pretty print the result from each engine
        """
        for k, v in a.items():
          print(f"-------------{k}------------")
          for result in v:
              pprint.pprint(result)
        """
        """
        print('--- show individual result -----')
        print('---- show titles -----')
        print(gresults["titles"][0])
        print('--- show links ----')
        print(gresults["links"][9])
        print('--- show more result ----')
        print(gresults[0])
        print(gresults[0])
        print(len(gresults))
        """
        # print 10th link from yahoo search
        #print(yresults["links"][9])
        # print 6th description from bing search
        #print(bresults["descriptions"][5])

        # print first result containing links, descriptions and title
        return gresults['links'], gresults['titles']
    except Exception as e:
        print(e)
        return '', ''
