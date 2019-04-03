from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

'''
  SPU -IS_UPPER_DEPT-> PDT
  SPU -OWN-> Feature
  SPU <-EMPLOYEEOF- Employee
  
  PDT <-IS_UPPER_DEPT- SPU
  PDT -OWN-> Feature
  PDT <-EMPLOYEEOF- Employee
  
  Employee -EMPLOYEEOF->PDT
  Employee -EMPLOYEEOF->SPU
  Employee -MANAGE->Feature
  
  Feature <-OWN-SPU
  Feature <-OWN-PDT
  Feature <-MANAGE-Employee
'''
class SPU(GraphObject):
    __primarykey__ = "name"

    name = Property()
    supervisor = Property()
    pdts = RelatedTo("PDT","IS_UPPER_DEPT")
    features = RelatedTo("Feature","OWNS")
    employees = RelatedFrom("Employee","EMPLOYEEOF")

    def __lt__(self,other):
        return self.name < other.name

class PDT(GraphObject):
    __primarykey__ = "name"

    name = Property()
    supervisor = Property()
    spu = RelatedFrom("SPU","IS_UPPER_DEPT")
    features = RelatedTo("Feature","OWNS")
    employees = RelatedFrom("Employee", "EMPLOYEEOF")

    def __lt__(self,other):
        return self.name < other.name

class Employee(GraphObject):
    __primarykey__ = "id"

    id = Property()
    name = Property()

    spu = RelatedTo("SPU","EMPLOYEEOF")
    pdt = RelatedTo("PDT","EMPLOYEEOF")
    features = RelatedTo("Feature","MANAGE")


    def __lt__(self,other):
        return self.id < other.id

class Feature(GraphObject):
    __primarykey__ = "name"

    name = Property()
    desc_zh_cn = Property()
    desc_en_us = Property()

    spu = RelatedFrom("SPU","OWN")
    pdt = RelatedFrom("PDT","OWN")
    employee = RelatedFrom("Feature","MANAGE")

    def __lt__(self,other):
        return self.name < other.name;




