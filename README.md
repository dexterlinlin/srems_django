一 技术栈选择
前端Vue的所有技术栈： vue2 + vuex + vue-router + webpack + d3
UI库： element-ui
网络请求：axios
前端脚手架构建工具：vue-cli
后端技术栈：Python+Django
对象图形框架：py2neo.ogm
数据库： neo4j /mysql
分布式：Apache Flink /Spark

二、开发环境准备：
1、安装NodeJS(https://nodejs.org/en/)
2、安装Django
   pip install django 
   pip install -r requirements.txt
3、安装VUE脚手架
   npm install -g cnpm --registry=https://registry.npm.taobao.org
   cnpm install -g vue-cli
   

 


杂项(待整理):
2019-3-31:
FrontEnd:VueJS d3
WebFramework:bottle django
DB: Neo4j (https://neo4j.com/docs/)
OGM: pyneo4jogm

Later： spark + neo4j

Export requirement： pip freeze > requirements.txt

remaining question: 
1. how to display topology in web
2. how to display chinese words properly in web
3. ....


generate ssh-key: 
ssh-keygen -t rsa -C "your_email@example.com"

2019-4-1：
clear neo4j database：
  match (n)
  detach delete n

