from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Bz387752_Enum(Enum):
    VAL0 = "VAL0"
    VAL1 = "VAL1"


############################################
# Definition of Classes
############################################

class HibernateTest_Bz397682P:

    def __init__(self, dbId: str, refToP: set["HibernateTest_Bz397682C"] = None, Bz397682P: "HibernateTest_Bz397682C" = None):
        self.dbId = dbId
        self.refToP = refToP if refToP is not None else set()
        self.Bz397682P = Bz397682P
        
    @property
    def dbId(self) -> str:
        return self.__dbId

    @dbId.setter
    def dbId(self, dbId: str):
        self.__dbId = dbId

    @property
    def Bz397682P(self):
        return self.__Bz397682P

    @Bz397682P.setter
    def Bz397682P(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz397682P__Bz397682P", None)
        self.__Bz397682P = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "listOfC"):
                opp_val = getattr(old_value, "listOfC", None)
                if opp_val == self:
                    setattr(old_value, "listOfC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "listOfC"):
                opp_val = getattr(value, "listOfC", None)
                setattr(value, "listOfC", self)

    @property
    def refToP(self):
        return self.__refToP

    @refToP.setter
    def refToP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz397682P__refToP", None)
        self.__refToP = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bz397682C"):
                    opp_val = getattr(item, "Bz397682C", None)
                    
                    if opp_val == self:
                        setattr(item, "Bz397682C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bz397682C"):
                    opp_val = getattr(item, "Bz397682C", None)
                    
                    setattr(item, "Bz397682C", self)
                    

class Bz398057B:

    pass
class HibernateTest_Bz398057B1(Bz398057B):

    def __init__(self, valueStr: str):
        self.valueStr = valueStr
        
    @property
    def valueStr(self) -> str:
        return self.__valueStr

    @valueStr.setter
    def valueStr(self, valueStr: str):
        self.__valueStr = valueStr

class Bz398057A:

    pass
class HibernateTest_Bz398057A1(Bz398057A):

    pass
class HibernateTest_Bz398057B:

    def __init__(self, value: float, dbId: str, Bz398057B: "HibernateTest_Bz398057A" = None, listOfB: "HibernateTest_Bz398057A" = None):
        self.value = value
        self.dbId = dbId
        self.Bz398057B = Bz398057B
        self.listOfB = listOfB
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def dbId(self) -> str:
        return self.__dbId

    @dbId.setter
    def dbId(self, dbId: str):
        self.__dbId = dbId

    @property
    def listOfB(self):
        return self.__listOfB

    @listOfB.setter
    def listOfB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz398057B__listOfB", None)
        self.__listOfB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bz398057A"):
                opp_val = getattr(old_value, "Bz398057A", None)
                if opp_val == self:
                    setattr(old_value, "Bz398057A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bz398057A"):
                opp_val = getattr(value, "Bz398057A", None)
                setattr(value, "Bz398057A", self)

    @property
    def Bz398057B(self):
        return self.__Bz398057B

    @Bz398057B.setter
    def Bz398057B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz398057B__Bz398057B", None)
        self.__Bz398057B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refToClassA"):
                opp_val = getattr(old_value, "refToClassA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refToClassA"):
                opp_val = getattr(value, "refToClassA", None)
                if opp_val is None:
                    setattr(value, "refToClassA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HibernateTest_Bz397682C:

    def __init__(self, dbId: str, Bz397682C: "HibernateTest_Bz397682P" = None, listOfC: "HibernateTest_Bz397682P" = None, HibernateTest_Bz397682C: "HibernateTest_Bz397682C" = None, HibernateTest_Bz397682C16: "HibernateTest_Bz397682C" = None):
        self.dbId = dbId
        self.Bz397682C = Bz397682C
        self.listOfC = listOfC
        self.HibernateTest_Bz397682C = HibernateTest_Bz397682C
        self.HibernateTest_Bz397682C16 = HibernateTest_Bz397682C16
        
    @property
    def dbId(self) -> str:
        return self.__dbId

    @dbId.setter
    def dbId(self, dbId: str):
        self.__dbId = dbId

    @property
    def HibernateTest_Bz397682C16(self):
        return self.__HibernateTest_Bz397682C16

    @HibernateTest_Bz397682C16.setter
    def HibernateTest_Bz397682C16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz397682C__HibernateTest_Bz397682C16", None)
        self.__HibernateTest_Bz397682C16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HibernateTest_Bz397682C"):
                opp_val = getattr(old_value, "HibernateTest_Bz397682C", None)
                if opp_val == self:
                    setattr(old_value, "HibernateTest_Bz397682C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HibernateTest_Bz397682C"):
                opp_val = getattr(value, "HibernateTest_Bz397682C", None)
                setattr(value, "HibernateTest_Bz397682C", self)

    @property
    def HibernateTest_Bz397682C(self):
        return self.__HibernateTest_Bz397682C

    @HibernateTest_Bz397682C.setter
    def HibernateTest_Bz397682C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz397682C__HibernateTest_Bz397682C", None)
        self.__HibernateTest_Bz397682C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HibernateTest_Bz397682C16"):
                opp_val = getattr(old_value, "HibernateTest_Bz397682C16", None)
                if opp_val == self:
                    setattr(old_value, "HibernateTest_Bz397682C16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HibernateTest_Bz397682C16"):
                opp_val = getattr(value, "HibernateTest_Bz397682C16", None)
                setattr(value, "HibernateTest_Bz397682C16", self)

    @property
    def listOfC(self):
        return self.__listOfC

    @listOfC.setter
    def listOfC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz397682C__listOfC", None)
        self.__listOfC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bz397682P"):
                opp_val = getattr(old_value, "Bz397682P", None)
                if opp_val == self:
                    setattr(old_value, "Bz397682P", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bz397682P"):
                opp_val = getattr(value, "Bz397682P", None)
                setattr(value, "Bz397682P", self)

    @property
    def Bz397682C(self):
        return self.__Bz397682C

    @Bz397682C.setter
    def Bz397682C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz397682C__Bz397682C", None)
        self.__Bz397682C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refToP"):
                opp_val = getattr(old_value, "refToP", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refToP"):
                opp_val = getattr(value, "refToP", None)
                if opp_val is None:
                    setattr(value, "refToP", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HibernateTest_Bz380987_Place:

    def __init__(self, name: str, places: set["HibernateTest_Bz380987_Person"] = None, Bz380987_Place: "HibernateTest_Bz380987_Person" = None):
        self.name = name
        self.places = places if places is not None else set()
        self.Bz380987_Place = Bz380987_Place
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Bz380987_Place(self):
        return self.__Bz380987_Place

    @Bz380987_Place.setter
    def Bz380987_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz380987_Place__Bz380987_Place", None)
        self.__Bz380987_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people11"):
                opp_val = getattr(old_value, "people11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people11"):
                opp_val = getattr(value, "people11", None)
                if opp_val is None:
                    setattr(value, "people11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz380987_Place__places", None)
        self.__places = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bz380987_Person8"):
                    opp_val = getattr(item, "Bz380987_Person8", None)
                    
                    if opp_val == self:
                        setattr(item, "Bz380987_Person8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bz380987_Person8"):
                    opp_val = getattr(item, "Bz380987_Person8", None)
                    
                    setattr(item, "Bz380987_Person8", self)
                    

class HibernateTest_Bz380987_Person:

    def __init__(self, name: str, Bz380987_Person: "HibernateTest_Bz380987_Group" = None, Bz380987_Person8: "HibernateTest_Bz380987_Place" = None, people: set["HibernateTest_Bz380987_Group"] = None, people11: set["HibernateTest_Bz380987_Place"] = None):
        self.name = name
        self.Bz380987_Person = Bz380987_Person
        self.Bz380987_Person8 = Bz380987_Person8
        self.people = people if people is not None else set()
        self.people11 = people11 if people11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Bz380987_Person(self):
        return self.__Bz380987_Person

    @Bz380987_Person.setter
    def Bz380987_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz380987_Person__Bz380987_Person", None)
        self.__Bz380987_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                if opp_val is None:
                    setattr(value, "group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Bz380987_Person8(self):
        return self.__Bz380987_Person8

    @Bz380987_Person8.setter
    def Bz380987_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz380987_Person__Bz380987_Person8", None)
        self.__Bz380987_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "places"):
                opp_val = getattr(old_value, "places", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "places"):
                opp_val = getattr(value, "places", None)
                if opp_val is None:
                    setattr(value, "places", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def people11(self):
        return self.__people11

    @people11.setter
    def people11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz380987_Person__people11", None)
        self.__people11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bz380987_Place"):
                    opp_val = getattr(item, "Bz380987_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "Bz380987_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bz380987_Place"):
                    opp_val = getattr(item, "Bz380987_Place", None)
                    
                    setattr(item, "Bz380987_Place", self)
                    

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz380987_Person__people", None)
        self.__people = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bz380987_Group"):
                    opp_val = getattr(item, "Bz380987_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Bz380987_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bz380987_Group"):
                    opp_val = getattr(item, "Bz380987_Group", None)
                    
                    setattr(item, "Bz380987_Group", self)
                    

class HibernateTest_Bz380987_Group:

    pass
class HibernateTest_Bz398057A:

    def __init__(self, dbId: str, refToClassA: set["HibernateTest_Bz398057B"] = None, Bz398057A: "HibernateTest_Bz398057B" = None):
        self.dbId = dbId
        self.refToClassA = refToClassA if refToClassA is not None else set()
        self.Bz398057A = Bz398057A
        
    @property
    def dbId(self) -> str:
        return self.__dbId

    @dbId.setter
    def dbId(self, dbId: str):
        self.__dbId = dbId

    @property
    def Bz398057A(self):
        return self.__Bz398057A

    @Bz398057A.setter
    def Bz398057A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz398057A__Bz398057A", None)
        self.__Bz398057A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "listOfB"):
                opp_val = getattr(old_value, "listOfB", None)
                if opp_val == self:
                    setattr(old_value, "listOfB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "listOfB"):
                opp_val = getattr(value, "listOfB", None)
                setattr(value, "listOfB", self)

    @property
    def refToClassA(self):
        return self.__refToClassA

    @refToClassA.setter
    def refToClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz398057A__refToClassA", None)
        self.__refToClassA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bz398057B"):
                    opp_val = getattr(item, "Bz398057B", None)
                    
                    if opp_val == self:
                        setattr(item, "Bz398057B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bz398057B"):
                    opp_val = getattr(item, "Bz398057B", None)
                    
                    setattr(item, "Bz398057B", self)
                    

class HibernateTest_Bz356181_NonTransient:

    pass
class HibernateTest_Bz356181_Transient:

    pass
class HibernateTest_Bz356181_Main:

    def __init__(self, transient: str, nonTransient: str, HibernateTest_Bz356181_Main: "HibernateTest_Bz356181_Transient" = None, HibernateTest_Bz356181_Main2: "HibernateTest_Bz356181_NonTransient" = None, HibernateTest_Bz356181_Main5: "HibernateTest_Bz356181_NonTransient" = None):
        self.transient = transient
        self.nonTransient = nonTransient
        self.HibernateTest_Bz356181_Main = HibernateTest_Bz356181_Main
        self.HibernateTest_Bz356181_Main2 = HibernateTest_Bz356181_Main2
        self.HibernateTest_Bz356181_Main5 = HibernateTest_Bz356181_Main5
        
    @property
    def nonTransient(self) -> str:
        return self.__nonTransient

    @nonTransient.setter
    def nonTransient(self, nonTransient: str):
        self.__nonTransient = nonTransient

    @property
    def transient(self) -> str:
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient

    @property
    def HibernateTest_Bz356181_Main(self):
        return self.__HibernateTest_Bz356181_Main

    @HibernateTest_Bz356181_Main.setter
    def HibernateTest_Bz356181_Main(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz356181_Main__HibernateTest_Bz356181_Main", None)
        self.__HibernateTest_Bz356181_Main = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HibernateTest_Bz356181_Transient"):
                opp_val = getattr(old_value, "HibernateTest_Bz356181_Transient", None)
                if opp_val == self:
                    setattr(old_value, "HibernateTest_Bz356181_Transient", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HibernateTest_Bz356181_Transient"):
                opp_val = getattr(value, "HibernateTest_Bz356181_Transient", None)
                setattr(value, "HibernateTest_Bz356181_Transient", self)

    @property
    def HibernateTest_Bz356181_Main5(self):
        return self.__HibernateTest_Bz356181_Main5

    @HibernateTest_Bz356181_Main5.setter
    def HibernateTest_Bz356181_Main5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz356181_Main__HibernateTest_Bz356181_Main5", None)
        self.__HibernateTest_Bz356181_Main5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HibernateTest_Bz356181_NonTransient4"):
                opp_val = getattr(old_value, "HibernateTest_Bz356181_NonTransient4", None)
                if opp_val == self:
                    setattr(old_value, "HibernateTest_Bz356181_NonTransient4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HibernateTest_Bz356181_NonTransient4"):
                opp_val = getattr(value, "HibernateTest_Bz356181_NonTransient4", None)
                setattr(value, "HibernateTest_Bz356181_NonTransient4", self)

    @property
    def HibernateTest_Bz356181_Main2(self):
        return self.__HibernateTest_Bz356181_Main2

    @HibernateTest_Bz356181_Main2.setter
    def HibernateTest_Bz356181_Main2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HibernateTest_Bz356181_Main__HibernateTest_Bz356181_Main2", None)
        self.__HibernateTest_Bz356181_Main2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HibernateTest_Bz356181_NonTransient"):
                opp_val = getattr(old_value, "HibernateTest_Bz356181_NonTransient", None)
                if opp_val == self:
                    setattr(old_value, "HibernateTest_Bz356181_NonTransient", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HibernateTest_Bz356181_NonTransient"):
                opp_val = getattr(value, "HibernateTest_Bz356181_NonTransient", None)
                setattr(value, "HibernateTest_Bz356181_NonTransient", self)

class HibernateTest_Bz387752_Main:

    def __init__(self, strUnsettable: str, strSettable: str, enumSettable: str, enumUnsettable: str):
        self.strUnsettable = strUnsettable
        self.strSettable = strSettable
        self.enumSettable = enumSettable
        self.enumUnsettable = enumUnsettable
        
    @property
    def strUnsettable(self) -> str:
        return self.__strUnsettable

    @strUnsettable.setter
    def strUnsettable(self, strUnsettable: str):
        self.__strUnsettable = strUnsettable

    @property
    def strSettable(self) -> str:
        return self.__strSettable

    @strSettable.setter
    def strSettable(self, strSettable: str):
        self.__strSettable = strSettable

    @property
    def enumUnsettable(self) -> str:
        return self.__enumUnsettable

    @enumUnsettable.setter
    def enumUnsettable(self, enumUnsettable: str):
        self.__enumUnsettable = enumUnsettable

    @property
    def enumSettable(self) -> str:
        return self.__enumSettable

    @enumSettable.setter
    def enumSettable(self, enumSettable: str):
        self.__enumSettable = enumSettable
