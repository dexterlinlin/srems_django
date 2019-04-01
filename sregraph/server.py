from bottle import get, post, redirect, request, run, static_file, template, TEMPLATE_PATH
from calendar import month_name
from datetime import date
from os import getenv
from os.path import dirname, join as path_join
from py2neo import Graph, watch

home = dirname(__file__)
static = path_join(home, "static")
TEMPLATE_PATH.insert(0, path_join(home, "views"))

# Set up a link to the local graph database.
graph = Graph(password=getenv("NEO4J_PASSWORD"))
watch("neo4j.bolt")

if __name__ =="__main__":
    run(host="localhost",port=8080,reloader=True)
