from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Exp:

    pass
class deviceModelingLanguage_PrimaryExp(Exp):

    pass
class deviceModelingLanguage_UnaryExp(Exp):

    def __init__(self, op: str, deviceModelingLanguage_UnaryExp: "deviceModelingLanguage_Exp" = None):
        self.op = op
        self.deviceModelingLanguage_UnaryExp = deviceModelingLanguage_UnaryExp
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op


    @property
    def deviceModelingLanguage_UnaryExp(self):
        return self.__deviceModelingLanguage_UnaryExp

    @deviceModelingLanguage_UnaryExp.setter
    def deviceModelingLanguage_UnaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_UnaryExp__deviceModelingLanguage_UnaryExp", None)
        self.__deviceModelingLanguage_UnaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Exp102"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Exp102", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Exp102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Exp102"):
                opp_val = getattr(value, "deviceModelingLanguage_Exp102", None)
                setattr(value, "deviceModelingLanguage_Exp102", self)

class deviceModelingLanguage_BinaryExp(Exp):

    def __init__(self, op: str, deviceModelingLanguage_BinaryExp: "deviceModelingLanguage_Exp" = None, deviceModelingLanguage_BinaryExp99: "deviceModelingLanguage_Exp" = None):
        self.op = op
        self.deviceModelingLanguage_BinaryExp = deviceModelingLanguage_BinaryExp
        self.deviceModelingLanguage_BinaryExp99 = deviceModelingLanguage_BinaryExp99
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op


    @property
    def deviceModelingLanguage_BinaryExp(self):
        return self.__deviceModelingLanguage_BinaryExp

    @deviceModelingLanguage_BinaryExp.setter
    def deviceModelingLanguage_BinaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_BinaryExp__deviceModelingLanguage_BinaryExp", None)
        self.__deviceModelingLanguage_BinaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Exp97"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Exp97", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Exp97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Exp97"):
                opp_val = getattr(value, "deviceModelingLanguage_Exp97", None)
                setattr(value, "deviceModelingLanguage_Exp97", self)

    @property
    def deviceModelingLanguage_BinaryExp99(self):
        return self.__deviceModelingLanguage_BinaryExp99

    @deviceModelingLanguage_BinaryExp99.setter
    def deviceModelingLanguage_BinaryExp99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_BinaryExp__deviceModelingLanguage_BinaryExp99", None)
        self.__deviceModelingLanguage_BinaryExp99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Exp100"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Exp100", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Exp100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Exp100"):
                opp_val = getattr(value, "deviceModelingLanguage_Exp100", None)
                setattr(value, "deviceModelingLanguage_Exp100", self)

class OptionLiteral:

    pass
class deviceModelingLanguage_SomeLiteral(OptionLiteral):

    pass
class deviceModelingLanguage_NoneLiteral(OptionLiteral):

    pass
class BaseType:

    pass
class deviceModelingLanguage_OptionType(BaseType):

    pass
class deviceModelingLanguage_SomeType(BaseType):

    pass
class deviceModelingLanguage_NoneType(BaseType):

    pass
class deviceModelingLanguage_TupleType(BaseType):

    pass
class Primary:

    pass
class deviceModelingLanguage_LiteralExp(Primary):

    pass
class deviceModelingLanguage_NameExp(Primary):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class deviceModelingLanguage_AccessExp(Exp):

    pass
class Modifier:

    pass
class MModifier:

    pass
class deviceModelingLanguage_Const(Modifier, MModifier):

    def __init__(self, schema: bool, class_: bool, product: bool, instance: bool):
        self.schema = schema
        self.class_ = class_
        self.product = product
        self.instance = instance
        
        pass
    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: bool):
        self.__schema = schema


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: bool):
        self.__class_ = class_


    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, instance: bool):
        self.__instance = instance


    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product: bool):
        self.__product = product


class ConstraintNat:

    pass
class deviceModelingLanguage_AnyNatConstraint(ConstraintNat):

    pass
class deviceModelingLanguage_NumNatConstraint(ConstraintNat):

    def __init__(self, num: str):
        self.num = num
        
        pass
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num: str):
        self.__num = num


class deviceModelingLanguage_Override(Modifier, MModifier):

    pass
class SimpleOptionLiteral:

    pass
class deviceModelingLanguage_SimpleSomeLiteral(SimpleOptionLiteral):

    pass
class deviceModelingLanguage_SimpleNoneLiteral(SimpleOptionLiteral):

    pass
class deviceModelingLanguage_Decl:

    def __init__(self, name: str, deviceModelingLanguage_Decl: "deviceModelingLanguage_Model" = None):
        self.name = name
        self.deviceModelingLanguage_Decl = deviceModelingLanguage_Decl
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def deviceModelingLanguage_Decl(self):
        return self.__deviceModelingLanguage_Decl

    @deviceModelingLanguage_Decl.setter
    def deviceModelingLanguage_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_Decl__deviceModelingLanguage_Decl", None)
        self.__deviceModelingLanguage_Decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Model"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Model"):
                opp_val = getattr(value, "deviceModelingLanguage_Model", None)
                if opp_val is None:
                    setattr(value, "deviceModelingLanguage_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class deviceModelingLanguage_Var(Modifier, MModifier):

    pass
class deviceModelingLanguage_Val(Modifier, MModifier):

    pass
class Type:

    pass
class deviceModelingLanguage_SeqType(Type):

    pass
class deviceModelingLanguage_SetType(Type):

    pass
class deviceModelingLanguage_BaseType(Type):

    pass
class deviceModelingLanguage_Primary:

    pass
class deviceModelingLanguage_Accessor:

    pass
class SimpleLiteral:

    pass
class deviceModelingLanguage_SimpleSeqLiteral(SimpleLiteral):

    pass
class deviceModelingLanguage_SimpleSetLiteral(SimpleLiteral):

    pass
class deviceModelingLanguage_SimpleTupleLiteral(SimpleLiteral):

    pass
class deviceModelingLanguage_SimpleOptionLiteral(SimpleLiteral):

    pass
class deviceModelingLanguage_SimpleBasicLiteral(SimpleLiteral):

    def __init__(self, lit: str):
        self.lit = lit
        
        pass
    @property
    def lit(self):
        return self.__lit

    @lit.setter
    def lit(self, lit: str):
        self.__lit = lit


class deviceModelingLanguage_SimpleLiteral:

    pass
class Literal:

    pass
class deviceModelingLanguage_OptionLiteral(Literal):

    pass
class deviceModelingLanguage_TupleLiteral(Literal):

    pass
class deviceModelingLanguage_BasicLiteral(Literal):

    def __init__(self, lit: str, deviceModelingLanguage_BasicLiteral: "deviceModelingLanguage_TypeDecl" = None, deviceModelingLanguage_BasicLiteral110: "deviceModelingLanguage_LiteralExp" = None):
        self.lit = lit
        self.deviceModelingLanguage_BasicLiteral = deviceModelingLanguage_BasicLiteral
        self.deviceModelingLanguage_BasicLiteral110 = deviceModelingLanguage_BasicLiteral110
        
        pass
    @property
    def lit(self):
        return self.__lit

    @lit.setter
    def lit(self, lit: str):
        self.__lit = lit


    @property
    def deviceModelingLanguage_BasicLiteral110(self):
        return self.__deviceModelingLanguage_BasicLiteral110

    @deviceModelingLanguage_BasicLiteral110.setter
    def deviceModelingLanguage_BasicLiteral110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_BasicLiteral__deviceModelingLanguage_BasicLiteral110", None)
        self.__deviceModelingLanguage_BasicLiteral110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_LiteralExp"):
                opp_val = getattr(old_value, "deviceModelingLanguage_LiteralExp", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_LiteralExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_LiteralExp"):
                opp_val = getattr(value, "deviceModelingLanguage_LiteralExp", None)
                setattr(value, "deviceModelingLanguage_LiteralExp", self)

    @property
    def deviceModelingLanguage_BasicLiteral(self):
        return self.__deviceModelingLanguage_BasicLiteral

    @deviceModelingLanguage_BasicLiteral.setter
    def deviceModelingLanguage_BasicLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_BasicLiteral__deviceModelingLanguage_BasicLiteral", None)
        self.__deviceModelingLanguage_BasicLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_TypeDecl56"):
                opp_val = getattr(old_value, "deviceModelingLanguage_TypeDecl56", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_TypeDecl56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_TypeDecl56"):
                opp_val = getattr(value, "deviceModelingLanguage_TypeDecl56", None)
                setattr(value, "deviceModelingLanguage_TypeDecl56", self)

class deviceModelingLanguage_SeqLiteral(Literal):

    pass
class deviceModelingLanguage_SetLiteral(Literal):

    pass
class deviceModelingLanguage_Report:

    def __init__(self, name: str, deviceModelingLanguage_Report: set["deviceModelingLanguage_Exp"] = None):
        self.name = name
        self.deviceModelingLanguage_Report = deviceModelingLanguage_Report if deviceModelingLanguage_Report is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def deviceModelingLanguage_Report(self):
        return self.__deviceModelingLanguage_Report

    @deviceModelingLanguage_Report.setter
    def deviceModelingLanguage_Report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_Report__deviceModelingLanguage_Report", None)
        self.__deviceModelingLanguage_Report = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deviceModelingLanguage_Exp25"):
                    opp_val = getattr(item, "deviceModelingLanguage_Exp25", None)
                    
                    if opp_val == self:
                        setattr(item, "deviceModelingLanguage_Exp25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deviceModelingLanguage_Exp25"):
                    opp_val = getattr(item, "deviceModelingLanguage_Exp25", None)
                    
                    setattr(item, "deviceModelingLanguage_Exp25", self)
                    

class deviceModelingLanguage_FeatureType:

    pass
class deviceModelingLanguage_MModifier:

    pass
class deviceModelingLanguage_ReportMemberDecl:

    def __init__(self, name: str, deviceModelingLanguage_ReportMemberDecl: set["deviceModelingLanguage_Accessor"] = None):
        self.name = name
        self.deviceModelingLanguage_ReportMemberDecl = deviceModelingLanguage_ReportMemberDecl if deviceModelingLanguage_ReportMemberDecl is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def deviceModelingLanguage_ReportMemberDecl(self):
        return self.__deviceModelingLanguage_ReportMemberDecl

    @deviceModelingLanguage_ReportMemberDecl.setter
    def deviceModelingLanguage_ReportMemberDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_ReportMemberDecl__deviceModelingLanguage_ReportMemberDecl", None)
        self.__deviceModelingLanguage_ReportMemberDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deviceModelingLanguage_Accessor"):
                    opp_val = getattr(item, "deviceModelingLanguage_Accessor", None)
                    
                    if opp_val == self:
                        setattr(item, "deviceModelingLanguage_Accessor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deviceModelingLanguage_Accessor"):
                    opp_val = getattr(item, "deviceModelingLanguage_Accessor", None)
                    
                    setattr(item, "deviceModelingLanguage_Accessor", self)
                    

class deviceModelingLanguage_Param:

    def __init__(self, name: str, deviceModelingLanguage_Param: "deviceModelingLanguage_BaseFeatureType" = None):
        self.name = name
        self.deviceModelingLanguage_Param = deviceModelingLanguage_Param
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def deviceModelingLanguage_Param(self):
        return self.__deviceModelingLanguage_Param

    @deviceModelingLanguage_Param.setter
    def deviceModelingLanguage_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_Param__deviceModelingLanguage_Param", None)
        self.__deviceModelingLanguage_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_BaseFeatureType51"):
                opp_val = getattr(old_value, "deviceModelingLanguage_BaseFeatureType51", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_BaseFeatureType51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_BaseFeatureType51"):
                opp_val = getattr(value, "deviceModelingLanguage_BaseFeatureType51", None)
                setattr(value, "deviceModelingLanguage_BaseFeatureType51", self)

class deviceModelingLanguage_ConstraintExp:

    pass
class FeatureDecl:

    pass
class deviceModelingLanguage_Feature(FeatureDecl):

    def __init__(self, schema: bool, class_: bool, product: bool):
        self.schema = schema
        self.class_ = class_
        self.product = product
        
        pass
    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: bool):
        self.__class_ = class_


    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: bool):
        self.__schema = schema


    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product: bool):
        self.__product = product


class deviceModelingLanguage_App(FeatureDecl):

    pass
class deviceModelingLanguage_Data(FeatureDecl, MModifier):

    pass
class deviceModelingLanguage_SubMemberMatch:

    def __init__(self, qNames: str, name: str, any: str, deviceModelingLanguage_SubMemberMatch: "deviceModelingLanguage_MultiplicityInvariant" = None):
        self.qNames = qNames
        self.name = name
        self.any = any
        self.deviceModelingLanguage_SubMemberMatch = deviceModelingLanguage_SubMemberMatch
        
        pass
    @property
    def any(self):
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def qNames(self):
        return self.__qNames

    @qNames.setter
    def qNames(self, qNames: str):
        self.__qNames = qNames


    @property
    def deviceModelingLanguage_SubMemberMatch(self):
        return self.__deviceModelingLanguage_SubMemberMatch

    @deviceModelingLanguage_SubMemberMatch.setter
    def deviceModelingLanguage_SubMemberMatch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_SubMemberMatch__deviceModelingLanguage_SubMemberMatch", None)
        self.__deviceModelingLanguage_SubMemberMatch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_MultiplicityInvariant36"):
                opp_val = getattr(old_value, "deviceModelingLanguage_MultiplicityInvariant36", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_MultiplicityInvariant36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_MultiplicityInvariant36"):
                opp_val = getattr(value, "deviceModelingLanguage_MultiplicityInvariant36", None)
                setattr(value, "deviceModelingLanguage_MultiplicityInvariant36", self)

class deviceModelingLanguage_ConstraintNat:

    pass
class InvariantDecl:

    pass
class deviceModelingLanguage_GeneralInvariant(InvariantDecl):

    pass
class deviceModelingLanguage_MultiplicityInvariant(InvariantDecl):

    pass
class FeatureType:

    pass
class deviceModelingLanguage_EitherFeatureType(FeatureType):

    def __init__(self, choice: str, deviceModelingLanguage_EitherFeatureType: set["deviceModelingLanguage_BaseFeatureType"] = None, deviceModelingLanguage_EitherFeatureType84: set["deviceModelingLanguage_MemberDecl"] = None):
        self.choice = choice
        self.deviceModelingLanguage_EitherFeatureType = deviceModelingLanguage_EitherFeatureType if deviceModelingLanguage_EitherFeatureType is not None else set()
        self.deviceModelingLanguage_EitherFeatureType84 = deviceModelingLanguage_EitherFeatureType84 if deviceModelingLanguage_EitherFeatureType84 is not None else set()
        
        pass
    @property
    def choice(self):
        return self.__choice

    @choice.setter
    def choice(self, choice: str):
        self.__choice = choice


    @property
    def deviceModelingLanguage_EitherFeatureType84(self):
        return self.__deviceModelingLanguage_EitherFeatureType84

    @deviceModelingLanguage_EitherFeatureType84.setter
    def deviceModelingLanguage_EitherFeatureType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_EitherFeatureType__deviceModelingLanguage_EitherFeatureType84", None)
        self.__deviceModelingLanguage_EitherFeatureType84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deviceModelingLanguage_MemberDecl85"):
                    opp_val = getattr(item, "deviceModelingLanguage_MemberDecl85", None)
                    
                    if opp_val == self:
                        setattr(item, "deviceModelingLanguage_MemberDecl85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deviceModelingLanguage_MemberDecl85"):
                    opp_val = getattr(item, "deviceModelingLanguage_MemberDecl85", None)
                    
                    setattr(item, "deviceModelingLanguage_MemberDecl85", self)
                    

    @property
    def deviceModelingLanguage_EitherFeatureType(self):
        return self.__deviceModelingLanguage_EitherFeatureType

    @deviceModelingLanguage_EitherFeatureType.setter
    def deviceModelingLanguage_EitherFeatureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_EitherFeatureType__deviceModelingLanguage_EitherFeatureType", None)
        self.__deviceModelingLanguage_EitherFeatureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deviceModelingLanguage_BaseFeatureType82"):
                    opp_val = getattr(item, "deviceModelingLanguage_BaseFeatureType82", None)
                    
                    if opp_val == self:
                        setattr(item, "deviceModelingLanguage_BaseFeatureType82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deviceModelingLanguage_BaseFeatureType82"):
                    opp_val = getattr(item, "deviceModelingLanguage_BaseFeatureType82", None)
                    
                    setattr(item, "deviceModelingLanguage_BaseFeatureType82", self)
                    

class deviceModelingLanguage_OptionFeatureType(FeatureType):

    def __init__(self, none: bool, deviceModelingLanguage_OptionFeatureType: "deviceModelingLanguage_BaseFeatureType" = None):
        self.none = none
        self.deviceModelingLanguage_OptionFeatureType = deviceModelingLanguage_OptionFeatureType
        
        pass
    @property
    def none(self):
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none


    @property
    def deviceModelingLanguage_OptionFeatureType(self):
        return self.__deviceModelingLanguage_OptionFeatureType

    @deviceModelingLanguage_OptionFeatureType.setter
    def deviceModelingLanguage_OptionFeatureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_OptionFeatureType__deviceModelingLanguage_OptionFeatureType", None)
        self.__deviceModelingLanguage_OptionFeatureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_BaseFeatureType75"):
                opp_val = getattr(old_value, "deviceModelingLanguage_BaseFeatureType75", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_BaseFeatureType75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_BaseFeatureType75"):
                opp_val = getattr(value, "deviceModelingLanguage_BaseFeatureType75", None)
                setattr(value, "deviceModelingLanguage_BaseFeatureType75", self)

class deviceModelingLanguage_SetFeatureType(FeatureType):

    pass
class deviceModelingLanguage_SeqFeatureType(FeatureType):

    pass
class deviceModelingLanguage_SomeFeatureType(FeatureType):

    pass
class deviceModelingLanguage_BaseFeatureType(FeatureType):

    pass
class deviceModelingLanguage_Model:

    def __init__(self, class_: bool, product: bool, schema: bool, deviceModelingLanguage_Model: set["deviceModelingLanguage_Decl"] = None):
        self.class_ = class_
        self.product = product
        self.schema = schema
        self.deviceModelingLanguage_Model = deviceModelingLanguage_Model if deviceModelingLanguage_Model is not None else set()
        
        pass
    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: bool):
        self.__class_ = class_


    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: bool):
        self.__schema = schema


    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product: bool):
        self.__product = product


    @property
    def deviceModelingLanguage_Model(self):
        return self.__deviceModelingLanguage_Model

    @deviceModelingLanguage_Model.setter
    def deviceModelingLanguage_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_Model__deviceModelingLanguage_Model", None)
        self.__deviceModelingLanguage_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deviceModelingLanguage_Decl"):
                    opp_val = getattr(item, "deviceModelingLanguage_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "deviceModelingLanguage_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deviceModelingLanguage_Decl"):
                    opp_val = getattr(item, "deviceModelingLanguage_Decl", None)
                    
                    setattr(item, "deviceModelingLanguage_Decl", self)
                    

class deviceModelingLanguage_Literal:

    pass
class deviceModelingLanguage_Type:

    pass
class deviceModelingLanguage_Modifier:

    pass
class Accessor:

    pass
class MemberDecl:

    pass
class deviceModelingLanguage_InvariantDecl(MemberDecl):

    def __init__(self, invName: str):
        self.invName = invName
        
        pass
    @property
    def invName(self):
        return self.__invName

    @invName.setter
    def invName(self, invName: str):
        self.__invName = invName


class deviceModelingLanguage_SubMemberDecl(Accessor, MemberDecl):

    def __init__(self, name: str, deviceModelingLanguage_SubMemberDecl: "deviceModelingLanguage_MModifier" = None, deviceModelingLanguage_SubMemberDecl20: "deviceModelingLanguage_FeatureType" = None):
        self.name = name
        self.deviceModelingLanguage_SubMemberDecl = deviceModelingLanguage_SubMemberDecl
        self.deviceModelingLanguage_SubMemberDecl20 = deviceModelingLanguage_SubMemberDecl20
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def deviceModelingLanguage_SubMemberDecl(self):
        return self.__deviceModelingLanguage_SubMemberDecl

    @deviceModelingLanguage_SubMemberDecl.setter
    def deviceModelingLanguage_SubMemberDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_SubMemberDecl__deviceModelingLanguage_SubMemberDecl", None)
        self.__deviceModelingLanguage_SubMemberDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_MModifier"):
                opp_val = getattr(old_value, "deviceModelingLanguage_MModifier", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_MModifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_MModifier"):
                opp_val = getattr(value, "deviceModelingLanguage_MModifier", None)
                setattr(value, "deviceModelingLanguage_MModifier", self)

    @property
    def deviceModelingLanguage_SubMemberDecl20(self):
        return self.__deviceModelingLanguage_SubMemberDecl20

    @deviceModelingLanguage_SubMemberDecl20.setter
    def deviceModelingLanguage_SubMemberDecl20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_SubMemberDecl__deviceModelingLanguage_SubMemberDecl20", None)
        self.__deviceModelingLanguage_SubMemberDecl20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_FeatureType"):
                opp_val = getattr(old_value, "deviceModelingLanguage_FeatureType", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_FeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_FeatureType"):
                opp_val = getattr(value, "deviceModelingLanguage_FeatureType", None)
                setattr(value, "deviceModelingLanguage_FeatureType", self)

class deviceModelingLanguage_AttrDecl(Accessor, MemberDecl):

    def __init__(self, attributeName: str, deviceModelingLanguage_AttrDecl15: "deviceModelingLanguage_Type" = None, deviceModelingLanguage_AttrDecl17: "deviceModelingLanguage_Literal" = None, deviceModelingLanguage_AttrDecl: "deviceModelingLanguage_Modifier" = None):
        self.attributeName = attributeName
        self.deviceModelingLanguage_AttrDecl15 = deviceModelingLanguage_AttrDecl15
        self.deviceModelingLanguage_AttrDecl17 = deviceModelingLanguage_AttrDecl17
        self.deviceModelingLanguage_AttrDecl = deviceModelingLanguage_AttrDecl
        
        pass
    @property
    def attributeName(self):
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName


    @property
    def deviceModelingLanguage_AttrDecl15(self):
        return self.__deviceModelingLanguage_AttrDecl15

    @deviceModelingLanguage_AttrDecl15.setter
    def deviceModelingLanguage_AttrDecl15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_AttrDecl__deviceModelingLanguage_AttrDecl15", None)
        self.__deviceModelingLanguage_AttrDecl15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Type"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Type", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Type"):
                opp_val = getattr(value, "deviceModelingLanguage_Type", None)
                setattr(value, "deviceModelingLanguage_Type", self)

    @property
    def deviceModelingLanguage_AttrDecl17(self):
        return self.__deviceModelingLanguage_AttrDecl17

    @deviceModelingLanguage_AttrDecl17.setter
    def deviceModelingLanguage_AttrDecl17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_AttrDecl__deviceModelingLanguage_AttrDecl17", None)
        self.__deviceModelingLanguage_AttrDecl17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Literal"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Literal", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Literal"):
                opp_val = getattr(value, "deviceModelingLanguage_Literal", None)
                setattr(value, "deviceModelingLanguage_Literal", self)

    @property
    def deviceModelingLanguage_AttrDecl(self):
        return self.__deviceModelingLanguage_AttrDecl

    @deviceModelingLanguage_AttrDecl.setter
    def deviceModelingLanguage_AttrDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_AttrDecl__deviceModelingLanguage_AttrDecl", None)
        self.__deviceModelingLanguage_AttrDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Modifier"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Modifier", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Modifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Modifier"):
                opp_val = getattr(value, "deviceModelingLanguage_Modifier", None)
                setattr(value, "deviceModelingLanguage_Modifier", self)

class deviceModelingLanguage_Exp:

    pass
class deviceModelingLanguage_Assignment:

    def __init__(self, name: str, deviceModelingLanguage_Assignment: "deviceModelingLanguage_FeatureDecl" = None, deviceModelingLanguage_Assignment22: "deviceModelingLanguage_Exp" = None):
        self.name = name
        self.deviceModelingLanguage_Assignment = deviceModelingLanguage_Assignment
        self.deviceModelingLanguage_Assignment22 = deviceModelingLanguage_Assignment22
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def deviceModelingLanguage_Assignment(self):
        return self.__deviceModelingLanguage_Assignment

    @deviceModelingLanguage_Assignment.setter
    def deviceModelingLanguage_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_Assignment__deviceModelingLanguage_Assignment", None)
        self.__deviceModelingLanguage_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_FeatureDecl10"):
                opp_val = getattr(old_value, "deviceModelingLanguage_FeatureDecl10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_FeatureDecl10"):
                opp_val = getattr(value, "deviceModelingLanguage_FeatureDecl10", None)
                if opp_val is None:
                    setattr(value, "deviceModelingLanguage_FeatureDecl10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deviceModelingLanguage_Assignment22(self):
        return self.__deviceModelingLanguage_Assignment22

    @deviceModelingLanguage_Assignment22.setter
    def deviceModelingLanguage_Assignment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deviceModelingLanguage_Assignment__deviceModelingLanguage_Assignment22", None)
        self.__deviceModelingLanguage_Assignment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deviceModelingLanguage_Exp23"):
                opp_val = getattr(old_value, "deviceModelingLanguage_Exp23", None)
                if opp_val == self:
                    setattr(old_value, "deviceModelingLanguage_Exp23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deviceModelingLanguage_Exp23"):
                opp_val = getattr(value, "deviceModelingLanguage_Exp23", None)
                setattr(value, "deviceModelingLanguage_Exp23", self)

class deviceModelingLanguage_Device(FeatureDecl):

    pass
class deviceModelingLanguage_MemberDecl:

    pass
class Decl:

    pass
class deviceModelingLanguage_FeatureDecl(Decl):

    pass
class deviceModelingLanguage_TypeDecl(Decl):

    pass