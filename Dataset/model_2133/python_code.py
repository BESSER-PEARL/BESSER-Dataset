from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class architecture_extension_Bop:

    pass
class architecture_extension_RelationshipConstraint(ABC):

    def __init__(self):
        
    def check(self, relationship: str) -> bool:
        # TODO: Implement check method
        pass

class ReferenceDependency:

    pass
class architecture_ImportReferenceDependency(ReferenceDependency):

    pass
class architecture_FieldReferenceDependency(ReferenceDependency):

    pass
class RuntimeDependency:

    pass
class architecture_InjectionDependency(RuntimeDependency):

    pass
class Relationship:

    pass
class architecture_extension_RoleRelationship(Relationship):

    def __init__(self):
        
    def checkConstraint(self) -> bool:
        # TODO: Implement checkConstraint method
        pass

    def getTarget(self):
        # TODO: Implement getTarget method
        pass

class architecture_extension_PatternRelationship(Relationship):

    def __init__(self, referenceName: str):
        self.referenceName = referenceName
        
    @property
    def referenceName(self) -> str:
        return self.__referenceName

    @referenceName.setter
    def referenceName(self, referenceName: str):
        self.__referenceName = referenceName

    def checkConstraint(self) -> bool:
        # TODO: Implement checkConstraint method
        pass

    def getSource(self) -> str:
        # TODO: Implement getSource method
        pass

    def getTarget(self):
        # TODO: Implement getTarget method
        pass

class architecture_extension_ExtensionRelationship(Relationship):

    def __init__(self):
        
    def checkConstraint(self) -> bool:
        # TODO: Implement checkConstraint method
        pass

class architecture_Dependency(Relationship):

    pass
class Dependency:

    pass
class architecture_ReferenceDependency(Dependency):

    def __init__(self, uri: str, name: str):
        self.uri = uri
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class architecture_RuntimeDependency(Dependency):

    pass
class architecture_InheritanceDependency(Dependency):

    pass
class AnalysedElement:

    pass
class architecture_Library(AnalysedElement):

    pass
class architecture_extension_Role(AnalysedElement):

    def __init__(self, attachedElement: str):
        self.attachedElement = attachedElement
        
    @property
    def attachedElement(self) -> str:
        return self.__attachedElement

    @attachedElement.setter
    def attachedElement(self, attachedElement: str):
        self.__attachedElement = attachedElement

class architecture_extension_Pattern(AnalysedElement):

    pass
class architecture_ArchitectureFile(AnalysedElement):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class architecture_Type(AnalysedElement):

    def __init__(self, qualifiedName: str, source: bool, binary: bool):
        self.qualifiedName = qualifiedName
        self.source = source
        self.binary = binary
        
    @property
    def binary(self) -> bool:
        return self.__binary

    @binary.setter
    def binary(self, binary: bool):
        self.__binary = binary

    @property
    def source(self) -> bool:
        return self.__source

    @source.setter
    def source(self, source: bool):
        self.__source = source

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class architecture_DeclaredType(Relationship):

    pass
class architecture_Field(AnalysedElement):

    pass
class architecture_CallRelationship(Relationship):

    pass
class architecture_ParameterRelationship(Relationship):

    pass
class architecture_ReturnTypeRelationship(Relationship):

    pass
class architecture_Method(AnalysedElement):

    pass
class architecture_Project(AnalysedElement):

    pass
class architecture_AnalysedElement(ABC):

    def __init__(self, idAnalyzedElement: int, name: str, properties: int, source: set["architecture_Relationship"] = None, target: set["architecture_Relationship"] = None, AnalysedElement: "architecture_AnalysedElement" = None, parent: set["architecture_AnalysedElement"] = None, AnalysedElement7: "architecture_AnalysedElement" = None, containedElements: "architecture_AnalysedElement" = None, AnalysedElement9: "architecture_Relationship" = None, AnalysedElement11: "architecture_Relationship" = None, architecture_AnalysedElement: "architecture_InjectionDependency" = None):
        self.idAnalyzedElement = idAnalyzedElement
        self.name = name
        self.properties = properties
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.AnalysedElement = AnalysedElement
        self.parent = parent if parent is not None else set()
        self.AnalysedElement7 = AnalysedElement7
        self.containedElements = containedElements
        self.AnalysedElement9 = AnalysedElement9
        self.AnalysedElement11 = AnalysedElement11
        self.architecture_AnalysedElement = architecture_AnalysedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idAnalyzedElement(self) -> int:
        return self.__idAnalyzedElement

    @idAnalyzedElement.setter
    def idAnalyzedElement(self, idAnalyzedElement: int):
        self.__idAnalyzedElement = idAnalyzedElement

    @property
    def properties(self) -> int:
        return self.__properties

    @properties.setter
    def properties(self, properties: int):
        self.__properties = properties

    @property
    def AnalysedElement11(self):
        return self.__AnalysedElement11

    @AnalysedElement11.setter
    def AnalysedElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__AnalysedElement11", None)
        self.__AnalysedElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingRelationships"):
                opp_val = getattr(old_value, "outgoingRelationships", None)
                if opp_val == self:
                    setattr(old_value, "outgoingRelationships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingRelationships"):
                opp_val = getattr(value, "outgoingRelationships", None)
                setattr(value, "outgoingRelationships", self)

    @property
    def containedElements(self):
        return self.__containedElements

    @containedElements.setter
    def containedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__containedElements", None)
        self.__containedElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnalysedElement7"):
                opp_val = getattr(old_value, "AnalysedElement7", None)
                if opp_val == self:
                    setattr(old_value, "AnalysedElement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnalysedElement7"):
                opp_val = getattr(value, "AnalysedElement7", None)
                setattr(value, "AnalysedElement7", self)

    @property
    def AnalysedElement9(self):
        return self.__AnalysedElement9

    @AnalysedElement9.setter
    def AnalysedElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__AnalysedElement9", None)
        self.__AnalysedElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingRelationships"):
                opp_val = getattr(old_value, "incomingRelationships", None)
                if opp_val == self:
                    setattr(old_value, "incomingRelationships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingRelationships"):
                opp_val = getattr(value, "incomingRelationships", None)
                setattr(value, "incomingRelationships", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship2"):
                    opp_val = getattr(item, "Relationship2", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship2"):
                    opp_val = getattr(item, "Relationship2", None)
                    
                    setattr(item, "Relationship2", self)
                    

    @property
    def architecture_AnalysedElement(self):
        return self.__architecture_AnalysedElement

    @architecture_AnalysedElement.setter
    def architecture_AnalysedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__architecture_AnalysedElement", None)
        self.__architecture_AnalysedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_InjectionDependency"):
                opp_val = getattr(old_value, "architecture_InjectionDependency", None)
                if opp_val == self:
                    setattr(old_value, "architecture_InjectionDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_InjectionDependency"):
                opp_val = getattr(value, "architecture_InjectionDependency", None)
                setattr(value, "architecture_InjectionDependency", self)

    @property
    def AnalysedElement(self):
        return self.__AnalysedElement

    @AnalysedElement.setter
    def AnalysedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__AnalysedElement", None)
        self.__AnalysedElement = value
        
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
    def AnalysedElement7(self):
        return self.__AnalysedElement7

    @AnalysedElement7.setter
    def AnalysedElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__AnalysedElement7", None)
        self.__AnalysedElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedElements"):
                opp_val = getattr(old_value, "containedElements", None)
                if opp_val == self:
                    setattr(old_value, "containedElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedElements"):
                opp_val = getattr(value, "containedElements", None)
                setattr(value, "containedElements", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AnalysedElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnalysedElement"):
                    opp_val = getattr(item, "AnalysedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "AnalysedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnalysedElement"):
                    opp_val = getattr(item, "AnalysedElement", None)
                    
                    setattr(item, "AnalysedElement", self)
                    

class architecture_Relationship(ABC):

    def __init__(self, relationShipId: int, Relationship: "architecture_AnalysedElement" = None, Relationship2: "architecture_AnalysedElement" = None, incomingRelationships: "architecture_AnalysedElement" = None, outgoingRelationships: "architecture_AnalysedElement" = None):
        self.relationShipId = relationShipId
        self.Relationship = Relationship
        self.Relationship2 = Relationship2
        self.incomingRelationships = incomingRelationships
        self.outgoingRelationships = outgoingRelationships
        
    @property
    def relationShipId(self) -> int:
        return self.__relationShipId

    @relationShipId.setter
    def relationShipId(self, relationShipId: int):
        self.__relationShipId = relationShipId

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingRelationships(self):
        return self.__incomingRelationships

    @incomingRelationships.setter
    def incomingRelationships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Relationship__incomingRelationships", None)
        self.__incomingRelationships = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnalysedElement9"):
                opp_val = getattr(old_value, "AnalysedElement9", None)
                if opp_val == self:
                    setattr(old_value, "AnalysedElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnalysedElement9"):
                opp_val = getattr(value, "AnalysedElement9", None)
                setattr(value, "AnalysedElement9", self)

    @property
    def outgoingRelationships(self):
        return self.__outgoingRelationships

    @outgoingRelationships.setter
    def outgoingRelationships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Relationship__outgoingRelationships", None)
        self.__outgoingRelationships = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnalysedElement11"):
                opp_val = getattr(old_value, "AnalysedElement11", None)
                if opp_val == self:
                    setattr(old_value, "AnalysedElement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnalysedElement11"):
                opp_val = getattr(value, "AnalysedElement11", None)
                setattr(value, "AnalysedElement11", self)

    @property
    def Relationship2(self):
        return self.__Relationship2

    @Relationship2.setter
    def Relationship2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Relationship__Relationship2", None)
        self.__Relationship2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
