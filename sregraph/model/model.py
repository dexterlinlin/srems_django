from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

###
1.SPU PDT Employee Feature
2.
  SPU -IS_UPPER_DEPT-> PDT
  SPU -OWN -> Feature


###
class SPU(GraphObject):
    __primarykey__ = "name"

    name = Property()
    pdts = RelatedTo("PDT","IS_UPPER_DEPT")
    features = RelatedTo("Feature","OWNS")

    def __lt__(self,other):
        return self.name < other.name

class PDT(GraphObject):
    __primarykey__ = "name"

    name = Property()

    def __lt__(self,other):
        return self.name < other.name

class Employee(GraphObject):
    __primarykey__ = "id"

    id = Property()
    name = Property()

    def __lt__(self,other):
        return self.id < other.id

class Feature(GraphObject):
    __primarykey__ = "name"

    name = Property()
    desc_zh_cn = Property()
    desc_en_us = Property()

    def __lt__(self,other):
        return self.name < other.name;




