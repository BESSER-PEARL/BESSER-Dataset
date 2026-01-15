from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IntBinaryOperation:

    pass
class gx10_Time(IntBinaryOperation):

    pass
class gx10_Plus(IntBinaryOperation):

    pass
class IntExpression:

    pass
class gx10_IntVarAccess(IntExpression):

    pass
class gx10_IntBinaryOperation(IntExpression):

    def __init__(self, gx10_IntBinaryOperation: "gx10_IntExpression" = None, gx10_IntBinaryOperation39: "gx10_IntExpression" = None):
        self.gx10_IntBinaryOperation = gx10_IntBinaryOperation
        self.gx10_IntBinaryOperation39 = gx10_IntBinaryOperation39
        
    @property
    def gx10_IntBinaryOperation(self):
        return self.__gx10_IntBinaryOperation

    @gx10_IntBinaryOperation.setter
    def gx10_IntBinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntBinaryOperation__gx10_IntBinaryOperation", None)
        self.__gx10_IntBinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression"):
                opp_val = getattr(old_value, "gx10_IntExpression", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression"):
                opp_val = getattr(value, "gx10_IntExpression", None)
                setattr(value, "gx10_IntExpression", self)

    @property
    def gx10_IntBinaryOperation39(self):
        return self.__gx10_IntBinaryOperation39

    @gx10_IntBinaryOperation39.setter
    def gx10_IntBinaryOperation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntBinaryOperation__gx10_IntBinaryOperation39", None)
        self.__gx10_IntBinaryOperation39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression40"):
                opp_val = getattr(old_value, "gx10_IntExpression40", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression40"):
                opp_val = getattr(value, "gx10_IntExpression40", None)
                setattr(value, "gx10_IntExpression40", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_IntConst(IntExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class BoolExpression:

    pass
class gx10_BoolVarAccess(BoolExpression):

    pass
class gx10_False(BoolExpression):

    pass
class gx10_Equal(BoolExpression):

    def __init__(self, gx10_Equal: "gx10_IntExpression" = None, gx10_Equal68: "gx10_IntExpression" = None):
        self.gx10_Equal = gx10_Equal
        self.gx10_Equal68 = gx10_Equal68
        
    @property
    def gx10_Equal68(self):
        return self.__gx10_Equal68

    @gx10_Equal68.setter
    def gx10_Equal68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Equal__gx10_Equal68", None)
        self.__gx10_Equal68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression69"):
                opp_val = getattr(old_value, "gx10_IntExpression69", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression69"):
                opp_val = getattr(value, "gx10_IntExpression69", None)
                setattr(value, "gx10_IntExpression69", self)

    @property
    def gx10_Equal(self):
        return self.__gx10_Equal

    @gx10_Equal.setter
    def gx10_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Equal__gx10_Equal", None)
        self.__gx10_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression66"):
                opp_val = getattr(old_value, "gx10_IntExpression66", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression66"):
                opp_val = getattr(value, "gx10_IntExpression66", None)
                setattr(value, "gx10_IntExpression66", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_And(BoolExpression):

    pass
class gx10_Not(BoolExpression):

    pass
class gx10_True(BoolExpression):

    pass
class gx10_Statement(ABC):

    pass
class Statement:

    pass
class gx10_ControlStructure(Statement):

    pass
class gx10_Expression(Statement):

    pass
class gx10_Finish(Statement):

    pass
class gx10_IntVar(Statement):

    def __init__(self, gx10_IntVar: "gx10_IntExpression" = None, gx10_IntVar59: "gx10_Referentiable" = None):
        self.gx10_IntVar = gx10_IntVar
        self.gx10_IntVar59 = gx10_IntVar59
        
    @property
    def gx10_IntVar(self):
        return self.__gx10_IntVar

    @gx10_IntVar.setter
    def gx10_IntVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntVar__gx10_IntVar", None)
        self.__gx10_IntVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression57"):
                opp_val = getattr(old_value, "gx10_IntExpression57", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression57"):
                opp_val = getattr(value, "gx10_IntExpression57", None)
                setattr(value, "gx10_IntExpression57", self)

    @property
    def gx10_IntVar59(self):
        return self.__gx10_IntVar59

    @gx10_IntVar59.setter
    def gx10_IntVar59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntVar__gx10_IntVar59", None)
        self.__gx10_IntVar59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Referentiable60"):
                opp_val = getattr(old_value, "gx10_Referentiable60", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Referentiable60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Referentiable60"):
                opp_val = getattr(value, "gx10_Referentiable60", None)
                setattr(value, "gx10_Referentiable60", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_Async(Statement):

    pass
class gx10_Print(Statement):

    def __init__(self, gx10_Print: "gx10_Expression" = None):
        self.gx10_Print = gx10_Print
        
    @property
    def gx10_Print(self):
        return self.__gx10_Print

    @gx10_Print.setter
    def gx10_Print(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Print__gx10_Print", None)
        self.__gx10_Print = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Expression"):
                opp_val = getattr(old_value, "gx10_Expression", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Expression"):
                opp_val = getattr(value, "gx10_Expression", None)
                setattr(value, "gx10_Expression", self)

    def print(self):
        # TODO: Implement print method
        pass

class gx10_Referentiable:

    def __init__(self, name: str, gx10_Referentiable: "gx10_Method" = None, gx10_Referentiable64: "gx10_BoolVarAccess" = None, gx10_Referentiable55: "gx10_BoolVar" = None, gx10_Referentiable60: "gx10_IntVar" = None, gx10_Referentiable62: "gx10_IntVarAccess" = None):
        self.name = name
        self.gx10_Referentiable = gx10_Referentiable
        self.gx10_Referentiable64 = gx10_Referentiable64
        self.gx10_Referentiable55 = gx10_Referentiable55
        self.gx10_Referentiable60 = gx10_Referentiable60
        self.gx10_Referentiable62 = gx10_Referentiable62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gx10_Referentiable62(self):
        return self.__gx10_Referentiable62

    @gx10_Referentiable62.setter
    def gx10_Referentiable62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable62", None)
        self.__gx10_Referentiable62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntVarAccess"):
                opp_val = getattr(old_value, "gx10_IntVarAccess", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntVarAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntVarAccess"):
                opp_val = getattr(value, "gx10_IntVarAccess", None)
                setattr(value, "gx10_IntVarAccess", self)

    @property
    def gx10_Referentiable60(self):
        return self.__gx10_Referentiable60

    @gx10_Referentiable60.setter
    def gx10_Referentiable60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable60", None)
        self.__gx10_Referentiable60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntVar59"):
                opp_val = getattr(old_value, "gx10_IntVar59", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntVar59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntVar59"):
                opp_val = getattr(value, "gx10_IntVar59", None)
                setattr(value, "gx10_IntVar59", self)

    @property
    def gx10_Referentiable64(self):
        return self.__gx10_Referentiable64

    @gx10_Referentiable64.setter
    def gx10_Referentiable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable64", None)
        self.__gx10_Referentiable64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolVarAccess"):
                opp_val = getattr(old_value, "gx10_BoolVarAccess", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolVarAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolVarAccess"):
                opp_val = getattr(value, "gx10_BoolVarAccess", None)
                setattr(value, "gx10_BoolVarAccess", self)

    @property
    def gx10_Referentiable55(self):
        return self.__gx10_Referentiable55

    @gx10_Referentiable55.setter
    def gx10_Referentiable55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable55", None)
        self.__gx10_Referentiable55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolVar54"):
                opp_val = getattr(old_value, "gx10_BoolVar54", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolVar54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolVar54"):
                opp_val = getattr(value, "gx10_BoolVar54", None)
                setattr(value, "gx10_BoolVar54", self)

    @property
    def gx10_Referentiable(self):
        return self.__gx10_Referentiable

    @gx10_Referentiable.setter
    def gx10_Referentiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable", None)
        self.__gx10_Referentiable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Method12"):
                opp_val = getattr(old_value, "gx10_Method12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Method12"):
                opp_val = getattr(value, "gx10_Method12", None)
                if opp_val is None:
                    setattr(value, "gx10_Method12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gx10_Block(Statement):

    def __init__(self, gx10_Block24: "gx10_If" = None, gx10_Block: "gx10_Method" = None, 14: set["gx10_Statement"] = None, 18: "gx10_Statement" = None, gx10_Block27: "gx10_If" = None, gx10_Block29: "gx10_While" = None):
        self.gx10_Block24 = gx10_Block24
        self.gx10_Block = gx10_Block
        self.14 = 14 if 14 is not None else set()
        self.18 = 18
        self.gx10_Block27 = gx10_Block27
        self.gx10_Block29 = gx10_Block29
        
    @property
    def gx10_Block27(self):
        return self.__gx10_Block27

    @gx10_Block27.setter
    def gx10_Block27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block27", None)
        self.__gx10_Block27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_If26"):
                opp_val = getattr(old_value, "gx10_If26", None)
                if opp_val == self:
                    setattr(old_value, "gx10_If26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_If26"):
                opp_val = getattr(value, "gx10_If26", None)
                setattr(value, "gx10_If26", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__14", None)
        self.__14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    if opp_val == self:
                        setattr(item, "15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    setattr(item, "15", self)
                    

    @property
    def gx10_Block29(self):
        return self.__gx10_Block29

    @gx10_Block29.setter
    def gx10_Block29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block29", None)
        self.__gx10_Block29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_While"):
                opp_val = getattr(old_value, "gx10_While", None)
                if opp_val == self:
                    setattr(old_value, "gx10_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_While"):
                opp_val = getattr(value, "gx10_While", None)
                setattr(value, "gx10_While", self)

    @property
    def gx10_Block24(self):
        return self.__gx10_Block24

    @gx10_Block24.setter
    def gx10_Block24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block24", None)
        self.__gx10_Block24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_If"):
                opp_val = getattr(old_value, "gx10_If", None)
                if opp_val == self:
                    setattr(old_value, "gx10_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_If"):
                opp_val = getattr(value, "gx10_If", None)
                setattr(value, "gx10_If", self)

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if opp_val == self:
                    setattr(old_value, "17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                setattr(value, "17", self)

    @property
    def gx10_Block(self):
        return self.__gx10_Block

    @gx10_Block.setter
    def gx10_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block", None)
        self.__gx10_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Method7"):
                opp_val = getattr(old_value, "gx10_Method7", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Method7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Method7"):
                opp_val = getattr(value, "gx10_Method7", None)
                setattr(value, "gx10_Method7", self)

    def initBlock(self):
        # TODO: Implement initBlock method
        pass

class gx10_Method:

    def __init__(self, name: bool, 1: "gx10_Program" = None, gx10_Method: "gx10_Program" = None, 4: "gx10_Program" = None, gx10_Method7: "gx10_Block" = None, 9: set["gx10_MethodCall"] = None, gx10_Method12: set["gx10_Referentiable"] = None, 44: "gx10_MethodCall" = None):
        self.name = name
        self.1 = 1
        self.gx10_Method = gx10_Method
        self.4 = 4
        self.gx10_Method7 = gx10_Method7
        self.9 = 9 if 9 is not None else set()
        self.gx10_Method12 = gx10_Method12 if gx10_Method12 is not None else set()
        self.44 = 44
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def gx10_Method7(self):
        return self.__gx10_Method7

    @gx10_Method7.setter
    def gx10_Method7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__gx10_Method7", None)
        self.__gx10_Method7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Block"):
                opp_val = getattr(old_value, "gx10_Block", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Block"):
                opp_val = getattr(value, "gx10_Block", None)
                setattr(value, "gx10_Block", self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def gx10_Method(self):
        return self.__gx10_Method

    @gx10_Method.setter
    def gx10_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__gx10_Method", None)
        self.__gx10_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Program"):
                opp_val = getattr(old_value, "gx10_Program", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Program"):
                opp_val = getattr(value, "gx10_Program", None)
                setattr(value, "gx10_Program", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 44(self):
        return self.__44

    @44.setter
    def 44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__44", None)
        self.__44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "43"):
                opp_val = getattr(old_value, "43", None)
                if opp_val == self:
                    setattr(old_value, "43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "43"):
                opp_val = getattr(value, "43", None)
                setattr(value, "43", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "5"):
                opp_val = getattr(old_value, "5", None)
                if opp_val == self:
                    setattr(old_value, "5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "5"):
                opp_val = getattr(value, "5", None)
                setattr(value, "5", self)

    @property
    def gx10_Method12(self):
        return self.__gx10_Method12

    @gx10_Method12.setter
    def gx10_Method12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__gx10_Method12", None)
        self.__gx10_Method12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gx10_Referentiable"):
                    opp_val = getattr(item, "gx10_Referentiable", None)
                    
                    if opp_val == self:
                        setattr(item, "gx10_Referentiable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gx10_Referentiable"):
                    opp_val = getattr(item, "gx10_Referentiable", None)
                    
                    setattr(item, "gx10_Referentiable", self)
                    

class ControlStructure:

    pass
class gx10_While(ControlStructure):

    pass
class gx10_If(ControlStructure):

    pass
class gx10_MethodCallParameter:

    def __init__(self, name: str, 22: "gx10_IntExpression" = None, 47: "gx10_MethodCall" = None, 71: "gx10_IntExpression" = None, 74: "gx10_MethodCall" = None):
        self.name = name
        self.22 = 22
        self.47 = 47
        self.71 = 71
        self.74 = 74
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 71(self):
        return self.__71

    @71.setter
    def 71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__71", None)
        self.__71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "72"):
                opp_val = getattr(old_value, "72", None)
                if opp_val == self:
                    setattr(old_value, "72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "72"):
                opp_val = getattr(value, "72", None)
                setattr(value, "72", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

    @property
    def 47(self):
        return self.__47

    @47.setter
    def 47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__47", None)
        self.__47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "46"):
                opp_val = getattr(old_value, "46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "46"):
                opp_val = getattr(value, "46", None)
                if opp_val is None:
                    setattr(value, "46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 74(self):
        return self.__74

    @74.setter
    def 74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__74", None)
        self.__74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "75"):
                opp_val = getattr(old_value, "75", None)
                if opp_val == self:
                    setattr(old_value, "75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "75"):
                opp_val = getattr(value, "75", None)
                setattr(value, "75", self)

class Expression:

    pass
class gx10_BoolExpression(Expression):

    def __init__(self, gx10_BoolExpression: "gx10_ControlStructure" = None, gx10_BoolExpression31: "gx10_Not" = None, gx10_BoolExpression33: "gx10_And" = None, gx10_BoolExpression36: "gx10_And" = None, gx10_BoolExpression52: "gx10_BoolVar" = None):
        self.gx10_BoolExpression = gx10_BoolExpression
        self.gx10_BoolExpression31 = gx10_BoolExpression31
        self.gx10_BoolExpression33 = gx10_BoolExpression33
        self.gx10_BoolExpression36 = gx10_BoolExpression36
        self.gx10_BoolExpression52 = gx10_BoolExpression52
        
    @property
    def gx10_BoolExpression31(self):
        return self.__gx10_BoolExpression31

    @gx10_BoolExpression31.setter
    def gx10_BoolExpression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression31", None)
        self.__gx10_BoolExpression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Not"):
                opp_val = getattr(old_value, "gx10_Not", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Not", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Not"):
                opp_val = getattr(value, "gx10_Not", None)
                setattr(value, "gx10_Not", self)

    @property
    def gx10_BoolExpression(self):
        return self.__gx10_BoolExpression

    @gx10_BoolExpression.setter
    def gx10_BoolExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression", None)
        self.__gx10_BoolExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_ControlStructure"):
                opp_val = getattr(old_value, "gx10_ControlStructure", None)
                if opp_val == self:
                    setattr(old_value, "gx10_ControlStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_ControlStructure"):
                opp_val = getattr(value, "gx10_ControlStructure", None)
                setattr(value, "gx10_ControlStructure", self)

    @property
    def gx10_BoolExpression36(self):
        return self.__gx10_BoolExpression36

    @gx10_BoolExpression36.setter
    def gx10_BoolExpression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression36", None)
        self.__gx10_BoolExpression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_And35"):
                opp_val = getattr(old_value, "gx10_And35", None)
                if opp_val == self:
                    setattr(old_value, "gx10_And35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_And35"):
                opp_val = getattr(value, "gx10_And35", None)
                setattr(value, "gx10_And35", self)

    @property
    def gx10_BoolExpression33(self):
        return self.__gx10_BoolExpression33

    @gx10_BoolExpression33.setter
    def gx10_BoolExpression33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression33", None)
        self.__gx10_BoolExpression33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_And"):
                opp_val = getattr(old_value, "gx10_And", None)
                if opp_val == self:
                    setattr(old_value, "gx10_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_And"):
                opp_val = getattr(value, "gx10_And", None)
                setattr(value, "gx10_And", self)

    @property
    def gx10_BoolExpression52(self):
        return self.__gx10_BoolExpression52

    @gx10_BoolExpression52.setter
    def gx10_BoolExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression52", None)
        self.__gx10_BoolExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolVar"):
                opp_val = getattr(old_value, "gx10_BoolVar", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolVar"):
                opp_val = getattr(value, "gx10_BoolVar", None)
                setattr(value, "gx10_BoolVar", self)

    def getCurrentValue(self):
        # TODO: Implement getCurrentValue method
        pass

class gx10_MethodCall(Expression):

    def __init__(self, 10: "gx10_Method" = None, 43: "gx10_Method" = None, 46: set["gx10_MethodCallParameter"] = None, 75: "gx10_MethodCallParameter" = None):
        self.10 = 10
        self.43 = 43
        self.46 = 46 if 46 is not None else set()
        self.75 = 75
        
    @property
    def 43(self):
        return self.__43

    @43.setter
    def 43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__43", None)
        self.__43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "44"):
                opp_val = getattr(old_value, "44", None)
                if opp_val == self:
                    setattr(old_value, "44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "44"):
                opp_val = getattr(value, "44", None)
                setattr(value, "44", self)

    @property
    def 46(self):
        return self.__46

    @46.setter
    def 46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__46", None)
        self.__46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "47"):
                    opp_val = getattr(item, "47", None)
                    
                    if opp_val == self:
                        setattr(item, "47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "47"):
                    opp_val = getattr(item, "47", None)
                    
                    setattr(item, "47", self)
                    

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                if opp_val is None:
                    setattr(value, "9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 75(self):
        return self.__75

    @75.setter
    def 75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__75", None)
        self.__75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "74"):
                opp_val = getattr(old_value, "74", None)
                if opp_val == self:
                    setattr(old_value, "74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "74"):
                opp_val = getattr(value, "74", None)
                setattr(value, "74", self)

    def call(self):
        # TODO: Implement call method
        pass

class gx10_BoolVar(Expression):

    def __init__(self, gx10_BoolVar: "gx10_BoolExpression" = None, gx10_BoolVar54: "gx10_Referentiable" = None):
        self.gx10_BoolVar = gx10_BoolVar
        self.gx10_BoolVar54 = gx10_BoolVar54
        
    @property
    def gx10_BoolVar(self):
        return self.__gx10_BoolVar

    @gx10_BoolVar.setter
    def gx10_BoolVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolVar__gx10_BoolVar", None)
        self.__gx10_BoolVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolExpression52"):
                opp_val = getattr(old_value, "gx10_BoolExpression52", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolExpression52"):
                opp_val = getattr(value, "gx10_BoolExpression52", None)
                setattr(value, "gx10_BoolExpression52", self)

    @property
    def gx10_BoolVar54(self):
        return self.__gx10_BoolVar54

    @gx10_BoolVar54.setter
    def gx10_BoolVar54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolVar__gx10_BoolVar54", None)
        self.__gx10_BoolVar54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Referentiable55"):
                opp_val = getattr(old_value, "gx10_Referentiable55", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Referentiable55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Referentiable55"):
                opp_val = getattr(value, "gx10_Referentiable55", None)
                setattr(value, "gx10_Referentiable55", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_IntExpression(Expression):

    def __init__(self, 21: "gx10_MethodCallParameter" = None, gx10_IntExpression: "gx10_IntBinaryOperation" = None, gx10_IntExpression40: "gx10_IntBinaryOperation" = None, gx10_IntExpression66: "gx10_Equal" = None, gx10_IntExpression69: "gx10_Equal" = None, gx10_IntExpression57: "gx10_IntVar" = None, 72: "gx10_MethodCallParameter" = None):
        self.21 = 21
        self.gx10_IntExpression = gx10_IntExpression
        self.gx10_IntExpression40 = gx10_IntExpression40
        self.gx10_IntExpression66 = gx10_IntExpression66
        self.gx10_IntExpression69 = gx10_IntExpression69
        self.gx10_IntExpression57 = gx10_IntExpression57
        self.72 = 72
        
    @property
    def gx10_IntExpression40(self):
        return self.__gx10_IntExpression40

    @gx10_IntExpression40.setter
    def gx10_IntExpression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression40", None)
        self.__gx10_IntExpression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntBinaryOperation39"):
                opp_val = getattr(old_value, "gx10_IntBinaryOperation39", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntBinaryOperation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntBinaryOperation39"):
                opp_val = getattr(value, "gx10_IntBinaryOperation39", None)
                setattr(value, "gx10_IntBinaryOperation39", self)

    @property
    def gx10_IntExpression66(self):
        return self.__gx10_IntExpression66

    @gx10_IntExpression66.setter
    def gx10_IntExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression66", None)
        self.__gx10_IntExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Equal"):
                opp_val = getattr(old_value, "gx10_Equal", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Equal"):
                opp_val = getattr(value, "gx10_Equal", None)
                setattr(value, "gx10_Equal", self)

    @property
    def gx10_IntExpression57(self):
        return self.__gx10_IntExpression57

    @gx10_IntExpression57.setter
    def gx10_IntExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression57", None)
        self.__gx10_IntExpression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntVar"):
                opp_val = getattr(old_value, "gx10_IntVar", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntVar"):
                opp_val = getattr(value, "gx10_IntVar", None)
                setattr(value, "gx10_IntVar", self)

    @property
    def gx10_IntExpression(self):
        return self.__gx10_IntExpression

    @gx10_IntExpression.setter
    def gx10_IntExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression", None)
        self.__gx10_IntExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntBinaryOperation"):
                opp_val = getattr(old_value, "gx10_IntBinaryOperation", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntBinaryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntBinaryOperation"):
                opp_val = getattr(value, "gx10_IntBinaryOperation", None)
                setattr(value, "gx10_IntBinaryOperation", self)

    @property
    def 21(self):
        return self.__21

    @21.setter
    def 21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__21", None)
        self.__21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "22"):
                opp_val = getattr(old_value, "22", None)
                if opp_val == self:
                    setattr(old_value, "22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "22"):
                opp_val = getattr(value, "22", None)
                setattr(value, "22", self)

    @property
    def gx10_IntExpression69(self):
        return self.__gx10_IntExpression69

    @gx10_IntExpression69.setter
    def gx10_IntExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression69", None)
        self.__gx10_IntExpression69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Equal68"):
                opp_val = getattr(old_value, "gx10_Equal68", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Equal68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Equal68"):
                opp_val = getattr(value, "gx10_Equal68", None)
                setattr(value, "gx10_Equal68", self)

    @property
    def 72(self):
        return self.__72

    @72.setter
    def 72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__72", None)
        self.__72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "71"):
                opp_val = getattr(old_value, "71", None)
                if opp_val == self:
                    setattr(old_value, "71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "71"):
                opp_val = getattr(value, "71", None)
                setattr(value, "71", self)

    def getCurrentValue(self):
        # TODO: Implement getCurrentValue method
        pass

class gx10_Program:

    pass