from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CallFor:

    pass
class go_varFor(CallFor):

    pass
class go_operationsOne:

    pass
class go_FunctionReturn:

    pass
class go_FunctionBody:

    pass
class go_ElseCondition:

    pass
class go_ElseIfCondition:

    pass
class ElseIfCondition:

    pass
class go_Double:

    def __init__(self, d: int, go_Double: "go_Numbers" = None):
        self.d = d
        self.go_Double = go_Double
        
    @property
    def d(self) -> int:
        return self.__d

    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def go_Double(self):
        return self.__go_Double

    @go_Double.setter
    def go_Double(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Double__go_Double", None)
        self.__go_Double = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Numbers35"):
                opp_val = getattr(old_value, "go_Numbers35", None)
                if opp_val == self:
                    setattr(old_value, "go_Numbers35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Numbers35"):
                opp_val = getattr(value, "go_Numbers35", None)
                setattr(value, "go_Numbers35", self)

class go_Intg:

    def __init__(self, i: int, go_Intg: "go_Numbers" = None):
        self.i = i
        self.go_Intg = go_Intg
        
    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

    @property
    def go_Intg(self):
        return self.__go_Intg

    @go_Intg.setter
    def go_Intg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Intg__go_Intg", None)
        self.__go_Intg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Numbers"):
                opp_val = getattr(old_value, "go_Numbers", None)
                if opp_val == self:
                    setattr(old_value, "go_Numbers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Numbers"):
                opp_val = getattr(value, "go_Numbers", None)
                setattr(value, "go_Numbers", self)

class go_IfCondition(ElseIfCondition):

    pass
class T:

    pass
class go_F(T):

    pass
class go_Y:

    pass
class I:

    pass
class Operations:

    pass
class go_T(Operations, I):

    pass
class go_I:

    pass
class go_DecVars:

    def __init__(self, vars: str, go_DecVars: set["go_Atrib_Aux"] = None):
        self.vars = vars
        self.go_DecVars = go_DecVars if go_DecVars is not None else set()
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def go_DecVars(self):
        return self.__go_DecVars

    @go_DecVars.setter
    def go_DecVars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_DecVars__go_DecVars", None)
        self.__go_DecVars = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_Atrib_Aux27"):
                    opp_val = getattr(item, "go_Atrib_Aux27", None)
                    
                    if opp_val == self:
                        setattr(item, "go_Atrib_Aux27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_Atrib_Aux27"):
                    opp_val = getattr(item, "go_Atrib_Aux27", None)
                    
                    setattr(item, "go_Atrib_Aux27", self)
                    

class F:

    pass
class go_OperationsOneEquals:

    pass
class TypeValue:

    pass
class go_Bool(TypeValue):

    def __init__(self, val: str, go_Bool: "go_Literal" = None):
        self.val = val
        self.go_Bool = go_Bool
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def go_Bool(self):
        return self.__go_Bool

    @go_Bool.setter
    def go_Bool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Bool__go_Bool", None)
        self.__go_Bool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Literal"):
                opp_val = getattr(old_value, "go_Literal", None)
                if opp_val == self:
                    setattr(old_value, "go_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Literal"):
                opp_val = getattr(value, "go_Literal", None)
                setattr(value, "go_Literal", self)

class go_Str(TypeValue):

    def __init__(self, s: str):
        self.s = s
        
    @property
    def s(self) -> str:
        return self.__s

    @s.setter
    def s(self, s: str):
        self.__s = s

class Atri:

    pass
class go_Params:

    def __init__(self, params: str, type: str, go_Params: "go_DecFunc" = None, go_Params77: "go_CallFunc" = None):
        self.params = params
        self.type = type
        self.go_Params = go_Params
        self.go_Params77 = go_Params77
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def go_Params77(self):
        return self.__go_Params77

    @go_Params77.setter
    def go_Params77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Params__go_Params77", None)
        self.__go_Params77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_CallFunc"):
                opp_val = getattr(old_value, "go_CallFunc", None)
                if opp_val == self:
                    setattr(old_value, "go_CallFunc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_CallFunc"):
                opp_val = getattr(value, "go_CallFunc", None)
                setattr(value, "go_CallFunc", self)

    @property
    def go_Params(self):
        return self.__go_Params

    @go_Params.setter
    def go_Params(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Params__go_Params", None)
        self.__go_Params = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_DecFunc"):
                opp_val = getattr(old_value, "go_DecFunc", None)
                if opp_val == self:
                    setattr(old_value, "go_DecFunc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_DecFunc"):
                opp_val = getattr(value, "go_DecFunc", None)
                setattr(value, "go_DecFunc", self)

class varFor:

    pass
class go_Expression(varFor):

    pass
class go_Cases:

    pass
class Expression:

    pass
class go_Addition(Expression):

    pass
class go_AndExpression(Expression):

    pass
class go_Multiplication(Expression):

    pass
class go_Division(Expression):

    pass
class go_ComparisonExpression(Expression):

    pass
class go_Subtration(Expression):

    pass
class go_OrExpression(Expression):

    pass
class go_Numbers(TypeValue, Expression, F):

    pass
class go_Literal(Expression):

    pass
class operationsOne:

    pass
class go_TypeValue(Atri):

    pass
class go_EObject:

    pass
class OperationsOneEquals:

    pass
class go_Decl:

    def __init__(self, name: str, type: str, go_Decl: "go_DecVar" = None):
        self.name = name
        self.type = type
        self.go_Decl = go_Decl
        
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
    def go_Decl(self):
        return self.__go_Decl

    @go_Decl.setter
    def go_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Decl__go_Decl", None)
        self.__go_Decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_DecVar"):
                opp_val = getattr(old_value, "go_DecVar", None)
                if opp_val == self:
                    setattr(old_value, "go_DecVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_DecVar"):
                opp_val = getattr(value, "go_DecVar", None)
                setattr(value, "go_DecVar", self)

class SwitchCase:

    pass
class Atrib_Aux:

    pass
class go_Atri(Atrib_Aux):

    pass
class go_Operations(Atrib_Aux):

    pass
class go_Atrib_Aux:

    pass
class go_ReAtrib(varFor):

    def __init__(self, name: str, go_ReAtrib: "go_DecVar" = None, go_ReAtrib20: "go_Atrib_Aux" = None, go_ReAtrib23: "go_EObject" = None):
        self.name = name
        self.go_ReAtrib = go_ReAtrib
        self.go_ReAtrib20 = go_ReAtrib20
        self.go_ReAtrib23 = go_ReAtrib23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def go_ReAtrib23(self):
        return self.__go_ReAtrib23

    @go_ReAtrib23.setter
    def go_ReAtrib23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ReAtrib__go_ReAtrib23", None)
        self.__go_ReAtrib23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EObject24"):
                opp_val = getattr(old_value, "go_EObject24", None)
                if opp_val == self:
                    setattr(old_value, "go_EObject24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EObject24"):
                opp_val = getattr(value, "go_EObject24", None)
                setattr(value, "go_EObject24", self)

    @property
    def go_ReAtrib(self):
        return self.__go_ReAtrib

    @go_ReAtrib.setter
    def go_ReAtrib(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ReAtrib__go_ReAtrib", None)
        self.__go_ReAtrib = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_DecVar7"):
                opp_val = getattr(old_value, "go_DecVar7", None)
                if opp_val == self:
                    setattr(old_value, "go_DecVar7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_DecVar7"):
                opp_val = getattr(value, "go_DecVar7", None)
                setattr(value, "go_DecVar7", self)

    @property
    def go_ReAtrib20(self):
        return self.__go_ReAtrib20

    @go_ReAtrib20.setter
    def go_ReAtrib20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ReAtrib__go_ReAtrib20", None)
        self.__go_ReAtrib20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Atrib_Aux21"):
                opp_val = getattr(old_value, "go_Atrib_Aux21", None)
                if opp_val == self:
                    setattr(old_value, "go_Atrib_Aux21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Atrib_Aux21"):
                opp_val = getattr(value, "go_Atrib_Aux21", None)
                setattr(value, "go_Atrib_Aux21", self)

class go_AtribVar:

    def __init__(self, vars: str, type: str, go_AtribVar: "go_DecVar" = None, go_AtribVar9: set["go_Atrib_Aux"] = None):
        self.vars = vars
        self.type = type
        self.go_AtribVar = go_AtribVar
        self.go_AtribVar9 = go_AtribVar9 if go_AtribVar9 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def go_AtribVar9(self):
        return self.__go_AtribVar9

    @go_AtribVar9.setter
    def go_AtribVar9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_AtribVar__go_AtribVar9", None)
        self.__go_AtribVar9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_Atrib_Aux"):
                    opp_val = getattr(item, "go_Atrib_Aux", None)
                    
                    if opp_val == self:
                        setattr(item, "go_Atrib_Aux", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_Atrib_Aux"):
                    opp_val = getattr(item, "go_Atrib_Aux", None)
                    
                    setattr(item, "go_Atrib_Aux", self)
                    

    @property
    def go_AtribVar(self):
        return self.__go_AtribVar

    @go_AtribVar.setter
    def go_AtribVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_AtribVar__go_AtribVar", None)
        self.__go_AtribVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_DecVar5"):
                opp_val = getattr(old_value, "go_DecVar5", None)
                if opp_val == self:
                    setattr(old_value, "go_DecVar5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_DecVar5"):
                opp_val = getattr(value, "go_DecVar5", None)
                setattr(value, "go_DecVar5", self)

class go_Atrib(varFor):

    def __init__(self, name: str, type: str, modifier: str, go_Atrib: "go_DecVar" = None, go_Atrib15: "go_Atrib_Aux" = None, go_Atrib18: "go_EObject" = None):
        self.name = name
        self.type = type
        self.modifier = modifier
        self.go_Atrib = go_Atrib
        self.go_Atrib15 = go_Atrib15
        self.go_Atrib18 = go_Atrib18
        
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
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def go_Atrib15(self):
        return self.__go_Atrib15

    @go_Atrib15.setter
    def go_Atrib15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Atrib__go_Atrib15", None)
        self.__go_Atrib15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Atrib_Aux16"):
                opp_val = getattr(old_value, "go_Atrib_Aux16", None)
                if opp_val == self:
                    setattr(old_value, "go_Atrib_Aux16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Atrib_Aux16"):
                opp_val = getattr(value, "go_Atrib_Aux16", None)
                setattr(value, "go_Atrib_Aux16", self)

    @property
    def go_Atrib18(self):
        return self.__go_Atrib18

    @go_Atrib18.setter
    def go_Atrib18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Atrib__go_Atrib18", None)
        self.__go_Atrib18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EObject"):
                opp_val = getattr(old_value, "go_EObject", None)
                if opp_val == self:
                    setattr(old_value, "go_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EObject"):
                opp_val = getattr(value, "go_EObject", None)
                setattr(value, "go_EObject", self)

    @property
    def go_Atrib(self):
        return self.__go_Atrib

    @go_Atrib.setter
    def go_Atrib(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Atrib__go_Atrib", None)
        self.__go_Atrib = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_DecVar3"):
                opp_val = getattr(old_value, "go_DecVar3", None)
                if opp_val == self:
                    setattr(old_value, "go_DecVar3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_DecVar3"):
                opp_val = getattr(value, "go_DecVar3", None)
                setattr(value, "go_DecVar3", self)

class Greeting:

    pass
class go_Condition(Greeting):

    pass
class go_CallFunc(Greeting, Atrib_Aux):

    def __init__(self, nameFunc: str, go_CallFunc: "go_Params" = None):
        self.nameFunc = nameFunc
        self.go_CallFunc = go_CallFunc
        
    @property
    def nameFunc(self) -> str:
        return self.__nameFunc

    @nameFunc.setter
    def nameFunc(self, nameFunc: str):
        self.__nameFunc = nameFunc

    @property
    def go_CallFunc(self):
        return self.__go_CallFunc

    @go_CallFunc.setter
    def go_CallFunc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_CallFunc__go_CallFunc", None)
        self.__go_CallFunc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Params77"):
                opp_val = getattr(old_value, "go_Params77", None)
                if opp_val == self:
                    setattr(old_value, "go_Params77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Params77"):
                opp_val = getattr(value, "go_Params77", None)
                setattr(value, "go_Params77", self)

class go_Variable(OperationsOneEquals, Greeting, operationsOne, SwitchCase, Expression, Atrib_Aux):

    def __init__(self, name: str, go_Variable: "go_Cases" = None, go_Variable12: "go_Greeting" = None):
        self.name = name
        self.go_Variable = go_Variable
        self.go_Variable12 = go_Variable12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def go_Variable(self):
        return self.__go_Variable

    @go_Variable.setter
    def go_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Variable__go_Variable", None)
        self.__go_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Cases"):
                opp_val = getattr(old_value, "go_Cases", None)
                if opp_val == self:
                    setattr(old_value, "go_Cases", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Cases"):
                opp_val = getattr(value, "go_Cases", None)
                setattr(value, "go_Cases", self)

    @property
    def go_Variable12(self):
        return self.__go_Variable12

    @go_Variable12.setter
    def go_Variable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Variable__go_Variable12", None)
        self.__go_Variable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Greeting13"):
                opp_val = getattr(old_value, "go_Greeting13", None)
                if opp_val == self:
                    setattr(old_value, "go_Greeting13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Greeting13"):
                opp_val = getattr(value, "go_Greeting13", None)
                setattr(value, "go_Greeting13", self)

class go_DecFunc(Greeting):

    def __init__(self, name: str, returnType: str, go_DecFunc: "go_Params" = None, go_DecFunc67: "go_FunctionBody" = None):
        self.name = name
        self.returnType = returnType
        self.go_DecFunc = go_DecFunc
        self.go_DecFunc67 = go_DecFunc67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def go_DecFunc67(self):
        return self.__go_DecFunc67

    @go_DecFunc67.setter
    def go_DecFunc67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_DecFunc__go_DecFunc67", None)
        self.__go_DecFunc67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_FunctionBody"):
                opp_val = getattr(old_value, "go_FunctionBody", None)
                if opp_val == self:
                    setattr(old_value, "go_FunctionBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_FunctionBody"):
                opp_val = getattr(value, "go_FunctionBody", None)
                setattr(value, "go_FunctionBody", self)

    @property
    def go_DecFunc(self):
        return self.__go_DecFunc

    @go_DecFunc.setter
    def go_DecFunc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_DecFunc__go_DecFunc", None)
        self.__go_DecFunc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Params"):
                opp_val = getattr(old_value, "go_Params", None)
                if opp_val == self:
                    setattr(old_value, "go_Params", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Params"):
                opp_val = getattr(value, "go_Params", None)
                setattr(value, "go_Params", self)

class go_CallFor(Greeting):

    pass
class go_DataType(Greeting):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class go_MultDecVars(Greeting):

    def __init__(self, name: str, value: str, go_MultDecVars: "go_TypeValue" = None):
        self.name = name
        self.value = value
        self.go_MultDecVars = go_MultDecVars
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def go_MultDecVars(self):
        return self.__go_MultDecVars

    @go_MultDecVars.setter
    def go_MultDecVars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_MultDecVars__go_MultDecVars", None)
        self.__go_MultDecVars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TypeValue"):
                opp_val = getattr(old_value, "go_TypeValue", None)
                if opp_val == self:
                    setattr(old_value, "go_TypeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TypeValue"):
                opp_val = getattr(value, "go_TypeValue", None)
                setattr(value, "go_TypeValue", self)

class go_DecVar(Greeting):

    pass
class go_SwitchCase(Greeting):

    pass
class go_Greeting:

    pass
class go_Go:

    pass