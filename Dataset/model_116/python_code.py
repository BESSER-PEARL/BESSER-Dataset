from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"


############################################
# Definition of Classes
############################################

class dsl_DefaultValue:

    pass
class dsl_AnnotationTypeMemberDeclaration:

    def __init__(self, id: str, dsl_AnnotationTypeMemberDeclaration: "dsl_AnnotationTypeBody" = None, dsl_AnnotationTypeMemberDeclaration473: "dsl_TypeBodyModifier" = None, dsl_AnnotationTypeMemberDeclaration476: "dsl_Type" = None, dsl_AnnotationTypeMemberDeclaration479: "dsl_DefaultValue" = None, dsl_AnnotationTypeMemberDeclaration481: "dsl_ClassOrInterfaceDeclaration" = None, dsl_AnnotationTypeMemberDeclaration484: "dsl_EnumDeclaration" = None, dsl_AnnotationTypeMemberDeclaration487: "dsl_AnnotationTypeDeclaration" = None, dsl_AnnotationTypeMemberDeclaration490: "dsl_FieldDeclaration" = None):
        self.id = id
        self.dsl_AnnotationTypeMemberDeclaration = dsl_AnnotationTypeMemberDeclaration
        self.dsl_AnnotationTypeMemberDeclaration473 = dsl_AnnotationTypeMemberDeclaration473
        self.dsl_AnnotationTypeMemberDeclaration476 = dsl_AnnotationTypeMemberDeclaration476
        self.dsl_AnnotationTypeMemberDeclaration479 = dsl_AnnotationTypeMemberDeclaration479
        self.dsl_AnnotationTypeMemberDeclaration481 = dsl_AnnotationTypeMemberDeclaration481
        self.dsl_AnnotationTypeMemberDeclaration484 = dsl_AnnotationTypeMemberDeclaration484
        self.dsl_AnnotationTypeMemberDeclaration487 = dsl_AnnotationTypeMemberDeclaration487
        self.dsl_AnnotationTypeMemberDeclaration490 = dsl_AnnotationTypeMemberDeclaration490
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_AnnotationTypeMemberDeclaration473(self):
        return self.__dsl_AnnotationTypeMemberDeclaration473

    @dsl_AnnotationTypeMemberDeclaration473.setter
    def dsl_AnnotationTypeMemberDeclaration473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration473", None)
        self.__dsl_AnnotationTypeMemberDeclaration473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeBodyModifier474"):
                opp_val = getattr(old_value, "dsl_TypeBodyModifier474", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeBodyModifier474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeBodyModifier474"):
                opp_val = getattr(value, "dsl_TypeBodyModifier474", None)
                setattr(value, "dsl_TypeBodyModifier474", self)

    @property
    def dsl_AnnotationTypeMemberDeclaration476(self):
        return self.__dsl_AnnotationTypeMemberDeclaration476

    @dsl_AnnotationTypeMemberDeclaration476.setter
    def dsl_AnnotationTypeMemberDeclaration476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration476", None)
        self.__dsl_AnnotationTypeMemberDeclaration476 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type477"):
                opp_val = getattr(old_value, "dsl_Type477", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type477"):
                opp_val = getattr(value, "dsl_Type477", None)
                setattr(value, "dsl_Type477", self)

    @property
    def dsl_AnnotationTypeMemberDeclaration479(self):
        return self.__dsl_AnnotationTypeMemberDeclaration479

    @dsl_AnnotationTypeMemberDeclaration479.setter
    def dsl_AnnotationTypeMemberDeclaration479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration479", None)
        self.__dsl_AnnotationTypeMemberDeclaration479 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_DefaultValue"):
                opp_val = getattr(old_value, "dsl_DefaultValue", None)
                if opp_val == self:
                    setattr(old_value, "dsl_DefaultValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_DefaultValue"):
                opp_val = getattr(value, "dsl_DefaultValue", None)
                setattr(value, "dsl_DefaultValue", self)

    @property
    def dsl_AnnotationTypeMemberDeclaration490(self):
        return self.__dsl_AnnotationTypeMemberDeclaration490

    @dsl_AnnotationTypeMemberDeclaration490.setter
    def dsl_AnnotationTypeMemberDeclaration490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration490", None)
        self.__dsl_AnnotationTypeMemberDeclaration490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FieldDeclaration491"):
                opp_val = getattr(old_value, "dsl_FieldDeclaration491", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FieldDeclaration491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FieldDeclaration491"):
                opp_val = getattr(value, "dsl_FieldDeclaration491", None)
                setattr(value, "dsl_FieldDeclaration491", self)

    @property
    def dsl_AnnotationTypeMemberDeclaration487(self):
        return self.__dsl_AnnotationTypeMemberDeclaration487

    @dsl_AnnotationTypeMemberDeclaration487.setter
    def dsl_AnnotationTypeMemberDeclaration487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration487", None)
        self.__dsl_AnnotationTypeMemberDeclaration487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeDeclaration488"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeDeclaration488", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeDeclaration488", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeDeclaration488"):
                opp_val = getattr(value, "dsl_AnnotationTypeDeclaration488", None)
                setattr(value, "dsl_AnnotationTypeDeclaration488", self)

    @property
    def dsl_AnnotationTypeMemberDeclaration484(self):
        return self.__dsl_AnnotationTypeMemberDeclaration484

    @dsl_AnnotationTypeMemberDeclaration484.setter
    def dsl_AnnotationTypeMemberDeclaration484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration484", None)
        self.__dsl_AnnotationTypeMemberDeclaration484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_EnumDeclaration485"):
                opp_val = getattr(old_value, "dsl_EnumDeclaration485", None)
                if opp_val == self:
                    setattr(old_value, "dsl_EnumDeclaration485", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_EnumDeclaration485"):
                opp_val = getattr(value, "dsl_EnumDeclaration485", None)
                setattr(value, "dsl_EnumDeclaration485", self)

    @property
    def dsl_AnnotationTypeMemberDeclaration(self):
        return self.__dsl_AnnotationTypeMemberDeclaration

    @dsl_AnnotationTypeMemberDeclaration.setter
    def dsl_AnnotationTypeMemberDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration", None)
        self.__dsl_AnnotationTypeMemberDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeBody471"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeBody471", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeBody471"):
                opp_val = getattr(value, "dsl_AnnotationTypeBody471", None)
                if opp_val is None:
                    setattr(value, "dsl_AnnotationTypeBody471", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_AnnotationTypeMemberDeclaration481(self):
        return self.__dsl_AnnotationTypeMemberDeclaration481

    @dsl_AnnotationTypeMemberDeclaration481.setter
    def dsl_AnnotationTypeMemberDeclaration481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeMemberDeclaration__dsl_AnnotationTypeMemberDeclaration481", None)
        self.__dsl_AnnotationTypeMemberDeclaration481 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceDeclaration482"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceDeclaration482", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceDeclaration482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceDeclaration482"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceDeclaration482", None)
                setattr(value, "dsl_ClassOrInterfaceDeclaration482", self)

class dsl_AnnotationTypeBody:

    pass
class dsl_MemberValueArrayInitializer:

    pass
class DefaultValue:

    pass
class dsl_MemberValuePair:

    def __init__(self, id: str, dsl_MemberValuePair: "dsl_MemberValuePairs" = None, dsl_MemberValuePair455: "dsl_MemberValue" = None):
        self.id = id
        self.dsl_MemberValuePair = dsl_MemberValuePair
        self.dsl_MemberValuePair455 = dsl_MemberValuePair455
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_MemberValuePair(self):
        return self.__dsl_MemberValuePair

    @dsl_MemberValuePair.setter
    def dsl_MemberValuePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MemberValuePair__dsl_MemberValuePair", None)
        self.__dsl_MemberValuePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MemberValuePairs453"):
                opp_val = getattr(old_value, "dsl_MemberValuePairs453", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MemberValuePairs453"):
                opp_val = getattr(value, "dsl_MemberValuePairs453", None)
                if opp_val is None:
                    setattr(value, "dsl_MemberValuePairs453", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_MemberValuePair455(self):
        return self.__dsl_MemberValuePair455

    @dsl_MemberValuePair455.setter
    def dsl_MemberValuePair455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MemberValuePair__dsl_MemberValuePair455", None)
        self.__dsl_MemberValuePair455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MemberValue456"):
                opp_val = getattr(old_value, "dsl_MemberValue456", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MemberValue456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MemberValue456"):
                opp_val = getattr(value, "dsl_MemberValue456", None)
                setattr(value, "dsl_MemberValue456", self)

class dsl_MemberValue(DefaultValue):

    pass
class dsl_MemberValuePairs:

    pass
class dsl_Annotation:

    pass
class dsl_StatementExpressionList:

    pass
class dsl_ForUpdate:

    pass
class dsl_ForInit:

    pass
class dsl_SwitchLabel:

    def __init__(self, defaultOp: str, dsl_SwitchLabel: "dsl_SwitchStatement" = None, dsl_SwitchLabel384: "dsl_Expression" = None):
        self.defaultOp = defaultOp
        self.dsl_SwitchLabel = dsl_SwitchLabel
        self.dsl_SwitchLabel384 = dsl_SwitchLabel384
        
    @property
    def defaultOp(self) -> str:
        return self.__defaultOp

    @defaultOp.setter
    def defaultOp(self, defaultOp: str):
        self.__defaultOp = defaultOp

    @property
    def dsl_SwitchLabel(self):
        return self.__dsl_SwitchLabel

    @dsl_SwitchLabel.setter
    def dsl_SwitchLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_SwitchLabel__dsl_SwitchLabel", None)
        self.__dsl_SwitchLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SwitchStatement379"):
                opp_val = getattr(old_value, "dsl_SwitchStatement379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SwitchStatement379"):
                opp_val = getattr(value, "dsl_SwitchStatement379", None)
                if opp_val is None:
                    setattr(value, "dsl_SwitchStatement379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_SwitchLabel384(self):
        return self.__dsl_SwitchLabel384

    @dsl_SwitchLabel384.setter
    def dsl_SwitchLabel384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_SwitchLabel__dsl_SwitchLabel384", None)
        self.__dsl_SwitchLabel384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression385"):
                opp_val = getattr(old_value, "dsl_Expression385", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression385"):
                opp_val = getattr(value, "dsl_Expression385", None)
                setattr(value, "dsl_Expression385", self)

class dsl_LocalVariableDeclaration:

    def __init__(self, finality: str, dsl_LocalVariableDeclaration: "dsl_BlockStatement" = None, dsl_LocalVariableDeclaration358: "dsl_Type" = None, dsl_LocalVariableDeclaration361: set["dsl_VariableDeclarator"] = None, dsl_LocalVariableDeclaration416: "dsl_ForInit" = None):
        self.finality = finality
        self.dsl_LocalVariableDeclaration = dsl_LocalVariableDeclaration
        self.dsl_LocalVariableDeclaration358 = dsl_LocalVariableDeclaration358
        self.dsl_LocalVariableDeclaration361 = dsl_LocalVariableDeclaration361 if dsl_LocalVariableDeclaration361 is not None else set()
        self.dsl_LocalVariableDeclaration416 = dsl_LocalVariableDeclaration416
        
    @property
    def finality(self) -> str:
        return self.__finality

    @finality.setter
    def finality(self, finality: str):
        self.__finality = finality

    @property
    def dsl_LocalVariableDeclaration358(self):
        return self.__dsl_LocalVariableDeclaration358

    @dsl_LocalVariableDeclaration358.setter
    def dsl_LocalVariableDeclaration358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LocalVariableDeclaration__dsl_LocalVariableDeclaration358", None)
        self.__dsl_LocalVariableDeclaration358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type359"):
                opp_val = getattr(old_value, "dsl_Type359", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type359"):
                opp_val = getattr(value, "dsl_Type359", None)
                setattr(value, "dsl_Type359", self)

    @property
    def dsl_LocalVariableDeclaration(self):
        return self.__dsl_LocalVariableDeclaration

    @dsl_LocalVariableDeclaration.setter
    def dsl_LocalVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LocalVariableDeclaration__dsl_LocalVariableDeclaration", None)
        self.__dsl_LocalVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_BlockStatement350"):
                opp_val = getattr(old_value, "dsl_BlockStatement350", None)
                if opp_val == self:
                    setattr(old_value, "dsl_BlockStatement350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_BlockStatement350"):
                opp_val = getattr(value, "dsl_BlockStatement350", None)
                setattr(value, "dsl_BlockStatement350", self)

    @property
    def dsl_LocalVariableDeclaration361(self):
        return self.__dsl_LocalVariableDeclaration361

    @dsl_LocalVariableDeclaration361.setter
    def dsl_LocalVariableDeclaration361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LocalVariableDeclaration__dsl_LocalVariableDeclaration361", None)
        self.__dsl_LocalVariableDeclaration361 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_VariableDeclarator362"):
                    opp_val = getattr(item, "dsl_VariableDeclarator362", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_VariableDeclarator362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_VariableDeclarator362"):
                    opp_val = getattr(item, "dsl_VariableDeclarator362", None)
                    
                    setattr(item, "dsl_VariableDeclarator362", self)
                    

    @property
    def dsl_LocalVariableDeclaration416(self):
        return self.__dsl_LocalVariableDeclaration416

    @dsl_LocalVariableDeclaration416.setter
    def dsl_LocalVariableDeclaration416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LocalVariableDeclaration__dsl_LocalVariableDeclaration416", None)
        self.__dsl_LocalVariableDeclaration416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ForInit415"):
                opp_val = getattr(old_value, "dsl_ForInit415", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ForInit415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ForInit415"):
                opp_val = getattr(value, "dsl_ForInit415", None)
                setattr(value, "dsl_ForInit415", self)

class dsl_TryStatement:

    pass
class dsl_SynchronizedStatement:

    pass
class dsl_ThrowStatement:

    pass
class dsl_ReturnStatement:

    pass
class dsl_ForStatement:

    def __init__(self, id: str, dsl_ForStatement: "dsl_Statement" = None, dsl_ForStatement399: "dsl_Type" = None, dsl_ForStatement402: "dsl_Expression" = None, dsl_ForStatement405: "dsl_ForInit" = None, dsl_ForStatement407: "dsl_Expression" = None, dsl_ForStatement410: "dsl_ForUpdate" = None, dsl_ForStatement412: "dsl_Statement" = None):
        self.id = id
        self.dsl_ForStatement = dsl_ForStatement
        self.dsl_ForStatement399 = dsl_ForStatement399
        self.dsl_ForStatement402 = dsl_ForStatement402
        self.dsl_ForStatement405 = dsl_ForStatement405
        self.dsl_ForStatement407 = dsl_ForStatement407
        self.dsl_ForStatement410 = dsl_ForStatement410
        self.dsl_ForStatement412 = dsl_ForStatement412
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_ForStatement405(self):
        return self.__dsl_ForStatement405

    @dsl_ForStatement405.setter
    def dsl_ForStatement405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement405", None)
        self.__dsl_ForStatement405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ForInit"):
                opp_val = getattr(old_value, "dsl_ForInit", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ForInit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ForInit"):
                opp_val = getattr(value, "dsl_ForInit", None)
                setattr(value, "dsl_ForInit", self)

    @property
    def dsl_ForStatement412(self):
        return self.__dsl_ForStatement412

    @dsl_ForStatement412.setter
    def dsl_ForStatement412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement412", None)
        self.__dsl_ForStatement412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement413"):
                opp_val = getattr(old_value, "dsl_Statement413", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement413"):
                opp_val = getattr(value, "dsl_Statement413", None)
                setattr(value, "dsl_Statement413", self)

    @property
    def dsl_ForStatement399(self):
        return self.__dsl_ForStatement399

    @dsl_ForStatement399.setter
    def dsl_ForStatement399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement399", None)
        self.__dsl_ForStatement399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type400"):
                opp_val = getattr(old_value, "dsl_Type400", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type400"):
                opp_val = getattr(value, "dsl_Type400", None)
                setattr(value, "dsl_Type400", self)

    @property
    def dsl_ForStatement(self):
        return self.__dsl_ForStatement

    @dsl_ForStatement.setter
    def dsl_ForStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement", None)
        self.__dsl_ForStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement324"):
                opp_val = getattr(old_value, "dsl_Statement324", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement324"):
                opp_val = getattr(value, "dsl_Statement324", None)
                setattr(value, "dsl_Statement324", self)

    @property
    def dsl_ForStatement410(self):
        return self.__dsl_ForStatement410

    @dsl_ForStatement410.setter
    def dsl_ForStatement410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement410", None)
        self.__dsl_ForStatement410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ForUpdate"):
                opp_val = getattr(old_value, "dsl_ForUpdate", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ForUpdate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ForUpdate"):
                opp_val = getattr(value, "dsl_ForUpdate", None)
                setattr(value, "dsl_ForUpdate", self)

    @property
    def dsl_ForStatement407(self):
        return self.__dsl_ForStatement407

    @dsl_ForStatement407.setter
    def dsl_ForStatement407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement407", None)
        self.__dsl_ForStatement407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression408"):
                opp_val = getattr(old_value, "dsl_Expression408", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression408"):
                opp_val = getattr(value, "dsl_Expression408", None)
                setattr(value, "dsl_Expression408", self)

    @property
    def dsl_ForStatement402(self):
        return self.__dsl_ForStatement402

    @dsl_ForStatement402.setter
    def dsl_ForStatement402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ForStatement__dsl_ForStatement402", None)
        self.__dsl_ForStatement402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression403"):
                opp_val = getattr(old_value, "dsl_Expression403", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression403"):
                opp_val = getattr(value, "dsl_Expression403", None)
                setattr(value, "dsl_Expression403", self)

class dsl_DoStatement:

    pass
class dsl_WhileStatement:

    pass
class dsl_IfStatement:

    pass
class dsl_SwitchStatement:

    pass
class dsl_ContinueStatement:

    def __init__(self, id: str, dsl_ContinueStatement: "dsl_Statement" = None):
        self.id = id
        self.dsl_ContinueStatement = dsl_ContinueStatement
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_ContinueStatement(self):
        return self.__dsl_ContinueStatement

    @dsl_ContinueStatement.setter
    def dsl_ContinueStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ContinueStatement__dsl_ContinueStatement", None)
        self.__dsl_ContinueStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement328"):
                opp_val = getattr(old_value, "dsl_Statement328", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement328"):
                opp_val = getattr(value, "dsl_Statement328", None)
                setattr(value, "dsl_Statement328", self)

class dsl_BreakStatement:

    def __init__(self, id: str, dsl_BreakStatement: "dsl_Statement" = None):
        self.id = id
        self.dsl_BreakStatement = dsl_BreakStatement
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_BreakStatement(self):
        return self.__dsl_BreakStatement

    @dsl_BreakStatement.setter
    def dsl_BreakStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_BreakStatement__dsl_BreakStatement", None)
        self.__dsl_BreakStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement326"):
                opp_val = getattr(old_value, "dsl_Statement326", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement326"):
                opp_val = getattr(value, "dsl_Statement326", None)
                setattr(value, "dsl_Statement326", self)

class dsl_AssertStatement:

    pass
class dsl_LabeledStatement:

    def __init__(self, id: str, dsl_LabeledStatement: "dsl_Statement" = None, dsl_LabeledStatement344: "dsl_Statement" = None):
        self.id = id
        self.dsl_LabeledStatement = dsl_LabeledStatement
        self.dsl_LabeledStatement344 = dsl_LabeledStatement344
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_LabeledStatement344(self):
        return self.__dsl_LabeledStatement344

    @dsl_LabeledStatement344.setter
    def dsl_LabeledStatement344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LabeledStatement__dsl_LabeledStatement344", None)
        self.__dsl_LabeledStatement344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement345"):
                opp_val = getattr(old_value, "dsl_Statement345", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement345"):
                opp_val = getattr(value, "dsl_Statement345", None)
                setattr(value, "dsl_Statement345", self)

    @property
    def dsl_LabeledStatement(self):
        return self.__dsl_LabeledStatement

    @dsl_LabeledStatement.setter
    def dsl_LabeledStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LabeledStatement__dsl_LabeledStatement", None)
        self.__dsl_LabeledStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement307"):
                opp_val = getattr(old_value, "dsl_Statement307", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement307"):
                opp_val = getattr(value, "dsl_Statement307", None)
                setattr(value, "dsl_Statement307", self)

class dsl_StatementExpression:

    def __init__(self, plusOp: str, minOp: str, assignOp: str, dsl_StatementExpression: "dsl_Statement" = None, dsl_StatementExpression364: "dsl_PreIncrementExpression" = None, dsl_StatementExpression367: "dsl_PreDecrementExpression" = None, dsl_StatementExpression370: "dsl_PrimaryExpression" = None, dsl_StatementExpression373: "dsl_Expression" = None, dsl_StatementExpression421: "dsl_StatementExpressionList" = None):
        self.plusOp = plusOp
        self.minOp = minOp
        self.assignOp = assignOp
        self.dsl_StatementExpression = dsl_StatementExpression
        self.dsl_StatementExpression364 = dsl_StatementExpression364
        self.dsl_StatementExpression367 = dsl_StatementExpression367
        self.dsl_StatementExpression370 = dsl_StatementExpression370
        self.dsl_StatementExpression373 = dsl_StatementExpression373
        self.dsl_StatementExpression421 = dsl_StatementExpression421
        
    @property
    def assignOp(self) -> str:
        return self.__assignOp

    @assignOp.setter
    def assignOp(self, assignOp: str):
        self.__assignOp = assignOp

    @property
    def plusOp(self) -> str:
        return self.__plusOp

    @plusOp.setter
    def plusOp(self, plusOp: str):
        self.__plusOp = plusOp

    @property
    def minOp(self) -> str:
        return self.__minOp

    @minOp.setter
    def minOp(self, minOp: str):
        self.__minOp = minOp

    @property
    def dsl_StatementExpression373(self):
        return self.__dsl_StatementExpression373

    @dsl_StatementExpression373.setter
    def dsl_StatementExpression373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_StatementExpression__dsl_StatementExpression373", None)
        self.__dsl_StatementExpression373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression374"):
                opp_val = getattr(old_value, "dsl_Expression374", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression374"):
                opp_val = getattr(value, "dsl_Expression374", None)
                setattr(value, "dsl_Expression374", self)

    @property
    def dsl_StatementExpression367(self):
        return self.__dsl_StatementExpression367

    @dsl_StatementExpression367.setter
    def dsl_StatementExpression367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_StatementExpression__dsl_StatementExpression367", None)
        self.__dsl_StatementExpression367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PreDecrementExpression368"):
                opp_val = getattr(old_value, "dsl_PreDecrementExpression368", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PreDecrementExpression368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PreDecrementExpression368"):
                opp_val = getattr(value, "dsl_PreDecrementExpression368", None)
                setattr(value, "dsl_PreDecrementExpression368", self)

    @property
    def dsl_StatementExpression421(self):
        return self.__dsl_StatementExpression421

    @dsl_StatementExpression421.setter
    def dsl_StatementExpression421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_StatementExpression__dsl_StatementExpression421", None)
        self.__dsl_StatementExpression421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_StatementExpressionList420"):
                opp_val = getattr(old_value, "dsl_StatementExpressionList420", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_StatementExpressionList420"):
                opp_val = getattr(value, "dsl_StatementExpressionList420", None)
                if opp_val is None:
                    setattr(value, "dsl_StatementExpressionList420", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_StatementExpression(self):
        return self.__dsl_StatementExpression

    @dsl_StatementExpression.setter
    def dsl_StatementExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_StatementExpression__dsl_StatementExpression", None)
        self.__dsl_StatementExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement314"):
                opp_val = getattr(old_value, "dsl_Statement314", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement314"):
                opp_val = getattr(value, "dsl_Statement314", None)
                setattr(value, "dsl_Statement314", self)

    @property
    def dsl_StatementExpression364(self):
        return self.__dsl_StatementExpression364

    @dsl_StatementExpression364.setter
    def dsl_StatementExpression364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_StatementExpression__dsl_StatementExpression364", None)
        self.__dsl_StatementExpression364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PreIncrementExpression365"):
                opp_val = getattr(old_value, "dsl_PreIncrementExpression365", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PreIncrementExpression365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PreIncrementExpression365"):
                opp_val = getattr(value, "dsl_PreIncrementExpression365", None)
                setattr(value, "dsl_PreIncrementExpression365", self)

    @property
    def dsl_StatementExpression370(self):
        return self.__dsl_StatementExpression370

    @dsl_StatementExpression370.setter
    def dsl_StatementExpression370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_StatementExpression__dsl_StatementExpression370", None)
        self.__dsl_StatementExpression370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryExpression371"):
                opp_val = getattr(old_value, "dsl_PrimaryExpression371", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryExpression371", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryExpression371"):
                opp_val = getattr(value, "dsl_PrimaryExpression371", None)
                setattr(value, "dsl_PrimaryExpression371", self)

class dsl_ArrayDimsAndInits:

    def __init__(self, squareBrackets: str, dsl_ArrayDimsAndInits: "dsl_AllocationExpression" = None, dsl_ArrayDimsAndInits301: set["dsl_Expression"] = None, dsl_ArrayDimsAndInits304: "dsl_ArrayInitializer" = None):
        self.squareBrackets = squareBrackets
        self.dsl_ArrayDimsAndInits = dsl_ArrayDimsAndInits
        self.dsl_ArrayDimsAndInits301 = dsl_ArrayDimsAndInits301 if dsl_ArrayDimsAndInits301 is not None else set()
        self.dsl_ArrayDimsAndInits304 = dsl_ArrayDimsAndInits304
        
    @property
    def squareBrackets(self) -> str:
        return self.__squareBrackets

    @squareBrackets.setter
    def squareBrackets(self, squareBrackets: str):
        self.__squareBrackets = squareBrackets

    @property
    def dsl_ArrayDimsAndInits301(self):
        return self.__dsl_ArrayDimsAndInits301

    @dsl_ArrayDimsAndInits301.setter
    def dsl_ArrayDimsAndInits301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ArrayDimsAndInits__dsl_ArrayDimsAndInits301", None)
        self.__dsl_ArrayDimsAndInits301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Expression302"):
                    opp_val = getattr(item, "dsl_Expression302", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Expression302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Expression302"):
                    opp_val = getattr(item, "dsl_Expression302", None)
                    
                    setattr(item, "dsl_Expression302", self)
                    

    @property
    def dsl_ArrayDimsAndInits304(self):
        return self.__dsl_ArrayDimsAndInits304

    @dsl_ArrayDimsAndInits304.setter
    def dsl_ArrayDimsAndInits304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ArrayDimsAndInits__dsl_ArrayDimsAndInits304", None)
        self.__dsl_ArrayDimsAndInits304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ArrayInitializer305"):
                opp_val = getattr(old_value, "dsl_ArrayInitializer305", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ArrayInitializer305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ArrayInitializer305"):
                opp_val = getattr(value, "dsl_ArrayInitializer305", None)
                setattr(value, "dsl_ArrayInitializer305", self)

    @property
    def dsl_ArrayDimsAndInits(self):
        return self.__dsl_ArrayDimsAndInits

    @dsl_ArrayDimsAndInits.setter
    def dsl_ArrayDimsAndInits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ArrayDimsAndInits__dsl_ArrayDimsAndInits", None)
        self.__dsl_ArrayDimsAndInits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AllocationExpression287"):
                opp_val = getattr(old_value, "dsl_AllocationExpression287", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AllocationExpression287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AllocationExpression287"):
                opp_val = getattr(value, "dsl_AllocationExpression287", None)
                setattr(value, "dsl_AllocationExpression287", self)

class dsl_BooleanLiteral:

    def __init__(self, truthiness: str, dsl_BooleanLiteral: "dsl_Literal" = None):
        self.truthiness = truthiness
        self.dsl_BooleanLiteral = dsl_BooleanLiteral
        
    @property
    def truthiness(self) -> str:
        return self.__truthiness

    @truthiness.setter
    def truthiness(self, truthiness: str):
        self.__truthiness = truthiness

    @property
    def dsl_BooleanLiteral(self):
        return self.__dsl_BooleanLiteral

    @dsl_BooleanLiteral.setter
    def dsl_BooleanLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_BooleanLiteral__dsl_BooleanLiteral", None)
        self.__dsl_BooleanLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Literal280"):
                opp_val = getattr(old_value, "dsl_Literal280", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Literal280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Literal280"):
                opp_val = getattr(value, "dsl_Literal280", None)
                setattr(value, "dsl_Literal280", self)

class dsl_ArgumentList:

    pass
class dsl_IntegerLiteral:

    def __init__(self, zero: str, one: str, dsl_IntegerLiteral: "dsl_SignedIntLiteral" = None, dsl_IntegerLiteral266: "dsl_UnsignedIntLiteral" = None, dsl_IntegerLiteral275: "dsl_Literal" = None):
        self.zero = zero
        self.one = one
        self.dsl_IntegerLiteral = dsl_IntegerLiteral
        self.dsl_IntegerLiteral266 = dsl_IntegerLiteral266
        self.dsl_IntegerLiteral275 = dsl_IntegerLiteral275
        
    @property
    def zero(self) -> str:
        return self.__zero

    @zero.setter
    def zero(self, zero: str):
        self.__zero = zero

    @property
    def one(self) -> str:
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one

    @property
    def dsl_IntegerLiteral275(self):
        return self.__dsl_IntegerLiteral275

    @dsl_IntegerLiteral275.setter
    def dsl_IntegerLiteral275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_IntegerLiteral__dsl_IntegerLiteral275", None)
        self.__dsl_IntegerLiteral275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Literal274"):
                opp_val = getattr(old_value, "dsl_Literal274", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Literal274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Literal274"):
                opp_val = getattr(value, "dsl_Literal274", None)
                setattr(value, "dsl_Literal274", self)

    @property
    def dsl_IntegerLiteral(self):
        return self.__dsl_IntegerLiteral

    @dsl_IntegerLiteral.setter
    def dsl_IntegerLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_IntegerLiteral__dsl_IntegerLiteral", None)
        self.__dsl_IntegerLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SignedIntLiteral264"):
                opp_val = getattr(old_value, "dsl_SignedIntLiteral264", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SignedIntLiteral264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SignedIntLiteral264"):
                opp_val = getattr(value, "dsl_SignedIntLiteral264", None)
                setattr(value, "dsl_SignedIntLiteral264", self)

    @property
    def dsl_IntegerLiteral266(self):
        return self.__dsl_IntegerLiteral266

    @dsl_IntegerLiteral266.setter
    def dsl_IntegerLiteral266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_IntegerLiteral__dsl_IntegerLiteral266", None)
        self.__dsl_IntegerLiteral266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnsignedIntLiteral267"):
                opp_val = getattr(old_value, "dsl_UnsignedIntLiteral267", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnsignedIntLiteral267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnsignedIntLiteral267"):
                opp_val = getattr(value, "dsl_UnsignedIntLiteral267", None)
                setattr(value, "dsl_UnsignedIntLiteral267", self)

class dsl_SignedIntLiteral:

    def __init__(self, bitWidth: int, dsl_SignedIntLiteral264: "dsl_IntegerLiteral" = None, dsl_SignedIntLiteral: "dsl_BaseLiteral" = None):
        self.bitWidth = bitWidth
        self.dsl_SignedIntLiteral264 = dsl_SignedIntLiteral264
        self.dsl_SignedIntLiteral = dsl_SignedIntLiteral
        
    @property
    def bitWidth(self) -> int:
        return self.__bitWidth

    @bitWidth.setter
    def bitWidth(self, bitWidth: int):
        self.__bitWidth = bitWidth

    @property
    def dsl_SignedIntLiteral(self):
        return self.__dsl_SignedIntLiteral

    @dsl_SignedIntLiteral.setter
    def dsl_SignedIntLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_SignedIntLiteral__dsl_SignedIntLiteral", None)
        self.__dsl_SignedIntLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_BaseLiteral262"):
                opp_val = getattr(old_value, "dsl_BaseLiteral262", None)
                if opp_val == self:
                    setattr(old_value, "dsl_BaseLiteral262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_BaseLiteral262"):
                opp_val = getattr(value, "dsl_BaseLiteral262", None)
                setattr(value, "dsl_BaseLiteral262", self)

    @property
    def dsl_SignedIntLiteral264(self):
        return self.__dsl_SignedIntLiteral264

    @dsl_SignedIntLiteral264.setter
    def dsl_SignedIntLiteral264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_SignedIntLiteral__dsl_SignedIntLiteral264", None)
        self.__dsl_SignedIntLiteral264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_IntegerLiteral"):
                opp_val = getattr(old_value, "dsl_IntegerLiteral", None)
                if opp_val == self:
                    setattr(old_value, "dsl_IntegerLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_IntegerLiteral"):
                opp_val = getattr(value, "dsl_IntegerLiteral", None)
                setattr(value, "dsl_IntegerLiteral", self)

class dsl_UnsignedIntLiteral:

    def __init__(self, sign: str, dsl_UnsignedIntLiteral267: "dsl_IntegerLiteral" = None, dsl_UnsignedIntLiteral: "dsl_DecimalNumber" = None, dsl_UnsignedIntLiteral260: "dsl_BaseLiteral" = None):
        self.sign = sign
        self.dsl_UnsignedIntLiteral267 = dsl_UnsignedIntLiteral267
        self.dsl_UnsignedIntLiteral = dsl_UnsignedIntLiteral
        self.dsl_UnsignedIntLiteral260 = dsl_UnsignedIntLiteral260
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def dsl_UnsignedIntLiteral267(self):
        return self.__dsl_UnsignedIntLiteral267

    @dsl_UnsignedIntLiteral267.setter
    def dsl_UnsignedIntLiteral267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnsignedIntLiteral__dsl_UnsignedIntLiteral267", None)
        self.__dsl_UnsignedIntLiteral267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_IntegerLiteral266"):
                opp_val = getattr(old_value, "dsl_IntegerLiteral266", None)
                if opp_val == self:
                    setattr(old_value, "dsl_IntegerLiteral266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_IntegerLiteral266"):
                opp_val = getattr(value, "dsl_IntegerLiteral266", None)
                setattr(value, "dsl_IntegerLiteral266", self)

    @property
    def dsl_UnsignedIntLiteral(self):
        return self.__dsl_UnsignedIntLiteral

    @dsl_UnsignedIntLiteral.setter
    def dsl_UnsignedIntLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnsignedIntLiteral__dsl_UnsignedIntLiteral", None)
        self.__dsl_UnsignedIntLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_DecimalNumber"):
                opp_val = getattr(old_value, "dsl_DecimalNumber", None)
                if opp_val == self:
                    setattr(old_value, "dsl_DecimalNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_DecimalNumber"):
                opp_val = getattr(value, "dsl_DecimalNumber", None)
                setattr(value, "dsl_DecimalNumber", self)

    @property
    def dsl_UnsignedIntLiteral260(self):
        return self.__dsl_UnsignedIntLiteral260

    @dsl_UnsignedIntLiteral260.setter
    def dsl_UnsignedIntLiteral260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnsignedIntLiteral__dsl_UnsignedIntLiteral260", None)
        self.__dsl_UnsignedIntLiteral260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_BaseLiteral"):
                opp_val = getattr(old_value, "dsl_BaseLiteral", None)
                if opp_val == self:
                    setattr(old_value, "dsl_BaseLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_BaseLiteral"):
                opp_val = getattr(value, "dsl_BaseLiteral", None)
                setattr(value, "dsl_BaseLiteral", self)

class dsl_FloatLiteral:

    def __init__(self, digits: str, dsl_FloatLiteral: "dsl_DecimalNumber" = None, dsl_FloatLiteral271: "dsl_DecimalNumber" = None, dsl_FloatLiteral278: "dsl_Literal" = None):
        self.digits = digits
        self.dsl_FloatLiteral = dsl_FloatLiteral
        self.dsl_FloatLiteral271 = dsl_FloatLiteral271
        self.dsl_FloatLiteral278 = dsl_FloatLiteral278
        
    @property
    def digits(self) -> str:
        return self.__digits

    @digits.setter
    def digits(self, digits: str):
        self.__digits = digits

    @property
    def dsl_FloatLiteral278(self):
        return self.__dsl_FloatLiteral278

    @dsl_FloatLiteral278.setter
    def dsl_FloatLiteral278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FloatLiteral__dsl_FloatLiteral278", None)
        self.__dsl_FloatLiteral278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Literal277"):
                opp_val = getattr(old_value, "dsl_Literal277", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Literal277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Literal277"):
                opp_val = getattr(value, "dsl_Literal277", None)
                setattr(value, "dsl_Literal277", self)

    @property
    def dsl_FloatLiteral271(self):
        return self.__dsl_FloatLiteral271

    @dsl_FloatLiteral271.setter
    def dsl_FloatLiteral271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FloatLiteral__dsl_FloatLiteral271", None)
        self.__dsl_FloatLiteral271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_DecimalNumber272"):
                opp_val = getattr(old_value, "dsl_DecimalNumber272", None)
                if opp_val == self:
                    setattr(old_value, "dsl_DecimalNumber272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_DecimalNumber272"):
                opp_val = getattr(value, "dsl_DecimalNumber272", None)
                setattr(value, "dsl_DecimalNumber272", self)

    @property
    def dsl_FloatLiteral(self):
        return self.__dsl_FloatLiteral

    @dsl_FloatLiteral.setter
    def dsl_FloatLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FloatLiteral__dsl_FloatLiteral", None)
        self.__dsl_FloatLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_DecimalNumber269"):
                opp_val = getattr(old_value, "dsl_DecimalNumber269", None)
                if opp_val == self:
                    setattr(old_value, "dsl_DecimalNumber269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_DecimalNumber269"):
                opp_val = getattr(value, "dsl_DecimalNumber269", None)
                setattr(value, "dsl_DecimalNumber269", self)

class dsl_DecimalNumber:

    def __init__(self, decDigitsUnderscore: str, decDigits: int, dsl_DecimalNumber: "dsl_UnsignedIntLiteral" = None, dsl_DecimalNumber269: "dsl_FloatLiteral" = None, dsl_DecimalNumber272: "dsl_FloatLiteral" = None):
        self.decDigitsUnderscore = decDigitsUnderscore
        self.decDigits = decDigits
        self.dsl_DecimalNumber = dsl_DecimalNumber
        self.dsl_DecimalNumber269 = dsl_DecimalNumber269
        self.dsl_DecimalNumber272 = dsl_DecimalNumber272
        
    @property
    def decDigitsUnderscore(self) -> str:
        return self.__decDigitsUnderscore

    @decDigitsUnderscore.setter
    def decDigitsUnderscore(self, decDigitsUnderscore: str):
        self.__decDigitsUnderscore = decDigitsUnderscore

    @property
    def decDigits(self) -> int:
        return self.__decDigits

    @decDigits.setter
    def decDigits(self, decDigits: int):
        self.__decDigits = decDigits

    @property
    def dsl_DecimalNumber272(self):
        return self.__dsl_DecimalNumber272

    @dsl_DecimalNumber272.setter
    def dsl_DecimalNumber272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_DecimalNumber__dsl_DecimalNumber272", None)
        self.__dsl_DecimalNumber272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FloatLiteral271"):
                opp_val = getattr(old_value, "dsl_FloatLiteral271", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FloatLiteral271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FloatLiteral271"):
                opp_val = getattr(value, "dsl_FloatLiteral271", None)
                setattr(value, "dsl_FloatLiteral271", self)

    @property
    def dsl_DecimalNumber(self):
        return self.__dsl_DecimalNumber

    @dsl_DecimalNumber.setter
    def dsl_DecimalNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_DecimalNumber__dsl_DecimalNumber", None)
        self.__dsl_DecimalNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnsignedIntLiteral"):
                opp_val = getattr(old_value, "dsl_UnsignedIntLiteral", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnsignedIntLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnsignedIntLiteral"):
                opp_val = getattr(value, "dsl_UnsignedIntLiteral", None)
                setattr(value, "dsl_UnsignedIntLiteral", self)

    @property
    def dsl_DecimalNumber269(self):
        return self.__dsl_DecimalNumber269

    @dsl_DecimalNumber269.setter
    def dsl_DecimalNumber269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_DecimalNumber__dsl_DecimalNumber269", None)
        self.__dsl_DecimalNumber269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FloatLiteral"):
                opp_val = getattr(old_value, "dsl_FloatLiteral", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FloatLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FloatLiteral"):
                opp_val = getattr(value, "dsl_FloatLiteral", None)
                setattr(value, "dsl_FloatLiteral", self)

class dsl_PrimarySuffix:

    def __init__(self, thisOp: bool, id: str, dsl_PrimarySuffix: "dsl_AllocationExpression" = None, dsl_PrimarySuffix250: "dsl_MemberSelector" = None, dsl_PrimarySuffix253: "dsl_Expression" = None, dsl_PrimarySuffix256: "dsl_Arguments" = None):
        self.thisOp = thisOp
        self.id = id
        self.dsl_PrimarySuffix = dsl_PrimarySuffix
        self.dsl_PrimarySuffix250 = dsl_PrimarySuffix250
        self.dsl_PrimarySuffix253 = dsl_PrimarySuffix253
        self.dsl_PrimarySuffix256 = dsl_PrimarySuffix256
        
    @property
    def thisOp(self) -> bool:
        return self.__thisOp

    @thisOp.setter
    def thisOp(self, thisOp: bool):
        self.__thisOp = thisOp

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_PrimarySuffix256(self):
        return self.__dsl_PrimarySuffix256

    @dsl_PrimarySuffix256.setter
    def dsl_PrimarySuffix256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimarySuffix__dsl_PrimarySuffix256", None)
        self.__dsl_PrimarySuffix256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Arguments257"):
                opp_val = getattr(old_value, "dsl_Arguments257", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Arguments257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Arguments257"):
                opp_val = getattr(value, "dsl_Arguments257", None)
                setattr(value, "dsl_Arguments257", self)

    @property
    def dsl_PrimarySuffix253(self):
        return self.__dsl_PrimarySuffix253

    @dsl_PrimarySuffix253.setter
    def dsl_PrimarySuffix253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimarySuffix__dsl_PrimarySuffix253", None)
        self.__dsl_PrimarySuffix253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression254"):
                opp_val = getattr(old_value, "dsl_Expression254", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression254"):
                opp_val = getattr(value, "dsl_Expression254", None)
                setattr(value, "dsl_Expression254", self)

    @property
    def dsl_PrimarySuffix250(self):
        return self.__dsl_PrimarySuffix250

    @dsl_PrimarySuffix250.setter
    def dsl_PrimarySuffix250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimarySuffix__dsl_PrimarySuffix250", None)
        self.__dsl_PrimarySuffix250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MemberSelector251"):
                opp_val = getattr(old_value, "dsl_MemberSelector251", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MemberSelector251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MemberSelector251"):
                opp_val = getattr(value, "dsl_MemberSelector251", None)
                setattr(value, "dsl_MemberSelector251", self)

    @property
    def dsl_PrimarySuffix(self):
        return self.__dsl_PrimarySuffix

    @dsl_PrimarySuffix.setter
    def dsl_PrimarySuffix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimarySuffix__dsl_PrimarySuffix", None)
        self.__dsl_PrimarySuffix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AllocationExpression248"):
                opp_val = getattr(old_value, "dsl_AllocationExpression248", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AllocationExpression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AllocationExpression248"):
                opp_val = getattr(value, "dsl_AllocationExpression248", None)
                setattr(value, "dsl_AllocationExpression248", self)

class dsl_BaseLiteral:

    def __init__(self, binDigitsUnderscore: str, decDigitsUnderscore: str, hexDigitsUnderscore: str, dsl_BaseLiteral: "dsl_UnsignedIntLiteral" = None, dsl_BaseLiteral262: "dsl_SignedIntLiteral" = None):
        self.binDigitsUnderscore = binDigitsUnderscore
        self.decDigitsUnderscore = decDigitsUnderscore
        self.hexDigitsUnderscore = hexDigitsUnderscore
        self.dsl_BaseLiteral = dsl_BaseLiteral
        self.dsl_BaseLiteral262 = dsl_BaseLiteral262
        
    @property
    def decDigitsUnderscore(self) -> str:
        return self.__decDigitsUnderscore

    @decDigitsUnderscore.setter
    def decDigitsUnderscore(self, decDigitsUnderscore: str):
        self.__decDigitsUnderscore = decDigitsUnderscore

    @property
    def binDigitsUnderscore(self) -> str:
        return self.__binDigitsUnderscore

    @binDigitsUnderscore.setter
    def binDigitsUnderscore(self, binDigitsUnderscore: str):
        self.__binDigitsUnderscore = binDigitsUnderscore

    @property
    def hexDigitsUnderscore(self) -> str:
        return self.__hexDigitsUnderscore

    @hexDigitsUnderscore.setter
    def hexDigitsUnderscore(self, hexDigitsUnderscore: str):
        self.__hexDigitsUnderscore = hexDigitsUnderscore

    @property
    def dsl_BaseLiteral(self):
        return self.__dsl_BaseLiteral

    @dsl_BaseLiteral.setter
    def dsl_BaseLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_BaseLiteral__dsl_BaseLiteral", None)
        self.__dsl_BaseLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnsignedIntLiteral260"):
                opp_val = getattr(old_value, "dsl_UnsignedIntLiteral260", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnsignedIntLiteral260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnsignedIntLiteral260"):
                opp_val = getattr(value, "dsl_UnsignedIntLiteral260", None)
                setattr(value, "dsl_UnsignedIntLiteral260", self)

    @property
    def dsl_BaseLiteral262(self):
        return self.__dsl_BaseLiteral262

    @dsl_BaseLiteral262.setter
    def dsl_BaseLiteral262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_BaseLiteral__dsl_BaseLiteral262", None)
        self.__dsl_BaseLiteral262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SignedIntLiteral"):
                opp_val = getattr(old_value, "dsl_SignedIntLiteral", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SignedIntLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SignedIntLiteral"):
                opp_val = getattr(value, "dsl_SignedIntLiteral", None)
                setattr(value, "dsl_SignedIntLiteral", self)

class dsl_AllocationExpression:

    def __init__(self, primType: str, dsl_AllocationExpression: "dsl_PrimaryPrefix" = None, dsl_AllocationExpression248: "dsl_PrimarySuffix" = None, dsl_AllocationExpression295: "dsl_Arguments" = None, dsl_AllocationExpression298: "dsl_ClassOrInterfaceBody" = None, dsl_AllocationExpression287: "dsl_ArrayDimsAndInits" = None, dsl_AllocationExpression289: "dsl_ClassOrInterfaceType" = None, dsl_AllocationExpression292: "dsl_TypeArguments" = None):
        self.primType = primType
        self.dsl_AllocationExpression = dsl_AllocationExpression
        self.dsl_AllocationExpression248 = dsl_AllocationExpression248
        self.dsl_AllocationExpression295 = dsl_AllocationExpression295
        self.dsl_AllocationExpression298 = dsl_AllocationExpression298
        self.dsl_AllocationExpression287 = dsl_AllocationExpression287
        self.dsl_AllocationExpression289 = dsl_AllocationExpression289
        self.dsl_AllocationExpression292 = dsl_AllocationExpression292
        
    @property
    def primType(self) -> str:
        return self.__primType

    @primType.setter
    def primType(self, primType: str):
        self.__primType = primType

    @property
    def dsl_AllocationExpression287(self):
        return self.__dsl_AllocationExpression287

    @dsl_AllocationExpression287.setter
    def dsl_AllocationExpression287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression287", None)
        self.__dsl_AllocationExpression287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ArrayDimsAndInits"):
                opp_val = getattr(old_value, "dsl_ArrayDimsAndInits", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ArrayDimsAndInits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ArrayDimsAndInits"):
                opp_val = getattr(value, "dsl_ArrayDimsAndInits", None)
                setattr(value, "dsl_ArrayDimsAndInits", self)

    @property
    def dsl_AllocationExpression298(self):
        return self.__dsl_AllocationExpression298

    @dsl_AllocationExpression298.setter
    def dsl_AllocationExpression298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression298", None)
        self.__dsl_AllocationExpression298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBody299"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBody299", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBody299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBody299"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBody299", None)
                setattr(value, "dsl_ClassOrInterfaceBody299", self)

    @property
    def dsl_AllocationExpression295(self):
        return self.__dsl_AllocationExpression295

    @dsl_AllocationExpression295.setter
    def dsl_AllocationExpression295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression295", None)
        self.__dsl_AllocationExpression295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Arguments296"):
                opp_val = getattr(old_value, "dsl_Arguments296", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Arguments296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Arguments296"):
                opp_val = getattr(value, "dsl_Arguments296", None)
                setattr(value, "dsl_Arguments296", self)

    @property
    def dsl_AllocationExpression(self):
        return self.__dsl_AllocationExpression

    @dsl_AllocationExpression.setter
    def dsl_AllocationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression", None)
        self.__dsl_AllocationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryPrefix240"):
                opp_val = getattr(old_value, "dsl_PrimaryPrefix240", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryPrefix240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryPrefix240"):
                opp_val = getattr(value, "dsl_PrimaryPrefix240", None)
                setattr(value, "dsl_PrimaryPrefix240", self)

    @property
    def dsl_AllocationExpression248(self):
        return self.__dsl_AllocationExpression248

    @dsl_AllocationExpression248.setter
    def dsl_AllocationExpression248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression248", None)
        self.__dsl_AllocationExpression248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimarySuffix"):
                opp_val = getattr(old_value, "dsl_PrimarySuffix", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimarySuffix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimarySuffix"):
                opp_val = getattr(value, "dsl_PrimarySuffix", None)
                setattr(value, "dsl_PrimarySuffix", self)

    @property
    def dsl_AllocationExpression289(self):
        return self.__dsl_AllocationExpression289

    @dsl_AllocationExpression289.setter
    def dsl_AllocationExpression289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression289", None)
        self.__dsl_AllocationExpression289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceType290"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceType290", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceType290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceType290"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceType290", None)
                setattr(value, "dsl_ClassOrInterfaceType290", self)

    @property
    def dsl_AllocationExpression292(self):
        return self.__dsl_AllocationExpression292

    @dsl_AllocationExpression292.setter
    def dsl_AllocationExpression292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AllocationExpression__dsl_AllocationExpression292", None)
        self.__dsl_AllocationExpression292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeArguments293"):
                opp_val = getattr(old_value, "dsl_TypeArguments293", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeArguments293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeArguments293"):
                opp_val = getattr(value, "dsl_TypeArguments293", None)
                setattr(value, "dsl_TypeArguments293", self)

class dsl_PrimaryPrefix:

    def __init__(self, thisOp: str, superOp: str, id: str, dsl_PrimaryPrefix240: "dsl_AllocationExpression" = None, dsl_PrimaryPrefix242: "dsl_ResultType" = None, dsl_PrimaryPrefix245: "dsl_Name" = None, dsl_PrimaryPrefix: "dsl_Literal" = None, dsl_PrimaryPrefix237: "dsl_Expression" = None):
        self.thisOp = thisOp
        self.superOp = superOp
        self.id = id
        self.dsl_PrimaryPrefix240 = dsl_PrimaryPrefix240
        self.dsl_PrimaryPrefix242 = dsl_PrimaryPrefix242
        self.dsl_PrimaryPrefix245 = dsl_PrimaryPrefix245
        self.dsl_PrimaryPrefix = dsl_PrimaryPrefix
        self.dsl_PrimaryPrefix237 = dsl_PrimaryPrefix237
        
    @property
    def superOp(self) -> str:
        return self.__superOp

    @superOp.setter
    def superOp(self, superOp: str):
        self.__superOp = superOp

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def thisOp(self) -> str:
        return self.__thisOp

    @thisOp.setter
    def thisOp(self, thisOp: str):
        self.__thisOp = thisOp

    @property
    def dsl_PrimaryPrefix242(self):
        return self.__dsl_PrimaryPrefix242

    @dsl_PrimaryPrefix242.setter
    def dsl_PrimaryPrefix242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimaryPrefix__dsl_PrimaryPrefix242", None)
        self.__dsl_PrimaryPrefix242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ResultType243"):
                opp_val = getattr(old_value, "dsl_ResultType243", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ResultType243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ResultType243"):
                opp_val = getattr(value, "dsl_ResultType243", None)
                setattr(value, "dsl_ResultType243", self)

    @property
    def dsl_PrimaryPrefix245(self):
        return self.__dsl_PrimaryPrefix245

    @dsl_PrimaryPrefix245.setter
    def dsl_PrimaryPrefix245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimaryPrefix__dsl_PrimaryPrefix245", None)
        self.__dsl_PrimaryPrefix245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Name246"):
                opp_val = getattr(old_value, "dsl_Name246", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Name246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Name246"):
                opp_val = getattr(value, "dsl_Name246", None)
                setattr(value, "dsl_Name246", self)

    @property
    def dsl_PrimaryPrefix237(self):
        return self.__dsl_PrimaryPrefix237

    @dsl_PrimaryPrefix237.setter
    def dsl_PrimaryPrefix237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimaryPrefix__dsl_PrimaryPrefix237", None)
        self.__dsl_PrimaryPrefix237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression238"):
                opp_val = getattr(old_value, "dsl_Expression238", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression238"):
                opp_val = getattr(value, "dsl_Expression238", None)
                setattr(value, "dsl_Expression238", self)

    @property
    def dsl_PrimaryPrefix240(self):
        return self.__dsl_PrimaryPrefix240

    @dsl_PrimaryPrefix240.setter
    def dsl_PrimaryPrefix240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimaryPrefix__dsl_PrimaryPrefix240", None)
        self.__dsl_PrimaryPrefix240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AllocationExpression"):
                opp_val = getattr(old_value, "dsl_AllocationExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AllocationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AllocationExpression"):
                opp_val = getattr(value, "dsl_AllocationExpression", None)
                setattr(value, "dsl_AllocationExpression", self)

    @property
    def dsl_PrimaryPrefix(self):
        return self.__dsl_PrimaryPrefix

    @dsl_PrimaryPrefix.setter
    def dsl_PrimaryPrefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PrimaryPrefix__dsl_PrimaryPrefix", None)
        self.__dsl_PrimaryPrefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Literal235"):
                opp_val = getattr(old_value, "dsl_Literal235", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Literal235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Literal235"):
                opp_val = getattr(value, "dsl_Literal235", None)
                setattr(value, "dsl_Literal235", self)

class dsl_MemberSelector:

    def __init__(self, id: str, dsl_MemberSelector: "dsl_TypeArguments" = None, dsl_MemberSelector251: "dsl_PrimarySuffix" = None):
        self.id = id
        self.dsl_MemberSelector = dsl_MemberSelector
        self.dsl_MemberSelector251 = dsl_MemberSelector251
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_MemberSelector(self):
        return self.__dsl_MemberSelector

    @dsl_MemberSelector.setter
    def dsl_MemberSelector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MemberSelector__dsl_MemberSelector", None)
        self.__dsl_MemberSelector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeArguments233"):
                opp_val = getattr(old_value, "dsl_TypeArguments233", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeArguments233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeArguments233"):
                opp_val = getattr(value, "dsl_TypeArguments233", None)
                setattr(value, "dsl_TypeArguments233", self)

    @property
    def dsl_MemberSelector251(self):
        return self.__dsl_MemberSelector251

    @dsl_MemberSelector251.setter
    def dsl_MemberSelector251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MemberSelector__dsl_MemberSelector251", None)
        self.__dsl_MemberSelector251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimarySuffix250"):
                opp_val = getattr(old_value, "dsl_PrimarySuffix250", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimarySuffix250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimarySuffix250"):
                opp_val = getattr(value, "dsl_PrimarySuffix250", None)
                setattr(value, "dsl_PrimarySuffix250", self)

class dsl_Literal:

    def __init__(self, nullLit: str, charLit: str, stringLit: str, dsl_Literal: "dsl_CastLookahead" = None, dsl_Literal235: "dsl_PrimaryPrefix" = None, dsl_Literal274: "dsl_IntegerLiteral" = None, dsl_Literal277: "dsl_FloatLiteral" = None, dsl_Literal280: "dsl_BooleanLiteral" = None):
        self.nullLit = nullLit
        self.charLit = charLit
        self.stringLit = stringLit
        self.dsl_Literal = dsl_Literal
        self.dsl_Literal235 = dsl_Literal235
        self.dsl_Literal274 = dsl_Literal274
        self.dsl_Literal277 = dsl_Literal277
        self.dsl_Literal280 = dsl_Literal280
        
    @property
    def charLit(self) -> str:
        return self.__charLit

    @charLit.setter
    def charLit(self, charLit: str):
        self.__charLit = charLit

    @property
    def stringLit(self) -> str:
        return self.__stringLit

    @stringLit.setter
    def stringLit(self, stringLit: str):
        self.__stringLit = stringLit

    @property
    def nullLit(self) -> str:
        return self.__nullLit

    @nullLit.setter
    def nullLit(self, nullLit: str):
        self.__nullLit = nullLit

    @property
    def dsl_Literal235(self):
        return self.__dsl_Literal235

    @dsl_Literal235.setter
    def dsl_Literal235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Literal__dsl_Literal235", None)
        self.__dsl_Literal235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryPrefix"):
                opp_val = getattr(old_value, "dsl_PrimaryPrefix", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryPrefix"):
                opp_val = getattr(value, "dsl_PrimaryPrefix", None)
                setattr(value, "dsl_PrimaryPrefix", self)

    @property
    def dsl_Literal(self):
        return self.__dsl_Literal

    @dsl_Literal.setter
    def dsl_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Literal__dsl_Literal", None)
        self.__dsl_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_CastLookahead220"):
                opp_val = getattr(old_value, "dsl_CastLookahead220", None)
                if opp_val == self:
                    setattr(old_value, "dsl_CastLookahead220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_CastLookahead220"):
                opp_val = getattr(value, "dsl_CastLookahead220", None)
                setattr(value, "dsl_CastLookahead220", self)

    @property
    def dsl_Literal277(self):
        return self.__dsl_Literal277

    @dsl_Literal277.setter
    def dsl_Literal277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Literal__dsl_Literal277", None)
        self.__dsl_Literal277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FloatLiteral278"):
                opp_val = getattr(old_value, "dsl_FloatLiteral278", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FloatLiteral278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FloatLiteral278"):
                opp_val = getattr(value, "dsl_FloatLiteral278", None)
                setattr(value, "dsl_FloatLiteral278", self)

    @property
    def dsl_Literal274(self):
        return self.__dsl_Literal274

    @dsl_Literal274.setter
    def dsl_Literal274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Literal__dsl_Literal274", None)
        self.__dsl_Literal274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_IntegerLiteral275"):
                opp_val = getattr(old_value, "dsl_IntegerLiteral275", None)
                if opp_val == self:
                    setattr(old_value, "dsl_IntegerLiteral275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_IntegerLiteral275"):
                opp_val = getattr(value, "dsl_IntegerLiteral275", None)
                setattr(value, "dsl_IntegerLiteral275", self)

    @property
    def dsl_Literal280(self):
        return self.__dsl_Literal280

    @dsl_Literal280.setter
    def dsl_Literal280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Literal__dsl_Literal280", None)
        self.__dsl_Literal280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_BooleanLiteral"):
                opp_val = getattr(old_value, "dsl_BooleanLiteral", None)
                if opp_val == self:
                    setattr(old_value, "dsl_BooleanLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_BooleanLiteral"):
                opp_val = getattr(value, "dsl_BooleanLiteral", None)
                setattr(value, "dsl_BooleanLiteral", self)

class dsl_EObject:

    pass
class dsl_CastLookahead:

    def __init__(self, bitNegOp: str, negOp: str, primType: str, openBracket: str, id: str, thisOp: str, superOp: str, newOp: str, dsl_CastLookahead217: "dsl_Type" = None, dsl_CastLookahead: "dsl_Type" = None, dsl_CastLookahead220: "dsl_Literal" = None):
        self.bitNegOp = bitNegOp
        self.negOp = negOp
        self.primType = primType
        self.openBracket = openBracket
        self.id = id
        self.thisOp = thisOp
        self.superOp = superOp
        self.newOp = newOp
        self.dsl_CastLookahead217 = dsl_CastLookahead217
        self.dsl_CastLookahead = dsl_CastLookahead
        self.dsl_CastLookahead220 = dsl_CastLookahead220
        
    @property
    def bitNegOp(self) -> str:
        return self.__bitNegOp

    @bitNegOp.setter
    def bitNegOp(self, bitNegOp: str):
        self.__bitNegOp = bitNegOp

    @property
    def thisOp(self) -> str:
        return self.__thisOp

    @thisOp.setter
    def thisOp(self, thisOp: str):
        self.__thisOp = thisOp

    @property
    def openBracket(self) -> str:
        return self.__openBracket

    @openBracket.setter
    def openBracket(self, openBracket: str):
        self.__openBracket = openBracket

    @property
    def superOp(self) -> str:
        return self.__superOp

    @superOp.setter
    def superOp(self, superOp: str):
        self.__superOp = superOp

    @property
    def newOp(self) -> str:
        return self.__newOp

    @newOp.setter
    def newOp(self, newOp: str):
        self.__newOp = newOp

    @property
    def negOp(self) -> str:
        return self.__negOp

    @negOp.setter
    def negOp(self, negOp: str):
        self.__negOp = negOp

    @property
    def primType(self) -> str:
        return self.__primType

    @primType.setter
    def primType(self, primType: str):
        self.__primType = primType

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_CastLookahead(self):
        return self.__dsl_CastLookahead

    @dsl_CastLookahead.setter
    def dsl_CastLookahead(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_CastLookahead__dsl_CastLookahead", None)
        self.__dsl_CastLookahead = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type215"):
                opp_val = getattr(old_value, "dsl_Type215", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type215"):
                opp_val = getattr(value, "dsl_Type215", None)
                setattr(value, "dsl_Type215", self)

    @property
    def dsl_CastLookahead217(self):
        return self.__dsl_CastLookahead217

    @dsl_CastLookahead217.setter
    def dsl_CastLookahead217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_CastLookahead__dsl_CastLookahead217", None)
        self.__dsl_CastLookahead217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type218"):
                opp_val = getattr(old_value, "dsl_Type218", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type218"):
                opp_val = getattr(value, "dsl_Type218", None)
                setattr(value, "dsl_Type218", self)

    @property
    def dsl_CastLookahead220(self):
        return self.__dsl_CastLookahead220

    @dsl_CastLookahead220.setter
    def dsl_CastLookahead220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_CastLookahead__dsl_CastLookahead220", None)
        self.__dsl_CastLookahead220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Literal"):
                opp_val = getattr(old_value, "dsl_Literal", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Literal"):
                opp_val = getattr(value, "dsl_Literal", None)
                setattr(value, "dsl_Literal", self)

class dsl_PostfixExpression:

    def __init__(self, op: str, dsl_PostfixExpression: "dsl_UnaryExpressionNotPlusMinus" = None, dsl_PostfixExpression222: "dsl_PrimaryExpression" = None):
        self.op = op
        self.dsl_PostfixExpression = dsl_PostfixExpression
        self.dsl_PostfixExpression222 = dsl_PostfixExpression222
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def dsl_PostfixExpression(self):
        return self.__dsl_PostfixExpression

    @dsl_PostfixExpression.setter
    def dsl_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PostfixExpression__dsl_PostfixExpression", None)
        self.__dsl_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpressionNotPlusMinus213"):
                opp_val = getattr(old_value, "dsl_UnaryExpressionNotPlusMinus213", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpressionNotPlusMinus213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpressionNotPlusMinus213"):
                opp_val = getattr(value, "dsl_UnaryExpressionNotPlusMinus213", None)
                setattr(value, "dsl_UnaryExpressionNotPlusMinus213", self)

    @property
    def dsl_PostfixExpression222(self):
        return self.__dsl_PostfixExpression222

    @dsl_PostfixExpression222.setter
    def dsl_PostfixExpression222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PostfixExpression__dsl_PostfixExpression222", None)
        self.__dsl_PostfixExpression222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryExpression223"):
                opp_val = getattr(old_value, "dsl_PrimaryExpression223", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryExpression223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryExpression223"):
                opp_val = getattr(value, "dsl_PrimaryExpression223", None)
                setattr(value, "dsl_PrimaryExpression223", self)

class dsl_CastExpression:

    pass
class dsl_UnaryExpressionNotPlusMinus:

    def __init__(self, negOp: str, dsl_UnaryExpressionNotPlusMinus: "dsl_UnaryExpression" = None, dsl_UnaryExpressionNotPlusMinus208: "dsl_UnaryExpression" = None, dsl_UnaryExpressionNotPlusMinus211: "dsl_CastExpression" = None, dsl_UnaryExpressionNotPlusMinus213: "dsl_PostfixExpression" = None):
        self.negOp = negOp
        self.dsl_UnaryExpressionNotPlusMinus = dsl_UnaryExpressionNotPlusMinus
        self.dsl_UnaryExpressionNotPlusMinus208 = dsl_UnaryExpressionNotPlusMinus208
        self.dsl_UnaryExpressionNotPlusMinus211 = dsl_UnaryExpressionNotPlusMinus211
        self.dsl_UnaryExpressionNotPlusMinus213 = dsl_UnaryExpressionNotPlusMinus213
        
    @property
    def negOp(self) -> str:
        return self.__negOp

    @negOp.setter
    def negOp(self, negOp: str):
        self.__negOp = negOp

    @property
    def dsl_UnaryExpressionNotPlusMinus213(self):
        return self.__dsl_UnaryExpressionNotPlusMinus213

    @dsl_UnaryExpressionNotPlusMinus213.setter
    def dsl_UnaryExpressionNotPlusMinus213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpressionNotPlusMinus__dsl_UnaryExpressionNotPlusMinus213", None)
        self.__dsl_UnaryExpressionNotPlusMinus213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PostfixExpression"):
                opp_val = getattr(old_value, "dsl_PostfixExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PostfixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PostfixExpression"):
                opp_val = getattr(value, "dsl_PostfixExpression", None)
                setattr(value, "dsl_PostfixExpression", self)

    @property
    def dsl_UnaryExpressionNotPlusMinus(self):
        return self.__dsl_UnaryExpressionNotPlusMinus

    @dsl_UnaryExpressionNotPlusMinus.setter
    def dsl_UnaryExpressionNotPlusMinus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpressionNotPlusMinus__dsl_UnaryExpressionNotPlusMinus", None)
        self.__dsl_UnaryExpressionNotPlusMinus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpression200"):
                opp_val = getattr(old_value, "dsl_UnaryExpression200", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpression200"):
                opp_val = getattr(value, "dsl_UnaryExpression200", None)
                setattr(value, "dsl_UnaryExpression200", self)

    @property
    def dsl_UnaryExpressionNotPlusMinus211(self):
        return self.__dsl_UnaryExpressionNotPlusMinus211

    @dsl_UnaryExpressionNotPlusMinus211.setter
    def dsl_UnaryExpressionNotPlusMinus211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpressionNotPlusMinus__dsl_UnaryExpressionNotPlusMinus211", None)
        self.__dsl_UnaryExpressionNotPlusMinus211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_CastExpression"):
                opp_val = getattr(old_value, "dsl_CastExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_CastExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_CastExpression"):
                opp_val = getattr(value, "dsl_CastExpression", None)
                setattr(value, "dsl_CastExpression", self)

    @property
    def dsl_UnaryExpressionNotPlusMinus208(self):
        return self.__dsl_UnaryExpressionNotPlusMinus208

    @dsl_UnaryExpressionNotPlusMinus208.setter
    def dsl_UnaryExpressionNotPlusMinus208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpressionNotPlusMinus__dsl_UnaryExpressionNotPlusMinus208", None)
        self.__dsl_UnaryExpressionNotPlusMinus208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpression209"):
                opp_val = getattr(old_value, "dsl_UnaryExpression209", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpression209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpression209"):
                opp_val = getattr(value, "dsl_UnaryExpression209", None)
                setattr(value, "dsl_UnaryExpression209", self)

class dsl_PreDecrementExpression:

    pass
class dsl_PreIncrementExpression:

    pass
class dsl_AdditiveExpression:

    def __init__(self, ops: str, dsl_AdditiveExpression189: set["dsl_MultiplicativeExpression"] = None, dsl_AdditiveExpression: "dsl_ShiftExpression" = None):
        self.ops = ops
        self.dsl_AdditiveExpression189 = dsl_AdditiveExpression189 if dsl_AdditiveExpression189 is not None else set()
        self.dsl_AdditiveExpression = dsl_AdditiveExpression
        
    @property
    def ops(self) -> str:
        return self.__ops

    @ops.setter
    def ops(self, ops: str):
        self.__ops = ops

    @property
    def dsl_AdditiveExpression189(self):
        return self.__dsl_AdditiveExpression189

    @dsl_AdditiveExpression189.setter
    def dsl_AdditiveExpression189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AdditiveExpression__dsl_AdditiveExpression189", None)
        self.__dsl_AdditiveExpression189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_MultiplicativeExpression"):
                    opp_val = getattr(item, "dsl_MultiplicativeExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_MultiplicativeExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_MultiplicativeExpression"):
                    opp_val = getattr(item, "dsl_MultiplicativeExpression", None)
                    
                    setattr(item, "dsl_MultiplicativeExpression", self)
                    

    @property
    def dsl_AdditiveExpression(self):
        return self.__dsl_AdditiveExpression

    @dsl_AdditiveExpression.setter
    def dsl_AdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AdditiveExpression__dsl_AdditiveExpression", None)
        self.__dsl_AdditiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ShiftExpression187"):
                opp_val = getattr(old_value, "dsl_ShiftExpression187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ShiftExpression187"):
                opp_val = getattr(value, "dsl_ShiftExpression187", None)
                if opp_val is None:
                    setattr(value, "dsl_ShiftExpression187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_ShiftExpression:

    def __init__(self, ops: str, dsl_ShiftExpression: "dsl_RelationalExpression" = None, dsl_ShiftExpression187: set["dsl_AdditiveExpression"] = None):
        self.ops = ops
        self.dsl_ShiftExpression = dsl_ShiftExpression
        self.dsl_ShiftExpression187 = dsl_ShiftExpression187 if dsl_ShiftExpression187 is not None else set()
        
    @property
    def ops(self) -> str:
        return self.__ops

    @ops.setter
    def ops(self, ops: str):
        self.__ops = ops

    @property
    def dsl_ShiftExpression(self):
        return self.__dsl_ShiftExpression

    @dsl_ShiftExpression.setter
    def dsl_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ShiftExpression__dsl_ShiftExpression", None)
        self.__dsl_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_RelationalExpression185"):
                opp_val = getattr(old_value, "dsl_RelationalExpression185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_RelationalExpression185"):
                opp_val = getattr(value, "dsl_RelationalExpression185", None)
                if opp_val is None:
                    setattr(value, "dsl_RelationalExpression185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_ShiftExpression187(self):
        return self.__dsl_ShiftExpression187

    @dsl_ShiftExpression187.setter
    def dsl_ShiftExpression187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ShiftExpression__dsl_ShiftExpression187", None)
        self.__dsl_ShiftExpression187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_AdditiveExpression"):
                    opp_val = getattr(item, "dsl_AdditiveExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_AdditiveExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_AdditiveExpression"):
                    opp_val = getattr(item, "dsl_AdditiveExpression", None)
                    
                    setattr(item, "dsl_AdditiveExpression", self)
                    

class dsl_UnaryExpression:

    def __init__(self, sign: str, dsl_UnaryExpression: "dsl_MultiplicativeExpression" = None, dsl_UnaryExpression194: "dsl_UnaryExpression" = None, dsl_UnaryExpression192: "dsl_UnaryExpression" = None, dsl_UnaryExpression196: "dsl_PreIncrementExpression" = None, dsl_UnaryExpression198: "dsl_PreDecrementExpression" = None, dsl_UnaryExpression200: "dsl_UnaryExpressionNotPlusMinus" = None, dsl_UnaryExpression209: "dsl_UnaryExpressionNotPlusMinus" = None):
        self.sign = sign
        self.dsl_UnaryExpression = dsl_UnaryExpression
        self.dsl_UnaryExpression194 = dsl_UnaryExpression194
        self.dsl_UnaryExpression192 = dsl_UnaryExpression192
        self.dsl_UnaryExpression196 = dsl_UnaryExpression196
        self.dsl_UnaryExpression198 = dsl_UnaryExpression198
        self.dsl_UnaryExpression200 = dsl_UnaryExpression200
        self.dsl_UnaryExpression209 = dsl_UnaryExpression209
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def dsl_UnaryExpression(self):
        return self.__dsl_UnaryExpression

    @dsl_UnaryExpression.setter
    def dsl_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression", None)
        self.__dsl_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MultiplicativeExpression191"):
                opp_val = getattr(old_value, "dsl_MultiplicativeExpression191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MultiplicativeExpression191"):
                opp_val = getattr(value, "dsl_MultiplicativeExpression191", None)
                if opp_val is None:
                    setattr(value, "dsl_MultiplicativeExpression191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_UnaryExpression209(self):
        return self.__dsl_UnaryExpression209

    @dsl_UnaryExpression209.setter
    def dsl_UnaryExpression209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression209", None)
        self.__dsl_UnaryExpression209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpressionNotPlusMinus208"):
                opp_val = getattr(old_value, "dsl_UnaryExpressionNotPlusMinus208", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpressionNotPlusMinus208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpressionNotPlusMinus208"):
                opp_val = getattr(value, "dsl_UnaryExpressionNotPlusMinus208", None)
                setattr(value, "dsl_UnaryExpressionNotPlusMinus208", self)

    @property
    def dsl_UnaryExpression198(self):
        return self.__dsl_UnaryExpression198

    @dsl_UnaryExpression198.setter
    def dsl_UnaryExpression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression198", None)
        self.__dsl_UnaryExpression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PreDecrementExpression"):
                opp_val = getattr(old_value, "dsl_PreDecrementExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PreDecrementExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PreDecrementExpression"):
                opp_val = getattr(value, "dsl_PreDecrementExpression", None)
                setattr(value, "dsl_PreDecrementExpression", self)

    @property
    def dsl_UnaryExpression192(self):
        return self.__dsl_UnaryExpression192

    @dsl_UnaryExpression192.setter
    def dsl_UnaryExpression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression192", None)
        self.__dsl_UnaryExpression192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpression194"):
                opp_val = getattr(old_value, "dsl_UnaryExpression194", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpression194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpression194"):
                opp_val = getattr(value, "dsl_UnaryExpression194", None)
                setattr(value, "dsl_UnaryExpression194", self)

    @property
    def dsl_UnaryExpression196(self):
        return self.__dsl_UnaryExpression196

    @dsl_UnaryExpression196.setter
    def dsl_UnaryExpression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression196", None)
        self.__dsl_UnaryExpression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PreIncrementExpression"):
                opp_val = getattr(old_value, "dsl_PreIncrementExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PreIncrementExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PreIncrementExpression"):
                opp_val = getattr(value, "dsl_PreIncrementExpression", None)
                setattr(value, "dsl_PreIncrementExpression", self)

    @property
    def dsl_UnaryExpression200(self):
        return self.__dsl_UnaryExpression200

    @dsl_UnaryExpression200.setter
    def dsl_UnaryExpression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression200", None)
        self.__dsl_UnaryExpression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpressionNotPlusMinus"):
                opp_val = getattr(old_value, "dsl_UnaryExpressionNotPlusMinus", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpressionNotPlusMinus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpressionNotPlusMinus"):
                opp_val = getattr(value, "dsl_UnaryExpressionNotPlusMinus", None)
                setattr(value, "dsl_UnaryExpressionNotPlusMinus", self)

    @property
    def dsl_UnaryExpression194(self):
        return self.__dsl_UnaryExpression194

    @dsl_UnaryExpression194.setter
    def dsl_UnaryExpression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_UnaryExpression__dsl_UnaryExpression194", None)
        self.__dsl_UnaryExpression194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnaryExpression192"):
                opp_val = getattr(old_value, "dsl_UnaryExpression192", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnaryExpression192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnaryExpression192"):
                opp_val = getattr(value, "dsl_UnaryExpression192", None)
                setattr(value, "dsl_UnaryExpression192", self)

class dsl_MultiplicativeExpression:

    def __init__(self, ops: str, dsl_MultiplicativeExpression: "dsl_AdditiveExpression" = None, dsl_MultiplicativeExpression191: set["dsl_UnaryExpression"] = None):
        self.ops = ops
        self.dsl_MultiplicativeExpression = dsl_MultiplicativeExpression
        self.dsl_MultiplicativeExpression191 = dsl_MultiplicativeExpression191 if dsl_MultiplicativeExpression191 is not None else set()
        
    @property
    def ops(self) -> str:
        return self.__ops

    @ops.setter
    def ops(self, ops: str):
        self.__ops = ops

    @property
    def dsl_MultiplicativeExpression(self):
        return self.__dsl_MultiplicativeExpression

    @dsl_MultiplicativeExpression.setter
    def dsl_MultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MultiplicativeExpression__dsl_MultiplicativeExpression", None)
        self.__dsl_MultiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AdditiveExpression189"):
                opp_val = getattr(old_value, "dsl_AdditiveExpression189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AdditiveExpression189"):
                opp_val = getattr(value, "dsl_AdditiveExpression189", None)
                if opp_val is None:
                    setattr(value, "dsl_AdditiveExpression189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_MultiplicativeExpression191(self):
        return self.__dsl_MultiplicativeExpression191

    @dsl_MultiplicativeExpression191.setter
    def dsl_MultiplicativeExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MultiplicativeExpression__dsl_MultiplicativeExpression191", None)
        self.__dsl_MultiplicativeExpression191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_UnaryExpression"):
                    opp_val = getattr(item, "dsl_UnaryExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_UnaryExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_UnaryExpression"):
                    opp_val = getattr(item, "dsl_UnaryExpression", None)
                    
                    setattr(item, "dsl_UnaryExpression", self)
                    

class dsl_EqualityExpression:

    pass
class dsl_AndExpression:

    pass
class dsl_ExclusiveOrExpression:

    pass
class dsl_InclusiveOrExpression:

    pass
class dsl_RelationalExpression:

    def __init__(self, ops: str, dsl_RelationalExpression: "dsl_InstanceOfExpression" = None, dsl_RelationalExpression185: set["dsl_ShiftExpression"] = None):
        self.ops = ops
        self.dsl_RelationalExpression = dsl_RelationalExpression
        self.dsl_RelationalExpression185 = dsl_RelationalExpression185 if dsl_RelationalExpression185 is not None else set()
        
    @property
    def ops(self) -> str:
        return self.__ops

    @ops.setter
    def ops(self, ops: str):
        self.__ops = ops

    @property
    def dsl_RelationalExpression(self):
        return self.__dsl_RelationalExpression

    @dsl_RelationalExpression.setter
    def dsl_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RelationalExpression__dsl_RelationalExpression", None)
        self.__dsl_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_InstanceOfExpression180"):
                opp_val = getattr(old_value, "dsl_InstanceOfExpression180", None)
                if opp_val == self:
                    setattr(old_value, "dsl_InstanceOfExpression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_InstanceOfExpression180"):
                opp_val = getattr(value, "dsl_InstanceOfExpression180", None)
                setattr(value, "dsl_InstanceOfExpression180", self)

    @property
    def dsl_RelationalExpression185(self):
        return self.__dsl_RelationalExpression185

    @dsl_RelationalExpression185.setter
    def dsl_RelationalExpression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RelationalExpression__dsl_RelationalExpression185", None)
        self.__dsl_RelationalExpression185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_ShiftExpression"):
                    opp_val = getattr(item, "dsl_ShiftExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_ShiftExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_ShiftExpression"):
                    opp_val = getattr(item, "dsl_ShiftExpression", None)
                    
                    setattr(item, "dsl_ShiftExpression", self)
                    

class dsl_InstanceOfExpression:

    pass
class dsl_ConditionalOrExpression:

    pass
class dsl_Statement:

    pass
class dsl_ConditionalExpression:

    pass
class dsl_ConditionalAndExpression:

    pass
class dsl_WildcardBounds:

    def __init__(self, ext: bool, sup: bool, dsl_WildcardBounds: "dsl_TypeArgument" = None, dsl_WildcardBounds141: "dsl_ReferenceType" = None):
        self.ext = ext
        self.sup = sup
        self.dsl_WildcardBounds = dsl_WildcardBounds
        self.dsl_WildcardBounds141 = dsl_WildcardBounds141
        
    @property
    def sup(self) -> bool:
        return self.__sup

    @sup.setter
    def sup(self, sup: bool):
        self.__sup = sup

    @property
    def ext(self) -> bool:
        return self.__ext

    @ext.setter
    def ext(self, ext: bool):
        self.__ext = ext

    @property
    def dsl_WildcardBounds141(self):
        return self.__dsl_WildcardBounds141

    @dsl_WildcardBounds141.setter
    def dsl_WildcardBounds141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_WildcardBounds__dsl_WildcardBounds141", None)
        self.__dsl_WildcardBounds141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReferenceType142"):
                opp_val = getattr(old_value, "dsl_ReferenceType142", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReferenceType142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReferenceType142"):
                opp_val = getattr(value, "dsl_ReferenceType142", None)
                setattr(value, "dsl_ReferenceType142", self)

    @property
    def dsl_WildcardBounds(self):
        return self.__dsl_WildcardBounds

    @dsl_WildcardBounds.setter
    def dsl_WildcardBounds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_WildcardBounds__dsl_WildcardBounds", None)
        self.__dsl_WildcardBounds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeArgument139"):
                opp_val = getattr(old_value, "dsl_TypeArgument139", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeArgument139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeArgument139"):
                opp_val = getattr(value, "dsl_TypeArgument139", None)
                setattr(value, "dsl_TypeArgument139", self)

class IfStatement:

    pass
class dsl_TypeArguments:

    pass
class dsl_ReferenceType:

    def __init__(self, primType: str, squareBracketsAlpha: str, squareBracketsBeta: str, dsl_ReferenceType: "dsl_Type" = None, dsl_ReferenceType129: "dsl_ClassOrInterfaceType" = None, dsl_ReferenceType137: "dsl_TypeArgument" = None, dsl_ReferenceType142: "dsl_WildcardBounds" = None):
        self.primType = primType
        self.squareBracketsAlpha = squareBracketsAlpha
        self.squareBracketsBeta = squareBracketsBeta
        self.dsl_ReferenceType = dsl_ReferenceType
        self.dsl_ReferenceType129 = dsl_ReferenceType129
        self.dsl_ReferenceType137 = dsl_ReferenceType137
        self.dsl_ReferenceType142 = dsl_ReferenceType142
        
    @property
    def primType(self) -> str:
        return self.__primType

    @primType.setter
    def primType(self, primType: str):
        self.__primType = primType

    @property
    def squareBracketsBeta(self) -> str:
        return self.__squareBracketsBeta

    @squareBracketsBeta.setter
    def squareBracketsBeta(self, squareBracketsBeta: str):
        self.__squareBracketsBeta = squareBracketsBeta

    @property
    def squareBracketsAlpha(self) -> str:
        return self.__squareBracketsAlpha

    @squareBracketsAlpha.setter
    def squareBracketsAlpha(self, squareBracketsAlpha: str):
        self.__squareBracketsAlpha = squareBracketsAlpha

    @property
    def dsl_ReferenceType(self):
        return self.__dsl_ReferenceType

    @dsl_ReferenceType.setter
    def dsl_ReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ReferenceType__dsl_ReferenceType", None)
        self.__dsl_ReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type127"):
                opp_val = getattr(old_value, "dsl_Type127", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type127"):
                opp_val = getattr(value, "dsl_Type127", None)
                setattr(value, "dsl_Type127", self)

    @property
    def dsl_ReferenceType129(self):
        return self.__dsl_ReferenceType129

    @dsl_ReferenceType129.setter
    def dsl_ReferenceType129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ReferenceType__dsl_ReferenceType129", None)
        self.__dsl_ReferenceType129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceType130"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceType130", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceType130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceType130"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceType130", None)
                setattr(value, "dsl_ClassOrInterfaceType130", self)

    @property
    def dsl_ReferenceType137(self):
        return self.__dsl_ReferenceType137

    @dsl_ReferenceType137.setter
    def dsl_ReferenceType137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ReferenceType__dsl_ReferenceType137", None)
        self.__dsl_ReferenceType137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeArgument136"):
                opp_val = getattr(old_value, "dsl_TypeArgument136", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeArgument136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeArgument136"):
                opp_val = getattr(value, "dsl_TypeArgument136", None)
                setattr(value, "dsl_TypeArgument136", self)

    @property
    def dsl_ReferenceType142(self):
        return self.__dsl_ReferenceType142

    @dsl_ReferenceType142.setter
    def dsl_ReferenceType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ReferenceType__dsl_ReferenceType142", None)
        self.__dsl_ReferenceType142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_WildcardBounds141"):
                opp_val = getattr(old_value, "dsl_WildcardBounds141", None)
                if opp_val == self:
                    setattr(old_value, "dsl_WildcardBounds141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_WildcardBounds141"):
                opp_val = getattr(value, "dsl_WildcardBounds141", None)
                setattr(value, "dsl_WildcardBounds141", self)

class dsl_TypeArgument:

    pass
class dsl_PrimaryExpression:

    pass
class dsl_FormalParameter:

    def __init__(self, final: bool, dsl_FormalParameter: "dsl_FormalParameters" = None, dsl_FormalParameter113: "dsl_Type" = None, dsl_FormalParameter116: "dsl_VariableDeclaratorId" = None, dsl_FormalParameter442: "dsl_TryStatement" = None):
        self.final = final
        self.dsl_FormalParameter = dsl_FormalParameter
        self.dsl_FormalParameter113 = dsl_FormalParameter113
        self.dsl_FormalParameter116 = dsl_FormalParameter116
        self.dsl_FormalParameter442 = dsl_FormalParameter442
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def dsl_FormalParameter(self):
        return self.__dsl_FormalParameter

    @dsl_FormalParameter.setter
    def dsl_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FormalParameter__dsl_FormalParameter", None)
        self.__dsl_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FormalParameters111"):
                opp_val = getattr(old_value, "dsl_FormalParameters111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FormalParameters111"):
                opp_val = getattr(value, "dsl_FormalParameters111", None)
                if opp_val is None:
                    setattr(value, "dsl_FormalParameters111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_FormalParameter442(self):
        return self.__dsl_FormalParameter442

    @dsl_FormalParameter442.setter
    def dsl_FormalParameter442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FormalParameter__dsl_FormalParameter442", None)
        self.__dsl_FormalParameter442 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TryStatement441"):
                opp_val = getattr(old_value, "dsl_TryStatement441", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TryStatement441"):
                opp_val = getattr(value, "dsl_TryStatement441", None)
                if opp_val is None:
                    setattr(value, "dsl_TryStatement441", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_FormalParameter113(self):
        return self.__dsl_FormalParameter113

    @dsl_FormalParameter113.setter
    def dsl_FormalParameter113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FormalParameter__dsl_FormalParameter113", None)
        self.__dsl_FormalParameter113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type114"):
                opp_val = getattr(old_value, "dsl_Type114", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type114"):
                opp_val = getattr(value, "dsl_Type114", None)
                setattr(value, "dsl_Type114", self)

    @property
    def dsl_FormalParameter116(self):
        return self.__dsl_FormalParameter116

    @dsl_FormalParameter116.setter
    def dsl_FormalParameter116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_FormalParameter__dsl_FormalParameter116", None)
        self.__dsl_FormalParameter116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_VariableDeclaratorId117"):
                opp_val = getattr(old_value, "dsl_VariableDeclaratorId117", None)
                if opp_val == self:
                    setattr(old_value, "dsl_VariableDeclaratorId117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_VariableDeclaratorId117"):
                opp_val = getattr(value, "dsl_VariableDeclaratorId117", None)
                setattr(value, "dsl_VariableDeclaratorId117", self)

class dsl_MethodDeclarator:

    def __init__(self, id: str, squareBrackets: str, dsl_MethodDeclarator108: "dsl_FormalParameters" = None, dsl_MethodDeclarator: "dsl_MethodOrCtorDeclaration" = None):
        self.id = id
        self.squareBrackets = squareBrackets
        self.dsl_MethodDeclarator108 = dsl_MethodDeclarator108
        self.dsl_MethodDeclarator = dsl_MethodDeclarator
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def squareBrackets(self) -> str:
        return self.__squareBrackets

    @squareBrackets.setter
    def squareBrackets(self, squareBrackets: str):
        self.__squareBrackets = squareBrackets

    @property
    def dsl_MethodDeclarator108(self):
        return self.__dsl_MethodDeclarator108

    @dsl_MethodDeclarator108.setter
    def dsl_MethodDeclarator108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodDeclarator__dsl_MethodDeclarator108", None)
        self.__dsl_MethodDeclarator108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FormalParameters109"):
                opp_val = getattr(old_value, "dsl_FormalParameters109", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FormalParameters109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FormalParameters109"):
                opp_val = getattr(value, "dsl_FormalParameters109", None)
                setattr(value, "dsl_FormalParameters109", self)

    @property
    def dsl_MethodDeclarator(self):
        return self.__dsl_MethodDeclarator

    @dsl_MethodDeclarator.setter
    def dsl_MethodDeclarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodDeclarator__dsl_MethodDeclarator", None)
        self.__dsl_MethodDeclarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MethodOrCtorDeclaration104"):
                opp_val = getattr(old_value, "dsl_MethodOrCtorDeclaration104", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MethodOrCtorDeclaration104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MethodOrCtorDeclaration104"):
                opp_val = getattr(value, "dsl_MethodOrCtorDeclaration104", None)
                setattr(value, "dsl_MethodOrCtorDeclaration104", self)

class dsl_ResultType:

    pass
class dsl_BlockStatement:

    pass
class dsl_ExplicitConstructorInvocation:

    def __init__(self, parent: str, self: bool, dsl_ExplicitConstructorInvocation: "dsl_MethodOrCtorDeclaration" = None, dsl_ExplicitConstructorInvocation119: "dsl_Arguments" = None, dsl_ExplicitConstructorInvocation122: "dsl_PrimaryExpression" = None):
        self.parent = parent
        self.self = self
        self.dsl_ExplicitConstructorInvocation = dsl_ExplicitConstructorInvocation
        self.dsl_ExplicitConstructorInvocation119 = dsl_ExplicitConstructorInvocation119
        self.dsl_ExplicitConstructorInvocation122 = dsl_ExplicitConstructorInvocation122
        
    @property
    def self(self) -> bool:
        return self.__self

    @self.setter
    def self(self, self: bool):
        self.__self = self

    @property
    def parent(self) -> str:
        return self.__parent

    @parent.setter
    def parent(self, parent: str):
        self.__parent = parent

    @property
    def dsl_ExplicitConstructorInvocation119(self):
        return self.__dsl_ExplicitConstructorInvocation119

    @dsl_ExplicitConstructorInvocation119.setter
    def dsl_ExplicitConstructorInvocation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ExplicitConstructorInvocation__dsl_ExplicitConstructorInvocation119", None)
        self.__dsl_ExplicitConstructorInvocation119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Arguments120"):
                opp_val = getattr(old_value, "dsl_Arguments120", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Arguments120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Arguments120"):
                opp_val = getattr(value, "dsl_Arguments120", None)
                setattr(value, "dsl_Arguments120", self)

    @property
    def dsl_ExplicitConstructorInvocation122(self):
        return self.__dsl_ExplicitConstructorInvocation122

    @dsl_ExplicitConstructorInvocation122.setter
    def dsl_ExplicitConstructorInvocation122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ExplicitConstructorInvocation__dsl_ExplicitConstructorInvocation122", None)
        self.__dsl_ExplicitConstructorInvocation122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryExpression"):
                opp_val = getattr(old_value, "dsl_PrimaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryExpression"):
                opp_val = getattr(value, "dsl_PrimaryExpression", None)
                setattr(value, "dsl_PrimaryExpression", self)

    @property
    def dsl_ExplicitConstructorInvocation(self):
        return self.__dsl_ExplicitConstructorInvocation

    @dsl_ExplicitConstructorInvocation.setter
    def dsl_ExplicitConstructorInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ExplicitConstructorInvocation__dsl_ExplicitConstructorInvocation", None)
        self.__dsl_ExplicitConstructorInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MethodOrCtorDeclaration98"):
                opp_val = getattr(old_value, "dsl_MethodOrCtorDeclaration98", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MethodOrCtorDeclaration98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MethodOrCtorDeclaration98"):
                opp_val = getattr(value, "dsl_MethodOrCtorDeclaration98", None)
                setattr(value, "dsl_MethodOrCtorDeclaration98", self)

class dsl_NameList:

    pass
class dsl_FormalParameters:

    pass
class dsl_Block:

    pass
class dsl_VariableInitializer:

    pass
class dsl_VariableDeclaratorId:

    def __init__(self, id: str, squareBrackets: str, dsl_VariableDeclaratorId: "dsl_VariableDeclarator" = None, dsl_VariableDeclaratorId117: "dsl_FormalParameter" = None):
        self.id = id
        self.squareBrackets = squareBrackets
        self.dsl_VariableDeclaratorId = dsl_VariableDeclaratorId
        self.dsl_VariableDeclaratorId117 = dsl_VariableDeclaratorId117
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def squareBrackets(self) -> str:
        return self.__squareBrackets

    @squareBrackets.setter
    def squareBrackets(self, squareBrackets: str):
        self.__squareBrackets = squareBrackets

    @property
    def dsl_VariableDeclaratorId(self):
        return self.__dsl_VariableDeclaratorId

    @dsl_VariableDeclaratorId.setter
    def dsl_VariableDeclaratorId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_VariableDeclaratorId__dsl_VariableDeclaratorId", None)
        self.__dsl_VariableDeclaratorId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_VariableDeclarator80"):
                opp_val = getattr(old_value, "dsl_VariableDeclarator80", None)
                if opp_val == self:
                    setattr(old_value, "dsl_VariableDeclarator80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_VariableDeclarator80"):
                opp_val = getattr(value, "dsl_VariableDeclarator80", None)
                setattr(value, "dsl_VariableDeclarator80", self)

    @property
    def dsl_VariableDeclaratorId117(self):
        return self.__dsl_VariableDeclaratorId117

    @dsl_VariableDeclaratorId117.setter
    def dsl_VariableDeclaratorId117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_VariableDeclaratorId__dsl_VariableDeclaratorId117", None)
        self.__dsl_VariableDeclaratorId117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FormalParameter116"):
                opp_val = getattr(old_value, "dsl_FormalParameter116", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FormalParameter116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FormalParameter116"):
                opp_val = getattr(value, "dsl_FormalParameter116", None)
                setattr(value, "dsl_FormalParameter116", self)

class dsl_VariableDeclarator:

    pass
class dsl_Type:

    def __init__(self, primType: str, dsl_Type: "dsl_FieldDeclaration" = None, dsl_Type114: "dsl_FormalParameter" = None, dsl_Type127: "dsl_ReferenceType" = None, dsl_Type145: "dsl_ResultType" = None, dsl_Type183: "dsl_InstanceOfExpression" = None, dsl_Type218: "dsl_CastLookahead" = None, dsl_Type215: "dsl_CastLookahead" = None, dsl_Type226: "dsl_CastExpression" = None, dsl_Type359: "dsl_LocalVariableDeclaration" = None, dsl_Type400: "dsl_ForStatement" = None, dsl_Type477: "dsl_AnnotationTypeMemberDeclaration" = None):
        self.primType = primType
        self.dsl_Type = dsl_Type
        self.dsl_Type114 = dsl_Type114
        self.dsl_Type127 = dsl_Type127
        self.dsl_Type145 = dsl_Type145
        self.dsl_Type183 = dsl_Type183
        self.dsl_Type218 = dsl_Type218
        self.dsl_Type215 = dsl_Type215
        self.dsl_Type226 = dsl_Type226
        self.dsl_Type359 = dsl_Type359
        self.dsl_Type400 = dsl_Type400
        self.dsl_Type477 = dsl_Type477
        
    @property
    def primType(self) -> str:
        return self.__primType

    @primType.setter
    def primType(self, primType: str):
        self.__primType = primType

    @property
    def dsl_Type(self):
        return self.__dsl_Type

    @dsl_Type.setter
    def dsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type", None)
        self.__dsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FieldDeclaration76"):
                opp_val = getattr(old_value, "dsl_FieldDeclaration76", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FieldDeclaration76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FieldDeclaration76"):
                opp_val = getattr(value, "dsl_FieldDeclaration76", None)
                setattr(value, "dsl_FieldDeclaration76", self)

    @property
    def dsl_Type359(self):
        return self.__dsl_Type359

    @dsl_Type359.setter
    def dsl_Type359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type359", None)
        self.__dsl_Type359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_LocalVariableDeclaration358"):
                opp_val = getattr(old_value, "dsl_LocalVariableDeclaration358", None)
                if opp_val == self:
                    setattr(old_value, "dsl_LocalVariableDeclaration358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_LocalVariableDeclaration358"):
                opp_val = getattr(value, "dsl_LocalVariableDeclaration358", None)
                setattr(value, "dsl_LocalVariableDeclaration358", self)

    @property
    def dsl_Type114(self):
        return self.__dsl_Type114

    @dsl_Type114.setter
    def dsl_Type114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type114", None)
        self.__dsl_Type114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FormalParameter113"):
                opp_val = getattr(old_value, "dsl_FormalParameter113", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FormalParameter113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FormalParameter113"):
                opp_val = getattr(value, "dsl_FormalParameter113", None)
                setattr(value, "dsl_FormalParameter113", self)

    @property
    def dsl_Type145(self):
        return self.__dsl_Type145

    @dsl_Type145.setter
    def dsl_Type145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type145", None)
        self.__dsl_Type145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ResultType144"):
                opp_val = getattr(old_value, "dsl_ResultType144", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ResultType144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ResultType144"):
                opp_val = getattr(value, "dsl_ResultType144", None)
                setattr(value, "dsl_ResultType144", self)

    @property
    def dsl_Type218(self):
        return self.__dsl_Type218

    @dsl_Type218.setter
    def dsl_Type218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type218", None)
        self.__dsl_Type218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_CastLookahead217"):
                opp_val = getattr(old_value, "dsl_CastLookahead217", None)
                if opp_val == self:
                    setattr(old_value, "dsl_CastLookahead217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_CastLookahead217"):
                opp_val = getattr(value, "dsl_CastLookahead217", None)
                setattr(value, "dsl_CastLookahead217", self)

    @property
    def dsl_Type400(self):
        return self.__dsl_Type400

    @dsl_Type400.setter
    def dsl_Type400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type400", None)
        self.__dsl_Type400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ForStatement399"):
                opp_val = getattr(old_value, "dsl_ForStatement399", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ForStatement399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ForStatement399"):
                opp_val = getattr(value, "dsl_ForStatement399", None)
                setattr(value, "dsl_ForStatement399", self)

    @property
    def dsl_Type226(self):
        return self.__dsl_Type226

    @dsl_Type226.setter
    def dsl_Type226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type226", None)
        self.__dsl_Type226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_CastExpression225"):
                opp_val = getattr(old_value, "dsl_CastExpression225", None)
                if opp_val == self:
                    setattr(old_value, "dsl_CastExpression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_CastExpression225"):
                opp_val = getattr(value, "dsl_CastExpression225", None)
                setattr(value, "dsl_CastExpression225", self)

    @property
    def dsl_Type215(self):
        return self.__dsl_Type215

    @dsl_Type215.setter
    def dsl_Type215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type215", None)
        self.__dsl_Type215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_CastLookahead"):
                opp_val = getattr(old_value, "dsl_CastLookahead", None)
                if opp_val == self:
                    setattr(old_value, "dsl_CastLookahead", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_CastLookahead"):
                opp_val = getattr(value, "dsl_CastLookahead", None)
                setattr(value, "dsl_CastLookahead", self)

    @property
    def dsl_Type477(self):
        return self.__dsl_Type477

    @dsl_Type477.setter
    def dsl_Type477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type477", None)
        self.__dsl_Type477 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeMemberDeclaration476"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeMemberDeclaration476", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeMemberDeclaration476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeMemberDeclaration476"):
                opp_val = getattr(value, "dsl_AnnotationTypeMemberDeclaration476", None)
                setattr(value, "dsl_AnnotationTypeMemberDeclaration476", self)

    @property
    def dsl_Type127(self):
        return self.__dsl_Type127

    @dsl_Type127.setter
    def dsl_Type127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type127", None)
        self.__dsl_Type127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReferenceType"):
                opp_val = getattr(old_value, "dsl_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReferenceType"):
                opp_val = getattr(value, "dsl_ReferenceType", None)
                setattr(value, "dsl_ReferenceType", self)

    @property
    def dsl_Type183(self):
        return self.__dsl_Type183

    @dsl_Type183.setter
    def dsl_Type183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type183", None)
        self.__dsl_Type183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_InstanceOfExpression182"):
                opp_val = getattr(old_value, "dsl_InstanceOfExpression182", None)
                if opp_val == self:
                    setattr(old_value, "dsl_InstanceOfExpression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_InstanceOfExpression182"):
                opp_val = getattr(value, "dsl_InstanceOfExpression182", None)
                setattr(value, "dsl_InstanceOfExpression182", self)

class dsl_FieldDeclaration:

    pass
class dsl_MethodOrCtorDeclaration:

    def __init__(self, id: str, dsl_MethodOrCtorDeclaration: "dsl_ClassOrInterfaceBodyDeclaration" = None, dsl_MethodOrCtorDeclaration106: "dsl_Block" = None, dsl_MethodOrCtorDeclaration91: "dsl_TypeParameters" = None, dsl_MethodOrCtorDeclaration94: "dsl_FormalParameters" = None, dsl_MethodOrCtorDeclaration96: "dsl_NameList" = None, dsl_MethodOrCtorDeclaration98: "dsl_ExplicitConstructorInvocation" = None, dsl_MethodOrCtorDeclaration100: set["dsl_BlockStatement"] = None, dsl_MethodOrCtorDeclaration102: "dsl_ResultType" = None, dsl_MethodOrCtorDeclaration104: "dsl_MethodDeclarator" = None):
        self.id = id
        self.dsl_MethodOrCtorDeclaration = dsl_MethodOrCtorDeclaration
        self.dsl_MethodOrCtorDeclaration106 = dsl_MethodOrCtorDeclaration106
        self.dsl_MethodOrCtorDeclaration91 = dsl_MethodOrCtorDeclaration91
        self.dsl_MethodOrCtorDeclaration94 = dsl_MethodOrCtorDeclaration94
        self.dsl_MethodOrCtorDeclaration96 = dsl_MethodOrCtorDeclaration96
        self.dsl_MethodOrCtorDeclaration98 = dsl_MethodOrCtorDeclaration98
        self.dsl_MethodOrCtorDeclaration100 = dsl_MethodOrCtorDeclaration100 if dsl_MethodOrCtorDeclaration100 is not None else set()
        self.dsl_MethodOrCtorDeclaration102 = dsl_MethodOrCtorDeclaration102
        self.dsl_MethodOrCtorDeclaration104 = dsl_MethodOrCtorDeclaration104
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_MethodOrCtorDeclaration104(self):
        return self.__dsl_MethodOrCtorDeclaration104

    @dsl_MethodOrCtorDeclaration104.setter
    def dsl_MethodOrCtorDeclaration104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration104", None)
        self.__dsl_MethodOrCtorDeclaration104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MethodDeclarator"):
                opp_val = getattr(old_value, "dsl_MethodDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MethodDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MethodDeclarator"):
                opp_val = getattr(value, "dsl_MethodDeclarator", None)
                setattr(value, "dsl_MethodDeclarator", self)

    @property
    def dsl_MethodOrCtorDeclaration100(self):
        return self.__dsl_MethodOrCtorDeclaration100

    @dsl_MethodOrCtorDeclaration100.setter
    def dsl_MethodOrCtorDeclaration100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration100", None)
        self.__dsl_MethodOrCtorDeclaration100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_BlockStatement"):
                    opp_val = getattr(item, "dsl_BlockStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_BlockStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_BlockStatement"):
                    opp_val = getattr(item, "dsl_BlockStatement", None)
                    
                    setattr(item, "dsl_BlockStatement", self)
                    

    @property
    def dsl_MethodOrCtorDeclaration106(self):
        return self.__dsl_MethodOrCtorDeclaration106

    @dsl_MethodOrCtorDeclaration106.setter
    def dsl_MethodOrCtorDeclaration106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration106", None)
        self.__dsl_MethodOrCtorDeclaration106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Block"):
                opp_val = getattr(old_value, "dsl_Block", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Block"):
                opp_val = getattr(value, "dsl_Block", None)
                setattr(value, "dsl_Block", self)

    @property
    def dsl_MethodOrCtorDeclaration102(self):
        return self.__dsl_MethodOrCtorDeclaration102

    @dsl_MethodOrCtorDeclaration102.setter
    def dsl_MethodOrCtorDeclaration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration102", None)
        self.__dsl_MethodOrCtorDeclaration102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ResultType"):
                opp_val = getattr(old_value, "dsl_ResultType", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ResultType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ResultType"):
                opp_val = getattr(value, "dsl_ResultType", None)
                setattr(value, "dsl_ResultType", self)

    @property
    def dsl_MethodOrCtorDeclaration(self):
        return self.__dsl_MethodOrCtorDeclaration

    @dsl_MethodOrCtorDeclaration.setter
    def dsl_MethodOrCtorDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration", None)
        self.__dsl_MethodOrCtorDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration72"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration72", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBodyDeclaration72"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBodyDeclaration72", None)
                setattr(value, "dsl_ClassOrInterfaceBodyDeclaration72", self)

    @property
    def dsl_MethodOrCtorDeclaration98(self):
        return self.__dsl_MethodOrCtorDeclaration98

    @dsl_MethodOrCtorDeclaration98.setter
    def dsl_MethodOrCtorDeclaration98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration98", None)
        self.__dsl_MethodOrCtorDeclaration98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ExplicitConstructorInvocation"):
                opp_val = getattr(old_value, "dsl_ExplicitConstructorInvocation", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ExplicitConstructorInvocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ExplicitConstructorInvocation"):
                opp_val = getattr(value, "dsl_ExplicitConstructorInvocation", None)
                setattr(value, "dsl_ExplicitConstructorInvocation", self)

    @property
    def dsl_MethodOrCtorDeclaration96(self):
        return self.__dsl_MethodOrCtorDeclaration96

    @dsl_MethodOrCtorDeclaration96.setter
    def dsl_MethodOrCtorDeclaration96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration96", None)
        self.__dsl_MethodOrCtorDeclaration96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_NameList"):
                opp_val = getattr(old_value, "dsl_NameList", None)
                if opp_val == self:
                    setattr(old_value, "dsl_NameList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_NameList"):
                opp_val = getattr(value, "dsl_NameList", None)
                setattr(value, "dsl_NameList", self)

    @property
    def dsl_MethodOrCtorDeclaration94(self):
        return self.__dsl_MethodOrCtorDeclaration94

    @dsl_MethodOrCtorDeclaration94.setter
    def dsl_MethodOrCtorDeclaration94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration94", None)
        self.__dsl_MethodOrCtorDeclaration94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_FormalParameters"):
                opp_val = getattr(old_value, "dsl_FormalParameters", None)
                if opp_val == self:
                    setattr(old_value, "dsl_FormalParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_FormalParameters"):
                opp_val = getattr(value, "dsl_FormalParameters", None)
                setattr(value, "dsl_FormalParameters", self)

    @property
    def dsl_MethodOrCtorDeclaration91(self):
        return self.__dsl_MethodOrCtorDeclaration91

    @dsl_MethodOrCtorDeclaration91.setter
    def dsl_MethodOrCtorDeclaration91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodOrCtorDeclaration__dsl_MethodOrCtorDeclaration91", None)
        self.__dsl_MethodOrCtorDeclaration91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeParameters92"):
                opp_val = getattr(old_value, "dsl_TypeParameters92", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeParameters92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeParameters92"):
                opp_val = getattr(value, "dsl_TypeParameters92", None)
                setattr(value, "dsl_TypeParameters92", self)

class dsl_Expression(IfStatement):

    def __init__(self, assignOp: str, dsl_Expression: "dsl_VariableInitializer" = None, dsl_Expression166: "dsl_ConditionalExpression" = None, dsl_Expression150: "dsl_ConditionalExpression" = None, dsl_Expression153: "dsl_Expression" = None, dsl_Expression151: "dsl_Expression" = None, dsl_Expression155: "dsl_Statement" = None, dsl_Expression157: "dsl_Statement" = None, dsl_Expression163: "dsl_ConditionalExpression" = None, dsl_Expression238: "dsl_PrimaryPrefix" = None, dsl_Expression254: "dsl_PrimarySuffix" = None, dsl_Expression285: "dsl_ArgumentList" = None, dsl_Expression302: "dsl_ArrayDimsAndInits" = None, dsl_Expression342: "dsl_AssertStatement" = None, dsl_Expression339: "dsl_AssertStatement" = None, dsl_Expression374: "dsl_StatementExpression" = None, dsl_Expression385: "dsl_SwitchLabel" = None, dsl_Expression388: "dsl_WhileStatement" = None, dsl_Expression377: "dsl_SwitchStatement" = None, dsl_Expression397: "dsl_DoStatement" = None, dsl_Expression403: "dsl_ForStatement" = None, dsl_Expression408: "dsl_ForStatement" = None, dsl_Expression427: "dsl_ReturnStatement" = None, dsl_Expression430: "dsl_ThrowStatement" = None, dsl_Expression433: "dsl_SynchronizedStatement" = None):
        self.assignOp = assignOp
        self.dsl_Expression = dsl_Expression
        self.dsl_Expression166 = dsl_Expression166
        self.dsl_Expression150 = dsl_Expression150
        self.dsl_Expression153 = dsl_Expression153
        self.dsl_Expression151 = dsl_Expression151
        self.dsl_Expression155 = dsl_Expression155
        self.dsl_Expression157 = dsl_Expression157
        self.dsl_Expression163 = dsl_Expression163
        self.dsl_Expression238 = dsl_Expression238
        self.dsl_Expression254 = dsl_Expression254
        self.dsl_Expression285 = dsl_Expression285
        self.dsl_Expression302 = dsl_Expression302
        self.dsl_Expression342 = dsl_Expression342
        self.dsl_Expression339 = dsl_Expression339
        self.dsl_Expression374 = dsl_Expression374
        self.dsl_Expression385 = dsl_Expression385
        self.dsl_Expression388 = dsl_Expression388
        self.dsl_Expression377 = dsl_Expression377
        self.dsl_Expression397 = dsl_Expression397
        self.dsl_Expression403 = dsl_Expression403
        self.dsl_Expression408 = dsl_Expression408
        self.dsl_Expression427 = dsl_Expression427
        self.dsl_Expression430 = dsl_Expression430
        self.dsl_Expression433 = dsl_Expression433
        
    @property
    def assignOp(self) -> str:
        return self.__assignOp

    @assignOp.setter
    def assignOp(self, assignOp: str):
        self.__assignOp = assignOp

    @property
    def dsl_Expression427(self):
        return self.__dsl_Expression427

    @dsl_Expression427.setter
    def dsl_Expression427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression427", None)
        self.__dsl_Expression427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReturnStatement426"):
                opp_val = getattr(old_value, "dsl_ReturnStatement426", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReturnStatement426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReturnStatement426"):
                opp_val = getattr(value, "dsl_ReturnStatement426", None)
                setattr(value, "dsl_ReturnStatement426", self)

    @property
    def dsl_Expression155(self):
        return self.__dsl_Expression155

    @dsl_Expression155.setter
    def dsl_Expression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression155", None)
        self.__dsl_Expression155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement"):
                opp_val = getattr(old_value, "dsl_Statement", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement"):
                opp_val = getattr(value, "dsl_Statement", None)
                setattr(value, "dsl_Statement", self)

    @property
    def dsl_Expression153(self):
        return self.__dsl_Expression153

    @dsl_Expression153.setter
    def dsl_Expression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression153", None)
        self.__dsl_Expression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression151"):
                opp_val = getattr(old_value, "dsl_Expression151", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression151"):
                opp_val = getattr(value, "dsl_Expression151", None)
                setattr(value, "dsl_Expression151", self)

    @property
    def dsl_Expression388(self):
        return self.__dsl_Expression388

    @dsl_Expression388.setter
    def dsl_Expression388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression388", None)
        self.__dsl_Expression388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_WhileStatement387"):
                opp_val = getattr(old_value, "dsl_WhileStatement387", None)
                if opp_val == self:
                    setattr(old_value, "dsl_WhileStatement387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_WhileStatement387"):
                opp_val = getattr(value, "dsl_WhileStatement387", None)
                setattr(value, "dsl_WhileStatement387", self)

    @property
    def dsl_Expression302(self):
        return self.__dsl_Expression302

    @dsl_Expression302.setter
    def dsl_Expression302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression302", None)
        self.__dsl_Expression302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ArrayDimsAndInits301"):
                opp_val = getattr(old_value, "dsl_ArrayDimsAndInits301", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ArrayDimsAndInits301"):
                opp_val = getattr(value, "dsl_ArrayDimsAndInits301", None)
                if opp_val is None:
                    setattr(value, "dsl_ArrayDimsAndInits301", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Expression339(self):
        return self.__dsl_Expression339

    @dsl_Expression339.setter
    def dsl_Expression339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression339", None)
        self.__dsl_Expression339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AssertStatement338"):
                opp_val = getattr(old_value, "dsl_AssertStatement338", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AssertStatement338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AssertStatement338"):
                opp_val = getattr(value, "dsl_AssertStatement338", None)
                setattr(value, "dsl_AssertStatement338", self)

    @property
    def dsl_Expression238(self):
        return self.__dsl_Expression238

    @dsl_Expression238.setter
    def dsl_Expression238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression238", None)
        self.__dsl_Expression238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryPrefix237"):
                opp_val = getattr(old_value, "dsl_PrimaryPrefix237", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryPrefix237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryPrefix237"):
                opp_val = getattr(value, "dsl_PrimaryPrefix237", None)
                setattr(value, "dsl_PrimaryPrefix237", self)

    @property
    def dsl_Expression377(self):
        return self.__dsl_Expression377

    @dsl_Expression377.setter
    def dsl_Expression377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression377", None)
        self.__dsl_Expression377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SwitchStatement376"):
                opp_val = getattr(old_value, "dsl_SwitchStatement376", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SwitchStatement376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SwitchStatement376"):
                opp_val = getattr(value, "dsl_SwitchStatement376", None)
                setattr(value, "dsl_SwitchStatement376", self)

    @property
    def dsl_Expression254(self):
        return self.__dsl_Expression254

    @dsl_Expression254.setter
    def dsl_Expression254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression254", None)
        self.__dsl_Expression254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimarySuffix253"):
                opp_val = getattr(old_value, "dsl_PrimarySuffix253", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimarySuffix253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimarySuffix253"):
                opp_val = getattr(value, "dsl_PrimarySuffix253", None)
                setattr(value, "dsl_PrimarySuffix253", self)

    @property
    def dsl_Expression166(self):
        return self.__dsl_Expression166

    @dsl_Expression166.setter
    def dsl_Expression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression166", None)
        self.__dsl_Expression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ConditionalExpression165"):
                opp_val = getattr(old_value, "dsl_ConditionalExpression165", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ConditionalExpression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ConditionalExpression165"):
                opp_val = getattr(value, "dsl_ConditionalExpression165", None)
                setattr(value, "dsl_ConditionalExpression165", self)

    @property
    def dsl_Expression(self):
        return self.__dsl_Expression

    @dsl_Expression.setter
    def dsl_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression", None)
        self.__dsl_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_VariableInitializer86"):
                opp_val = getattr(old_value, "dsl_VariableInitializer86", None)
                if opp_val == self:
                    setattr(old_value, "dsl_VariableInitializer86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_VariableInitializer86"):
                opp_val = getattr(value, "dsl_VariableInitializer86", None)
                setattr(value, "dsl_VariableInitializer86", self)

    @property
    def dsl_Expression433(self):
        return self.__dsl_Expression433

    @dsl_Expression433.setter
    def dsl_Expression433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression433", None)
        self.__dsl_Expression433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SynchronizedStatement432"):
                opp_val = getattr(old_value, "dsl_SynchronizedStatement432", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SynchronizedStatement432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SynchronizedStatement432"):
                opp_val = getattr(value, "dsl_SynchronizedStatement432", None)
                setattr(value, "dsl_SynchronizedStatement432", self)

    @property
    def dsl_Expression374(self):
        return self.__dsl_Expression374

    @dsl_Expression374.setter
    def dsl_Expression374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression374", None)
        self.__dsl_Expression374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_StatementExpression373"):
                opp_val = getattr(old_value, "dsl_StatementExpression373", None)
                if opp_val == self:
                    setattr(old_value, "dsl_StatementExpression373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_StatementExpression373"):
                opp_val = getattr(value, "dsl_StatementExpression373", None)
                setattr(value, "dsl_StatementExpression373", self)

    @property
    def dsl_Expression157(self):
        return self.__dsl_Expression157

    @dsl_Expression157.setter
    def dsl_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression157", None)
        self.__dsl_Expression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statement158"):
                opp_val = getattr(old_value, "dsl_Statement158", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statement158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statement158"):
                opp_val = getattr(value, "dsl_Statement158", None)
                setattr(value, "dsl_Statement158", self)

    @property
    def dsl_Expression342(self):
        return self.__dsl_Expression342

    @dsl_Expression342.setter
    def dsl_Expression342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression342", None)
        self.__dsl_Expression342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AssertStatement341"):
                opp_val = getattr(old_value, "dsl_AssertStatement341", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AssertStatement341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AssertStatement341"):
                opp_val = getattr(value, "dsl_AssertStatement341", None)
                setattr(value, "dsl_AssertStatement341", self)

    @property
    def dsl_Expression403(self):
        return self.__dsl_Expression403

    @dsl_Expression403.setter
    def dsl_Expression403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression403", None)
        self.__dsl_Expression403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ForStatement402"):
                opp_val = getattr(old_value, "dsl_ForStatement402", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ForStatement402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ForStatement402"):
                opp_val = getattr(value, "dsl_ForStatement402", None)
                setattr(value, "dsl_ForStatement402", self)

    @property
    def dsl_Expression397(self):
        return self.__dsl_Expression397

    @dsl_Expression397.setter
    def dsl_Expression397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression397", None)
        self.__dsl_Expression397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_DoStatement396"):
                opp_val = getattr(old_value, "dsl_DoStatement396", None)
                if opp_val == self:
                    setattr(old_value, "dsl_DoStatement396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_DoStatement396"):
                opp_val = getattr(value, "dsl_DoStatement396", None)
                setattr(value, "dsl_DoStatement396", self)

    @property
    def dsl_Expression408(self):
        return self.__dsl_Expression408

    @dsl_Expression408.setter
    def dsl_Expression408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression408", None)
        self.__dsl_Expression408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ForStatement407"):
                opp_val = getattr(old_value, "dsl_ForStatement407", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ForStatement407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ForStatement407"):
                opp_val = getattr(value, "dsl_ForStatement407", None)
                setattr(value, "dsl_ForStatement407", self)

    @property
    def dsl_Expression385(self):
        return self.__dsl_Expression385

    @dsl_Expression385.setter
    def dsl_Expression385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression385", None)
        self.__dsl_Expression385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SwitchLabel384"):
                opp_val = getattr(old_value, "dsl_SwitchLabel384", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SwitchLabel384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SwitchLabel384"):
                opp_val = getattr(value, "dsl_SwitchLabel384", None)
                setattr(value, "dsl_SwitchLabel384", self)

    @property
    def dsl_Expression163(self):
        return self.__dsl_Expression163

    @dsl_Expression163.setter
    def dsl_Expression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression163", None)
        self.__dsl_Expression163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ConditionalExpression162"):
                opp_val = getattr(old_value, "dsl_ConditionalExpression162", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ConditionalExpression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ConditionalExpression162"):
                opp_val = getattr(value, "dsl_ConditionalExpression162", None)
                setattr(value, "dsl_ConditionalExpression162", self)

    @property
    def dsl_Expression430(self):
        return self.__dsl_Expression430

    @dsl_Expression430.setter
    def dsl_Expression430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression430", None)
        self.__dsl_Expression430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ThrowStatement429"):
                opp_val = getattr(old_value, "dsl_ThrowStatement429", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ThrowStatement429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ThrowStatement429"):
                opp_val = getattr(value, "dsl_ThrowStatement429", None)
                setattr(value, "dsl_ThrowStatement429", self)

    @property
    def dsl_Expression151(self):
        return self.__dsl_Expression151

    @dsl_Expression151.setter
    def dsl_Expression151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression151", None)
        self.__dsl_Expression151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression153"):
                opp_val = getattr(old_value, "dsl_Expression153", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression153"):
                opp_val = getattr(value, "dsl_Expression153", None)
                setattr(value, "dsl_Expression153", self)

    @property
    def dsl_Expression150(self):
        return self.__dsl_Expression150

    @dsl_Expression150.setter
    def dsl_Expression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression150", None)
        self.__dsl_Expression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ConditionalExpression"):
                opp_val = getattr(old_value, "dsl_ConditionalExpression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ConditionalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ConditionalExpression"):
                opp_val = getattr(value, "dsl_ConditionalExpression", None)
                setattr(value, "dsl_ConditionalExpression", self)

    @property
    def dsl_Expression285(self):
        return self.__dsl_Expression285

    @dsl_Expression285.setter
    def dsl_Expression285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression285", None)
        self.__dsl_Expression285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ArgumentList284"):
                opp_val = getattr(old_value, "dsl_ArgumentList284", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ArgumentList284"):
                opp_val = getattr(value, "dsl_ArgumentList284", None)
                if opp_val is None:
                    setattr(value, "dsl_ArgumentList284", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_ArrayInitializer:

    pass
class dsl_Initializer:

    def __init__(self, static: bool, dsl_Initializer: "dsl_ClassOrInterfaceBodyDeclaration" = None, dsl_Initializer124: "dsl_Block" = None):
        self.static = static
        self.dsl_Initializer = dsl_Initializer
        self.dsl_Initializer124 = dsl_Initializer124
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def dsl_Initializer(self):
        return self.__dsl_Initializer

    @dsl_Initializer.setter
    def dsl_Initializer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Initializer__dsl_Initializer", None)
        self.__dsl_Initializer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration61"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration61", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBodyDeclaration61"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBodyDeclaration61", None)
                setattr(value, "dsl_ClassOrInterfaceBodyDeclaration61", self)

    @property
    def dsl_Initializer124(self):
        return self.__dsl_Initializer124

    @dsl_Initializer124.setter
    def dsl_Initializer124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Initializer__dsl_Initializer124", None)
        self.__dsl_Initializer124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Block125"):
                opp_val = getattr(old_value, "dsl_Block125", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Block125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Block125"):
                opp_val = getattr(value, "dsl_Block125", None)
                setattr(value, "dsl_Block125", self)

class dsl_TypeBound:

    pass
class dsl_TypeParameter:

    def __init__(self, id: str, dsl_TypeParameter: "dsl_TypeParameters" = None, dsl_TypeParameter53: "dsl_TypeBound" = None):
        self.id = id
        self.dsl_TypeParameter = dsl_TypeParameter
        self.dsl_TypeParameter53 = dsl_TypeParameter53
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_TypeParameter(self):
        return self.__dsl_TypeParameter

    @dsl_TypeParameter.setter
    def dsl_TypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_TypeParameter__dsl_TypeParameter", None)
        self.__dsl_TypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeParameters51"):
                opp_val = getattr(old_value, "dsl_TypeParameters51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeParameters51"):
                opp_val = getattr(value, "dsl_TypeParameters51", None)
                if opp_val is None:
                    setattr(value, "dsl_TypeParameters51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_TypeParameter53(self):
        return self.__dsl_TypeParameter53

    @dsl_TypeParameter53.setter
    def dsl_TypeParameter53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_TypeParameter__dsl_TypeParameter53", None)
        self.__dsl_TypeParameter53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeBound"):
                opp_val = getattr(old_value, "dsl_TypeBound", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeBound", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeBound"):
                opp_val = getattr(value, "dsl_TypeBound", None)
                setattr(value, "dsl_TypeBound", self)

class dsl_EnumConstant:

    def __init__(self, id: str, dsl_EnumConstant: "dsl_EnumBody" = None, dsl_EnumConstant46: "dsl_Arguments" = None, dsl_EnumConstant48: "dsl_ClassOrInterfaceBody" = None):
        self.id = id
        self.dsl_EnumConstant = dsl_EnumConstant
        self.dsl_EnumConstant46 = dsl_EnumConstant46
        self.dsl_EnumConstant48 = dsl_EnumConstant48
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_EnumConstant48(self):
        return self.__dsl_EnumConstant48

    @dsl_EnumConstant48.setter
    def dsl_EnumConstant48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumConstant__dsl_EnumConstant48", None)
        self.__dsl_EnumConstant48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBody49"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBody49", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBody49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBody49"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBody49", None)
                setattr(value, "dsl_ClassOrInterfaceBody49", self)

    @property
    def dsl_EnumConstant46(self):
        return self.__dsl_EnumConstant46

    @dsl_EnumConstant46.setter
    def dsl_EnumConstant46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumConstant__dsl_EnumConstant46", None)
        self.__dsl_EnumConstant46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Arguments"):
                opp_val = getattr(old_value, "dsl_Arguments", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Arguments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Arguments"):
                opp_val = getattr(value, "dsl_Arguments", None)
                setattr(value, "dsl_Arguments", self)

    @property
    def dsl_EnumConstant(self):
        return self.__dsl_EnumConstant

    @dsl_EnumConstant.setter
    def dsl_EnumConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumConstant__dsl_EnumConstant", None)
        self.__dsl_EnumConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_EnumBody42"):
                opp_val = getattr(old_value, "dsl_EnumBody42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_EnumBody42"):
                opp_val = getattr(value, "dsl_EnumBody42", None)
                if opp_val is None:
                    setattr(value, "dsl_EnumBody42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_EnumBody:

    pass
class dsl_ClassOrInterfaceType:

    def __init__(self, ids: str, dsl_ClassOrInterfaceType: "dsl_ExtendsList" = None, dsl_ClassOrInterfaceType32: "dsl_ExtendsList" = None, dsl_ClassOrInterfaceType35: "dsl_ImplementsList" = None, dsl_ClassOrInterfaceType56: "dsl_TypeBound" = None, dsl_ClassOrInterfaceType130: "dsl_ReferenceType" = None, dsl_ClassOrInterfaceType132: set["dsl_TypeArguments"] = None, dsl_ClassOrInterfaceType290: "dsl_AllocationExpression" = None):
        self.ids = ids
        self.dsl_ClassOrInterfaceType = dsl_ClassOrInterfaceType
        self.dsl_ClassOrInterfaceType32 = dsl_ClassOrInterfaceType32
        self.dsl_ClassOrInterfaceType35 = dsl_ClassOrInterfaceType35
        self.dsl_ClassOrInterfaceType56 = dsl_ClassOrInterfaceType56
        self.dsl_ClassOrInterfaceType130 = dsl_ClassOrInterfaceType130
        self.dsl_ClassOrInterfaceType132 = dsl_ClassOrInterfaceType132 if dsl_ClassOrInterfaceType132 is not None else set()
        self.dsl_ClassOrInterfaceType290 = dsl_ClassOrInterfaceType290
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def dsl_ClassOrInterfaceType35(self):
        return self.__dsl_ClassOrInterfaceType35

    @dsl_ClassOrInterfaceType35.setter
    def dsl_ClassOrInterfaceType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType35", None)
        self.__dsl_ClassOrInterfaceType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ImplementsList34"):
                opp_val = getattr(old_value, "dsl_ImplementsList34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ImplementsList34"):
                opp_val = getattr(value, "dsl_ImplementsList34", None)
                if opp_val is None:
                    setattr(value, "dsl_ImplementsList34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_ClassOrInterfaceType32(self):
        return self.__dsl_ClassOrInterfaceType32

    @dsl_ClassOrInterfaceType32.setter
    def dsl_ClassOrInterfaceType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType32", None)
        self.__dsl_ClassOrInterfaceType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ExtendsList31"):
                opp_val = getattr(old_value, "dsl_ExtendsList31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ExtendsList31"):
                opp_val = getattr(value, "dsl_ExtendsList31", None)
                if opp_val is None:
                    setattr(value, "dsl_ExtendsList31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_ClassOrInterfaceType290(self):
        return self.__dsl_ClassOrInterfaceType290

    @dsl_ClassOrInterfaceType290.setter
    def dsl_ClassOrInterfaceType290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType290", None)
        self.__dsl_ClassOrInterfaceType290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AllocationExpression289"):
                opp_val = getattr(old_value, "dsl_AllocationExpression289", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AllocationExpression289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AllocationExpression289"):
                opp_val = getattr(value, "dsl_AllocationExpression289", None)
                setattr(value, "dsl_AllocationExpression289", self)

    @property
    def dsl_ClassOrInterfaceType(self):
        return self.__dsl_ClassOrInterfaceType

    @dsl_ClassOrInterfaceType.setter
    def dsl_ClassOrInterfaceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType", None)
        self.__dsl_ClassOrInterfaceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ExtendsList29"):
                opp_val = getattr(old_value, "dsl_ExtendsList29", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ExtendsList29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ExtendsList29"):
                opp_val = getattr(value, "dsl_ExtendsList29", None)
                setattr(value, "dsl_ExtendsList29", self)

    @property
    def dsl_ClassOrInterfaceType132(self):
        return self.__dsl_ClassOrInterfaceType132

    @dsl_ClassOrInterfaceType132.setter
    def dsl_ClassOrInterfaceType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType132", None)
        self.__dsl_ClassOrInterfaceType132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_TypeArguments"):
                    opp_val = getattr(item, "dsl_TypeArguments", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_TypeArguments", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_TypeArguments"):
                    opp_val = getattr(item, "dsl_TypeArguments", None)
                    
                    setattr(item, "dsl_TypeArguments", self)
                    

    @property
    def dsl_ClassOrInterfaceType130(self):
        return self.__dsl_ClassOrInterfaceType130

    @dsl_ClassOrInterfaceType130.setter
    def dsl_ClassOrInterfaceType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType130", None)
        self.__dsl_ClassOrInterfaceType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReferenceType129"):
                opp_val = getattr(old_value, "dsl_ReferenceType129", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReferenceType129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReferenceType129"):
                opp_val = getattr(value, "dsl_ReferenceType129", None)
                setattr(value, "dsl_ReferenceType129", self)

    @property
    def dsl_ClassOrInterfaceType56(self):
        return self.__dsl_ClassOrInterfaceType56

    @dsl_ClassOrInterfaceType56.setter
    def dsl_ClassOrInterfaceType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceType__dsl_ClassOrInterfaceType56", None)
        self.__dsl_ClassOrInterfaceType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeBound55"):
                opp_val = getattr(old_value, "dsl_TypeBound55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeBound55"):
                opp_val = getattr(value, "dsl_TypeBound55", None)
                if opp_val is None:
                    setattr(value, "dsl_TypeBound55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_ClassOrInterfaceBody:

    pass
class dsl_Arguments:

    pass
class dsl_ClassOrInterfaceBodyDeclaration:

    pass
class dsl_AnnotationTypeDeclaration:

    def __init__(self, id: str, dsl_AnnotationTypeDeclaration: "dsl_TypeDeclaration" = None, dsl_AnnotationTypeDeclaration469: "dsl_AnnotationTypeBody" = None, dsl_AnnotationTypeDeclaration488: "dsl_AnnotationTypeMemberDeclaration" = None):
        self.id = id
        self.dsl_AnnotationTypeDeclaration = dsl_AnnotationTypeDeclaration
        self.dsl_AnnotationTypeDeclaration469 = dsl_AnnotationTypeDeclaration469
        self.dsl_AnnotationTypeDeclaration488 = dsl_AnnotationTypeDeclaration488
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_AnnotationTypeDeclaration469(self):
        return self.__dsl_AnnotationTypeDeclaration469

    @dsl_AnnotationTypeDeclaration469.setter
    def dsl_AnnotationTypeDeclaration469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeDeclaration__dsl_AnnotationTypeDeclaration469", None)
        self.__dsl_AnnotationTypeDeclaration469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeBody"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeBody", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeBody"):
                opp_val = getattr(value, "dsl_AnnotationTypeBody", None)
                setattr(value, "dsl_AnnotationTypeBody", self)

    @property
    def dsl_AnnotationTypeDeclaration(self):
        return self.__dsl_AnnotationTypeDeclaration

    @dsl_AnnotationTypeDeclaration.setter
    def dsl_AnnotationTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeDeclaration__dsl_AnnotationTypeDeclaration", None)
        self.__dsl_AnnotationTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeDeclaration19"):
                opp_val = getattr(old_value, "dsl_TypeDeclaration19", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeDeclaration19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeDeclaration19"):
                opp_val = getattr(value, "dsl_TypeDeclaration19", None)
                setattr(value, "dsl_TypeDeclaration19", self)

    @property
    def dsl_AnnotationTypeDeclaration488(self):
        return self.__dsl_AnnotationTypeDeclaration488

    @dsl_AnnotationTypeDeclaration488.setter
    def dsl_AnnotationTypeDeclaration488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AnnotationTypeDeclaration__dsl_AnnotationTypeDeclaration488", None)
        self.__dsl_AnnotationTypeDeclaration488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeMemberDeclaration487"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeMemberDeclaration487", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeMemberDeclaration487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeMemberDeclaration487"):
                opp_val = getattr(value, "dsl_AnnotationTypeMemberDeclaration487", None)
                setattr(value, "dsl_AnnotationTypeMemberDeclaration487", self)

class dsl_EnumDeclaration:

    def __init__(self, id: str, dsl_EnumDeclaration: "dsl_TypeDeclaration" = None, dsl_EnumDeclaration37: set["dsl_ImplementsList"] = None, dsl_EnumDeclaration40: "dsl_EnumBody" = None, dsl_EnumDeclaration70: "dsl_ClassOrInterfaceBodyDeclaration" = None, dsl_EnumDeclaration485: "dsl_AnnotationTypeMemberDeclaration" = None):
        self.id = id
        self.dsl_EnumDeclaration = dsl_EnumDeclaration
        self.dsl_EnumDeclaration37 = dsl_EnumDeclaration37 if dsl_EnumDeclaration37 is not None else set()
        self.dsl_EnumDeclaration40 = dsl_EnumDeclaration40
        self.dsl_EnumDeclaration70 = dsl_EnumDeclaration70
        self.dsl_EnumDeclaration485 = dsl_EnumDeclaration485
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_EnumDeclaration(self):
        return self.__dsl_EnumDeclaration

    @dsl_EnumDeclaration.setter
    def dsl_EnumDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumDeclaration__dsl_EnumDeclaration", None)
        self.__dsl_EnumDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeDeclaration17"):
                opp_val = getattr(old_value, "dsl_TypeDeclaration17", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeDeclaration17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeDeclaration17"):
                opp_val = getattr(value, "dsl_TypeDeclaration17", None)
                setattr(value, "dsl_TypeDeclaration17", self)

    @property
    def dsl_EnumDeclaration40(self):
        return self.__dsl_EnumDeclaration40

    @dsl_EnumDeclaration40.setter
    def dsl_EnumDeclaration40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumDeclaration__dsl_EnumDeclaration40", None)
        self.__dsl_EnumDeclaration40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_EnumBody"):
                opp_val = getattr(old_value, "dsl_EnumBody", None)
                if opp_val == self:
                    setattr(old_value, "dsl_EnumBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_EnumBody"):
                opp_val = getattr(value, "dsl_EnumBody", None)
                setattr(value, "dsl_EnumBody", self)

    @property
    def dsl_EnumDeclaration37(self):
        return self.__dsl_EnumDeclaration37

    @dsl_EnumDeclaration37.setter
    def dsl_EnumDeclaration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumDeclaration__dsl_EnumDeclaration37", None)
        self.__dsl_EnumDeclaration37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_ImplementsList38"):
                    opp_val = getattr(item, "dsl_ImplementsList38", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_ImplementsList38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_ImplementsList38"):
                    opp_val = getattr(item, "dsl_ImplementsList38", None)
                    
                    setattr(item, "dsl_ImplementsList38", self)
                    

    @property
    def dsl_EnumDeclaration70(self):
        return self.__dsl_EnumDeclaration70

    @dsl_EnumDeclaration70.setter
    def dsl_EnumDeclaration70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumDeclaration__dsl_EnumDeclaration70", None)
        self.__dsl_EnumDeclaration70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration69"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration69", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBodyDeclaration69"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBodyDeclaration69", None)
                setattr(value, "dsl_ClassOrInterfaceBodyDeclaration69", self)

    @property
    def dsl_EnumDeclaration485(self):
        return self.__dsl_EnumDeclaration485

    @dsl_EnumDeclaration485.setter
    def dsl_EnumDeclaration485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EnumDeclaration__dsl_EnumDeclaration485", None)
        self.__dsl_EnumDeclaration485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeMemberDeclaration484"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeMemberDeclaration484", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeMemberDeclaration484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeMemberDeclaration484"):
                opp_val = getattr(value, "dsl_AnnotationTypeMemberDeclaration484", None)
                setattr(value, "dsl_AnnotationTypeMemberDeclaration484", self)

class dsl_ClassOrInterfaceDeclaration:

    def __init__(self, typeCategory: str, id: str, dsl_ClassOrInterfaceDeclaration21: set["dsl_TypeParameters"] = None, dsl_ClassOrInterfaceDeclaration23: "dsl_ExtendsList" = None, dsl_ClassOrInterfaceDeclaration25: set["dsl_ImplementsList"] = None, dsl_ClassOrInterfaceDeclaration: "dsl_TypeDeclaration" = None, dsl_ClassOrInterfaceDeclaration27: "dsl_ClassOrInterfaceBody" = None, dsl_ClassOrInterfaceDeclaration67: "dsl_ClassOrInterfaceBodyDeclaration" = None, dsl_ClassOrInterfaceDeclaration356: "dsl_BlockStatement" = None, dsl_ClassOrInterfaceDeclaration482: "dsl_AnnotationTypeMemberDeclaration" = None):
        self.typeCategory = typeCategory
        self.id = id
        self.dsl_ClassOrInterfaceDeclaration21 = dsl_ClassOrInterfaceDeclaration21 if dsl_ClassOrInterfaceDeclaration21 is not None else set()
        self.dsl_ClassOrInterfaceDeclaration23 = dsl_ClassOrInterfaceDeclaration23
        self.dsl_ClassOrInterfaceDeclaration25 = dsl_ClassOrInterfaceDeclaration25 if dsl_ClassOrInterfaceDeclaration25 is not None else set()
        self.dsl_ClassOrInterfaceDeclaration = dsl_ClassOrInterfaceDeclaration
        self.dsl_ClassOrInterfaceDeclaration27 = dsl_ClassOrInterfaceDeclaration27
        self.dsl_ClassOrInterfaceDeclaration67 = dsl_ClassOrInterfaceDeclaration67
        self.dsl_ClassOrInterfaceDeclaration356 = dsl_ClassOrInterfaceDeclaration356
        self.dsl_ClassOrInterfaceDeclaration482 = dsl_ClassOrInterfaceDeclaration482
        
    @property
    def typeCategory(self) -> str:
        return self.__typeCategory

    @typeCategory.setter
    def typeCategory(self, typeCategory: str):
        self.__typeCategory = typeCategory

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dsl_ClassOrInterfaceDeclaration356(self):
        return self.__dsl_ClassOrInterfaceDeclaration356

    @dsl_ClassOrInterfaceDeclaration356.setter
    def dsl_ClassOrInterfaceDeclaration356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration356", None)
        self.__dsl_ClassOrInterfaceDeclaration356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_BlockStatement355"):
                opp_val = getattr(old_value, "dsl_BlockStatement355", None)
                if opp_val == self:
                    setattr(old_value, "dsl_BlockStatement355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_BlockStatement355"):
                opp_val = getattr(value, "dsl_BlockStatement355", None)
                setattr(value, "dsl_BlockStatement355", self)

    @property
    def dsl_ClassOrInterfaceDeclaration27(self):
        return self.__dsl_ClassOrInterfaceDeclaration27

    @dsl_ClassOrInterfaceDeclaration27.setter
    def dsl_ClassOrInterfaceDeclaration27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration27", None)
        self.__dsl_ClassOrInterfaceDeclaration27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBody"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBody", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBody"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBody", None)
                setattr(value, "dsl_ClassOrInterfaceBody", self)

    @property
    def dsl_ClassOrInterfaceDeclaration482(self):
        return self.__dsl_ClassOrInterfaceDeclaration482

    @dsl_ClassOrInterfaceDeclaration482.setter
    def dsl_ClassOrInterfaceDeclaration482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration482", None)
        self.__dsl_ClassOrInterfaceDeclaration482 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeMemberDeclaration481"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeMemberDeclaration481", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeMemberDeclaration481", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeMemberDeclaration481"):
                opp_val = getattr(value, "dsl_AnnotationTypeMemberDeclaration481", None)
                setattr(value, "dsl_AnnotationTypeMemberDeclaration481", self)

    @property
    def dsl_ClassOrInterfaceDeclaration25(self):
        return self.__dsl_ClassOrInterfaceDeclaration25

    @dsl_ClassOrInterfaceDeclaration25.setter
    def dsl_ClassOrInterfaceDeclaration25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration25", None)
        self.__dsl_ClassOrInterfaceDeclaration25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_ImplementsList"):
                    opp_val = getattr(item, "dsl_ImplementsList", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_ImplementsList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_ImplementsList"):
                    opp_val = getattr(item, "dsl_ImplementsList", None)
                    
                    setattr(item, "dsl_ImplementsList", self)
                    

    @property
    def dsl_ClassOrInterfaceDeclaration23(self):
        return self.__dsl_ClassOrInterfaceDeclaration23

    @dsl_ClassOrInterfaceDeclaration23.setter
    def dsl_ClassOrInterfaceDeclaration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration23", None)
        self.__dsl_ClassOrInterfaceDeclaration23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ExtendsList"):
                opp_val = getattr(old_value, "dsl_ExtendsList", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ExtendsList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ExtendsList"):
                opp_val = getattr(value, "dsl_ExtendsList", None)
                setattr(value, "dsl_ExtendsList", self)

    @property
    def dsl_ClassOrInterfaceDeclaration67(self):
        return self.__dsl_ClassOrInterfaceDeclaration67

    @dsl_ClassOrInterfaceDeclaration67.setter
    def dsl_ClassOrInterfaceDeclaration67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration67", None)
        self.__dsl_ClassOrInterfaceDeclaration67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration66"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration66", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBodyDeclaration66"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBodyDeclaration66", None)
                setattr(value, "dsl_ClassOrInterfaceBodyDeclaration66", self)

    @property
    def dsl_ClassOrInterfaceDeclaration21(self):
        return self.__dsl_ClassOrInterfaceDeclaration21

    @dsl_ClassOrInterfaceDeclaration21.setter
    def dsl_ClassOrInterfaceDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration21", None)
        self.__dsl_ClassOrInterfaceDeclaration21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_TypeParameters"):
                    opp_val = getattr(item, "dsl_TypeParameters", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_TypeParameters", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_TypeParameters"):
                    opp_val = getattr(item, "dsl_TypeParameters", None)
                    
                    setattr(item, "dsl_TypeParameters", self)
                    

    @property
    def dsl_ClassOrInterfaceDeclaration(self):
        return self.__dsl_ClassOrInterfaceDeclaration

    @dsl_ClassOrInterfaceDeclaration.setter
    def dsl_ClassOrInterfaceDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration", None)
        self.__dsl_ClassOrInterfaceDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeDeclaration15"):
                opp_val = getattr(old_value, "dsl_TypeDeclaration15", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeDeclaration15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeDeclaration15"):
                opp_val = getattr(value, "dsl_TypeDeclaration15", None)
                setattr(value, "dsl_TypeDeclaration15", self)

class dsl_ImplementsList:

    pass
class dsl_ExtendsList:

    pass
class dsl_TypeParameters:

    pass
class dsl_CommonModifier:

    def __init__(self, visibility: str, static: bool, final: bool, abstract: bool, dsl_CommonModifier: "dsl_TypeBodyModifier" = None, dsl_CommonModifier13: "dsl_TypeDeclaration" = None):
        self.visibility = visibility
        self.static = static
        self.final = final
        self.abstract = abstract
        self.dsl_CommonModifier = dsl_CommonModifier
        self.dsl_CommonModifier13 = dsl_CommonModifier13
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def dsl_CommonModifier(self):
        return self.__dsl_CommonModifier

    @dsl_CommonModifier.setter
    def dsl_CommonModifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_CommonModifier__dsl_CommonModifier", None)
        self.__dsl_CommonModifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeBodyModifier"):
                opp_val = getattr(old_value, "dsl_TypeBodyModifier", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeBodyModifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeBodyModifier"):
                opp_val = getattr(value, "dsl_TypeBodyModifier", None)
                setattr(value, "dsl_TypeBodyModifier", self)

    @property
    def dsl_CommonModifier13(self):
        return self.__dsl_CommonModifier13

    @dsl_CommonModifier13.setter
    def dsl_CommonModifier13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_CommonModifier__dsl_CommonModifier13", None)
        self.__dsl_CommonModifier13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_TypeDeclaration12"):
                opp_val = getattr(old_value, "dsl_TypeDeclaration12", None)
                if opp_val == self:
                    setattr(old_value, "dsl_TypeDeclaration12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_TypeDeclaration12"):
                opp_val = getattr(value, "dsl_TypeDeclaration12", None)
                setattr(value, "dsl_TypeDeclaration12", self)

class dsl_Name:

    def __init__(self, ids: str, dsl_Name: "dsl_PackageDeclaration" = None, dsl_Name9: "dsl_ImportDeclaration" = None, dsl_Name148: "dsl_NameList" = None, dsl_Name246: "dsl_PrimaryPrefix" = None, dsl_Name447: "dsl_Annotation" = None):
        self.ids = ids
        self.dsl_Name = dsl_Name
        self.dsl_Name9 = dsl_Name9
        self.dsl_Name148 = dsl_Name148
        self.dsl_Name246 = dsl_Name246
        self.dsl_Name447 = dsl_Name447
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def dsl_Name447(self):
        return self.__dsl_Name447

    @dsl_Name447.setter
    def dsl_Name447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Name__dsl_Name447", None)
        self.__dsl_Name447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Annotation"):
                opp_val = getattr(old_value, "dsl_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Annotation"):
                opp_val = getattr(value, "dsl_Annotation", None)
                setattr(value, "dsl_Annotation", self)

    @property
    def dsl_Name148(self):
        return self.__dsl_Name148

    @dsl_Name148.setter
    def dsl_Name148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Name__dsl_Name148", None)
        self.__dsl_Name148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_NameList147"):
                opp_val = getattr(old_value, "dsl_NameList147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_NameList147"):
                opp_val = getattr(value, "dsl_NameList147", None)
                if opp_val is None:
                    setattr(value, "dsl_NameList147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Name9(self):
        return self.__dsl_Name9

    @dsl_Name9.setter
    def dsl_Name9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Name__dsl_Name9", None)
        self.__dsl_Name9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ImportDeclaration8"):
                opp_val = getattr(old_value, "dsl_ImportDeclaration8", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ImportDeclaration8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ImportDeclaration8"):
                opp_val = getattr(value, "dsl_ImportDeclaration8", None)
                setattr(value, "dsl_ImportDeclaration8", self)

    @property
    def dsl_Name246(self):
        return self.__dsl_Name246

    @dsl_Name246.setter
    def dsl_Name246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Name__dsl_Name246", None)
        self.__dsl_Name246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PrimaryPrefix245"):
                opp_val = getattr(old_value, "dsl_PrimaryPrefix245", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PrimaryPrefix245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PrimaryPrefix245"):
                opp_val = getattr(value, "dsl_PrimaryPrefix245", None)
                setattr(value, "dsl_PrimaryPrefix245", self)

    @property
    def dsl_Name(self):
        return self.__dsl_Name

    @dsl_Name.setter
    def dsl_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Name__dsl_Name", None)
        self.__dsl_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PackageDeclaration6"):
                opp_val = getattr(old_value, "dsl_PackageDeclaration6", None)
                if opp_val == self:
                    setattr(old_value, "dsl_PackageDeclaration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PackageDeclaration6"):
                opp_val = getattr(value, "dsl_PackageDeclaration6", None)
                setattr(value, "dsl_PackageDeclaration6", self)

class dsl_TypeDeclaration:

    pass
class dsl_ImportDeclaration:

    pass
class dsl_PackageDeclaration:

    pass
class dsl_TypeBodyModifier:

    def __init__(self, native: bool, transient: bool, volatile: bool, strictfp: bool, synchronized: bool, dsl_TypeBodyModifier: "dsl_CommonModifier" = None, dsl_TypeBodyModifier64: "dsl_ClassOrInterfaceBodyDeclaration" = None, dsl_TypeBodyModifier474: "dsl_AnnotationTypeMemberDeclaration" = None):
        self.native = native
        self.transient = transient
        self.volatile = volatile
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.dsl_TypeBodyModifier = dsl_TypeBodyModifier
        self.dsl_TypeBodyModifier64 = dsl_TypeBodyModifier64
        self.dsl_TypeBodyModifier474 = dsl_TypeBodyModifier474
        
    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def strictfp(self) -> bool:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: bool):
        self.__strictfp = strictfp

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def dsl_TypeBodyModifier(self):
        return self.__dsl_TypeBodyModifier

    @dsl_TypeBodyModifier.setter
    def dsl_TypeBodyModifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_TypeBodyModifier__dsl_TypeBodyModifier", None)
        self.__dsl_TypeBodyModifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_CommonModifier"):
                opp_val = getattr(old_value, "dsl_CommonModifier", None)
                if opp_val == self:
                    setattr(old_value, "dsl_CommonModifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_CommonModifier"):
                opp_val = getattr(value, "dsl_CommonModifier", None)
                setattr(value, "dsl_CommonModifier", self)

    @property
    def dsl_TypeBodyModifier64(self):
        return self.__dsl_TypeBodyModifier64

    @dsl_TypeBodyModifier64.setter
    def dsl_TypeBodyModifier64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_TypeBodyModifier__dsl_TypeBodyModifier64", None)
        self.__dsl_TypeBodyModifier64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration63"):
                opp_val = getattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration63", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ClassOrInterfaceBodyDeclaration63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ClassOrInterfaceBodyDeclaration63"):
                opp_val = getattr(value, "dsl_ClassOrInterfaceBodyDeclaration63", None)
                setattr(value, "dsl_ClassOrInterfaceBodyDeclaration63", self)

    @property
    def dsl_TypeBodyModifier474(self):
        return self.__dsl_TypeBodyModifier474

    @dsl_TypeBodyModifier474.setter
    def dsl_TypeBodyModifier474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_TypeBodyModifier__dsl_TypeBodyModifier474", None)
        self.__dsl_TypeBodyModifier474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AnnotationTypeMemberDeclaration473"):
                opp_val = getattr(old_value, "dsl_AnnotationTypeMemberDeclaration473", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AnnotationTypeMemberDeclaration473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AnnotationTypeMemberDeclaration473"):
                opp_val = getattr(value, "dsl_AnnotationTypeMemberDeclaration473", None)
                setattr(value, "dsl_AnnotationTypeMemberDeclaration473", self)

class dsl_CompilationUnit:

    pass