from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class classifierTypeRule:

    pass
class ale_ClassifierType(classifierTypeRule):

    def __init__(self, className: str, packageName: str):
        self.className = className
        self.packageName = packageName
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

class Expression:

    pass
class ale_Feature(Expression):

    def __init__(self, feature: str, ale_Feature: "ale_Expression" = None):
        self.feature = feature
        self.ale_Feature = ale_Feature
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def ale_Feature(self):
        return self.__ale_Feature

    @ale_Feature.setter
    def ale_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Feature__ale_Feature", None)
        self.__ale_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression99"):
                opp_val = getattr(old_value, "ale_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression99"):
                opp_val = getattr(value, "ale_Expression99", None)
                setattr(value, "ale_Expression99", self)

class ale_Conditional(Expression):

    pass
class ale_Xor(Expression):

    pass
class ale_Or(Expression):

    pass
class ale_Let(Expression):

    pass
class ale_Comp(Expression):

    def __init__(self, op: str, ale_Comp: "ale_Expression" = None, ale_Comp124: "ale_Expression" = None):
        self.op = op
        self.ale_Comp = ale_Comp
        self.ale_Comp124 = ale_Comp124
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def ale_Comp124(self):
        return self.__ale_Comp124

    @ale_Comp124.setter
    def ale_Comp124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Comp__ale_Comp124", None)
        self.__ale_Comp124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression125"):
                opp_val = getattr(old_value, "ale_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression125"):
                opp_val = getattr(value, "ale_Expression125", None)
                setattr(value, "ale_Expression125", self)

    @property
    def ale_Comp(self):
        return self.__ale_Comp

    @ale_Comp.setter
    def ale_Comp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Comp__ale_Comp", None)
        self.__ale_Comp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression122"):
                opp_val = getattr(old_value, "ale_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression122"):
                opp_val = getattr(value, "ale_Expression122", None)
                setattr(value, "ale_Expression122", self)

class ale_Min(Expression):

    pass
class ale_Implie(Expression):

    pass
class ale_VarRef(Expression):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class ale_Apply(Expression):

    def __init__(self, name: str, varName: str, ale_Apply109: set["ale_Expression"] = None, ale_Apply: "ale_Expression" = None, ale_Apply103: "ale_typeLiteral" = None, ale_Apply106: "ale_Expression" = None):
        self.name = name
        self.varName = varName
        self.ale_Apply109 = ale_Apply109 if ale_Apply109 is not None else set()
        self.ale_Apply = ale_Apply
        self.ale_Apply103 = ale_Apply103
        self.ale_Apply106 = ale_Apply106
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Apply(self):
        return self.__ale_Apply

    @ale_Apply.setter
    def ale_Apply(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Apply__ale_Apply", None)
        self.__ale_Apply = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression101"):
                opp_val = getattr(old_value, "ale_Expression101", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression101"):
                opp_val = getattr(value, "ale_Expression101", None)
                setattr(value, "ale_Expression101", self)

    @property
    def ale_Apply106(self):
        return self.__ale_Apply106

    @ale_Apply106.setter
    def ale_Apply106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Apply__ale_Apply106", None)
        self.__ale_Apply106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression107"):
                opp_val = getattr(old_value, "ale_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression107"):
                opp_val = getattr(value, "ale_Expression107", None)
                setattr(value, "ale_Expression107", self)

    @property
    def ale_Apply103(self):
        return self.__ale_Apply103

    @ale_Apply103.setter
    def ale_Apply103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Apply__ale_Apply103", None)
        self.__ale_Apply103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_typeLiteral104"):
                opp_val = getattr(old_value, "ale_typeLiteral104", None)
                if opp_val == self:
                    setattr(old_value, "ale_typeLiteral104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_typeLiteral104"):
                opp_val = getattr(value, "ale_typeLiteral104", None)
                setattr(value, "ale_typeLiteral104", self)

    @property
    def ale_Apply109(self):
        return self.__ale_Apply109

    @ale_Apply109.setter
    def ale_Apply109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Apply__ale_Apply109", None)
        self.__ale_Apply109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Expression110"):
                    opp_val = getattr(item, "ale_Expression110", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Expression110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Expression110"):
                    opp_val = getattr(item, "ale_Expression110", None)
                    
                    setattr(item, "ale_Expression110", self)
                    

class ale_Lit(Expression):

    pass
class ale_Not(Expression):

    pass
class ale_And(Expression):

    pass
class ale_Call(Expression):

    def __init__(self, name: str, ale_Call: "ale_Expression" = None, ale_Call96: set["ale_Expression"] = None):
        self.name = name
        self.ale_Call = ale_Call
        self.ale_Call96 = ale_Call96 if ale_Call96 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Call96(self):
        return self.__ale_Call96

    @ale_Call96.setter
    def ale_Call96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Call__ale_Call96", None)
        self.__ale_Call96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Expression97"):
                    opp_val = getattr(item, "ale_Expression97", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Expression97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Expression97"):
                    opp_val = getattr(item, "ale_Expression97", None)
                    
                    setattr(item, "ale_Expression97", self)
                    

    @property
    def ale_Call(self):
        return self.__ale_Call

    @ale_Call.setter
    def ale_Call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Call__ale_Call", None)
        self.__ale_Call = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression94"):
                opp_val = getattr(old_value, "ale_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression94"):
                opp_val = getattr(value, "ale_Expression94", None)
                setattr(value, "ale_Expression94", self)

class typeLiteral:

    pass
class ale_BoolType(typeLiteral):

    pass
class ale_StringType(typeLiteral):

    pass
class ale_ClassifierSetType(typeLiteral):

    pass
class ale_SeqType(typeLiteral):

    pass
class ale_RealType(typeLiteral):

    pass
class ale_IntType(typeLiteral):

    pass
class ale_SetType(typeLiteral):

    pass
class ale_classifierTypeRule(typeLiteral):

    pass
class rType:

    pass
class literal:

    pass
class ale_OrderedSet(literal):

    pass
class ale_Enum(literal):

    pass
class ale_False(literal):

    pass
class ale_Int(literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ale_True(literal):

    pass
class ale_Real(literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ale_String(literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ale_Null(literal):

    pass
class ale_Sequence(literal):

    pass
class ale_literal:

    pass
class ale_typeLiteral(rType, literal):

    pass
class ale_Add(Expression):

    def __init__(self, op: str, ale_Add: "ale_Expression" = None, ale_Add119: "ale_Expression" = None):
        self.op = op
        self.ale_Add = ale_Add
        self.ale_Add119 = ale_Add119
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def ale_Add(self):
        return self.__ale_Add

    @ale_Add.setter
    def ale_Add(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Add__ale_Add", None)
        self.__ale_Add = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression117"):
                opp_val = getattr(old_value, "ale_Expression117", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression117"):
                opp_val = getattr(value, "ale_Expression117", None)
                setattr(value, "ale_Expression117", self)

    @property
    def ale_Add119(self):
        return self.__ale_Add119

    @ale_Add119.setter
    def ale_Add119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Add__ale_Add119", None)
        self.__ale_Add119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression120"):
                opp_val = getattr(old_value, "ale_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression120"):
                opp_val = getattr(value, "ale_Expression120", None)
                setattr(value, "ale_Expression120", self)

class ale_Mult(Expression):

    def __init__(self, op: str, ale_Mult: "ale_Expression" = None, ale_Mult114: "ale_Expression" = None):
        self.op = op
        self.ale_Mult = ale_Mult
        self.ale_Mult114 = ale_Mult114
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def ale_Mult114(self):
        return self.__ale_Mult114

    @ale_Mult114.setter
    def ale_Mult114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Mult__ale_Mult114", None)
        self.__ale_Mult114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression115"):
                opp_val = getattr(old_value, "ale_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression115"):
                opp_val = getattr(value, "ale_Expression115", None)
                setattr(value, "ale_Expression115", self)

    @property
    def ale_Mult(self):
        return self.__ale_Mult

    @ale_Mult.setter
    def ale_Mult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Mult__ale_Mult", None)
        self.__ale_Mult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression112"):
                opp_val = getattr(old_value, "ale_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression112"):
                opp_val = getattr(value, "ale_Expression112", None)
                setattr(value, "ale_Expression112", self)

class ale_rCase:

    pass
class ale_rSwitch:

    def __init__(self, paramName: str, ale_rSwitch: "ale_ExpressionStmt" = None, ale_rSwitch74: set["ale_rCase"] = None, ale_rSwitch76: "ale_ExpressionStmt" = None):
        self.paramName = paramName
        self.ale_rSwitch = ale_rSwitch
        self.ale_rSwitch74 = ale_rSwitch74 if ale_rSwitch74 is not None else set()
        self.ale_rSwitch76 = ale_rSwitch76
        
    @property
    def paramName(self) -> str:
        return self.__paramName

    @paramName.setter
    def paramName(self, paramName: str):
        self.__paramName = paramName

    @property
    def ale_rSwitch74(self):
        return self.__ale_rSwitch74

    @ale_rSwitch74.setter
    def ale_rSwitch74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rSwitch__ale_rSwitch74", None)
        self.__ale_rSwitch74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_rCase"):
                    opp_val = getattr(item, "ale_rCase", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_rCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_rCase"):
                    opp_val = getattr(item, "ale_rCase", None)
                    
                    setattr(item, "ale_rCase", self)
                    

    @property
    def ale_rSwitch76(self):
        return self.__ale_rSwitch76

    @ale_rSwitch76.setter
    def ale_rSwitch76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rSwitch__ale_rSwitch76", None)
        self.__ale_rSwitch76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_ExpressionStmt77"):
                opp_val = getattr(old_value, "ale_ExpressionStmt77", None)
                if opp_val == self:
                    setattr(old_value, "ale_ExpressionStmt77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_ExpressionStmt77"):
                opp_val = getattr(value, "ale_ExpressionStmt77", None)
                setattr(value, "ale_ExpressionStmt77", self)

    @property
    def ale_rSwitch(self):
        return self.__ale_rSwitch

    @ale_rSwitch.setter
    def ale_rSwitch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rSwitch__ale_rSwitch", None)
        self.__ale_rSwitch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_ExpressionStmt72"):
                opp_val = getattr(old_value, "ale_ExpressionStmt72", None)
                if opp_val == self:
                    setattr(old_value, "ale_ExpressionStmt72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_ExpressionStmt72"):
                opp_val = getattr(value, "ale_ExpressionStmt72", None)
                setattr(value, "ale_ExpressionStmt72", self)

class ale_binding:

    def __init__(self, name: str, ale_binding: "ale_typeLiteral" = None, ale_binding91: "ale_Expression" = None, ale_binding160: "ale_Let" = None):
        self.name = name
        self.ale_binding = ale_binding
        self.ale_binding91 = ale_binding91
        self.ale_binding160 = ale_binding160
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_binding160(self):
        return self.__ale_binding160

    @ale_binding160.setter
    def ale_binding160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_binding__ale_binding160", None)
        self.__ale_binding160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Let"):
                opp_val = getattr(old_value, "ale_Let", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Let"):
                opp_val = getattr(value, "ale_Let", None)
                if opp_val is None:
                    setattr(value, "ale_Let", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ale_binding91(self):
        return self.__ale_binding91

    @ale_binding91.setter
    def ale_binding91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_binding__ale_binding91", None)
        self.__ale_binding91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Expression92"):
                opp_val = getattr(old_value, "ale_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "ale_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Expression92"):
                opp_val = getattr(value, "ale_Expression92", None)
                setattr(value, "ale_Expression92", self)

    @property
    def ale_binding(self):
        return self.__ale_binding

    @ale_binding.setter
    def ale_binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_binding__ale_binding", None)
        self.__ale_binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_typeLiteral"):
                opp_val = getattr(old_value, "ale_typeLiteral", None)
                if opp_val == self:
                    setattr(old_value, "ale_typeLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_typeLiteral"):
                opp_val = getattr(value, "ale_typeLiteral", None)
                setattr(value, "ale_typeLiteral", self)

class ale_EObject:

    pass
class ale_Collection:

    def __init__(self, min: int, max: int, ale_Collection: "ale_ForEach" = None, ale_Collection51: "ale_ExpressionStmt" = None):
        self.min = min
        self.max = max
        self.ale_Collection = ale_Collection
        self.ale_Collection51 = ale_Collection51
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def ale_Collection(self):
        return self.__ale_Collection

    @ale_Collection.setter
    def ale_Collection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Collection__ale_Collection", None)
        self.__ale_Collection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_ForEach"):
                opp_val = getattr(old_value, "ale_ForEach", None)
                if opp_val == self:
                    setattr(old_value, "ale_ForEach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_ForEach"):
                opp_val = getattr(value, "ale_ForEach", None)
                setattr(value, "ale_ForEach", self)

    @property
    def ale_Collection51(self):
        return self.__ale_Collection51

    @ale_Collection51.setter
    def ale_Collection51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Collection__ale_Collection51", None)
        self.__ale_Collection51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_ExpressionStmt52"):
                opp_val = getattr(old_value, "ale_ExpressionStmt52", None)
                if opp_val == self:
                    setattr(old_value, "ale_ExpressionStmt52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_ExpressionStmt52"):
                opp_val = getattr(value, "ale_ExpressionStmt52", None)
                setattr(value, "ale_ExpressionStmt52", self)

class ale_Expression:

    pass
class Statement:

    pass
class ale_ForEach(Statement):

    def __init__(self, iterator: str, ale_ForEach: "ale_Collection" = None, ale_ForEach48: "ale_Block" = None):
        self.iterator = iterator
        self.ale_ForEach = ale_ForEach
        self.ale_ForEach48 = ale_ForEach48
        
    @property
    def iterator(self) -> str:
        return self.__iterator

    @iterator.setter
    def iterator(self, iterator: str):
        self.__iterator = iterator

    @property
    def ale_ForEach48(self):
        return self.__ale_ForEach48

    @ale_ForEach48.setter
    def ale_ForEach48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_ForEach__ale_ForEach48", None)
        self.__ale_ForEach48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Block49"):
                opp_val = getattr(old_value, "ale_Block49", None)
                if opp_val == self:
                    setattr(old_value, "ale_Block49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Block49"):
                opp_val = getattr(value, "ale_Block49", None)
                setattr(value, "ale_Block49", self)

    @property
    def ale_ForEach(self):
        return self.__ale_ForEach

    @ale_ForEach.setter
    def ale_ForEach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_ForEach__ale_ForEach", None)
        self.__ale_ForEach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Collection"):
                opp_val = getattr(old_value, "ale_Collection", None)
                if opp_val == self:
                    setattr(old_value, "ale_Collection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Collection"):
                opp_val = getattr(value, "ale_Collection", None)
                setattr(value, "ale_Collection", self)

class ale_While(Statement):

    pass
class ale_If(Statement):

    pass
class ale_Assign(Statement):

    pass
class ale_Insert(Statement):

    pass
class ale_VarDecl(Statement):

    def __init__(self, name: str, ale_VarDecl: "ale_rType" = None, ale_VarDecl30: "ale_ExpressionStmt" = None):
        self.name = name
        self.ale_VarDecl = ale_VarDecl
        self.ale_VarDecl30 = ale_VarDecl30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_VarDecl30(self):
        return self.__ale_VarDecl30

    @ale_VarDecl30.setter
    def ale_VarDecl30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_VarDecl__ale_VarDecl30", None)
        self.__ale_VarDecl30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_ExpressionStmt31"):
                opp_val = getattr(old_value, "ale_ExpressionStmt31", None)
                if opp_val == self:
                    setattr(old_value, "ale_ExpressionStmt31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_ExpressionStmt31"):
                opp_val = getattr(value, "ale_ExpressionStmt31", None)
                setattr(value, "ale_ExpressionStmt31", self)

    @property
    def ale_VarDecl(self):
        return self.__ale_VarDecl

    @ale_VarDecl.setter
    def ale_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_VarDecl__ale_VarDecl", None)
        self.__ale_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_rType28"):
                opp_val = getattr(old_value, "ale_rType28", None)
                if opp_val == self:
                    setattr(old_value, "ale_rType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_rType28"):
                opp_val = getattr(value, "ale_rType28", None)
                setattr(value, "ale_rType28", self)

class ale_Statement:

    pass
class ale_ExpressionStmt(Statement):

    pass
class ale_Remove(Statement):

    pass
class ale_Block:

    pass
class ale_Variable:

    def __init__(self, name: str, ale_Variable18: "ale_rType" = None, ale_Variable: "ale_Operation" = None):
        self.name = name
        self.ale_Variable18 = ale_Variable18
        self.ale_Variable = ale_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Variable(self):
        return self.__ale_Variable

    @ale_Variable.setter
    def ale_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Variable__ale_Variable", None)
        self.__ale_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Operation14"):
                opp_val = getattr(old_value, "ale_Operation14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Operation14"):
                opp_val = getattr(value, "ale_Operation14", None)
                if opp_val is None:
                    setattr(value, "ale_Operation14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ale_Variable18(self):
        return self.__ale_Variable18

    @ale_Variable18.setter
    def ale_Variable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Variable__ale_Variable18", None)
        self.__ale_Variable18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_rType19"):
                opp_val = getattr(old_value, "ale_rType19", None)
                if opp_val == self:
                    setattr(old_value, "ale_rType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_rType19"):
                opp_val = getattr(value, "ale_rType19", None)
                setattr(value, "ale_rType19", self)

class ale_rType:

    def __init__(self, name: str, ale_rType19: "ale_Variable" = None, ale_rType24: "ale_Attribute" = None, ale_rType: "ale_Operation" = None, ale_rType28: "ale_VarDecl" = None, ale_rType80: "ale_rCase" = None):
        self.name = name
        self.ale_rType19 = ale_rType19
        self.ale_rType24 = ale_rType24
        self.ale_rType = ale_rType
        self.ale_rType28 = ale_rType28
        self.ale_rType80 = ale_rType80
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_rType(self):
        return self.__ale_rType

    @ale_rType.setter
    def ale_rType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rType__ale_rType", None)
        self.__ale_rType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Operation12"):
                opp_val = getattr(old_value, "ale_Operation12", None)
                if opp_val == self:
                    setattr(old_value, "ale_Operation12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Operation12"):
                opp_val = getattr(value, "ale_Operation12", None)
                setattr(value, "ale_Operation12", self)

    @property
    def ale_rType24(self):
        return self.__ale_rType24

    @ale_rType24.setter
    def ale_rType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rType__ale_rType24", None)
        self.__ale_rType24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Attribute23"):
                opp_val = getattr(old_value, "ale_Attribute23", None)
                if opp_val == self:
                    setattr(old_value, "ale_Attribute23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Attribute23"):
                opp_val = getattr(value, "ale_Attribute23", None)
                setattr(value, "ale_Attribute23", self)

    @property
    def ale_rType19(self):
        return self.__ale_rType19

    @ale_rType19.setter
    def ale_rType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rType__ale_rType19", None)
        self.__ale_rType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Variable18"):
                opp_val = getattr(old_value, "ale_Variable18", None)
                if opp_val == self:
                    setattr(old_value, "ale_Variable18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Variable18"):
                opp_val = getattr(value, "ale_Variable18", None)
                setattr(value, "ale_Variable18", self)

    @property
    def ale_rType80(self):
        return self.__ale_rType80

    @ale_rType80.setter
    def ale_rType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rType__ale_rType80", None)
        self.__ale_rType80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_rCase79"):
                opp_val = getattr(old_value, "ale_rCase79", None)
                if opp_val == self:
                    setattr(old_value, "ale_rCase79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_rCase79"):
                opp_val = getattr(value, "ale_rCase79", None)
                setattr(value, "ale_rCase79", self)

    @property
    def ale_rType28(self):
        return self.__ale_rType28

    @ale_rType28.setter
    def ale_rType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rType__ale_rType28", None)
        self.__ale_rType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_VarDecl"):
                opp_val = getattr(old_value, "ale_VarDecl", None)
                if opp_val == self:
                    setattr(old_value, "ale_VarDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_VarDecl"):
                opp_val = getattr(value, "ale_VarDecl", None)
                setattr(value, "ale_VarDecl", self)

class ale_Tag:

    def __init__(self, name: str, ale_Tag: "ale_Operation" = None):
        self.name = name
        self.ale_Tag = ale_Tag
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Tag(self):
        return self.__ale_Tag

    @ale_Tag.setter
    def ale_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Tag__ale_Tag", None)
        self.__ale_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Operation10"):
                opp_val = getattr(old_value, "ale_Operation10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Operation10"):
                opp_val = getattr(value, "ale_Operation10", None)
                if opp_val is None:
                    setattr(value, "ale_Operation10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BehavioredClass:

    pass
class ale_RuntimeClass(BehavioredClass):

    pass
class ale_ExtendedClass(BehavioredClass):

    def __init__(self, extends: str):
        self.extends = extends
        
    @property
    def extends(self) -> str:
        return self.__extends

    @extends.setter
    def extends(self, extends: str):
        self.__extends = extends

class ale_Operation:

    def __init__(self, name: str, ale_Operation: "ale_BehavioredClass" = None, ale_Operation10: set["ale_Tag"] = None, ale_Operation12: "ale_rType" = None, ale_Operation14: set["ale_Variable"] = None, ale_Operation16: "ale_Block" = None):
        self.name = name
        self.ale_Operation = ale_Operation
        self.ale_Operation10 = ale_Operation10 if ale_Operation10 is not None else set()
        self.ale_Operation12 = ale_Operation12
        self.ale_Operation14 = ale_Operation14 if ale_Operation14 is not None else set()
        self.ale_Operation16 = ale_Operation16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Operation16(self):
        return self.__ale_Operation16

    @ale_Operation16.setter
    def ale_Operation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Operation__ale_Operation16", None)
        self.__ale_Operation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Block"):
                opp_val = getattr(old_value, "ale_Block", None)
                if opp_val == self:
                    setattr(old_value, "ale_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Block"):
                opp_val = getattr(value, "ale_Block", None)
                setattr(value, "ale_Block", self)

    @property
    def ale_Operation14(self):
        return self.__ale_Operation14

    @ale_Operation14.setter
    def ale_Operation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Operation__ale_Operation14", None)
        self.__ale_Operation14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Variable"):
                    opp_val = getattr(item, "ale_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Variable"):
                    opp_val = getattr(item, "ale_Variable", None)
                    
                    setattr(item, "ale_Variable", self)
                    

    @property
    def ale_Operation12(self):
        return self.__ale_Operation12

    @ale_Operation12.setter
    def ale_Operation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Operation__ale_Operation12", None)
        self.__ale_Operation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_rType"):
                opp_val = getattr(old_value, "ale_rType", None)
                if opp_val == self:
                    setattr(old_value, "ale_rType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_rType"):
                opp_val = getattr(value, "ale_rType", None)
                setattr(value, "ale_rType", self)

    @property
    def ale_Operation10(self):
        return self.__ale_Operation10

    @ale_Operation10.setter
    def ale_Operation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Operation__ale_Operation10", None)
        self.__ale_Operation10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Tag"):
                    opp_val = getattr(item, "ale_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Tag"):
                    opp_val = getattr(item, "ale_Tag", None)
                    
                    setattr(item, "ale_Tag", self)
                    

    @property
    def ale_Operation(self):
        return self.__ale_Operation

    @ale_Operation.setter
    def ale_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Operation__ale_Operation", None)
        self.__ale_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_BehavioredClass8"):
                opp_val = getattr(old_value, "ale_BehavioredClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_BehavioredClass8"):
                opp_val = getattr(value, "ale_BehavioredClass8", None)
                if opp_val is None:
                    setattr(value, "ale_BehavioredClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ale_rOpposite:

    def __init__(self, name: str, ale_rOpposite: "ale_Attribute" = None):
        self.name = name
        self.ale_rOpposite = ale_rOpposite
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_rOpposite(self):
        return self.__ale_rOpposite

    @ale_rOpposite.setter
    def ale_rOpposite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_rOpposite__ale_rOpposite", None)
        self.__ale_rOpposite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Attribute21"):
                opp_val = getattr(old_value, "ale_Attribute21", None)
                if opp_val == self:
                    setattr(old_value, "ale_Attribute21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Attribute21"):
                opp_val = getattr(value, "ale_Attribute21", None)
                setattr(value, "ale_Attribute21", self)

class ale_BehavioredClass:

    def __init__(self, name: str, ale_BehavioredClass6: set["ale_Attribute"] = None, ale_BehavioredClass: "ale_Unit" = None, ale_BehavioredClass8: set["ale_Operation"] = None):
        self.name = name
        self.ale_BehavioredClass6 = ale_BehavioredClass6 if ale_BehavioredClass6 is not None else set()
        self.ale_BehavioredClass = ale_BehavioredClass
        self.ale_BehavioredClass8 = ale_BehavioredClass8 if ale_BehavioredClass8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_BehavioredClass6(self):
        return self.__ale_BehavioredClass6

    @ale_BehavioredClass6.setter
    def ale_BehavioredClass6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_BehavioredClass__ale_BehavioredClass6", None)
        self.__ale_BehavioredClass6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Attribute"):
                    opp_val = getattr(item, "ale_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Attribute"):
                    opp_val = getattr(item, "ale_Attribute", None)
                    
                    setattr(item, "ale_Attribute", self)
                    

    @property
    def ale_BehavioredClass8(self):
        return self.__ale_BehavioredClass8

    @ale_BehavioredClass8.setter
    def ale_BehavioredClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_BehavioredClass__ale_BehavioredClass8", None)
        self.__ale_BehavioredClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Operation"):
                    opp_val = getattr(item, "ale_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Operation"):
                    opp_val = getattr(item, "ale_Operation", None)
                    
                    setattr(item, "ale_Operation", self)
                    

    @property
    def ale_BehavioredClass(self):
        return self.__ale_BehavioredClass

    @ale_BehavioredClass.setter
    def ale_BehavioredClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_BehavioredClass__ale_BehavioredClass", None)
        self.__ale_BehavioredClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Unit4"):
                opp_val = getattr(old_value, "ale_Unit4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Unit4"):
                opp_val = getattr(value, "ale_Unit4", None)
                if opp_val is None:
                    setattr(value, "ale_Unit4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ale_Service:

    def __init__(self, name: str, ale_Service: "ale_Unit" = None):
        self.name = name
        self.ale_Service = ale_Service
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Service(self):
        return self.__ale_Service

    @ale_Service.setter
    def ale_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Service__ale_Service", None)
        self.__ale_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Unit2"):
                opp_val = getattr(old_value, "ale_Unit2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Unit2"):
                opp_val = getattr(value, "ale_Unit2", None)
                if opp_val is None:
                    setattr(value, "ale_Unit2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ale_Import:

    def __init__(self, name: str, alias: str, ale_Import: "ale_Unit" = None):
        self.name = name
        self.alias = alias
        self.ale_Import = ale_Import
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def ale_Import(self):
        return self.__ale_Import

    @ale_Import.setter
    def ale_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Import__ale_Import", None)
        self.__ale_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_Unit"):
                opp_val = getattr(old_value, "ale_Unit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_Unit"):
                opp_val = getattr(value, "ale_Unit", None)
                if opp_val is None:
                    setattr(value, "ale_Unit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ale_Unit:

    def __init__(self, name: str, ale_Unit: set["ale_Import"] = None, ale_Unit2: set["ale_Service"] = None, ale_Unit4: set["ale_BehavioredClass"] = None):
        self.name = name
        self.ale_Unit = ale_Unit if ale_Unit is not None else set()
        self.ale_Unit2 = ale_Unit2 if ale_Unit2 is not None else set()
        self.ale_Unit4 = ale_Unit4 if ale_Unit4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Unit2(self):
        return self.__ale_Unit2

    @ale_Unit2.setter
    def ale_Unit2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Unit__ale_Unit2", None)
        self.__ale_Unit2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Service"):
                    opp_val = getattr(item, "ale_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Service"):
                    opp_val = getattr(item, "ale_Service", None)
                    
                    setattr(item, "ale_Service", self)
                    

    @property
    def ale_Unit(self):
        return self.__ale_Unit

    @ale_Unit.setter
    def ale_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Unit__ale_Unit", None)
        self.__ale_Unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_Import"):
                    opp_val = getattr(item, "ale_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_Import"):
                    opp_val = getattr(item, "ale_Import", None)
                    
                    setattr(item, "ale_Import", self)
                    

    @property
    def ale_Unit4(self):
        return self.__ale_Unit4

    @ale_Unit4.setter
    def ale_Unit4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Unit__ale_Unit4", None)
        self.__ale_Unit4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ale_BehavioredClass"):
                    opp_val = getattr(item, "ale_BehavioredClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ale_BehavioredClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ale_BehavioredClass"):
                    opp_val = getattr(item, "ale_BehavioredClass", None)
                    
                    setattr(item, "ale_BehavioredClass", self)
                    

class ale_Attribute:

    def __init__(self, modifier: str, bounds: str, name: str, ale_Attribute: "ale_BehavioredClass" = None, ale_Attribute21: "ale_rOpposite" = None, ale_Attribute23: "ale_rType" = None, ale_Attribute26: "ale_ExpressionStmt" = None):
        self.modifier = modifier
        self.bounds = bounds
        self.name = name
        self.ale_Attribute = ale_Attribute
        self.ale_Attribute21 = ale_Attribute21
        self.ale_Attribute23 = ale_Attribute23
        self.ale_Attribute26 = ale_Attribute26
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ale_Attribute26(self):
        return self.__ale_Attribute26

    @ale_Attribute26.setter
    def ale_Attribute26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Attribute__ale_Attribute26", None)
        self.__ale_Attribute26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_ExpressionStmt"):
                opp_val = getattr(old_value, "ale_ExpressionStmt", None)
                if opp_val == self:
                    setattr(old_value, "ale_ExpressionStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_ExpressionStmt"):
                opp_val = getattr(value, "ale_ExpressionStmt", None)
                setattr(value, "ale_ExpressionStmt", self)

    @property
    def ale_Attribute23(self):
        return self.__ale_Attribute23

    @ale_Attribute23.setter
    def ale_Attribute23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Attribute__ale_Attribute23", None)
        self.__ale_Attribute23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_rType24"):
                opp_val = getattr(old_value, "ale_rType24", None)
                if opp_val == self:
                    setattr(old_value, "ale_rType24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_rType24"):
                opp_val = getattr(value, "ale_rType24", None)
                setattr(value, "ale_rType24", self)

    @property
    def ale_Attribute(self):
        return self.__ale_Attribute

    @ale_Attribute.setter
    def ale_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Attribute__ale_Attribute", None)
        self.__ale_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_BehavioredClass6"):
                opp_val = getattr(old_value, "ale_BehavioredClass6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_BehavioredClass6"):
                opp_val = getattr(value, "ale_BehavioredClass6", None)
                if opp_val is None:
                    setattr(value, "ale_BehavioredClass6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ale_Attribute21(self):
        return self.__ale_Attribute21

    @ale_Attribute21.setter
    def ale_Attribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ale_Attribute__ale_Attribute21", None)
        self.__ale_Attribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ale_rOpposite"):
                opp_val = getattr(old_value, "ale_rOpposite", None)
                if opp_val == self:
                    setattr(old_value, "ale_rOpposite", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ale_rOpposite"):
                opp_val = getattr(value, "ale_rOpposite", None)
                setattr(value, "ale_rOpposite", self)
