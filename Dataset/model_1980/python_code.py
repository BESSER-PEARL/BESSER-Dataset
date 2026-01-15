from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TraceMetamodel_EObject:

    pass
class TraceMetamodel_TraceLinkEnd:

    def __init__(self, name: str, type: str, TraceMetamodel_TraceLinkEnd: "TraceMetamodel_TraceLink" = None, TraceMetamodel_TraceLinkEnd5: "TraceMetamodel_TraceLink" = None, TraceMetamodel_TraceLinkEnd7: "TraceMetamodel_EObject" = None):
        self.name = name
        self.type = type
        self.TraceMetamodel_TraceLinkEnd = TraceMetamodel_TraceLinkEnd
        self.TraceMetamodel_TraceLinkEnd5 = TraceMetamodel_TraceLinkEnd5
        self.TraceMetamodel_TraceLinkEnd7 = TraceMetamodel_TraceLinkEnd7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def TraceMetamodel_TraceLinkEnd5(self):
        return self.__TraceMetamodel_TraceLinkEnd5

    @TraceMetamodel_TraceLinkEnd5.setter
    def TraceMetamodel_TraceLinkEnd5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceLinkEnd__TraceMetamodel_TraceLinkEnd5", None)
        self.__TraceMetamodel_TraceLinkEnd5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceMetamodel_TraceLink4"):
                opp_val = getattr(old_value, "TraceMetamodel_TraceLink4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceMetamodel_TraceLink4"):
                opp_val = getattr(value, "TraceMetamodel_TraceLink4", None)
                if opp_val is None:
                    setattr(value, "TraceMetamodel_TraceLink4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TraceMetamodel_TraceLinkEnd7(self):
        return self.__TraceMetamodel_TraceLinkEnd7

    @TraceMetamodel_TraceLinkEnd7.setter
    def TraceMetamodel_TraceLinkEnd7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceLinkEnd__TraceMetamodel_TraceLinkEnd7", None)
        self.__TraceMetamodel_TraceLinkEnd7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceMetamodel_EObject"):
                opp_val = getattr(old_value, "TraceMetamodel_EObject", None)
                if opp_val == self:
                    setattr(old_value, "TraceMetamodel_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceMetamodel_EObject"):
                opp_val = getattr(value, "TraceMetamodel_EObject", None)
                setattr(value, "TraceMetamodel_EObject", self)

    @property
    def TraceMetamodel_TraceLinkEnd(self):
        return self.__TraceMetamodel_TraceLinkEnd

    @TraceMetamodel_TraceLinkEnd.setter
    def TraceMetamodel_TraceLinkEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceLinkEnd__TraceMetamodel_TraceLinkEnd", None)
        self.__TraceMetamodel_TraceLinkEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceMetamodel_TraceLink2"):
                opp_val = getattr(old_value, "TraceMetamodel_TraceLink2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceMetamodel_TraceLink2"):
                opp_val = getattr(value, "TraceMetamodel_TraceLink2", None)
                if opp_val is None:
                    setattr(value, "TraceMetamodel_TraceLink2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TraceMetamodel_TraceLink:

    def __init__(self, name: str, trule: str, id: str, isPartial: bool, isNonInjective: bool, TraceMetamodel_TraceLink: "TraceMetamodel_TraceModel" = None, TraceMetamodel_TraceLink2: set["TraceMetamodel_TraceLinkEnd"] = None, TraceMetamodel_TraceLink4: set["TraceMetamodel_TraceLinkEnd"] = None):
        self.name = name
        self.trule = trule
        self.id = id
        self.isPartial = isPartial
        self.isNonInjective = isNonInjective
        self.TraceMetamodel_TraceLink = TraceMetamodel_TraceLink
        self.TraceMetamodel_TraceLink2 = TraceMetamodel_TraceLink2 if TraceMetamodel_TraceLink2 is not None else set()
        self.TraceMetamodel_TraceLink4 = TraceMetamodel_TraceLink4 if TraceMetamodel_TraceLink4 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isNonInjective(self) -> bool:
        return self.__isNonInjective

    @isNonInjective.setter
    def isNonInjective(self, isNonInjective: bool):
        self.__isNonInjective = isNonInjective

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isPartial(self) -> bool:
        return self.__isPartial

    @isPartial.setter
    def isPartial(self, isPartial: bool):
        self.__isPartial = isPartial

    @property
    def trule(self) -> str:
        return self.__trule

    @trule.setter
    def trule(self, trule: str):
        self.__trule = trule

    @property
    def TraceMetamodel_TraceLink(self):
        return self.__TraceMetamodel_TraceLink

    @TraceMetamodel_TraceLink.setter
    def TraceMetamodel_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceLink__TraceMetamodel_TraceLink", None)
        self.__TraceMetamodel_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceMetamodel_TraceModel"):
                opp_val = getattr(old_value, "TraceMetamodel_TraceModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceMetamodel_TraceModel"):
                opp_val = getattr(value, "TraceMetamodel_TraceModel", None)
                if opp_val is None:
                    setattr(value, "TraceMetamodel_TraceModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TraceMetamodel_TraceLink4(self):
        return self.__TraceMetamodel_TraceLink4

    @TraceMetamodel_TraceLink4.setter
    def TraceMetamodel_TraceLink4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceLink__TraceMetamodel_TraceLink4", None)
        self.__TraceMetamodel_TraceLink4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceMetamodel_TraceLinkEnd5"):
                    opp_val = getattr(item, "TraceMetamodel_TraceLinkEnd5", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceMetamodel_TraceLinkEnd5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceMetamodel_TraceLinkEnd5"):
                    opp_val = getattr(item, "TraceMetamodel_TraceLinkEnd5", None)
                    
                    setattr(item, "TraceMetamodel_TraceLinkEnd5", self)
                    

    @property
    def TraceMetamodel_TraceLink2(self):
        return self.__TraceMetamodel_TraceLink2

    @TraceMetamodel_TraceLink2.setter
    def TraceMetamodel_TraceLink2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceLink__TraceMetamodel_TraceLink2", None)
        self.__TraceMetamodel_TraceLink2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceMetamodel_TraceLinkEnd"):
                    opp_val = getattr(item, "TraceMetamodel_TraceLinkEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceMetamodel_TraceLinkEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceMetamodel_TraceLinkEnd"):
                    opp_val = getattr(item, "TraceMetamodel_TraceLinkEnd", None)
                    
                    setattr(item, "TraceMetamodel_TraceLinkEnd", self)
                    

class TraceMetamodel_TraceModel:

    def __init__(self, name: str, TraceMetamodel_TraceModel: set["TraceMetamodel_TraceLink"] = None):
        self.name = name
        self.TraceMetamodel_TraceModel = TraceMetamodel_TraceModel if TraceMetamodel_TraceModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TraceMetamodel_TraceModel(self):
        return self.__TraceMetamodel_TraceModel

    @TraceMetamodel_TraceModel.setter
    def TraceMetamodel_TraceModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TraceMetamodel_TraceModel__TraceMetamodel_TraceModel", None)
        self.__TraceMetamodel_TraceModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceMetamodel_TraceLink"):
                    opp_val = getattr(item, "TraceMetamodel_TraceLink", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceMetamodel_TraceLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceMetamodel_TraceLink"):
                    opp_val = getattr(item, "TraceMetamodel_TraceLink", None)
                    
                    setattr(item, "TraceMetamodel_TraceLink", self)
                    
