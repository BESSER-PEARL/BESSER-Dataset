from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeSpec(Enum):
    void = "void"
    any = "any"
    string = "string"
    int = "int"
    boolean = "boolean"
    real = "real"
    type = "type"
class VisibilityModifier(Enum):
    public = "public"
    private = "private"
class AnnotationTargetSpec(Enum):
    module = "module"
    rule = "rule"
    parameter = "parameter"
class CollectionTypeSpec(Enum):
    Collection = "Collection"
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
class AssignmentOperator(Enum):
    set = "set"
    add = "add"
    sub = "sub"
class UnaryMathOperator(Enum):
    plus = "plus"
    minus = "minus"
class BooleanOperator(Enum):
    and = "and"
    or = "or"
    andsc = "andsc"
    orsc = "orsc"
class EqualityOperator(Enum):
    eq = "eq"
    neq = "neq"
class ParameterModifier(Enum):
    use = "use"
    from = "from"
    into = "into"
    return = "return"
    create = "create"
class MathOperator(Enum):
    add = "add"
    sub = "sub"
    mul = "mul"
    div = "div"
class ExecutionModifier(Enum):
    called = "called"
    abstract = "abstract"
    manual = "manual"
    auto = "auto"
    confirm = "confirm"
class RelationalOperator(Enum):
    lt = "lt"
    gt = "gt"
    leq = "leq"
    geq = "geq"
class PPOperator(Enum):
    NULL = "NULL"
    inc = "inc"
    dec = "dec"


############################################
# Definition of Classes
############################################

class mitra_AnnotationProperty:

    pass
class mitra_AnnotationPropertyDecl:

    def __init__(self, name: str, required: bool, mitra_AnnotationPropertyDecl: "mitra_AnnotationDecl" = None, mitra_AnnotationPropertyDecl178: "mitra_PrimitiveType" = None, mitra_AnnotationPropertyDecl181: "mitra_Literal" = None, mitra_AnnotationPropertyDecl193: "mitra_AnnotationProperty" = None):
        self.name = name
        self.required = required
        self.mitra_AnnotationPropertyDecl = mitra_AnnotationPropertyDecl
        self.mitra_AnnotationPropertyDecl178 = mitra_AnnotationPropertyDecl178
        self.mitra_AnnotationPropertyDecl181 = mitra_AnnotationPropertyDecl181
        self.mitra_AnnotationPropertyDecl193 = mitra_AnnotationPropertyDecl193
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def mitra_AnnotationPropertyDecl178(self):
        return self.__mitra_AnnotationPropertyDecl178

    @mitra_AnnotationPropertyDecl178.setter
    def mitra_AnnotationPropertyDecl178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationPropertyDecl__mitra_AnnotationPropertyDecl178", None)
        self.__mitra_AnnotationPropertyDecl178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_PrimitiveType179"):
                opp_val = getattr(old_value, "mitra_PrimitiveType179", None)
                if opp_val == self:
                    setattr(old_value, "mitra_PrimitiveType179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_PrimitiveType179"):
                opp_val = getattr(value, "mitra_PrimitiveType179", None)
                setattr(value, "mitra_PrimitiveType179", self)

    @property
    def mitra_AnnotationPropertyDecl193(self):
        return self.__mitra_AnnotationPropertyDecl193

    @mitra_AnnotationPropertyDecl193.setter
    def mitra_AnnotationPropertyDecl193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationPropertyDecl__mitra_AnnotationPropertyDecl193", None)
        self.__mitra_AnnotationPropertyDecl193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_AnnotationProperty192"):
                opp_val = getattr(old_value, "mitra_AnnotationProperty192", None)
                if opp_val == self:
                    setattr(old_value, "mitra_AnnotationProperty192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_AnnotationProperty192"):
                opp_val = getattr(value, "mitra_AnnotationProperty192", None)
                setattr(value, "mitra_AnnotationProperty192", self)

    @property
    def mitra_AnnotationPropertyDecl181(self):
        return self.__mitra_AnnotationPropertyDecl181

    @mitra_AnnotationPropertyDecl181.setter
    def mitra_AnnotationPropertyDecl181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationPropertyDecl__mitra_AnnotationPropertyDecl181", None)
        self.__mitra_AnnotationPropertyDecl181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Literal182"):
                opp_val = getattr(old_value, "mitra_Literal182", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Literal182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Literal182"):
                opp_val = getattr(value, "mitra_Literal182", None)
                setattr(value, "mitra_Literal182", self)

    @property
    def mitra_AnnotationPropertyDecl(self):
        return self.__mitra_AnnotationPropertyDecl

    @mitra_AnnotationPropertyDecl.setter
    def mitra_AnnotationPropertyDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationPropertyDecl__mitra_AnnotationPropertyDecl", None)
        self.__mitra_AnnotationPropertyDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_AnnotationDecl176"):
                opp_val = getattr(old_value, "mitra_AnnotationDecl176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_AnnotationDecl176"):
                opp_val = getattr(value, "mitra_AnnotationDecl176", None)
                if opp_val is None:
                    setattr(value, "mitra_AnnotationDecl176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mitra_AnnotationDecl:

    def __init__(self, name: str, targets: str, many: bool, required: bool, mitra_AnnotationDecl: "mitra_AnnotationsDefinition" = None, mitra_AnnotationDecl172: "mitra_PrimitiveType" = None, mitra_AnnotationDecl176: set["mitra_AnnotationPropertyDecl"] = None, mitra_AnnotationDecl174: "mitra_Literal" = None, mitra_AnnotationDecl185: "mitra_Annotation" = None):
        self.name = name
        self.targets = targets
        self.many = many
        self.required = required
        self.mitra_AnnotationDecl = mitra_AnnotationDecl
        self.mitra_AnnotationDecl172 = mitra_AnnotationDecl172
        self.mitra_AnnotationDecl176 = mitra_AnnotationDecl176 if mitra_AnnotationDecl176 is not None else set()
        self.mitra_AnnotationDecl174 = mitra_AnnotationDecl174
        self.mitra_AnnotationDecl185 = mitra_AnnotationDecl185
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def targets(self) -> str:
        return self.__targets

    @targets.setter
    def targets(self, targets: str):
        self.__targets = targets

    @property
    def mitra_AnnotationDecl185(self):
        return self.__mitra_AnnotationDecl185

    @mitra_AnnotationDecl185.setter
    def mitra_AnnotationDecl185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationDecl__mitra_AnnotationDecl185", None)
        self.__mitra_AnnotationDecl185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Annotation184"):
                opp_val = getattr(old_value, "mitra_Annotation184", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Annotation184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Annotation184"):
                opp_val = getattr(value, "mitra_Annotation184", None)
                setattr(value, "mitra_Annotation184", self)

    @property
    def mitra_AnnotationDecl174(self):
        return self.__mitra_AnnotationDecl174

    @mitra_AnnotationDecl174.setter
    def mitra_AnnotationDecl174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationDecl__mitra_AnnotationDecl174", None)
        self.__mitra_AnnotationDecl174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Literal"):
                opp_val = getattr(old_value, "mitra_Literal", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Literal"):
                opp_val = getattr(value, "mitra_Literal", None)
                setattr(value, "mitra_Literal", self)

    @property
    def mitra_AnnotationDecl176(self):
        return self.__mitra_AnnotationDecl176

    @mitra_AnnotationDecl176.setter
    def mitra_AnnotationDecl176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationDecl__mitra_AnnotationDecl176", None)
        self.__mitra_AnnotationDecl176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_AnnotationPropertyDecl"):
                    opp_val = getattr(item, "mitra_AnnotationPropertyDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_AnnotationPropertyDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_AnnotationPropertyDecl"):
                    opp_val = getattr(item, "mitra_AnnotationPropertyDecl", None)
                    
                    setattr(item, "mitra_AnnotationPropertyDecl", self)
                    

    @property
    def mitra_AnnotationDecl(self):
        return self.__mitra_AnnotationDecl

    @mitra_AnnotationDecl.setter
    def mitra_AnnotationDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationDecl__mitra_AnnotationDecl", None)
        self.__mitra_AnnotationDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_AnnotationsDefinition170"):
                opp_val = getattr(old_value, "mitra_AnnotationsDefinition170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_AnnotationsDefinition170"):
                opp_val = getattr(value, "mitra_AnnotationsDefinition170", None)
                if opp_val is None:
                    setattr(value, "mitra_AnnotationsDefinition170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_AnnotationDecl172(self):
        return self.__mitra_AnnotationDecl172

    @mitra_AnnotationDecl172.setter
    def mitra_AnnotationDecl172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_AnnotationDecl__mitra_AnnotationDecl172", None)
        self.__mitra_AnnotationDecl172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_PrimitiveType"):
                opp_val = getattr(old_value, "mitra_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "mitra_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_PrimitiveType"):
                opp_val = getattr(value, "mitra_PrimitiveType", None)
                setattr(value, "mitra_PrimitiveType", self)

class MetamodelFeature:

    pass
class MethodInvocation:

    pass
class mitra_FeatureMethodInvocation(MetamodelFeature, MethodInvocation):

    pass
class mitra_MetamodelFeature:

    pass
class mitra_NativeOperationInvocation(MethodInvocation):

    pass
class Feature:

    pass
class mitra_FeatureField(MetamodelFeature, Feature):

    pass
class mitra_MethodInvocation(Feature):

    pass
class mitra_Feature:

    def __init__(self, name: str, mitra_Feature: "mitra_VariableAccess" = None, mitra_Feature168: "mitra_StaticAccess" = None):
        self.name = name
        self.mitra_Feature = mitra_Feature
        self.mitra_Feature168 = mitra_Feature168
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mitra_Feature168(self):
        return self.__mitra_Feature168

    @mitra_Feature168.setter
    def mitra_Feature168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Feature__mitra_Feature168", None)
        self.__mitra_Feature168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_StaticAccess167"):
                opp_val = getattr(old_value, "mitra_StaticAccess167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_StaticAccess167"):
                opp_val = getattr(value, "mitra_StaticAccess167", None)
                if opp_val is None:
                    setattr(value, "mitra_StaticAccess167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_Feature(self):
        return self.__mitra_Feature

    @mitra_Feature.setter
    def mitra_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Feature__mitra_Feature", None)
        self.__mitra_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_VariableAccess157"):
                opp_val = getattr(old_value, "mitra_VariableAccess157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_VariableAccess157"):
                opp_val = getattr(value, "mitra_VariableAccess157", None)
                if opp_val is None:
                    setattr(value, "mitra_VariableAccess157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class Literal:

    pass
class mitra_StringLiteral(Literal):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class TerminalExpression:

    pass
class mitra_Literal(TerminalExpression):

    pass
class Expression:

    pass
class mitra_EqualityExpression(Expression):

    def __init__(self, op: str, mitra_EqualityExpression: "mitra_Expression" = None, mitra_EqualityExpression215: "mitra_Expression" = None):
        self.op = op
        self.mitra_EqualityExpression = mitra_EqualityExpression
        self.mitra_EqualityExpression215 = mitra_EqualityExpression215
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def mitra_EqualityExpression215(self):
        return self.__mitra_EqualityExpression215

    @mitra_EqualityExpression215.setter
    def mitra_EqualityExpression215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_EqualityExpression__mitra_EqualityExpression215", None)
        self.__mitra_EqualityExpression215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression216"):
                opp_val = getattr(old_value, "mitra_Expression216", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression216"):
                opp_val = getattr(value, "mitra_Expression216", None)
                setattr(value, "mitra_Expression216", self)

    @property
    def mitra_EqualityExpression(self):
        return self.__mitra_EqualityExpression

    @mitra_EqualityExpression.setter
    def mitra_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_EqualityExpression__mitra_EqualityExpression", None)
        self.__mitra_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression213"):
                opp_val = getattr(old_value, "mitra_Expression213", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression213"):
                opp_val = getattr(value, "mitra_Expression213", None)
                setattr(value, "mitra_Expression213", self)

class mitra_UnaryCastExpression(Expression):

    pass
class mitra_BooleanExpression(Expression):

    def __init__(self, op: str, mitra_BooleanExpression: "mitra_Expression" = None, mitra_BooleanExpression210: "mitra_Expression" = None):
        self.op = op
        self.mitra_BooleanExpression = mitra_BooleanExpression
        self.mitra_BooleanExpression210 = mitra_BooleanExpression210
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def mitra_BooleanExpression210(self):
        return self.__mitra_BooleanExpression210

    @mitra_BooleanExpression210.setter
    def mitra_BooleanExpression210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_BooleanExpression__mitra_BooleanExpression210", None)
        self.__mitra_BooleanExpression210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression211"):
                opp_val = getattr(old_value, "mitra_Expression211", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression211"):
                opp_val = getattr(value, "mitra_Expression211", None)
                setattr(value, "mitra_Expression211", self)

    @property
    def mitra_BooleanExpression(self):
        return self.__mitra_BooleanExpression

    @mitra_BooleanExpression.setter
    def mitra_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_BooleanExpression__mitra_BooleanExpression", None)
        self.__mitra_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression208"):
                opp_val = getattr(old_value, "mitra_Expression208", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression208"):
                opp_val = getattr(value, "mitra_Expression208", None)
                setattr(value, "mitra_Expression208", self)

class mitra_UnaryBooleanExpression(Expression):

    pass
class mitra_MathExpression(Expression):

    def __init__(self, op: str, mitra_MathExpression: "mitra_Expression" = None, mitra_MathExpression225: "mitra_Expression" = None):
        self.op = op
        self.mitra_MathExpression = mitra_MathExpression
        self.mitra_MathExpression225 = mitra_MathExpression225
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def mitra_MathExpression225(self):
        return self.__mitra_MathExpression225

    @mitra_MathExpression225.setter
    def mitra_MathExpression225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_MathExpression__mitra_MathExpression225", None)
        self.__mitra_MathExpression225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression226"):
                opp_val = getattr(old_value, "mitra_Expression226", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression226"):
                opp_val = getattr(value, "mitra_Expression226", None)
                setattr(value, "mitra_Expression226", self)

    @property
    def mitra_MathExpression(self):
        return self.__mitra_MathExpression

    @mitra_MathExpression.setter
    def mitra_MathExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_MathExpression__mitra_MathExpression", None)
        self.__mitra_MathExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression223"):
                opp_val = getattr(old_value, "mitra_Expression223", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression223"):
                opp_val = getattr(value, "mitra_Expression223", None)
                setattr(value, "mitra_Expression223", self)

class mitra_IteratorExpression(Expression):

    pass
class mitra_RelationalExpression(Expression):

    def __init__(self, op: str, mitra_RelationalExpression220: "mitra_Expression" = None, mitra_RelationalExpression: "mitra_Expression" = None):
        self.op = op
        self.mitra_RelationalExpression220 = mitra_RelationalExpression220
        self.mitra_RelationalExpression = mitra_RelationalExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def mitra_RelationalExpression(self):
        return self.__mitra_RelationalExpression

    @mitra_RelationalExpression.setter
    def mitra_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RelationalExpression__mitra_RelationalExpression", None)
        self.__mitra_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression218"):
                opp_val = getattr(old_value, "mitra_Expression218", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression218"):
                opp_val = getattr(value, "mitra_Expression218", None)
                setattr(value, "mitra_Expression218", self)

    @property
    def mitra_RelationalExpression220(self):
        return self.__mitra_RelationalExpression220

    @mitra_RelationalExpression220.setter
    def mitra_RelationalExpression220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RelationalExpression__mitra_RelationalExpression220", None)
        self.__mitra_RelationalExpression220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression221"):
                opp_val = getattr(old_value, "mitra_Expression221", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression221"):
                opp_val = getattr(value, "mitra_Expression221", None)
                setattr(value, "mitra_Expression221", self)

class mitra_UnaryMathExpression(Expression):

    def __init__(self, op: str, mitra_UnaryMathExpression: "mitra_Expression" = None):
        self.op = op
        self.mitra_UnaryMathExpression = mitra_UnaryMathExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def mitra_UnaryMathExpression(self):
        return self.__mitra_UnaryMathExpression

    @mitra_UnaryMathExpression.setter
    def mitra_UnaryMathExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_UnaryMathExpression__mitra_UnaryMathExpression", None)
        self.__mitra_UnaryMathExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression235"):
                opp_val = getattr(old_value, "mitra_Expression235", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression235"):
                opp_val = getattr(value, "mitra_Expression235", None)
                setattr(value, "mitra_Expression235", self)

class mitra_InstanceOfExpression(Expression):

    pass
class StatementExpression:

    pass
class mitra_Assignment(StatementExpression):

    def __init__(self, operator: str, mitra_Assignment: set["mitra_VariableAccess"] = None, mitra_Assignment200: "mitra_Expression" = None):
        self.operator = operator
        self.mitra_Assignment = mitra_Assignment if mitra_Assignment is not None else set()
        self.mitra_Assignment200 = mitra_Assignment200
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mitra_Assignment200(self):
        return self.__mitra_Assignment200

    @mitra_Assignment200.setter
    def mitra_Assignment200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Assignment__mitra_Assignment200", None)
        self.__mitra_Assignment200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression201"):
                opp_val = getattr(old_value, "mitra_Expression201", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression201"):
                opp_val = getattr(value, "mitra_Expression201", None)
                setattr(value, "mitra_Expression201", self)

    @property
    def mitra_Assignment(self):
        return self.__mitra_Assignment

    @mitra_Assignment.setter
    def mitra_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Assignment__mitra_Assignment", None)
        self.__mitra_Assignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_VariableAccess198"):
                    opp_val = getattr(item, "mitra_VariableAccess198", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_VariableAccess198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_VariableAccess198"):
                    opp_val = getattr(item, "mitra_VariableAccess198", None)
                    
                    setattr(item, "mitra_VariableAccess198", self)
                    

class mitra_RuleInvocation(TerminalExpression, StatementExpression):

    def __init__(self, mitra_RuleInvocation: "mitra_RuleDeclaration" = None, mitra_RuleInvocation146: set["mitra_Expression"] = None):
        self.mitra_RuleInvocation = mitra_RuleInvocation
        self.mitra_RuleInvocation146 = mitra_RuleInvocation146 if mitra_RuleInvocation146 is not None else set()
        
    @property
    def mitra_RuleInvocation146(self):
        return self.__mitra_RuleInvocation146

    @mitra_RuleInvocation146.setter
    def mitra_RuleInvocation146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleInvocation__mitra_RuleInvocation146", None)
        self.__mitra_RuleInvocation146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_Expression147"):
                    opp_val = getattr(item, "mitra_Expression147", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_Expression147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_Expression147"):
                    opp_val = getattr(item, "mitra_Expression147", None)
                    
                    setattr(item, "mitra_Expression147", self)
                    

    @property
    def mitra_RuleInvocation(self):
        return self.__mitra_RuleInvocation

    @mitra_RuleInvocation.setter
    def mitra_RuleInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleInvocation__mitra_RuleInvocation", None)
        self.__mitra_RuleInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleDeclaration144"):
                opp_val = getattr(old_value, "mitra_RuleDeclaration144", None)
                if opp_val == self:
                    setattr(old_value, "mitra_RuleDeclaration144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleDeclaration144"):
                opp_val = getattr(value, "mitra_RuleDeclaration144", None)
                setattr(value, "mitra_RuleDeclaration144", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_StaticAccess(TerminalExpression, StatementExpression):

    pass
class mitra_VariableAccess(TerminalExpression, StatementExpression):

    def __init__(self, prefixOperator: str, postfixOperator: str, mitra_VariableAccess: "mitra_VarDeclaration" = None, mitra_VariableAccess157: set["mitra_Feature"] = None, mitra_VariableAccess159: "mitra_Expression" = None, mitra_VariableAccess198: "mitra_Assignment" = None):
        self.prefixOperator = prefixOperator
        self.postfixOperator = postfixOperator
        self.mitra_VariableAccess = mitra_VariableAccess
        self.mitra_VariableAccess157 = mitra_VariableAccess157 if mitra_VariableAccess157 is not None else set()
        self.mitra_VariableAccess159 = mitra_VariableAccess159
        self.mitra_VariableAccess198 = mitra_VariableAccess198
        
    @property
    def prefixOperator(self) -> str:
        return self.__prefixOperator

    @prefixOperator.setter
    def prefixOperator(self, prefixOperator: str):
        self.__prefixOperator = prefixOperator

    @property
    def postfixOperator(self) -> str:
        return self.__postfixOperator

    @postfixOperator.setter
    def postfixOperator(self, postfixOperator: str):
        self.__postfixOperator = postfixOperator

    @property
    def mitra_VariableAccess157(self):
        return self.__mitra_VariableAccess157

    @mitra_VariableAccess157.setter
    def mitra_VariableAccess157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VariableAccess__mitra_VariableAccess157", None)
        self.__mitra_VariableAccess157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_Feature"):
                    opp_val = getattr(item, "mitra_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_Feature"):
                    opp_val = getattr(item, "mitra_Feature", None)
                    
                    setattr(item, "mitra_Feature", self)
                    

    @property
    def mitra_VariableAccess198(self):
        return self.__mitra_VariableAccess198

    @mitra_VariableAccess198.setter
    def mitra_VariableAccess198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VariableAccess__mitra_VariableAccess198", None)
        self.__mitra_VariableAccess198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Assignment"):
                opp_val = getattr(old_value, "mitra_Assignment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Assignment"):
                opp_val = getattr(value, "mitra_Assignment", None)
                if opp_val is None:
                    setattr(value, "mitra_Assignment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_VariableAccess159(self):
        return self.__mitra_VariableAccess159

    @mitra_VariableAccess159.setter
    def mitra_VariableAccess159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VariableAccess__mitra_VariableAccess159", None)
        self.__mitra_VariableAccess159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Expression160"):
                opp_val = getattr(old_value, "mitra_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Expression160"):
                opp_val = getattr(value, "mitra_Expression160", None)
                setattr(value, "mitra_Expression160", self)

    @property
    def mitra_VariableAccess(self):
        return self.__mitra_VariableAccess

    @mitra_VariableAccess.setter
    def mitra_VariableAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VariableAccess__mitra_VariableAccess", None)
        self.__mitra_VariableAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_VarDeclaration155"):
                opp_val = getattr(old_value, "mitra_VarDeclaration155", None)
                if opp_val == self:
                    setattr(old_value, "mitra_VarDeclaration155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_VarDeclaration155"):
                opp_val = getattr(value, "mitra_VarDeclaration155", None)
                setattr(value, "mitra_VarDeclaration155", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_RuleInvocationSuper(TerminalExpression, StatementExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_ClassInstanceCreationExpression(TerminalExpression, StatementExpression):

    pass
class mitra_NullLiteral(Literal):

    pass
class mitra_BooleanLiteral(Literal):

    def __init__(self, booleanValue: bool):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> bool:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: bool):
        self.__booleanValue = booleanValue

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_RealLiteral(Literal):

    def __init__(self, floatValue: str):
        self.floatValue = floatValue
        
    @property
    def floatValue(self) -> str:
        return self.__floatValue

    @floatValue.setter
    def floatValue(self, floatValue: str):
        self.__floatValue = floatValue

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_IntLiteral(Literal):

    def __init__(self, intValue: int):
        self.intValue = intValue
        
    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_TerminalExpression(Expression):

    pass
class mitra_LoopVariable:

    pass
class mitra_Catch:

    pass
class mitra_ForUpdate:

    pass
class mitra_ForInit:

    pass
class mitra_VarDeclaration:

    def __init__(self, name: str, mitra_VarDeclaration: "mitra_Type" = None, mitra_VarDeclaration122: "mitra_LoopVariable" = None, mitra_VarDeclaration155: "mitra_VariableAccess" = None):
        self.name = name
        self.mitra_VarDeclaration = mitra_VarDeclaration
        self.mitra_VarDeclaration122 = mitra_VarDeclaration122
        self.mitra_VarDeclaration155 = mitra_VarDeclaration155
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mitra_VarDeclaration155(self):
        return self.__mitra_VarDeclaration155

    @mitra_VarDeclaration155.setter
    def mitra_VarDeclaration155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VarDeclaration__mitra_VarDeclaration155", None)
        self.__mitra_VarDeclaration155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_VariableAccess"):
                opp_val = getattr(old_value, "mitra_VariableAccess", None)
                if opp_val == self:
                    setattr(old_value, "mitra_VariableAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_VariableAccess"):
                opp_val = getattr(value, "mitra_VariableAccess", None)
                setattr(value, "mitra_VariableAccess", self)

    @property
    def mitra_VarDeclaration(self):
        return self.__mitra_VarDeclaration

    @mitra_VarDeclaration.setter
    def mitra_VarDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VarDeclaration__mitra_VarDeclaration", None)
        self.__mitra_VarDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Type79"):
                opp_val = getattr(old_value, "mitra_Type79", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Type79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Type79"):
                opp_val = getattr(value, "mitra_Type79", None)
                setattr(value, "mitra_Type79", self)

    @property
    def mitra_VarDeclaration122(self):
        return self.__mitra_VarDeclaration122

    @mitra_VarDeclaration122.setter
    def mitra_VarDeclaration122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_VarDeclaration__mitra_VarDeclaration122", None)
        self.__mitra_VarDeclaration122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_LoopVariable121"):
                opp_val = getattr(old_value, "mitra_LoopVariable121", None)
                if opp_val == self:
                    setattr(old_value, "mitra_LoopVariable121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_LoopVariable121"):
                opp_val = getattr(value, "mitra_LoopVariable121", None)
                setattr(value, "mitra_LoopVariable121", self)

class mitra_StatementExpression:

    pass
class VarDeclaration:

    pass
class mitra_InferredVarDeclaration(VarDeclaration):

    pass
class mitra_LocalVariableDeclaration:

    pass
class BlockStatement:

    pass
class mitra_LocalVariableDeclarationStatement(BlockStatement):

    pass
class mitra_Statement(BlockStatement):

    pass
class mitra_BlockStatement:

    pass
class Statement:

    pass
class mitra_TryStatement(Statement):

    pass
class mitra_EmptyStatement(Statement):

    pass
class mitra_DoStatement(Statement):

    pass
class mitra_WhileStatement(Statement):

    pass
class mitra_IfStatement(Statement):

    pass
class mitra_ExpressionStatement(Statement):

    pass
class mitra_ReturnStatement(Statement):

    pass
class mitra_ForStatement(Statement):

    pass
class mitra_BreakStatement(Statement):

    pass
class mitra_ThrowStatement(Statement):

    pass
class mitra_EClassifier:

    pass
class Type:

    pass
class mitra_CollectionType(Type):

    def __init__(self, collectionType: str, mitra_CollectionType: "mitra_Type" = None):
        self.collectionType = collectionType
        self.mitra_CollectionType = mitra_CollectionType
        
    @property
    def collectionType(self) -> str:
        return self.__collectionType

    @collectionType.setter
    def collectionType(self, collectionType: str):
        self.__collectionType = collectionType

    @property
    def mitra_CollectionType(self):
        return self.__mitra_CollectionType

    @mitra_CollectionType.setter
    def mitra_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_CollectionType__mitra_CollectionType", None)
        self.__mitra_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Type68"):
                opp_val = getattr(old_value, "mitra_Type68", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Type68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Type68"):
                opp_val = getattr(value, "mitra_Type68", None)
                setattr(value, "mitra_Type68", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_PrimitiveType(Type):

    def __init__(self, primitiveType: str, mitra_PrimitiveType: "mitra_AnnotationDecl" = None, mitra_PrimitiveType179: "mitra_AnnotationPropertyDecl" = None):
        self.primitiveType = primitiveType
        self.mitra_PrimitiveType = mitra_PrimitiveType
        self.mitra_PrimitiveType179 = mitra_PrimitiveType179
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def mitra_PrimitiveType(self):
        return self.__mitra_PrimitiveType

    @mitra_PrimitiveType.setter
    def mitra_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_PrimitiveType__mitra_PrimitiveType", None)
        self.__mitra_PrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_AnnotationDecl172"):
                opp_val = getattr(old_value, "mitra_AnnotationDecl172", None)
                if opp_val == self:
                    setattr(old_value, "mitra_AnnotationDecl172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_AnnotationDecl172"):
                opp_val = getattr(value, "mitra_AnnotationDecl172", None)
                setattr(value, "mitra_AnnotationDecl172", self)

    @property
    def mitra_PrimitiveType179(self):
        return self.__mitra_PrimitiveType179

    @mitra_PrimitiveType179.setter
    def mitra_PrimitiveType179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_PrimitiveType__mitra_PrimitiveType179", None)
        self.__mitra_PrimitiveType179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_AnnotationPropertyDecl178"):
                opp_val = getattr(old_value, "mitra_AnnotationPropertyDecl178", None)
                if opp_val == self:
                    setattr(old_value, "mitra_AnnotationPropertyDecl178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_AnnotationPropertyDecl178"):
                opp_val = getattr(value, "mitra_AnnotationPropertyDecl178", None)
                setattr(value, "mitra_AnnotationPropertyDecl178", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_ReferenceType(Type):

    def __init__(self, mitra_ReferenceType: "mitra_MetamodelDeclaration" = None, mitra_ReferenceType66: "mitra_EClassifier" = None):
        self.mitra_ReferenceType = mitra_ReferenceType
        self.mitra_ReferenceType66 = mitra_ReferenceType66
        
    @property
    def mitra_ReferenceType66(self):
        return self.__mitra_ReferenceType66

    @mitra_ReferenceType66.setter
    def mitra_ReferenceType66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_ReferenceType__mitra_ReferenceType66", None)
        self.__mitra_ReferenceType66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_EClassifier"):
                opp_val = getattr(old_value, "mitra_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "mitra_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_EClassifier"):
                opp_val = getattr(value, "mitra_EClassifier", None)
                setattr(value, "mitra_EClassifier", self)

    @property
    def mitra_ReferenceType(self):
        return self.__mitra_ReferenceType

    @mitra_ReferenceType.setter
    def mitra_ReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_ReferenceType__mitra_ReferenceType", None)
        self.__mitra_ReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_MetamodelDeclaration64"):
                opp_val = getattr(old_value, "mitra_MetamodelDeclaration64", None)
                if opp_val == self:
                    setattr(old_value, "mitra_MetamodelDeclaration64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_MetamodelDeclaration64"):
                opp_val = getattr(value, "mitra_MetamodelDeclaration64", None)
                setattr(value, "mitra_MetamodelDeclaration64", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_Expression:

    pass
class mitra_TypedVarDeclaration(VarDeclaration):

    pass
class Parameter:

    pass
class mitra_Type:

    pass
class mitra_Parameter:

    def __init__(self, modifier: str, mitra_Parameter: set["mitra_Annotation"] = None, mitra_Parameter61: "mitra_TypedVarDeclaration" = None):
        self.modifier = modifier
        self.mitra_Parameter = mitra_Parameter if mitra_Parameter is not None else set()
        self.mitra_Parameter61 = mitra_Parameter61
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def mitra_Parameter(self):
        return self.__mitra_Parameter

    @mitra_Parameter.setter
    def mitra_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Parameter__mitra_Parameter", None)
        self.__mitra_Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_Annotation59"):
                    opp_val = getattr(item, "mitra_Annotation59", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_Annotation59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_Annotation59"):
                    opp_val = getattr(item, "mitra_Annotation59", None)
                    
                    setattr(item, "mitra_Annotation59", self)
                    

    @property
    def mitra_Parameter61(self):
        return self.__mitra_Parameter61

    @mitra_Parameter61.setter
    def mitra_Parameter61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Parameter__mitra_Parameter61", None)
        self.__mitra_Parameter61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_TypedVarDeclaration62"):
                opp_val = getattr(old_value, "mitra_TypedVarDeclaration62", None)
                if opp_val == self:
                    setattr(old_value, "mitra_TypedVarDeclaration62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_TypedVarDeclaration62"):
                opp_val = getattr(value, "mitra_TypedVarDeclaration62", None)
                setattr(value, "mitra_TypedVarDeclaration62", self)

class ParameterReference:

    pass
class mitra_ParameterReference:

    pass
class mitra_SimpleParameterReference(ParameterReference):

    def __init__(self, name: str, mitra_SimpleParameterReference: "mitra_SimpleRuleReference" = None, mitra_SimpleParameterReference38: "mitra_SimpleRuleReference" = None, mitra_SimpleParameterReference44: "mitra_Type" = None):
        self.name = name
        self.mitra_SimpleParameterReference = mitra_SimpleParameterReference
        self.mitra_SimpleParameterReference38 = mitra_SimpleParameterReference38
        self.mitra_SimpleParameterReference44 = mitra_SimpleParameterReference44
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mitra_SimpleParameterReference44(self):
        return self.__mitra_SimpleParameterReference44

    @mitra_SimpleParameterReference44.setter
    def mitra_SimpleParameterReference44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleParameterReference__mitra_SimpleParameterReference44", None)
        self.__mitra_SimpleParameterReference44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Type"):
                opp_val = getattr(old_value, "mitra_Type", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Type"):
                opp_val = getattr(value, "mitra_Type", None)
                setattr(value, "mitra_Type", self)

    @property
    def mitra_SimpleParameterReference38(self):
        return self.__mitra_SimpleParameterReference38

    @mitra_SimpleParameterReference38.setter
    def mitra_SimpleParameterReference38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleParameterReference__mitra_SimpleParameterReference38", None)
        self.__mitra_SimpleParameterReference38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_SimpleRuleReference37"):
                opp_val = getattr(old_value, "mitra_SimpleRuleReference37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_SimpleRuleReference37"):
                opp_val = getattr(value, "mitra_SimpleRuleReference37", None)
                if opp_val is None:
                    setattr(value, "mitra_SimpleRuleReference37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_SimpleParameterReference(self):
        return self.__mitra_SimpleParameterReference

    @mitra_SimpleParameterReference.setter
    def mitra_SimpleParameterReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleParameterReference__mitra_SimpleParameterReference", None)
        self.__mitra_SimpleParameterReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_SimpleRuleReference35"):
                opp_val = getattr(old_value, "mitra_SimpleRuleReference35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_SimpleRuleReference35"):
                opp_val = getattr(value, "mitra_SimpleRuleReference35", None)
                if opp_val is None:
                    setattr(value, "mitra_SimpleRuleReference35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class RuleReference:

    pass
class mitra_QualifiedRuleReference(RuleReference):

    def __init__(self, mitra_QualifiedRuleReference: set["mitra_QualifiedParameterReference"] = None, mitra_QualifiedRuleReference41: set["mitra_QualifiedParameterReference"] = None, mitra_QualifiedRuleReference49: "mitra_Trigger" = None):
        self.mitra_QualifiedRuleReference = mitra_QualifiedRuleReference if mitra_QualifiedRuleReference is not None else set()
        self.mitra_QualifiedRuleReference41 = mitra_QualifiedRuleReference41 if mitra_QualifiedRuleReference41 is not None else set()
        self.mitra_QualifiedRuleReference49 = mitra_QualifiedRuleReference49
        
    @property
    def mitra_QualifiedRuleReference(self):
        return self.__mitra_QualifiedRuleReference

    @mitra_QualifiedRuleReference.setter
    def mitra_QualifiedRuleReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_QualifiedRuleReference__mitra_QualifiedRuleReference", None)
        self.__mitra_QualifiedRuleReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_QualifiedParameterReference"):
                    opp_val = getattr(item, "mitra_QualifiedParameterReference", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_QualifiedParameterReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_QualifiedParameterReference"):
                    opp_val = getattr(item, "mitra_QualifiedParameterReference", None)
                    
                    setattr(item, "mitra_QualifiedParameterReference", self)
                    

    @property
    def mitra_QualifiedRuleReference49(self):
        return self.__mitra_QualifiedRuleReference49

    @mitra_QualifiedRuleReference49.setter
    def mitra_QualifiedRuleReference49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_QualifiedRuleReference__mitra_QualifiedRuleReference49", None)
        self.__mitra_QualifiedRuleReference49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Trigger48"):
                opp_val = getattr(old_value, "mitra_Trigger48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Trigger48"):
                opp_val = getattr(value, "mitra_Trigger48", None)
                if opp_val is None:
                    setattr(value, "mitra_Trigger48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_QualifiedRuleReference41(self):
        return self.__mitra_QualifiedRuleReference41

    @mitra_QualifiedRuleReference41.setter
    def mitra_QualifiedRuleReference41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_QualifiedRuleReference__mitra_QualifiedRuleReference41", None)
        self.__mitra_QualifiedRuleReference41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_QualifiedParameterReference42"):
                    opp_val = getattr(item, "mitra_QualifiedParameterReference42", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_QualifiedParameterReference42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_QualifiedParameterReference42"):
                    opp_val = getattr(item, "mitra_QualifiedParameterReference42", None)
                    
                    setattr(item, "mitra_QualifiedParameterReference42", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_RuleReference:

    pass
class mitra_Block(Statement):

    pass
class mitra_JavaSpec:

    pass
class mitra_Trigger:

    pass
class mitra_QualifiedParameterReference(ParameterReference):

    def __init__(self, mitra_QualifiedParameterReference: "mitra_QualifiedRuleReference" = None, mitra_QualifiedParameterReference42: "mitra_QualifiedRuleReference" = None, mitra_QualifiedParameterReference46: "mitra_TypedVarDeclaration" = None):
        self.mitra_QualifiedParameterReference = mitra_QualifiedParameterReference
        self.mitra_QualifiedParameterReference42 = mitra_QualifiedParameterReference42
        self.mitra_QualifiedParameterReference46 = mitra_QualifiedParameterReference46
        
    @property
    def mitra_QualifiedParameterReference42(self):
        return self.__mitra_QualifiedParameterReference42

    @mitra_QualifiedParameterReference42.setter
    def mitra_QualifiedParameterReference42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_QualifiedParameterReference__mitra_QualifiedParameterReference42", None)
        self.__mitra_QualifiedParameterReference42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_QualifiedRuleReference41"):
                opp_val = getattr(old_value, "mitra_QualifiedRuleReference41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_QualifiedRuleReference41"):
                opp_val = getattr(value, "mitra_QualifiedRuleReference41", None)
                if opp_val is None:
                    setattr(value, "mitra_QualifiedRuleReference41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_QualifiedParameterReference46(self):
        return self.__mitra_QualifiedParameterReference46

    @mitra_QualifiedParameterReference46.setter
    def mitra_QualifiedParameterReference46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_QualifiedParameterReference__mitra_QualifiedParameterReference46", None)
        self.__mitra_QualifiedParameterReference46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_TypedVarDeclaration"):
                opp_val = getattr(old_value, "mitra_TypedVarDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "mitra_TypedVarDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_TypedVarDeclaration"):
                opp_val = getattr(value, "mitra_TypedVarDeclaration", None)
                setattr(value, "mitra_TypedVarDeclaration", self)

    @property
    def mitra_QualifiedParameterReference(self):
        return self.__mitra_QualifiedParameterReference

    @mitra_QualifiedParameterReference.setter
    def mitra_QualifiedParameterReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_QualifiedParameterReference__mitra_QualifiedParameterReference", None)
        self.__mitra_QualifiedParameterReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_QualifiedRuleReference"):
                opp_val = getattr(old_value, "mitra_QualifiedRuleReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_QualifiedRuleReference"):
                opp_val = getattr(value, "mitra_QualifiedRuleReference", None)
                if opp_val is None:
                    setattr(value, "mitra_QualifiedRuleReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_SimpleRuleReference(RuleReference):

    def __init__(self, mitra_SimpleRuleReference25: "mitra_RuleDeclaration" = None, mitra_SimpleRuleReference: "mitra_RuleDeclaration" = None, mitra_SimpleRuleReference22: "mitra_RuleDeclaration" = None, mitra_SimpleRuleReference35: set["mitra_SimpleParameterReference"] = None, mitra_SimpleRuleReference37: set["mitra_SimpleParameterReference"] = None):
        self.mitra_SimpleRuleReference25 = mitra_SimpleRuleReference25
        self.mitra_SimpleRuleReference = mitra_SimpleRuleReference
        self.mitra_SimpleRuleReference22 = mitra_SimpleRuleReference22
        self.mitra_SimpleRuleReference35 = mitra_SimpleRuleReference35 if mitra_SimpleRuleReference35 is not None else set()
        self.mitra_SimpleRuleReference37 = mitra_SimpleRuleReference37 if mitra_SimpleRuleReference37 is not None else set()
        
    @property
    def mitra_SimpleRuleReference37(self):
        return self.__mitra_SimpleRuleReference37

    @mitra_SimpleRuleReference37.setter
    def mitra_SimpleRuleReference37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleRuleReference__mitra_SimpleRuleReference37", None)
        self.__mitra_SimpleRuleReference37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_SimpleParameterReference38"):
                    opp_val = getattr(item, "mitra_SimpleParameterReference38", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_SimpleParameterReference38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_SimpleParameterReference38"):
                    opp_val = getattr(item, "mitra_SimpleParameterReference38", None)
                    
                    setattr(item, "mitra_SimpleParameterReference38", self)
                    

    @property
    def mitra_SimpleRuleReference25(self):
        return self.__mitra_SimpleRuleReference25

    @mitra_SimpleRuleReference25.setter
    def mitra_SimpleRuleReference25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleRuleReference__mitra_SimpleRuleReference25", None)
        self.__mitra_SimpleRuleReference25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleDeclaration24"):
                opp_val = getattr(old_value, "mitra_RuleDeclaration24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleDeclaration24"):
                opp_val = getattr(value, "mitra_RuleDeclaration24", None)
                if opp_val is None:
                    setattr(value, "mitra_RuleDeclaration24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_SimpleRuleReference(self):
        return self.__mitra_SimpleRuleReference

    @mitra_SimpleRuleReference.setter
    def mitra_SimpleRuleReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleRuleReference__mitra_SimpleRuleReference", None)
        self.__mitra_SimpleRuleReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleDeclaration19"):
                opp_val = getattr(old_value, "mitra_RuleDeclaration19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleDeclaration19"):
                opp_val = getattr(value, "mitra_RuleDeclaration19", None)
                if opp_val is None:
                    setattr(value, "mitra_RuleDeclaration19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_SimpleRuleReference22(self):
        return self.__mitra_SimpleRuleReference22

    @mitra_SimpleRuleReference22.setter
    def mitra_SimpleRuleReference22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleRuleReference__mitra_SimpleRuleReference22", None)
        self.__mitra_SimpleRuleReference22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleDeclaration21"):
                opp_val = getattr(old_value, "mitra_RuleDeclaration21", None)
                if opp_val == self:
                    setattr(old_value, "mitra_RuleDeclaration21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleDeclaration21"):
                opp_val = getattr(value, "mitra_RuleDeclaration21", None)
                setattr(value, "mitra_RuleDeclaration21", self)

    @property
    def mitra_SimpleRuleReference35(self):
        return self.__mitra_SimpleRuleReference35

    @mitra_SimpleRuleReference35.setter
    def mitra_SimpleRuleReference35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_SimpleRuleReference__mitra_SimpleRuleReference35", None)
        self.__mitra_SimpleRuleReference35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_SimpleParameterReference"):
                    opp_val = getattr(item, "mitra_SimpleParameterReference", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_SimpleParameterReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_SimpleParameterReference"):
                    opp_val = getattr(item, "mitra_SimpleParameterReference", None)
                    
                    setattr(item, "mitra_SimpleParameterReference", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_ReturnParameter(Parameter):

    def __init__(self, mitra_ReturnParameter: "mitra_RuleDeclaration" = None):
        self.mitra_ReturnParameter = mitra_ReturnParameter
        
    @property
    def mitra_ReturnParameter(self):
        return self.__mitra_ReturnParameter

    @mitra_ReturnParameter.setter
    def mitra_ReturnParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_ReturnParameter__mitra_ReturnParameter", None)
        self.__mitra_ReturnParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleDeclaration17"):
                opp_val = getattr(old_value, "mitra_RuleDeclaration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleDeclaration17"):
                opp_val = getattr(value, "mitra_RuleDeclaration17", None)
                if opp_val is None:
                    setattr(value, "mitra_RuleDeclaration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_FormalParameter(Parameter):

    def __init__(self, mitra_FormalParameter: "mitra_RuleDeclaration" = None, mitra_FormalParameter134: "mitra_Catch" = None):
        self.mitra_FormalParameter = mitra_FormalParameter
        self.mitra_FormalParameter134 = mitra_FormalParameter134
        
    @property
    def mitra_FormalParameter134(self):
        return self.__mitra_FormalParameter134

    @mitra_FormalParameter134.setter
    def mitra_FormalParameter134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_FormalParameter__mitra_FormalParameter134", None)
        self.__mitra_FormalParameter134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Catch133"):
                opp_val = getattr(old_value, "mitra_Catch133", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Catch133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Catch133"):
                opp_val = getattr(value, "mitra_Catch133", None)
                setattr(value, "mitra_Catch133", self)

    @property
    def mitra_FormalParameter(self):
        return self.__mitra_FormalParameter

    @mitra_FormalParameter.setter
    def mitra_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_FormalParameter__mitra_FormalParameter", None)
        self.__mitra_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleDeclaration15"):
                opp_val = getattr(old_value, "mitra_RuleDeclaration15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleDeclaration15"):
                opp_val = getattr(value, "mitra_RuleDeclaration15", None)
                if opp_val is None:
                    setattr(value, "mitra_RuleDeclaration15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_Annotation:

    pass
class mitra_Property:

    def __init__(self, value: str, name: str, mitra_Property: "mitra_MetamodelDeclaration" = None, mitra_Property57: "mitra_JavaSpec" = None):
        self.value = value
        self.name = name
        self.mitra_Property = mitra_Property
        self.mitra_Property57 = mitra_Property57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def mitra_Property57(self):
        return self.__mitra_Property57

    @mitra_Property57.setter
    def mitra_Property57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Property__mitra_Property57", None)
        self.__mitra_Property57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_JavaSpec56"):
                opp_val = getattr(old_value, "mitra_JavaSpec56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_JavaSpec56"):
                opp_val = getattr(value, "mitra_JavaSpec56", None)
                if opp_val is None:
                    setattr(value, "mitra_JavaSpec56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_Property(self):
        return self.__mitra_Property

    @mitra_Property.setter
    def mitra_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Property__mitra_Property", None)
        self.__mitra_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_MetamodelDeclaration11"):
                opp_val = getattr(old_value, "mitra_MetamodelDeclaration11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_MetamodelDeclaration11"):
                opp_val = getattr(value, "mitra_MetamodelDeclaration11", None)
                if opp_val is None:
                    setattr(value, "mitra_MetamodelDeclaration11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_RuleDeclaration:

    def __init__(self, visibility: str, exec: str, traced: bool, stealth: bool, virtual: bool, multi: bool, name: str, mitra_RuleDeclaration: "mitra_Module" = None, mitra_RuleDeclaration13: set["mitra_Annotation"] = None, mitra_RuleDeclaration15: set["mitra_FormalParameter"] = None, mitra_RuleDeclaration17: set["mitra_ReturnParameter"] = None, mitra_RuleDeclaration19: set["mitra_SimpleRuleReference"] = None, mitra_RuleDeclaration21: "mitra_SimpleRuleReference" = None, mitra_RuleDeclaration24: set["mitra_SimpleRuleReference"] = None, mitra_RuleDeclaration27: "mitra_Trigger" = None, mitra_RuleDeclaration29: "mitra_JavaSpec" = None, mitra_RuleDeclaration31: "mitra_Block" = None, mitra_RuleDeclaration33: "mitra_RuleReference" = None, mitra_RuleDeclaration144: "mitra_RuleInvocation" = None):
        self.visibility = visibility
        self.exec = exec
        self.traced = traced
        self.stealth = stealth
        self.virtual = virtual
        self.multi = multi
        self.name = name
        self.mitra_RuleDeclaration = mitra_RuleDeclaration
        self.mitra_RuleDeclaration13 = mitra_RuleDeclaration13 if mitra_RuleDeclaration13 is not None else set()
        self.mitra_RuleDeclaration15 = mitra_RuleDeclaration15 if mitra_RuleDeclaration15 is not None else set()
        self.mitra_RuleDeclaration17 = mitra_RuleDeclaration17 if mitra_RuleDeclaration17 is not None else set()
        self.mitra_RuleDeclaration19 = mitra_RuleDeclaration19 if mitra_RuleDeclaration19 is not None else set()
        self.mitra_RuleDeclaration21 = mitra_RuleDeclaration21
        self.mitra_RuleDeclaration24 = mitra_RuleDeclaration24 if mitra_RuleDeclaration24 is not None else set()
        self.mitra_RuleDeclaration27 = mitra_RuleDeclaration27
        self.mitra_RuleDeclaration29 = mitra_RuleDeclaration29
        self.mitra_RuleDeclaration31 = mitra_RuleDeclaration31
        self.mitra_RuleDeclaration33 = mitra_RuleDeclaration33
        self.mitra_RuleDeclaration144 = mitra_RuleDeclaration144
        
    @property
    def multi(self) -> bool:
        return self.__multi

    @multi.setter
    def multi(self, multi: bool):
        self.__multi = multi

    @property
    def stealth(self) -> bool:
        return self.__stealth

    @stealth.setter
    def stealth(self, stealth: bool):
        self.__stealth = stealth

    @property
    def virtual(self) -> bool:
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: bool):
        self.__virtual = virtual

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def exec(self) -> str:
        return self.__exec

    @exec.setter
    def exec(self, exec: str):
        self.__exec = exec

    @property
    def traced(self) -> bool:
        return self.__traced

    @traced.setter
    def traced(self, traced: bool):
        self.__traced = traced

    @property
    def mitra_RuleDeclaration31(self):
        return self.__mitra_RuleDeclaration31

    @mitra_RuleDeclaration31.setter
    def mitra_RuleDeclaration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration31", None)
        self.__mitra_RuleDeclaration31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Block"):
                opp_val = getattr(old_value, "mitra_Block", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Block"):
                opp_val = getattr(value, "mitra_Block", None)
                setattr(value, "mitra_Block", self)

    @property
    def mitra_RuleDeclaration21(self):
        return self.__mitra_RuleDeclaration21

    @mitra_RuleDeclaration21.setter
    def mitra_RuleDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration21", None)
        self.__mitra_RuleDeclaration21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_SimpleRuleReference22"):
                opp_val = getattr(old_value, "mitra_SimpleRuleReference22", None)
                if opp_val == self:
                    setattr(old_value, "mitra_SimpleRuleReference22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_SimpleRuleReference22"):
                opp_val = getattr(value, "mitra_SimpleRuleReference22", None)
                setattr(value, "mitra_SimpleRuleReference22", self)

    @property
    def mitra_RuleDeclaration27(self):
        return self.__mitra_RuleDeclaration27

    @mitra_RuleDeclaration27.setter
    def mitra_RuleDeclaration27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration27", None)
        self.__mitra_RuleDeclaration27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Trigger"):
                opp_val = getattr(old_value, "mitra_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "mitra_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Trigger"):
                opp_val = getattr(value, "mitra_Trigger", None)
                setattr(value, "mitra_Trigger", self)

    @property
    def mitra_RuleDeclaration15(self):
        return self.__mitra_RuleDeclaration15

    @mitra_RuleDeclaration15.setter
    def mitra_RuleDeclaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration15", None)
        self.__mitra_RuleDeclaration15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_FormalParameter"):
                    opp_val = getattr(item, "mitra_FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_FormalParameter"):
                    opp_val = getattr(item, "mitra_FormalParameter", None)
                    
                    setattr(item, "mitra_FormalParameter", self)
                    

    @property
    def mitra_RuleDeclaration33(self):
        return self.__mitra_RuleDeclaration33

    @mitra_RuleDeclaration33.setter
    def mitra_RuleDeclaration33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration33", None)
        self.__mitra_RuleDeclaration33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleReference"):
                opp_val = getattr(old_value, "mitra_RuleReference", None)
                if opp_val == self:
                    setattr(old_value, "mitra_RuleReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleReference"):
                opp_val = getattr(value, "mitra_RuleReference", None)
                setattr(value, "mitra_RuleReference", self)

    @property
    def mitra_RuleDeclaration29(self):
        return self.__mitra_RuleDeclaration29

    @mitra_RuleDeclaration29.setter
    def mitra_RuleDeclaration29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration29", None)
        self.__mitra_RuleDeclaration29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_JavaSpec"):
                opp_val = getattr(old_value, "mitra_JavaSpec", None)
                if opp_val == self:
                    setattr(old_value, "mitra_JavaSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_JavaSpec"):
                opp_val = getattr(value, "mitra_JavaSpec", None)
                setattr(value, "mitra_JavaSpec", self)

    @property
    def mitra_RuleDeclaration17(self):
        return self.__mitra_RuleDeclaration17

    @mitra_RuleDeclaration17.setter
    def mitra_RuleDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration17", None)
        self.__mitra_RuleDeclaration17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_ReturnParameter"):
                    opp_val = getattr(item, "mitra_ReturnParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_ReturnParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_ReturnParameter"):
                    opp_val = getattr(item, "mitra_ReturnParameter", None)
                    
                    setattr(item, "mitra_ReturnParameter", self)
                    

    @property
    def mitra_RuleDeclaration19(self):
        return self.__mitra_RuleDeclaration19

    @mitra_RuleDeclaration19.setter
    def mitra_RuleDeclaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration19", None)
        self.__mitra_RuleDeclaration19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_SimpleRuleReference"):
                    opp_val = getattr(item, "mitra_SimpleRuleReference", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_SimpleRuleReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_SimpleRuleReference"):
                    opp_val = getattr(item, "mitra_SimpleRuleReference", None)
                    
                    setattr(item, "mitra_SimpleRuleReference", self)
                    

    @property
    def mitra_RuleDeclaration(self):
        return self.__mitra_RuleDeclaration

    @mitra_RuleDeclaration.setter
    def mitra_RuleDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration", None)
        self.__mitra_RuleDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Module6"):
                opp_val = getattr(old_value, "mitra_Module6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Module6"):
                opp_val = getattr(value, "mitra_Module6", None)
                if opp_val is None:
                    setattr(value, "mitra_Module6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mitra_RuleDeclaration144(self):
        return self.__mitra_RuleDeclaration144

    @mitra_RuleDeclaration144.setter
    def mitra_RuleDeclaration144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration144", None)
        self.__mitra_RuleDeclaration144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_RuleInvocation"):
                opp_val = getattr(old_value, "mitra_RuleInvocation", None)
                if opp_val == self:
                    setattr(old_value, "mitra_RuleInvocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_RuleInvocation"):
                opp_val = getattr(value, "mitra_RuleInvocation", None)
                setattr(value, "mitra_RuleInvocation", self)

    @property
    def mitra_RuleDeclaration24(self):
        return self.__mitra_RuleDeclaration24

    @mitra_RuleDeclaration24.setter
    def mitra_RuleDeclaration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration24", None)
        self.__mitra_RuleDeclaration24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_SimpleRuleReference25"):
                    opp_val = getattr(item, "mitra_SimpleRuleReference25", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_SimpleRuleReference25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_SimpleRuleReference25"):
                    opp_val = getattr(item, "mitra_SimpleRuleReference25", None)
                    
                    setattr(item, "mitra_SimpleRuleReference25", self)
                    

    @property
    def mitra_RuleDeclaration13(self):
        return self.__mitra_RuleDeclaration13

    @mitra_RuleDeclaration13.setter
    def mitra_RuleDeclaration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_RuleDeclaration__mitra_RuleDeclaration13", None)
        self.__mitra_RuleDeclaration13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_Annotation"):
                    opp_val = getattr(item, "mitra_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_Annotation"):
                    opp_val = getattr(item, "mitra_Annotation", None)
                    
                    setattr(item, "mitra_Annotation", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_AnnotationsDefinition:

    pass
class mitra_MetamodelDeclaration:

    def __init__(self, type: str, name: str, replaces: str, mitra_MetamodelDeclaration: "mitra_Module" = None, mitra_MetamodelDeclaration11: set["mitra_Property"] = None, mitra_MetamodelDeclaration64: "mitra_ReferenceType" = None):
        self.type = type
        self.name = name
        self.replaces = replaces
        self.mitra_MetamodelDeclaration = mitra_MetamodelDeclaration
        self.mitra_MetamodelDeclaration11 = mitra_MetamodelDeclaration11 if mitra_MetamodelDeclaration11 is not None else set()
        self.mitra_MetamodelDeclaration64 = mitra_MetamodelDeclaration64
        
    @property
    def replaces(self) -> str:
        return self.__replaces

    @replaces.setter
    def replaces(self, replaces: str):
        self.__replaces = replaces

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mitra_MetamodelDeclaration11(self):
        return self.__mitra_MetamodelDeclaration11

    @mitra_MetamodelDeclaration11.setter
    def mitra_MetamodelDeclaration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_MetamodelDeclaration__mitra_MetamodelDeclaration11", None)
        self.__mitra_MetamodelDeclaration11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_Property"):
                    opp_val = getattr(item, "mitra_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_Property"):
                    opp_val = getattr(item, "mitra_Property", None)
                    
                    setattr(item, "mitra_Property", self)
                    

    @property
    def mitra_MetamodelDeclaration64(self):
        return self.__mitra_MetamodelDeclaration64

    @mitra_MetamodelDeclaration64.setter
    def mitra_MetamodelDeclaration64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_MetamodelDeclaration__mitra_MetamodelDeclaration64", None)
        self.__mitra_MetamodelDeclaration64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_ReferenceType"):
                opp_val = getattr(old_value, "mitra_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "mitra_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_ReferenceType"):
                opp_val = getattr(value, "mitra_ReferenceType", None)
                setattr(value, "mitra_ReferenceType", self)

    @property
    def mitra_MetamodelDeclaration(self):
        return self.__mitra_MetamodelDeclaration

    @mitra_MetamodelDeclaration.setter
    def mitra_MetamodelDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_MetamodelDeclaration__mitra_MetamodelDeclaration", None)
        self.__mitra_MetamodelDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_Module2"):
                opp_val = getattr(old_value, "mitra_Module2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_Module2"):
                opp_val = getattr(value, "mitra_Module2", None)
                if opp_val is None:
                    setattr(value, "mitra_Module2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_Module:

    def __init__(self, packageName: str, name: str, mitra_Module: set["mitra_ModuleReference"] = None, mitra_Module2: set["mitra_MetamodelDeclaration"] = None, mitra_Module4: set["mitra_AnnotationsDefinition"] = None, mitra_Module6: set["mitra_RuleDeclaration"] = None, mitra_Module9: "mitra_ModuleReference" = None):
        self.packageName = packageName
        self.name = name
        self.mitra_Module = mitra_Module if mitra_Module is not None else set()
        self.mitra_Module2 = mitra_Module2 if mitra_Module2 is not None else set()
        self.mitra_Module4 = mitra_Module4 if mitra_Module4 is not None else set()
        self.mitra_Module6 = mitra_Module6 if mitra_Module6 is not None else set()
        self.mitra_Module9 = mitra_Module9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def mitra_Module9(self):
        return self.__mitra_Module9

    @mitra_Module9.setter
    def mitra_Module9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Module__mitra_Module9", None)
        self.__mitra_Module9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mitra_ModuleReference8"):
                opp_val = getattr(old_value, "mitra_ModuleReference8", None)
                if opp_val == self:
                    setattr(old_value, "mitra_ModuleReference8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mitra_ModuleReference8"):
                opp_val = getattr(value, "mitra_ModuleReference8", None)
                setattr(value, "mitra_ModuleReference8", self)

    @property
    def mitra_Module6(self):
        return self.__mitra_Module6

    @mitra_Module6.setter
    def mitra_Module6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Module__mitra_Module6", None)
        self.__mitra_Module6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_RuleDeclaration"):
                    opp_val = getattr(item, "mitra_RuleDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_RuleDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_RuleDeclaration"):
                    opp_val = getattr(item, "mitra_RuleDeclaration", None)
                    
                    setattr(item, "mitra_RuleDeclaration", self)
                    

    @property
    def mitra_Module2(self):
        return self.__mitra_Module2

    @mitra_Module2.setter
    def mitra_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Module__mitra_Module2", None)
        self.__mitra_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_MetamodelDeclaration"):
                    opp_val = getattr(item, "mitra_MetamodelDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_MetamodelDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_MetamodelDeclaration"):
                    opp_val = getattr(item, "mitra_MetamodelDeclaration", None)
                    
                    setattr(item, "mitra_MetamodelDeclaration", self)
                    

    @property
    def mitra_Module4(self):
        return self.__mitra_Module4

    @mitra_Module4.setter
    def mitra_Module4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Module__mitra_Module4", None)
        self.__mitra_Module4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_AnnotationsDefinition"):
                    opp_val = getattr(item, "mitra_AnnotationsDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_AnnotationsDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_AnnotationsDefinition"):
                    opp_val = getattr(item, "mitra_AnnotationsDefinition", None)
                    
                    setattr(item, "mitra_AnnotationsDefinition", self)
                    

    @property
    def mitra_Module(self):
        return self.__mitra_Module

    @mitra_Module.setter
    def mitra_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mitra_Module__mitra_Module", None)
        self.__mitra_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mitra_ModuleReference"):
                    opp_val = getattr(item, "mitra_ModuleReference", None)
                    
                    if opp_val == self:
                        setattr(item, "mitra_ModuleReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mitra_ModuleReference"):
                    opp_val = getattr(item, "mitra_ModuleReference", None)
                    
                    setattr(item, "mitra_ModuleReference", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class mitra_ModuleReference:

    pass