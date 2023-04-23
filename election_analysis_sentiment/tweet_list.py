'''tweets = ["congress made vemula nation talk point even though doubt case amp vemula dalit itself stop bjp make ramalingam case attain nation scale amp chang dalit discours take one remark pm modi make happen",
"bjp win battl past month bengal pm modi arriv win biggest battl announc warcri upcom war tmc elect modisonarbangla",
"inclusivemind ark bjpindia rahul gandhi bjp think cellchatumediacroniesscrit writer andbhakt crore speach give victori then late atal bihari vajpeyi much better shine india",
"senior congress leader manishtewari jpc definit next parliament parallel crimin investig process go go away rafal rafalenot",
"bc congress take kickback fr pp",
"rahul lie caught exclus former defenc secretari g mohan kumar tear rahul gandhi lie say no pmo interfer rafal price",
"expect meltdown congress elect wait till februari end bahut saar possibl hain ji",
"stori realli expos develop propaganda nation congress cudnt yrs modi sirji ask month abl hear terrifi stori jharkhand govt cudnt even solv basic issu last yrs",
"issu problem parrikar say defenc secretari resolv problemmatt princip secretari pm actual nail modi anyth els",
"forthefirsttim activ diplomaci pm modi india emerg leader intern platform first indian prime minist visit israel strengthen tie ageold natur alli year",
"modiunstopp speech made noisi kharg amp compani nervous confid speak way come easili one sincer amp honest job paplu taplu remain absent perhap nirmala ji arunji piyush ji s trailer prefer avoid modi ji s punch",
"piti state affair swachh bharat mission modi s kashi could understood fact even minist neelkanth tiwari also admit work mark flopswachhbharat",
"jim jordan remain best argument drug test member congress whitakerhear",
"rahul rahul gandhi ji use claim defenc minist manoharparrikar ji complet ignor rafaled note rafal file anoth lie expos rahulliecaught",
"modi govt make kitchen smoke free pmuy approx crore lpg connect provid poor india becom second largest lpg consum lpg coverag cleaner fuel ensur cleaner environ too transformingindia",
"bjp mp sh ianuragthakur launch campaign abkibaarpaar",
"prime minist shri modi today expos congress parti s fals fake campaign sever issu deliv outstand speech floor lok sabha congratul prime minist complet demolish opposit s claim",
]



def fetch_tweet():
    return tweets'''

import csv

def retrieve_tweet(query):
  tweets_list = []
  filename = 'Final_Tweet_Dataset.csv'
  column_name = 'Id'
  count =0
  with open(filename, 'r') as csvfile:
      #reader = csv.reader(csvfile)
      reader = csv.DictReader(csvfile)
      flag = 0
      for row in reader:
          #if query in row:
          if row[column_name] == query:
            flag = 1
            #print(type(row))
            if(count == 100):
              break
            count = count + 1 
            tweets_list.append(row.get('Tweet'))

  return tweets_list
