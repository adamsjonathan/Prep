import datetime
import requests
import webhoseio
webhoseio.config(token="36670ea5-52b9-4339-a937-1733739e0385")


def notify(user,role,company,timetoiview):  #notification function to identify which message to send

    notifications={
    '-2':"Hi "+user+" your interview with "+company+" for the "+role+" role is in 2 days time, have you got your outfit picked out?",
    '-1': "Hi "+user+", it's the big day tomorrow!  You’re well prepared, get a good night’s sleep.  You’re going to do great!",
    '0':"Big day today "+user+"!  You’re going to get the "+role+" role at "+company+", we believe in you!",
    '1':"Hi "+user+", we hope the interview at "+company+" went well!  Time for a debrief, click here",
    '2':user+", it’s been 2 days since your interview with "+company+" for the "+role+" role.  Time to send a follow up note.  If you’d like some help click here.",
    '4':"Hi "+user+", any news on the interview for the "+role+" at "+company+" ? We’d love to here how you got on.",
    'travelalert':"Hi "+user+", looks like there might be a delay on your preferred route, click here to review."
    }

    message=notifications[str(timetoiview)]
    print(timetoiview, message)
#    return send_simple_message(message,user,useremail)


def companynews(company, user, useremail):
    query=company+" language:english performance_score:>2 organization:"+company+" site_type:news"+" thread.title:"+company
    query_params = {
    "q": query,
    "ts": "1506702682219",
	"sort": "relevancy",
    "is_first" : "true"
    }
    output = webhoseio.query("filterWebContent", query_params)
    newslist=list()

    for articles in output['posts']: #parses json respponse in ooutput to extract stories
        image=(articles['thread']['main_image'])
        title=(articles['thread']['title'])
        story=(articles['text'])
        paragraph=(story[:500],'...')
        link=(articles['thread']['url'])

        #creates html body object for each story
        body= """\
        <p><img src="{image}" alt="News source image" width="150" height="100" /></p>
        <h3>{title}</h3>
        <pre><code></code></pre>
        <p>{paragraph}</p>
        <pre><code></code></pre>
        <p>Here's a link to the full article:</p>
        <h3><code><br /><a href="{link}" target="_blank" rel="noopener">Here's a link to the full article<br /></code></h3>
        <hr />
        """.format(user=user, company=company, image=image,title=title,paragraph=paragraph,link=link)

        newslist.append(body) #creates a list of stories in html format

    #generic html header for the start of the email
    generic_header="""\
    <p><img src="https://image.ibb.co/josVLm/Screen_Shot_2017_10_26_at_11_23_41.png" width="800" height="100"> </p>
    <pre><code></code></pre>
    <h2>Hi {user},</h2>
    <pre><code></code></pre>
    <p><h2>Here is the latest news on {company} from across the web:</h2></p>
    <pre><code></code></pre>
    <hr />
    <pre><code></code></pre>
    """.format(user=user, company=company)

    #generic html footer for the end of the email
    generic_footer="""
    <h3><code><br /><a href="http://www.prepped.io" target="_blank" rel="noopener">www.prepped.io</a>&nbsp;- Your interview coach<br /></code></h3>"""


    message=(generic_header,newslist,generic_footer) #creates email message by adding header, body and footer

    #return send_simple_message(message,user,useremail)


def send_simple_message(message,user,useremail): # mailgun function to send messages
    return requests.post(
        "https://api.mailgun.net/v3/sandbox82b15a0e185b43d08896115aae76d63a.mailgun.org/messages",
        auth=("api", "key-09b37f8b0cc146089d2bcedf1e32b824"),
        data={"from": "notifications@prepped.io",
              "to": useremail,
              "subject": "Hello "+user+" a message from your interview coach",
              "html":message})


#time monitoring
today=1 #datetime.datetime.now()
iviewdatetime=1
timetoiview=(iviewdatetime-today)


#get parameters to pass to functions
user="Jonathan" #input('which user? ')
useremail= "adamsjonathan1@gmail.com" #input("Whats the user's email address? ")
role='CEO' #input("Which role? ")
company='Tesla' #input('Which company? ')

#Call notify and companynews functions, which complete and invoke send_simple_message function
notify(user,role,company,timetoiview)
companynews(company,user,useremail)
