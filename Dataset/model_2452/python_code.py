from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExmodeDatatype(Enum):
    strict = "strict"
    lax = "lax"
class AdapterToken(Enum):
    DESCRIPTION = "DESCRIPTION"
    DATAMODEL = "DATAMODEL"
class HistoryTypeDatatype(Enum):
    shallow = "shallow"
    deep = "deep"


############################################
# Definition of Classes
############################################

class scxml_Description:

    def __init__(self, value: str, scxml_Description: "scxml_DescriptionContainer" = None):
        self.value = value
        self.scxml_Description = scxml_Description
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def scxml_Description(self):
        return self.__scxml_Description

    @scxml_Description.setter
    def scxml_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Description__scxml_Description", None)
        self.__scxml_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DescriptionContainer"):
                opp_val = getattr(old_value, "scxml_DescriptionContainer", None)
                if opp_val == self:
                    setattr(old_value, "scxml_DescriptionContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DescriptionContainer"):
                opp_val = getattr(value, "scxml_DescriptionContainer", None)
                setattr(value, "scxml_DescriptionContainer", self)

class IAdaptable:

    pass
class scxml_DescriptionContainer(IAdaptable):

    def __init__(self, scxml_DescriptionContainer: "scxml_Description" = None):
        self.scxml_DescriptionContainer = scxml_DescriptionContainer
        
        pass
    @property
    def scxml_DescriptionContainer(self):
        return self.__scxml_DescriptionContainer

    @scxml_DescriptionContainer.setter
    def scxml_DescriptionContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DescriptionContainer__scxml_DescriptionContainer", None)
        self.__scxml_DescriptionContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Description"):
                opp_val = getattr(old_value, "scxml_Description", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Description"):
                opp_val = getattr(value, "scxml_Description", None)
                setattr(value, "scxml_Description", self)

    def getAdapter(self, scxml_adapter) :
        # TODO: Implement getAdapter method
        pass

class scxml_DatamodelContainer(IAdaptable):

    def __init__(self, scxml_DatamodelContainer: "scxml_Datamodel" = None):
        self.scxml_DatamodelContainer = scxml_DatamodelContainer
        
        pass
    @property
    def scxml_DatamodelContainer(self):
        return self.__scxml_DatamodelContainer

    @scxml_DatamodelContainer.setter
    def scxml_DatamodelContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DatamodelContainer__scxml_DatamodelContainer", None)
        self.__scxml_DatamodelContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Datamodel55"):
                opp_val = getattr(old_value, "scxml_Datamodel55", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Datamodel55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Datamodel55"):
                opp_val = getattr(value, "scxml_Datamodel55", None)
                setattr(value, "scxml_Datamodel55", self)

    def getAdapter(self, scxml_adapter) :
        # TODO: Implement getAdapter method
        pass

class scxml_EClass:

    pass
class scxml_IAdaptable(ABC):

    pass
class Data:

    pass
class scxml_XData(Data):

    pass
class scxml_XObject:

    def __init__(self, nsUri: str, classifierName: str, exchange: bool, scxml_XObject: "scxml_EClass" = None):
        self.nsUri = nsUri
        self.classifierName = classifierName
        self.exchange = exchange
        self.scxml_XObject = scxml_XObject
        
        pass
    @property
    def nsUri(self):
        return self.__nsUri

    @nsUri.setter
    def nsUri(self, nsUri: str):
        self.__nsUri = nsUri


    @property
    def exchange(self):
        return self.__exchange

    @exchange.setter
    def exchange(self, exchange: bool):
        self.__exchange = exchange


    @property
    def classifierName(self):
        return self.__classifierName

    @classifierName.setter
    def classifierName(self, classifierName: str):
        self.__classifierName = classifierName


    @property
    def scxml_XObject(self):
        return self.__scxml_XObject

    @scxml_XObject.setter
    def scxml_XObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_XObject__scxml_XObject", None)
        self.__scxml_XObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_EClass"):
                opp_val = getattr(old_value, "scxml_EClass", None)
                if opp_val == self:
                    setattr(old_value, "scxml_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_EClass"):
                opp_val = getattr(value, "scxml_EClass", None)
                setattr(value, "scxml_EClass", self)

    def registerAdapter(self):
        # TODO: Implement registerAdapter method
        pass

class scxml_Else:

    pass
class Conditional:

    pass
class scxml_ElseIf(Conditional):

    pass
class scxml_Conditional:

    def __init__(self, cond: str):
        self.cond = cond
        
        pass
    @property
    def cond(self):
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond


class scxml_Validate:

    def __init__(self, location: str, schema: str, scxml_Validate: "scxml_ExecutableContent" = None):
        self.location = location
        self.schema = schema
        self.scxml_Validate = scxml_Validate
        
        pass
    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def scxml_Validate(self):
        return self.__scxml_Validate

    @scxml_Validate.setter
    def scxml_Validate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Validate__scxml_Validate", None)
        self.__scxml_Validate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent39"):
                opp_val = getattr(old_value, "scxml_ExecutableContent39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent39"):
                opp_val = getattr(value, "scxml_ExecutableContent39", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Assign:

    def __init__(self, location: str, expr: str, name: str, scxml_Assign: "scxml_ExecutableContent" = None):
        self.location = location
        self.expr = expr
        self.name = name
        self.scxml_Assign = scxml_Assign
        
        pass
    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def scxml_Assign(self):
        return self.__scxml_Assign

    @scxml_Assign.setter
    def scxml_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Assign__scxml_Assign", None)
        self.__scxml_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent37"):
                opp_val = getattr(old_value, "scxml_ExecutableContent37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent37"):
                opp_val = getattr(value, "scxml_ExecutableContent37", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Cancel:

    def __init__(self, sendid: str, sendidexpr: str, scxml_Cancel: "scxml_ExecutableContent" = None):
        self.sendid = sendid
        self.sendidexpr = sendidexpr
        self.scxml_Cancel = scxml_Cancel
        
        pass
    @property
    def sendidexpr(self):
        return self.__sendidexpr

    @sendidexpr.setter
    def sendidexpr(self, sendidexpr: str):
        self.__sendidexpr = sendidexpr


    @property
    def sendid(self):
        return self.__sendid

    @sendid.setter
    def sendid(self, sendid: str):
        self.__sendid = sendid


    @property
    def scxml_Cancel(self):
        return self.__scxml_Cancel

    @scxml_Cancel.setter
    def scxml_Cancel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Cancel__scxml_Cancel", None)
        self.__scxml_Cancel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent35"):
                opp_val = getattr(old_value, "scxml_ExecutableContent35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent35"):
                opp_val = getattr(value, "scxml_ExecutableContent35", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Donedata:

    pass
class scxml_Send(Donedata):

    def __init__(self, event: str, eventexpr: str, target: str, targetexpr: str, type: str, typeexpr: str, id: str, idlocation: str, delay: str, delayexpr: str, namelist: str, hints: str, hintsexpr: str, scxml_Send: "scxml_ExecutableContent" = None):
        self.event = event
        self.eventexpr = eventexpr
        self.target = target
        self.targetexpr = targetexpr
        self.type = type
        self.typeexpr = typeexpr
        self.id = id
        self.idlocation = idlocation
        self.delay = delay
        self.delayexpr = delayexpr
        self.namelist = namelist
        self.hints = hints
        self.hintsexpr = hintsexpr
        self.scxml_Send = scxml_Send
        
        pass
    @property
    def namelist(self):
        return self.__namelist

    @namelist.setter
    def namelist(self, namelist: str):
        self.__namelist = namelist


    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay


    @property
    def delayexpr(self):
        return self.__delayexpr

    @delayexpr.setter
    def delayexpr(self, delayexpr: str):
        self.__delayexpr = delayexpr


    @property
    def hints(self):
        return self.__hints

    @hints.setter
    def hints(self, hints: str):
        self.__hints = hints


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def typeexpr(self):
        return self.__typeexpr

    @typeexpr.setter
    def typeexpr(self, typeexpr: str):
        self.__typeexpr = typeexpr


    @property
    def hintsexpr(self):
        return self.__hintsexpr

    @hintsexpr.setter
    def hintsexpr(self, hintsexpr: str):
        self.__hintsexpr = hintsexpr


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def targetexpr(self):
        return self.__targetexpr

    @targetexpr.setter
    def targetexpr(self, targetexpr: str):
        self.__targetexpr = targetexpr


    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event


    @property
    def eventexpr(self):
        return self.__eventexpr

    @eventexpr.setter
    def eventexpr(self, eventexpr: str):
        self.__eventexpr = eventexpr


    @property
    def idlocation(self):
        return self.__idlocation

    @idlocation.setter
    def idlocation(self, idlocation: str):
        self.__idlocation = idlocation


    @property
    def scxml_Send(self):
        return self.__scxml_Send

    @scxml_Send.setter
    def scxml_Send(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Send__scxml_Send", None)
        self.__scxml_Send = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent33"):
                opp_val = getattr(old_value, "scxml_ExecutableContent33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent33"):
                opp_val = getattr(value, "scxml_ExecutableContent33", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ExecutableContent:

    def __init__(self, group: str, scxml_ExecutableContent: set["scxml_If"] = None, scxml_ExecutableContent29: set["scxml_Log"] = None, scxml_ExecutableContent31: set["scxml_Raise"] = None, scxml_ExecutableContent33: set["scxml_Send"] = None, scxml_ExecutableContent35: set["scxml_Cancel"] = None, scxml_ExecutableContent37: set["scxml_Assign"] = None, scxml_ExecutableContent39: set["scxml_Validate"] = None, scxml_ExecutableContent41: set["scxml_Script"] = None, scxml_ExecutableContent49: "scxml_Invoke" = None):
        self.group = group
        self.scxml_ExecutableContent = scxml_ExecutableContent if scxml_ExecutableContent is not None else set()
        self.scxml_ExecutableContent29 = scxml_ExecutableContent29 if scxml_ExecutableContent29 is not None else set()
        self.scxml_ExecutableContent31 = scxml_ExecutableContent31 if scxml_ExecutableContent31 is not None else set()
        self.scxml_ExecutableContent33 = scxml_ExecutableContent33 if scxml_ExecutableContent33 is not None else set()
        self.scxml_ExecutableContent35 = scxml_ExecutableContent35 if scxml_ExecutableContent35 is not None else set()
        self.scxml_ExecutableContent37 = scxml_ExecutableContent37 if scxml_ExecutableContent37 is not None else set()
        self.scxml_ExecutableContent39 = scxml_ExecutableContent39 if scxml_ExecutableContent39 is not None else set()
        self.scxml_ExecutableContent41 = scxml_ExecutableContent41 if scxml_ExecutableContent41 is not None else set()
        self.scxml_ExecutableContent49 = scxml_ExecutableContent49
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def scxml_ExecutableContent41(self):
        return self.__scxml_ExecutableContent41

    @scxml_ExecutableContent41.setter
    def scxml_ExecutableContent41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent41", None)
        self.__scxml_ExecutableContent41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Script42"):
                    opp_val = getattr(item, "scxml_Script42", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Script42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Script42"):
                    opp_val = getattr(item, "scxml_Script42", None)
                    
                    setattr(item, "scxml_Script42", self)
                    

    @property
    def scxml_ExecutableContent29(self):
        return self.__scxml_ExecutableContent29

    @scxml_ExecutableContent29.setter
    def scxml_ExecutableContent29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent29", None)
        self.__scxml_ExecutableContent29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Log"):
                    opp_val = getattr(item, "scxml_Log", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Log", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Log"):
                    opp_val = getattr(item, "scxml_Log", None)
                    
                    setattr(item, "scxml_Log", self)
                    

    @property
    def scxml_ExecutableContent31(self):
        return self.__scxml_ExecutableContent31

    @scxml_ExecutableContent31.setter
    def scxml_ExecutableContent31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent31", None)
        self.__scxml_ExecutableContent31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Raise"):
                    opp_val = getattr(item, "scxml_Raise", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Raise", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Raise"):
                    opp_val = getattr(item, "scxml_Raise", None)
                    
                    setattr(item, "scxml_Raise", self)
                    

    @property
    def scxml_ExecutableContent(self):
        return self.__scxml_ExecutableContent

    @scxml_ExecutableContent.setter
    def scxml_ExecutableContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent", None)
        self.__scxml_ExecutableContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_If"):
                    opp_val = getattr(item, "scxml_If", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_If", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_If"):
                    opp_val = getattr(item, "scxml_If", None)
                    
                    setattr(item, "scxml_If", self)
                    

    @property
    def scxml_ExecutableContent33(self):
        return self.__scxml_ExecutableContent33

    @scxml_ExecutableContent33.setter
    def scxml_ExecutableContent33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent33", None)
        self.__scxml_ExecutableContent33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Send"):
                    opp_val = getattr(item, "scxml_Send", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Send", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Send"):
                    opp_val = getattr(item, "scxml_Send", None)
                    
                    setattr(item, "scxml_Send", self)
                    

    @property
    def scxml_ExecutableContent39(self):
        return self.__scxml_ExecutableContent39

    @scxml_ExecutableContent39.setter
    def scxml_ExecutableContent39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent39", None)
        self.__scxml_ExecutableContent39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Validate"):
                    opp_val = getattr(item, "scxml_Validate", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Validate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Validate"):
                    opp_val = getattr(item, "scxml_Validate", None)
                    
                    setattr(item, "scxml_Validate", self)
                    

    @property
    def scxml_ExecutableContent35(self):
        return self.__scxml_ExecutableContent35

    @scxml_ExecutableContent35.setter
    def scxml_ExecutableContent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent35", None)
        self.__scxml_ExecutableContent35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Cancel"):
                    opp_val = getattr(item, "scxml_Cancel", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Cancel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Cancel"):
                    opp_val = getattr(item, "scxml_Cancel", None)
                    
                    setattr(item, "scxml_Cancel", self)
                    

    @property
    def scxml_ExecutableContent49(self):
        return self.__scxml_ExecutableContent49

    @scxml_ExecutableContent49.setter
    def scxml_ExecutableContent49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent49", None)
        self.__scxml_ExecutableContent49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Invoke48"):
                opp_val = getattr(old_value, "scxml_Invoke48", None)
                if opp_val == self:
                    setattr(old_value, "scxml_Invoke48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Invoke48"):
                opp_val = getattr(value, "scxml_Invoke48", None)
                setattr(value, "scxml_Invoke48", self)

    @property
    def scxml_ExecutableContent37(self):
        return self.__scxml_ExecutableContent37

    @scxml_ExecutableContent37.setter
    def scxml_ExecutableContent37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ExecutableContent__scxml_ExecutableContent37", None)
        self.__scxml_ExecutableContent37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Assign"):
                    opp_val = getattr(item, "scxml_Assign", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Assign", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Assign"):
                    opp_val = getattr(item, "scxml_Assign", None)
                    
                    setattr(item, "scxml_Assign", self)
                    

class InitialState:

    pass
class scxml_Invoke(Donedata):

    def __init__(self, typeexpr: str, src: str, srcexpr: str, id: str, idlocation: str, namelist: str, autoforward: str, type: str, scxml_Invoke: "scxml_SimpleState" = None, scxml_Invoke48: "scxml_ExecutableContent" = None):
        self.typeexpr = typeexpr
        self.src = src
        self.srcexpr = srcexpr
        self.id = id
        self.idlocation = idlocation
        self.namelist = namelist
        self.autoforward = autoforward
        self.type = type
        self.scxml_Invoke = scxml_Invoke
        self.scxml_Invoke48 = scxml_Invoke48
        
        pass
    @property
    def namelist(self):
        return self.__namelist

    @namelist.setter
    def namelist(self, namelist: str):
        self.__namelist = namelist


    @property
    def typeexpr(self):
        return self.__typeexpr

    @typeexpr.setter
    def typeexpr(self, typeexpr: str):
        self.__typeexpr = typeexpr


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def idlocation(self):
        return self.__idlocation

    @idlocation.setter
    def idlocation(self, idlocation: str):
        self.__idlocation = idlocation


    @property
    def autoforward(self):
        return self.__autoforward

    @autoforward.setter
    def autoforward(self, autoforward: str):
        self.__autoforward = autoforward


    @property
    def srcexpr(self):
        return self.__srcexpr

    @srcexpr.setter
    def srcexpr(self, srcexpr: str):
        self.__srcexpr = srcexpr


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def scxml_Invoke48(self):
        return self.__scxml_Invoke48

    @scxml_Invoke48.setter
    def scxml_Invoke48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Invoke__scxml_Invoke48", None)
        self.__scxml_Invoke48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent49"):
                opp_val = getattr(old_value, "scxml_ExecutableContent49", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ExecutableContent49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent49"):
                opp_val = getattr(value, "scxml_ExecutableContent49", None)
                setattr(value, "scxml_ExecutableContent49", self)

    @property
    def scxml_Invoke(self):
        return self.__scxml_Invoke

    @scxml_Invoke.setter
    def scxml_Invoke(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Invoke__scxml_Invoke", None)
        self.__scxml_Invoke = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_SimpleState26"):
                opp_val = getattr(old_value, "scxml_SimpleState26", None)
                if opp_val == self:
                    setattr(old_value, "scxml_SimpleState26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_SimpleState26"):
                opp_val = getattr(value, "scxml_SimpleState26", None)
                setattr(value, "scxml_SimpleState26", self)

class scxml_AbstractSimpleState(ABC):

    pass
class State:

    pass
class scxml_Raise(Donedata):

    def __init__(self, event: str, scxml_Raise: "scxml_ExecutableContent" = None):
        self.event = event
        self.scxml_Raise = scxml_Raise
        
        pass
    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event


    @property
    def scxml_Raise(self):
        return self.__scxml_Raise

    @scxml_Raise.setter
    def scxml_Raise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Raise__scxml_Raise", None)
        self.__scxml_Raise = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent31"):
                opp_val = getattr(old_value, "scxml_ExecutableContent31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent31"):
                opp_val = getattr(value, "scxml_ExecutableContent31", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_Log:

    def __init__(self, expr: str, level: str, label: str, scxml_Log: "scxml_ExecutableContent" = None):
        self.expr = expr
        self.level = level
        self.label = label
        self.scxml_Log = scxml_Log
        
        pass
    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def scxml_Log(self):
        return self.__scxml_Log

    @scxml_Log.setter
    def scxml_Log(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Log__scxml_Log", None)
        self.__scxml_Log = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent29"):
                opp_val = getattr(old_value, "scxml_ExecutableContent29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent29"):
                opp_val = getattr(value, "scxml_ExecutableContent29", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_EObject:

    pass
class scxml_Donedata:

    pass
class scxml_Param:

    def __init__(self, name: str, expr: str, scxml_Param: "scxml_Donedata" = None):
        self.name = name
        self.expr = expr
        self.scxml_Param = scxml_Param
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


    @property
    def scxml_Param(self):
        return self.__scxml_Param

    @scxml_Param.setter
    def scxml_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Param__scxml_Param", None)
        self.__scxml_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Donedata"):
                opp_val = getattr(old_value, "scxml_Donedata", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Donedata"):
                opp_val = getattr(value, "scxml_Donedata", None)
                if opp_val is None:
                    setattr(value, "scxml_Donedata", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transition:

    pass
class scxml_Content:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class scxml_ParallelState(State):

    pass
class scxml_AbstractState(ABC):

    pass
class scxml_CondEventTransition(Transition):

    def __init__(self, cond: str, event: str, scxml_CondEventTransition: "scxml_TransitionSource" = None):
        self.cond = cond
        self.event = event
        self.scxml_CondEventTransition = scxml_CondEventTransition
        
        pass
    @property
    def cond(self):
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond


    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event


    @property
    def scxml_CondEventTransition(self):
        return self.__scxml_CondEventTransition

    @scxml_CondEventTransition.setter
    def scxml_CondEventTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_CondEventTransition__scxml_CondEventTransition", None)
        self.__scxml_CondEventTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_TransitionSource"):
                opp_val = getattr(old_value, "scxml_TransitionSource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_TransitionSource"):
                opp_val = getattr(value, "scxml_TransitionSource", None)
                if opp_val is None:
                    setattr(value, "scxml_TransitionSource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class scxml_TransitionTarget(Node):

    def __init__(self, id: str, scxml_TransitionTarget: "scxml_Transition" = None, scxml_TransitionTarget18: "scxml_AbstractSimpleState" = None):
        self.id = id
        self.scxml_TransitionTarget = scxml_TransitionTarget
        self.scxml_TransitionTarget18 = scxml_TransitionTarget18
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def scxml_TransitionTarget18(self):
        return self.__scxml_TransitionTarget18

    @scxml_TransitionTarget18.setter
    def scxml_TransitionTarget18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_TransitionTarget__scxml_TransitionTarget18", None)
        self.__scxml_TransitionTarget18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_AbstractSimpleState"):
                opp_val = getattr(old_value, "scxml_AbstractSimpleState", None)
                if opp_val == self:
                    setattr(old_value, "scxml_AbstractSimpleState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_AbstractSimpleState"):
                opp_val = getattr(value, "scxml_AbstractSimpleState", None)
                setattr(value, "scxml_AbstractSimpleState", self)

    @property
    def scxml_TransitionTarget(self):
        return self.__scxml_TransitionTarget

    @scxml_TransitionTarget.setter
    def scxml_TransitionTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_TransitionTarget__scxml_TransitionTarget", None)
        self.__scxml_TransitionTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Transition"):
                opp_val = getattr(old_value, "scxml_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Transition"):
                opp_val = getattr(value, "scxml_Transition", None)
                if opp_val is None:
                    setattr(value, "scxml_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_TransitionSource(Node):

    pass
class ExecutableContent:

    pass
class scxml_OnExit(ExecutableContent):

    pass
class scxml_OnEntry(ExecutableContent):

    pass
class scxml_If(Conditional, ExecutableContent):

    pass
class TransitionSource:

    pass
class TransitionTarget:

    pass
class scxml_HistoryState(TransitionTarget, InitialState):

    def __init__(self, type: str, scxml_HistoryState: "scxml_State" = None):
        self.type = type
        self.scxml_HistoryState = scxml_HistoryState
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def scxml_HistoryState(self):
        return self.__scxml_HistoryState

    @scxml_HistoryState.setter
    def scxml_HistoryState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_HistoryState__scxml_HistoryState", None)
        self.__scxml_HistoryState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_State"):
                opp_val = getattr(old_value, "scxml_State", None)
                if opp_val == self:
                    setattr(old_value, "scxml_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_State"):
                opp_val = getattr(value, "scxml_State", None)
                setattr(value, "scxml_State", self)

class scxml_FinalState(TransitionTarget):

    pass
class scxml_Script:

    def __init__(self, value: str, scxml_Script: "scxml_StateChart" = None, scxml_Script42: "scxml_ExecutableContent" = None):
        self.value = value
        self.scxml_Script = scxml_Script
        self.scxml_Script42 = scxml_Script42
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def scxml_Script(self):
        return self.__scxml_Script

    @scxml_Script.setter
    def scxml_Script(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Script__scxml_Script", None)
        self.__scxml_Script = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_StateChart"):
                opp_val = getattr(old_value, "scxml_StateChart", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_StateChart"):
                opp_val = getattr(value, "scxml_StateChart", None)
                if opp_val is None:
                    setattr(value, "scxml_StateChart", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_Script42(self):
        return self.__scxml_Script42

    @scxml_Script42.setter
    def scxml_Script42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Script__scxml_Script42", None)
        self.__scxml_Script42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ExecutableContent41"):
                opp_val = getattr(old_value, "scxml_ExecutableContent41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ExecutableContent41"):
                opp_val = getattr(value, "scxml_ExecutableContent41", None)
                if opp_val is None:
                    setattr(value, "scxml_ExecutableContent41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DescriptionContainer:

    pass
class scxml_Node(DescriptionContainer):

    pass
class scxml_Data(DescriptionContainer):

    def __init__(self, id: str, src: str, expr: str, scxml_Data: "scxml_Datamodel" = None):
        self.id = id
        self.src = src
        self.expr = expr
        self.scxml_Data = scxml_Data
        
        pass
    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


    @property
    def scxml_Data(self):
        return self.__scxml_Data

    @scxml_Data.setter
    def scxml_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Data__scxml_Data", None)
        self.__scxml_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_Datamodel"):
                opp_val = getattr(old_value, "scxml_Datamodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_Datamodel"):
                opp_val = getattr(value, "scxml_Datamodel", None)
                if opp_val is None:
                    setattr(value, "scxml_Datamodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_InitialState(DescriptionContainer):

    pass
class scxml_Datamodel(DescriptionContainer):

    def __init__(self, schema: str, scxml_Datamodel: set["scxml_Data"] = None, scxml_Datamodel55: "scxml_DatamodelContainer" = None):
        self.schema = schema
        self.scxml_Datamodel = scxml_Datamodel if scxml_Datamodel is not None else set()
        self.scxml_Datamodel55 = scxml_Datamodel55
        
        pass
    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema


    @property
    def scxml_Datamodel(self):
        return self.__scxml_Datamodel

    @scxml_Datamodel.setter
    def scxml_Datamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Datamodel__scxml_Datamodel", None)
        self.__scxml_Datamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Data"):
                    opp_val = getattr(item, "scxml_Data", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Data"):
                    opp_val = getattr(item, "scxml_Data", None)
                    
                    setattr(item, "scxml_Data", self)
                    

    @property
    def scxml_Datamodel55(self):
        return self.__scxml_Datamodel55

    @scxml_Datamodel55.setter
    def scxml_Datamodel55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_Datamodel__scxml_Datamodel55", None)
        self.__scxml_Datamodel55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DatamodelContainer"):
                opp_val = getattr(old_value, "scxml_DatamodelContainer", None)
                if opp_val == self:
                    setattr(old_value, "scxml_DatamodelContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DatamodelContainer"):
                opp_val = getattr(value, "scxml_DatamodelContainer", None)
                setattr(value, "scxml_DatamodelContainer", self)

class scxml_Transition(DescriptionContainer, ExecutableContent):

    pass
class DatamodelContainer:

    pass
class AbstractSimpleState:

    pass
class scxml_SimpleState(State, AbstractSimpleState):

    pass
class AbstractState:

    pass
class scxml_State(TransitionTarget, AbstractState, TransitionSource, DatamodelContainer):

    pass
class scxml_StateChart(DescriptionContainer, AbstractState, DatamodelContainer, AbstractSimpleState):

    def __init__(self, xmlns: str, version: str, profile: str, exmode: str, id: str, scxml_StateChart: set["scxml_Script"] = None):
        self.xmlns = xmlns
        self.version = version
        self.profile = profile
        self.exmode = exmode
        self.id = id
        self.scxml_StateChart = scxml_StateChart if scxml_StateChart is not None else set()
        
        pass
    @property
    def profile(self):
        return self.__profile

    @profile.setter
    def profile(self, profile: str):
        self.__profile = profile


    @property
    def xmlns(self):
        return self.__xmlns

    @xmlns.setter
    def xmlns(self, xmlns: str):
        self.__xmlns = xmlns


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def exmode(self):
        return self.__exmode

    @exmode.setter
    def exmode(self, exmode: str):
        self.__exmode = exmode


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def scxml_StateChart(self):
        return self.__scxml_StateChart

    @scxml_StateChart.setter
    def scxml_StateChart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_StateChart__scxml_StateChart", None)
        self.__scxml_StateChart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_Script"):
                    opp_val = getattr(item, "scxml_Script", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_Script", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_Script"):
                    opp_val = getattr(item, "scxml_Script", None)
                    
                    setattr(item, "scxml_Script", self)
                    
