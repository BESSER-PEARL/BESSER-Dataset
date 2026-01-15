from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tgg_NamedElements:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tgg_OperatorPattern:

    pass
class tgg_Operator:

    def __init__(self, value: str, tgg_Operator: "tgg_OperatorPattern" = None):
        self.value = value
        self.tgg_Operator = tgg_Operator
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def tgg_Operator(self):
        return self.__tgg_Operator

    @tgg_Operator.setter
    def tgg_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Operator__tgg_Operator", None)
        self.__tgg_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_OperatorPattern"):
                opp_val = getattr(old_value, "tgg_OperatorPattern", None)
                if opp_val == self:
                    setattr(old_value, "tgg_OperatorPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_OperatorPattern"):
                opp_val = getattr(value, "tgg_OperatorPattern", None)
                setattr(value, "tgg_OperatorPattern", self)

class tgg_EReference:

    pass
class OperatorPattern:

    pass
class tgg_EObject:

    pass
class tgg_EEnumLiteral:

    pass
class tgg_EEnum:

    pass
class Expression:

    pass
class tgg_LiteralExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class tgg_AttributeExpression(Expression):

    pass
class tgg_EnumExpression(Expression):

    pass
class tgg_ParamValue:

    pass
class tgg_EAttribute:

    pass
class tgg_ContextLinkVariablePattern:

    pass
class tgg_ContextObjectVariablePattern:

    def __init__(self, name: str, tgg_ContextObjectVariablePattern: "tgg_EClass" = None, tgg_ContextObjectVariablePattern83: set["tgg_AttributeConstraint"] = None, tgg_ContextObjectVariablePattern86: set["tgg_ContextLinkVariablePattern"] = None, tgg_ContextObjectVariablePattern114: "tgg_ContextLinkVariablePattern" = None, tgg_ContextObjectVariablePattern135: "tgg_Nac" = None, tgg_ContextObjectVariablePattern138: "tgg_Nac" = None):
        self.name = name
        self.tgg_ContextObjectVariablePattern = tgg_ContextObjectVariablePattern
        self.tgg_ContextObjectVariablePattern83 = tgg_ContextObjectVariablePattern83 if tgg_ContextObjectVariablePattern83 is not None else set()
        self.tgg_ContextObjectVariablePattern86 = tgg_ContextObjectVariablePattern86 if tgg_ContextObjectVariablePattern86 is not None else set()
        self.tgg_ContextObjectVariablePattern114 = tgg_ContextObjectVariablePattern114
        self.tgg_ContextObjectVariablePattern135 = tgg_ContextObjectVariablePattern135
        self.tgg_ContextObjectVariablePattern138 = tgg_ContextObjectVariablePattern138
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tgg_ContextObjectVariablePattern114(self):
        return self.__tgg_ContextObjectVariablePattern114

    @tgg_ContextObjectVariablePattern114.setter
    def tgg_ContextObjectVariablePattern114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_ContextObjectVariablePattern__tgg_ContextObjectVariablePattern114", None)
        self.__tgg_ContextObjectVariablePattern114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_ContextLinkVariablePattern113"):
                opp_val = getattr(old_value, "tgg_ContextLinkVariablePattern113", None)
                if opp_val == self:
                    setattr(old_value, "tgg_ContextLinkVariablePattern113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_ContextLinkVariablePattern113"):
                opp_val = getattr(value, "tgg_ContextLinkVariablePattern113", None)
                setattr(value, "tgg_ContextLinkVariablePattern113", self)

    @property
    def tgg_ContextObjectVariablePattern135(self):
        return self.__tgg_ContextObjectVariablePattern135

    @tgg_ContextObjectVariablePattern135.setter
    def tgg_ContextObjectVariablePattern135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_ContextObjectVariablePattern__tgg_ContextObjectVariablePattern135", None)
        self.__tgg_ContextObjectVariablePattern135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Nac134"):
                opp_val = getattr(old_value, "tgg_Nac134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Nac134"):
                opp_val = getattr(value, "tgg_Nac134", None)
                if opp_val is None:
                    setattr(value, "tgg_Nac134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_ContextObjectVariablePattern86(self):
        return self.__tgg_ContextObjectVariablePattern86

    @tgg_ContextObjectVariablePattern86.setter
    def tgg_ContextObjectVariablePattern86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_ContextObjectVariablePattern__tgg_ContextObjectVariablePattern86", None)
        self.__tgg_ContextObjectVariablePattern86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_ContextLinkVariablePattern"):
                    opp_val = getattr(item, "tgg_ContextLinkVariablePattern", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_ContextLinkVariablePattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_ContextLinkVariablePattern"):
                    opp_val = getattr(item, "tgg_ContextLinkVariablePattern", None)
                    
                    setattr(item, "tgg_ContextLinkVariablePattern", self)
                    

    @property
    def tgg_ContextObjectVariablePattern138(self):
        return self.__tgg_ContextObjectVariablePattern138

    @tgg_ContextObjectVariablePattern138.setter
    def tgg_ContextObjectVariablePattern138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_ContextObjectVariablePattern__tgg_ContextObjectVariablePattern138", None)
        self.__tgg_ContextObjectVariablePattern138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Nac137"):
                opp_val = getattr(old_value, "tgg_Nac137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Nac137"):
                opp_val = getattr(value, "tgg_Nac137", None)
                if opp_val is None:
                    setattr(value, "tgg_Nac137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_ContextObjectVariablePattern83(self):
        return self.__tgg_ContextObjectVariablePattern83

    @tgg_ContextObjectVariablePattern83.setter
    def tgg_ContextObjectVariablePattern83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_ContextObjectVariablePattern__tgg_ContextObjectVariablePattern83", None)
        self.__tgg_ContextObjectVariablePattern83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_AttributeConstraint84"):
                    opp_val = getattr(item, "tgg_AttributeConstraint84", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_AttributeConstraint84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_AttributeConstraint84"):
                    opp_val = getattr(item, "tgg_AttributeConstraint84", None)
                    
                    setattr(item, "tgg_AttributeConstraint84", self)
                    

    @property
    def tgg_ContextObjectVariablePattern(self):
        return self.__tgg_ContextObjectVariablePattern

    @tgg_ContextObjectVariablePattern.setter
    def tgg_ContextObjectVariablePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_ContextObjectVariablePattern__tgg_ContextObjectVariablePattern", None)
        self.__tgg_ContextObjectVariablePattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_EClass81"):
                opp_val = getattr(old_value, "tgg_EClass81", None)
                if opp_val == self:
                    setattr(old_value, "tgg_EClass81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_EClass81"):
                opp_val = getattr(value, "tgg_EClass81", None)
                setattr(value, "tgg_EClass81", self)

class tgg_LinkVariablePattern(OperatorPattern):

    pass
class tgg_AttributeConstraint:

    def __init__(self, op: str, tgg_AttributeConstraint: "tgg_ObjectVariablePattern" = None, tgg_AttributeConstraint84: "tgg_ContextObjectVariablePattern" = None, tgg_AttributeConstraint88: "tgg_EAttribute" = None, tgg_AttributeConstraint90: "tgg_Expression" = None):
        self.op = op
        self.tgg_AttributeConstraint = tgg_AttributeConstraint
        self.tgg_AttributeConstraint84 = tgg_AttributeConstraint84
        self.tgg_AttributeConstraint88 = tgg_AttributeConstraint88
        self.tgg_AttributeConstraint90 = tgg_AttributeConstraint90
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def tgg_AttributeConstraint(self):
        return self.__tgg_AttributeConstraint

    @tgg_AttributeConstraint.setter
    def tgg_AttributeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeConstraint__tgg_AttributeConstraint", None)
        self.__tgg_AttributeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_ObjectVariablePattern77"):
                opp_val = getattr(old_value, "tgg_ObjectVariablePattern77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_ObjectVariablePattern77"):
                opp_val = getattr(value, "tgg_ObjectVariablePattern77", None)
                if opp_val is None:
                    setattr(value, "tgg_ObjectVariablePattern77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_AttributeConstraint84(self):
        return self.__tgg_AttributeConstraint84

    @tgg_AttributeConstraint84.setter
    def tgg_AttributeConstraint84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeConstraint__tgg_AttributeConstraint84", None)
        self.__tgg_AttributeConstraint84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_ContextObjectVariablePattern83"):
                opp_val = getattr(old_value, "tgg_ContextObjectVariablePattern83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_ContextObjectVariablePattern83"):
                opp_val = getattr(value, "tgg_ContextObjectVariablePattern83", None)
                if opp_val is None:
                    setattr(value, "tgg_ContextObjectVariablePattern83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_AttributeConstraint88(self):
        return self.__tgg_AttributeConstraint88

    @tgg_AttributeConstraint88.setter
    def tgg_AttributeConstraint88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeConstraint__tgg_AttributeConstraint88", None)
        self.__tgg_AttributeConstraint88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_EAttribute"):
                opp_val = getattr(old_value, "tgg_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "tgg_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_EAttribute"):
                opp_val = getattr(value, "tgg_EAttribute", None)
                setattr(value, "tgg_EAttribute", self)

    @property
    def tgg_AttributeConstraint90(self):
        return self.__tgg_AttributeConstraint90

    @tgg_AttributeConstraint90.setter
    def tgg_AttributeConstraint90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeConstraint__tgg_AttributeConstraint90", None)
        self.__tgg_AttributeConstraint90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Expression"):
                opp_val = getattr(old_value, "tgg_Expression", None)
                if opp_val == self:
                    setattr(old_value, "tgg_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Expression"):
                opp_val = getattr(value, "tgg_Expression", None)
                setattr(value, "tgg_Expression", self)

class tgg_AttributeAssignment:

    def __init__(self, op: str, tgg_AttributeAssignment: "tgg_ObjectVariablePattern" = None, tgg_AttributeAssignment92: "tgg_EAttribute" = None, tgg_AttributeAssignment95: "tgg_Expression" = None):
        self.op = op
        self.tgg_AttributeAssignment = tgg_AttributeAssignment
        self.tgg_AttributeAssignment92 = tgg_AttributeAssignment92
        self.tgg_AttributeAssignment95 = tgg_AttributeAssignment95
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def tgg_AttributeAssignment(self):
        return self.__tgg_AttributeAssignment

    @tgg_AttributeAssignment.setter
    def tgg_AttributeAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeAssignment__tgg_AttributeAssignment", None)
        self.__tgg_AttributeAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_ObjectVariablePattern75"):
                opp_val = getattr(old_value, "tgg_ObjectVariablePattern75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_ObjectVariablePattern75"):
                opp_val = getattr(value, "tgg_ObjectVariablePattern75", None)
                if opp_val is None:
                    setattr(value, "tgg_ObjectVariablePattern75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_AttributeAssignment92(self):
        return self.__tgg_AttributeAssignment92

    @tgg_AttributeAssignment92.setter
    def tgg_AttributeAssignment92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeAssignment__tgg_AttributeAssignment92", None)
        self.__tgg_AttributeAssignment92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_EAttribute93"):
                opp_val = getattr(old_value, "tgg_EAttribute93", None)
                if opp_val == self:
                    setattr(old_value, "tgg_EAttribute93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_EAttribute93"):
                opp_val = getattr(value, "tgg_EAttribute93", None)
                setattr(value, "tgg_EAttribute93", self)

    @property
    def tgg_AttributeAssignment95(self):
        return self.__tgg_AttributeAssignment95

    @tgg_AttributeAssignment95.setter
    def tgg_AttributeAssignment95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttributeAssignment__tgg_AttributeAssignment95", None)
        self.__tgg_AttributeAssignment95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Expression96"):
                opp_val = getattr(old_value, "tgg_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "tgg_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Expression96"):
                opp_val = getattr(value, "tgg_Expression96", None)
                setattr(value, "tgg_Expression96", self)

class NamePattern:

    pass
class ParamValue:

    pass
class tgg_Expression(ParamValue):

    pass
class tgg_LocalVariable(ParamValue):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tgg_AttrCond:

    pass
class tgg_CorrVariablePattern(NamePattern):

    pass
class tgg_ObjectVariablePattern(NamePattern):

    pass
class tgg_EDataType:

    pass
class tgg_Adornment:

    def __init__(self, value: str, tgg_Adornment: "tgg_AttrCondDef" = None, tgg_Adornment36: "tgg_AttrCondDef" = None):
        self.value = value
        self.tgg_Adornment = tgg_Adornment
        self.tgg_Adornment36 = tgg_Adornment36
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def tgg_Adornment36(self):
        return self.__tgg_Adornment36

    @tgg_Adornment36.setter
    def tgg_Adornment36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Adornment__tgg_Adornment36", None)
        self.__tgg_Adornment36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_AttrCondDef35"):
                opp_val = getattr(old_value, "tgg_AttrCondDef35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_AttrCondDef35"):
                opp_val = getattr(value, "tgg_AttrCondDef35", None)
                if opp_val is None:
                    setattr(value, "tgg_AttrCondDef35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_Adornment(self):
        return self.__tgg_Adornment

    @tgg_Adornment.setter
    def tgg_Adornment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Adornment__tgg_Adornment", None)
        self.__tgg_Adornment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_AttrCondDef33"):
                opp_val = getattr(old_value, "tgg_AttrCondDef33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_AttrCondDef33"):
                opp_val = getattr(value, "tgg_AttrCondDef33", None)
                if opp_val is None:
                    setattr(value, "tgg_AttrCondDef33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tgg_Param:

    def __init__(self, paramName: str, tgg_Param: "tgg_AttrCondDef" = None, tgg_Param38: "tgg_EDataType" = None):
        self.paramName = paramName
        self.tgg_Param = tgg_Param
        self.tgg_Param38 = tgg_Param38
        
    @property
    def paramName(self) -> str:
        return self.__paramName

    @paramName.setter
    def paramName(self, paramName: str):
        self.__paramName = paramName

    @property
    def tgg_Param(self):
        return self.__tgg_Param

    @tgg_Param.setter
    def tgg_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Param__tgg_Param", None)
        self.__tgg_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_AttrCondDef31"):
                opp_val = getattr(old_value, "tgg_AttrCondDef31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_AttrCondDef31"):
                opp_val = getattr(value, "tgg_AttrCondDef31", None)
                if opp_val is None:
                    setattr(value, "tgg_AttrCondDef31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_Param38(self):
        return self.__tgg_Param38

    @tgg_Param38.setter
    def tgg_Param38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Param__tgg_Param38", None)
        self.__tgg_Param38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_EDataType"):
                opp_val = getattr(old_value, "tgg_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "tgg_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_EDataType"):
                opp_val = getattr(value, "tgg_EDataType", None)
                setattr(value, "tgg_EDataType", self)

class tgg_EClass:

    pass
class tgg_EPackage:

    pass
class NamedElements:

    pass
class tgg_NamePattern(OperatorPattern, NamedElements):

    pass
class tgg_CorrType(NamedElements):

    pass
class tgg_AttrCondDef(NamedElements):

    def __init__(self, userDefined: bool, tgg_AttrCondDef: "tgg_Schema" = None, tgg_AttrCondDef31: set["tgg_Param"] = None, tgg_AttrCondDef33: set["tgg_Adornment"] = None, tgg_AttrCondDef35: set["tgg_Adornment"] = None, tgg_AttrCondDef56: "tgg_AttrCond" = None, tgg_AttrCondDef61: "tgg_AttrCondDefLibrary" = None):
        self.userDefined = userDefined
        self.tgg_AttrCondDef = tgg_AttrCondDef
        self.tgg_AttrCondDef31 = tgg_AttrCondDef31 if tgg_AttrCondDef31 is not None else set()
        self.tgg_AttrCondDef33 = tgg_AttrCondDef33 if tgg_AttrCondDef33 is not None else set()
        self.tgg_AttrCondDef35 = tgg_AttrCondDef35 if tgg_AttrCondDef35 is not None else set()
        self.tgg_AttrCondDef56 = tgg_AttrCondDef56
        self.tgg_AttrCondDef61 = tgg_AttrCondDef61
        
    @property
    def userDefined(self) -> bool:
        return self.__userDefined

    @userDefined.setter
    def userDefined(self, userDefined: bool):
        self.__userDefined = userDefined

    @property
    def tgg_AttrCondDef31(self):
        return self.__tgg_AttrCondDef31

    @tgg_AttrCondDef31.setter
    def tgg_AttrCondDef31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttrCondDef__tgg_AttrCondDef31", None)
        self.__tgg_AttrCondDef31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_Param"):
                    opp_val = getattr(item, "tgg_Param", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_Param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_Param"):
                    opp_val = getattr(item, "tgg_Param", None)
                    
                    setattr(item, "tgg_Param", self)
                    

    @property
    def tgg_AttrCondDef61(self):
        return self.__tgg_AttrCondDef61

    @tgg_AttrCondDef61.setter
    def tgg_AttrCondDef61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttrCondDef__tgg_AttrCondDef61", None)
        self.__tgg_AttrCondDef61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_AttrCondDefLibrary60"):
                opp_val = getattr(old_value, "tgg_AttrCondDefLibrary60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_AttrCondDefLibrary60"):
                opp_val = getattr(value, "tgg_AttrCondDefLibrary60", None)
                if opp_val is None:
                    setattr(value, "tgg_AttrCondDefLibrary60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_AttrCondDef35(self):
        return self.__tgg_AttrCondDef35

    @tgg_AttrCondDef35.setter
    def tgg_AttrCondDef35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttrCondDef__tgg_AttrCondDef35", None)
        self.__tgg_AttrCondDef35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_Adornment36"):
                    opp_val = getattr(item, "tgg_Adornment36", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_Adornment36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_Adornment36"):
                    opp_val = getattr(item, "tgg_Adornment36", None)
                    
                    setattr(item, "tgg_Adornment36", self)
                    

    @property
    def tgg_AttrCondDef(self):
        return self.__tgg_AttrCondDef

    @tgg_AttrCondDef.setter
    def tgg_AttrCondDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttrCondDef__tgg_AttrCondDef", None)
        self.__tgg_AttrCondDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Schema21"):
                opp_val = getattr(old_value, "tgg_Schema21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Schema21"):
                opp_val = getattr(value, "tgg_Schema21", None)
                if opp_val is None:
                    setattr(value, "tgg_Schema21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_AttrCondDef33(self):
        return self.__tgg_AttrCondDef33

    @tgg_AttrCondDef33.setter
    def tgg_AttrCondDef33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttrCondDef__tgg_AttrCondDef33", None)
        self.__tgg_AttrCondDef33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_Adornment"):
                    opp_val = getattr(item, "tgg_Adornment", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_Adornment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_Adornment"):
                    opp_val = getattr(item, "tgg_Adornment", None)
                    
                    setattr(item, "tgg_Adornment", self)
                    

    @property
    def tgg_AttrCondDef56(self):
        return self.__tgg_AttrCondDef56

    @tgg_AttrCondDef56.setter
    def tgg_AttrCondDef56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_AttrCondDef__tgg_AttrCondDef56", None)
        self.__tgg_AttrCondDef56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_AttrCond55"):
                opp_val = getattr(old_value, "tgg_AttrCond55", None)
                if opp_val == self:
                    setattr(old_value, "tgg_AttrCond55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_AttrCond55"):
                opp_val = getattr(value, "tgg_AttrCond55", None)
                setattr(value, "tgg_AttrCond55", self)

class tgg_AttrCondDefLibrary(NamedElements):

    pass
class tgg_Nac(NamedElements):

    pass
class tgg_ComplementRule(NamedElements):

    pass
class tgg_Rule(NamedElements):

    def __init__(self, abstractRule: bool, tgg_Rule: "tgg_TripleGraphGrammarFile" = None, tgg_Rule41: "tgg_Rule" = None, tgg_Rule39: set["tgg_Rule"] = None, tgg_Rule43: "tgg_Schema" = None, tgg_Rule46: set["tgg_ObjectVariablePattern"] = None, tgg_Rule48: set["tgg_ObjectVariablePattern"] = None, tgg_Rule51: set["tgg_CorrVariablePattern"] = None, tgg_Rule53: set["tgg_AttrCond"] = None, tgg_Rule117: "tgg_ComplementRule" = None, tgg_Rule132: "tgg_Nac" = None):
        self.abstractRule = abstractRule
        self.tgg_Rule = tgg_Rule
        self.tgg_Rule41 = tgg_Rule41
        self.tgg_Rule39 = tgg_Rule39 if tgg_Rule39 is not None else set()
        self.tgg_Rule43 = tgg_Rule43
        self.tgg_Rule46 = tgg_Rule46 if tgg_Rule46 is not None else set()
        self.tgg_Rule48 = tgg_Rule48 if tgg_Rule48 is not None else set()
        self.tgg_Rule51 = tgg_Rule51 if tgg_Rule51 is not None else set()
        self.tgg_Rule53 = tgg_Rule53 if tgg_Rule53 is not None else set()
        self.tgg_Rule117 = tgg_Rule117
        self.tgg_Rule132 = tgg_Rule132
        
    @property
    def abstractRule(self) -> bool:
        return self.__abstractRule

    @abstractRule.setter
    def abstractRule(self, abstractRule: bool):
        self.__abstractRule = abstractRule

    @property
    def tgg_Rule46(self):
        return self.__tgg_Rule46

    @tgg_Rule46.setter
    def tgg_Rule46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule46", None)
        self.__tgg_Rule46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_ObjectVariablePattern"):
                    opp_val = getattr(item, "tgg_ObjectVariablePattern", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_ObjectVariablePattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_ObjectVariablePattern"):
                    opp_val = getattr(item, "tgg_ObjectVariablePattern", None)
                    
                    setattr(item, "tgg_ObjectVariablePattern", self)
                    

    @property
    def tgg_Rule(self):
        return self.__tgg_Rule

    @tgg_Rule.setter
    def tgg_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule", None)
        self.__tgg_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_TripleGraphGrammarFile6"):
                opp_val = getattr(old_value, "tgg_TripleGraphGrammarFile6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_TripleGraphGrammarFile6"):
                opp_val = getattr(value, "tgg_TripleGraphGrammarFile6", None)
                if opp_val is None:
                    setattr(value, "tgg_TripleGraphGrammarFile6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_Rule41(self):
        return self.__tgg_Rule41

    @tgg_Rule41.setter
    def tgg_Rule41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule41", None)
        self.__tgg_Rule41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Rule39"):
                opp_val = getattr(old_value, "tgg_Rule39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Rule39"):
                opp_val = getattr(value, "tgg_Rule39", None)
                if opp_val is None:
                    setattr(value, "tgg_Rule39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tgg_Rule117(self):
        return self.__tgg_Rule117

    @tgg_Rule117.setter
    def tgg_Rule117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule117", None)
        self.__tgg_Rule117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_ComplementRule116"):
                opp_val = getattr(old_value, "tgg_ComplementRule116", None)
                if opp_val == self:
                    setattr(old_value, "tgg_ComplementRule116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_ComplementRule116"):
                opp_val = getattr(value, "tgg_ComplementRule116", None)
                setattr(value, "tgg_ComplementRule116", self)

    @property
    def tgg_Rule39(self):
        return self.__tgg_Rule39

    @tgg_Rule39.setter
    def tgg_Rule39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule39", None)
        self.__tgg_Rule39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_Rule41"):
                    opp_val = getattr(item, "tgg_Rule41", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_Rule41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_Rule41"):
                    opp_val = getattr(item, "tgg_Rule41", None)
                    
                    setattr(item, "tgg_Rule41", self)
                    

    @property
    def tgg_Rule51(self):
        return self.__tgg_Rule51

    @tgg_Rule51.setter
    def tgg_Rule51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule51", None)
        self.__tgg_Rule51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_CorrVariablePattern"):
                    opp_val = getattr(item, "tgg_CorrVariablePattern", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_CorrVariablePattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_CorrVariablePattern"):
                    opp_val = getattr(item, "tgg_CorrVariablePattern", None)
                    
                    setattr(item, "tgg_CorrVariablePattern", self)
                    

    @property
    def tgg_Rule53(self):
        return self.__tgg_Rule53

    @tgg_Rule53.setter
    def tgg_Rule53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule53", None)
        self.__tgg_Rule53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_AttrCond"):
                    opp_val = getattr(item, "tgg_AttrCond", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_AttrCond", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_AttrCond"):
                    opp_val = getattr(item, "tgg_AttrCond", None)
                    
                    setattr(item, "tgg_AttrCond", self)
                    

    @property
    def tgg_Rule43(self):
        return self.__tgg_Rule43

    @tgg_Rule43.setter
    def tgg_Rule43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule43", None)
        self.__tgg_Rule43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Schema44"):
                opp_val = getattr(old_value, "tgg_Schema44", None)
                if opp_val == self:
                    setattr(old_value, "tgg_Schema44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Schema44"):
                opp_val = getattr(value, "tgg_Schema44", None)
                setattr(value, "tgg_Schema44", self)

    @property
    def tgg_Rule48(self):
        return self.__tgg_Rule48

    @tgg_Rule48.setter
    def tgg_Rule48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule48", None)
        self.__tgg_Rule48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tgg_ObjectVariablePattern49"):
                    opp_val = getattr(item, "tgg_ObjectVariablePattern49", None)
                    
                    if opp_val == self:
                        setattr(item, "tgg_ObjectVariablePattern49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tgg_ObjectVariablePattern49"):
                    opp_val = getattr(item, "tgg_ObjectVariablePattern49", None)
                    
                    setattr(item, "tgg_ObjectVariablePattern49", self)
                    

    @property
    def tgg_Rule132(self):
        return self.__tgg_Rule132

    @tgg_Rule132.setter
    def tgg_Rule132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Rule__tgg_Rule132", None)
        self.__tgg_Rule132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_Nac131"):
                opp_val = getattr(old_value, "tgg_Nac131", None)
                if opp_val == self:
                    setattr(old_value, "tgg_Nac131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_Nac131"):
                opp_val = getattr(value, "tgg_Nac131", None)
                setattr(value, "tgg_Nac131", self)

class tgg_Schema(NamedElements):

    pass
class tgg_Using:

    def __init__(self, importedNamespace: str, tgg_Using: "tgg_TripleGraphGrammarFile" = None):
        self.importedNamespace = importedNamespace
        self.tgg_Using = tgg_Using
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def tgg_Using(self):
        return self.__tgg_Using

    @tgg_Using.setter
    def tgg_Using(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Using__tgg_Using", None)
        self.__tgg_Using = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_TripleGraphGrammarFile2"):
                opp_val = getattr(old_value, "tgg_TripleGraphGrammarFile2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_TripleGraphGrammarFile2"):
                opp_val = getattr(value, "tgg_TripleGraphGrammarFile2", None)
                if opp_val is None:
                    setattr(value, "tgg_TripleGraphGrammarFile2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tgg_Import:

    def __init__(self, name: str, tgg_Import: "tgg_TripleGraphGrammarFile" = None):
        self.name = name
        self.tgg_Import = tgg_Import
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tgg_Import(self):
        return self.__tgg_Import

    @tgg_Import.setter
    def tgg_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tgg_Import__tgg_Import", None)
        self.__tgg_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgg_TripleGraphGrammarFile"):
                opp_val = getattr(old_value, "tgg_TripleGraphGrammarFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgg_TripleGraphGrammarFile"):
                opp_val = getattr(value, "tgg_TripleGraphGrammarFile", None)
                if opp_val is None:
                    setattr(value, "tgg_TripleGraphGrammarFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tgg_TripleGraphGrammarFile:

    pass