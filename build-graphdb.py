#!/usr/bin/python

from stix2 import TAXIICollectionSource
from taxii2client import Server
from stix2 import TAXIICollectionSource, Filter
from taxii2client import Collection
from itertools import chain
from py2neo import Graph
graph=Graph(password="1234")
from py2neo import Node, Relationship, Graph, NodeMatcher
matcher = NodeMatcher(graph)


# Instantiate server and get API Root
server = Server("https://cti-taxii.mitre.org/taxii/")
api_root = server.api_roots[0]

# Print name and ID of all ATT&CK technology-domains available as collections
for collection in api_root.collections:
          print(collection.title + ": " + collection.id)

collection = Collection("https://cti-taxii.mitre.org/stix/collections/95ecc380-afe9-11e4-9b6c-751b66dd541e/")
tc_source = TAXIICollectionSource(collection)
print("collection source initialized")

#getting all techniques in a list 

filt=Filter('type','=','attack-pattern')
techniques=tc_source.query([filt])
print("tehniques pulled")
#pushing techiques to Neo4j GrapgDB
print(len(techniques))
lt=len(techniques)
i=0
for i in range(len(techniques)):
	technique=Node("techniques",id=techniques[i]['id'],name=techniques[i]['name'])
	graph.create(technique)

print("techniques pushed")

#Getting All Software-data in a list 

def get_all_software(src):
    filts = [
        [Filter('type', '=', 'malware')],
        [Filter('type', '=', 'tool')]
    ]
    return list(chain.from_iterable(
        src.query(f) for f in filts
    ))
tools=get_all_software(tc_source)
print("software pulled")
print(len(tools))
lto=len(tools)
# Pushing software in Neo4j GraphDB 
i=0
for i in range(len(tools)):
	software=Node("software",id=tools[i]['id'],name=tools[i]['name'])
	graph.create(software)
print("software pushed")

#getting all groups in to a list 

filt=Filter('type','=','intrusion-set')
groups=tc_source.query([filt])
print("groups pulled")
print(len(groups))
lg=len(groups)
#pushing gropups in neo4j Graph DB
i=0
for i in range(len(groups)):
	group=Node("groups",id=groups[i]['id'],name=groups[i]['name'])
	graph.create(group)

print("groups pushed")
print("total entities pushed=",lt+lto+lg)
