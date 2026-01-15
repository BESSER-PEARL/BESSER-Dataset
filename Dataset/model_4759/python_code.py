from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionDomain(Enum):
    time = "time"
    space = "space"
    form = "form"


############################################
# Definition of Classes
############################################

class effbdpattern_Force:

    def __init__(self, value: int, scale: int, description: str, Force: "effbdpattern_Problem" = None, forces: "effbdpattern_Problem" = None, effbdpattern_Force: "effbdpattern_Condition" = None):
        self.value = value
        self.scale = scale
        self.description = description
        self.Force = Force
        self.forces = forces
        self.effbdpattern_Force = effbdpattern_Force
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def forces(self):
        return self.__forces

    @forces.setter
    def forces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Force__forces", None)
        self.__forces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Problem"):
                opp_val = getattr(old_value, "Problem", None)
                if opp_val == self:
                    setattr(old_value, "Problem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Problem"):
                opp_val = getattr(value, "Problem", None)
                setattr(value, "Problem", self)

    @property
    def effbdpattern_Force(self):
        return self.__effbdpattern_Force

    @effbdpattern_Force.setter
    def effbdpattern_Force(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Force__effbdpattern_Force", None)
        self.__effbdpattern_Force = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Condition89"):
                opp_val = getattr(old_value, "effbdpattern_Condition89", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Condition89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Condition89"):
                opp_val = getattr(value, "effbdpattern_Condition89", None)
                setattr(value, "effbdpattern_Condition89", self)

    @property
    def Force(self):
        return self.__Force

    @Force.setter
    def Force(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Force__Force", None)
        self.__Force = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "problem"):
                opp_val = getattr(old_value, "problem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "problem"):
                opp_val = getattr(value, "problem", None)
                if opp_val is None:
                    setattr(value, "problem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Impact:

    def __init__(self, value: int, scale: int, effbdpattern_Impact: "effbdpattern_Feature" = None, impacts: "effbdpattern_SystemPattern" = None, Impact: "effbdpattern_SystemPattern" = None):
        self.value = value
        self.scale = scale
        self.effbdpattern_Impact = effbdpattern_Impact
        self.impacts = impacts
        self.Impact = Impact
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def effbdpattern_Impact(self):
        return self.__effbdpattern_Impact

    @effbdpattern_Impact.setter
    def effbdpattern_Impact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Impact__effbdpattern_Impact", None)
        self.__effbdpattern_Impact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Feature98"):
                opp_val = getattr(old_value, "effbdpattern_Feature98", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Feature98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Feature98"):
                opp_val = getattr(value, "effbdpattern_Feature98", None)
                setattr(value, "effbdpattern_Feature98", self)

    @property
    def Impact(self):
        return self.__Impact

    @Impact.setter
    def Impact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Impact__Impact", None)
        self.__Impact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern"):
                opp_val = getattr(old_value, "pattern", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern"):
                opp_val = getattr(value, "pattern", None)
                if opp_val is None:
                    setattr(value, "pattern", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def impacts(self):
        return self.__impacts

    @impacts.setter
    def impacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Impact__impacts", None)
        self.__impacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SystemPattern100"):
                opp_val = getattr(old_value, "SystemPattern100", None)
                if opp_val == self:
                    setattr(old_value, "SystemPattern100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemPattern100"):
                opp_val = getattr(value, "SystemPattern100", None)
                setattr(value, "SystemPattern100", self)

class AbstractModel:

    pass
class effbdpattern_PatternModel(AbstractModel):

    pass
class effbdpattern_Parameter:

    def __init__(self, name: str, effbdpattern_Parameter: "effbdpattern_ModelElement" = None, effbdpattern_Parameter63: "effbdpattern_ModelElement" = None, effbdpattern_Parameter103: "effbdpattern_SystemPattern" = None):
        self.name = name
        self.effbdpattern_Parameter = effbdpattern_Parameter
        self.effbdpattern_Parameter63 = effbdpattern_Parameter63
        self.effbdpattern_Parameter103 = effbdpattern_Parameter103
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbdpattern_Parameter103(self):
        return self.__effbdpattern_Parameter103

    @effbdpattern_Parameter103.setter
    def effbdpattern_Parameter103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Parameter__effbdpattern_Parameter103", None)
        self.__effbdpattern_Parameter103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern102"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern102"):
                opp_val = getattr(value, "effbdpattern_SystemPattern102", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_SystemPattern102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Parameter(self):
        return self.__effbdpattern_Parameter

    @effbdpattern_Parameter.setter
    def effbdpattern_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Parameter__effbdpattern_Parameter", None)
        self.__effbdpattern_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_ModelElement"):
                opp_val = getattr(old_value, "effbdpattern_ModelElement", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_ModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_ModelElement"):
                opp_val = getattr(value, "effbdpattern_ModelElement", None)
                setattr(value, "effbdpattern_ModelElement", self)

    @property
    def effbdpattern_Parameter63(self):
        return self.__effbdpattern_Parameter63

    @effbdpattern_Parameter63.setter
    def effbdpattern_Parameter63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Parameter__effbdpattern_Parameter63", None)
        self.__effbdpattern_Parameter63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_ModelElement64"):
                opp_val = getattr(old_value, "effbdpattern_ModelElement64", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_ModelElement64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_ModelElement64"):
                opp_val = getattr(value, "effbdpattern_ModelElement64", None)
                setattr(value, "effbdpattern_ModelElement64", self)

class Indexable:

    pass
class effbdpattern_AbstractModel(Indexable):

    def __init__(self, name: str, version: str, effbdpattern_AbstractModel: "effbdpattern_Domain" = None, AbstractModel: "effbdpattern_AbstractModel" = None, fragments: "effbdpattern_AbstractModel" = None, AbstractModel86: "effbdpattern_AbstractModel" = None, parent85: set["effbdpattern_AbstractModel"] = None):
        self.name = name
        self.version = version
        self.effbdpattern_AbstractModel = effbdpattern_AbstractModel
        self.AbstractModel = AbstractModel
        self.fragments = fragments
        self.AbstractModel86 = AbstractModel86
        self.parent85 = parent85 if parent85 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def AbstractModel(self):
        return self.__AbstractModel

    @AbstractModel.setter
    def AbstractModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_AbstractModel__AbstractModel", None)
        self.__AbstractModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragments"):
                opp_val = getattr(old_value, "fragments", None)
                if opp_val == self:
                    setattr(old_value, "fragments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragments"):
                opp_val = getattr(value, "fragments", None)
                setattr(value, "fragments", self)

    @property
    def effbdpattern_AbstractModel(self):
        return self.__effbdpattern_AbstractModel

    @effbdpattern_AbstractModel.setter
    def effbdpattern_AbstractModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_AbstractModel__effbdpattern_AbstractModel", None)
        self.__effbdpattern_AbstractModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Domain80"):
                opp_val = getattr(old_value, "effbdpattern_Domain80", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Domain80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Domain80"):
                opp_val = getattr(value, "effbdpattern_Domain80", None)
                setattr(value, "effbdpattern_Domain80", self)

    @property
    def parent85(self):
        return self.__parent85

    @parent85.setter
    def parent85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_AbstractModel__parent85", None)
        self.__parent85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractModel86"):
                    opp_val = getattr(item, "AbstractModel86", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractModel86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractModel86"):
                    opp_val = getattr(item, "AbstractModel86", None)
                    
                    setattr(item, "AbstractModel86", self)
                    

    @property
    def fragments(self):
        return self.__fragments

    @fragments.setter
    def fragments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_AbstractModel__fragments", None)
        self.__fragments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractModel"):
                opp_val = getattr(old_value, "AbstractModel", None)
                if opp_val == self:
                    setattr(old_value, "AbstractModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractModel"):
                opp_val = getattr(value, "AbstractModel", None)
                setattr(value, "AbstractModel", self)

    @property
    def AbstractModel86(self):
        return self.__AbstractModel86

    @AbstractModel86.setter
    def AbstractModel86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_AbstractModel__AbstractModel86", None)
        self.__AbstractModel86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent85"):
                opp_val = getattr(old_value, "parent85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent85"):
                opp_val = getattr(value, "parent85", None)
                if opp_val is None:
                    setattr(value, "parent85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_ModelElement(Indexable):

    def __init__(self, modelId: int, modelName: str, modelElement: "effbdpattern_SystemPattern" = None, effbdpattern_ModelElement: "effbdpattern_Parameter" = None, effbdpattern_ModelElement64: "effbdpattern_Parameter" = None, ModelElement: "effbdpattern_SystemPattern" = None):
        self.modelId = modelId
        self.modelName = modelName
        self.modelElement = modelElement
        self.effbdpattern_ModelElement = effbdpattern_ModelElement
        self.effbdpattern_ModelElement64 = effbdpattern_ModelElement64
        self.ModelElement = ModelElement
        
    @property
    def modelId(self) -> int:
        return self.__modelId

    @modelId.setter
    def modelId(self, modelId: int):
        self.__modelId = modelId

    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

    @property
    def effbdpattern_ModelElement64(self):
        return self.__effbdpattern_ModelElement64

    @effbdpattern_ModelElement64.setter
    def effbdpattern_ModelElement64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_ModelElement__effbdpattern_ModelElement64", None)
        self.__effbdpattern_ModelElement64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Parameter63"):
                opp_val = getattr(old_value, "effbdpattern_Parameter63", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Parameter63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Parameter63"):
                opp_val = getattr(value, "effbdpattern_Parameter63", None)
                setattr(value, "effbdpattern_Parameter63", self)

    @property
    def ModelElement(self):
        return self.__ModelElement

    @ModelElement.setter
    def ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_ModelElement__ModelElement", None)
        self.__ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern130"):
                opp_val = getattr(old_value, "pattern130", None)
                if opp_val == self:
                    setattr(old_value, "pattern130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern130"):
                opp_val = getattr(value, "pattern130", None)
                setattr(value, "pattern130", self)

    @property
    def effbdpattern_ModelElement(self):
        return self.__effbdpattern_ModelElement

    @effbdpattern_ModelElement.setter
    def effbdpattern_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_ModelElement__effbdpattern_ModelElement", None)
        self.__effbdpattern_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Parameter"):
                opp_val = getattr(old_value, "effbdpattern_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Parameter"):
                opp_val = getattr(value, "effbdpattern_Parameter", None)
                setattr(value, "effbdpattern_Parameter", self)

    @property
    def modelElement(self):
        return self.__modelElement

    @modelElement.setter
    def modelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_ModelElement__modelElement", None)
        self.__modelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SystemPattern"):
                opp_val = getattr(old_value, "SystemPattern", None)
                if opp_val == self:
                    setattr(old_value, "SystemPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemPattern"):
                opp_val = getattr(value, "SystemPattern", None)
                setattr(value, "SystemPattern", self)

class effbdpattern_Allocation:

    def __init__(self, id: str, redundant: bool, effbdpattern_Allocation: "effbdpattern_Workbench" = None, effbdpattern_Allocation141: "effbdpattern_Function" = None, effbdpattern_Allocation144: "effbdpattern_Component" = None):
        self.id = id
        self.redundant = redundant
        self.effbdpattern_Allocation = effbdpattern_Allocation
        self.effbdpattern_Allocation141 = effbdpattern_Allocation141
        self.effbdpattern_Allocation144 = effbdpattern_Allocation144
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def redundant(self) -> bool:
        return self.__redundant

    @redundant.setter
    def redundant(self, redundant: bool):
        self.__redundant = redundant

    @property
    def effbdpattern_Allocation144(self):
        return self.__effbdpattern_Allocation144

    @effbdpattern_Allocation144.setter
    def effbdpattern_Allocation144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Allocation__effbdpattern_Allocation144", None)
        self.__effbdpattern_Allocation144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Component145"):
                opp_val = getattr(old_value, "effbdpattern_Component145", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Component145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Component145"):
                opp_val = getattr(value, "effbdpattern_Component145", None)
                setattr(value, "effbdpattern_Component145", self)

    @property
    def effbdpattern_Allocation(self):
        return self.__effbdpattern_Allocation

    @effbdpattern_Allocation.setter
    def effbdpattern_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Allocation__effbdpattern_Allocation", None)
        self.__effbdpattern_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench57"):
                opp_val = getattr(old_value, "effbdpattern_Workbench57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench57"):
                opp_val = getattr(value, "effbdpattern_Workbench57", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Allocation141(self):
        return self.__effbdpattern_Allocation141

    @effbdpattern_Allocation141.setter
    def effbdpattern_Allocation141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Allocation__effbdpattern_Allocation141", None)
        self.__effbdpattern_Allocation141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Function142"):
                opp_val = getattr(old_value, "effbdpattern_Function142", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Function142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Function142"):
                opp_val = getattr(value, "effbdpattern_Function142", None)
                setattr(value, "effbdpattern_Function142", self)

class effbdpattern_Model(AbstractModel):

    pass
class effbdpattern_Context(Indexable):

    def __init__(self, description: str, effbdpattern_Context: "effbdpattern_Workbench" = None, effbdpattern_Context66: set["effbdpattern_Condition"] = None, effbdpattern_Context106: "effbdpattern_SystemPattern" = None):
        self.description = description
        self.effbdpattern_Context = effbdpattern_Context
        self.effbdpattern_Context66 = effbdpattern_Context66 if effbdpattern_Context66 is not None else set()
        self.effbdpattern_Context106 = effbdpattern_Context106
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def effbdpattern_Context106(self):
        return self.__effbdpattern_Context106

    @effbdpattern_Context106.setter
    def effbdpattern_Context106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Context__effbdpattern_Context106", None)
        self.__effbdpattern_Context106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern105"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern105", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_SystemPattern105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern105"):
                opp_val = getattr(value, "effbdpattern_SystemPattern105", None)
                setattr(value, "effbdpattern_SystemPattern105", self)

    @property
    def effbdpattern_Context66(self):
        return self.__effbdpattern_Context66

    @effbdpattern_Context66.setter
    def effbdpattern_Context66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Context__effbdpattern_Context66", None)
        self.__effbdpattern_Context66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Condition67"):
                    opp_val = getattr(item, "effbdpattern_Condition67", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Condition67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Condition67"):
                    opp_val = getattr(item, "effbdpattern_Condition67", None)
                    
                    setattr(item, "effbdpattern_Condition67", self)
                    

    @property
    def effbdpattern_Context(self):
        return self.__effbdpattern_Context

    @effbdpattern_Context.setter
    def effbdpattern_Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Context__effbdpattern_Context", None)
        self.__effbdpattern_Context = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench50"):
                opp_val = getattr(old_value, "effbdpattern_Workbench50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench50"):
                opp_val = getattr(value, "effbdpattern_Workbench50", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Condition:

    def __init__(self, name: str, effbdpattern_Condition: "effbdpattern_Workbench" = None, effbdpattern_Condition67: "effbdpattern_Context" = None, effbdpattern_Condition89: "effbdpattern_Force" = None):
        self.name = name
        self.effbdpattern_Condition = effbdpattern_Condition
        self.effbdpattern_Condition67 = effbdpattern_Condition67
        self.effbdpattern_Condition89 = effbdpattern_Condition89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbdpattern_Condition67(self):
        return self.__effbdpattern_Condition67

    @effbdpattern_Condition67.setter
    def effbdpattern_Condition67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Condition__effbdpattern_Condition67", None)
        self.__effbdpattern_Condition67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Context66"):
                opp_val = getattr(old_value, "effbdpattern_Context66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Context66"):
                opp_val = getattr(value, "effbdpattern_Context66", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Context66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Condition89(self):
        return self.__effbdpattern_Condition89

    @effbdpattern_Condition89.setter
    def effbdpattern_Condition89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Condition__effbdpattern_Condition89", None)
        self.__effbdpattern_Condition89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Force"):
                opp_val = getattr(old_value, "effbdpattern_Force", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Force", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Force"):
                opp_val = getattr(value, "effbdpattern_Force", None)
                setattr(value, "effbdpattern_Force", self)

    @property
    def effbdpattern_Condition(self):
        return self.__effbdpattern_Condition

    @effbdpattern_Condition.setter
    def effbdpattern_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Condition__effbdpattern_Condition", None)
        self.__effbdpattern_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench48"):
                opp_val = getattr(old_value, "effbdpattern_Workbench48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench48"):
                opp_val = getattr(value, "effbdpattern_Workbench48", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Feature:

    def __init__(self, name: str, description: str, effbdpattern_Feature: "effbdpattern_Workbench" = None, effbdpattern_Feature95: "effbdpattern_Problem" = None, effbdpattern_Feature98: "effbdpattern_Impact" = None):
        self.name = name
        self.description = description
        self.effbdpattern_Feature = effbdpattern_Feature
        self.effbdpattern_Feature95 = effbdpattern_Feature95
        self.effbdpattern_Feature98 = effbdpattern_Feature98
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbdpattern_Feature(self):
        return self.__effbdpattern_Feature

    @effbdpattern_Feature.setter
    def effbdpattern_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Feature__effbdpattern_Feature", None)
        self.__effbdpattern_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench46"):
                opp_val = getattr(old_value, "effbdpattern_Workbench46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench46"):
                opp_val = getattr(value, "effbdpattern_Workbench46", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Feature98(self):
        return self.__effbdpattern_Feature98

    @effbdpattern_Feature98.setter
    def effbdpattern_Feature98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Feature__effbdpattern_Feature98", None)
        self.__effbdpattern_Feature98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Impact"):
                opp_val = getattr(old_value, "effbdpattern_Impact", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Impact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Impact"):
                opp_val = getattr(value, "effbdpattern_Impact", None)
                setattr(value, "effbdpattern_Impact", self)

    @property
    def effbdpattern_Feature95(self):
        return self.__effbdpattern_Feature95

    @effbdpattern_Feature95.setter
    def effbdpattern_Feature95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Feature__effbdpattern_Feature95", None)
        self.__effbdpattern_Feature95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Problem94"):
                opp_val = getattr(old_value, "effbdpattern_Problem94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Problem94"):
                opp_val = getattr(value, "effbdpattern_Problem94", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Problem94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Keyword:

    def __init__(self, value: str, effbdpattern_Keyword60: "effbdpattern_Indexable" = None, effbdpattern_Keyword: "effbdpattern_Workbench" = None):
        self.value = value
        self.effbdpattern_Keyword60 = effbdpattern_Keyword60
        self.effbdpattern_Keyword = effbdpattern_Keyword
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def effbdpattern_Keyword(self):
        return self.__effbdpattern_Keyword

    @effbdpattern_Keyword.setter
    def effbdpattern_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Keyword__effbdpattern_Keyword", None)
        self.__effbdpattern_Keyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench44"):
                opp_val = getattr(old_value, "effbdpattern_Workbench44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench44"):
                opp_val = getattr(value, "effbdpattern_Workbench44", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Keyword60(self):
        return self.__effbdpattern_Keyword60

    @effbdpattern_Keyword60.setter
    def effbdpattern_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Keyword__effbdpattern_Keyword60", None)
        self.__effbdpattern_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Indexable"):
                opp_val = getattr(old_value, "effbdpattern_Indexable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Indexable"):
                opp_val = getattr(value, "effbdpattern_Indexable", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Indexable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Domain(Indexable):

    def __init__(self, name: str, description: str, effbdpattern_Domain: "effbdpattern_Workbench" = None, effbdpattern_Domain80: "effbdpattern_AbstractModel" = None, effbdpattern_Domain112: "effbdpattern_SystemPattern" = None):
        self.name = name
        self.description = description
        self.effbdpattern_Domain = effbdpattern_Domain
        self.effbdpattern_Domain80 = effbdpattern_Domain80
        self.effbdpattern_Domain112 = effbdpattern_Domain112
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def effbdpattern_Domain80(self):
        return self.__effbdpattern_Domain80

    @effbdpattern_Domain80.setter
    def effbdpattern_Domain80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Domain__effbdpattern_Domain80", None)
        self.__effbdpattern_Domain80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_AbstractModel"):
                opp_val = getattr(old_value, "effbdpattern_AbstractModel", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_AbstractModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_AbstractModel"):
                opp_val = getattr(value, "effbdpattern_AbstractModel", None)
                setattr(value, "effbdpattern_AbstractModel", self)

    @property
    def effbdpattern_Domain(self):
        return self.__effbdpattern_Domain

    @effbdpattern_Domain.setter
    def effbdpattern_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Domain__effbdpattern_Domain", None)
        self.__effbdpattern_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench42"):
                opp_val = getattr(old_value, "effbdpattern_Workbench42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench42"):
                opp_val = getattr(value, "effbdpattern_Workbench42", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Domain112(self):
        return self.__effbdpattern_Domain112

    @effbdpattern_Domain112.setter
    def effbdpattern_Domain112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Domain__effbdpattern_Domain112", None)
        self.__effbdpattern_Domain112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern111"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern111", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_SystemPattern111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern111"):
                opp_val = getattr(value, "effbdpattern_SystemPattern111", None)
                setattr(value, "effbdpattern_SystemPattern111", self)

class effbdpattern_Problem(Indexable):

    def __init__(self, name: str, description: str, effbdpattern_Problem: "effbdpattern_Workbench" = None, effbdpattern_Problem91: set["effbdpattern_PatternModel"] = None, effbdpattern_Problem94: set["effbdpattern_Feature"] = None, problem: set["effbdpattern_Force"] = None, effbdpattern_Problem109: "effbdpattern_SystemPattern" = None, Problem: "effbdpattern_Force" = None):
        self.name = name
        self.description = description
        self.effbdpattern_Problem = effbdpattern_Problem
        self.effbdpattern_Problem91 = effbdpattern_Problem91 if effbdpattern_Problem91 is not None else set()
        self.effbdpattern_Problem94 = effbdpattern_Problem94 if effbdpattern_Problem94 is not None else set()
        self.problem = problem if problem is not None else set()
        self.effbdpattern_Problem109 = effbdpattern_Problem109
        self.Problem = Problem
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Problem(self):
        return self.__Problem

    @Problem.setter
    def Problem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Problem__Problem", None)
        self.__Problem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forces"):
                opp_val = getattr(old_value, "forces", None)
                if opp_val == self:
                    setattr(old_value, "forces", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forces"):
                opp_val = getattr(value, "forces", None)
                setattr(value, "forces", self)

    @property
    def effbdpattern_Problem109(self):
        return self.__effbdpattern_Problem109

    @effbdpattern_Problem109.setter
    def effbdpattern_Problem109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Problem__effbdpattern_Problem109", None)
        self.__effbdpattern_Problem109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern108"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern108", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_SystemPattern108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern108"):
                opp_val = getattr(value, "effbdpattern_SystemPattern108", None)
                setattr(value, "effbdpattern_SystemPattern108", self)

    @property
    def effbdpattern_Problem91(self):
        return self.__effbdpattern_Problem91

    @effbdpattern_Problem91.setter
    def effbdpattern_Problem91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Problem__effbdpattern_Problem91", None)
        self.__effbdpattern_Problem91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_PatternModel92"):
                    opp_val = getattr(item, "effbdpattern_PatternModel92", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_PatternModel92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_PatternModel92"):
                    opp_val = getattr(item, "effbdpattern_PatternModel92", None)
                    
                    setattr(item, "effbdpattern_PatternModel92", self)
                    

    @property
    def effbdpattern_Problem(self):
        return self.__effbdpattern_Problem

    @effbdpattern_Problem.setter
    def effbdpattern_Problem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Problem__effbdpattern_Problem", None)
        self.__effbdpattern_Problem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench40"):
                opp_val = getattr(old_value, "effbdpattern_Workbench40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench40"):
                opp_val = getattr(value, "effbdpattern_Workbench40", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Problem94(self):
        return self.__effbdpattern_Problem94

    @effbdpattern_Problem94.setter
    def effbdpattern_Problem94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Problem__effbdpattern_Problem94", None)
        self.__effbdpattern_Problem94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Feature95"):
                    opp_val = getattr(item, "effbdpattern_Feature95", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Feature95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Feature95"):
                    opp_val = getattr(item, "effbdpattern_Feature95", None)
                    
                    setattr(item, "effbdpattern_Feature95", self)
                    

    @property
    def problem(self):
        return self.__problem

    @problem.setter
    def problem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Problem__problem", None)
        self.__problem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Force"):
                    opp_val = getattr(item, "Force", None)
                    
                    if opp_val == self:
                        setattr(item, "Force", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Force"):
                    opp_val = getattr(item, "Force", None)
                    
                    setattr(item, "Force", self)
                    

class effbdpattern_Workbench:

    pass
class effbdpattern_SystemPattern(Indexable):

    def __init__(self, patternId: int, name: str, alias: str, challeng: str, description: str, creationDate: date, knownApplications: str, SystemPattern: "effbdpattern_ModelElement" = None, effbdpattern_SystemPattern: "effbdpattern_PatternCatalog" = None, SystemPattern100: "effbdpattern_Impact" = None, effbdpattern_SystemPattern102: set["effbdpattern_Parameter"] = None, effbdpattern_SystemPattern105: "effbdpattern_Context" = None, effbdpattern_SystemPattern108: "effbdpattern_Problem" = None, effbdpattern_SystemPattern111: "effbdpattern_Domain" = None, effbdpattern_SystemPattern115: "effbdpattern_SystemPattern" = None, effbdpattern_SystemPattern113: set["effbdpattern_SystemPattern"] = None, effbdpattern_SystemPattern126: "effbdpattern_PatternModel" = None, pattern: set["effbdpattern_Impact"] = None, pattern130: "effbdpattern_ModelElement" = None, effbdpattern_SystemPattern118: "effbdpattern_SystemPattern" = None, effbdpattern_SystemPattern116: set["effbdpattern_SystemPattern"] = None, effbdpattern_SystemPattern121: "effbdpattern_SystemPattern" = None, effbdpattern_SystemPattern119: set["effbdpattern_SystemPattern"] = None, effbdpattern_SystemPattern124: "effbdpattern_SystemPattern" = None, effbdpattern_SystemPattern122: set["effbdpattern_SystemPattern"] = None):
        self.patternId = patternId
        self.name = name
        self.alias = alias
        self.challeng = challeng
        self.description = description
        self.creationDate = creationDate
        self.knownApplications = knownApplications
        self.SystemPattern = SystemPattern
        self.effbdpattern_SystemPattern = effbdpattern_SystemPattern
        self.SystemPattern100 = SystemPattern100
        self.effbdpattern_SystemPattern102 = effbdpattern_SystemPattern102 if effbdpattern_SystemPattern102 is not None else set()
        self.effbdpattern_SystemPattern105 = effbdpattern_SystemPattern105
        self.effbdpattern_SystemPattern108 = effbdpattern_SystemPattern108
        self.effbdpattern_SystemPattern111 = effbdpattern_SystemPattern111
        self.effbdpattern_SystemPattern115 = effbdpattern_SystemPattern115
        self.effbdpattern_SystemPattern113 = effbdpattern_SystemPattern113 if effbdpattern_SystemPattern113 is not None else set()
        self.effbdpattern_SystemPattern126 = effbdpattern_SystemPattern126
        self.pattern = pattern if pattern is not None else set()
        self.pattern130 = pattern130
        self.effbdpattern_SystemPattern118 = effbdpattern_SystemPattern118
        self.effbdpattern_SystemPattern116 = effbdpattern_SystemPattern116 if effbdpattern_SystemPattern116 is not None else set()
        self.effbdpattern_SystemPattern121 = effbdpattern_SystemPattern121
        self.effbdpattern_SystemPattern119 = effbdpattern_SystemPattern119 if effbdpattern_SystemPattern119 is not None else set()
        self.effbdpattern_SystemPattern124 = effbdpattern_SystemPattern124
        self.effbdpattern_SystemPattern122 = effbdpattern_SystemPattern122 if effbdpattern_SystemPattern122 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def challeng(self) -> str:
        return self.__challeng

    @challeng.setter
    def challeng(self, challeng: str):
        self.__challeng = challeng

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def patternId(self) -> int:
        return self.__patternId

    @patternId.setter
    def patternId(self, patternId: int):
        self.__patternId = patternId

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def knownApplications(self) -> str:
        return self.__knownApplications

    @knownApplications.setter
    def knownApplications(self, knownApplications: str):
        self.__knownApplications = knownApplications

    @property
    def effbdpattern_SystemPattern126(self):
        return self.__effbdpattern_SystemPattern126

    @effbdpattern_SystemPattern126.setter
    def effbdpattern_SystemPattern126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern126", None)
        self.__effbdpattern_SystemPattern126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_PatternModel127"):
                opp_val = getattr(old_value, "effbdpattern_PatternModel127", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_PatternModel127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_PatternModel127"):
                opp_val = getattr(value, "effbdpattern_PatternModel127", None)
                setattr(value, "effbdpattern_PatternModel127", self)

    @property
    def effbdpattern_SystemPattern122(self):
        return self.__effbdpattern_SystemPattern122

    @effbdpattern_SystemPattern122.setter
    def effbdpattern_SystemPattern122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern122", None)
        self.__effbdpattern_SystemPattern122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_SystemPattern124"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern124", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_SystemPattern124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_SystemPattern124"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern124", None)
                    
                    setattr(item, "effbdpattern_SystemPattern124", self)
                    

    @property
    def effbdpattern_SystemPattern115(self):
        return self.__effbdpattern_SystemPattern115

    @effbdpattern_SystemPattern115.setter
    def effbdpattern_SystemPattern115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern115", None)
        self.__effbdpattern_SystemPattern115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern113"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern113"):
                opp_val = getattr(value, "effbdpattern_SystemPattern113", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_SystemPattern113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_SystemPattern111(self):
        return self.__effbdpattern_SystemPattern111

    @effbdpattern_SystemPattern111.setter
    def effbdpattern_SystemPattern111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern111", None)
        self.__effbdpattern_SystemPattern111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Domain112"):
                opp_val = getattr(old_value, "effbdpattern_Domain112", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Domain112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Domain112"):
                opp_val = getattr(value, "effbdpattern_Domain112", None)
                setattr(value, "effbdpattern_Domain112", self)

    @property
    def effbdpattern_SystemPattern119(self):
        return self.__effbdpattern_SystemPattern119

    @effbdpattern_SystemPattern119.setter
    def effbdpattern_SystemPattern119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern119", None)
        self.__effbdpattern_SystemPattern119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_SystemPattern121"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern121", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_SystemPattern121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_SystemPattern121"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern121", None)
                    
                    setattr(item, "effbdpattern_SystemPattern121", self)
                    

    @property
    def effbdpattern_SystemPattern124(self):
        return self.__effbdpattern_SystemPattern124

    @effbdpattern_SystemPattern124.setter
    def effbdpattern_SystemPattern124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern124", None)
        self.__effbdpattern_SystemPattern124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern122"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern122"):
                opp_val = getattr(value, "effbdpattern_SystemPattern122", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_SystemPattern122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_SystemPattern105(self):
        return self.__effbdpattern_SystemPattern105

    @effbdpattern_SystemPattern105.setter
    def effbdpattern_SystemPattern105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern105", None)
        self.__effbdpattern_SystemPattern105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Context106"):
                opp_val = getattr(old_value, "effbdpattern_Context106", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Context106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Context106"):
                opp_val = getattr(value, "effbdpattern_Context106", None)
                setattr(value, "effbdpattern_Context106", self)

    @property
    def effbdpattern_SystemPattern(self):
        return self.__effbdpattern_SystemPattern

    @effbdpattern_SystemPattern.setter
    def effbdpattern_SystemPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern", None)
        self.__effbdpattern_SystemPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_PatternCatalog36"):
                opp_val = getattr(old_value, "effbdpattern_PatternCatalog36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_PatternCatalog36"):
                opp_val = getattr(value, "effbdpattern_PatternCatalog36", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_PatternCatalog36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_SystemPattern102(self):
        return self.__effbdpattern_SystemPattern102

    @effbdpattern_SystemPattern102.setter
    def effbdpattern_SystemPattern102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern102", None)
        self.__effbdpattern_SystemPattern102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Parameter103"):
                    opp_val = getattr(item, "effbdpattern_Parameter103", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Parameter103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Parameter103"):
                    opp_val = getattr(item, "effbdpattern_Parameter103", None)
                    
                    setattr(item, "effbdpattern_Parameter103", self)
                    

    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__pattern", None)
        self.__pattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Impact"):
                    opp_val = getattr(item, "Impact", None)
                    
                    if opp_val == self:
                        setattr(item, "Impact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Impact"):
                    opp_val = getattr(item, "Impact", None)
                    
                    setattr(item, "Impact", self)
                    

    @property
    def effbdpattern_SystemPattern118(self):
        return self.__effbdpattern_SystemPattern118

    @effbdpattern_SystemPattern118.setter
    def effbdpattern_SystemPattern118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern118", None)
        self.__effbdpattern_SystemPattern118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern116"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern116"):
                opp_val = getattr(value, "effbdpattern_SystemPattern116", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_SystemPattern116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_SystemPattern108(self):
        return self.__effbdpattern_SystemPattern108

    @effbdpattern_SystemPattern108.setter
    def effbdpattern_SystemPattern108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern108", None)
        self.__effbdpattern_SystemPattern108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Problem109"):
                opp_val = getattr(old_value, "effbdpattern_Problem109", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Problem109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Problem109"):
                opp_val = getattr(value, "effbdpattern_Problem109", None)
                setattr(value, "effbdpattern_Problem109", self)

    @property
    def effbdpattern_SystemPattern121(self):
        return self.__effbdpattern_SystemPattern121

    @effbdpattern_SystemPattern121.setter
    def effbdpattern_SystemPattern121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern121", None)
        self.__effbdpattern_SystemPattern121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SystemPattern119"):
                opp_val = getattr(old_value, "effbdpattern_SystemPattern119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SystemPattern119"):
                opp_val = getattr(value, "effbdpattern_SystemPattern119", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_SystemPattern119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_SystemPattern113(self):
        return self.__effbdpattern_SystemPattern113

    @effbdpattern_SystemPattern113.setter
    def effbdpattern_SystemPattern113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern113", None)
        self.__effbdpattern_SystemPattern113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_SystemPattern115"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern115", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_SystemPattern115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_SystemPattern115"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern115", None)
                    
                    setattr(item, "effbdpattern_SystemPattern115", self)
                    

    @property
    def SystemPattern100(self):
        return self.__SystemPattern100

    @SystemPattern100.setter
    def SystemPattern100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__SystemPattern100", None)
        self.__SystemPattern100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impacts"):
                opp_val = getattr(old_value, "impacts", None)
                if opp_val == self:
                    setattr(old_value, "impacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impacts"):
                opp_val = getattr(value, "impacts", None)
                setattr(value, "impacts", self)

    @property
    def SystemPattern(self):
        return self.__SystemPattern

    @SystemPattern.setter
    def SystemPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__SystemPattern", None)
        self.__SystemPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelElement"):
                opp_val = getattr(old_value, "modelElement", None)
                if opp_val == self:
                    setattr(old_value, "modelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelElement"):
                opp_val = getattr(value, "modelElement", None)
                setattr(value, "modelElement", self)

    @property
    def effbdpattern_SystemPattern116(self):
        return self.__effbdpattern_SystemPattern116

    @effbdpattern_SystemPattern116.setter
    def effbdpattern_SystemPattern116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__effbdpattern_SystemPattern116", None)
        self.__effbdpattern_SystemPattern116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_SystemPattern118"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern118", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_SystemPattern118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_SystemPattern118"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern118", None)
                    
                    setattr(item, "effbdpattern_SystemPattern118", self)
                    

    @property
    def pattern130(self):
        return self.__pattern130

    @pattern130.setter
    def pattern130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SystemPattern__pattern130", None)
        self.__pattern130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElement"):
                opp_val = getattr(old_value, "ModelElement", None)
                if opp_val == self:
                    setattr(old_value, "ModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElement"):
                opp_val = getattr(value, "ModelElement", None)
                setattr(value, "ModelElement", self)

class effbdpattern_Indexable(ABC):

    pass
class effbdpattern_PatternCatalog:

    def __init__(self, id: str, effbdpattern_PatternCatalog: set["effbdpattern_Function"] = None, effbdpattern_PatternCatalog36: set["effbdpattern_SystemPattern"] = None, effbdpattern_PatternCatalog55: "effbdpattern_Workbench" = None):
        self.id = id
        self.effbdpattern_PatternCatalog = effbdpattern_PatternCatalog if effbdpattern_PatternCatalog is not None else set()
        self.effbdpattern_PatternCatalog36 = effbdpattern_PatternCatalog36 if effbdpattern_PatternCatalog36 is not None else set()
        self.effbdpattern_PatternCatalog55 = effbdpattern_PatternCatalog55
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def effbdpattern_PatternCatalog(self):
        return self.__effbdpattern_PatternCatalog

    @effbdpattern_PatternCatalog.setter
    def effbdpattern_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_PatternCatalog__effbdpattern_PatternCatalog", None)
        self.__effbdpattern_PatternCatalog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Function34"):
                    opp_val = getattr(item, "effbdpattern_Function34", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Function34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Function34"):
                    opp_val = getattr(item, "effbdpattern_Function34", None)
                    
                    setattr(item, "effbdpattern_Function34", self)
                    

    @property
    def effbdpattern_PatternCatalog55(self):
        return self.__effbdpattern_PatternCatalog55

    @effbdpattern_PatternCatalog55.setter
    def effbdpattern_PatternCatalog55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_PatternCatalog__effbdpattern_PatternCatalog55", None)
        self.__effbdpattern_PatternCatalog55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench54"):
                opp_val = getattr(old_value, "effbdpattern_Workbench54", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Workbench54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench54"):
                opp_val = getattr(value, "effbdpattern_Workbench54", None)
                setattr(value, "effbdpattern_Workbench54", self)

    @property
    def effbdpattern_PatternCatalog36(self):
        return self.__effbdpattern_PatternCatalog36

    @effbdpattern_PatternCatalog36.setter
    def effbdpattern_PatternCatalog36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_PatternCatalog__effbdpattern_PatternCatalog36", None)
        self.__effbdpattern_PatternCatalog36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_SystemPattern"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_SystemPattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_SystemPattern"):
                    opp_val = getattr(item, "effbdpattern_SystemPattern", None)
                    
                    setattr(item, "effbdpattern_SystemPattern", self)
                    

class effbdpattern_Port(ABC):

    def __init__(self, id: str, effbdpattern_Port: "effbdpattern_Port" = None, effbdpattern_Port20: "effbdpattern_Port" = None):
        self.id = id
        self.effbdpattern_Port = effbdpattern_Port
        self.effbdpattern_Port20 = effbdpattern_Port20
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def effbdpattern_Port(self):
        return self.__effbdpattern_Port

    @effbdpattern_Port.setter
    def effbdpattern_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Port__effbdpattern_Port", None)
        self.__effbdpattern_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Port20"):
                opp_val = getattr(old_value, "effbdpattern_Port20", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Port20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Port20"):
                opp_val = getattr(value, "effbdpattern_Port20", None)
                setattr(value, "effbdpattern_Port20", self)

    @property
    def effbdpattern_Port20(self):
        return self.__effbdpattern_Port20

    @effbdpattern_Port20.setter
    def effbdpattern_Port20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Port__effbdpattern_Port20", None)
        self.__effbdpattern_Port20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Port"):
                opp_val = getattr(old_value, "effbdpattern_Port", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Port"):
                opp_val = getattr(value, "effbdpattern_Port", None)
                setattr(value, "effbdpattern_Port", self)

class Port:

    pass
class effbdpattern_Item:

    def __init__(self, name: str, effbdpattern_Item: "effbdpattern_Flow" = None):
        self.name = name
        self.effbdpattern_Item = effbdpattern_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbdpattern_Item(self):
        return self.__effbdpattern_Item

    @effbdpattern_Item.setter
    def effbdpattern_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Item__effbdpattern_Item", None)
        self.__effbdpattern_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Flow26"):
                opp_val = getattr(old_value, "effbdpattern_Flow26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Flow26"):
                opp_val = getattr(value, "effbdpattern_Flow26", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Flow26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Sequence:

    pass
class effbdpattern_Or(Sequence):

    pass
class effbdpattern_Iteration(Sequence):

    pass
class effbdpattern_LoopExit(Sequence):

    pass
class effbdpattern_Start(Sequence):

    pass
class effbdpattern_Loop(Sequence):

    pass
class effbdpattern_And(Sequence):

    pass
class effbdpattern_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, effbdpattern_SequenceNode: "effbdpattern_SequenceNode" = None, effbdpattern_SequenceNode18: set["effbdpattern_SequenceNode"] = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.effbdpattern_SequenceNode = effbdpattern_SequenceNode
        self.effbdpattern_SequenceNode18 = effbdpattern_SequenceNode18 if effbdpattern_SequenceNode18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def effbdpattern_SequenceNode18(self):
        return self.__effbdpattern_SequenceNode18

    @effbdpattern_SequenceNode18.setter
    def effbdpattern_SequenceNode18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SequenceNode__effbdpattern_SequenceNode18", None)
        self.__effbdpattern_SequenceNode18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_SequenceNode"):
                    opp_val = getattr(item, "effbdpattern_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_SequenceNode"):
                    opp_val = getattr(item, "effbdpattern_SequenceNode", None)
                    
                    setattr(item, "effbdpattern_SequenceNode", self)
                    

    @property
    def effbdpattern_SequenceNode(self):
        return self.__effbdpattern_SequenceNode

    @effbdpattern_SequenceNode.setter
    def effbdpattern_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_SequenceNode__effbdpattern_SequenceNode", None)
        self.__effbdpattern_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_SequenceNode18"):
                opp_val = getattr(old_value, "effbdpattern_SequenceNode18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_SequenceNode18"):
                opp_val = getattr(value, "effbdpattern_SequenceNode18", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_SequenceNode18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Final(Sequence):

    pass
class ModelElement:

    pass
class effbdpattern_Component(ModelElement):

    pass
class SequenceNode:

    pass
class effbdpattern_Sequence(SequenceNode):

    pass
class effbdpattern_Function(SequenceNode, ModelElement):

    def __init__(self, domain: str, effbdpattern_Function4: set["effbdpattern_Flow"] = None, effbdpattern_Function6: set["effbdpattern_OutputPort"] = None, effbdpattern_Function8: set["effbdpattern_InputPort"] = None, effbdpattern_Function10: set["effbdpattern_Description"] = None, effbdpattern_Function12: set["effbdpattern_Token"] = None, effbdpattern_Function14: set["effbdpattern_FunctionProperty"] = None, Function17: "effbdpattern_Function" = None, decompositions: "effbdpattern_Function" = None, Function: "effbdpattern_Function" = None, parent: set["effbdpattern_Function"] = None, effbdpattern_Function: set["effbdpattern_Sequence"] = None, effbdpattern_Function34: "effbdpattern_PatternCatalog" = None, effbdpattern_Function69: "effbdpattern_PatternModel" = None, effbdpattern_Function136: "effbdpattern_Model" = None, effbdpattern_Function142: "effbdpattern_Allocation" = None):
        self.domain = domain
        self.effbdpattern_Function4 = effbdpattern_Function4 if effbdpattern_Function4 is not None else set()
        self.effbdpattern_Function6 = effbdpattern_Function6 if effbdpattern_Function6 is not None else set()
        self.effbdpattern_Function8 = effbdpattern_Function8 if effbdpattern_Function8 is not None else set()
        self.effbdpattern_Function10 = effbdpattern_Function10 if effbdpattern_Function10 is not None else set()
        self.effbdpattern_Function12 = effbdpattern_Function12 if effbdpattern_Function12 is not None else set()
        self.effbdpattern_Function14 = effbdpattern_Function14 if effbdpattern_Function14 is not None else set()
        self.Function17 = Function17
        self.decompositions = decompositions
        self.Function = Function
        self.parent = parent if parent is not None else set()
        self.effbdpattern_Function = effbdpattern_Function if effbdpattern_Function is not None else set()
        self.effbdpattern_Function34 = effbdpattern_Function34
        self.effbdpattern_Function69 = effbdpattern_Function69
        self.effbdpattern_Function136 = effbdpattern_Function136
        self.effbdpattern_Function142 = effbdpattern_Function142
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def effbdpattern_Function10(self):
        return self.__effbdpattern_Function10

    @effbdpattern_Function10.setter
    def effbdpattern_Function10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function10", None)
        self.__effbdpattern_Function10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Description"):
                    opp_val = getattr(item, "effbdpattern_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Description"):
                    opp_val = getattr(item, "effbdpattern_Description", None)
                    
                    setattr(item, "effbdpattern_Description", self)
                    

    @property
    def decompositions(self):
        return self.__decompositions

    @decompositions.setter
    def decompositions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__decompositions", None)
        self.__decompositions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function17"):
                opp_val = getattr(old_value, "Function17", None)
                if opp_val == self:
                    setattr(old_value, "Function17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function17"):
                opp_val = getattr(value, "Function17", None)
                setattr(value, "Function17", self)

    @property
    def effbdpattern_Function69(self):
        return self.__effbdpattern_Function69

    @effbdpattern_Function69.setter
    def effbdpattern_Function69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function69", None)
        self.__effbdpattern_Function69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_PatternModel"):
                opp_val = getattr(old_value, "effbdpattern_PatternModel", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_PatternModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_PatternModel"):
                opp_val = getattr(value, "effbdpattern_PatternModel", None)
                setattr(value, "effbdpattern_PatternModel", self)

    @property
    def effbdpattern_Function4(self):
        return self.__effbdpattern_Function4

    @effbdpattern_Function4.setter
    def effbdpattern_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function4", None)
        self.__effbdpattern_Function4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Flow"):
                    opp_val = getattr(item, "effbdpattern_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Flow"):
                    opp_val = getattr(item, "effbdpattern_Flow", None)
                    
                    setattr(item, "effbdpattern_Flow", self)
                    

    @property
    def effbdpattern_Function6(self):
        return self.__effbdpattern_Function6

    @effbdpattern_Function6.setter
    def effbdpattern_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function6", None)
        self.__effbdpattern_Function6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_OutputPort"):
                    opp_val = getattr(item, "effbdpattern_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_OutputPort"):
                    opp_val = getattr(item, "effbdpattern_OutputPort", None)
                    
                    setattr(item, "effbdpattern_OutputPort", self)
                    

    @property
    def effbdpattern_Function12(self):
        return self.__effbdpattern_Function12

    @effbdpattern_Function12.setter
    def effbdpattern_Function12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function12", None)
        self.__effbdpattern_Function12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Token"):
                    opp_val = getattr(item, "effbdpattern_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Token"):
                    opp_val = getattr(item, "effbdpattern_Token", None)
                    
                    setattr(item, "effbdpattern_Token", self)
                    

    @property
    def effbdpattern_Function14(self):
        return self.__effbdpattern_Function14

    @effbdpattern_Function14.setter
    def effbdpattern_Function14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function14", None)
        self.__effbdpattern_Function14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_FunctionProperty"):
                    opp_val = getattr(item, "effbdpattern_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_FunctionProperty"):
                    opp_val = getattr(item, "effbdpattern_FunctionProperty", None)
                    
                    setattr(item, "effbdpattern_FunctionProperty", self)
                    

    @property
    def effbdpattern_Function142(self):
        return self.__effbdpattern_Function142

    @effbdpattern_Function142.setter
    def effbdpattern_Function142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function142", None)
        self.__effbdpattern_Function142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Allocation141"):
                opp_val = getattr(old_value, "effbdpattern_Allocation141", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Allocation141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Allocation141"):
                opp_val = getattr(value, "effbdpattern_Allocation141", None)
                setattr(value, "effbdpattern_Allocation141", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    if opp_val == self:
                        setattr(item, "Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    setattr(item, "Function", self)
                    

    @property
    def effbdpattern_Function8(self):
        return self.__effbdpattern_Function8

    @effbdpattern_Function8.setter
    def effbdpattern_Function8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function8", None)
        self.__effbdpattern_Function8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_InputPort"):
                    opp_val = getattr(item, "effbdpattern_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_InputPort"):
                    opp_val = getattr(item, "effbdpattern_InputPort", None)
                    
                    setattr(item, "effbdpattern_InputPort", self)
                    

    @property
    def effbdpattern_Function(self):
        return self.__effbdpattern_Function

    @effbdpattern_Function.setter
    def effbdpattern_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function", None)
        self.__effbdpattern_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Sequence"):
                    opp_val = getattr(item, "effbdpattern_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Sequence"):
                    opp_val = getattr(item, "effbdpattern_Sequence", None)
                    
                    setattr(item, "effbdpattern_Sequence", self)
                    

    @property
    def effbdpattern_Function136(self):
        return self.__effbdpattern_Function136

    @effbdpattern_Function136.setter
    def effbdpattern_Function136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function136", None)
        self.__effbdpattern_Function136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Model135"):
                opp_val = getattr(old_value, "effbdpattern_Model135", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_Model135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Model135"):
                opp_val = getattr(value, "effbdpattern_Model135", None)
                setattr(value, "effbdpattern_Model135", self)

    @property
    def Function(self):
        return self.__Function

    @Function.setter
    def Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__Function", None)
        self.__Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Function17(self):
        return self.__Function17

    @Function17.setter
    def Function17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__Function17", None)
        self.__Function17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decompositions"):
                opp_val = getattr(old_value, "decompositions", None)
                if opp_val == self:
                    setattr(old_value, "decompositions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decompositions"):
                opp_val = getattr(value, "decompositions", None)
                setattr(value, "decompositions", self)

    @property
    def effbdpattern_Function34(self):
        return self.__effbdpattern_Function34

    @effbdpattern_Function34.setter
    def effbdpattern_Function34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Function__effbdpattern_Function34", None)
        self.__effbdpattern_Function34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_PatternCatalog"):
                opp_val = getattr(old_value, "effbdpattern_PatternCatalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_PatternCatalog"):
                opp_val = getattr(value, "effbdpattern_PatternCatalog", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_PatternCatalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_FunctionProperty:

    def __init__(self, description: str, effbdpattern_FunctionProperty: "effbdpattern_Function" = None, effbdpattern_FunctionProperty32: "effbdpattern_FunctionProperty" = None, effbdpattern_FunctionProperty30: "effbdpattern_FunctionProperty" = None, effbdpattern_FunctionProperty38: "effbdpattern_Workbench" = None):
        self.description = description
        self.effbdpattern_FunctionProperty = effbdpattern_FunctionProperty
        self.effbdpattern_FunctionProperty32 = effbdpattern_FunctionProperty32
        self.effbdpattern_FunctionProperty30 = effbdpattern_FunctionProperty30
        self.effbdpattern_FunctionProperty38 = effbdpattern_FunctionProperty38
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def effbdpattern_FunctionProperty38(self):
        return self.__effbdpattern_FunctionProperty38

    @effbdpattern_FunctionProperty38.setter
    def effbdpattern_FunctionProperty38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_FunctionProperty__effbdpattern_FunctionProperty38", None)
        self.__effbdpattern_FunctionProperty38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Workbench"):
                opp_val = getattr(old_value, "effbdpattern_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Workbench"):
                opp_val = getattr(value, "effbdpattern_Workbench", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_FunctionProperty32(self):
        return self.__effbdpattern_FunctionProperty32

    @effbdpattern_FunctionProperty32.setter
    def effbdpattern_FunctionProperty32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_FunctionProperty__effbdpattern_FunctionProperty32", None)
        self.__effbdpattern_FunctionProperty32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_FunctionProperty30"):
                opp_val = getattr(old_value, "effbdpattern_FunctionProperty30", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_FunctionProperty30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_FunctionProperty30"):
                opp_val = getattr(value, "effbdpattern_FunctionProperty30", None)
                setattr(value, "effbdpattern_FunctionProperty30", self)

    @property
    def effbdpattern_FunctionProperty30(self):
        return self.__effbdpattern_FunctionProperty30

    @effbdpattern_FunctionProperty30.setter
    def effbdpattern_FunctionProperty30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_FunctionProperty__effbdpattern_FunctionProperty30", None)
        self.__effbdpattern_FunctionProperty30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_FunctionProperty32"):
                opp_val = getattr(old_value, "effbdpattern_FunctionProperty32", None)
                if opp_val == self:
                    setattr(old_value, "effbdpattern_FunctionProperty32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_FunctionProperty32"):
                opp_val = getattr(value, "effbdpattern_FunctionProperty32", None)
                setattr(value, "effbdpattern_FunctionProperty32", self)

    @property
    def effbdpattern_FunctionProperty(self):
        return self.__effbdpattern_FunctionProperty

    @effbdpattern_FunctionProperty.setter
    def effbdpattern_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_FunctionProperty__effbdpattern_FunctionProperty", None)
        self.__effbdpattern_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Function14"):
                opp_val = getattr(old_value, "effbdpattern_Function14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Function14"):
                opp_val = getattr(value, "effbdpattern_Function14", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Function14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_Token:

    pass
class effbdpattern_Description:

    def __init__(self, content: str, effbdpattern_Description: "effbdpattern_Function" = None):
        self.content = content
        self.effbdpattern_Description = effbdpattern_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbdpattern_Description(self):
        return self.__effbdpattern_Description

    @effbdpattern_Description.setter
    def effbdpattern_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Description__effbdpattern_Description", None)
        self.__effbdpattern_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Function10"):
                opp_val = getattr(old_value, "effbdpattern_Function10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Function10"):
                opp_val = getattr(value, "effbdpattern_Function10", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Function10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbdpattern_InputPort(Port):

    pass
class effbdpattern_OutputPort(Port):

    pass
class effbdpattern_Flow:

    def __init__(self, flowName: str, effbdpattern_Flow: "effbdpattern_Function" = None, effbdpattern_Flow23: set["effbdpattern_InputPort"] = None, effbdpattern_Flow26: set["effbdpattern_Item"] = None, effbdpattern_Flow29: "effbdpattern_OutputPort" = None):
        self.flowName = flowName
        self.effbdpattern_Flow = effbdpattern_Flow
        self.effbdpattern_Flow23 = effbdpattern_Flow23 if effbdpattern_Flow23 is not None else set()
        self.effbdpattern_Flow26 = effbdpattern_Flow26 if effbdpattern_Flow26 is not None else set()
        self.effbdpattern_Flow29 = effbdpattern_Flow29
        
    @property
    def flowName(self) -> str:
        return self.__flowName

    @flowName.setter
    def flowName(self, flowName: str):
        self.__flowName = flowName

    @property
    def effbdpattern_Flow26(self):
        return self.__effbdpattern_Flow26

    @effbdpattern_Flow26.setter
    def effbdpattern_Flow26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Flow__effbdpattern_Flow26", None)
        self.__effbdpattern_Flow26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_Item"):
                    opp_val = getattr(item, "effbdpattern_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_Item"):
                    opp_val = getattr(item, "effbdpattern_Item", None)
                    
                    setattr(item, "effbdpattern_Item", self)
                    

    @property
    def effbdpattern_Flow29(self):
        return self.__effbdpattern_Flow29

    @effbdpattern_Flow29.setter
    def effbdpattern_Flow29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Flow__effbdpattern_Flow29", None)
        self.__effbdpattern_Flow29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_OutputPort28"):
                opp_val = getattr(old_value, "effbdpattern_OutputPort28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_OutputPort28"):
                opp_val = getattr(value, "effbdpattern_OutputPort28", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_OutputPort28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Flow(self):
        return self.__effbdpattern_Flow

    @effbdpattern_Flow.setter
    def effbdpattern_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Flow__effbdpattern_Flow", None)
        self.__effbdpattern_Flow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbdpattern_Function4"):
                opp_val = getattr(old_value, "effbdpattern_Function4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbdpattern_Function4"):
                opp_val = getattr(value, "effbdpattern_Function4", None)
                if opp_val is None:
                    setattr(value, "effbdpattern_Function4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbdpattern_Flow23(self):
        return self.__effbdpattern_Flow23

    @effbdpattern_Flow23.setter
    def effbdpattern_Flow23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbdpattern_Flow__effbdpattern_Flow23", None)
        self.__effbdpattern_Flow23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbdpattern_InputPort24"):
                    opp_val = getattr(item, "effbdpattern_InputPort24", None)
                    
                    if opp_val == self:
                        setattr(item, "effbdpattern_InputPort24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbdpattern_InputPort24"):
                    opp_val = getattr(item, "effbdpattern_InputPort24", None)
                    
                    setattr(item, "effbdpattern_InputPort24", self)
                    
