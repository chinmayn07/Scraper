from urllib.request import urlopen
from bs4 import BeautifulSoup
# from pymongo import MongoClient 
import pymongo

html = urlopen("https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&s") 
soup = BeautifulSoup(html.read(),features='html5lib');
table = soup.findAll('table',{"id":"sample_1"})[0] 	#extracting link of home page table
link=[]

for ref in table.findAll('a', attrs={"class": "points"}):
	link.append(ref.get('href'))

pdf=[]
def direct(path):
	html2 = urlopen(path) 
	soup2 = BeautifulSoup(html2.read(),features='html5lib');
	try:
		div = soup2.findAll('div',{"class":"cover"})[0]
		pdf1=""
		for di in div.findAll('iframe'):
			di=di.get('src')
			if di==None:
				pass
			else:
				pdf1=pdf1.join(di)
				pdf1=pdf1[19:]
		return pdf1
	except IndexError:
		flag="N"
		return flag
	

def open(path):
	html1 = urlopen(path) # Insert your URL to extract
	soup1 = BeautifulSoup(html1.read(),features='html5lib');
	table = soup1.findAll('table',{"class":"table-bordered"})[0]
	pdf.clear()
	for pf in table.findAll('a'):
		pf=pf.get('href')
		pdf.append(pf)
	return pdf

store=""
store2=[]
li=[]
dicts={}
for path in link:
	store=(direct(path))
	if(store=="N"):
		store2.extend(open(path))
	else:
		li.append(store)
		store=""
store2.extend(li)
# print(store2)
print(len(store2))
dicts = { store2[i] : i for i in range(0, len(store2))}
print(dicts)
# try: 
#     conn = MongoClient() 
#     print("Connected successfully!!!") 
# except:   
#     print("Could not connect to MongoDB")

# db = conn.database 
# collection = db.pdf

# rec_id1 = collection.insert_one(dicts) 

# print("Data Stored with record ids",rec_id1)
myclient = pymongo.MongoClient("localhost")


mydb = myclient["internship"]
mycol = mydb["linkpdf"]
def insert(self, doc_or_docs, manipulate=True,safe=None, check_keys=True, continue_on_error=False, **kwargs):
	pass

mycol.insert(dicts,check_keys=False)


