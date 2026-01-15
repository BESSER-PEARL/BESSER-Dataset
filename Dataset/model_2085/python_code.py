from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeEnum(Enum):
    String = "String"
    Boolean = "Boolean"
    Integer = "Integer"
    Real = "Real"
    UnlimitedNatural = "UnlimitedNatural"


############################################
# Definition of Classes
############################################

class cvlmodel_CVLModel:

    def __init__(self, name: str, cvlmodel_CVLModel: "cvlmodel_VSpecTree" = None, cvlmodel_CVLModel33: set["cvlmodel_VariationPoint"] = None):
        self.name = name
        self.cvlmodel_CVLModel = cvlmodel_CVLModel
        self.cvlmodel_CVLModel33 = cvlmodel_CVLModel33 if cvlmodel_CVLModel33 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cvlmodel_CVLModel(self):
        return self.__cvlmodel_CVLModel

    @cvlmodel_CVLModel.setter
    def cvlmodel_CVLModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_CVLModel__cvlmodel_CVLModel", None)
        self.__cvlmodel_CVLModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpecTree31"):
                opp_val = getattr(old_value, "cvlmodel_VSpecTree31", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpecTree31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpecTree31"):
                opp_val = getattr(value, "cvlmodel_VSpecTree31", None)
                setattr(value, "cvlmodel_VSpecTree31", self)

    @property
    def cvlmodel_CVLModel33(self):
        return self.__cvlmodel_CVLModel33

    @cvlmodel_CVLModel33.setter
    def cvlmodel_CVLModel33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_CVLModel__cvlmodel_CVLModel33", None)
        self.__cvlmodel_CVLModel33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cvlmodel_VariationPoint34"):
                    opp_val = getattr(item, "cvlmodel_VariationPoint34", None)
                    
                    if opp_val == self:
                        setattr(item, "cvlmodel_VariationPoint34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cvlmodel_VariationPoint34"):
                    opp_val = getattr(item, "cvlmodel_VariationPoint34", None)
                    
                    setattr(item, "cvlmodel_VariationPoint34", self)
                    

class cvlmodel_ResolutionModel:

    def __init__(self, name: str, cvlmodel_ResolutionModel: set["cvlmodel_VSpecResolution"] = None, cvlmodel_ResolutionModel28: "cvlmodel_VSpecTree" = None):
        self.name = name
        self.cvlmodel_ResolutionModel = cvlmodel_ResolutionModel if cvlmodel_ResolutionModel is not None else set()
        self.cvlmodel_ResolutionModel28 = cvlmodel_ResolutionModel28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cvlmodel_ResolutionModel(self):
        return self.__cvlmodel_ResolutionModel

    @cvlmodel_ResolutionModel.setter
    def cvlmodel_ResolutionModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_ResolutionModel__cvlmodel_ResolutionModel", None)
        self.__cvlmodel_ResolutionModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cvlmodel_VSpecResolution26"):
                    opp_val = getattr(item, "cvlmodel_VSpecResolution26", None)
                    
                    if opp_val == self:
                        setattr(item, "cvlmodel_VSpecResolution26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cvlmodel_VSpecResolution26"):
                    opp_val = getattr(item, "cvlmodel_VSpecResolution26", None)
                    
                    setattr(item, "cvlmodel_VSpecResolution26", self)
                    

    @property
    def cvlmodel_ResolutionModel28(self):
        return self.__cvlmodel_ResolutionModel28

    @cvlmodel_ResolutionModel28.setter
    def cvlmodel_ResolutionModel28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_ResolutionModel__cvlmodel_ResolutionModel28", None)
        self.__cvlmodel_ResolutionModel28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpecTree29"):
                opp_val = getattr(old_value, "cvlmodel_VSpecTree29", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpecTree29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpecTree29"):
                opp_val = getattr(value, "cvlmodel_VSpecTree29", None)
                setattr(value, "cvlmodel_VSpecTree29", self)

    def getVSpecResolutionsForVSpec(self, vspec: VSpec) -> str:
        # TODO: Implement getVSpecResolutionsForVSpec method
        pass

class cvlmodel_MOFRef:

    def __init__(self, id: str, cvlmodel_MOFRef: "cvlmodel_StringToMOFRefMap" = None):
        self.id = id
        self.cvlmodel_MOFRef = cvlmodel_MOFRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def cvlmodel_MOFRef(self):
        return self.__cvlmodel_MOFRef

    @cvlmodel_MOFRef.setter
    def cvlmodel_MOFRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_MOFRef__cvlmodel_MOFRef", None)
        self.__cvlmodel_MOFRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_StringToMOFRefMap19"):
                opp_val = getattr(old_value, "cvlmodel_StringToMOFRefMap19", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_StringToMOFRefMap19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_StringToMOFRefMap19"):
                opp_val = getattr(value, "cvlmodel_StringToMOFRefMap19", None)
                setattr(value, "cvlmodel_StringToMOFRefMap19", self)

class cvlmodel_StringToMOFRefMap:

    def __init__(self, key: str, cvlmodel_StringToMOFRefMap19: "cvlmodel_MOFRef" = None, cvlmodel_StringToMOFRefMap: "cvlmodel_VariationPoint" = None):
        self.key = key
        self.cvlmodel_StringToMOFRefMap19 = cvlmodel_StringToMOFRefMap19
        self.cvlmodel_StringToMOFRefMap = cvlmodel_StringToMOFRefMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def cvlmodel_StringToMOFRefMap19(self):
        return self.__cvlmodel_StringToMOFRefMap19

    @cvlmodel_StringToMOFRefMap19.setter
    def cvlmodel_StringToMOFRefMap19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_StringToMOFRefMap__cvlmodel_StringToMOFRefMap19", None)
        self.__cvlmodel_StringToMOFRefMap19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_MOFRef"):
                opp_val = getattr(old_value, "cvlmodel_MOFRef", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_MOFRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_MOFRef"):
                opp_val = getattr(value, "cvlmodel_MOFRef", None)
                setattr(value, "cvlmodel_MOFRef", self)

    @property
    def cvlmodel_StringToMOFRefMap(self):
        return self.__cvlmodel_StringToMOFRefMap

    @cvlmodel_StringToMOFRefMap.setter
    def cvlmodel_StringToMOFRefMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_StringToMOFRefMap__cvlmodel_StringToMOFRefMap", None)
        self.__cvlmodel_StringToMOFRefMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VariationPoint17"):
                opp_val = getattr(old_value, "cvlmodel_VariationPoint17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VariationPoint17"):
                opp_val = getattr(value, "cvlmodel_VariationPoint17", None)
                if opp_val is None:
                    setattr(value, "cvlmodel_VariationPoint17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cvlmodel_VSpecTree:

    pass
class VariationPoint:

    pass
class cvlmodel_ObjectExistence(VariationPoint):

    def __init__(self, target: str):
        self.target = target
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class cvlmodel_VSpecResolution(ABC):

    def __init__(self, name: str, cvlmodel_VSpecResolution: "cvlmodel_VSpec" = None, cvlmodel_VSpecResolution26: "cvlmodel_ResolutionModel" = None):
        self.name = name
        self.cvlmodel_VSpecResolution = cvlmodel_VSpecResolution
        self.cvlmodel_VSpecResolution26 = cvlmodel_VSpecResolution26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cvlmodel_VSpecResolution26(self):
        return self.__cvlmodel_VSpecResolution26

    @cvlmodel_VSpecResolution26.setter
    def cvlmodel_VSpecResolution26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpecResolution__cvlmodel_VSpecResolution26", None)
        self.__cvlmodel_VSpecResolution26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_ResolutionModel"):
                opp_val = getattr(old_value, "cvlmodel_ResolutionModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_ResolutionModel"):
                opp_val = getattr(value, "cvlmodel_ResolutionModel", None)
                if opp_val is None:
                    setattr(value, "cvlmodel_ResolutionModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cvlmodel_VSpecResolution(self):
        return self.__cvlmodel_VSpecResolution

    @cvlmodel_VSpecResolution.setter
    def cvlmodel_VSpecResolution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpecResolution__cvlmodel_VSpecResolution", None)
        self.__cvlmodel_VSpecResolution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpec13"):
                opp_val = getattr(old_value, "cvlmodel_VSpec13", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpec13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpec13"):
                opp_val = getattr(value, "cvlmodel_VSpec13", None)
                setattr(value, "cvlmodel_VSpec13", self)

    def isPossitivelyResolved(self) -> str:
        # TODO: Implement isPossitivelyResolved method
        pass

class cvlmodel_VariationPoint(ABC):

    def __init__(self, modelTransformationURL: str, modelTransformationSourceURL: str, name: str, negativeVariability: str, cvlmodel_VariationPoint: "cvlmodel_VSpec" = None, cvlmodel_VariationPoint17: set["cvlmodel_StringToMOFRefMap"] = None, cvlmodel_VariationPoint34: "cvlmodel_CVLModel" = None):
        self.modelTransformationURL = modelTransformationURL
        self.modelTransformationSourceURL = modelTransformationSourceURL
        self.name = name
        self.negativeVariability = negativeVariability
        self.cvlmodel_VariationPoint = cvlmodel_VariationPoint
        self.cvlmodel_VariationPoint17 = cvlmodel_VariationPoint17 if cvlmodel_VariationPoint17 is not None else set()
        self.cvlmodel_VariationPoint34 = cvlmodel_VariationPoint34
        
    @property
    def modelTransformationURL(self) -> str:
        return self.__modelTransformationURL

    @modelTransformationURL.setter
    def modelTransformationURL(self, modelTransformationURL: str):
        self.__modelTransformationURL = modelTransformationURL

    @property
    def modelTransformationSourceURL(self) -> str:
        return self.__modelTransformationSourceURL

    @modelTransformationSourceURL.setter
    def modelTransformationSourceURL(self, modelTransformationSourceURL: str):
        self.__modelTransformationSourceURL = modelTransformationSourceURL

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def negativeVariability(self) -> str:
        return self.__negativeVariability

    @negativeVariability.setter
    def negativeVariability(self, negativeVariability: str):
        self.__negativeVariability = negativeVariability

    @property
    def cvlmodel_VariationPoint(self):
        return self.__cvlmodel_VariationPoint

    @cvlmodel_VariationPoint.setter
    def cvlmodel_VariationPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VariationPoint__cvlmodel_VariationPoint", None)
        self.__cvlmodel_VariationPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpec15"):
                opp_val = getattr(old_value, "cvlmodel_VSpec15", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpec15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpec15"):
                opp_val = getattr(value, "cvlmodel_VSpec15", None)
                setattr(value, "cvlmodel_VSpec15", self)

    @property
    def cvlmodel_VariationPoint34(self):
        return self.__cvlmodel_VariationPoint34

    @cvlmodel_VariationPoint34.setter
    def cvlmodel_VariationPoint34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VariationPoint__cvlmodel_VariationPoint34", None)
        self.__cvlmodel_VariationPoint34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_CVLModel33"):
                opp_val = getattr(old_value, "cvlmodel_CVLModel33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_CVLModel33"):
                opp_val = getattr(value, "cvlmodel_CVLModel33", None)
                if opp_val is None:
                    setattr(value, "cvlmodel_CVLModel33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cvlmodel_VariationPoint17(self):
        return self.__cvlmodel_VariationPoint17

    @cvlmodel_VariationPoint17.setter
    def cvlmodel_VariationPoint17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VariationPoint__cvlmodel_VariationPoint17", None)
        self.__cvlmodel_VariationPoint17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cvlmodel_StringToMOFRefMap"):
                    opp_val = getattr(item, "cvlmodel_StringToMOFRefMap", None)
                    
                    if opp_val == self:
                        setattr(item, "cvlmodel_StringToMOFRefMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cvlmodel_StringToMOFRefMap"):
                    opp_val = getattr(item, "cvlmodel_StringToMOFRefMap", None)
                    
                    setattr(item, "cvlmodel_StringToMOFRefMap", self)
                    

class VSpecResolution:

    pass
class cvlmodel_VClassifierResolution(VSpecResolution):

    def __init__(self, instance: str):
        self.instance = instance
        
    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

class cvlmodel_VariableResolution(VSpecResolution):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cvlmodel_ChoiceResolution(VSpecResolution):

    def __init__(self, decision: str):
        self.decision = decision
        
    @property
    def decision(self) -> str:
        return self.__decision

    @decision.setter
    def decision(self, decision: str):
        self.__decision = decision

class VSpec:

    pass
class cvlmodel_Choice(VSpec):

    pass
class cvlmodel_Multiplicity:

    def __init__(self, min: str, max: str, cvlmodel_Multiplicity8: set["cvlmodel_VSpec"] = None, cvlmodel_Multiplicity: "cvlmodel_VSpec" = None, cvlmodel_Multiplicity11: "cvlmodel_VClassifier" = None):
        self.min = min
        self.max = max
        self.cvlmodel_Multiplicity8 = cvlmodel_Multiplicity8 if cvlmodel_Multiplicity8 is not None else set()
        self.cvlmodel_Multiplicity = cvlmodel_Multiplicity
        self.cvlmodel_Multiplicity11 = cvlmodel_Multiplicity11
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def cvlmodel_Multiplicity11(self):
        return self.__cvlmodel_Multiplicity11

    @cvlmodel_Multiplicity11.setter
    def cvlmodel_Multiplicity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_Multiplicity__cvlmodel_Multiplicity11", None)
        self.__cvlmodel_Multiplicity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VClassifier"):
                opp_val = getattr(old_value, "cvlmodel_VClassifier", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VClassifier"):
                opp_val = getattr(value, "cvlmodel_VClassifier", None)
                setattr(value, "cvlmodel_VClassifier", self)

    @property
    def cvlmodel_Multiplicity8(self):
        return self.__cvlmodel_Multiplicity8

    @cvlmodel_Multiplicity8.setter
    def cvlmodel_Multiplicity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_Multiplicity__cvlmodel_Multiplicity8", None)
        self.__cvlmodel_Multiplicity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cvlmodel_VSpec9"):
                    opp_val = getattr(item, "cvlmodel_VSpec9", None)
                    
                    if opp_val == self:
                        setattr(item, "cvlmodel_VSpec9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cvlmodel_VSpec9"):
                    opp_val = getattr(item, "cvlmodel_VSpec9", None)
                    
                    setattr(item, "cvlmodel_VSpec9", self)
                    

    @property
    def cvlmodel_Multiplicity(self):
        return self.__cvlmodel_Multiplicity

    @cvlmodel_Multiplicity.setter
    def cvlmodel_Multiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_Multiplicity__cvlmodel_Multiplicity", None)
        self.__cvlmodel_Multiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpec"):
                opp_val = getattr(old_value, "cvlmodel_VSpec", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpec"):
                opp_val = getattr(value, "cvlmodel_VSpec", None)
                setattr(value, "cvlmodel_VSpec", self)

class cvlmodel_VClassifier(VSpec):

    pass
class cvlmodel_Variable(VSpec):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class cvlmodel_VSpec(ABC):

    def __init__(self, name: str, mandatory: str, cvlmodel_VSpec9: "cvlmodel_Multiplicity" = None, cvlmodel_VSpec: "cvlmodel_Multiplicity" = None, cvlmodel_VSpec3: "cvlmodel_VSpec" = None, cvlmodel_VSpec1: "cvlmodel_VSpec" = None, cvlmodel_VSpec6: "cvlmodel_VSpec" = None, cvlmodel_VSpec4: set["cvlmodel_VSpec"] = None, cvlmodel_VSpec13: "cvlmodel_VSpecResolution" = None, cvlmodel_VSpec21: "cvlmodel_VSpecTree" = None, cvlmodel_VSpec24: "cvlmodel_VSpecTree" = None, cvlmodel_VSpec15: "cvlmodel_VariationPoint" = None):
        self.name = name
        self.mandatory = mandatory
        self.cvlmodel_VSpec9 = cvlmodel_VSpec9
        self.cvlmodel_VSpec = cvlmodel_VSpec
        self.cvlmodel_VSpec3 = cvlmodel_VSpec3
        self.cvlmodel_VSpec1 = cvlmodel_VSpec1
        self.cvlmodel_VSpec6 = cvlmodel_VSpec6
        self.cvlmodel_VSpec4 = cvlmodel_VSpec4 if cvlmodel_VSpec4 is not None else set()
        self.cvlmodel_VSpec13 = cvlmodel_VSpec13
        self.cvlmodel_VSpec21 = cvlmodel_VSpec21
        self.cvlmodel_VSpec24 = cvlmodel_VSpec24
        self.cvlmodel_VSpec15 = cvlmodel_VSpec15
        
    @property
    def mandatory(self) -> str:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: str):
        self.__mandatory = mandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cvlmodel_VSpec21(self):
        return self.__cvlmodel_VSpec21

    @cvlmodel_VSpec21.setter
    def cvlmodel_VSpec21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec21", None)
        self.__cvlmodel_VSpec21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpecTree"):
                opp_val = getattr(old_value, "cvlmodel_VSpecTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpecTree"):
                opp_val = getattr(value, "cvlmodel_VSpecTree", None)
                if opp_val is None:
                    setattr(value, "cvlmodel_VSpecTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cvlmodel_VSpec1(self):
        return self.__cvlmodel_VSpec1

    @cvlmodel_VSpec1.setter
    def cvlmodel_VSpec1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec1", None)
        self.__cvlmodel_VSpec1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpec3"):
                opp_val = getattr(old_value, "cvlmodel_VSpec3", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpec3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpec3"):
                opp_val = getattr(value, "cvlmodel_VSpec3", None)
                setattr(value, "cvlmodel_VSpec3", self)

    @property
    def cvlmodel_VSpec13(self):
        return self.__cvlmodel_VSpec13

    @cvlmodel_VSpec13.setter
    def cvlmodel_VSpec13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec13", None)
        self.__cvlmodel_VSpec13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpecResolution"):
                opp_val = getattr(old_value, "cvlmodel_VSpecResolution", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpecResolution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpecResolution"):
                opp_val = getattr(value, "cvlmodel_VSpecResolution", None)
                setattr(value, "cvlmodel_VSpecResolution", self)

    @property
    def cvlmodel_VSpec6(self):
        return self.__cvlmodel_VSpec6

    @cvlmodel_VSpec6.setter
    def cvlmodel_VSpec6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec6", None)
        self.__cvlmodel_VSpec6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpec4"):
                opp_val = getattr(old_value, "cvlmodel_VSpec4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpec4"):
                opp_val = getattr(value, "cvlmodel_VSpec4", None)
                if opp_val is None:
                    setattr(value, "cvlmodel_VSpec4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cvlmodel_VSpec(self):
        return self.__cvlmodel_VSpec

    @cvlmodel_VSpec.setter
    def cvlmodel_VSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec", None)
        self.__cvlmodel_VSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_Multiplicity"):
                opp_val = getattr(old_value, "cvlmodel_Multiplicity", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_Multiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_Multiplicity"):
                opp_val = getattr(value, "cvlmodel_Multiplicity", None)
                setattr(value, "cvlmodel_Multiplicity", self)

    @property
    def cvlmodel_VSpec3(self):
        return self.__cvlmodel_VSpec3

    @cvlmodel_VSpec3.setter
    def cvlmodel_VSpec3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec3", None)
        self.__cvlmodel_VSpec3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpec1"):
                opp_val = getattr(old_value, "cvlmodel_VSpec1", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpec1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpec1"):
                opp_val = getattr(value, "cvlmodel_VSpec1", None)
                setattr(value, "cvlmodel_VSpec1", self)

    @property
    def cvlmodel_VSpec4(self):
        return self.__cvlmodel_VSpec4

    @cvlmodel_VSpec4.setter
    def cvlmodel_VSpec4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec4", None)
        self.__cvlmodel_VSpec4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cvlmodel_VSpec6"):
                    opp_val = getattr(item, "cvlmodel_VSpec6", None)
                    
                    if opp_val == self:
                        setattr(item, "cvlmodel_VSpec6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cvlmodel_VSpec6"):
                    opp_val = getattr(item, "cvlmodel_VSpec6", None)
                    
                    setattr(item, "cvlmodel_VSpec6", self)
                    

    @property
    def cvlmodel_VSpec9(self):
        return self.__cvlmodel_VSpec9

    @cvlmodel_VSpec9.setter
    def cvlmodel_VSpec9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec9", None)
        self.__cvlmodel_VSpec9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_Multiplicity8"):
                opp_val = getattr(old_value, "cvlmodel_Multiplicity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_Multiplicity8"):
                opp_val = getattr(value, "cvlmodel_Multiplicity8", None)
                if opp_val is None:
                    setattr(value, "cvlmodel_Multiplicity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cvlmodel_VSpec24(self):
        return self.__cvlmodel_VSpec24

    @cvlmodel_VSpec24.setter
    def cvlmodel_VSpec24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec24", None)
        self.__cvlmodel_VSpec24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VSpecTree23"):
                opp_val = getattr(old_value, "cvlmodel_VSpecTree23", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VSpecTree23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VSpecTree23"):
                opp_val = getattr(value, "cvlmodel_VSpecTree23", None)
                setattr(value, "cvlmodel_VSpecTree23", self)

    @property
    def cvlmodel_VSpec15(self):
        return self.__cvlmodel_VSpec15

    @cvlmodel_VSpec15.setter
    def cvlmodel_VSpec15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cvlmodel_VSpec__cvlmodel_VSpec15", None)
        self.__cvlmodel_VSpec15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cvlmodel_VariationPoint"):
                opp_val = getattr(old_value, "cvlmodel_VariationPoint", None)
                if opp_val == self:
                    setattr(old_value, "cvlmodel_VariationPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cvlmodel_VariationPoint"):
                opp_val = getattr(value, "cvlmodel_VariationPoint", None)
                setattr(value, "cvlmodel_VariationPoint", self)

    def isClon(self) -> str:
        # TODO: Implement isClon method
        pass

    def isCloneable(self) -> str:
        # TODO: Implement isCloneable method
        pass

    def isRoot(self) -> str:
        # TODO: Implement isRoot method
        pass
