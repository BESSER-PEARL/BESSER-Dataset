from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Field:

    def __init__(self, name: str, myDsl_Field: "myDsl_BObject" = None, myDsl_Field95: "myDsl_Expr" = None):
        self.name = name
        self.myDsl_Field = myDsl_Field
        self.myDsl_Field95 = myDsl_Field95
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Field95(self):
        return self.__myDsl_Field95

    @myDsl_Field95.setter
    def myDsl_Field95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field__myDsl_Field95", None)
        self.__myDsl_Field95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr96"):
                opp_val = getattr(old_value, "myDsl_Expr96", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr96"):
                opp_val = getattr(value, "myDsl_Expr96", None)
                setattr(value, "myDsl_Expr96", self)

    @property
    def myDsl_Field(self):
        return self.__myDsl_Field

    @myDsl_Field.setter
    def myDsl_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field__myDsl_Field", None)
        self.__myDsl_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_BObject"):
                opp_val = getattr(old_value, "myDsl_BObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_BObject"):
                opp_val = getattr(value, "myDsl_BObject", None)
                if opp_val is None:
                    setattr(value, "myDsl_BObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expr:

    pass
class TopLevelCmd:

    pass
class myDsl_CmpOpUnequal(TopLevelCmd, Expr):

    pass
class myDsl_Let(TopLevelCmd, Expr):

    def __init__(self, name: str, myDsl_Let: "myDsl_Expr" = None, myDsl_Let30: "myDsl_Expr" = None):
        self.name = name
        self.myDsl_Let = myDsl_Let
        self.myDsl_Let30 = myDsl_Let30
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Let(self):
        return self.__myDsl_Let

    @myDsl_Let.setter
    def myDsl_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Let__myDsl_Let", None)
        self.__myDsl_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr28"):
                opp_val = getattr(old_value, "myDsl_Expr28", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr28"):
                opp_val = getattr(value, "myDsl_Expr28", None)
                setattr(value, "myDsl_Expr28", self)

    @property
    def myDsl_Let30(self):
        return self.__myDsl_Let30

    @myDsl_Let30.setter
    def myDsl_Let30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Let__myDsl_Let30", None)
        self.__myDsl_Let30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr31"):
                opp_val = getattr(old_value, "myDsl_Expr31", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr31"):
                opp_val = getattr(value, "myDsl_Expr31", None)
                setattr(value, "myDsl_Expr31", self)

class myDsl_This(TopLevelCmd, Expr):

    pass
class myDsl_Var(TopLevelCmd, Expr):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class myDsl_ArithOpRemainder(TopLevelCmd, Expr):

    pass
class myDsl_Fun(TopLevelCmd, Expr):

    def __init__(self, name: str, myDsl_Fun: "myDsl_Expr" = None):
        self.name = name
        self.myDsl_Fun = myDsl_Fun
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Fun(self):
        return self.__myDsl_Fun

    @myDsl_Fun.setter
    def myDsl_Fun(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Fun__myDsl_Fun", None)
        self.__myDsl_Fun = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr33"):
                opp_val = getattr(old_value, "myDsl_Expr33", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr33"):
                opp_val = getattr(value, "myDsl_Expr33", None)
                setattr(value, "myDsl_Expr33", self)

class myDsl_ArithOpPlus(TopLevelCmd, Expr):

    pass
class myDsl_Skip(TopLevelCmd, Expr):

    pass
class myDsl_BoolOpOr(TopLevelCmd, Expr):

    pass
class myDsl_ArithOpTimes(TopLevelCmd, Expr):

    pass
class myDsl_ArithOpDivide(TopLevelCmd, Expr):

    pass
class myDsl_Int(TopLevelCmd, Expr):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class myDsl_With(TopLevelCmd, Expr):

    pass
class myDsl_Bool(TopLevelCmd, Expr):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class myDsl_CmpOpLess(TopLevelCmd, Expr):

    pass
class myDsl_Not(TopLevelCmd, Expr):

    pass
class myDsl_ArithOpMinus(TopLevelCmd, Expr):

    pass
class myDsl_If(TopLevelCmd, Expr):

    pass
class myDsl_CmpOpEqual(TopLevelCmd, Expr):

    pass
class myDsl_App(TopLevelCmd, Expr):

    pass
class myDsl_Project(TopLevelCmd, Expr):

    def __init__(self, name: str, myDsl_Project: "myDsl_Expr" = None):
        self.name = name
        self.myDsl_Project = myDsl_Project
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Project(self):
        return self.__myDsl_Project

    @myDsl_Project.setter
    def myDsl_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Project__myDsl_Project", None)
        self.__myDsl_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr8"):
                opp_val = getattr(old_value, "myDsl_Expr8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr8"):
                opp_val = getattr(value, "myDsl_Expr8", None)
                setattr(value, "myDsl_Expr8", self)

class myDsl_Seq(TopLevelCmd, Expr):

    pass
class myDsl_BoolOpAnd(TopLevelCmd, Expr):

    pass
class myDsl_Copy(TopLevelCmd, Expr):

    pass
class myDsl_BObject(TopLevelCmd, Expr):

    pass
class myDsl_Assign(TopLevelCmd, Expr):

    def __init__(self, name: str, myDsl_Assign: "myDsl_Expr" = None, myDsl_Assign37: "myDsl_Expr" = None):
        self.name = name
        self.myDsl_Assign = myDsl_Assign
        self.myDsl_Assign37 = myDsl_Assign37
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Assign(self):
        return self.__myDsl_Assign

    @myDsl_Assign.setter
    def myDsl_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Assign__myDsl_Assign", None)
        self.__myDsl_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr35"):
                opp_val = getattr(old_value, "myDsl_Expr35", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr35"):
                opp_val = getattr(value, "myDsl_Expr35", None)
                setattr(value, "myDsl_Expr35", self)

    @property
    def myDsl_Assign37(self):
        return self.__myDsl_Assign37

    @myDsl_Assign37.setter
    def myDsl_Assign37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Assign__myDsl_Assign37", None)
        self.__myDsl_Assign37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr38"):
                opp_val = getattr(old_value, "myDsl_Expr38", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr38"):
                opp_val = getattr(value, "myDsl_Expr38", None)
                setattr(value, "myDsl_Expr38", self)

class myDsl_Def(TopLevelCmd):

    def __init__(self, name: str, myDsl_Def: "myDsl_Expr" = None):
        self.name = name
        self.myDsl_Def = myDsl_Def
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Def(self):
        return self.__myDsl_Def

    @myDsl_Def.setter
    def myDsl_Def(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Def__myDsl_Def", None)
        self.__myDsl_Def = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr"):
                opp_val = getattr(old_value, "myDsl_Expr", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr"):
                opp_val = getattr(value, "myDsl_Expr", None)
                setattr(value, "myDsl_Expr", self)

class myDsl_Expr:

    pass
class myDsl_TopLevelCmd:

    pass
class myDsl_File:

    pass