# MITRE ATTACK-Threat_Intel

## Graph Representation of MITRE ATT&CK's CTI data

### Background

This project is a prototype-build for representing MITRE's ATT&CK CTI data in a Graph view with relationships between various objects.
The objects could be Threat Groups,Techniques used in cyber attacks OR software (tools,malware). 

![Graph ATT&CK's CTI Data](https://github.com/Kirtar22/ATTACK-Threat_Intel/blob/master/Graph_ATT%26CK_CTI.PNG)

MITRE has published its CTI data via TAXII2.0 server in the STIXX2.0 format. In ATT&CK, there are three main concepts (excluding Tactics for now): Techniques, Groups, and Software. Most techniques also have Mitigations. 

STIX 2.0 describes these as objects and uses different terminology to describe them. The following table is a mapping of ATT&CK concepts to STIX 2.0 objects:

|ATT&CK concept|STIX Object type|
|--------------|----------------|
|  Technique   |`attack-pattern`|
|  Group       |`intrusion-set`|
|  Software    |`malware` or `tool`|
|Mitigation|`course-of-action`|
|Tactic|`x-mitre-tactic`|
|Matrix|`x-mitre-matrix`|

### This Project 

### Prerequsites 

- [Neo4j Desktop](https://neo4j.com/product/#desktop)

- Python 
**Python Libraries**

[STIX2.0](https://stix2.readthedocs.io/en/latest/)

[TAXII2.0 Client](https://taxii2client.readthedocs.io/en/stable/)

[Py2neo](https://py2neo.org/v4/)

[BeautifulSoup (bs4)](https://beautiful-soup-4.readthedocs.io/en/latest/)

Py2neo is a client library and toolkit for working with Neo4j from within Python applications and from the command line. 
I have used Py2neo python library that connects to Neo4j API to perform all Neo4j operations so that we do not need to go outof Python Application.

**Logical Flow of the Scripts**

1. Connect with MITRE's TAXII2 Sever
2. Pull the STIXX2.0 data(techniques,software,groups) from the MITRE's TAXII2 Server 
3. Create the objects out of the pulled data & Push them to Neo4j and build the the GraphDB
4. Scrap the MITRE ATT&CK's page for a specific group that contains corrosponding software & techniques (used by that specific group)
5. Create the relationships and push them to Neo4j 

**Note/Observations:** 

I believe there is some bug in g.merge() function of latest py2neo version as it does not work as expected always. Therefore, I have to use create() function in "" script instead of merge. merege() is prefered as it will not create the duplicate node if a matching node is arleady exist whereas create() will make duplicate objects. 

This is just a prototype and this can be scalled up and improved to take this to the production level. This is the one of the many ways by which this database can be built and represented.I do not deny that there could be an effecient way of doing the same thing.The MITRE's CTI data can be pulled and stored in json files and then json-files can be called and loaded in neo4j using its "CYPHER"s to build the database.Once the database is built, CYPHER can be used to build the relationships as well. 
