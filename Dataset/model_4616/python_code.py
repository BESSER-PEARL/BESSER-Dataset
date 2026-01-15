from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeType(Enum):
    IS_ATYPE = "IS_ATYPE"
    AKO_TYPE = "AKO_TYPE"
    ROLE_CONSTRAINT_TYPE = "ROLE_CONSTRAINT_TYPE"
class KindOfTopicType(Enum):
    TopicType = "TopicType"
    OccurrenceType = "OccurrenceType"
    NameType = "NameType"
    RoleType = "RoleType"
    AssociationType = "AssociationType"
    ScopeType = "ScopeType"
    NoType = "NoType"
class TopicId(Enum):
    SUBJECT_LOCATOR = "SUBJECT_LOCATOR"
    SUBJECT_IDENTIFIER = "SUBJECT_IDENTIFIER"
    ITEM_IDENTIFIER = "ITEM_IDENTIFIER"
    IDENTIFIER = "IDENTIFIER"


############################################
# Definition of Classes
############################################

class model_OnoObject(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class Diagram:

    pass
class model_DomainDiagram(Diagram):

    pass
class ReifiableTopicType:

    pass
class TopicType:

    pass
class model_ReifiableTopicType(TopicType):

    pass
class model_AbstractRegExpTopicType(TopicType):

    def __init__(self, regExp: str):
        self.regExp = regExp
        
    @property
    def regExp(self) -> str:
        return self.__regExp

    @regExp.setter
    def regExp(self, regExp: str):
        self.__regExp = regExp

class model_AbstractUniqueValueTopicType(TopicType):

    def __init__(self, unique: bool):
        self.unique = unique
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

class model_ScopedTopicType(TopicType):

    pass
class model_RoleType(TopicType):

    pass
class AbstractUniqueValueTopicType:

    pass
class AbstractRegExpTopicType:

    pass
class ScopedReifiableTopicType:

    pass
class ScopedTopicType:

    pass
class model_ScopedReifiableTopicType(ScopedTopicType, ReifiableTopicType):

    pass
class model_NameType(ScopedTopicType, ScopedReifiableTopicType, AbstractUniqueValueTopicType, AbstractRegExpTopicType):

    pass
class model_OccurrenceType(ScopedTopicType, ScopedReifiableTopicType, AbstractUniqueValueTopicType, AbstractRegExpTopicType):

    def __init__(self, dataType: str):
        self.dataType = dataType
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

class model_AssociationType(ScopedTopicType, ScopedReifiableTopicType):

    pass
class AbstractCardinalityConstraint:

    pass
class model_RolePlayerConstraint(AbstractCardinalityConstraint):

    pass
class AbstractTypedCardinalityConstraint:

    pass
class model_ReifierConstraint(AbstractTypedCardinalityConstraint):

    pass
class model_RoleConstraint(AbstractTypedCardinalityConstraint):

    pass
class model_ScopeConstraint(AbstractTypedCardinalityConstraint):

    pass
class AbstractConstraint:

    pass
class model_AbstractTypedConstraint(AbstractConstraint):

    pass
class model_RoleCombinationConstraint(AbstractConstraint):

    pass
class model_AbstractCardinalityConstraint(AbstractConstraint):

    def __init__(self, cardMin: str, cardMax: str):
        self.cardMin = cardMin
        self.cardMax = cardMax
        
    @property
    def cardMin(self) -> str:
        return self.__cardMin

    @cardMin.setter
    def cardMin(self, cardMin: str):
        self.__cardMin = cardMin

    @property
    def cardMax(self) -> str:
        return self.__cardMax

    @cardMax.setter
    def cardMax(self, cardMax: str):
        self.__cardMax = cardMax

class model_AbstractRegExpConstraint(AbstractConstraint):

    def __init__(self, regexp: str):
        self.regexp = regexp
        
    @property
    def regexp(self) -> str:
        return self.__regexp

    @regexp.setter
    def regexp(self, regexp: str):
        self.__regexp = regexp

class Node:

    pass
class model_Comment(Node):

    def __init__(self, content: str, width: int, height: int, model_Comment: "model_Diagram" = None):
        self.content = content
        self.width = width
        self.height = height
        self.model_Comment = model_Comment
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def model_Comment(self):
        return self.__model_Comment

    @model_Comment.setter
    def model_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Comment__model_Comment", None)
        self.__model_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Diagram54"):
                opp_val = getattr(old_value, "model_Diagram54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Diagram54"):
                opp_val = getattr(value, "model_Diagram54", None)
                if opp_val is None:
                    setattr(value, "model_Diagram54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_AssociationNode(Node):

    pass
class model_TypeNode(Node):

    def __init__(self, image: str, model_TypeNode: "model_TopicType" = None):
        self.image = image
        self.model_TypeNode = model_TypeNode
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def model_TypeNode(self):
        return self.__model_TypeNode

    @model_TypeNode.setter
    def model_TypeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TypeNode__model_TypeNode", None)
        self.__model_TypeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicType34"):
                opp_val = getattr(old_value, "model_TopicType34", None)
                if opp_val == self:
                    setattr(old_value, "model_TopicType34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicType34"):
                opp_val = getattr(value, "model_TopicType34", None)
                setattr(value, "model_TopicType34", self)

class OnoObject:

    pass
class model_File(OnoObject):

    def __init__(self, filename: str, dirty: bool, notes: str, model_File: set["model_Diagram"] = None, model_File58: "model_TopicMapSchema" = None):
        self.filename = filename
        self.dirty = dirty
        self.notes = notes
        self.model_File = model_File if model_File is not None else set()
        self.model_File58 = model_File58
        
    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def dirty(self) -> bool:
        return self.__dirty

    @dirty.setter
    def dirty(self, dirty: bool):
        self.__dirty = dirty

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def model_File(self):
        return self.__model_File

    @model_File.setter
    def model_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_File__model_File", None)
        self.__model_File = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Diagram56"):
                    opp_val = getattr(item, "model_Diagram56", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Diagram56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Diagram56"):
                    opp_val = getattr(item, "model_Diagram56", None)
                    
                    setattr(item, "model_Diagram56", self)
                    

    @property
    def model_File58(self):
        return self.__model_File58

    @model_File58.setter
    def model_File58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_File__model_File58", None)
        self.__model_File58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicMapSchema59"):
                opp_val = getattr(old_value, "model_TopicMapSchema59", None)
                if opp_val == self:
                    setattr(old_value, "model_TopicMapSchema59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicMapSchema59"):
                opp_val = getattr(value, "model_TopicMapSchema59", None)
                setattr(value, "model_TopicMapSchema59", self)

class model_Bendpoint(OnoObject):

    def __init__(self, posX: int, posY: int, model_Bendpoint: "model_Edge" = None):
        self.posX = posX
        self.posY = posY
        self.model_Bendpoint = model_Bendpoint
        
    @property
    def posY(self) -> int:
        return self.__posY

    @posY.setter
    def posY(self, posY: int):
        self.__posY = posY

    @property
    def posX(self) -> int:
        return self.__posX

    @posX.setter
    def posX(self, posX: int):
        self.__posX = posX

    @property
    def model_Bendpoint(self):
        return self.__model_Bendpoint

    @model_Bendpoint.setter
    def model_Bendpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Bendpoint__model_Bendpoint", None)
        self.__model_Bendpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge"):
                opp_val = getattr(old_value, "model_Edge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge"):
                opp_val = getattr(value, "model_Edge", None)
                if opp_val is None:
                    setattr(value, "model_Edge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_TMCLConstruct(OnoObject):

    def __init__(self, see_also: str, comment: str, description: str, model_TMCLConstruct: set["model_Annotation"] = None):
        self.see_also = see_also
        self.comment = comment
        self.description = description
        self.model_TMCLConstruct = model_TMCLConstruct if model_TMCLConstruct is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def see_also(self) -> str:
        return self.__see_also

    @see_also.setter
    def see_also(self, see_also: str):
        self.__see_also = see_also

    @property
    def model_TMCLConstruct(self):
        return self.__model_TMCLConstruct

    @model_TMCLConstruct.setter
    def model_TMCLConstruct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TMCLConstruct__model_TMCLConstruct", None)
        self.__model_TMCLConstruct = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Annotation"):
                    opp_val = getattr(item, "model_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Annotation"):
                    opp_val = getattr(item, "model_Annotation", None)
                    
                    setattr(item, "model_Annotation", self)
                    

class model_Edge(OnoObject):

    def __init__(self, type: str, model_Edge49: "model_Diagram" = None, model_Edge: set["model_Bendpoint"] = None, model_Edge37: "model_Node" = None, model_Edge39: "model_Node" = None, model_Edge42: "model_RolePlayerConstraint" = None, model_Edge45: set["model_LabelPos"] = None):
        self.type = type
        self.model_Edge49 = model_Edge49
        self.model_Edge = model_Edge if model_Edge is not None else set()
        self.model_Edge37 = model_Edge37
        self.model_Edge39 = model_Edge39
        self.model_Edge42 = model_Edge42
        self.model_Edge45 = model_Edge45 if model_Edge45 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def model_Edge(self):
        return self.__model_Edge

    @model_Edge.setter
    def model_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge", None)
        self.__model_Edge = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Bendpoint"):
                    opp_val = getattr(item, "model_Bendpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Bendpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Bendpoint"):
                    opp_val = getattr(item, "model_Bendpoint", None)
                    
                    setattr(item, "model_Bendpoint", self)
                    

    @property
    def model_Edge42(self):
        return self.__model_Edge42

    @model_Edge42.setter
    def model_Edge42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge42", None)
        self.__model_Edge42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RolePlayerConstraint43"):
                opp_val = getattr(old_value, "model_RolePlayerConstraint43", None)
                if opp_val == self:
                    setattr(old_value, "model_RolePlayerConstraint43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RolePlayerConstraint43"):
                opp_val = getattr(value, "model_RolePlayerConstraint43", None)
                setattr(value, "model_RolePlayerConstraint43", self)

    @property
    def model_Edge49(self):
        return self.__model_Edge49

    @model_Edge49.setter
    def model_Edge49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge49", None)
        self.__model_Edge49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Diagram"):
                opp_val = getattr(old_value, "model_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Diagram"):
                opp_val = getattr(value, "model_Diagram", None)
                if opp_val is None:
                    setattr(value, "model_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Edge37(self):
        return self.__model_Edge37

    @model_Edge37.setter
    def model_Edge37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge37", None)
        self.__model_Edge37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node"):
                opp_val = getattr(old_value, "model_Node", None)
                if opp_val == self:
                    setattr(old_value, "model_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node"):
                opp_val = getattr(value, "model_Node", None)
                setattr(value, "model_Node", self)

    @property
    def model_Edge39(self):
        return self.__model_Edge39

    @model_Edge39.setter
    def model_Edge39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge39", None)
        self.__model_Edge39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node40"):
                opp_val = getattr(old_value, "model_Node40", None)
                if opp_val == self:
                    setattr(old_value, "model_Node40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node40"):
                opp_val = getattr(value, "model_Node40", None)
                setattr(value, "model_Node40", self)

    @property
    def model_Edge45(self):
        return self.__model_Edge45

    @model_Edge45.setter
    def model_Edge45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge45", None)
        self.__model_Edge45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_LabelPos"):
                    opp_val = getattr(item, "model_LabelPos", None)
                    
                    if opp_val == self:
                        setattr(item, "model_LabelPos", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_LabelPos"):
                    opp_val = getattr(item, "model_LabelPos", None)
                    
                    setattr(item, "model_LabelPos", self)
                    

class model_LabelPos(OnoObject):

    def __init__(self, posX: int, posY: int, model_LabelPos: "model_Edge" = None):
        self.posX = posX
        self.posY = posY
        self.model_LabelPos = model_LabelPos
        
    @property
    def posX(self) -> int:
        return self.__posX

    @posX.setter
    def posX(self, posX: int):
        self.__posX = posX

    @property
    def posY(self) -> int:
        return self.__posY

    @posY.setter
    def posY(self, posY: int):
        self.__posY = posY

    @property
    def model_LabelPos(self):
        return self.__model_LabelPos

    @model_LabelPos.setter
    def model_LabelPos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_LabelPos__model_LabelPos", None)
        self.__model_LabelPos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge45"):
                opp_val = getattr(old_value, "model_Edge45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge45"):
                opp_val = getattr(value, "model_Edge45", None)
                if opp_val is None:
                    setattr(value, "model_Edge45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Diagram(OnoObject):

    def __init__(self, name: str, model_Diagram: set["model_Edge"] = None, model_Diagram51: set["model_Node"] = None, model_Diagram54: set["model_Comment"] = None, model_Diagram56: "model_File" = None):
        self.name = name
        self.model_Diagram = model_Diagram if model_Diagram is not None else set()
        self.model_Diagram51 = model_Diagram51 if model_Diagram51 is not None else set()
        self.model_Diagram54 = model_Diagram54 if model_Diagram54 is not None else set()
        self.model_Diagram56 = model_Diagram56
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Diagram56(self):
        return self.__model_Diagram56

    @model_Diagram56.setter
    def model_Diagram56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Diagram__model_Diagram56", None)
        self.__model_Diagram56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_File"):
                opp_val = getattr(old_value, "model_File", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_File"):
                opp_val = getattr(value, "model_File", None)
                if opp_val is None:
                    setattr(value, "model_File", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Diagram54(self):
        return self.__model_Diagram54

    @model_Diagram54.setter
    def model_Diagram54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Diagram__model_Diagram54", None)
        self.__model_Diagram54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Comment"):
                    opp_val = getattr(item, "model_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Comment"):
                    opp_val = getattr(item, "model_Comment", None)
                    
                    setattr(item, "model_Comment", self)
                    

    @property
    def model_Diagram(self):
        return self.__model_Diagram

    @model_Diagram.setter
    def model_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Diagram__model_Diagram", None)
        self.__model_Diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Edge49"):
                    opp_val = getattr(item, "model_Edge49", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Edge49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Edge49"):
                    opp_val = getattr(item, "model_Edge49", None)
                    
                    setattr(item, "model_Edge49", self)
                    

    @property
    def model_Diagram51(self):
        return self.__model_Diagram51

    @model_Diagram51.setter
    def model_Diagram51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Diagram__model_Diagram51", None)
        self.__model_Diagram51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Node52"):
                    opp_val = getattr(item, "model_Node52", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Node52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Node52"):
                    opp_val = getattr(item, "model_Node52", None)
                    
                    setattr(item, "model_Node52", self)
                    

class model_Annotation(OnoObject):

    def __init__(self, key: str, value: str, model_Annotation: "model_TMCLConstruct" = None):
        self.key = key
        self.value = value
        self.model_Annotation = model_Annotation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_Annotation(self):
        return self.__model_Annotation

    @model_Annotation.setter
    def model_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Annotation__model_Annotation", None)
        self.__model_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TMCLConstruct"):
                opp_val = getattr(old_value, "model_TMCLConstruct", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TMCLConstruct"):
                opp_val = getattr(value, "model_TMCLConstruct", None)
                if opp_val is None:
                    setattr(value, "model_TMCLConstruct", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Node(OnoObject):

    def __init__(self, posX: int, posY: int, model_Node52: "model_Diagram" = None, model_Node: "model_Edge" = None, model_Node40: "model_Edge" = None):
        self.posX = posX
        self.posY = posY
        self.model_Node52 = model_Node52
        self.model_Node = model_Node
        self.model_Node40 = model_Node40
        
    @property
    def posX(self) -> int:
        return self.__posX

    @posX.setter
    def posX(self, posX: int):
        self.__posX = posX

    @property
    def posY(self) -> int:
        return self.__posY

    @posY.setter
    def posY(self, posY: int):
        self.__posY = posY

    @property
    def model_Node52(self):
        return self.__model_Node52

    @model_Node52.setter
    def model_Node52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node52", None)
        self.__model_Node52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Diagram51"):
                opp_val = getattr(old_value, "model_Diagram51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Diagram51"):
                opp_val = getattr(value, "model_Diagram51", None)
                if opp_val is None:
                    setattr(value, "model_Diagram51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Node40(self):
        return self.__model_Node40

    @model_Node40.setter
    def model_Node40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node40", None)
        self.__model_Node40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge39"):
                opp_val = getattr(old_value, "model_Edge39", None)
                if opp_val == self:
                    setattr(old_value, "model_Edge39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge39"):
                opp_val = getattr(value, "model_Edge39", None)
                setattr(value, "model_Edge39", self)

    @property
    def model_Node(self):
        return self.__model_Node

    @model_Node.setter
    def model_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node", None)
        self.__model_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge37"):
                opp_val = getattr(old_value, "model_Edge37", None)
                if opp_val == self:
                    setattr(old_value, "model_Edge37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge37"):
                opp_val = getattr(value, "model_Edge37", None)
                setattr(value, "model_Edge37", self)

class AbstractTypedConstraint:

    pass
class model_AbstractTypedCardinalityConstraint(AbstractTypedConstraint, AbstractCardinalityConstraint):

    pass
class AbstractRegExpConstraint:

    pass
class model_MappingElement(OnoObject):

    def __init__(self, key: str, value: str, model_MappingElement: "model_TopicMapSchema" = None):
        self.key = key
        self.value = value
        self.model_MappingElement = model_MappingElement
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_MappingElement(self):
        return self.__model_MappingElement

    @model_MappingElement.setter
    def model_MappingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappingElement__model_MappingElement", None)
        self.__model_MappingElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicMapSchema29"):
                opp_val = getattr(old_value, "model_TopicMapSchema29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicMapSchema29"):
                opp_val = getattr(value, "model_TopicMapSchema29", None)
                if opp_val is None:
                    setattr(value, "model_TopicMapSchema29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_AssociationTypeConstraint(AbstractTypedConstraint):

    pass
class model_ItemIdentifierConstraint(AbstractRegExpConstraint, AbstractCardinalityConstraint):

    pass
class model_TopicReifiesConstraint(AbstractTypedCardinalityConstraint):

    pass
class model_SubjectLocatorConstraint(AbstractRegExpConstraint, AbstractCardinalityConstraint):

    pass
class model_SubjectIdentifierConstraint(AbstractRegExpConstraint, AbstractCardinalityConstraint):

    pass
class model_NameTypeConstraint(AbstractTypedCardinalityConstraint):

    pass
class model_OccurrenceTypeConstraint(AbstractTypedCardinalityConstraint):

    pass
class TMCLConstruct:

    pass
class model_TopicType(TMCLConstruct):

    def __init__(self, identifiers: str, idType: str, abstract: bool, kind: str, name: str, locators: str, model_TopicType: "model_TopicType" = None, model_TopicType0: set["model_TopicType"] = None, model_TopicType4: "model_TopicType" = None, model_TopicType2: set["model_TopicType"] = None, model_TopicType6: set["model_OccurrenceTypeConstraint"] = None, model_TopicType8: set["model_NameTypeConstraint"] = None, model_TopicType10: set["model_SubjectIdentifierConstraint"] = None, model_TopicType12: set["model_SubjectLocatorConstraint"] = None, model_TopicType15: "model_TopicType" = None, model_TopicType13: set["model_TopicType"] = None, model_TopicType17: set["model_TopicReifiesConstraint"] = None, model_TopicType19: set["model_ItemIdentifierConstraint"] = None, model_TopicType34: "model_TypeNode" = None, model_TopicType21: "model_RolePlayerConstraint" = None, model_TopicType25: "model_TopicMapSchema" = None, model_TopicType69: "model_RoleCombinationConstraint" = None, model_TopicType72: "model_RoleCombinationConstraint" = None, model_TopicType75: "model_RoleCombinationConstraint" = None, model_TopicType61: "model_AbstractTypedConstraint" = None, model_TopicType78: "model_RoleCombinationConstraint" = None):
        self.identifiers = identifiers
        self.idType = idType
        self.abstract = abstract
        self.kind = kind
        self.name = name
        self.locators = locators
        self.model_TopicType = model_TopicType
        self.model_TopicType0 = model_TopicType0 if model_TopicType0 is not None else set()
        self.model_TopicType4 = model_TopicType4
        self.model_TopicType2 = model_TopicType2 if model_TopicType2 is not None else set()
        self.model_TopicType6 = model_TopicType6 if model_TopicType6 is not None else set()
        self.model_TopicType8 = model_TopicType8 if model_TopicType8 is not None else set()
        self.model_TopicType10 = model_TopicType10 if model_TopicType10 is not None else set()
        self.model_TopicType12 = model_TopicType12 if model_TopicType12 is not None else set()
        self.model_TopicType15 = model_TopicType15
        self.model_TopicType13 = model_TopicType13 if model_TopicType13 is not None else set()
        self.model_TopicType17 = model_TopicType17 if model_TopicType17 is not None else set()
        self.model_TopicType19 = model_TopicType19 if model_TopicType19 is not None else set()
        self.model_TopicType34 = model_TopicType34
        self.model_TopicType21 = model_TopicType21
        self.model_TopicType25 = model_TopicType25
        self.model_TopicType69 = model_TopicType69
        self.model_TopicType72 = model_TopicType72
        self.model_TopicType75 = model_TopicType75
        self.model_TopicType61 = model_TopicType61
        self.model_TopicType78 = model_TopicType78
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def idType(self) -> str:
        return self.__idType

    @idType.setter
    def idType(self, idType: str):
        self.__idType = idType

    @property
    def locators(self) -> str:
        return self.__locators

    @locators.setter
    def locators(self, locators: str):
        self.__locators = locators

    @property
    def identifiers(self) -> str:
        return self.__identifiers

    @identifiers.setter
    def identifiers(self, identifiers: str):
        self.__identifiers = identifiers

    @property
    def model_TopicType6(self):
        return self.__model_TopicType6

    @model_TopicType6.setter
    def model_TopicType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType6", None)
        self.__model_TopicType6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_OccurrenceTypeConstraint"):
                    opp_val = getattr(item, "model_OccurrenceTypeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_OccurrenceTypeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_OccurrenceTypeConstraint"):
                    opp_val = getattr(item, "model_OccurrenceTypeConstraint", None)
                    
                    setattr(item, "model_OccurrenceTypeConstraint", self)
                    

    @property
    def model_TopicType0(self):
        return self.__model_TopicType0

    @model_TopicType0.setter
    def model_TopicType0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType0", None)
        self.__model_TopicType0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TopicType"):
                    opp_val = getattr(item, "model_TopicType", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TopicType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TopicType"):
                    opp_val = getattr(item, "model_TopicType", None)
                    
                    setattr(item, "model_TopicType", self)
                    

    @property
    def model_TopicType72(self):
        return self.__model_TopicType72

    @model_TopicType72.setter
    def model_TopicType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType72", None)
        self.__model_TopicType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoleCombinationConstraint71"):
                opp_val = getattr(old_value, "model_RoleCombinationConstraint71", None)
                if opp_val == self:
                    setattr(old_value, "model_RoleCombinationConstraint71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoleCombinationConstraint71"):
                opp_val = getattr(value, "model_RoleCombinationConstraint71", None)
                setattr(value, "model_RoleCombinationConstraint71", self)

    @property
    def model_TopicType25(self):
        return self.__model_TopicType25

    @model_TopicType25.setter
    def model_TopicType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType25", None)
        self.__model_TopicType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicMapSchema"):
                opp_val = getattr(old_value, "model_TopicMapSchema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicMapSchema"):
                opp_val = getattr(value, "model_TopicMapSchema", None)
                if opp_val is None:
                    setattr(value, "model_TopicMapSchema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TopicType69(self):
        return self.__model_TopicType69

    @model_TopicType69.setter
    def model_TopicType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType69", None)
        self.__model_TopicType69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoleCombinationConstraint68"):
                opp_val = getattr(old_value, "model_RoleCombinationConstraint68", None)
                if opp_val == self:
                    setattr(old_value, "model_RoleCombinationConstraint68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoleCombinationConstraint68"):
                opp_val = getattr(value, "model_RoleCombinationConstraint68", None)
                setattr(value, "model_RoleCombinationConstraint68", self)

    @property
    def model_TopicType78(self):
        return self.__model_TopicType78

    @model_TopicType78.setter
    def model_TopicType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType78", None)
        self.__model_TopicType78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoleCombinationConstraint77"):
                opp_val = getattr(old_value, "model_RoleCombinationConstraint77", None)
                if opp_val == self:
                    setattr(old_value, "model_RoleCombinationConstraint77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoleCombinationConstraint77"):
                opp_val = getattr(value, "model_RoleCombinationConstraint77", None)
                setattr(value, "model_RoleCombinationConstraint77", self)

    @property
    def model_TopicType61(self):
        return self.__model_TopicType61

    @model_TopicType61.setter
    def model_TopicType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType61", None)
        self.__model_TopicType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractTypedConstraint"):
                opp_val = getattr(old_value, "model_AbstractTypedConstraint", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractTypedConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractTypedConstraint"):
                opp_val = getattr(value, "model_AbstractTypedConstraint", None)
                setattr(value, "model_AbstractTypedConstraint", self)

    @property
    def model_TopicType21(self):
        return self.__model_TopicType21

    @model_TopicType21.setter
    def model_TopicType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType21", None)
        self.__model_TopicType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RolePlayerConstraint"):
                opp_val = getattr(old_value, "model_RolePlayerConstraint", None)
                if opp_val == self:
                    setattr(old_value, "model_RolePlayerConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RolePlayerConstraint"):
                opp_val = getattr(value, "model_RolePlayerConstraint", None)
                setattr(value, "model_RolePlayerConstraint", self)

    @property
    def model_TopicType8(self):
        return self.__model_TopicType8

    @model_TopicType8.setter
    def model_TopicType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType8", None)
        self.__model_TopicType8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_NameTypeConstraint"):
                    opp_val = getattr(item, "model_NameTypeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_NameTypeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_NameTypeConstraint"):
                    opp_val = getattr(item, "model_NameTypeConstraint", None)
                    
                    setattr(item, "model_NameTypeConstraint", self)
                    

    @property
    def model_TopicType4(self):
        return self.__model_TopicType4

    @model_TopicType4.setter
    def model_TopicType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType4", None)
        self.__model_TopicType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicType2"):
                opp_val = getattr(old_value, "model_TopicType2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicType2"):
                opp_val = getattr(value, "model_TopicType2", None)
                if opp_val is None:
                    setattr(value, "model_TopicType2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TopicType2(self):
        return self.__model_TopicType2

    @model_TopicType2.setter
    def model_TopicType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType2", None)
        self.__model_TopicType2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TopicType4"):
                    opp_val = getattr(item, "model_TopicType4", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TopicType4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TopicType4"):
                    opp_val = getattr(item, "model_TopicType4", None)
                    
                    setattr(item, "model_TopicType4", self)
                    

    @property
    def model_TopicType75(self):
        return self.__model_TopicType75

    @model_TopicType75.setter
    def model_TopicType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType75", None)
        self.__model_TopicType75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoleCombinationConstraint74"):
                opp_val = getattr(old_value, "model_RoleCombinationConstraint74", None)
                if opp_val == self:
                    setattr(old_value, "model_RoleCombinationConstraint74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoleCombinationConstraint74"):
                opp_val = getattr(value, "model_RoleCombinationConstraint74", None)
                setattr(value, "model_RoleCombinationConstraint74", self)

    @property
    def model_TopicType19(self):
        return self.__model_TopicType19

    @model_TopicType19.setter
    def model_TopicType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType19", None)
        self.__model_TopicType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ItemIdentifierConstraint"):
                    opp_val = getattr(item, "model_ItemIdentifierConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ItemIdentifierConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ItemIdentifierConstraint"):
                    opp_val = getattr(item, "model_ItemIdentifierConstraint", None)
                    
                    setattr(item, "model_ItemIdentifierConstraint", self)
                    

    @property
    def model_TopicType15(self):
        return self.__model_TopicType15

    @model_TopicType15.setter
    def model_TopicType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType15", None)
        self.__model_TopicType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicType13"):
                opp_val = getattr(old_value, "model_TopicType13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicType13"):
                opp_val = getattr(value, "model_TopicType13", None)
                if opp_val is None:
                    setattr(value, "model_TopicType13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TopicType34(self):
        return self.__model_TopicType34

    @model_TopicType34.setter
    def model_TopicType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType34", None)
        self.__model_TopicType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TypeNode"):
                opp_val = getattr(old_value, "model_TypeNode", None)
                if opp_val == self:
                    setattr(old_value, "model_TypeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TypeNode"):
                opp_val = getattr(value, "model_TypeNode", None)
                setattr(value, "model_TypeNode", self)

    @property
    def model_TopicType12(self):
        return self.__model_TopicType12

    @model_TopicType12.setter
    def model_TopicType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType12", None)
        self.__model_TopicType12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_SubjectLocatorConstraint"):
                    opp_val = getattr(item, "model_SubjectLocatorConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_SubjectLocatorConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_SubjectLocatorConstraint"):
                    opp_val = getattr(item, "model_SubjectLocatorConstraint", None)
                    
                    setattr(item, "model_SubjectLocatorConstraint", self)
                    

    @property
    def model_TopicType17(self):
        return self.__model_TopicType17

    @model_TopicType17.setter
    def model_TopicType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType17", None)
        self.__model_TopicType17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TopicReifiesConstraint"):
                    opp_val = getattr(item, "model_TopicReifiesConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TopicReifiesConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TopicReifiesConstraint"):
                    opp_val = getattr(item, "model_TopicReifiesConstraint", None)
                    
                    setattr(item, "model_TopicReifiesConstraint", self)
                    

    @property
    def model_TopicType10(self):
        return self.__model_TopicType10

    @model_TopicType10.setter
    def model_TopicType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType10", None)
        self.__model_TopicType10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_SubjectIdentifierConstraint"):
                    opp_val = getattr(item, "model_SubjectIdentifierConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_SubjectIdentifierConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_SubjectIdentifierConstraint"):
                    opp_val = getattr(item, "model_SubjectIdentifierConstraint", None)
                    
                    setattr(item, "model_SubjectIdentifierConstraint", self)
                    

    @property
    def model_TopicType(self):
        return self.__model_TopicType

    @model_TopicType.setter
    def model_TopicType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType", None)
        self.__model_TopicType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TopicType0"):
                opp_val = getattr(old_value, "model_TopicType0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TopicType0"):
                opp_val = getattr(value, "model_TopicType0", None)
                if opp_val is None:
                    setattr(value, "model_TopicType0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TopicType13(self):
        return self.__model_TopicType13

    @model_TopicType13.setter
    def model_TopicType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicType__model_TopicType13", None)
        self.__model_TopicType13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TopicType15"):
                    opp_val = getattr(item, "model_TopicType15", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TopicType15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TopicType15"):
                    opp_val = getattr(item, "model_TopicType15", None)
                    
                    setattr(item, "model_TopicType15", self)
                    

class model_AbstractConstraint(TMCLConstruct):

    pass
class model_TopicMapSchema(TMCLConstruct):

    def __init__(self, includes: str, baseLocator: str, name: str, version: str, schemaResource: str, model_TopicMapSchema: set["model_TopicType"] = None, model_TopicMapSchema27: set["model_AssociationTypeConstraint"] = None, model_TopicMapSchema29: set["model_MappingElement"] = None, model_TopicMapSchema59: "model_File" = None):
        self.includes = includes
        self.baseLocator = baseLocator
        self.name = name
        self.version = version
        self.schemaResource = schemaResource
        self.model_TopicMapSchema = model_TopicMapSchema if model_TopicMapSchema is not None else set()
        self.model_TopicMapSchema27 = model_TopicMapSchema27 if model_TopicMapSchema27 is not None else set()
        self.model_TopicMapSchema29 = model_TopicMapSchema29 if model_TopicMapSchema29 is not None else set()
        self.model_TopicMapSchema59 = model_TopicMapSchema59
        
    @property
    def includes(self) -> str:
        return self.__includes

    @includes.setter
    def includes(self, includes: str):
        self.__includes = includes

    @property
    def schemaResource(self) -> str:
        return self.__schemaResource

    @schemaResource.setter
    def schemaResource(self, schemaResource: str):
        self.__schemaResource = schemaResource

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
    def baseLocator(self) -> str:
        return self.__baseLocator

    @baseLocator.setter
    def baseLocator(self, baseLocator: str):
        self.__baseLocator = baseLocator

    @property
    def model_TopicMapSchema27(self):
        return self.__model_TopicMapSchema27

    @model_TopicMapSchema27.setter
    def model_TopicMapSchema27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicMapSchema__model_TopicMapSchema27", None)
        self.__model_TopicMapSchema27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_AssociationTypeConstraint"):
                    opp_val = getattr(item, "model_AssociationTypeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_AssociationTypeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_AssociationTypeConstraint"):
                    opp_val = getattr(item, "model_AssociationTypeConstraint", None)
                    
                    setattr(item, "model_AssociationTypeConstraint", self)
                    

    @property
    def model_TopicMapSchema(self):
        return self.__model_TopicMapSchema

    @model_TopicMapSchema.setter
    def model_TopicMapSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicMapSchema__model_TopicMapSchema", None)
        self.__model_TopicMapSchema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TopicType25"):
                    opp_val = getattr(item, "model_TopicType25", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TopicType25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TopicType25"):
                    opp_val = getattr(item, "model_TopicType25", None)
                    
                    setattr(item, "model_TopicType25", self)
                    

    @property
    def model_TopicMapSchema29(self):
        return self.__model_TopicMapSchema29

    @model_TopicMapSchema29.setter
    def model_TopicMapSchema29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicMapSchema__model_TopicMapSchema29", None)
        self.__model_TopicMapSchema29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MappingElement"):
                    opp_val = getattr(item, "model_MappingElement", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MappingElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MappingElement"):
                    opp_val = getattr(item, "model_MappingElement", None)
                    
                    setattr(item, "model_MappingElement", self)
                    

    @property
    def model_TopicMapSchema59(self):
        return self.__model_TopicMapSchema59

    @model_TopicMapSchema59.setter
    def model_TopicMapSchema59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TopicMapSchema__model_TopicMapSchema59", None)
        self.__model_TopicMapSchema59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_File58"):
                opp_val = getattr(old_value, "model_File58", None)
                if opp_val == self:
                    setattr(old_value, "model_File58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_File58"):
                opp_val = getattr(value, "model_File58", None)
                setattr(value, "model_File58", self)
