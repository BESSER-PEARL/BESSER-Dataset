from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Variable:

    pass
class Type:

    pass
class dataflow_TypeUndefined(Type):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class dataflow_TypeBoolean(Type):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class dataflow_TypeDouble(Type):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class dataflow_TypeString(Type):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class dataflow_TypeInt(Type):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class dataflow_TypeList(Type):

    def __init__(self, elements: int, dataflow_TypeList: "dataflow_Type" = None):
        self.elements = elements
        self.dataflow_TypeList = dataflow_TypeList
        
    @property
    def elements(self) -> int:
        return self.__elements

    @elements.setter
    def elements(self, elements: int):
        self.__elements = elements

    @property
    def dataflow_TypeList(self):
        return self.__dataflow_TypeList

    @dataflow_TypeList.setter
    def dataflow_TypeList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_TypeList__dataflow_TypeList", None)
        self.__dataflow_TypeList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Type94"):
                opp_val = getattr(old_value, "dataflow_Type94", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Type94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Type94"):
                opp_val = getattr(value, "dataflow_Type94", None)
                setattr(value, "dataflow_Type94", self)

class dataflow_TypeUint(Type):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class dataflow_Type(ABC):

    def __init__(self, etype: str, bits: int, dataflow_Type: "dataflow_Variable" = None, dataflow_Type86: "dataflow_Buffer" = None, dataflow_Type94: "dataflow_TypeList" = None):
        self.etype = etype
        self.bits = bits
        self.dataflow_Type = dataflow_Type
        self.dataflow_Type86 = dataflow_Type86
        self.dataflow_Type94 = dataflow_Type94
        
    @property
    def bits(self) -> int:
        return self.__bits

    @bits.setter
    def bits(self, bits: int):
        self.__bits = bits

    @property
    def etype(self) -> str:
        return self.__etype

    @etype.setter
    def etype(self, etype: str):
        self.__etype = etype

    @property
    def dataflow_Type86(self):
        return self.__dataflow_Type86

    @dataflow_Type86.setter
    def dataflow_Type86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Type__dataflow_Type86", None)
        self.__dataflow_Type86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Buffer85"):
                opp_val = getattr(old_value, "dataflow_Buffer85", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Buffer85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Buffer85"):
                opp_val = getattr(value, "dataflow_Buffer85", None)
                setattr(value, "dataflow_Buffer85", self)

    @property
    def dataflow_Type94(self):
        return self.__dataflow_Type94

    @dataflow_Type94.setter
    def dataflow_Type94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Type__dataflow_Type94", None)
        self.__dataflow_Type94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_TypeList"):
                opp_val = getattr(old_value, "dataflow_TypeList", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_TypeList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_TypeList"):
                opp_val = getattr(value, "dataflow_TypeList", None)
                setattr(value, "dataflow_TypeList", self)

    @property
    def dataflow_Type(self):
        return self.__dataflow_Type

    @dataflow_Type.setter
    def dataflow_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Type__dataflow_Type", None)
        self.__dataflow_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Variable67"):
                opp_val = getattr(old_value, "dataflow_Variable67", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Variable67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Variable67"):
                opp_val = getattr(value, "dataflow_Variable67", None)
                setattr(value, "dataflow_Variable67", self)

class dataflow_Version:

    pass
class dataflow_SharedVariable(Variable):

    def __init__(self, tag: str, dataflow_SharedVariable: "dataflow_Network" = None):
        self.tag = tag
        self.dataflow_SharedVariable = dataflow_SharedVariable
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def dataflow_SharedVariable(self):
        return self.__dataflow_SharedVariable

    @dataflow_SharedVariable.setter
    def dataflow_SharedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_SharedVariable__dataflow_SharedVariable", None)
        self.__dataflow_SharedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network11"):
                opp_val = getattr(old_value, "dataflow_Network11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network11"):
                opp_val = getattr(value, "dataflow_Network11", None)
                if opp_val is None:
                    setattr(value, "dataflow_Network11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Attributable:

    pass
class dataflow_Network(Attributable):

    def __init__(self, name: str, sourceFile: str, project: str, dataflow_Network: set["dataflow_Actor"] = None, dataflow_Network2: set["dataflow_ActorClass"] = None, dataflow_Network4: set["dataflow_Buffer"] = None, dataflow_Network6: set["dataflow_Port"] = None, dataflow_Network8: set["dataflow_Port"] = None, dataflow_Network11: set["dataflow_SharedVariable"] = None, dataflow_Network13: "dataflow_Version" = None, dataflow_Network36: "dataflow_Actor" = None, dataflow_Network20: "dataflow_ActorClass" = None, dataflow_Network89: "dataflow_Buffer" = None):
        self.name = name
        self.sourceFile = sourceFile
        self.project = project
        self.dataflow_Network = dataflow_Network if dataflow_Network is not None else set()
        self.dataflow_Network2 = dataflow_Network2 if dataflow_Network2 is not None else set()
        self.dataflow_Network4 = dataflow_Network4 if dataflow_Network4 is not None else set()
        self.dataflow_Network6 = dataflow_Network6 if dataflow_Network6 is not None else set()
        self.dataflow_Network8 = dataflow_Network8 if dataflow_Network8 is not None else set()
        self.dataflow_Network11 = dataflow_Network11 if dataflow_Network11 is not None else set()
        self.dataflow_Network13 = dataflow_Network13
        self.dataflow_Network36 = dataflow_Network36
        self.dataflow_Network20 = dataflow_Network20
        self.dataflow_Network89 = dataflow_Network89
        
    @property
    def sourceFile(self) -> str:
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: str):
        self.__sourceFile = sourceFile

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def dataflow_Network8(self):
        return self.__dataflow_Network8

    @dataflow_Network8.setter
    def dataflow_Network8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network8", None)
        self.__dataflow_Network8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Port9"):
                    opp_val = getattr(item, "dataflow_Port9", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Port9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Port9"):
                    opp_val = getattr(item, "dataflow_Port9", None)
                    
                    setattr(item, "dataflow_Port9", self)
                    

    @property
    def dataflow_Network20(self):
        return self.__dataflow_Network20

    @dataflow_Network20.setter
    def dataflow_Network20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network20", None)
        self.__dataflow_Network20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_ActorClass19"):
                opp_val = getattr(old_value, "dataflow_ActorClass19", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_ActorClass19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_ActorClass19"):
                opp_val = getattr(value, "dataflow_ActorClass19", None)
                setattr(value, "dataflow_ActorClass19", self)

    @property
    def dataflow_Network11(self):
        return self.__dataflow_Network11

    @dataflow_Network11.setter
    def dataflow_Network11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network11", None)
        self.__dataflow_Network11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_SharedVariable"):
                    opp_val = getattr(item, "dataflow_SharedVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_SharedVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_SharedVariable"):
                    opp_val = getattr(item, "dataflow_SharedVariable", None)
                    
                    setattr(item, "dataflow_SharedVariable", self)
                    

    @property
    def dataflow_Network89(self):
        return self.__dataflow_Network89

    @dataflow_Network89.setter
    def dataflow_Network89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network89", None)
        self.__dataflow_Network89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Buffer88"):
                opp_val = getattr(old_value, "dataflow_Buffer88", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Buffer88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Buffer88"):
                opp_val = getattr(value, "dataflow_Buffer88", None)
                setattr(value, "dataflow_Buffer88", self)

    @property
    def dataflow_Network13(self):
        return self.__dataflow_Network13

    @dataflow_Network13.setter
    def dataflow_Network13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network13", None)
        self.__dataflow_Network13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Version"):
                opp_val = getattr(old_value, "dataflow_Version", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Version", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Version"):
                opp_val = getattr(value, "dataflow_Version", None)
                setattr(value, "dataflow_Version", self)

    @property
    def dataflow_Network36(self):
        return self.__dataflow_Network36

    @dataflow_Network36.setter
    def dataflow_Network36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network36", None)
        self.__dataflow_Network36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor35"):
                opp_val = getattr(old_value, "dataflow_Actor35", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Actor35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor35"):
                opp_val = getattr(value, "dataflow_Actor35", None)
                setattr(value, "dataflow_Actor35", self)

    @property
    def dataflow_Network(self):
        return self.__dataflow_Network

    @dataflow_Network.setter
    def dataflow_Network(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network", None)
        self.__dataflow_Network = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Actor"):
                    opp_val = getattr(item, "dataflow_Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Actor"):
                    opp_val = getattr(item, "dataflow_Actor", None)
                    
                    setattr(item, "dataflow_Actor", self)
                    

    @property
    def dataflow_Network6(self):
        return self.__dataflow_Network6

    @dataflow_Network6.setter
    def dataflow_Network6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network6", None)
        self.__dataflow_Network6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Port"):
                    opp_val = getattr(item, "dataflow_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Port"):
                    opp_val = getattr(item, "dataflow_Port", None)
                    
                    setattr(item, "dataflow_Port", self)
                    

    @property
    def dataflow_Network4(self):
        return self.__dataflow_Network4

    @dataflow_Network4.setter
    def dataflow_Network4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network4", None)
        self.__dataflow_Network4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Buffer"):
                    opp_val = getattr(item, "dataflow_Buffer", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Buffer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Buffer"):
                    opp_val = getattr(item, "dataflow_Buffer", None)
                    
                    setattr(item, "dataflow_Buffer", self)
                    

    @property
    def dataflow_Network2(self):
        return self.__dataflow_Network2

    @dataflow_Network2.setter
    def dataflow_Network2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Network__dataflow_Network2", None)
        self.__dataflow_Network2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_ActorClass"):
                    opp_val = getattr(item, "dataflow_ActorClass", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_ActorClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_ActorClass"):
                    opp_val = getattr(item, "dataflow_ActorClass", None)
                    
                    setattr(item, "dataflow_ActorClass", self)
                    

    def getOutputPort(self, name: str) -> str:
        # TODO: Implement getOutputPort method
        pass

    def getInputPort(self, name: str) -> str:
        # TODO: Implement getInputPort method
        pass

    def getActor(self, name: str) -> str:
        # TODO: Implement getActor method
        pass

    def getActorClass(self, name: str) -> str:
        # TODO: Implement getActorClass method
        pass

    def getSharedVariables(self, tag: str) -> str:
        # TODO: Implement getSharedVariables method
        pass

class dataflow_Variable(Attributable):

    def __init__(self, name: str, shared: bool, dataflow_Variable: "dataflow_Actor" = None, dataflow_Variable62: "dataflow_Procedure" = None, dataflow_Variable67: "dataflow_Type" = None, dataflow_Variable69: "dataflow_Actor" = None):
        self.name = name
        self.shared = shared
        self.dataflow_Variable = dataflow_Variable
        self.dataflow_Variable62 = dataflow_Variable62
        self.dataflow_Variable67 = dataflow_Variable67
        self.dataflow_Variable69 = dataflow_Variable69
        
    @property
    def shared(self) -> bool:
        return self.__shared

    @shared.setter
    def shared(self, shared: bool):
        self.__shared = shared

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataflow_Variable69(self):
        return self.__dataflow_Variable69

    @dataflow_Variable69.setter
    def dataflow_Variable69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Variable__dataflow_Variable69", None)
        self.__dataflow_Variable69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor70"):
                opp_val = getattr(old_value, "dataflow_Actor70", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Actor70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor70"):
                opp_val = getattr(value, "dataflow_Actor70", None)
                setattr(value, "dataflow_Actor70", self)

    @property
    def dataflow_Variable(self):
        return self.__dataflow_Variable

    @dataflow_Variable.setter
    def dataflow_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Variable__dataflow_Variable", None)
        self.__dataflow_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor28"):
                opp_val = getattr(old_value, "dataflow_Actor28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor28"):
                opp_val = getattr(value, "dataflow_Actor28", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Variable62(self):
        return self.__dataflow_Variable62

    @dataflow_Variable62.setter
    def dataflow_Variable62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Variable__dataflow_Variable62", None)
        self.__dataflow_Variable62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Procedure61"):
                opp_val = getattr(old_value, "dataflow_Procedure61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Procedure61"):
                opp_val = getattr(value, "dataflow_Procedure61", None)
                if opp_val is None:
                    setattr(value, "dataflow_Procedure61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Variable67(self):
        return self.__dataflow_Variable67

    @dataflow_Variable67.setter
    def dataflow_Variable67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Variable__dataflow_Variable67", None)
        self.__dataflow_Variable67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Type"):
                opp_val = getattr(old_value, "dataflow_Type", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Type"):
                opp_val = getattr(value, "dataflow_Type", None)
                setattr(value, "dataflow_Type", self)

class dataflow_Action(Attributable):

    def __init__(self, name: str, dataflow_Action: "dataflow_Actor" = None, readers: set["dataflow_Port"] = None, writers: set["dataflow_Port"] = None, dataflow_Action56: set["dataflow_Guard"] = None, dataflow_Action58: "dataflow_Actor" = None, dataflow_Action92: "dataflow_Guard" = None, Action: "dataflow_Port" = None, Action73: "dataflow_Port" = None):
        self.name = name
        self.dataflow_Action = dataflow_Action
        self.readers = readers if readers is not None else set()
        self.writers = writers if writers is not None else set()
        self.dataflow_Action56 = dataflow_Action56 if dataflow_Action56 is not None else set()
        self.dataflow_Action58 = dataflow_Action58
        self.dataflow_Action92 = dataflow_Action92
        self.Action = Action
        self.Action73 = Action73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataflow_Action92(self):
        return self.__dataflow_Action92

    @dataflow_Action92.setter
    def dataflow_Action92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__dataflow_Action92", None)
        self.__dataflow_Action92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Guard91"):
                opp_val = getattr(old_value, "dataflow_Guard91", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Guard91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Guard91"):
                opp_val = getattr(value, "dataflow_Guard91", None)
                setattr(value, "dataflow_Guard91", self)

    @property
    def dataflow_Action56(self):
        return self.__dataflow_Action56

    @dataflow_Action56.setter
    def dataflow_Action56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__dataflow_Action56", None)
        self.__dataflow_Action56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Guard"):
                    opp_val = getattr(item, "dataflow_Guard", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Guard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Guard"):
                    opp_val = getattr(item, "dataflow_Guard", None)
                    
                    setattr(item, "dataflow_Guard", self)
                    

    @property
    def dataflow_Action58(self):
        return self.__dataflow_Action58

    @dataflow_Action58.setter
    def dataflow_Action58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__dataflow_Action58", None)
        self.__dataflow_Action58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor59"):
                opp_val = getattr(old_value, "dataflow_Actor59", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Actor59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor59"):
                opp_val = getattr(value, "dataflow_Actor59", None)
                setattr(value, "dataflow_Actor59", self)

    @property
    def Action73(self):
        return self.__Action73

    @Action73.setter
    def Action73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__Action73", None)
        self.__Action73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputPorts"):
                opp_val = getattr(old_value, "inputPorts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputPorts"):
                opp_val = getattr(value, "inputPorts", None)
                if opp_val is None:
                    setattr(value, "inputPorts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Action(self):
        return self.__dataflow_Action

    @dataflow_Action.setter
    def dataflow_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__dataflow_Action", None)
        self.__dataflow_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor31"):
                opp_val = getattr(old_value, "dataflow_Actor31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor31"):
                opp_val = getattr(value, "dataflow_Actor31", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def writers(self):
        return self.__writers

    @writers.setter
    def writers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__writers", None)
        self.__writers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Port54"):
                    opp_val = getattr(item, "Port54", None)
                    
                    if opp_val == self:
                        setattr(item, "Port54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Port54"):
                    opp_val = getattr(item, "Port54", None)
                    
                    setattr(item, "Port54", self)
                    

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputPorts"):
                opp_val = getattr(old_value, "outputPorts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputPorts"):
                opp_val = getattr(value, "outputPorts", None)
                if opp_val is None:
                    setattr(value, "outputPorts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def readers(self):
        return self.__readers

    @readers.setter
    def readers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Action__readers", None)
        self.__readers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    if opp_val == self:
                        setattr(item, "Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    setattr(item, "Port", self)
                    

    def getGuard(self, tag: str) -> str:
        # TODO: Implement getGuard method
        pass

class dataflow_Buffer(Attributable):

    pass
class dataflow_Actor(Attributable):

    def __init__(self, name: str, dataflow_Actor: "dataflow_Network" = None, dataflow_Actor22: set["dataflow_Port"] = None, dataflow_Actor25: set["dataflow_Port"] = None, dataflow_Actor28: set["dataflow_Variable"] = None, actors: "dataflow_ActorClass" = None, dataflow_Actor31: set["dataflow_Action"] = None, dataflow_Actor33: set["dataflow_Procedure"] = None, dataflow_Actor35: "dataflow_Network" = None, dataflow_Actor38: set["dataflow_Buffer"] = None, Actor: "dataflow_ActorClass" = None, dataflow_Actor51: "dataflow_Actor" = None, dataflow_Actor49: set["dataflow_Actor"] = None, dataflow_Actor59: "dataflow_Action" = None, dataflow_Actor65: "dataflow_Procedure" = None, dataflow_Actor70: "dataflow_Variable" = None, dataflow_Actor41: set["dataflow_Buffer"] = None, dataflow_Actor44: set["dataflow_Buffer"] = None, dataflow_Actor48: "dataflow_Actor" = None, dataflow_Actor46: set["dataflow_Actor"] = None, dataflow_Actor79: "dataflow_Port" = None):
        self.name = name
        self.dataflow_Actor = dataflow_Actor
        self.dataflow_Actor22 = dataflow_Actor22 if dataflow_Actor22 is not None else set()
        self.dataflow_Actor25 = dataflow_Actor25 if dataflow_Actor25 is not None else set()
        self.dataflow_Actor28 = dataflow_Actor28 if dataflow_Actor28 is not None else set()
        self.actors = actors
        self.dataflow_Actor31 = dataflow_Actor31 if dataflow_Actor31 is not None else set()
        self.dataflow_Actor33 = dataflow_Actor33 if dataflow_Actor33 is not None else set()
        self.dataflow_Actor35 = dataflow_Actor35
        self.dataflow_Actor38 = dataflow_Actor38 if dataflow_Actor38 is not None else set()
        self.Actor = Actor
        self.dataflow_Actor51 = dataflow_Actor51
        self.dataflow_Actor49 = dataflow_Actor49 if dataflow_Actor49 is not None else set()
        self.dataflow_Actor59 = dataflow_Actor59
        self.dataflow_Actor65 = dataflow_Actor65
        self.dataflow_Actor70 = dataflow_Actor70
        self.dataflow_Actor41 = dataflow_Actor41 if dataflow_Actor41 is not None else set()
        self.dataflow_Actor44 = dataflow_Actor44 if dataflow_Actor44 is not None else set()
        self.dataflow_Actor48 = dataflow_Actor48
        self.dataflow_Actor46 = dataflow_Actor46 if dataflow_Actor46 is not None else set()
        self.dataflow_Actor79 = dataflow_Actor79
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataflow_Actor46(self):
        return self.__dataflow_Actor46

    @dataflow_Actor46.setter
    def dataflow_Actor46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor46", None)
        self.__dataflow_Actor46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Actor48"):
                    opp_val = getattr(item, "dataflow_Actor48", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Actor48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Actor48"):
                    opp_val = getattr(item, "dataflow_Actor48", None)
                    
                    setattr(item, "dataflow_Actor48", self)
                    

    @property
    def dataflow_Actor49(self):
        return self.__dataflow_Actor49

    @dataflow_Actor49.setter
    def dataflow_Actor49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor49", None)
        self.__dataflow_Actor49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Actor51"):
                    opp_val = getattr(item, "dataflow_Actor51", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Actor51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Actor51"):
                    opp_val = getattr(item, "dataflow_Actor51", None)
                    
                    setattr(item, "dataflow_Actor51", self)
                    

    @property
    def dataflow_Actor65(self):
        return self.__dataflow_Actor65

    @dataflow_Actor65.setter
    def dataflow_Actor65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor65", None)
        self.__dataflow_Actor65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Procedure64"):
                opp_val = getattr(old_value, "dataflow_Procedure64", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Procedure64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Procedure64"):
                opp_val = getattr(value, "dataflow_Procedure64", None)
                setattr(value, "dataflow_Procedure64", self)

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__actors", None)
        self.__actors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActorClass"):
                opp_val = getattr(old_value, "ActorClass", None)
                if opp_val == self:
                    setattr(old_value, "ActorClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActorClass"):
                opp_val = getattr(value, "ActorClass", None)
                setattr(value, "ActorClass", self)

    @property
    def Actor(self):
        return self.__Actor

    @Actor.setter
    def Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__Actor", None)
        self.__Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actorClass"):
                opp_val = getattr(old_value, "actorClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actorClass"):
                opp_val = getattr(value, "actorClass", None)
                if opp_val is None:
                    setattr(value, "actorClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Actor48(self):
        return self.__dataflow_Actor48

    @dataflow_Actor48.setter
    def dataflow_Actor48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor48", None)
        self.__dataflow_Actor48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor46"):
                opp_val = getattr(old_value, "dataflow_Actor46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor46"):
                opp_val = getattr(value, "dataflow_Actor46", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Actor35(self):
        return self.__dataflow_Actor35

    @dataflow_Actor35.setter
    def dataflow_Actor35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor35", None)
        self.__dataflow_Actor35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network36"):
                opp_val = getattr(old_value, "dataflow_Network36", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Network36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network36"):
                opp_val = getattr(value, "dataflow_Network36", None)
                setattr(value, "dataflow_Network36", self)

    @property
    def dataflow_Actor(self):
        return self.__dataflow_Actor

    @dataflow_Actor.setter
    def dataflow_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor", None)
        self.__dataflow_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network"):
                opp_val = getattr(old_value, "dataflow_Network", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network"):
                opp_val = getattr(value, "dataflow_Network", None)
                if opp_val is None:
                    setattr(value, "dataflow_Network", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Actor38(self):
        return self.__dataflow_Actor38

    @dataflow_Actor38.setter
    def dataflow_Actor38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor38", None)
        self.__dataflow_Actor38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Buffer39"):
                    opp_val = getattr(item, "dataflow_Buffer39", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Buffer39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Buffer39"):
                    opp_val = getattr(item, "dataflow_Buffer39", None)
                    
                    setattr(item, "dataflow_Buffer39", self)
                    

    @property
    def dataflow_Actor70(self):
        return self.__dataflow_Actor70

    @dataflow_Actor70.setter
    def dataflow_Actor70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor70", None)
        self.__dataflow_Actor70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Variable69"):
                opp_val = getattr(old_value, "dataflow_Variable69", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Variable69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Variable69"):
                opp_val = getattr(value, "dataflow_Variable69", None)
                setattr(value, "dataflow_Variable69", self)

    @property
    def dataflow_Actor28(self):
        return self.__dataflow_Actor28

    @dataflow_Actor28.setter
    def dataflow_Actor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor28", None)
        self.__dataflow_Actor28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Variable"):
                    opp_val = getattr(item, "dataflow_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Variable"):
                    opp_val = getattr(item, "dataflow_Variable", None)
                    
                    setattr(item, "dataflow_Variable", self)
                    

    @property
    def dataflow_Actor25(self):
        return self.__dataflow_Actor25

    @dataflow_Actor25.setter
    def dataflow_Actor25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor25", None)
        self.__dataflow_Actor25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Port26"):
                    opp_val = getattr(item, "dataflow_Port26", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Port26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Port26"):
                    opp_val = getattr(item, "dataflow_Port26", None)
                    
                    setattr(item, "dataflow_Port26", self)
                    

    @property
    def dataflow_Actor33(self):
        return self.__dataflow_Actor33

    @dataflow_Actor33.setter
    def dataflow_Actor33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor33", None)
        self.__dataflow_Actor33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Procedure"):
                    opp_val = getattr(item, "dataflow_Procedure", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Procedure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Procedure"):
                    opp_val = getattr(item, "dataflow_Procedure", None)
                    
                    setattr(item, "dataflow_Procedure", self)
                    

    @property
    def dataflow_Actor41(self):
        return self.__dataflow_Actor41

    @dataflow_Actor41.setter
    def dataflow_Actor41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor41", None)
        self.__dataflow_Actor41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Buffer42"):
                    opp_val = getattr(item, "dataflow_Buffer42", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Buffer42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Buffer42"):
                    opp_val = getattr(item, "dataflow_Buffer42", None)
                    
                    setattr(item, "dataflow_Buffer42", self)
                    

    @property
    def dataflow_Actor79(self):
        return self.__dataflow_Actor79

    @dataflow_Actor79.setter
    def dataflow_Actor79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor79", None)
        self.__dataflow_Actor79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Port78"):
                opp_val = getattr(old_value, "dataflow_Port78", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Port78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Port78"):
                opp_val = getattr(value, "dataflow_Port78", None)
                setattr(value, "dataflow_Port78", self)

    @property
    def dataflow_Actor31(self):
        return self.__dataflow_Actor31

    @dataflow_Actor31.setter
    def dataflow_Actor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor31", None)
        self.__dataflow_Actor31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Action"):
                    opp_val = getattr(item, "dataflow_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Action"):
                    opp_val = getattr(item, "dataflow_Action", None)
                    
                    setattr(item, "dataflow_Action", self)
                    

    @property
    def dataflow_Actor44(self):
        return self.__dataflow_Actor44

    @dataflow_Actor44.setter
    def dataflow_Actor44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor44", None)
        self.__dataflow_Actor44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Buffer45"):
                    opp_val = getattr(item, "dataflow_Buffer45", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Buffer45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Buffer45"):
                    opp_val = getattr(item, "dataflow_Buffer45", None)
                    
                    setattr(item, "dataflow_Buffer45", self)
                    

    @property
    def dataflow_Actor59(self):
        return self.__dataflow_Actor59

    @dataflow_Actor59.setter
    def dataflow_Actor59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor59", None)
        self.__dataflow_Actor59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Action58"):
                opp_val = getattr(old_value, "dataflow_Action58", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Action58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Action58"):
                opp_val = getattr(value, "dataflow_Action58", None)
                setattr(value, "dataflow_Action58", self)

    @property
    def dataflow_Actor51(self):
        return self.__dataflow_Actor51

    @dataflow_Actor51.setter
    def dataflow_Actor51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor51", None)
        self.__dataflow_Actor51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor49"):
                opp_val = getattr(old_value, "dataflow_Actor49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor49"):
                opp_val = getattr(value, "dataflow_Actor49", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Actor22(self):
        return self.__dataflow_Actor22

    @dataflow_Actor22.setter
    def dataflow_Actor22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Actor__dataflow_Actor22", None)
        self.__dataflow_Actor22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Port23"):
                    opp_val = getattr(item, "dataflow_Port23", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Port23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Port23"):
                    opp_val = getattr(item, "dataflow_Port23", None)
                    
                    setattr(item, "dataflow_Port23", self)
                    

    def getProcedure(self, name: str) -> str:
        # TODO: Implement getProcedure method
        pass

    def getVariable(self, name: str) -> str:
        # TODO: Implement getVariable method
        pass

    def getInputPort(self, name: str) -> str:
        # TODO: Implement getInputPort method
        pass

    def getSharedVariable(self, tag: str) -> str:
        # TODO: Implement getSharedVariable method
        pass

    def getAction(self, name: str) -> str:
        # TODO: Implement getAction method
        pass

    def getOutputPort(self, name: str) -> str:
        # TODO: Implement getOutputPort method
        pass

class dataflow_Procedure(Attributable):

    def __init__(self, name: str, dataflow_Procedure: "dataflow_Actor" = None, dataflow_Procedure61: set["dataflow_Variable"] = None, dataflow_Procedure64: "dataflow_Actor" = None):
        self.name = name
        self.dataflow_Procedure = dataflow_Procedure
        self.dataflow_Procedure61 = dataflow_Procedure61 if dataflow_Procedure61 is not None else set()
        self.dataflow_Procedure64 = dataflow_Procedure64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataflow_Procedure(self):
        return self.__dataflow_Procedure

    @dataflow_Procedure.setter
    def dataflow_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Procedure__dataflow_Procedure", None)
        self.__dataflow_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor33"):
                opp_val = getattr(old_value, "dataflow_Actor33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor33"):
                opp_val = getattr(value, "dataflow_Actor33", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Procedure61(self):
        return self.__dataflow_Procedure61

    @dataflow_Procedure61.setter
    def dataflow_Procedure61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Procedure__dataflow_Procedure61", None)
        self.__dataflow_Procedure61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflow_Variable62"):
                    opp_val = getattr(item, "dataflow_Variable62", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflow_Variable62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflow_Variable62"):
                    opp_val = getattr(item, "dataflow_Variable62", None)
                    
                    setattr(item, "dataflow_Variable62", self)
                    

    @property
    def dataflow_Procedure64(self):
        return self.__dataflow_Procedure64

    @dataflow_Procedure64.setter
    def dataflow_Procedure64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Procedure__dataflow_Procedure64", None)
        self.__dataflow_Procedure64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor65"):
                opp_val = getattr(old_value, "dataflow_Actor65", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Actor65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor65"):
                opp_val = getattr(value, "dataflow_Actor65", None)
                setattr(value, "dataflow_Actor65", self)

class dataflow_Guard(Attributable):

    def __init__(self, tag: str, dataflow_Guard: "dataflow_Action" = None, dataflow_Guard91: "dataflow_Action" = None):
        self.tag = tag
        self.dataflow_Guard = dataflow_Guard
        self.dataflow_Guard91 = dataflow_Guard91
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def dataflow_Guard(self):
        return self.__dataflow_Guard

    @dataflow_Guard.setter
    def dataflow_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Guard__dataflow_Guard", None)
        self.__dataflow_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Action56"):
                opp_val = getattr(old_value, "dataflow_Action56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Action56"):
                opp_val = getattr(value, "dataflow_Action56", None)
                if opp_val is None:
                    setattr(value, "dataflow_Action56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Guard91(self):
        return self.__dataflow_Guard91

    @dataflow_Guard91.setter
    def dataflow_Guard91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Guard__dataflow_Guard91", None)
        self.__dataflow_Guard91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Action92"):
                opp_val = getattr(old_value, "dataflow_Action92", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Action92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Action92"):
                opp_val = getattr(value, "dataflow_Action92", None)
                setattr(value, "dataflow_Action92", self)

class dataflow_ActorClass(Attributable):

    def __init__(self, sourceCode: str, name: str, sourceFile: str, nameSpace: str, dataflow_ActorClass: "dataflow_Network" = None, dataflow_ActorClass19: "dataflow_Network" = None, ActorClass: "dataflow_Actor" = None, actorClass: set["dataflow_Actor"] = None, dataflow_ActorClass16: "dataflow_Version" = None):
        self.sourceCode = sourceCode
        self.name = name
        self.sourceFile = sourceFile
        self.nameSpace = nameSpace
        self.dataflow_ActorClass = dataflow_ActorClass
        self.dataflow_ActorClass19 = dataflow_ActorClass19
        self.ActorClass = ActorClass
        self.actorClass = actorClass if actorClass is not None else set()
        self.dataflow_ActorClass16 = dataflow_ActorClass16
        
    @property
    def nameSpace(self) -> str:
        return self.__nameSpace

    @nameSpace.setter
    def nameSpace(self, nameSpace: str):
        self.__nameSpace = nameSpace

    @property
    def sourceFile(self) -> str:
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: str):
        self.__sourceFile = sourceFile

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sourceCode(self) -> str:
        return self.__sourceCode

    @sourceCode.setter
    def sourceCode(self, sourceCode: str):
        self.__sourceCode = sourceCode

    @property
    def dataflow_ActorClass19(self):
        return self.__dataflow_ActorClass19

    @dataflow_ActorClass19.setter
    def dataflow_ActorClass19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_ActorClass__dataflow_ActorClass19", None)
        self.__dataflow_ActorClass19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network20"):
                opp_val = getattr(old_value, "dataflow_Network20", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Network20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network20"):
                opp_val = getattr(value, "dataflow_Network20", None)
                setattr(value, "dataflow_Network20", self)

    @property
    def dataflow_ActorClass(self):
        return self.__dataflow_ActorClass

    @dataflow_ActorClass.setter
    def dataflow_ActorClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_ActorClass__dataflow_ActorClass", None)
        self.__dataflow_ActorClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network2"):
                opp_val = getattr(old_value, "dataflow_Network2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network2"):
                opp_val = getattr(value, "dataflow_Network2", None)
                if opp_val is None:
                    setattr(value, "dataflow_Network2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def actorClass(self):
        return self.__actorClass

    @actorClass.setter
    def actorClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_ActorClass__actorClass", None)
        self.__actorClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    setattr(item, "Actor", self)
                    

    @property
    def ActorClass(self):
        return self.__ActorClass

    @ActorClass.setter
    def ActorClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_ActorClass__ActorClass", None)
        self.__ActorClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actors"):
                opp_val = getattr(old_value, "actors", None)
                if opp_val == self:
                    setattr(old_value, "actors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actors"):
                opp_val = getattr(value, "actors", None)
                setattr(value, "actors", self)

    @property
    def dataflow_ActorClass16(self):
        return self.__dataflow_ActorClass16

    @dataflow_ActorClass16.setter
    def dataflow_ActorClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_ActorClass__dataflow_ActorClass16", None)
        self.__dataflow_ActorClass16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Version17"):
                opp_val = getattr(old_value, "dataflow_Version17", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Version17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Version17"):
                opp_val = getattr(value, "dataflow_Version17", None)
                setattr(value, "dataflow_Version17", self)

class dataflow_Port(Attributable):

    def __init__(self, name: str, dataflow_Port: "dataflow_Network" = None, dataflow_Port9: "dataflow_Network" = None, dataflow_Port23: "dataflow_Actor" = None, dataflow_Port26: "dataflow_Actor" = None, Port: "dataflow_Action" = None, Port54: "dataflow_Action" = None, target: "dataflow_Buffer" = None, source: set["dataflow_Buffer"] = None, dataflow_Port78: "dataflow_Actor" = None, Port81: "dataflow_Buffer" = None, Port83: "dataflow_Buffer" = None, outputPorts: set["dataflow_Action"] = None, inputPorts: set["dataflow_Action"] = None):
        self.name = name
        self.dataflow_Port = dataflow_Port
        self.dataflow_Port9 = dataflow_Port9
        self.dataflow_Port23 = dataflow_Port23
        self.dataflow_Port26 = dataflow_Port26
        self.Port = Port
        self.Port54 = Port54
        self.target = target
        self.source = source if source is not None else set()
        self.dataflow_Port78 = dataflow_Port78
        self.Port81 = Port81
        self.Port83 = Port83
        self.outputPorts = outputPorts if outputPorts is not None else set()
        self.inputPorts = inputPorts if inputPorts is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__target", None)
        self.__target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Buffer"):
                opp_val = getattr(old_value, "Buffer", None)
                if opp_val == self:
                    setattr(old_value, "Buffer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Buffer"):
                opp_val = getattr(value, "Buffer", None)
                setattr(value, "Buffer", self)

    @property
    def Port83(self):
        return self.__Port83

    @Port83.setter
    def Port83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__Port83", None)
        self.__Port83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "input"):
                opp_val = getattr(old_value, "input", None)
                if opp_val == self:
                    setattr(old_value, "input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "input"):
                opp_val = getattr(value, "input", None)
                setattr(value, "input", self)

    @property
    def dataflow_Port9(self):
        return self.__dataflow_Port9

    @dataflow_Port9.setter
    def dataflow_Port9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__dataflow_Port9", None)
        self.__dataflow_Port9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network8"):
                opp_val = getattr(old_value, "dataflow_Network8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network8"):
                opp_val = getattr(value, "dataflow_Network8", None)
                if opp_val is None:
                    setattr(value, "dataflow_Network8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Buffer76"):
                    opp_val = getattr(item, "Buffer76", None)
                    
                    if opp_val == self:
                        setattr(item, "Buffer76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Buffer76"):
                    opp_val = getattr(item, "Buffer76", None)
                    
                    setattr(item, "Buffer76", self)
                    

    @property
    def outputPorts(self):
        return self.__outputPorts

    @outputPorts.setter
    def outputPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__outputPorts", None)
        self.__outputPorts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

    @property
    def inputPorts(self):
        return self.__inputPorts

    @inputPorts.setter
    def inputPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__inputPorts", None)
        self.__inputPorts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action73"):
                    opp_val = getattr(item, "Action73", None)
                    
                    if opp_val == self:
                        setattr(item, "Action73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action73"):
                    opp_val = getattr(item, "Action73", None)
                    
                    setattr(item, "Action73", self)
                    

    @property
    def dataflow_Port(self):
        return self.__dataflow_Port

    @dataflow_Port.setter
    def dataflow_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__dataflow_Port", None)
        self.__dataflow_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Network6"):
                opp_val = getattr(old_value, "dataflow_Network6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Network6"):
                opp_val = getattr(value, "dataflow_Network6", None)
                if opp_val is None:
                    setattr(value, "dataflow_Network6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Port26(self):
        return self.__dataflow_Port26

    @dataflow_Port26.setter
    def dataflow_Port26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__dataflow_Port26", None)
        self.__dataflow_Port26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor25"):
                opp_val = getattr(old_value, "dataflow_Actor25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor25"):
                opp_val = getattr(value, "dataflow_Actor25", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__Port", None)
        self.__Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "readers"):
                opp_val = getattr(old_value, "readers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "readers"):
                opp_val = getattr(value, "readers", None)
                if opp_val is None:
                    setattr(value, "readers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Port81(self):
        return self.__Port81

    @Port81.setter
    def Port81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__Port81", None)
        self.__Port81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputs"):
                opp_val = getattr(old_value, "outputs", None)
                if opp_val == self:
                    setattr(old_value, "outputs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputs"):
                opp_val = getattr(value, "outputs", None)
                setattr(value, "outputs", self)

    @property
    def Port54(self):
        return self.__Port54

    @Port54.setter
    def Port54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__Port54", None)
        self.__Port54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers"):
                opp_val = getattr(old_value, "writers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers"):
                opp_val = getattr(value, "writers", None)
                if opp_val is None:
                    setattr(value, "writers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Port23(self):
        return self.__dataflow_Port23

    @dataflow_Port23.setter
    def dataflow_Port23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__dataflow_Port23", None)
        self.__dataflow_Port23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor22"):
                opp_val = getattr(old_value, "dataflow_Actor22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor22"):
                opp_val = getattr(value, "dataflow_Actor22", None)
                if opp_val is None:
                    setattr(value, "dataflow_Actor22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflow_Port78(self):
        return self.__dataflow_Port78

    @dataflow_Port78.setter
    def dataflow_Port78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflow_Port__dataflow_Port78", None)
        self.__dataflow_Port78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflow_Actor79"):
                opp_val = getattr(old_value, "dataflow_Actor79", None)
                if opp_val == self:
                    setattr(old_value, "dataflow_Actor79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflow_Actor79"):
                opp_val = getattr(value, "dataflow_Actor79", None)
                setattr(value, "dataflow_Actor79", self)
