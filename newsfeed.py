import webhoseio

webhoseio.config(token="36670ea5-52b9-4339-a937-1733739e0385")

def companynews(company):
    query=company+" language:english performance_score:>2 organization:"+company+" site_type:news"+" thread.title:"+company
    query_params = {
    "q": query,
    "ts": "1506702682219",
	"sort": "relevancy"
    }
    output = webhoseio.query("filterWebContent", query_params)
#    print (output)

    for articles in output['posts']:

        image=(articles['thread']['main_image'])
        title=(articles['thread']['title'])
        story=str(articles['text'])
        paragraph=(story[:500],'...')
        link=('Link to full article:',articles['thread']['url'])

        print (image,/n)
        print (title)
        print (paragraph)
        print (link)
# Get the next batch of posts
#    output = webhoseio.get_next()


company=input('Which company? ')
companynews(company)
