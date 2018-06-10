#WARNING! SPAGHETTI CODE
import pprint
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser
import tkinter
import tkinter.messagebox
qna = open('ocr.txt', 'r').read()
startTime = datetime.now()
q = qna[0:qna.find('?') + 1]
a = qna[qna.find("?") + 1:len(qna)]
a = a.replace("\n" , "¬")
a = a.replace("¬¬" , "¬")
if a[0] == "¬":
	a = a[1:len(a)]
if a[len(a)-1] == "¬":
	a = a[0:len(a)-1]
A1 = a[0:a.index("¬")]
a = a[a.index("¬")+1:len(a)]
A2 = a[0:a.index("¬")]
a = a[a.index("¬")+1:len(a)]
A3 = a
q = q.replace("\n" , " ")
q = q.replace("\"" , "")
q = q.replace("\'" , "")

S1 = requests.get("https://www.google.com/search", params={'q':q + " \"" + A1 + "\""})
soup1 = BeautifulSoup(S1.text, "lxml")
S1 = soup1.find("div", {"id": "resultStats"})
S1 = S1.text
S2 = requests.get("https://www.google.com/search", params={'q':q + " \"" + A2 + "\""})
soup2 = BeautifulSoup(S2.text, "lxml")
S2 = soup2.find("div", {"id": "resultStats"})
S2 = S2.text
S3 = requests.get("https://www.google.com/search", params={'q':q + " \"" + A3 + "\""})
soup3 = BeautifulSoup(S3.text, "lxml")
S3 = soup3.find("div", {"id": "resultStats"})
S3 = S3.text
S1 = S1.replace("About " , "")
S1 = S1.replace(" results" , "")
S1 = S1.replace(" result" , "")
S1 = S1.replace("," , "")
S2 = S2.replace("About " , "")
S2 = S2.replace(" results" , "")
S2 = S2.replace(" result" , "")
S2 = S2.replace("," , "")
S3 = S3.replace("About " , "")
S3 = S3.replace(" results" , "")
S3 = S3.replace(" result" , "")
S3 = S3.replace("," , "")
S1 = int(S1)
S2 = int(S2)
S3 = int(S3)
gq = q.replace(" " , "+")
gq = gq.replace("\'" , "")
gq = gq.replace("\"" , "")
#webbrowser.open("http://www.google.co.uk/search?q=" + gq)

if S1 < S2 > S3:
	bigsearch = A2
elif S2 < S1 > S3:
	bigsearch = A1
elif S1 < S3 > S2:
	bigsearch = A3
else:
	bigsearch = "null"

results = requests.get("https://www.google.com/search", params={'q':q})
resultsoup = BeautifulSoup(results.text, "lxml")
search = resultsoup.find("div", {"id": "search"})
search = search.text
search = search.lower()
A1count = search.count(A1.lower())
A2count = search.count(A2.lower())
A3count = search.count(A3.lower())
print(str(A3count))
if A1count < A2count > A3count:
	firstpage = A2
elif A2count < A1count > A3count:
	firstpage = A1
elif A1count < A3count > A2count:
	firstpage = A3
else:
	firstpage = "null"

if A1count > A2count < A3count:
	smallest = A2
elif A2count == A3count:
	smallest = A2 + " and " + A3
elif A2count == A1count:
	smallest = A2 + " and " + A1
elif A2count > A1count < A3count:
	smallest = A1
elif A1count == A3count:
	smallest = A1 + " and " + A3
elif A1count == A2count:
	smallest = A2 + " and " + A1
elif A1count > A3count < A2count:
	smallest = A3
elif A3count == A1count:
	smallest = A3 + " and " + A1
elif A2count == A1count:
	smallest = A2 + " and " + A1
else:
	smallest = "null"
if bigsearch == "null" and smallest == "null" and firstpage == "null":
	tkinter.messagebox.showinfo("Fuck, something went wrong.")
	webbrowser.open("http://www.google.co.uk/search?q=" + gq)
else:
	tkinter.messagebox.showinfo("Searches", "First Page: " + firstpage + "\n" + "Total: " + bigsearch + "\n" + "Smallest: " + smallest)
