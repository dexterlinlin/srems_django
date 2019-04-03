from bottle import get, post, redirect, request, run, static_file, template, TEMPLATE_PATH,Bottle
from calendar import month_name
from datetime import date
from os import getenv
from os.path import dirname, join as path_join
from py2neo import Graph

from sregraph.models.model import SPU
from sregraph.views import initDynamicViews

home = dirname(__file__)
static = path_join(home, "static")
TEMPLATE_PATH.insert(0, path_join(home, "views"))

# Set up a link to the local graph database.
graph = Graph(password=getenv("NEO4J_PASSWORD"))
bottle = Bottle()
initDynamicViews(bottle)
# watch("neo4j.bolt")

@bottle.get('/dept/list')
def get_dept():
    try:
        return SPU.match(graph)
    except Exception as e:
        print ("Exception:",e)




@bottle.post('/dept/add')
def addDept():
    dept = request.forms.get('dept')
    upperdept = request.forms.get('upperdept')
    role = request.forms.get('role')

@bottle.delete('/dept')
def modifyDept():
    dept = request.forms.get('dept')




if __name__ =="__main__":
    run(bottle,host="localhost",port=8080,reloader=True)
