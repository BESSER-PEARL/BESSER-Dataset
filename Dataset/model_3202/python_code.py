from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParamDirection(Enum):
    In = "In"
    Out = "Out"
    InOut = "InOut"


############################################
# Definition of Classes
############################################

class idl_ActualParameter:

    pass
class idl_FixedDefinition:

    pass
class idl_FormalParameterType:

    pass
class idl_TemplateDefinition:

    pass
class idl_FormalParameter:

    def __init__(self, name: str, idl_FormalParameter: "idl_TemplateModule" = None, idl_FormalParameter268: "idl_FormalParameterType" = None):
        self.name = name
        self.idl_FormalParameter = idl_FormalParameter
        self.idl_FormalParameter268 = idl_FormalParameter268
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_FormalParameter268(self):
        return self.__idl_FormalParameter268

    @idl_FormalParameter268.setter
    def idl_FormalParameter268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FormalParameter__idl_FormalParameter268", None)
        self.__idl_FormalParameter268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_FormalParameterType"):
                opp_val = getattr(old_value, "idl_FormalParameterType", None)
                if opp_val == self:
                    setattr(old_value, "idl_FormalParameterType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_FormalParameterType"):
                opp_val = getattr(value, "idl_FormalParameterType", None)
                setattr(value, "idl_FormalParameterType", self)

    @property
    def idl_FormalParameter(self):
        return self.__idl_FormalParameter

    @idl_FormalParameter.setter
    def idl_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FormalParameter__idl_FormalParameter", None)
        self.__idl_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_TemplateModule"):
                opp_val = getattr(old_value, "idl_TemplateModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_TemplateModule"):
                opp_val = getattr(value, "idl_TemplateModule", None)
                if opp_val is None:
                    setattr(value, "idl_TemplateModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class idl_ConnectorExport:

    pass
class idl_ConnectorHeader:

    def __init__(self, name: str, idl_ConnectorHeader: "idl_Connector" = None, idl_ConnectorHeader262: "idl_ScopedName" = None):
        self.name = name
        self.idl_ConnectorHeader = idl_ConnectorHeader
        self.idl_ConnectorHeader262 = idl_ConnectorHeader262
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ConnectorHeader262(self):
        return self.__idl_ConnectorHeader262

    @idl_ConnectorHeader262.setter
    def idl_ConnectorHeader262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConnectorHeader__idl_ConnectorHeader262", None)
        self.__idl_ConnectorHeader262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName263"):
                opp_val = getattr(old_value, "idl_ScopedName263", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName263"):
                opp_val = getattr(value, "idl_ScopedName263", None)
                setattr(value, "idl_ScopedName263", self)

    @property
    def idl_ConnectorHeader(self):
        return self.__idl_ConnectorHeader

    @idl_ConnectorHeader.setter
    def idl_ConnectorHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConnectorHeader__idl_ConnectorHeader", None)
        self.__idl_ConnectorHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Connector"):
                opp_val = getattr(old_value, "idl_Connector", None)
                if opp_val == self:
                    setattr(old_value, "idl_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Connector"):
                opp_val = getattr(value, "idl_Connector", None)
                setattr(value, "idl_Connector", self)

class idl_PortExport:

    pass
class idl_StateMember:

    def __init__(self, isPublic: bool, names: str, idl_StateMember: "idl_EventDcl" = None, idl_StateMember247: "idl_ParamTypeSpec" = None):
        self.isPublic = isPublic
        self.names = names
        self.idl_StateMember = idl_StateMember
        self.idl_StateMember247 = idl_StateMember247
        
    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def idl_StateMember(self):
        return self.__idl_StateMember

    @idl_StateMember.setter
    def idl_StateMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_StateMember__idl_StateMember", None)
        self.__idl_StateMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_EventDcl245"):
                opp_val = getattr(old_value, "idl_EventDcl245", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_EventDcl245"):
                opp_val = getattr(value, "idl_EventDcl245", None)
                if opp_val is None:
                    setattr(value, "idl_EventDcl245", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_StateMember247(self):
        return self.__idl_StateMember247

    @idl_StateMember247.setter
    def idl_StateMember247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_StateMember__idl_StateMember247", None)
        self.__idl_StateMember247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParamTypeSpec248"):
                opp_val = getattr(old_value, "idl_ParamTypeSpec248", None)
                if opp_val == self:
                    setattr(old_value, "idl_ParamTypeSpec248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParamTypeSpec248"):
                opp_val = getattr(value, "idl_ParamTypeSpec248", None)
                setattr(value, "idl_ParamTypeSpec248", self)

class Event:

    pass
class idl_EventForwardDcl(Event):

    pass
class idl_EventDcl(Event):

    def __init__(self, isCustom: bool, isTruncatable: bool, idl_EventDcl242: set["idl_Export"] = None, idl_EventDcl245: set["idl_StateMember"] = None, idl_EventDcl: set["idl_ScopedName"] = None, idl_EventDcl239: set["idl_ScopedName"] = None):
        self.isCustom = isCustom
        self.isTruncatable = isTruncatable
        self.idl_EventDcl242 = idl_EventDcl242 if idl_EventDcl242 is not None else set()
        self.idl_EventDcl245 = idl_EventDcl245 if idl_EventDcl245 is not None else set()
        self.idl_EventDcl = idl_EventDcl if idl_EventDcl is not None else set()
        self.idl_EventDcl239 = idl_EventDcl239 if idl_EventDcl239 is not None else set()
        
    @property
    def isCustom(self) -> bool:
        return self.__isCustom

    @isCustom.setter
    def isCustom(self, isCustom: bool):
        self.__isCustom = isCustom

    @property
    def isTruncatable(self) -> bool:
        return self.__isTruncatable

    @isTruncatable.setter
    def isTruncatable(self, isTruncatable: bool):
        self.__isTruncatable = isTruncatable

    @property
    def idl_EventDcl245(self):
        return self.__idl_EventDcl245

    @idl_EventDcl245.setter
    def idl_EventDcl245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EventDcl__idl_EventDcl245", None)
        self.__idl_EventDcl245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_StateMember"):
                    opp_val = getattr(item, "idl_StateMember", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_StateMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_StateMember"):
                    opp_val = getattr(item, "idl_StateMember", None)
                    
                    setattr(item, "idl_StateMember", self)
                    

    @property
    def idl_EventDcl242(self):
        return self.__idl_EventDcl242

    @idl_EventDcl242.setter
    def idl_EventDcl242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EventDcl__idl_EventDcl242", None)
        self.__idl_EventDcl242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_Export243"):
                    opp_val = getattr(item, "idl_Export243", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_Export243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_Export243"):
                    opp_val = getattr(item, "idl_Export243", None)
                    
                    setattr(item, "idl_Export243", self)
                    

    @property
    def idl_EventDcl(self):
        return self.__idl_EventDcl

    @idl_EventDcl.setter
    def idl_EventDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EventDcl__idl_EventDcl", None)
        self.__idl_EventDcl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ScopedName237"):
                    opp_val = getattr(item, "idl_ScopedName237", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ScopedName237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ScopedName237"):
                    opp_val = getattr(item, "idl_ScopedName237", None)
                    
                    setattr(item, "idl_ScopedName237", self)
                    

    @property
    def idl_EventDcl239(self):
        return self.__idl_EventDcl239

    @idl_EventDcl239.setter
    def idl_EventDcl239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EventDcl__idl_EventDcl239", None)
        self.__idl_EventDcl239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ScopedName240"):
                    opp_val = getattr(item, "idl_ScopedName240", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ScopedName240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ScopedName240"):
                    opp_val = getattr(item, "idl_ScopedName240", None)
                    
                    setattr(item, "idl_ScopedName240", self)
                    

class idl_HomeExport:

    pass
class idl_PrimaryKeySpec:

    pass
class idl_ShiftExpr:

    def __init__(self, op: str, idl_ShiftExpr151: "idl_AddExpr" = None, idl_ShiftExpr154: "idl_ShiftExpr" = None, idl_ShiftExpr152: "idl_ShiftExpr" = None, idl_ShiftExpr: "idl_AndExpr" = None):
        self.op = op
        self.idl_ShiftExpr151 = idl_ShiftExpr151
        self.idl_ShiftExpr154 = idl_ShiftExpr154
        self.idl_ShiftExpr152 = idl_ShiftExpr152
        self.idl_ShiftExpr = idl_ShiftExpr
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_ShiftExpr154(self):
        return self.__idl_ShiftExpr154

    @idl_ShiftExpr154.setter
    def idl_ShiftExpr154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ShiftExpr__idl_ShiftExpr154", None)
        self.__idl_ShiftExpr154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ShiftExpr152"):
                opp_val = getattr(old_value, "idl_ShiftExpr152", None)
                if opp_val == self:
                    setattr(old_value, "idl_ShiftExpr152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ShiftExpr152"):
                opp_val = getattr(value, "idl_ShiftExpr152", None)
                setattr(value, "idl_ShiftExpr152", self)

    @property
    def idl_ShiftExpr151(self):
        return self.__idl_ShiftExpr151

    @idl_ShiftExpr151.setter
    def idl_ShiftExpr151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ShiftExpr__idl_ShiftExpr151", None)
        self.__idl_ShiftExpr151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AddExpr"):
                opp_val = getattr(old_value, "idl_AddExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_AddExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AddExpr"):
                opp_val = getattr(value, "idl_AddExpr", None)
                setattr(value, "idl_AddExpr", self)

    @property
    def idl_ShiftExpr152(self):
        return self.__idl_ShiftExpr152

    @idl_ShiftExpr152.setter
    def idl_ShiftExpr152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ShiftExpr__idl_ShiftExpr152", None)
        self.__idl_ShiftExpr152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ShiftExpr154"):
                opp_val = getattr(old_value, "idl_ShiftExpr154", None)
                if opp_val == self:
                    setattr(old_value, "idl_ShiftExpr154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ShiftExpr154"):
                opp_val = getattr(value, "idl_ShiftExpr154", None)
                setattr(value, "idl_ShiftExpr154", self)

    @property
    def idl_ShiftExpr(self):
        return self.__idl_ShiftExpr

    @idl_ShiftExpr.setter
    def idl_ShiftExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ShiftExpr__idl_ShiftExpr", None)
        self.__idl_ShiftExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AndExpr146"):
                opp_val = getattr(old_value, "idl_AndExpr146", None)
                if opp_val == self:
                    setattr(old_value, "idl_AndExpr146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AndExpr146"):
                opp_val = getattr(value, "idl_AndExpr146", None)
                setattr(value, "idl_AndExpr146", self)

class idl_AndExpr:

    def __init__(self, op: str, idl_AndExpr149: "idl_AndExpr" = None, idl_AndExpr147: "idl_AndExpr" = None, idl_AndExpr: "idl_XOrExpr" = None, idl_AndExpr146: "idl_ShiftExpr" = None):
        self.op = op
        self.idl_AndExpr149 = idl_AndExpr149
        self.idl_AndExpr147 = idl_AndExpr147
        self.idl_AndExpr = idl_AndExpr
        self.idl_AndExpr146 = idl_AndExpr146
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_AndExpr147(self):
        return self.__idl_AndExpr147

    @idl_AndExpr147.setter
    def idl_AndExpr147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AndExpr__idl_AndExpr147", None)
        self.__idl_AndExpr147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AndExpr149"):
                opp_val = getattr(old_value, "idl_AndExpr149", None)
                if opp_val == self:
                    setattr(old_value, "idl_AndExpr149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AndExpr149"):
                opp_val = getattr(value, "idl_AndExpr149", None)
                setattr(value, "idl_AndExpr149", self)

    @property
    def idl_AndExpr149(self):
        return self.__idl_AndExpr149

    @idl_AndExpr149.setter
    def idl_AndExpr149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AndExpr__idl_AndExpr149", None)
        self.__idl_AndExpr149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AndExpr147"):
                opp_val = getattr(old_value, "idl_AndExpr147", None)
                if opp_val == self:
                    setattr(old_value, "idl_AndExpr147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AndExpr147"):
                opp_val = getattr(value, "idl_AndExpr147", None)
                setattr(value, "idl_AndExpr147", self)

    @property
    def idl_AndExpr146(self):
        return self.__idl_AndExpr146

    @idl_AndExpr146.setter
    def idl_AndExpr146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AndExpr__idl_AndExpr146", None)
        self.__idl_AndExpr146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ShiftExpr"):
                opp_val = getattr(old_value, "idl_ShiftExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_ShiftExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ShiftExpr"):
                opp_val = getattr(value, "idl_ShiftExpr", None)
                setattr(value, "idl_ShiftExpr", self)

    @property
    def idl_AndExpr(self):
        return self.__idl_AndExpr

    @idl_AndExpr.setter
    def idl_AndExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AndExpr__idl_AndExpr", None)
        self.__idl_AndExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_XOrExpr141"):
                opp_val = getattr(old_value, "idl_XOrExpr141", None)
                if opp_val == self:
                    setattr(old_value, "idl_XOrExpr141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_XOrExpr141"):
                opp_val = getattr(value, "idl_XOrExpr141", None)
                setattr(value, "idl_XOrExpr141", self)

class idl_ComponentExport:

    pass
class idl_XOrExpr:

    def __init__(self, op: str, idl_XOrExpr: "idl_OrExpr" = None, idl_XOrExpr141: "idl_AndExpr" = None, idl_XOrExpr144: "idl_XOrExpr" = None, idl_XOrExpr142: "idl_XOrExpr" = None):
        self.op = op
        self.idl_XOrExpr = idl_XOrExpr
        self.idl_XOrExpr141 = idl_XOrExpr141
        self.idl_XOrExpr144 = idl_XOrExpr144
        self.idl_XOrExpr142 = idl_XOrExpr142
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_XOrExpr142(self):
        return self.__idl_XOrExpr142

    @idl_XOrExpr142.setter
    def idl_XOrExpr142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_XOrExpr__idl_XOrExpr142", None)
        self.__idl_XOrExpr142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_XOrExpr144"):
                opp_val = getattr(old_value, "idl_XOrExpr144", None)
                if opp_val == self:
                    setattr(old_value, "idl_XOrExpr144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_XOrExpr144"):
                opp_val = getattr(value, "idl_XOrExpr144", None)
                setattr(value, "idl_XOrExpr144", self)

    @property
    def idl_XOrExpr(self):
        return self.__idl_XOrExpr

    @idl_XOrExpr.setter
    def idl_XOrExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_XOrExpr__idl_XOrExpr", None)
        self.__idl_XOrExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_OrExpr"):
                opp_val = getattr(old_value, "idl_OrExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_OrExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_OrExpr"):
                opp_val = getattr(value, "idl_OrExpr", None)
                setattr(value, "idl_OrExpr", self)

    @property
    def idl_XOrExpr141(self):
        return self.__idl_XOrExpr141

    @idl_XOrExpr141.setter
    def idl_XOrExpr141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_XOrExpr__idl_XOrExpr141", None)
        self.__idl_XOrExpr141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AndExpr"):
                opp_val = getattr(old_value, "idl_AndExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_AndExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AndExpr"):
                opp_val = getattr(value, "idl_AndExpr", None)
                setattr(value, "idl_AndExpr", self)

    @property
    def idl_XOrExpr144(self):
        return self.__idl_XOrExpr144

    @idl_XOrExpr144.setter
    def idl_XOrExpr144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_XOrExpr__idl_XOrExpr144", None)
        self.__idl_XOrExpr144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_XOrExpr142"):
                opp_val = getattr(old_value, "idl_XOrExpr142", None)
                if opp_val == self:
                    setattr(old_value, "idl_XOrExpr142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_XOrExpr142"):
                opp_val = getattr(value, "idl_XOrExpr142", None)
                setattr(value, "idl_XOrExpr142", self)

class ConstExp:

    pass
class idl_OrExpr(ConstExp):

    def __init__(self, op: str, idl_OrExpr: "idl_XOrExpr" = None, idl_OrExpr139: "idl_OrExpr" = None, idl_OrExpr137: "idl_OrExpr" = None):
        self.op = op
        self.idl_OrExpr = idl_OrExpr
        self.idl_OrExpr139 = idl_OrExpr139
        self.idl_OrExpr137 = idl_OrExpr137
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_OrExpr(self):
        return self.__idl_OrExpr

    @idl_OrExpr.setter
    def idl_OrExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OrExpr__idl_OrExpr", None)
        self.__idl_OrExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_XOrExpr"):
                opp_val = getattr(old_value, "idl_XOrExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_XOrExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_XOrExpr"):
                opp_val = getattr(value, "idl_XOrExpr", None)
                setattr(value, "idl_XOrExpr", self)

    @property
    def idl_OrExpr139(self):
        return self.__idl_OrExpr139

    @idl_OrExpr139.setter
    def idl_OrExpr139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OrExpr__idl_OrExpr139", None)
        self.__idl_OrExpr139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_OrExpr137"):
                opp_val = getattr(old_value, "idl_OrExpr137", None)
                if opp_val == self:
                    setattr(old_value, "idl_OrExpr137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_OrExpr137"):
                opp_val = getattr(value, "idl_OrExpr137", None)
                setattr(value, "idl_OrExpr137", self)

    @property
    def idl_OrExpr137(self):
        return self.__idl_OrExpr137

    @idl_OrExpr137.setter
    def idl_OrExpr137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OrExpr__idl_OrExpr137", None)
        self.__idl_OrExpr137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_OrExpr139"):
                opp_val = getattr(old_value, "idl_OrExpr139", None)
                if opp_val == self:
                    setattr(old_value, "idl_OrExpr139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_OrExpr139"):
                opp_val = getattr(value, "idl_OrExpr139", None)
                setattr(value, "idl_OrExpr139", self)

class ConstParamType:

    pass
class idl_PrimaryExpr:

    pass
class idl_ConstType(ConstParamType):

    pass
class idl_UnaryExpr:

    def __init__(self, op: str, idl_UnaryExpr: "idl_MultExpr" = None, idl_UnaryExpr166: "idl_PrimaryExpr" = None):
        self.op = op
        self.idl_UnaryExpr = idl_UnaryExpr
        self.idl_UnaryExpr166 = idl_UnaryExpr166
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_UnaryExpr(self):
        return self.__idl_UnaryExpr

    @idl_UnaryExpr.setter
    def idl_UnaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UnaryExpr__idl_UnaryExpr", None)
        self.__idl_UnaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_MultExpr161"):
                opp_val = getattr(old_value, "idl_MultExpr161", None)
                if opp_val == self:
                    setattr(old_value, "idl_MultExpr161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_MultExpr161"):
                opp_val = getattr(value, "idl_MultExpr161", None)
                setattr(value, "idl_MultExpr161", self)

    @property
    def idl_UnaryExpr166(self):
        return self.__idl_UnaryExpr166

    @idl_UnaryExpr166.setter
    def idl_UnaryExpr166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UnaryExpr__idl_UnaryExpr166", None)
        self.__idl_UnaryExpr166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PrimaryExpr"):
                opp_val = getattr(old_value, "idl_PrimaryExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_PrimaryExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PrimaryExpr"):
                opp_val = getattr(value, "idl_PrimaryExpr", None)
                setattr(value, "idl_PrimaryExpr", self)

class idl_MultExpr:

    def __init__(self, op: str, idl_MultExpr: "idl_AddExpr" = None, idl_MultExpr161: "idl_UnaryExpr" = None, idl_MultExpr164: "idl_MultExpr" = None, idl_MultExpr162: "idl_MultExpr" = None):
        self.op = op
        self.idl_MultExpr = idl_MultExpr
        self.idl_MultExpr161 = idl_MultExpr161
        self.idl_MultExpr164 = idl_MultExpr164
        self.idl_MultExpr162 = idl_MultExpr162
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_MultExpr(self):
        return self.__idl_MultExpr

    @idl_MultExpr.setter
    def idl_MultExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_MultExpr__idl_MultExpr", None)
        self.__idl_MultExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AddExpr156"):
                opp_val = getattr(old_value, "idl_AddExpr156", None)
                if opp_val == self:
                    setattr(old_value, "idl_AddExpr156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AddExpr156"):
                opp_val = getattr(value, "idl_AddExpr156", None)
                setattr(value, "idl_AddExpr156", self)

    @property
    def idl_MultExpr164(self):
        return self.__idl_MultExpr164

    @idl_MultExpr164.setter
    def idl_MultExpr164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_MultExpr__idl_MultExpr164", None)
        self.__idl_MultExpr164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_MultExpr162"):
                opp_val = getattr(old_value, "idl_MultExpr162", None)
                if opp_val == self:
                    setattr(old_value, "idl_MultExpr162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_MultExpr162"):
                opp_val = getattr(value, "idl_MultExpr162", None)
                setattr(value, "idl_MultExpr162", self)

    @property
    def idl_MultExpr161(self):
        return self.__idl_MultExpr161

    @idl_MultExpr161.setter
    def idl_MultExpr161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_MultExpr__idl_MultExpr161", None)
        self.__idl_MultExpr161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_UnaryExpr"):
                opp_val = getattr(old_value, "idl_UnaryExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_UnaryExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_UnaryExpr"):
                opp_val = getattr(value, "idl_UnaryExpr", None)
                setattr(value, "idl_UnaryExpr", self)

    @property
    def idl_MultExpr162(self):
        return self.__idl_MultExpr162

    @idl_MultExpr162.setter
    def idl_MultExpr162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_MultExpr__idl_MultExpr162", None)
        self.__idl_MultExpr162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_MultExpr164"):
                opp_val = getattr(old_value, "idl_MultExpr164", None)
                if opp_val == self:
                    setattr(old_value, "idl_MultExpr164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_MultExpr164"):
                opp_val = getattr(value, "idl_MultExpr164", None)
                setattr(value, "idl_MultExpr164", self)

class idl_AddExpr:

    def __init__(self, op: str, idl_AddExpr: "idl_ShiftExpr" = None, idl_AddExpr156: "idl_MultExpr" = None, idl_AddExpr159: "idl_AddExpr" = None, idl_AddExpr157: "idl_AddExpr" = None):
        self.op = op
        self.idl_AddExpr = idl_AddExpr
        self.idl_AddExpr156 = idl_AddExpr156
        self.idl_AddExpr159 = idl_AddExpr159
        self.idl_AddExpr157 = idl_AddExpr157
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_AddExpr(self):
        return self.__idl_AddExpr

    @idl_AddExpr.setter
    def idl_AddExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AddExpr__idl_AddExpr", None)
        self.__idl_AddExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ShiftExpr151"):
                opp_val = getattr(old_value, "idl_ShiftExpr151", None)
                if opp_val == self:
                    setattr(old_value, "idl_ShiftExpr151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ShiftExpr151"):
                opp_val = getattr(value, "idl_ShiftExpr151", None)
                setattr(value, "idl_ShiftExpr151", self)

    @property
    def idl_AddExpr159(self):
        return self.__idl_AddExpr159

    @idl_AddExpr159.setter
    def idl_AddExpr159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AddExpr__idl_AddExpr159", None)
        self.__idl_AddExpr159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AddExpr157"):
                opp_val = getattr(old_value, "idl_AddExpr157", None)
                if opp_val == self:
                    setattr(old_value, "idl_AddExpr157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AddExpr157"):
                opp_val = getattr(value, "idl_AddExpr157", None)
                setattr(value, "idl_AddExpr157", self)

    @property
    def idl_AddExpr157(self):
        return self.__idl_AddExpr157

    @idl_AddExpr157.setter
    def idl_AddExpr157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AddExpr__idl_AddExpr157", None)
        self.__idl_AddExpr157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AddExpr159"):
                opp_val = getattr(old_value, "idl_AddExpr159", None)
                if opp_val == self:
                    setattr(old_value, "idl_AddExpr159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AddExpr159"):
                opp_val = getattr(value, "idl_AddExpr159", None)
                setattr(value, "idl_AddExpr159", self)

    @property
    def idl_AddExpr156(self):
        return self.__idl_AddExpr156

    @idl_AddExpr156.setter
    def idl_AddExpr156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AddExpr__idl_AddExpr156", None)
        self.__idl_AddExpr156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_MultExpr"):
                opp_val = getattr(old_value, "idl_MultExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_MultExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_MultExpr"):
                opp_val = getattr(value, "idl_MultExpr", None)
                setattr(value, "idl_MultExpr", self)

class FormalParameterType:

    pass
class idl_ConstParamType(FormalParameterType):

    pass
class idl_UnionParamType(FormalParameterType):

    pass
class idl_EventParamType(FormalParameterType):

    pass
class idl_InterfaceParamType(FormalParameterType):

    pass
class idl_ExceptionParamType(FormalParameterType):

    pass
class idl_EnumParamType(FormalParameterType):

    pass
class idl_TypenameParamType(FormalParameterType):

    pass
class idl_SequenceParamType(FormalParameterType):

    pass
class idl_ValuetypeParamType(FormalParameterType):

    pass
class idl_StructParamType(FormalParameterType):

    pass
class idl_ElementSpec:

    pass
class idl_CaseLabel:

    def __init__(self, isCase: bool, isDefault: bool, idl_CaseLabel: "idl_Case" = None, idl_CaseLabel107: "idl_ConstExp" = None):
        self.isCase = isCase
        self.isDefault = isDefault
        self.idl_CaseLabel = idl_CaseLabel
        self.idl_CaseLabel107 = idl_CaseLabel107
        
    @property
    def isCase(self) -> bool:
        return self.__isCase

    @isCase.setter
    def isCase(self, isCase: bool):
        self.__isCase = isCase

    @property
    def isDefault(self) -> bool:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: bool):
        self.__isDefault = isDefault

    @property
    def idl_CaseLabel107(self):
        return self.__idl_CaseLabel107

    @idl_CaseLabel107.setter
    def idl_CaseLabel107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_CaseLabel__idl_CaseLabel107", None)
        self.__idl_CaseLabel107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConstExp108"):
                opp_val = getattr(old_value, "idl_ConstExp108", None)
                if opp_val == self:
                    setattr(old_value, "idl_ConstExp108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConstExp108"):
                opp_val = getattr(value, "idl_ConstExp108", None)
                setattr(value, "idl_ConstExp108", self)

    @property
    def idl_CaseLabel(self):
        return self.__idl_CaseLabel

    @idl_CaseLabel.setter
    def idl_CaseLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_CaseLabel__idl_CaseLabel", None)
        self.__idl_CaseLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Case103"):
                opp_val = getattr(old_value, "idl_Case103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Case103"):
                opp_val = getattr(value, "idl_Case103", None)
                if opp_val is None:
                    setattr(value, "idl_Case103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ConstrForwardDecl:

    pass
class idl_UnionForwardDecl(ConstrForwardDecl):

    pass
class idl_StructForwardDecl(ConstrForwardDecl):

    pass
class ConstrTypeSpec:

    pass
class TypeDecl:

    pass
class idl_ConstrForwardDecl(TypeDecl):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class idl_TypeDeclarator(TypeDecl):

    pass
class ComplexDeclarator:

    pass
class idl_ComplexDeclarator:

    pass
class Declarator:

    pass
class idl_ArrayDeclarator(Declarator, ComplexDeclarator):

    pass
class idl_SimpleDeclarator(Declarator):

    pass
class idl_Declarator:

    def __init__(self, id: str, idl_Declarator: "idl_Member" = None, idl_Declarator90: "idl_TypeDeclarator" = None, idl_Declarator114: "idl_ElementSpec" = None):
        self.id = id
        self.idl_Declarator = idl_Declarator
        self.idl_Declarator90 = idl_Declarator90
        self.idl_Declarator114 = idl_Declarator114
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def idl_Declarator114(self):
        return self.__idl_Declarator114

    @idl_Declarator114.setter
    def idl_Declarator114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Declarator__idl_Declarator114", None)
        self.__idl_Declarator114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ElementSpec113"):
                opp_val = getattr(old_value, "idl_ElementSpec113", None)
                if opp_val == self:
                    setattr(old_value, "idl_ElementSpec113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ElementSpec113"):
                opp_val = getattr(value, "idl_ElementSpec113", None)
                setattr(value, "idl_ElementSpec113", self)

    @property
    def idl_Declarator(self):
        return self.__idl_Declarator

    @idl_Declarator.setter
    def idl_Declarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Declarator__idl_Declarator", None)
        self.__idl_Declarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Member72"):
                opp_val = getattr(old_value, "idl_Member72", None)
                if opp_val == self:
                    setattr(old_value, "idl_Member72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Member72"):
                opp_val = getattr(value, "idl_Member72", None)
                setattr(value, "idl_Member72", self)

    @property
    def idl_Declarator90(self):
        return self.__idl_Declarator90

    @idl_Declarator90.setter
    def idl_Declarator90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Declarator__idl_Declarator90", None)
        self.__idl_Declarator90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_TypeDeclarator89"):
                opp_val = getattr(old_value, "idl_TypeDeclarator89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_TypeDeclarator89"):
                opp_val = getattr(value, "idl_TypeDeclarator89", None)
                if opp_val is None:
                    setattr(value, "idl_TypeDeclarator89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class idl_Case:

    pass
class idl_SwitchBody:

    pass
class idl_SwitchTypeSpec:

    pass
class idl_UnionType(ConstrTypeSpec, TypeDecl):

    def __init__(self, name: str, idl_UnionType: set["idl_IDLComment"] = None, idl_UnionType94: "idl_SwitchTypeSpec" = None, idl_UnionType96: "idl_SwitchBody" = None):
        self.name = name
        self.idl_UnionType = idl_UnionType if idl_UnionType is not None else set()
        self.idl_UnionType94 = idl_UnionType94
        self.idl_UnionType96 = idl_UnionType96
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_UnionType(self):
        return self.__idl_UnionType

    @idl_UnionType.setter
    def idl_UnionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UnionType__idl_UnionType", None)
        self.__idl_UnionType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment92"):
                    opp_val = getattr(item, "idl_IDLComment92", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment92"):
                    opp_val = getattr(item, "idl_IDLComment92", None)
                    
                    setattr(item, "idl_IDLComment92", self)
                    

    @property
    def idl_UnionType96(self):
        return self.__idl_UnionType96

    @idl_UnionType96.setter
    def idl_UnionType96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UnionType__idl_UnionType96", None)
        self.__idl_UnionType96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_SwitchBody"):
                opp_val = getattr(old_value, "idl_SwitchBody", None)
                if opp_val == self:
                    setattr(old_value, "idl_SwitchBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_SwitchBody"):
                opp_val = getattr(value, "idl_SwitchBody", None)
                setattr(value, "idl_SwitchBody", self)

    @property
    def idl_UnionType94(self):
        return self.__idl_UnionType94

    @idl_UnionType94.setter
    def idl_UnionType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UnionType__idl_UnionType94", None)
        self.__idl_UnionType94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_SwitchTypeSpec"):
                opp_val = getattr(old_value, "idl_SwitchTypeSpec", None)
                if opp_val == self:
                    setattr(old_value, "idl_SwitchTypeSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_SwitchTypeSpec"):
                opp_val = getattr(value, "idl_SwitchTypeSpec", None)
                setattr(value, "idl_SwitchTypeSpec", self)

class TypeSpec:

    pass
class idl_ConstrTypeSpec(TypeSpec):

    pass
class idl_SimpleTypeSpec(TypeSpec):

    pass
class ActualParameter:

    pass
class idl_TypeSpec(ActualParameter):

    pass
class UnsignedInt:

    pass
class idl_UnsignedLongLongInt(UnsignedInt):

    pass
class idl_UnsignedLongInt(UnsignedInt):

    pass
class idl_UnsignedShortInt(UnsignedInt):

    pass
class SignedInt:

    pass
class idl_SignedLongInt(SignedInt):

    pass
class idl_SignedLongLongInt(SignedInt):

    pass
class idl_SignedShortInt(SignedInt):

    pass
class IntegerType:

    pass
class idl_UnsignedInt(IntegerType):

    pass
class idl_SignedInt(IntegerType):

    pass
class FloatingPtType:

    pass
class idl_LongDoubleType(FloatingPtType):

    pass
class idl_DoubleType(FloatingPtType):

    pass
class idl_FloatType(FloatingPtType):

    pass
class BaseTypeSpec:

    pass
class PrimaryExpr:

    pass
class idl_Literal(PrimaryExpr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ConstType:

    pass
class idl_WideCharType(ConstType, BaseTypeSpec):

    pass
class idl_FixedPtConstType(ConstType):

    pass
class idl_FloatingPtType(ConstType, BaseTypeSpec):

    pass
class idl_OctetType(ConstType, BaseTypeSpec):

    pass
class SwitchTypeSpec:

    pass
class idl_EnumType(SwitchTypeSpec, ConstrTypeSpec, TypeDecl):

    def __init__(self, name: str, literal: str, idl_EnumType: set["idl_IDLComment"] = None):
        self.name = name
        self.literal = literal
        self.idl_EnumType = idl_EnumType if idl_EnumType is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def idl_EnumType(self):
        return self.__idl_EnumType

    @idl_EnumType.setter
    def idl_EnumType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EnumType__idl_EnumType", None)
        self.__idl_EnumType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment116"):
                    opp_val = getattr(item, "idl_IDLComment116", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment116"):
                    opp_val = getattr(item, "idl_IDLComment116", None)
                    
                    setattr(item, "idl_IDLComment116", self)
                    

class idl_IntegerType(ConstType, BaseTypeSpec, SwitchTypeSpec):

    pass
class idl_CharType(ConstType, BaseTypeSpec, SwitchTypeSpec):

    pass
class idl_BooleanType(ConstType, BaseTypeSpec, SwitchTypeSpec):

    pass
class SimpleTypeSpec:

    pass
class idl_TemplateTypeSpec(SimpleTypeSpec):

    pass
class ParamTypeSpec:

    pass
class idl_BaseTypeSpec(SimpleTypeSpec, ParamTypeSpec):

    pass
class idl_Member:

    pass
class idl_PositiveIntConst:

    pass
class TemplateTypeSpec:

    pass
class idl_WideStringType(ConstType, TemplateTypeSpec, ParamTypeSpec):

    pass
class idl_FixedPtType(TemplateTypeSpec):

    pass
class idl_SequenceType(TemplateTypeSpec, FormalParameterType):

    pass
class idl_StringType(ConstType, TemplateTypeSpec, ParamTypeSpec):

    pass
class idl_ValueBaseType(BaseTypeSpec):

    pass
class idl_ObjectType(BaseTypeSpec):

    pass
class idl_AnyType(BaseTypeSpec):

    pass
class idl_ContextExpr:

    def __init__(self, literal: str, idl_ContextExpr: "idl_OpDecl" = None):
        self.literal = literal
        self.idl_ContextExpr = idl_ContextExpr
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def idl_ContextExpr(self):
        return self.__idl_ContextExpr

    @idl_ContextExpr.setter
    def idl_ContextExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ContextExpr__idl_ContextExpr", None)
        self.__idl_ContextExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_OpDecl53"):
                opp_val = getattr(old_value, "idl_OpDecl53", None)
                if opp_val == self:
                    setattr(old_value, "idl_OpDecl53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_OpDecl53"):
                opp_val = getattr(value, "idl_OpDecl53", None)
                setattr(value, "idl_OpDecl53", self)

class idl_ParameterDecls:

    pass
class OpTypeDecl:

    pass
class idl_ParamDcl:

    def __init__(self, direction: str, name: str, idl_ParamDcl: "idl_ParameterDecls" = None, idl_ParamDcl60: "idl_ParamTypeSpec" = None):
        self.direction = direction
        self.name = name
        self.idl_ParamDcl = idl_ParamDcl
        self.idl_ParamDcl60 = idl_ParamDcl60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def idl_ParamDcl60(self):
        return self.__idl_ParamDcl60

    @idl_ParamDcl60.setter
    def idl_ParamDcl60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ParamDcl__idl_ParamDcl60", None)
        self.__idl_ParamDcl60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParamTypeSpec61"):
                opp_val = getattr(old_value, "idl_ParamTypeSpec61", None)
                if opp_val == self:
                    setattr(old_value, "idl_ParamTypeSpec61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParamTypeSpec61"):
                opp_val = getattr(value, "idl_ParamTypeSpec61", None)
                setattr(value, "idl_ParamTypeSpec61", self)

    @property
    def idl_ParamDcl(self):
        return self.__idl_ParamDcl

    @idl_ParamDcl.setter
    def idl_ParamDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ParamDcl__idl_ParamDcl", None)
        self.__idl_ParamDcl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParameterDecls58"):
                opp_val = getattr(old_value, "idl_ParameterDecls58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParameterDecls58"):
                opp_val = getattr(value, "idl_ParameterDecls58", None)
                if opp_val is None:
                    setattr(value, "idl_ParameterDecls58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class idl_AttrRaisesExpr:

    pass
class AttrDecl:

    pass
class idl_ReadOnlyAttrSpec(AttrDecl):

    pass
class idl_AttrSpec(AttrDecl):

    pass
class idl_ParamTypeSpec(OpTypeDecl):

    pass
class idl_OpTypeDecl:

    pass
class idl_ExceptionList:

    pass
class idl_InterfaceBody:

    pass
class idl_Interface_header:

    def __init__(self, isLocal: bool, name: str, isAbstract: bool, idl_Interface_header22: set["idl_ScopedName"] = None, idl_Interface_header24: set["idl_IDLComment"] = None, idl_Interface_header: "idl_Interface_decl" = None):
        self.isLocal = isLocal
        self.name = name
        self.isAbstract = isAbstract
        self.idl_Interface_header22 = idl_Interface_header22 if idl_Interface_header22 is not None else set()
        self.idl_Interface_header24 = idl_Interface_header24 if idl_Interface_header24 is not None else set()
        self.idl_Interface_header = idl_Interface_header
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def isLocal(self) -> bool:
        return self.__isLocal

    @isLocal.setter
    def isLocal(self, isLocal: bool):
        self.__isLocal = isLocal

    @property
    def idl_Interface_header(self):
        return self.__idl_Interface_header

    @idl_Interface_header.setter
    def idl_Interface_header(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Interface_header__idl_Interface_header", None)
        self.__idl_Interface_header = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Interface_decl"):
                opp_val = getattr(old_value, "idl_Interface_decl", None)
                if opp_val == self:
                    setattr(old_value, "idl_Interface_decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Interface_decl"):
                opp_val = getattr(value, "idl_Interface_decl", None)
                setattr(value, "idl_Interface_decl", self)

    @property
    def idl_Interface_header24(self):
        return self.__idl_Interface_header24

    @idl_Interface_header24.setter
    def idl_Interface_header24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Interface_header__idl_Interface_header24", None)
        self.__idl_Interface_header24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment25"):
                    opp_val = getattr(item, "idl_IDLComment25", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment25"):
                    opp_val = getattr(item, "idl_IDLComment25", None)
                    
                    setattr(item, "idl_IDLComment25", self)
                    

    @property
    def idl_Interface_header22(self):
        return self.__idl_Interface_header22

    @idl_Interface_header22.setter
    def idl_Interface_header22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Interface_header__idl_Interface_header22", None)
        self.__idl_Interface_header22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ScopedName"):
                    opp_val = getattr(item, "idl_ScopedName", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ScopedName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ScopedName"):
                    opp_val = getattr(item, "idl_ScopedName", None)
                    
                    setattr(item, "idl_ScopedName", self)
                    

class FixedDefinition:

    pass
class TemplateDefinition:

    pass
class idl_TemplateModuleRef(TemplateDefinition):

    def __init__(self, id: str, name: str, idl_TemplateModuleRef: "idl_ScopedName" = None):
        self.id = id
        self.name = name
        self.idl_TemplateModuleRef = idl_TemplateModuleRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_TemplateModuleRef(self):
        return self.__idl_TemplateModuleRef

    @idl_TemplateModuleRef.setter
    def idl_TemplateModuleRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_TemplateModuleRef__idl_TemplateModuleRef", None)
        self.__idl_TemplateModuleRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName278"):
                opp_val = getattr(old_value, "idl_ScopedName278", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName278"):
                opp_val = getattr(value, "idl_ScopedName278", None)
                setattr(value, "idl_ScopedName278", self)

class idl_FixedModule(FixedDefinition, TemplateDefinition):

    def __init__(self, name: str, idl_FixedModule: set["idl_FixedDefinition"] = None):
        self.name = name
        self.idl_FixedModule = idl_FixedModule if idl_FixedModule is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_FixedModule(self):
        return self.__idl_FixedModule

    @idl_FixedModule.setter
    def idl_FixedModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FixedModule__idl_FixedModule", None)
        self.__idl_FixedModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_FixedDefinition"):
                    opp_val = getattr(item, "idl_FixedDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_FixedDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_FixedDefinition"):
                    opp_val = getattr(item, "idl_FixedDefinition", None)
                    
                    setattr(item, "idl_FixedDefinition", self)
                    

class Interface_or_Forward_Decl:

    pass
class idl_Forward_decl(Interface_or_Forward_Decl):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class idl_Interface_decl(FixedDefinition, TemplateDefinition, Interface_or_Forward_Decl):

    pass
class ConnectorExport:

    pass
class PortExport:

    pass
class HomeExport:

    pass
class idl_FactoryDcl(HomeExport):

    def __init__(self, name: str, idl_FactoryDcl: set["idl_IDLComment"] = None, idl_FactoryDcl223: "idl_ParameterDecls" = None, idl_FactoryDcl226: "idl_ExceptionList" = None):
        self.name = name
        self.idl_FactoryDcl = idl_FactoryDcl if idl_FactoryDcl is not None else set()
        self.idl_FactoryDcl223 = idl_FactoryDcl223
        self.idl_FactoryDcl226 = idl_FactoryDcl226
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_FactoryDcl226(self):
        return self.__idl_FactoryDcl226

    @idl_FactoryDcl226.setter
    def idl_FactoryDcl226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FactoryDcl__idl_FactoryDcl226", None)
        self.__idl_FactoryDcl226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ExceptionList227"):
                opp_val = getattr(old_value, "idl_ExceptionList227", None)
                if opp_val == self:
                    setattr(old_value, "idl_ExceptionList227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ExceptionList227"):
                opp_val = getattr(value, "idl_ExceptionList227", None)
                setattr(value, "idl_ExceptionList227", self)

    @property
    def idl_FactoryDcl(self):
        return self.__idl_FactoryDcl

    @idl_FactoryDcl.setter
    def idl_FactoryDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FactoryDcl__idl_FactoryDcl", None)
        self.__idl_FactoryDcl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment221"):
                    opp_val = getattr(item, "idl_IDLComment221", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment221"):
                    opp_val = getattr(item, "idl_IDLComment221", None)
                    
                    setattr(item, "idl_IDLComment221", self)
                    

    @property
    def idl_FactoryDcl223(self):
        return self.__idl_FactoryDcl223

    @idl_FactoryDcl223.setter
    def idl_FactoryDcl223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FactoryDcl__idl_FactoryDcl223", None)
        self.__idl_FactoryDcl223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParameterDecls224"):
                opp_val = getattr(old_value, "idl_ParameterDecls224", None)
                if opp_val == self:
                    setattr(old_value, "idl_ParameterDecls224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParameterDecls224"):
                opp_val = getattr(value, "idl_ParameterDecls224", None)
                setattr(value, "idl_ParameterDecls224", self)

class idl_FinderDcl(HomeExport):

    def __init__(self, name: str, idl_FinderDcl: set["idl_IDLComment"] = None, idl_FinderDcl231: "idl_ParameterDecls" = None, idl_FinderDcl234: "idl_ExceptionList" = None):
        self.name = name
        self.idl_FinderDcl = idl_FinderDcl if idl_FinderDcl is not None else set()
        self.idl_FinderDcl231 = idl_FinderDcl231
        self.idl_FinderDcl234 = idl_FinderDcl234
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_FinderDcl231(self):
        return self.__idl_FinderDcl231

    @idl_FinderDcl231.setter
    def idl_FinderDcl231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FinderDcl__idl_FinderDcl231", None)
        self.__idl_FinderDcl231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParameterDecls232"):
                opp_val = getattr(old_value, "idl_ParameterDecls232", None)
                if opp_val == self:
                    setattr(old_value, "idl_ParameterDecls232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParameterDecls232"):
                opp_val = getattr(value, "idl_ParameterDecls232", None)
                setattr(value, "idl_ParameterDecls232", self)

    @property
    def idl_FinderDcl(self):
        return self.__idl_FinderDcl

    @idl_FinderDcl.setter
    def idl_FinderDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FinderDcl__idl_FinderDcl", None)
        self.__idl_FinderDcl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment229"):
                    opp_val = getattr(item, "idl_IDLComment229", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment229"):
                    opp_val = getattr(item, "idl_IDLComment229", None)
                    
                    setattr(item, "idl_IDLComment229", self)
                    

    @property
    def idl_FinderDcl234(self):
        return self.__idl_FinderDcl234

    @idl_FinderDcl234.setter
    def idl_FinderDcl234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FinderDcl__idl_FinderDcl234", None)
        self.__idl_FinderDcl234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ExceptionList235"):
                opp_val = getattr(old_value, "idl_ExceptionList235", None)
                if opp_val == self:
                    setattr(old_value, "idl_ExceptionList235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ExceptionList235"):
                opp_val = getattr(value, "idl_ExceptionList235", None)
                setattr(value, "idl_ExceptionList235", self)

class idl_Export(HomeExport):

    pass
class idl_ScopedName(PrimaryExpr, SwitchTypeSpec, SimpleTypeSpec, ParamTypeSpec, ConstType):

    def __init__(self, name: str, idl_ScopedName: "idl_Interface_header" = None, idl_ScopedName42: "idl_ExceptionList" = None, idl_ScopedName171: "idl_ComponentDecl" = None, idl_ScopedName174: "idl_ComponentDecl" = None, idl_ScopedName183: "idl_UsesDcl" = None, idl_ScopedName188: "idl_PublishesDcl" = None, idl_ScopedName193: "idl_EmitDcl" = None, idl_ScopedName198: "idl_ConsumesDcl" = None, idl_ScopedName178: "idl_ProvidesDcl" = None, idl_ScopedName209: "idl_HomeDecl" = None, idl_ScopedName212: "idl_HomeDecl" = None, idl_ScopedName219: "idl_PrimaryKeySpec" = None, idl_ScopedName206: "idl_HomeDecl" = None, idl_ScopedName254: "idl_PortDecl" = None, idl_ScopedName263: "idl_ConnectorHeader" = None, idl_ScopedName237: "idl_EventDcl" = None, idl_ScopedName240: "idl_EventDcl" = None, idl_ScopedName271: "idl_TemplateModuleInst" = None, idl_ScopedName278: "idl_TemplateModuleRef" = None):
        self.name = name
        self.idl_ScopedName = idl_ScopedName
        self.idl_ScopedName42 = idl_ScopedName42
        self.idl_ScopedName171 = idl_ScopedName171
        self.idl_ScopedName174 = idl_ScopedName174
        self.idl_ScopedName183 = idl_ScopedName183
        self.idl_ScopedName188 = idl_ScopedName188
        self.idl_ScopedName193 = idl_ScopedName193
        self.idl_ScopedName198 = idl_ScopedName198
        self.idl_ScopedName178 = idl_ScopedName178
        self.idl_ScopedName209 = idl_ScopedName209
        self.idl_ScopedName212 = idl_ScopedName212
        self.idl_ScopedName219 = idl_ScopedName219
        self.idl_ScopedName206 = idl_ScopedName206
        self.idl_ScopedName254 = idl_ScopedName254
        self.idl_ScopedName263 = idl_ScopedName263
        self.idl_ScopedName237 = idl_ScopedName237
        self.idl_ScopedName240 = idl_ScopedName240
        self.idl_ScopedName271 = idl_ScopedName271
        self.idl_ScopedName278 = idl_ScopedName278
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ScopedName198(self):
        return self.__idl_ScopedName198

    @idl_ScopedName198.setter
    def idl_ScopedName198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName198", None)
        self.__idl_ScopedName198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConsumesDcl"):
                opp_val = getattr(old_value, "idl_ConsumesDcl", None)
                if opp_val == self:
                    setattr(old_value, "idl_ConsumesDcl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConsumesDcl"):
                opp_val = getattr(value, "idl_ConsumesDcl", None)
                setattr(value, "idl_ConsumesDcl", self)

    @property
    def idl_ScopedName(self):
        return self.__idl_ScopedName

    @idl_ScopedName.setter
    def idl_ScopedName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName", None)
        self.__idl_ScopedName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Interface_header22"):
                opp_val = getattr(old_value, "idl_Interface_header22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Interface_header22"):
                opp_val = getattr(value, "idl_Interface_header22", None)
                if opp_val is None:
                    setattr(value, "idl_Interface_header22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_ScopedName237(self):
        return self.__idl_ScopedName237

    @idl_ScopedName237.setter
    def idl_ScopedName237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName237", None)
        self.__idl_ScopedName237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_EventDcl"):
                opp_val = getattr(old_value, "idl_EventDcl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_EventDcl"):
                opp_val = getattr(value, "idl_EventDcl", None)
                if opp_val is None:
                    setattr(value, "idl_EventDcl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_ScopedName278(self):
        return self.__idl_ScopedName278

    @idl_ScopedName278.setter
    def idl_ScopedName278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName278", None)
        self.__idl_ScopedName278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_TemplateModuleRef"):
                opp_val = getattr(old_value, "idl_TemplateModuleRef", None)
                if opp_val == self:
                    setattr(old_value, "idl_TemplateModuleRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_TemplateModuleRef"):
                opp_val = getattr(value, "idl_TemplateModuleRef", None)
                setattr(value, "idl_TemplateModuleRef", self)

    @property
    def idl_ScopedName42(self):
        return self.__idl_ScopedName42

    @idl_ScopedName42.setter
    def idl_ScopedName42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName42", None)
        self.__idl_ScopedName42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ExceptionList41"):
                opp_val = getattr(old_value, "idl_ExceptionList41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ExceptionList41"):
                opp_val = getattr(value, "idl_ExceptionList41", None)
                if opp_val is None:
                    setattr(value, "idl_ExceptionList41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_ScopedName188(self):
        return self.__idl_ScopedName188

    @idl_ScopedName188.setter
    def idl_ScopedName188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName188", None)
        self.__idl_ScopedName188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PublishesDcl"):
                opp_val = getattr(old_value, "idl_PublishesDcl", None)
                if opp_val == self:
                    setattr(old_value, "idl_PublishesDcl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PublishesDcl"):
                opp_val = getattr(value, "idl_PublishesDcl", None)
                setattr(value, "idl_PublishesDcl", self)

    @property
    def idl_ScopedName263(self):
        return self.__idl_ScopedName263

    @idl_ScopedName263.setter
    def idl_ScopedName263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName263", None)
        self.__idl_ScopedName263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConnectorHeader262"):
                opp_val = getattr(old_value, "idl_ConnectorHeader262", None)
                if opp_val == self:
                    setattr(old_value, "idl_ConnectorHeader262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConnectorHeader262"):
                opp_val = getattr(value, "idl_ConnectorHeader262", None)
                setattr(value, "idl_ConnectorHeader262", self)

    @property
    def idl_ScopedName212(self):
        return self.__idl_ScopedName212

    @idl_ScopedName212.setter
    def idl_ScopedName212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName212", None)
        self.__idl_ScopedName212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_HomeDecl211"):
                opp_val = getattr(old_value, "idl_HomeDecl211", None)
                if opp_val == self:
                    setattr(old_value, "idl_HomeDecl211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_HomeDecl211"):
                opp_val = getattr(value, "idl_HomeDecl211", None)
                setattr(value, "idl_HomeDecl211", self)

    @property
    def idl_ScopedName254(self):
        return self.__idl_ScopedName254

    @idl_ScopedName254.setter
    def idl_ScopedName254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName254", None)
        self.__idl_ScopedName254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PortDecl"):
                opp_val = getattr(old_value, "idl_PortDecl", None)
                if opp_val == self:
                    setattr(old_value, "idl_PortDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PortDecl"):
                opp_val = getattr(value, "idl_PortDecl", None)
                setattr(value, "idl_PortDecl", self)

    @property
    def idl_ScopedName193(self):
        return self.__idl_ScopedName193

    @idl_ScopedName193.setter
    def idl_ScopedName193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName193", None)
        self.__idl_ScopedName193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_EmitDcl"):
                opp_val = getattr(old_value, "idl_EmitDcl", None)
                if opp_val == self:
                    setattr(old_value, "idl_EmitDcl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_EmitDcl"):
                opp_val = getattr(value, "idl_EmitDcl", None)
                setattr(value, "idl_EmitDcl", self)

    @property
    def idl_ScopedName240(self):
        return self.__idl_ScopedName240

    @idl_ScopedName240.setter
    def idl_ScopedName240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName240", None)
        self.__idl_ScopedName240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_EventDcl239"):
                opp_val = getattr(old_value, "idl_EventDcl239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_EventDcl239"):
                opp_val = getattr(value, "idl_EventDcl239", None)
                if opp_val is None:
                    setattr(value, "idl_EventDcl239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_ScopedName183(self):
        return self.__idl_ScopedName183

    @idl_ScopedName183.setter
    def idl_ScopedName183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName183", None)
        self.__idl_ScopedName183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_UsesDcl"):
                opp_val = getattr(old_value, "idl_UsesDcl", None)
                if opp_val == self:
                    setattr(old_value, "idl_UsesDcl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_UsesDcl"):
                opp_val = getattr(value, "idl_UsesDcl", None)
                setattr(value, "idl_UsesDcl", self)

    @property
    def idl_ScopedName271(self):
        return self.__idl_ScopedName271

    @idl_ScopedName271.setter
    def idl_ScopedName271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName271", None)
        self.__idl_ScopedName271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_TemplateModuleInst"):
                opp_val = getattr(old_value, "idl_TemplateModuleInst", None)
                if opp_val == self:
                    setattr(old_value, "idl_TemplateModuleInst", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_TemplateModuleInst"):
                opp_val = getattr(value, "idl_TemplateModuleInst", None)
                setattr(value, "idl_TemplateModuleInst", self)

    @property
    def idl_ScopedName171(self):
        return self.__idl_ScopedName171

    @idl_ScopedName171.setter
    def idl_ScopedName171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName171", None)
        self.__idl_ScopedName171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ComponentDecl170"):
                opp_val = getattr(old_value, "idl_ComponentDecl170", None)
                if opp_val == self:
                    setattr(old_value, "idl_ComponentDecl170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ComponentDecl170"):
                opp_val = getattr(value, "idl_ComponentDecl170", None)
                setattr(value, "idl_ComponentDecl170", self)

    @property
    def idl_ScopedName174(self):
        return self.__idl_ScopedName174

    @idl_ScopedName174.setter
    def idl_ScopedName174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName174", None)
        self.__idl_ScopedName174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ComponentDecl173"):
                opp_val = getattr(old_value, "idl_ComponentDecl173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ComponentDecl173"):
                opp_val = getattr(value, "idl_ComponentDecl173", None)
                if opp_val is None:
                    setattr(value, "idl_ComponentDecl173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_ScopedName178(self):
        return self.__idl_ScopedName178

    @idl_ScopedName178.setter
    def idl_ScopedName178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName178", None)
        self.__idl_ScopedName178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ProvidesDcl"):
                opp_val = getattr(old_value, "idl_ProvidesDcl", None)
                if opp_val == self:
                    setattr(old_value, "idl_ProvidesDcl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ProvidesDcl"):
                opp_val = getattr(value, "idl_ProvidesDcl", None)
                setattr(value, "idl_ProvidesDcl", self)

    @property
    def idl_ScopedName209(self):
        return self.__idl_ScopedName209

    @idl_ScopedName209.setter
    def idl_ScopedName209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName209", None)
        self.__idl_ScopedName209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_HomeDecl208"):
                opp_val = getattr(old_value, "idl_HomeDecl208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_HomeDecl208"):
                opp_val = getattr(value, "idl_HomeDecl208", None)
                if opp_val is None:
                    setattr(value, "idl_HomeDecl208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_ScopedName219(self):
        return self.__idl_ScopedName219

    @idl_ScopedName219.setter
    def idl_ScopedName219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName219", None)
        self.__idl_ScopedName219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PrimaryKeySpec218"):
                opp_val = getattr(old_value, "idl_PrimaryKeySpec218", None)
                if opp_val == self:
                    setattr(old_value, "idl_PrimaryKeySpec218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PrimaryKeySpec218"):
                opp_val = getattr(value, "idl_PrimaryKeySpec218", None)
                setattr(value, "idl_PrimaryKeySpec218", self)

    @property
    def idl_ScopedName206(self):
        return self.__idl_ScopedName206

    @idl_ScopedName206.setter
    def idl_ScopedName206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ScopedName__idl_ScopedName206", None)
        self.__idl_ScopedName206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_HomeDecl205"):
                opp_val = getattr(old_value, "idl_HomeDecl205", None)
                if opp_val == self:
                    setattr(old_value, "idl_HomeDecl205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_HomeDecl205"):
                opp_val = getattr(value, "idl_HomeDecl205", None)
                setattr(value, "idl_HomeDecl205", self)

class idl_ConstExp(PrimaryExpr, ActualParameter):

    pass
class idl_Preproc_If_Val:

    pass
class idl_Preproc_If_Compare:

    def __init__(self, op: str, idl_Preproc_If_Compare: "idl_Preproc_If" = None, idl_Preproc_If_Compare6: "idl_Preproc_If_Val" = None, idl_Preproc_If_Compare8: "idl_Preproc_If_Val" = None):
        self.op = op
        self.idl_Preproc_If_Compare = idl_Preproc_If_Compare
        self.idl_Preproc_If_Compare6 = idl_Preproc_If_Compare6
        self.idl_Preproc_If_Compare8 = idl_Preproc_If_Compare8
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def idl_Preproc_If_Compare6(self):
        return self.__idl_Preproc_If_Compare6

    @idl_Preproc_If_Compare6.setter
    def idl_Preproc_If_Compare6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Preproc_If_Compare__idl_Preproc_If_Compare6", None)
        self.__idl_Preproc_If_Compare6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Preproc_If_Val"):
                opp_val = getattr(old_value, "idl_Preproc_If_Val", None)
                if opp_val == self:
                    setattr(old_value, "idl_Preproc_If_Val", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Preproc_If_Val"):
                opp_val = getattr(value, "idl_Preproc_If_Val", None)
                setattr(value, "idl_Preproc_If_Val", self)

    @property
    def idl_Preproc_If_Compare(self):
        return self.__idl_Preproc_If_Compare

    @idl_Preproc_If_Compare.setter
    def idl_Preproc_If_Compare(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Preproc_If_Compare__idl_Preproc_If_Compare", None)
        self.__idl_Preproc_If_Compare = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Preproc_If"):
                opp_val = getattr(old_value, "idl_Preproc_If", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Preproc_If"):
                opp_val = getattr(value, "idl_Preproc_If", None)
                if opp_val is None:
                    setattr(value, "idl_Preproc_If", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_Preproc_If_Compare8(self):
        return self.__idl_Preproc_If_Compare8

    @idl_Preproc_If_Compare8.setter
    def idl_Preproc_If_Compare8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Preproc_If_Compare__idl_Preproc_If_Compare8", None)
        self.__idl_Preproc_If_Compare8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Preproc_If_Val9"):
                opp_val = getattr(old_value, "idl_Preproc_If_Val9", None)
                if opp_val == self:
                    setattr(old_value, "idl_Preproc_If_Val9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Preproc_If_Val9"):
                opp_val = getattr(value, "idl_Preproc_If_Val9", None)
                setattr(value, "idl_Preproc_If_Val9", self)

class idl_FileName:

    def __init__(self, name: str, idl_FileName: "idl_Preproc_Include" = None):
        self.name = name
        self.idl_FileName = idl_FileName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_FileName(self):
        return self.__idl_FileName

    @idl_FileName.setter
    def idl_FileName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_FileName__idl_FileName", None)
        self.__idl_FileName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Preproc_Include"):
                opp_val = getattr(old_value, "idl_Preproc_Include", None)
                if opp_val == self:
                    setattr(old_value, "idl_Preproc_Include", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Preproc_Include"):
                opp_val = getattr(value, "idl_Preproc_Include", None)
                setattr(value, "idl_Preproc_Include", self)

class Preproc_Pragma:

    pass
class idl_Preproc_Pragma_Ciao_Lem(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Home(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Component(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Conn_Type(Preproc_Pragma):

    def __init__(self, valuePort: str, valueConnType: str):
        self.valuePort = valuePort
        self.valueConnType = valueConnType
        
    @property
    def valuePort(self) -> str:
        return self.__valuePort

    @valuePort.setter
    def valuePort(self, valuePort: str):
        self.__valuePort = valuePort

    @property
    def valueConnType(self) -> str:
        return self.__valueConnType

    @valueConnType.setter
    def valueConnType(self, valueConnType: str):
        self.__valueConnType = valueConnType

class idl_Preproc_Pragma_DDS4CCM_Impl(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Misc(Preproc_Pragma):

    pass
class idl_Preproc_Pragma_Ndds(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Ciao_Ami4ccm_Idl(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Ciao_Ami4ccm_Interface(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma_Prefix(Preproc_Pragma):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Preproc:

    pass
class idl_File_Marker(Preproc):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class idl_Preproc_Error(Preproc):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Else(Preproc):

    pass
class idl_Preproc_Ifdef(Preproc):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Pragma(Preproc):

    pass
class idl_Excluded_File_Marker(Preproc):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class idl_Preproc_Endif(Preproc):

    pass
class idl_Preproc_If(Preproc):

    def __init__(self, negation: bool, idl_Preproc_If: set["idl_Preproc_If_Compare"] = None):
        self.negation = negation
        self.idl_Preproc_If = idl_Preproc_If if idl_Preproc_If is not None else set()
        
    @property
    def negation(self) -> bool:
        return self.__negation

    @negation.setter
    def negation(self, negation: bool):
        self.__negation = negation

    @property
    def idl_Preproc_If(self):
        return self.__idl_Preproc_If

    @idl_Preproc_If.setter
    def idl_Preproc_If(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Preproc_If__idl_Preproc_If", None)
        self.__idl_Preproc_If = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_Preproc_If_Compare"):
                    opp_val = getattr(item, "idl_Preproc_If_Compare", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_Preproc_If_Compare", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_Preproc_If_Compare"):
                    opp_val = getattr(item, "idl_Preproc_If_Compare", None)
                    
                    setattr(item, "idl_Preproc_If_Compare", self)
                    

class idl_Preproc_Ifndef(Preproc):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Define(Preproc):

    def __init__(self, value: str, idl_Preproc_Define: "idl_ConstExp" = None):
        self.value = value
        self.idl_Preproc_Define = idl_Preproc_Define
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def idl_Preproc_Define(self):
        return self.__idl_Preproc_Define

    @idl_Preproc_Define.setter
    def idl_Preproc_Define(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Preproc_Define__idl_Preproc_Define", None)
        self.__idl_Preproc_Define = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConstExp13"):
                opp_val = getattr(old_value, "idl_ConstExp13", None)
                if opp_val == self:
                    setattr(old_value, "idl_ConstExp13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConstExp13"):
                opp_val = getattr(value, "idl_ConstExp13", None)
                setattr(value, "idl_ConstExp13", self)

class idl_Preproc_Undef(Preproc):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class idl_Preproc_Include(Preproc):

    def __init__(self, strValue: str, idl_Preproc_Include: "idl_FileName" = None):
        self.strValue = strValue
        self.idl_Preproc_Include = idl_Preproc_Include
        
    @property
    def strValue(self) -> str:
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue

    @property
    def idl_Preproc_Include(self):
        return self.__idl_Preproc_Include

    @idl_Preproc_Include.setter
    def idl_Preproc_Include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Preproc_Include__idl_Preproc_Include", None)
        self.__idl_Preproc_Include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_FileName"):
                opp_val = getattr(old_value, "idl_FileName", None)
                if opp_val == self:
                    setattr(old_value, "idl_FileName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_FileName"):
                opp_val = getattr(value, "idl_FileName", None)
                setattr(value, "idl_FileName", self)

class ComponentExport:

    pass
class idl_UsesDcl(ConnectorExport, PortExport, ComponentExport):

    def __init__(self, isMultiple: bool, name: str, idl_UsesDcl: "idl_ScopedName" = None, idl_UsesDcl185: set["idl_IDLComment"] = None):
        self.isMultiple = isMultiple
        self.name = name
        self.idl_UsesDcl = idl_UsesDcl
        self.idl_UsesDcl185 = idl_UsesDcl185 if idl_UsesDcl185 is not None else set()
        
    @property
    def isMultiple(self) -> bool:
        return self.__isMultiple

    @isMultiple.setter
    def isMultiple(self, isMultiple: bool):
        self.__isMultiple = isMultiple

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_UsesDcl(self):
        return self.__idl_UsesDcl

    @idl_UsesDcl.setter
    def idl_UsesDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UsesDcl__idl_UsesDcl", None)
        self.__idl_UsesDcl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName183"):
                opp_val = getattr(old_value, "idl_ScopedName183", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName183"):
                opp_val = getattr(value, "idl_ScopedName183", None)
                setattr(value, "idl_ScopedName183", self)

    @property
    def idl_UsesDcl185(self):
        return self.__idl_UsesDcl185

    @idl_UsesDcl185.setter
    def idl_UsesDcl185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_UsesDcl__idl_UsesDcl185", None)
        self.__idl_UsesDcl185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment186"):
                    opp_val = getattr(item, "idl_IDLComment186", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment186"):
                    opp_val = getattr(item, "idl_IDLComment186", None)
                    
                    setattr(item, "idl_IDLComment186", self)
                    

class idl_PortDecl(ComponentExport, ConnectorExport):

    def __init__(self, isMirror: bool, name: str, idl_PortDecl: "idl_ScopedName" = None, idl_PortDecl256: set["idl_IDLComment"] = None):
        self.isMirror = isMirror
        self.name = name
        self.idl_PortDecl = idl_PortDecl
        self.idl_PortDecl256 = idl_PortDecl256 if idl_PortDecl256 is not None else set()
        
    @property
    def isMirror(self) -> bool:
        return self.__isMirror

    @isMirror.setter
    def isMirror(self, isMirror: bool):
        self.__isMirror = isMirror

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_PortDecl(self):
        return self.__idl_PortDecl

    @idl_PortDecl.setter
    def idl_PortDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_PortDecl__idl_PortDecl", None)
        self.__idl_PortDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName254"):
                opp_val = getattr(old_value, "idl_ScopedName254", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName254"):
                opp_val = getattr(value, "idl_ScopedName254", None)
                setattr(value, "idl_ScopedName254", self)

    @property
    def idl_PortDecl256(self):
        return self.__idl_PortDecl256

    @idl_PortDecl256.setter
    def idl_PortDecl256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_PortDecl__idl_PortDecl256", None)
        self.__idl_PortDecl256 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment257"):
                    opp_val = getattr(item, "idl_IDLComment257", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment257"):
                    opp_val = getattr(item, "idl_IDLComment257", None)
                    
                    setattr(item, "idl_IDLComment257", self)
                    

class idl_EmitDcl(ComponentExport):

    def __init__(self, name: str, idl_EmitDcl: "idl_ScopedName" = None, idl_EmitDcl195: set["idl_IDLComment"] = None):
        self.name = name
        self.idl_EmitDcl = idl_EmitDcl
        self.idl_EmitDcl195 = idl_EmitDcl195 if idl_EmitDcl195 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_EmitDcl195(self):
        return self.__idl_EmitDcl195

    @idl_EmitDcl195.setter
    def idl_EmitDcl195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EmitDcl__idl_EmitDcl195", None)
        self.__idl_EmitDcl195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment196"):
                    opp_val = getattr(item, "idl_IDLComment196", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment196"):
                    opp_val = getattr(item, "idl_IDLComment196", None)
                    
                    setattr(item, "idl_IDLComment196", self)
                    

    @property
    def idl_EmitDcl(self):
        return self.__idl_EmitDcl

    @idl_EmitDcl.setter
    def idl_EmitDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_EmitDcl__idl_EmitDcl", None)
        self.__idl_EmitDcl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName193"):
                opp_val = getattr(old_value, "idl_ScopedName193", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName193"):
                opp_val = getattr(value, "idl_ScopedName193", None)
                setattr(value, "idl_ScopedName193", self)

class idl_ConsumesDcl(ComponentExport):

    def __init__(self, name: str, idl_ConsumesDcl: "idl_ScopedName" = None, idl_ConsumesDcl200: set["idl_IDLComment"] = None):
        self.name = name
        self.idl_ConsumesDcl = idl_ConsumesDcl
        self.idl_ConsumesDcl200 = idl_ConsumesDcl200 if idl_ConsumesDcl200 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ConsumesDcl200(self):
        return self.__idl_ConsumesDcl200

    @idl_ConsumesDcl200.setter
    def idl_ConsumesDcl200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConsumesDcl__idl_ConsumesDcl200", None)
        self.__idl_ConsumesDcl200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment201"):
                    opp_val = getattr(item, "idl_IDLComment201", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment201"):
                    opp_val = getattr(item, "idl_IDLComment201", None)
                    
                    setattr(item, "idl_IDLComment201", self)
                    

    @property
    def idl_ConsumesDcl(self):
        return self.__idl_ConsumesDcl

    @idl_ConsumesDcl.setter
    def idl_ConsumesDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConsumesDcl__idl_ConsumesDcl", None)
        self.__idl_ConsumesDcl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName198"):
                opp_val = getattr(old_value, "idl_ScopedName198", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName198"):
                opp_val = getattr(value, "idl_ScopedName198", None)
                setattr(value, "idl_ScopedName198", self)

class idl_ProvidesDcl(ConnectorExport, PortExport, ComponentExport):

    def __init__(self, name: str, idl_ProvidesDcl: "idl_ScopedName" = None, idl_ProvidesDcl180: set["idl_IDLComment"] = None):
        self.name = name
        self.idl_ProvidesDcl = idl_ProvidesDcl
        self.idl_ProvidesDcl180 = idl_ProvidesDcl180 if idl_ProvidesDcl180 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ProvidesDcl(self):
        return self.__idl_ProvidesDcl

    @idl_ProvidesDcl.setter
    def idl_ProvidesDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ProvidesDcl__idl_ProvidesDcl", None)
        self.__idl_ProvidesDcl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName178"):
                opp_val = getattr(old_value, "idl_ScopedName178", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName178"):
                opp_val = getattr(value, "idl_ScopedName178", None)
                setattr(value, "idl_ScopedName178", self)

    @property
    def idl_ProvidesDcl180(self):
        return self.__idl_ProvidesDcl180

    @idl_ProvidesDcl180.setter
    def idl_ProvidesDcl180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ProvidesDcl__idl_ProvidesDcl180", None)
        self.__idl_ProvidesDcl180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment181"):
                    opp_val = getattr(item, "idl_IDLComment181", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment181"):
                    opp_val = getattr(item, "idl_IDLComment181", None)
                    
                    setattr(item, "idl_IDLComment181", self)
                    

class idl_PublishesDcl(ComponentExport):

    def __init__(self, name: str, idl_PublishesDcl: "idl_ScopedName" = None, idl_PublishesDcl190: set["idl_IDLComment"] = None):
        self.name = name
        self.idl_PublishesDcl = idl_PublishesDcl
        self.idl_PublishesDcl190 = idl_PublishesDcl190 if idl_PublishesDcl190 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_PublishesDcl(self):
        return self.__idl_PublishesDcl

    @idl_PublishesDcl.setter
    def idl_PublishesDcl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_PublishesDcl__idl_PublishesDcl", None)
        self.__idl_PublishesDcl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName188"):
                opp_val = getattr(old_value, "idl_ScopedName188", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName188"):
                opp_val = getattr(value, "idl_ScopedName188", None)
                setattr(value, "idl_ScopedName188", self)

    @property
    def idl_PublishesDcl190(self):
        return self.__idl_PublishesDcl190

    @idl_PublishesDcl190.setter
    def idl_PublishesDcl190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_PublishesDcl__idl_PublishesDcl190", None)
        self.__idl_PublishesDcl190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment191"):
                    opp_val = getattr(item, "idl_IDLComment191", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment191"):
                    opp_val = getattr(item, "idl_IDLComment191", None)
                    
                    setattr(item, "idl_IDLComment191", self)
                    

class Export:

    pass
class idl_AttrDecl(Export, ConnectorExport, PortExport, ComponentExport):

    def __init__(self, names: str, idl_AttrDecl: set["idl_IDLComment"] = None, idl_AttrDecl31: "idl_ParamTypeSpec" = None):
        self.names = names
        self.idl_AttrDecl = idl_AttrDecl if idl_AttrDecl is not None else set()
        self.idl_AttrDecl31 = idl_AttrDecl31
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def idl_AttrDecl(self):
        return self.__idl_AttrDecl

    @idl_AttrDecl.setter
    def idl_AttrDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AttrDecl__idl_AttrDecl", None)
        self.__idl_AttrDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment29"):
                    opp_val = getattr(item, "idl_IDLComment29", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment29"):
                    opp_val = getattr(item, "idl_IDLComment29", None)
                    
                    setattr(item, "idl_IDLComment29", self)
                    

    @property
    def idl_AttrDecl31(self):
        return self.__idl_AttrDecl31

    @idl_AttrDecl31.setter
    def idl_AttrDecl31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_AttrDecl__idl_AttrDecl31", None)
        self.__idl_AttrDecl31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParamTypeSpec"):
                opp_val = getattr(old_value, "idl_ParamTypeSpec", None)
                if opp_val == self:
                    setattr(old_value, "idl_ParamTypeSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParamTypeSpec"):
                opp_val = getattr(value, "idl_ParamTypeSpec", None)
                setattr(value, "idl_ParamTypeSpec", self)

class idl_OpDecl(Export):

    def __init__(self, isOneway: bool, name: str, idl_OpDecl: set["idl_IDLComment"] = None, idl_OpDecl46: "idl_OpTypeDecl" = None, idl_OpDecl48: "idl_ParameterDecls" = None, idl_OpDecl50: "idl_ExceptionList" = None, idl_OpDecl53: "idl_ContextExpr" = None):
        self.isOneway = isOneway
        self.name = name
        self.idl_OpDecl = idl_OpDecl if idl_OpDecl is not None else set()
        self.idl_OpDecl46 = idl_OpDecl46
        self.idl_OpDecl48 = idl_OpDecl48
        self.idl_OpDecl50 = idl_OpDecl50
        self.idl_OpDecl53 = idl_OpDecl53
        
    @property
    def isOneway(self) -> bool:
        return self.__isOneway

    @isOneway.setter
    def isOneway(self, isOneway: bool):
        self.__isOneway = isOneway

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_OpDecl53(self):
        return self.__idl_OpDecl53

    @idl_OpDecl53.setter
    def idl_OpDecl53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OpDecl__idl_OpDecl53", None)
        self.__idl_OpDecl53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ContextExpr"):
                opp_val = getattr(old_value, "idl_ContextExpr", None)
                if opp_val == self:
                    setattr(old_value, "idl_ContextExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ContextExpr"):
                opp_val = getattr(value, "idl_ContextExpr", None)
                setattr(value, "idl_ContextExpr", self)

    @property
    def idl_OpDecl48(self):
        return self.__idl_OpDecl48

    @idl_OpDecl48.setter
    def idl_OpDecl48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OpDecl__idl_OpDecl48", None)
        self.__idl_OpDecl48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParameterDecls"):
                opp_val = getattr(old_value, "idl_ParameterDecls", None)
                if opp_val == self:
                    setattr(old_value, "idl_ParameterDecls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParameterDecls"):
                opp_val = getattr(value, "idl_ParameterDecls", None)
                setattr(value, "idl_ParameterDecls", self)

    @property
    def idl_OpDecl(self):
        return self.__idl_OpDecl

    @idl_OpDecl.setter
    def idl_OpDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OpDecl__idl_OpDecl", None)
        self.__idl_OpDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment44"):
                    opp_val = getattr(item, "idl_IDLComment44", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment44"):
                    opp_val = getattr(item, "idl_IDLComment44", None)
                    
                    setattr(item, "idl_IDLComment44", self)
                    

    @property
    def idl_OpDecl50(self):
        return self.__idl_OpDecl50

    @idl_OpDecl50.setter
    def idl_OpDecl50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OpDecl__idl_OpDecl50", None)
        self.__idl_OpDecl50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ExceptionList51"):
                opp_val = getattr(old_value, "idl_ExceptionList51", None)
                if opp_val == self:
                    setattr(old_value, "idl_ExceptionList51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ExceptionList51"):
                opp_val = getattr(value, "idl_ExceptionList51", None)
                setattr(value, "idl_ExceptionList51", self)

    @property
    def idl_OpDecl46(self):
        return self.__idl_OpDecl46

    @idl_OpDecl46.setter
    def idl_OpDecl46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_OpDecl__idl_OpDecl46", None)
        self.__idl_OpDecl46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_OpTypeDecl"):
                opp_val = getattr(old_value, "idl_OpTypeDecl", None)
                if opp_val == self:
                    setattr(old_value, "idl_OpTypeDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_OpTypeDecl"):
                opp_val = getattr(value, "idl_OpTypeDecl", None)
                setattr(value, "idl_OpTypeDecl", self)

class Definition:

    pass
class idl_ComponentDecl(FixedDefinition, Definition, TemplateDefinition):

    def __init__(self, name: str, idl_ComponentDecl: set["idl_IDLComment"] = None, idl_ComponentDecl170: "idl_ScopedName" = None, idl_ComponentDecl173: set["idl_ScopedName"] = None, idl_ComponentDecl176: set["idl_ComponentExport"] = None):
        self.name = name
        self.idl_ComponentDecl = idl_ComponentDecl if idl_ComponentDecl is not None else set()
        self.idl_ComponentDecl170 = idl_ComponentDecl170
        self.idl_ComponentDecl173 = idl_ComponentDecl173 if idl_ComponentDecl173 is not None else set()
        self.idl_ComponentDecl176 = idl_ComponentDecl176 if idl_ComponentDecl176 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ComponentDecl173(self):
        return self.__idl_ComponentDecl173

    @idl_ComponentDecl173.setter
    def idl_ComponentDecl173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ComponentDecl__idl_ComponentDecl173", None)
        self.__idl_ComponentDecl173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ScopedName174"):
                    opp_val = getattr(item, "idl_ScopedName174", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ScopedName174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ScopedName174"):
                    opp_val = getattr(item, "idl_ScopedName174", None)
                    
                    setattr(item, "idl_ScopedName174", self)
                    

    @property
    def idl_ComponentDecl(self):
        return self.__idl_ComponentDecl

    @idl_ComponentDecl.setter
    def idl_ComponentDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ComponentDecl__idl_ComponentDecl", None)
        self.__idl_ComponentDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment168"):
                    opp_val = getattr(item, "idl_IDLComment168", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment168"):
                    opp_val = getattr(item, "idl_IDLComment168", None)
                    
                    setattr(item, "idl_IDLComment168", self)
                    

    @property
    def idl_ComponentDecl176(self):
        return self.__idl_ComponentDecl176

    @idl_ComponentDecl176.setter
    def idl_ComponentDecl176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ComponentDecl__idl_ComponentDecl176", None)
        self.__idl_ComponentDecl176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ComponentExport"):
                    opp_val = getattr(item, "idl_ComponentExport", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ComponentExport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ComponentExport"):
                    opp_val = getattr(item, "idl_ComponentExport", None)
                    
                    setattr(item, "idl_ComponentExport", self)
                    

    @property
    def idl_ComponentDecl170(self):
        return self.__idl_ComponentDecl170

    @idl_ComponentDecl170.setter
    def idl_ComponentDecl170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ComponentDecl__idl_ComponentDecl170", None)
        self.__idl_ComponentDecl170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName171"):
                opp_val = getattr(old_value, "idl_ScopedName171", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName171"):
                opp_val = getattr(value, "idl_ScopedName171", None)
                setattr(value, "idl_ScopedName171", self)

class idl_HomeDecl(Definition, TemplateDefinition, FixedDefinition):

    def __init__(self, name: str, idl_HomeDecl208: set["idl_ScopedName"] = None, idl_HomeDecl211: "idl_ScopedName" = None, idl_HomeDecl214: "idl_PrimaryKeySpec" = None, idl_HomeDecl216: set["idl_HomeExport"] = None, idl_HomeDecl: set["idl_IDLComment"] = None, idl_HomeDecl205: "idl_ScopedName" = None):
        self.name = name
        self.idl_HomeDecl208 = idl_HomeDecl208 if idl_HomeDecl208 is not None else set()
        self.idl_HomeDecl211 = idl_HomeDecl211
        self.idl_HomeDecl214 = idl_HomeDecl214
        self.idl_HomeDecl216 = idl_HomeDecl216 if idl_HomeDecl216 is not None else set()
        self.idl_HomeDecl = idl_HomeDecl if idl_HomeDecl is not None else set()
        self.idl_HomeDecl205 = idl_HomeDecl205
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_HomeDecl211(self):
        return self.__idl_HomeDecl211

    @idl_HomeDecl211.setter
    def idl_HomeDecl211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_HomeDecl__idl_HomeDecl211", None)
        self.__idl_HomeDecl211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName212"):
                opp_val = getattr(old_value, "idl_ScopedName212", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName212"):
                opp_val = getattr(value, "idl_ScopedName212", None)
                setattr(value, "idl_ScopedName212", self)

    @property
    def idl_HomeDecl208(self):
        return self.__idl_HomeDecl208

    @idl_HomeDecl208.setter
    def idl_HomeDecl208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_HomeDecl__idl_HomeDecl208", None)
        self.__idl_HomeDecl208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ScopedName209"):
                    opp_val = getattr(item, "idl_ScopedName209", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ScopedName209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ScopedName209"):
                    opp_val = getattr(item, "idl_ScopedName209", None)
                    
                    setattr(item, "idl_ScopedName209", self)
                    

    @property
    def idl_HomeDecl(self):
        return self.__idl_HomeDecl

    @idl_HomeDecl.setter
    def idl_HomeDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_HomeDecl__idl_HomeDecl", None)
        self.__idl_HomeDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment203"):
                    opp_val = getattr(item, "idl_IDLComment203", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment203"):
                    opp_val = getattr(item, "idl_IDLComment203", None)
                    
                    setattr(item, "idl_IDLComment203", self)
                    

    @property
    def idl_HomeDecl214(self):
        return self.__idl_HomeDecl214

    @idl_HomeDecl214.setter
    def idl_HomeDecl214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_HomeDecl__idl_HomeDecl214", None)
        self.__idl_HomeDecl214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PrimaryKeySpec"):
                opp_val = getattr(old_value, "idl_PrimaryKeySpec", None)
                if opp_val == self:
                    setattr(old_value, "idl_PrimaryKeySpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PrimaryKeySpec"):
                opp_val = getattr(value, "idl_PrimaryKeySpec", None)
                setattr(value, "idl_PrimaryKeySpec", self)

    @property
    def idl_HomeDecl216(self):
        return self.__idl_HomeDecl216

    @idl_HomeDecl216.setter
    def idl_HomeDecl216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_HomeDecl__idl_HomeDecl216", None)
        self.__idl_HomeDecl216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_HomeExport"):
                    opp_val = getattr(item, "idl_HomeExport", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_HomeExport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_HomeExport"):
                    opp_val = getattr(item, "idl_HomeExport", None)
                    
                    setattr(item, "idl_HomeExport", self)
                    

    @property
    def idl_HomeDecl205(self):
        return self.__idl_HomeDecl205

    @idl_HomeDecl205.setter
    def idl_HomeDecl205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_HomeDecl__idl_HomeDecl205", None)
        self.__idl_HomeDecl205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName206"):
                opp_val = getattr(old_value, "idl_ScopedName206", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName206"):
                opp_val = getattr(value, "idl_ScopedName206", None)
                setattr(value, "idl_ScopedName206", self)

class idl_Module(Definition):

    def __init__(self, name: str, idl_Module: set["idl_IDLComment"] = None, idl_Module16: set["idl_Definition"] = None):
        self.name = name
        self.idl_Module = idl_Module if idl_Module is not None else set()
        self.idl_Module16 = idl_Module16 if idl_Module16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_Module16(self):
        return self.__idl_Module16

    @idl_Module16.setter
    def idl_Module16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Module__idl_Module16", None)
        self.__idl_Module16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_Definition17"):
                    opp_val = getattr(item, "idl_Definition17", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_Definition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_Definition17"):
                    opp_val = getattr(item, "idl_Definition17", None)
                    
                    setattr(item, "idl_Definition17", self)
                    

    @property
    def idl_Module(self):
        return self.__idl_Module

    @idl_Module.setter
    def idl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Module__idl_Module", None)
        self.__idl_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment"):
                    opp_val = getattr(item, "idl_IDLComment", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment"):
                    opp_val = getattr(item, "idl_IDLComment", None)
                    
                    setattr(item, "idl_IDLComment", self)
                    

class idl_Connector(FixedDefinition, Definition, TemplateDefinition):

    pass
class idl_TemplateModule(Definition):

    def __init__(self, name: str, idl_TemplateModule: set["idl_FormalParameter"] = None, idl_TemplateModule266: set["idl_TemplateDefinition"] = None):
        self.name = name
        self.idl_TemplateModule = idl_TemplateModule if idl_TemplateModule is not None else set()
        self.idl_TemplateModule266 = idl_TemplateModule266 if idl_TemplateModule266 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_TemplateModule(self):
        return self.__idl_TemplateModule

    @idl_TemplateModule.setter
    def idl_TemplateModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_TemplateModule__idl_TemplateModule", None)
        self.__idl_TemplateModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_FormalParameter"):
                    opp_val = getattr(item, "idl_FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_FormalParameter"):
                    opp_val = getattr(item, "idl_FormalParameter", None)
                    
                    setattr(item, "idl_FormalParameter", self)
                    

    @property
    def idl_TemplateModule266(self):
        return self.__idl_TemplateModule266

    @idl_TemplateModule266.setter
    def idl_TemplateModule266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_TemplateModule__idl_TemplateModule266", None)
        self.__idl_TemplateModule266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_TemplateDefinition"):
                    opp_val = getattr(item, "idl_TemplateDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_TemplateDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_TemplateDefinition"):
                    opp_val = getattr(item, "idl_TemplateDefinition", None)
                    
                    setattr(item, "idl_TemplateDefinition", self)
                    

class idl_StructType(Definition, ConstrTypeSpec, TypeDecl):

    def __init__(self, name: str, idl_StructType: set["idl_IDLComment"] = None, idl_StructType81: set["idl_Member"] = None):
        self.name = name
        self.idl_StructType = idl_StructType if idl_StructType is not None else set()
        self.idl_StructType81 = idl_StructType81 if idl_StructType81 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_StructType(self):
        return self.__idl_StructType

    @idl_StructType.setter
    def idl_StructType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_StructType__idl_StructType", None)
        self.__idl_StructType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment79"):
                    opp_val = getattr(item, "idl_IDLComment79", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment79"):
                    opp_val = getattr(item, "idl_IDLComment79", None)
                    
                    setattr(item, "idl_IDLComment79", self)
                    

    @property
    def idl_StructType81(self):
        return self.__idl_StructType81

    @idl_StructType81.setter
    def idl_StructType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_StructType__idl_StructType81", None)
        self.__idl_StructType81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_Member82"):
                    opp_val = getattr(item, "idl_Member82", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_Member82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_Member82"):
                    opp_val = getattr(item, "idl_Member82", None)
                    
                    setattr(item, "idl_Member82", self)
                    

class idl_Event(Definition, TemplateDefinition, FixedDefinition):

    def __init__(self, isAbstract: bool, name: str):
        self.isAbstract = isAbstract
        self.name = name
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class idl_IDLComment(ComponentExport, PortExport, FixedDefinition, TemplateDefinition, ConnectorExport, Definition, Export):

    def __init__(self, body: str, idl_IDLComment: "idl_Module" = None, idl_IDLComment25: "idl_Interface_header" = None, idl_IDLComment44: "idl_OpDecl" = None, idl_IDLComment29: "idl_AttrDecl" = None, idl_IDLComment56: "idl_ParameterDecls" = None, idl_IDLComment66: "idl_ExceptDecl" = None, idl_IDLComment92: "idl_UnionType" = None, idl_IDLComment101: "idl_Case" = None, idl_IDLComment75: "idl_Member" = None, idl_IDLComment79: "idl_StructType" = None, idl_IDLComment84: "idl_TypeDeclarator" = None, idl_IDLComment116: "idl_EnumType" = None, idl_IDLComment135: "idl_ConstDecl" = None, idl_IDLComment168: "idl_ComponentDecl" = None, idl_IDLComment186: "idl_UsesDcl" = None, idl_IDLComment191: "idl_PublishesDcl" = None, idl_IDLComment196: "idl_EmitDcl" = None, idl_IDLComment201: "idl_ConsumesDcl" = None, idl_IDLComment181: "idl_ProvidesDcl" = None, idl_IDLComment221: "idl_FactoryDcl" = None, idl_IDLComment229: "idl_FinderDcl" = None, idl_IDLComment203: "idl_HomeDecl" = None, idl_IDLComment250: "idl_PortTypeDecl" = None, idl_IDLComment257: "idl_PortDecl" = None, idl_IDLComment276: "idl_TemplateModuleInst" = None):
        self.body = body
        self.idl_IDLComment = idl_IDLComment
        self.idl_IDLComment25 = idl_IDLComment25
        self.idl_IDLComment44 = idl_IDLComment44
        self.idl_IDLComment29 = idl_IDLComment29
        self.idl_IDLComment56 = idl_IDLComment56
        self.idl_IDLComment66 = idl_IDLComment66
        self.idl_IDLComment92 = idl_IDLComment92
        self.idl_IDLComment101 = idl_IDLComment101
        self.idl_IDLComment75 = idl_IDLComment75
        self.idl_IDLComment79 = idl_IDLComment79
        self.idl_IDLComment84 = idl_IDLComment84
        self.idl_IDLComment116 = idl_IDLComment116
        self.idl_IDLComment135 = idl_IDLComment135
        self.idl_IDLComment168 = idl_IDLComment168
        self.idl_IDLComment186 = idl_IDLComment186
        self.idl_IDLComment191 = idl_IDLComment191
        self.idl_IDLComment196 = idl_IDLComment196
        self.idl_IDLComment201 = idl_IDLComment201
        self.idl_IDLComment181 = idl_IDLComment181
        self.idl_IDLComment221 = idl_IDLComment221
        self.idl_IDLComment229 = idl_IDLComment229
        self.idl_IDLComment203 = idl_IDLComment203
        self.idl_IDLComment250 = idl_IDLComment250
        self.idl_IDLComment257 = idl_IDLComment257
        self.idl_IDLComment276 = idl_IDLComment276
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def idl_IDLComment79(self):
        return self.__idl_IDLComment79

    @idl_IDLComment79.setter
    def idl_IDLComment79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment79", None)
        self.__idl_IDLComment79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_StructType"):
                opp_val = getattr(old_value, "idl_StructType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_StructType"):
                opp_val = getattr(value, "idl_StructType", None)
                if opp_val is None:
                    setattr(value, "idl_StructType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment44(self):
        return self.__idl_IDLComment44

    @idl_IDLComment44.setter
    def idl_IDLComment44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment44", None)
        self.__idl_IDLComment44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_OpDecl"):
                opp_val = getattr(old_value, "idl_OpDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_OpDecl"):
                opp_val = getattr(value, "idl_OpDecl", None)
                if opp_val is None:
                    setattr(value, "idl_OpDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment186(self):
        return self.__idl_IDLComment186

    @idl_IDLComment186.setter
    def idl_IDLComment186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment186", None)
        self.__idl_IDLComment186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_UsesDcl185"):
                opp_val = getattr(old_value, "idl_UsesDcl185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_UsesDcl185"):
                opp_val = getattr(value, "idl_UsesDcl185", None)
                if opp_val is None:
                    setattr(value, "idl_UsesDcl185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment25(self):
        return self.__idl_IDLComment25

    @idl_IDLComment25.setter
    def idl_IDLComment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment25", None)
        self.__idl_IDLComment25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Interface_header24"):
                opp_val = getattr(old_value, "idl_Interface_header24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Interface_header24"):
                opp_val = getattr(value, "idl_Interface_header24", None)
                if opp_val is None:
                    setattr(value, "idl_Interface_header24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment203(self):
        return self.__idl_IDLComment203

    @idl_IDLComment203.setter
    def idl_IDLComment203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment203", None)
        self.__idl_IDLComment203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_HomeDecl"):
                opp_val = getattr(old_value, "idl_HomeDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_HomeDecl"):
                opp_val = getattr(value, "idl_HomeDecl", None)
                if opp_val is None:
                    setattr(value, "idl_HomeDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment181(self):
        return self.__idl_IDLComment181

    @idl_IDLComment181.setter
    def idl_IDLComment181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment181", None)
        self.__idl_IDLComment181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ProvidesDcl180"):
                opp_val = getattr(old_value, "idl_ProvidesDcl180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ProvidesDcl180"):
                opp_val = getattr(value, "idl_ProvidesDcl180", None)
                if opp_val is None:
                    setattr(value, "idl_ProvidesDcl180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment29(self):
        return self.__idl_IDLComment29

    @idl_IDLComment29.setter
    def idl_IDLComment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment29", None)
        self.__idl_IDLComment29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_AttrDecl"):
                opp_val = getattr(old_value, "idl_AttrDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_AttrDecl"):
                opp_val = getattr(value, "idl_AttrDecl", None)
                if opp_val is None:
                    setattr(value, "idl_AttrDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment191(self):
        return self.__idl_IDLComment191

    @idl_IDLComment191.setter
    def idl_IDLComment191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment191", None)
        self.__idl_IDLComment191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PublishesDcl190"):
                opp_val = getattr(old_value, "idl_PublishesDcl190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PublishesDcl190"):
                opp_val = getattr(value, "idl_PublishesDcl190", None)
                if opp_val is None:
                    setattr(value, "idl_PublishesDcl190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment116(self):
        return self.__idl_IDLComment116

    @idl_IDLComment116.setter
    def idl_IDLComment116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment116", None)
        self.__idl_IDLComment116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_EnumType"):
                opp_val = getattr(old_value, "idl_EnumType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_EnumType"):
                opp_val = getattr(value, "idl_EnumType", None)
                if opp_val is None:
                    setattr(value, "idl_EnumType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment92(self):
        return self.__idl_IDLComment92

    @idl_IDLComment92.setter
    def idl_IDLComment92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment92", None)
        self.__idl_IDLComment92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_UnionType"):
                opp_val = getattr(old_value, "idl_UnionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_UnionType"):
                opp_val = getattr(value, "idl_UnionType", None)
                if opp_val is None:
                    setattr(value, "idl_UnionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment75(self):
        return self.__idl_IDLComment75

    @idl_IDLComment75.setter
    def idl_IDLComment75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment75", None)
        self.__idl_IDLComment75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Member74"):
                opp_val = getattr(old_value, "idl_Member74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Member74"):
                opp_val = getattr(value, "idl_Member74", None)
                if opp_val is None:
                    setattr(value, "idl_Member74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment257(self):
        return self.__idl_IDLComment257

    @idl_IDLComment257.setter
    def idl_IDLComment257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment257", None)
        self.__idl_IDLComment257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PortDecl256"):
                opp_val = getattr(old_value, "idl_PortDecl256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PortDecl256"):
                opp_val = getattr(value, "idl_PortDecl256", None)
                if opp_val is None:
                    setattr(value, "idl_PortDecl256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment201(self):
        return self.__idl_IDLComment201

    @idl_IDLComment201.setter
    def idl_IDLComment201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment201", None)
        self.__idl_IDLComment201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConsumesDcl200"):
                opp_val = getattr(old_value, "idl_ConsumesDcl200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConsumesDcl200"):
                opp_val = getattr(value, "idl_ConsumesDcl200", None)
                if opp_val is None:
                    setattr(value, "idl_ConsumesDcl200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment84(self):
        return self.__idl_IDLComment84

    @idl_IDLComment84.setter
    def idl_IDLComment84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment84", None)
        self.__idl_IDLComment84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_TypeDeclarator"):
                opp_val = getattr(old_value, "idl_TypeDeclarator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_TypeDeclarator"):
                opp_val = getattr(value, "idl_TypeDeclarator", None)
                if opp_val is None:
                    setattr(value, "idl_TypeDeclarator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment56(self):
        return self.__idl_IDLComment56

    @idl_IDLComment56.setter
    def idl_IDLComment56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment56", None)
        self.__idl_IDLComment56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ParameterDecls55"):
                opp_val = getattr(old_value, "idl_ParameterDecls55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ParameterDecls55"):
                opp_val = getattr(value, "idl_ParameterDecls55", None)
                if opp_val is None:
                    setattr(value, "idl_ParameterDecls55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment276(self):
        return self.__idl_IDLComment276

    @idl_IDLComment276.setter
    def idl_IDLComment276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment276", None)
        self.__idl_IDLComment276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_TemplateModuleInst275"):
                opp_val = getattr(old_value, "idl_TemplateModuleInst275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_TemplateModuleInst275"):
                opp_val = getattr(value, "idl_TemplateModuleInst275", None)
                if opp_val is None:
                    setattr(value, "idl_TemplateModuleInst275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment(self):
        return self.__idl_IDLComment

    @idl_IDLComment.setter
    def idl_IDLComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment", None)
        self.__idl_IDLComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Module"):
                opp_val = getattr(old_value, "idl_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Module"):
                opp_val = getattr(value, "idl_Module", None)
                if opp_val is None:
                    setattr(value, "idl_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment135(self):
        return self.__idl_IDLComment135

    @idl_IDLComment135.setter
    def idl_IDLComment135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment135", None)
        self.__idl_IDLComment135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConstDecl134"):
                opp_val = getattr(old_value, "idl_ConstDecl134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConstDecl134"):
                opp_val = getattr(value, "idl_ConstDecl134", None)
                if opp_val is None:
                    setattr(value, "idl_ConstDecl134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment229(self):
        return self.__idl_IDLComment229

    @idl_IDLComment229.setter
    def idl_IDLComment229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment229", None)
        self.__idl_IDLComment229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_FinderDcl"):
                opp_val = getattr(old_value, "idl_FinderDcl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_FinderDcl"):
                opp_val = getattr(value, "idl_FinderDcl", None)
                if opp_val is None:
                    setattr(value, "idl_FinderDcl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment221(self):
        return self.__idl_IDLComment221

    @idl_IDLComment221.setter
    def idl_IDLComment221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment221", None)
        self.__idl_IDLComment221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_FactoryDcl"):
                opp_val = getattr(old_value, "idl_FactoryDcl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_FactoryDcl"):
                opp_val = getattr(value, "idl_FactoryDcl", None)
                if opp_val is None:
                    setattr(value, "idl_FactoryDcl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment196(self):
        return self.__idl_IDLComment196

    @idl_IDLComment196.setter
    def idl_IDLComment196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment196", None)
        self.__idl_IDLComment196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_EmitDcl195"):
                opp_val = getattr(old_value, "idl_EmitDcl195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_EmitDcl195"):
                opp_val = getattr(value, "idl_EmitDcl195", None)
                if opp_val is None:
                    setattr(value, "idl_EmitDcl195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment101(self):
        return self.__idl_IDLComment101

    @idl_IDLComment101.setter
    def idl_IDLComment101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment101", None)
        self.__idl_IDLComment101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Case100"):
                opp_val = getattr(old_value, "idl_Case100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Case100"):
                opp_val = getattr(value, "idl_Case100", None)
                if opp_val is None:
                    setattr(value, "idl_Case100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment66(self):
        return self.__idl_IDLComment66

    @idl_IDLComment66.setter
    def idl_IDLComment66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment66", None)
        self.__idl_IDLComment66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ExceptDecl"):
                opp_val = getattr(old_value, "idl_ExceptDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ExceptDecl"):
                opp_val = getattr(value, "idl_ExceptDecl", None)
                if opp_val is None:
                    setattr(value, "idl_ExceptDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment168(self):
        return self.__idl_IDLComment168

    @idl_IDLComment168.setter
    def idl_IDLComment168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment168", None)
        self.__idl_IDLComment168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ComponentDecl"):
                opp_val = getattr(old_value, "idl_ComponentDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ComponentDecl"):
                opp_val = getattr(value, "idl_ComponentDecl", None)
                if opp_val is None:
                    setattr(value, "idl_ComponentDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def idl_IDLComment250(self):
        return self.__idl_IDLComment250

    @idl_IDLComment250.setter
    def idl_IDLComment250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_IDLComment__idl_IDLComment250", None)
        self.__idl_IDLComment250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_PortTypeDecl"):
                opp_val = getattr(old_value, "idl_PortTypeDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_PortTypeDecl"):
                opp_val = getattr(value, "idl_PortTypeDecl", None)
                if opp_val is None:
                    setattr(value, "idl_PortTypeDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class idl_ComponentForwardDecl(Definition):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class idl_TemplateModuleInst(Definition):

    def __init__(self, name: str, idl_TemplateModuleInst: "idl_ScopedName" = None, idl_TemplateModuleInst273: set["idl_ActualParameter"] = None, idl_TemplateModuleInst275: set["idl_IDLComment"] = None):
        self.name = name
        self.idl_TemplateModuleInst = idl_TemplateModuleInst
        self.idl_TemplateModuleInst273 = idl_TemplateModuleInst273 if idl_TemplateModuleInst273 is not None else set()
        self.idl_TemplateModuleInst275 = idl_TemplateModuleInst275 if idl_TemplateModuleInst275 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_TemplateModuleInst(self):
        return self.__idl_TemplateModuleInst

    @idl_TemplateModuleInst.setter
    def idl_TemplateModuleInst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_TemplateModuleInst__idl_TemplateModuleInst", None)
        self.__idl_TemplateModuleInst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ScopedName271"):
                opp_val = getattr(old_value, "idl_ScopedName271", None)
                if opp_val == self:
                    setattr(old_value, "idl_ScopedName271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ScopedName271"):
                opp_val = getattr(value, "idl_ScopedName271", None)
                setattr(value, "idl_ScopedName271", self)

    @property
    def idl_TemplateModuleInst273(self):
        return self.__idl_TemplateModuleInst273

    @idl_TemplateModuleInst273.setter
    def idl_TemplateModuleInst273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_TemplateModuleInst__idl_TemplateModuleInst273", None)
        self.__idl_TemplateModuleInst273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_ActualParameter"):
                    opp_val = getattr(item, "idl_ActualParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_ActualParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_ActualParameter"):
                    opp_val = getattr(item, "idl_ActualParameter", None)
                    
                    setattr(item, "idl_ActualParameter", self)
                    

    @property
    def idl_TemplateModuleInst275(self):
        return self.__idl_TemplateModuleInst275

    @idl_TemplateModuleInst275.setter
    def idl_TemplateModuleInst275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_TemplateModuleInst__idl_TemplateModuleInst275", None)
        self.__idl_TemplateModuleInst275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment276"):
                    opp_val = getattr(item, "idl_IDLComment276", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment276"):
                    opp_val = getattr(item, "idl_IDLComment276", None)
                    
                    setattr(item, "idl_IDLComment276", self)
                    

class idl_NativeType(Definition, TemplateDefinition, FixedDefinition):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class idl_Interface_or_Forward_Decl(Definition):

    pass
class idl_PortTypeDecl(Definition, TemplateDefinition, FixedDefinition):

    def __init__(self, name: str, idl_PortTypeDecl: set["idl_IDLComment"] = None, idl_PortTypeDecl252: set["idl_PortExport"] = None):
        self.name = name
        self.idl_PortTypeDecl = idl_PortTypeDecl if idl_PortTypeDecl is not None else set()
        self.idl_PortTypeDecl252 = idl_PortTypeDecl252 if idl_PortTypeDecl252 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_PortTypeDecl(self):
        return self.__idl_PortTypeDecl

    @idl_PortTypeDecl.setter
    def idl_PortTypeDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_PortTypeDecl__idl_PortTypeDecl", None)
        self.__idl_PortTypeDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment250"):
                    opp_val = getattr(item, "idl_IDLComment250", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment250"):
                    opp_val = getattr(item, "idl_IDLComment250", None)
                    
                    setattr(item, "idl_IDLComment250", self)
                    

    @property
    def idl_PortTypeDecl252(self):
        return self.__idl_PortTypeDecl252

    @idl_PortTypeDecl252.setter
    def idl_PortTypeDecl252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_PortTypeDecl__idl_PortTypeDecl252", None)
        self.__idl_PortTypeDecl252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_PortExport"):
                    opp_val = getattr(item, "idl_PortExport", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_PortExport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_PortExport"):
                    opp_val = getattr(item, "idl_PortExport", None)
                    
                    setattr(item, "idl_PortExport", self)
                    

class idl_ConstDecl(Export, FixedDefinition, Definition, TemplateDefinition):

    def __init__(self, name: str, idl_ConstDecl: "idl_ConstType" = None, idl_ConstDecl131: "idl_ConstExp" = None, idl_ConstDecl134: set["idl_IDLComment"] = None):
        self.name = name
        self.idl_ConstDecl = idl_ConstDecl
        self.idl_ConstDecl131 = idl_ConstDecl131
        self.idl_ConstDecl134 = idl_ConstDecl134 if idl_ConstDecl134 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ConstDecl(self):
        return self.__idl_ConstDecl

    @idl_ConstDecl.setter
    def idl_ConstDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConstDecl__idl_ConstDecl", None)
        self.__idl_ConstDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConstType"):
                opp_val = getattr(old_value, "idl_ConstType", None)
                if opp_val == self:
                    setattr(old_value, "idl_ConstType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConstType"):
                opp_val = getattr(value, "idl_ConstType", None)
                setattr(value, "idl_ConstType", self)

    @property
    def idl_ConstDecl131(self):
        return self.__idl_ConstDecl131

    @idl_ConstDecl131.setter
    def idl_ConstDecl131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConstDecl__idl_ConstDecl131", None)
        self.__idl_ConstDecl131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_ConstExp132"):
                opp_val = getattr(old_value, "idl_ConstExp132", None)
                if opp_val == self:
                    setattr(old_value, "idl_ConstExp132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_ConstExp132"):
                opp_val = getattr(value, "idl_ConstExp132", None)
                setattr(value, "idl_ConstExp132", self)

    @property
    def idl_ConstDecl134(self):
        return self.__idl_ConstDecl134

    @idl_ConstDecl134.setter
    def idl_ConstDecl134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ConstDecl__idl_ConstDecl134", None)
        self.__idl_ConstDecl134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment135"):
                    opp_val = getattr(item, "idl_IDLComment135", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment135"):
                    opp_val = getattr(item, "idl_IDLComment135", None)
                    
                    setattr(item, "idl_IDLComment135", self)
                    

class idl_TypeDecl(Export, FixedDefinition, Definition, TemplateDefinition):

    pass
class idl_ExceptDecl(Export, Definition, TemplateDefinition, FixedDefinition):

    def __init__(self, name: str, idl_ExceptDecl: set["idl_IDLComment"] = None, idl_ExceptDecl68: set["idl_Member"] = None):
        self.name = name
        self.idl_ExceptDecl = idl_ExceptDecl if idl_ExceptDecl is not None else set()
        self.idl_ExceptDecl68 = idl_ExceptDecl68 if idl_ExceptDecl68 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idl_ExceptDecl68(self):
        return self.__idl_ExceptDecl68

    @idl_ExceptDecl68.setter
    def idl_ExceptDecl68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ExceptDecl__idl_ExceptDecl68", None)
        self.__idl_ExceptDecl68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_Member"):
                    opp_val = getattr(item, "idl_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_Member"):
                    opp_val = getattr(item, "idl_Member", None)
                    
                    setattr(item, "idl_Member", self)
                    

    @property
    def idl_ExceptDecl(self):
        return self.__idl_ExceptDecl

    @idl_ExceptDecl.setter
    def idl_ExceptDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_ExceptDecl__idl_ExceptDecl", None)
        self.__idl_ExceptDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "idl_IDLComment66"):
                    opp_val = getattr(item, "idl_IDLComment66", None)
                    
                    if opp_val == self:
                        setattr(item, "idl_IDLComment66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "idl_IDLComment66"):
                    opp_val = getattr(item, "idl_IDLComment66", None)
                    
                    setattr(item, "idl_IDLComment66", self)
                    

class idl_Preproc(Export, ComponentExport, Definition):

    pass
class idl_Definition:

    pass
class idl_Import_decl:

    def __init__(self, imported_scope: str, idl_Import_decl: "idl_Specification" = None):
        self.imported_scope = imported_scope
        self.idl_Import_decl = idl_Import_decl
        
    @property
    def imported_scope(self) -> str:
        return self.__imported_scope

    @imported_scope.setter
    def imported_scope(self, imported_scope: str):
        self.__imported_scope = imported_scope

    @property
    def idl_Import_decl(self):
        return self.__idl_Import_decl

    @idl_Import_decl.setter
    def idl_Import_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_idl_Import_decl__idl_Import_decl", None)
        self.__idl_Import_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "idl_Specification"):
                opp_val = getattr(old_value, "idl_Specification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "idl_Specification"):
                opp_val = getattr(value, "idl_Specification", None)
                if opp_val is None:
                    setattr(value, "idl_Specification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class idl_Specification:

    pass