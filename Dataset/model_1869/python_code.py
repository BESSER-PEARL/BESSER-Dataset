from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Query:

    pass
class Wires_GenericQuery(Query):

    pass
class ActualParameter:

    pass
class Wires_TypeParameter(ActualParameter):

    pass
class FormalParameter:

    pass
class AtomicModelTransformation:

    pass
class Wires_GenericTransformation(AtomicModelTransformation):

    pass
class Wires_IdentityTransformation(AtomicModelTransformation):

    pass
class Wires_WiresElement(ABC):

    pass
class Wires_WiresSpecification:

    pass
class WiresSpecification:

    pass
class TransformationType:

    pass
class Wires_CompositeTransformationType(WiresSpecification, TransformationType):

    pass
class Wires_AtomicModelTransfomationType(TransformationType):

    pass
class Wires_QueryType(TransformationType):

    pass
class Wires_InputFormalParameter(FormalParameter):

    pass
class Wires_LibraryRef:

    def __init__(self, name: str, Wires_LibraryRef: "Wires_TransformationType" = None, Wires_LibraryRef29: "Wires_Library" = None, Wires_LibraryRef32: "Wires_Library" = None):
        self.name = name
        self.Wires_LibraryRef = Wires_LibraryRef
        self.Wires_LibraryRef29 = Wires_LibraryRef29
        self.Wires_LibraryRef32 = Wires_LibraryRef32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Wires_LibraryRef29(self):
        return self.__Wires_LibraryRef29

    @Wires_LibraryRef29.setter
    def Wires_LibraryRef29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_LibraryRef__Wires_LibraryRef29", None)
        self.__Wires_LibraryRef29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_Library"):
                opp_val = getattr(old_value, "Wires_Library", None)
                if opp_val == self:
                    setattr(old_value, "Wires_Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_Library"):
                opp_val = getattr(value, "Wires_Library", None)
                setattr(value, "Wires_Library", self)

    @property
    def Wires_LibraryRef(self):
        return self.__Wires_LibraryRef

    @Wires_LibraryRef.setter
    def Wires_LibraryRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_LibraryRef__Wires_LibraryRef", None)
        self.__Wires_LibraryRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_TransformationType20"):
                opp_val = getattr(old_value, "Wires_TransformationType20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_TransformationType20"):
                opp_val = getattr(value, "Wires_TransformationType20", None)
                if opp_val is None:
                    setattr(value, "Wires_TransformationType20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Wires_LibraryRef32(self):
        return self.__Wires_LibraryRef32

    @Wires_LibraryRef32.setter
    def Wires_LibraryRef32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_LibraryRef__Wires_LibraryRef32", None)
        self.__Wires_LibraryRef32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_Library31"):
                opp_val = getattr(old_value, "Wires_Library31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_Library31"):
                opp_val = getattr(value, "Wires_Library31", None)
                if opp_val is None:
                    setattr(value, "Wires_Library31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Wires_OutputFormalParameter(FormalParameter):

    pass
class WiresElement:

    pass
class Wires_DataFlow(WiresElement):

    pass
class Wires_Library(WiresElement):

    def __init__(self, name: str, path: str, Wires_Library: "Wires_LibraryRef" = None, Wires_Library31: set["Wires_LibraryRef"] = None):
        self.name = name
        self.path = path
        self.Wires_Library = Wires_Library
        self.Wires_Library31 = Wires_Library31 if Wires_Library31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def Wires_Library(self):
        return self.__Wires_Library

    @Wires_Library.setter
    def Wires_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_Library__Wires_Library", None)
        self.__Wires_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_LibraryRef29"):
                opp_val = getattr(old_value, "Wires_LibraryRef29", None)
                if opp_val == self:
                    setattr(old_value, "Wires_LibraryRef29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_LibraryRef29"):
                opp_val = getattr(value, "Wires_LibraryRef29", None)
                setattr(value, "Wires_LibraryRef29", self)

    @property
    def Wires_Library31(self):
        return self.__Wires_Library31

    @Wires_Library31.setter
    def Wires_Library31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_Library__Wires_Library31", None)
        self.__Wires_Library31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Wires_LibraryRef32"):
                    opp_val = getattr(item, "Wires_LibraryRef32", None)
                    
                    if opp_val == self:
                        setattr(item, "Wires_LibraryRef32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Wires_LibraryRef32"):
                    opp_val = getattr(item, "Wires_LibraryRef32", None)
                    
                    setattr(item, "Wires_LibraryRef32", self)
                    

class Type:

    pass
class Wires_FormalParameter(Type):

    def __init__(self, typeName: str, Wires_FormalParameter: "Wires_DataType" = None):
        self.typeName = typeName
        self.Wires_FormalParameter = Wires_FormalParameter
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def Wires_FormalParameter(self):
        return self.__Wires_FormalParameter

    @Wires_FormalParameter.setter
    def Wires_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_FormalParameter__Wires_FormalParameter", None)
        self.__Wires_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_DataType"):
                opp_val = getattr(old_value, "Wires_DataType", None)
                if opp_val == self:
                    setattr(old_value, "Wires_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_DataType"):
                opp_val = getattr(value, "Wires_DataType", None)
                setattr(value, "Wires_DataType", self)

class Wires_TransformationType(Type):

    pass
class Wires_DataType(Type):

    pass
class DataType:

    pass
class Wires_BasicDataType(DataType):

    pass
class Wires_ModelType(DataType):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class Wires_ConnectableElement(WiresElement):

    def __init__(self, name: str, ConnectableElement: "Wires_DataFlow" = None, ConnectableElement17: "Wires_DataFlow" = None, target: set["Wires_DataFlow"] = None, src: set["Wires_DataFlow"] = None):
        self.name = name
        self.ConnectableElement = ConnectableElement
        self.ConnectableElement17 = ConnectableElement17
        self.target = target if target is not None else set()
        self.src = src if src is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ConnectableElement(self):
        return self.__ConnectableElement

    @ConnectableElement.setter
    def ConnectableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_ConnectableElement__ConnectableElement", None)
        self.__ConnectableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_ConnectableElement__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataFlow"):
                    opp_val = getattr(item, "DataFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "DataFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataFlow"):
                    opp_val = getattr(item, "DataFlow", None)
                    
                    setattr(item, "DataFlow", self)
                    

    @property
    def ConnectableElement17(self):
        return self.__ConnectableElement17

    @ConnectableElement17.setter
    def ConnectableElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_ConnectableElement__ConnectableElement17", None)
        self.__ConnectableElement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_ConnectableElement__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataFlow26"):
                    opp_val = getattr(item, "DataFlow26", None)
                    
                    if opp_val == self:
                        setattr(item, "DataFlow26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataFlow26"):
                    opp_val = getattr(item, "DataFlow26", None)
                    
                    setattr(item, "DataFlow26", self)
                    

class ConnectableElement:

    pass
class Wires_Type(ConnectableElement):

    def __init__(self, path: str, Wires_Type: "Wires_TypedElement" = None):
        self.path = path
        self.Wires_Type = Wires_Type
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def Wires_Type(self):
        return self.__Wires_Type

    @Wires_Type.setter
    def Wires_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_Type__Wires_Type", None)
        self.__Wires_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_TypedElement"):
                opp_val = getattr(old_value, "Wires_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "Wires_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_TypedElement"):
                opp_val = getattr(value, "Wires_TypedElement", None)
                setattr(value, "Wires_TypedElement", self)

class Wires_TypedElement(ConnectableElement):

    pass
class Transformation:

    pass
class Wires_CompositeTransformation(Transformation):

    pass
class Wires_AtomicModelTransformation(Transformation):

    pass
class Wires_Query(Transformation):

    pass
class Wires_DecisionNode(WiresElement):

    def __init__(self, expression: str, Wires_DecisionNode: "Wires_Transformation" = None, Wires_DecisionNode7: set["Wires_Transformation"] = None, Wires_DecisionNode10: set["Wires_Transformation"] = None, Wires_DecisionNode13: set["Wires_InputActualParameter"] = None):
        self.expression = expression
        self.Wires_DecisionNode = Wires_DecisionNode
        self.Wires_DecisionNode7 = Wires_DecisionNode7 if Wires_DecisionNode7 is not None else set()
        self.Wires_DecisionNode10 = Wires_DecisionNode10 if Wires_DecisionNode10 is not None else set()
        self.Wires_DecisionNode13 = Wires_DecisionNode13 if Wires_DecisionNode13 is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def Wires_DecisionNode7(self):
        return self.__Wires_DecisionNode7

    @Wires_DecisionNode7.setter
    def Wires_DecisionNode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_DecisionNode__Wires_DecisionNode7", None)
        self.__Wires_DecisionNode7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Wires_Transformation8"):
                    opp_val = getattr(item, "Wires_Transformation8", None)
                    
                    if opp_val == self:
                        setattr(item, "Wires_Transformation8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Wires_Transformation8"):
                    opp_val = getattr(item, "Wires_Transformation8", None)
                    
                    setattr(item, "Wires_Transformation8", self)
                    

    @property
    def Wires_DecisionNode10(self):
        return self.__Wires_DecisionNode10

    @Wires_DecisionNode10.setter
    def Wires_DecisionNode10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_DecisionNode__Wires_DecisionNode10", None)
        self.__Wires_DecisionNode10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Wires_Transformation11"):
                    opp_val = getattr(item, "Wires_Transformation11", None)
                    
                    if opp_val == self:
                        setattr(item, "Wires_Transformation11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Wires_Transformation11"):
                    opp_val = getattr(item, "Wires_Transformation11", None)
                    
                    setattr(item, "Wires_Transformation11", self)
                    

    @property
    def Wires_DecisionNode(self):
        return self.__Wires_DecisionNode

    @Wires_DecisionNode.setter
    def Wires_DecisionNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_DecisionNode__Wires_DecisionNode", None)
        self.__Wires_DecisionNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Wires_Transformation4"):
                opp_val = getattr(old_value, "Wires_Transformation4", None)
                if opp_val == self:
                    setattr(old_value, "Wires_Transformation4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Wires_Transformation4"):
                opp_val = getattr(value, "Wires_Transformation4", None)
                setattr(value, "Wires_Transformation4", self)

    @property
    def Wires_DecisionNode13(self):
        return self.__Wires_DecisionNode13

    @Wires_DecisionNode13.setter
    def Wires_DecisionNode13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wires_DecisionNode__Wires_DecisionNode13", None)
        self.__Wires_DecisionNode13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Wires_InputActualParameter14"):
                    opp_val = getattr(item, "Wires_InputActualParameter14", None)
                    
                    if opp_val == self:
                        setattr(item, "Wires_InputActualParameter14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Wires_InputActualParameter14"):
                    opp_val = getattr(item, "Wires_InputActualParameter14", None)
                    
                    setattr(item, "Wires_InputActualParameter14", self)
                    

class Wires_OutputActualParameter(ActualParameter):

    pass
class Wires_InputActualParameter(ActualParameter):

    pass
class TypedElement:

    pass
class Wires_Model(TypedElement):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class Wires_ActualParameter(TypedElement):

    pass
class Wires_BasicData(TypedElement):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class Wires_Transformation(TypedElement):

    pass