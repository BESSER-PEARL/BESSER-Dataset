from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TraceEdge:

    pass
class ASPT_TraceNbEdge(TraceEdge):

    pass
class TraceProp:

    pass
class ASPT_TraceNbProp(TraceProp):

    pass
class TraceNode:

    pass
class ASPT_TraceNbNode(TraceNode):

    pass
class TraceElement:

    pass
class ASPT_TraceProp(TraceElement):

    def __init__(self, idp: str, idpx: str, value: str):
        self.idp = idp
        self.idpx = idpx
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def idp(self) -> str:
        return self.__idp

    @idp.setter
    def idp(self, idp: str):
        self.__idp = idp

    @property
    def idpx(self) -> str:
        return self.__idpx

    @idpx.setter
    def idpx(self, idpx: str):
        self.__idpx = idpx

class ASPT_TraceNode(TraceElement):

    pass
class ASPT_TraceEdge(TraceElement):

    def __init__(self, ids: str, idsx: str, idt: str, idtx: str):
        self.ids = ids
        self.idsx = idsx
        self.idt = idt
        self.idtx = idtx
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def idtx(self) -> str:
        return self.__idtx

    @idtx.setter
    def idtx(self, idtx: str):
        self.__idtx = idtx

    @property
    def idsx(self) -> str:
        return self.__idsx

    @idsx.setter
    def idsx(self, idsx: str):
        self.__idsx = idsx

    @property
    def idt(self) -> str:
        return self.__idt

    @idt.setter
    def idt(self, idt: str):
        self.__idt = idt

class ASPT_TraceElement:

    def __init__(self, metamodel: str, id: str, idx: str, type: str, ASPT_TraceElement: "ASPT_TraceModel" = None):
        self.metamodel = metamodel
        self.id = id
        self.idx = idx
        self.type = type
        self.ASPT_TraceElement = ASPT_TraceElement
        
    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def idx(self) -> str:
        return self.__idx

    @idx.setter
    def idx(self, idx: str):
        self.__idx = idx

    @property
    def ASPT_TraceElement(self):
        return self.__ASPT_TraceElement

    @ASPT_TraceElement.setter
    def ASPT_TraceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASPT_TraceElement__ASPT_TraceElement", None)
        self.__ASPT_TraceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ASPT_TraceModel2"):
                opp_val = getattr(old_value, "ASPT_TraceModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ASPT_TraceModel2"):
                opp_val = getattr(value, "ASPT_TraceModel2", None)
                if opp_val is None:
                    setattr(value, "ASPT_TraceModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ASPT_TraceLink(TraceElement):

    def __init__(self, relation: str, idref: str, idrefx: str, ASPT_TraceLink: "ASPT_TraceModel" = None):
        self.relation = relation
        self.idref = idref
        self.idrefx = idrefx
        self.ASPT_TraceLink = ASPT_TraceLink
        
    @property
    def idref(self) -> str:
        return self.__idref

    @idref.setter
    def idref(self, idref: str):
        self.__idref = idref

    @property
    def idrefx(self) -> str:
        return self.__idrefx

    @idrefx.setter
    def idrefx(self, idrefx: str):
        self.__idrefx = idrefx

    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def ASPT_TraceLink(self):
        return self.__ASPT_TraceLink

    @ASPT_TraceLink.setter
    def ASPT_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASPT_TraceLink__ASPT_TraceLink", None)
        self.__ASPT_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ASPT_TraceModel"):
                opp_val = getattr(old_value, "ASPT_TraceModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ASPT_TraceModel"):
                opp_val = getattr(value, "ASPT_TraceModel", None)
                if opp_val is None:
                    setattr(value, "ASPT_TraceModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ASPT_TraceModel:

    def __init__(self, ID: str, MMS: str, ASPT_TraceModel: set["ASPT_TraceLink"] = None, ASPT_TraceModel2: set["ASPT_TraceElement"] = None):
        self.ID = ID
        self.MMS = MMS
        self.ASPT_TraceModel = ASPT_TraceModel if ASPT_TraceModel is not None else set()
        self.ASPT_TraceModel2 = ASPT_TraceModel2 if ASPT_TraceModel2 is not None else set()
        
    @property
    def MMS(self) -> str:
        return self.__MMS

    @MMS.setter
    def MMS(self, MMS: str):
        self.__MMS = MMS

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ASPT_TraceModel2(self):
        return self.__ASPT_TraceModel2

    @ASPT_TraceModel2.setter
    def ASPT_TraceModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASPT_TraceModel__ASPT_TraceModel2", None)
        self.__ASPT_TraceModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ASPT_TraceElement"):
                    opp_val = getattr(item, "ASPT_TraceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ASPT_TraceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASPT_TraceElement"):
                    opp_val = getattr(item, "ASPT_TraceElement", None)
                    
                    setattr(item, "ASPT_TraceElement", self)
                    

    @property
    def ASPT_TraceModel(self):
        return self.__ASPT_TraceModel

    @ASPT_TraceModel.setter
    def ASPT_TraceModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASPT_TraceModel__ASPT_TraceModel", None)
        self.__ASPT_TraceModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ASPT_TraceLink"):
                    opp_val = getattr(item, "ASPT_TraceLink", None)
                    
                    if opp_val == self:
                        setattr(item, "ASPT_TraceLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASPT_TraceLink"):
                    opp_val = getattr(item, "ASPT_TraceLink", None)
                    
                    setattr(item, "ASPT_TraceLink", self)
                    
