#!/usr/bin/python

import requests
page = requests.get("https://attack.mitre.org/groups/G0087/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
from py2neo import Graph
graph=Graph(password="1234")
from py2neo import Node, Relationship, Graph, NodeMatcher
matcher = NodeMatcher(graph)

# collect tables in to table

table=soup.find_all("table",class_="table table-bordered table-alternate mt-2")

#collect the content of (tbody tags) of the table[1] to  table2

table2=table[1].tbody

td=table2.find_all('td')
techniques=[]
for i in range(2,len(td),4):
#		print((td[i].text).strip())
		techniques.append((td[i].text).strip())
print("techniques scraped")

#techniques[] list is with all the techniques used by the threat actor

#collect the content of table3-software (index at table[2]) as table3

table3=table[2]

# collect all <td> tags (actual software names details)

td=table3.find_all('td')

# td tags have software names in it, hence we need to target software names and leaving other information out.
# Starting with 1st element of the 'td' list ,after every 4 element there is a name of the software, hence loop through accordingly 
#and collect all software names in to a list named "software"

software=[]
for i in range(1,len(td),4):
#	print((td[i].text).strip())
	software.append((td[i].text).strip())

print("software scraped")

#Collect the "Threat Actor" (Group Name)in group 

group1=soup.h1.text.strip()
group=matcher.match("groups",name=group1).first()
print("group node loaded")
#Relationship Creation 

for i in range(len(techniques)):
	technique=matcher.match("techniques",name=techniques[i]).first()
	r=Relationship(group,"USES",technique)
	graph.merge(r)
print( "Relationships 'group USES techniques' are pushed")


for i in range(len(software)):
	s=matcher.match("software",name=software[i]).first()
	r=Relationship(group,"USES",s)
	graph.merge(r)
print("Relationships 'group USES software' are pushed" )




