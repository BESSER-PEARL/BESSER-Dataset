from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnumModular(Enum):
    Default = "Default"
    Project = "Project"
    Package = "Package"
    Unit = "Unit"
    InsideUnit = "InsideUnit"
    InsidePackage = "InsidePackage"
    InsideProject = "InsideProject"
    AbstractPackageUnit = "AbstractPackageUnit"
    AbstractPackage = "AbstractPackage"
    AbstractUnit = "AbstractUnit"
    RecursionPackage = "RecursionPackage"
    RecursionAbstractPackage = "RecursionAbstractPackage"
    RecursionUnit = "RecursionUnit"
    RecursionAbstractUnit = "RecursionAbstractUnit"


############################################
# Definition of Classes
############################################

class MetaModelGraph_EReference:

    pass
class Relation:

    pass
class MetaModelGraph_EAttribute:

    pass
class MetaModelGraph_Composition(Relation):

    pass
class MetaModelGraph_SubClass(Relation):

    pass
class MetaModelGraph_Reference(Relation):

    pass
class MetaModelGraph_Relation(ABC):

    pass
class MetaModelGraph_Node:

    def __init__(self, enumModularNotation: str, icon: str, extension: str, insideRecursion: bool, MetaModelGraph_Node15: "MetaModelGraph_SubGraph" = None, MetaModelGraph_Node: "MetaModelGraph_SubGraph" = None, MetaModelGraph_Node18: set["MetaModelGraph_Reference"] = None, MetaModelGraph_Node20: set["MetaModelGraph_SubClass"] = None, MetaModelGraph_Node22: "MetaModelGraph_EClass" = None, target: set["MetaModelGraph_Relation"] = None, MetaModelGraph_Node27: "MetaModelGraph_Node" = None, MetaModelGraph_Node25: set["MetaModelGraph_Node"] = None, MetaModelGraph_Node29: set["MetaModelGraph_SubClass"] = None, parentNode: set["MetaModelGraph_Composition"] = None, MetaModelGraph_Node34: "MetaModelGraph_EAttribute" = None, Node: "MetaModelGraph_Relation" = None, Node39: "MetaModelGraph_Composition" = None, MetaModelGraph_Node32: set["MetaModelGraph_Composition"] = None):
        self.enumModularNotation = enumModularNotation
        self.icon = icon
        self.extension = extension
        self.insideRecursion = insideRecursion
        self.MetaModelGraph_Node15 = MetaModelGraph_Node15
        self.MetaModelGraph_Node = MetaModelGraph_Node
        self.MetaModelGraph_Node18 = MetaModelGraph_Node18 if MetaModelGraph_Node18 is not None else set()
        self.MetaModelGraph_Node20 = MetaModelGraph_Node20 if MetaModelGraph_Node20 is not None else set()
        self.MetaModelGraph_Node22 = MetaModelGraph_Node22
        self.target = target if target is not None else set()
        self.MetaModelGraph_Node27 = MetaModelGraph_Node27
        self.MetaModelGraph_Node25 = MetaModelGraph_Node25 if MetaModelGraph_Node25 is not None else set()
        self.MetaModelGraph_Node29 = MetaModelGraph_Node29 if MetaModelGraph_Node29 is not None else set()
        self.parentNode = parentNode if parentNode is not None else set()
        self.MetaModelGraph_Node34 = MetaModelGraph_Node34
        self.Node = Node
        self.Node39 = Node39
        self.MetaModelGraph_Node32 = MetaModelGraph_Node32 if MetaModelGraph_Node32 is not None else set()
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def enumModularNotation(self) -> str:
        return self.__enumModularNotation

    @enumModularNotation.setter
    def enumModularNotation(self, enumModularNotation: str):
        self.__enumModularNotation = enumModularNotation

    @property
    def insideRecursion(self) -> bool:
        return self.__insideRecursion

    @insideRecursion.setter
    def insideRecursion(self, insideRecursion: bool):
        self.__insideRecursion = insideRecursion

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def MetaModelGraph_Node29(self):
        return self.__MetaModelGraph_Node29

    @MetaModelGraph_Node29.setter
    def MetaModelGraph_Node29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node29", None)
        self.__MetaModelGraph_Node29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_SubClass30"):
                    opp_val = getattr(item, "MetaModelGraph_SubClass30", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_SubClass30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_SubClass30"):
                    opp_val = getattr(item, "MetaModelGraph_SubClass30", None)
                    
                    setattr(item, "MetaModelGraph_SubClass30", self)
                    

    @property
    def MetaModelGraph_Node32(self):
        return self.__MetaModelGraph_Node32

    @MetaModelGraph_Node32.setter
    def MetaModelGraph_Node32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node32", None)
        self.__MetaModelGraph_Node32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_Composition"):
                    opp_val = getattr(item, "MetaModelGraph_Composition", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_Composition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_Composition"):
                    opp_val = getattr(item, "MetaModelGraph_Composition", None)
                    
                    setattr(item, "MetaModelGraph_Composition", self)
                    

    @property
    def MetaModelGraph_Node18(self):
        return self.__MetaModelGraph_Node18

    @MetaModelGraph_Node18.setter
    def MetaModelGraph_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node18", None)
        self.__MetaModelGraph_Node18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_Reference"):
                    opp_val = getattr(item, "MetaModelGraph_Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_Reference"):
                    opp_val = getattr(item, "MetaModelGraph_Reference", None)
                    
                    setattr(item, "MetaModelGraph_Reference", self)
                    

    @property
    def MetaModelGraph_Node15(self):
        return self.__MetaModelGraph_Node15

    @MetaModelGraph_Node15.setter
    def MetaModelGraph_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node15", None)
        self.__MetaModelGraph_Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_SubGraph14"):
                opp_val = getattr(old_value, "MetaModelGraph_SubGraph14", None)
                if opp_val == self:
                    setattr(old_value, "MetaModelGraph_SubGraph14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_SubGraph14"):
                opp_val = getattr(value, "MetaModelGraph_SubGraph14", None)
                setattr(value, "MetaModelGraph_SubGraph14", self)

    @property
    def MetaModelGraph_Node(self):
        return self.__MetaModelGraph_Node

    @MetaModelGraph_Node.setter
    def MetaModelGraph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node", None)
        self.__MetaModelGraph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_SubGraph7"):
                opp_val = getattr(old_value, "MetaModelGraph_SubGraph7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_SubGraph7"):
                opp_val = getattr(value, "MetaModelGraph_SubGraph7", None)
                if opp_val is None:
                    setattr(value, "MetaModelGraph_SubGraph7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node39(self):
        return self.__Node39

    @Node39.setter
    def Node39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__Node39", None)
        self.__Node39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compositions"):
                opp_val = getattr(old_value, "compositions", None)
                if opp_val == self:
                    setattr(old_value, "compositions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compositions"):
                opp_val = getattr(value, "compositions", None)
                setattr(value, "compositions", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    setattr(item, "Relation", self)
                    

    @property
    def MetaModelGraph_Node20(self):
        return self.__MetaModelGraph_Node20

    @MetaModelGraph_Node20.setter
    def MetaModelGraph_Node20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node20", None)
        self.__MetaModelGraph_Node20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_SubClass"):
                    opp_val = getattr(item, "MetaModelGraph_SubClass", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_SubClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_SubClass"):
                    opp_val = getattr(item, "MetaModelGraph_SubClass", None)
                    
                    setattr(item, "MetaModelGraph_SubClass", self)
                    

    @property
    def MetaModelGraph_Node34(self):
        return self.__MetaModelGraph_Node34

    @MetaModelGraph_Node34.setter
    def MetaModelGraph_Node34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node34", None)
        self.__MetaModelGraph_Node34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_EAttribute"):
                opp_val = getattr(old_value, "MetaModelGraph_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "MetaModelGraph_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_EAttribute"):
                opp_val = getattr(value, "MetaModelGraph_EAttribute", None)
                setattr(value, "MetaModelGraph_EAttribute", self)

    @property
    def MetaModelGraph_Node22(self):
        return self.__MetaModelGraph_Node22

    @MetaModelGraph_Node22.setter
    def MetaModelGraph_Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node22", None)
        self.__MetaModelGraph_Node22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_EClass23"):
                opp_val = getattr(old_value, "MetaModelGraph_EClass23", None)
                if opp_val == self:
                    setattr(old_value, "MetaModelGraph_EClass23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_EClass23"):
                opp_val = getattr(value, "MetaModelGraph_EClass23", None)
                setattr(value, "MetaModelGraph_EClass23", self)

    @property
    def MetaModelGraph_Node25(self):
        return self.__MetaModelGraph_Node25

    @MetaModelGraph_Node25.setter
    def MetaModelGraph_Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node25", None)
        self.__MetaModelGraph_Node25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_Node27"):
                    opp_val = getattr(item, "MetaModelGraph_Node27", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_Node27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_Node27"):
                    opp_val = getattr(item, "MetaModelGraph_Node27", None)
                    
                    setattr(item, "MetaModelGraph_Node27", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relations"):
                opp_val = getattr(old_value, "relations", None)
                if opp_val == self:
                    setattr(old_value, "relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relations"):
                opp_val = getattr(value, "relations", None)
                setattr(value, "relations", self)

    @property
    def parentNode(self):
        return self.__parentNode

    @parentNode.setter
    def parentNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__parentNode", None)
        self.__parentNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Composition"):
                    opp_val = getattr(item, "Composition", None)
                    
                    if opp_val == self:
                        setattr(item, "Composition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Composition"):
                    opp_val = getattr(item, "Composition", None)
                    
                    setattr(item, "Composition", self)
                    

    @property
    def MetaModelGraph_Node27(self):
        return self.__MetaModelGraph_Node27

    @MetaModelGraph_Node27.setter
    def MetaModelGraph_Node27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Node__MetaModelGraph_Node27", None)
        self.__MetaModelGraph_Node27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_Node25"):
                opp_val = getattr(old_value, "MetaModelGraph_Node25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_Node25"):
                opp_val = getattr(value, "MetaModelGraph_Node25", None)
                if opp_val is None:
                    setattr(value, "MetaModelGraph_Node25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MetaModelGraph_EClass:

    pass
class MetaModelGraph_SubGraph:

    def __init__(self, height: int, amountOfConcreteEClass: int, amountEClassesOut: int, amountOfAbstractEClass: int, amountOfParentEClass: int, amountOfParentAbstractEClass: int, amountPackages: int, amountUnits: int, amountRecursionUnits: int, amountOfRecursionPackages: int, MetaModelGraph_SubGraph: "MetaModelGraph_Graph" = None, MetaModelGraph_SubGraph9: set["MetaModelGraph_Relation"] = None, MetaModelGraph_SubGraph11: set["MetaModelGraph_EClass"] = None, MetaModelGraph_SubGraph14: "MetaModelGraph_Node" = None, MetaModelGraph_SubGraph7: set["MetaModelGraph_Node"] = None):
        self.height = height
        self.amountOfConcreteEClass = amountOfConcreteEClass
        self.amountEClassesOut = amountEClassesOut
        self.amountOfAbstractEClass = amountOfAbstractEClass
        self.amountOfParentEClass = amountOfParentEClass
        self.amountOfParentAbstractEClass = amountOfParentAbstractEClass
        self.amountPackages = amountPackages
        self.amountUnits = amountUnits
        self.amountRecursionUnits = amountRecursionUnits
        self.amountOfRecursionPackages = amountOfRecursionPackages
        self.MetaModelGraph_SubGraph = MetaModelGraph_SubGraph
        self.MetaModelGraph_SubGraph9 = MetaModelGraph_SubGraph9 if MetaModelGraph_SubGraph9 is not None else set()
        self.MetaModelGraph_SubGraph11 = MetaModelGraph_SubGraph11 if MetaModelGraph_SubGraph11 is not None else set()
        self.MetaModelGraph_SubGraph14 = MetaModelGraph_SubGraph14
        self.MetaModelGraph_SubGraph7 = MetaModelGraph_SubGraph7 if MetaModelGraph_SubGraph7 is not None else set()
        
    @property
    def amountOfParentAbstractEClass(self) -> int:
        return self.__amountOfParentAbstractEClass

    @amountOfParentAbstractEClass.setter
    def amountOfParentAbstractEClass(self, amountOfParentAbstractEClass: int):
        self.__amountOfParentAbstractEClass = amountOfParentAbstractEClass

    @property
    def amountOfRecursionPackages(self) -> int:
        return self.__amountOfRecursionPackages

    @amountOfRecursionPackages.setter
    def amountOfRecursionPackages(self, amountOfRecursionPackages: int):
        self.__amountOfRecursionPackages = amountOfRecursionPackages

    @property
    def amountOfAbstractEClass(self) -> int:
        return self.__amountOfAbstractEClass

    @amountOfAbstractEClass.setter
    def amountOfAbstractEClass(self, amountOfAbstractEClass: int):
        self.__amountOfAbstractEClass = amountOfAbstractEClass

    @property
    def amountOfParentEClass(self) -> int:
        return self.__amountOfParentEClass

    @amountOfParentEClass.setter
    def amountOfParentEClass(self, amountOfParentEClass: int):
        self.__amountOfParentEClass = amountOfParentEClass

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def amountEClassesOut(self) -> int:
        return self.__amountEClassesOut

    @amountEClassesOut.setter
    def amountEClassesOut(self, amountEClassesOut: int):
        self.__amountEClassesOut = amountEClassesOut

    @property
    def amountOfConcreteEClass(self) -> int:
        return self.__amountOfConcreteEClass

    @amountOfConcreteEClass.setter
    def amountOfConcreteEClass(self, amountOfConcreteEClass: int):
        self.__amountOfConcreteEClass = amountOfConcreteEClass

    @property
    def amountUnits(self) -> int:
        return self.__amountUnits

    @amountUnits.setter
    def amountUnits(self, amountUnits: int):
        self.__amountUnits = amountUnits

    @property
    def amountRecursionUnits(self) -> int:
        return self.__amountRecursionUnits

    @amountRecursionUnits.setter
    def amountRecursionUnits(self, amountRecursionUnits: int):
        self.__amountRecursionUnits = amountRecursionUnits

    @property
    def amountPackages(self) -> int:
        return self.__amountPackages

    @amountPackages.setter
    def amountPackages(self, amountPackages: int):
        self.__amountPackages = amountPackages

    @property
    def MetaModelGraph_SubGraph14(self):
        return self.__MetaModelGraph_SubGraph14

    @MetaModelGraph_SubGraph14.setter
    def MetaModelGraph_SubGraph14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_SubGraph__MetaModelGraph_SubGraph14", None)
        self.__MetaModelGraph_SubGraph14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_Node15"):
                opp_val = getattr(old_value, "MetaModelGraph_Node15", None)
                if opp_val == self:
                    setattr(old_value, "MetaModelGraph_Node15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_Node15"):
                opp_val = getattr(value, "MetaModelGraph_Node15", None)
                setattr(value, "MetaModelGraph_Node15", self)

    @property
    def MetaModelGraph_SubGraph9(self):
        return self.__MetaModelGraph_SubGraph9

    @MetaModelGraph_SubGraph9.setter
    def MetaModelGraph_SubGraph9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_SubGraph__MetaModelGraph_SubGraph9", None)
        self.__MetaModelGraph_SubGraph9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_Relation"):
                    opp_val = getattr(item, "MetaModelGraph_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_Relation"):
                    opp_val = getattr(item, "MetaModelGraph_Relation", None)
                    
                    setattr(item, "MetaModelGraph_Relation", self)
                    

    @property
    def MetaModelGraph_SubGraph7(self):
        return self.__MetaModelGraph_SubGraph7

    @MetaModelGraph_SubGraph7.setter
    def MetaModelGraph_SubGraph7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_SubGraph__MetaModelGraph_SubGraph7", None)
        self.__MetaModelGraph_SubGraph7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_Node"):
                    opp_val = getattr(item, "MetaModelGraph_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_Node"):
                    opp_val = getattr(item, "MetaModelGraph_Node", None)
                    
                    setattr(item, "MetaModelGraph_Node", self)
                    

    @property
    def MetaModelGraph_SubGraph11(self):
        return self.__MetaModelGraph_SubGraph11

    @MetaModelGraph_SubGraph11.setter
    def MetaModelGraph_SubGraph11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_SubGraph__MetaModelGraph_SubGraph11", None)
        self.__MetaModelGraph_SubGraph11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_EClass12"):
                    opp_val = getattr(item, "MetaModelGraph_EClass12", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_EClass12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_EClass12"):
                    opp_val = getattr(item, "MetaModelGraph_EClass12", None)
                    
                    setattr(item, "MetaModelGraph_EClass12", self)
                    

    @property
    def MetaModelGraph_SubGraph(self):
        return self.__MetaModelGraph_SubGraph

    @MetaModelGraph_SubGraph.setter
    def MetaModelGraph_SubGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_SubGraph__MetaModelGraph_SubGraph", None)
        self.__MetaModelGraph_SubGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModelGraph_Graph"):
                opp_val = getattr(old_value, "MetaModelGraph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModelGraph_Graph"):
                opp_val = getattr(value, "MetaModelGraph_Graph", None)
                if opp_val is None:
                    setattr(value, "MetaModelGraph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MetaModelGraph_Graph:

    def __init__(self, amountEClasses: int, amountAbstractEClasses: int, amountConcreteEClass: int, MetaModelGraph_Graph: set["MetaModelGraph_SubGraph"] = None, MetaModelGraph_Graph2: set["MetaModelGraph_EClass"] = None, MetaModelGraph_Graph4: set["MetaModelGraph_EClass"] = None):
        self.amountEClasses = amountEClasses
        self.amountAbstractEClasses = amountAbstractEClasses
        self.amountConcreteEClass = amountConcreteEClass
        self.MetaModelGraph_Graph = MetaModelGraph_Graph if MetaModelGraph_Graph is not None else set()
        self.MetaModelGraph_Graph2 = MetaModelGraph_Graph2 if MetaModelGraph_Graph2 is not None else set()
        self.MetaModelGraph_Graph4 = MetaModelGraph_Graph4 if MetaModelGraph_Graph4 is not None else set()
        
    @property
    def amountEClasses(self) -> int:
        return self.__amountEClasses

    @amountEClasses.setter
    def amountEClasses(self, amountEClasses: int):
        self.__amountEClasses = amountEClasses

    @property
    def amountConcreteEClass(self) -> int:
        return self.__amountConcreteEClass

    @amountConcreteEClass.setter
    def amountConcreteEClass(self, amountConcreteEClass: int):
        self.__amountConcreteEClass = amountConcreteEClass

    @property
    def amountAbstractEClasses(self) -> int:
        return self.__amountAbstractEClasses

    @amountAbstractEClasses.setter
    def amountAbstractEClasses(self, amountAbstractEClasses: int):
        self.__amountAbstractEClasses = amountAbstractEClasses

    @property
    def MetaModelGraph_Graph4(self):
        return self.__MetaModelGraph_Graph4

    @MetaModelGraph_Graph4.setter
    def MetaModelGraph_Graph4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Graph__MetaModelGraph_Graph4", None)
        self.__MetaModelGraph_Graph4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_EClass5"):
                    opp_val = getattr(item, "MetaModelGraph_EClass5", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_EClass5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_EClass5"):
                    opp_val = getattr(item, "MetaModelGraph_EClass5", None)
                    
                    setattr(item, "MetaModelGraph_EClass5", self)
                    

    @property
    def MetaModelGraph_Graph2(self):
        return self.__MetaModelGraph_Graph2

    @MetaModelGraph_Graph2.setter
    def MetaModelGraph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Graph__MetaModelGraph_Graph2", None)
        self.__MetaModelGraph_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_EClass"):
                    opp_val = getattr(item, "MetaModelGraph_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_EClass"):
                    opp_val = getattr(item, "MetaModelGraph_EClass", None)
                    
                    setattr(item, "MetaModelGraph_EClass", self)
                    

    @property
    def MetaModelGraph_Graph(self):
        return self.__MetaModelGraph_Graph

    @MetaModelGraph_Graph.setter
    def MetaModelGraph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModelGraph_Graph__MetaModelGraph_Graph", None)
        self.__MetaModelGraph_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModelGraph_SubGraph"):
                    opp_val = getattr(item, "MetaModelGraph_SubGraph", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModelGraph_SubGraph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModelGraph_SubGraph"):
                    opp_val = getattr(item, "MetaModelGraph_SubGraph", None)
                    
                    setattr(item, "MetaModelGraph_SubGraph", self)
                    
