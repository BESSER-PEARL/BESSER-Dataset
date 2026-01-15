from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConstraintType(Enum):
    Undefined = "Undefined"
    NotAllowed = "NotAllowed"
    GlobalIncoming = "GlobalIncoming"
    LocalIncoming = "LocalIncoming"
    GlobalOutgoing = "GlobalOutgoing"
    LocalOutgoing = "LocalOutgoing"
    Expected = "Expected"


############################################
# Definition of Classes
############################################

class Ensemble:

    pass
class datamodel_ConcreteEnsemble(Ensemble):

    pass
class datamodel_EmptyEnsemble(Ensemble):

    pass
class datamodel_TreeNode(ABC):

    pass
class datamodel_Slice:

    def __init__(self, diagram: str, name: str, Slice9: "datamodel_SliceRepository" = None, Slice: "datamodel_Ensemble" = None, datamodel_Slice: set["datamodel_Constraint"] = None, slices: set["datamodel_Ensemble"] = None, slices16: "datamodel_SliceRepository" = None):
        self.diagram = diagram
        self.name = name
        self.Slice9 = Slice9
        self.Slice = Slice
        self.datamodel_Slice = datamodel_Slice if datamodel_Slice is not None else set()
        self.slices = slices if slices is not None else set()
        self.slices16 = slices16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagram(self) -> str:
        return self.__diagram

    @diagram.setter
    def diagram(self, diagram: str):
        self.__diagram = diagram

    @property
    def Slice9(self):
        return self.__Slice9

    @Slice9.setter
    def Slice9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Slice__Slice9", None)
        self.__Slice9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sliceRepository"):
                opp_val = getattr(old_value, "sliceRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sliceRepository"):
                opp_val = getattr(value, "sliceRepository", None)
                if opp_val is None:
                    setattr(value, "sliceRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Slice(self):
        return self.__Slice

    @Slice.setter
    def Slice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Slice__Slice", None)
        self.__Slice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ensembles"):
                opp_val = getattr(old_value, "ensembles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ensembles"):
                opp_val = getattr(value, "ensembles", None)
                if opp_val is None:
                    setattr(value, "ensembles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datamodel_Slice(self):
        return self.__datamodel_Slice

    @datamodel_Slice.setter
    def datamodel_Slice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Slice__datamodel_Slice", None)
        self.__datamodel_Slice = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datamodel_Constraint13"):
                    opp_val = getattr(item, "datamodel_Constraint13", None)
                    
                    if opp_val == self:
                        setattr(item, "datamodel_Constraint13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datamodel_Constraint13"):
                    opp_val = getattr(item, "datamodel_Constraint13", None)
                    
                    setattr(item, "datamodel_Constraint13", self)
                    

    @property
    def slices16(self):
        return self.__slices16

    @slices16.setter
    def slices16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Slice__slices16", None)
        self.__slices16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SliceRepository"):
                opp_val = getattr(old_value, "SliceRepository", None)
                if opp_val == self:
                    setattr(old_value, "SliceRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SliceRepository"):
                opp_val = getattr(value, "SliceRepository", None)
                setattr(value, "SliceRepository", self)

    @property
    def slices(self):
        return self.__slices

    @slices.setter
    def slices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Slice__slices", None)
        self.__slices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ensemble"):
                    opp_val = getattr(item, "Ensemble", None)
                    
                    if opp_val == self:
                        setattr(item, "Ensemble", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ensemble"):
                    opp_val = getattr(item, "Ensemble", None)
                    
                    setattr(item, "Ensemble", self)
                    

class datamodel_SliceRepository:

    pass
class datamodel_Constraint:

    def __init__(self, dependencyKind: str, constraintType: str, datamodel_Constraint: "datamodel_Ensemble" = None, datamodel_Constraint3: "datamodel_Ensemble" = None, datamodel_Constraint6: "datamodel_Ensemble" = None, datamodel_Constraint13: "datamodel_Slice" = None):
        self.dependencyKind = dependencyKind
        self.constraintType = constraintType
        self.datamodel_Constraint = datamodel_Constraint
        self.datamodel_Constraint3 = datamodel_Constraint3
        self.datamodel_Constraint6 = datamodel_Constraint6
        self.datamodel_Constraint13 = datamodel_Constraint13
        
    @property
    def constraintType(self) -> str:
        return self.__constraintType

    @constraintType.setter
    def constraintType(self, constraintType: str):
        self.__constraintType = constraintType

    @property
    def dependencyKind(self) -> str:
        return self.__dependencyKind

    @dependencyKind.setter
    def dependencyKind(self, dependencyKind: str):
        self.__dependencyKind = dependencyKind

    @property
    def datamodel_Constraint13(self):
        return self.__datamodel_Constraint13

    @datamodel_Constraint13.setter
    def datamodel_Constraint13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Constraint__datamodel_Constraint13", None)
        self.__datamodel_Constraint13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_Slice"):
                opp_val = getattr(old_value, "datamodel_Slice", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_Slice"):
                opp_val = getattr(value, "datamodel_Slice", None)
                if opp_val is None:
                    setattr(value, "datamodel_Slice", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datamodel_Constraint(self):
        return self.__datamodel_Constraint

    @datamodel_Constraint.setter
    def datamodel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Constraint__datamodel_Constraint", None)
        self.__datamodel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_Ensemble"):
                opp_val = getattr(old_value, "datamodel_Ensemble", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_Ensemble"):
                opp_val = getattr(value, "datamodel_Ensemble", None)
                if opp_val is None:
                    setattr(value, "datamodel_Ensemble", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datamodel_Constraint6(self):
        return self.__datamodel_Constraint6

    @datamodel_Constraint6.setter
    def datamodel_Constraint6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Constraint__datamodel_Constraint6", None)
        self.__datamodel_Constraint6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_Ensemble7"):
                opp_val = getattr(old_value, "datamodel_Ensemble7", None)
                if opp_val == self:
                    setattr(old_value, "datamodel_Ensemble7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_Ensemble7"):
                opp_val = getattr(value, "datamodel_Ensemble7", None)
                setattr(value, "datamodel_Ensemble7", self)

    @property
    def datamodel_Constraint3(self):
        return self.__datamodel_Constraint3

    @datamodel_Constraint3.setter
    def datamodel_Constraint3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Constraint__datamodel_Constraint3", None)
        self.__datamodel_Constraint3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_Ensemble4"):
                opp_val = getattr(old_value, "datamodel_Ensemble4", None)
                if opp_val == self:
                    setattr(old_value, "datamodel_Ensemble4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_Ensemble4"):
                opp_val = getattr(value, "datamodel_Ensemble4", None)
                setattr(value, "datamodel_Ensemble4", self)

class TreeNode:

    pass
class datamodel_EnsembleRepository(TreeNode):

    pass
class datamodel_Ensemble(TreeNode):

    def __init__(self, name: str, derived: bool, description: str, query: str, datamodel_Ensemble: set["datamodel_Constraint"] = None, datamodel_Ensemble4: "datamodel_Constraint" = None, datamodel_Ensemble7: "datamodel_Constraint" = None, ensembles: set["datamodel_Slice"] = None, Ensemble: "datamodel_Slice" = None, datamodel_Ensemble11: "datamodel_SliceRepository" = None):
        self.name = name
        self.derived = derived
        self.description = description
        self.query = query
        self.datamodel_Ensemble = datamodel_Ensemble if datamodel_Ensemble is not None else set()
        self.datamodel_Ensemble4 = datamodel_Ensemble4
        self.datamodel_Ensemble7 = datamodel_Ensemble7
        self.ensembles = ensembles if ensembles is not None else set()
        self.Ensemble = Ensemble
        self.datamodel_Ensemble11 = datamodel_Ensemble11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def datamodel_Ensemble(self):
        return self.__datamodel_Ensemble

    @datamodel_Ensemble.setter
    def datamodel_Ensemble(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Ensemble__datamodel_Ensemble", None)
        self.__datamodel_Ensemble = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datamodel_Constraint"):
                    opp_val = getattr(item, "datamodel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "datamodel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datamodel_Constraint"):
                    opp_val = getattr(item, "datamodel_Constraint", None)
                    
                    setattr(item, "datamodel_Constraint", self)
                    

    @property
    def ensembles(self):
        return self.__ensembles

    @ensembles.setter
    def ensembles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Ensemble__ensembles", None)
        self.__ensembles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Slice"):
                    opp_val = getattr(item, "Slice", None)
                    
                    if opp_val == self:
                        setattr(item, "Slice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Slice"):
                    opp_val = getattr(item, "Slice", None)
                    
                    setattr(item, "Slice", self)
                    

    @property
    def datamodel_Ensemble4(self):
        return self.__datamodel_Ensemble4

    @datamodel_Ensemble4.setter
    def datamodel_Ensemble4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Ensemble__datamodel_Ensemble4", None)
        self.__datamodel_Ensemble4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_Constraint3"):
                opp_val = getattr(old_value, "datamodel_Constraint3", None)
                if opp_val == self:
                    setattr(old_value, "datamodel_Constraint3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_Constraint3"):
                opp_val = getattr(value, "datamodel_Constraint3", None)
                setattr(value, "datamodel_Constraint3", self)

    @property
    def datamodel_Ensemble7(self):
        return self.__datamodel_Ensemble7

    @datamodel_Ensemble7.setter
    def datamodel_Ensemble7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Ensemble__datamodel_Ensemble7", None)
        self.__datamodel_Ensemble7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_Constraint6"):
                opp_val = getattr(old_value, "datamodel_Constraint6", None)
                if opp_val == self:
                    setattr(old_value, "datamodel_Constraint6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_Constraint6"):
                opp_val = getattr(value, "datamodel_Constraint6", None)
                setattr(value, "datamodel_Constraint6", self)

    @property
    def Ensemble(self):
        return self.__Ensemble

    @Ensemble.setter
    def Ensemble(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Ensemble__Ensemble", None)
        self.__Ensemble = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slices"):
                opp_val = getattr(old_value, "slices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slices"):
                opp_val = getattr(value, "slices", None)
                if opp_val is None:
                    setattr(value, "slices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datamodel_Ensemble11(self):
        return self.__datamodel_Ensemble11

    @datamodel_Ensemble11.setter
    def datamodel_Ensemble11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datamodel_Ensemble__datamodel_Ensemble11", None)
        self.__datamodel_Ensemble11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datamodel_SliceRepository"):
                opp_val = getattr(old_value, "datamodel_SliceRepository", None)
                if opp_val == self:
                    setattr(old_value, "datamodel_SliceRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datamodel_SliceRepository"):
                opp_val = getattr(value, "datamodel_SliceRepository", None)
                setattr(value, "datamodel_SliceRepository", self)
