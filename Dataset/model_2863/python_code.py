from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Mexp:

    pass
class abs_MexpAnd_expr(Mexp):

    pass
class abs_MexpEquality_expr(Mexp):

    def __init__(self, op: str, abs_MexpEquality_expr: "abs_Mexp" = None, abs_MexpEquality_expr454: "abs_Mexp" = None):
        self.op = op
        self.abs_MexpEquality_expr = abs_MexpEquality_expr
        self.abs_MexpEquality_expr454 = abs_MexpEquality_expr454
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def abs_MexpEquality_expr454(self):
        return self.__abs_MexpEquality_expr454

    @abs_MexpEquality_expr454.setter
    def abs_MexpEquality_expr454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpEquality_expr__abs_MexpEquality_expr454", None)
        self.__abs_MexpEquality_expr454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp455"):
                opp_val = getattr(old_value, "abs_Mexp455", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp455", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp455"):
                opp_val = getattr(value, "abs_Mexp455", None)
                setattr(value, "abs_Mexp455", self)

    @property
    def abs_MexpEquality_expr(self):
        return self.__abs_MexpEquality_expr

    @abs_MexpEquality_expr.setter
    def abs_MexpEquality_expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpEquality_expr__abs_MexpEquality_expr", None)
        self.__abs_MexpEquality_expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp452"):
                opp_val = getattr(old_value, "abs_Mexp452", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp452"):
                opp_val = getattr(value, "abs_Mexp452", None)
                setattr(value, "abs_Mexp452", self)

class abs_MexpImplies_expr(Mexp):

    def __init__(self, op: str, abs_MexpImplies_expr449: "abs_Mexp" = None, abs_MexpImplies_expr: "abs_Mexp" = None):
        self.op = op
        self.abs_MexpImplies_expr449 = abs_MexpImplies_expr449
        self.abs_MexpImplies_expr = abs_MexpImplies_expr
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def abs_MexpImplies_expr449(self):
        return self.__abs_MexpImplies_expr449

    @abs_MexpImplies_expr449.setter
    def abs_MexpImplies_expr449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpImplies_expr__abs_MexpImplies_expr449", None)
        self.__abs_MexpImplies_expr449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp450"):
                opp_val = getattr(old_value, "abs_Mexp450", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp450"):
                opp_val = getattr(value, "abs_Mexp450", None)
                setattr(value, "abs_Mexp450", self)

    @property
    def abs_MexpImplies_expr(self):
        return self.__abs_MexpImplies_expr

    @abs_MexpImplies_expr.setter
    def abs_MexpImplies_expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpImplies_expr__abs_MexpImplies_expr", None)
        self.__abs_MexpImplies_expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp447"):
                opp_val = getattr(old_value, "abs_Mexp447", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp447"):
                opp_val = getattr(value, "abs_Mexp447", None)
                setattr(value, "abs_Mexp447", self)

class abs_MexpMulDivOrMod_expr(Mexp):

    def __init__(self, op: str, abs_MexpMulDivOrMod_expr: "abs_Mexp" = None, abs_MexpMulDivOrMod_expr469: "abs_Mexp" = None):
        self.op = op
        self.abs_MexpMulDivOrMod_expr = abs_MexpMulDivOrMod_expr
        self.abs_MexpMulDivOrMod_expr469 = abs_MexpMulDivOrMod_expr469
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def abs_MexpMulDivOrMod_expr469(self):
        return self.__abs_MexpMulDivOrMod_expr469

    @abs_MexpMulDivOrMod_expr469.setter
    def abs_MexpMulDivOrMod_expr469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpMulDivOrMod_expr__abs_MexpMulDivOrMod_expr469", None)
        self.__abs_MexpMulDivOrMod_expr469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp470"):
                opp_val = getattr(old_value, "abs_Mexp470", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp470"):
                opp_val = getattr(value, "abs_Mexp470", None)
                setattr(value, "abs_Mexp470", self)

    @property
    def abs_MexpMulDivOrMod_expr(self):
        return self.__abs_MexpMulDivOrMod_expr

    @abs_MexpMulDivOrMod_expr.setter
    def abs_MexpMulDivOrMod_expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpMulDivOrMod_expr__abs_MexpMulDivOrMod_expr", None)
        self.__abs_MexpMulDivOrMod_expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp467"):
                opp_val = getattr(old_value, "abs_Mexp467", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp467"):
                opp_val = getattr(value, "abs_Mexp467", None)
                setattr(value, "abs_Mexp467", self)

class abs_MexpComparison_expr(Mexp):

    def __init__(self, op: str, abs_MexpComparison_expr: "abs_Mexp" = None, abs_MexpComparison_expr459: "abs_Mexp" = None):
        self.op = op
        self.abs_MexpComparison_expr = abs_MexpComparison_expr
        self.abs_MexpComparison_expr459 = abs_MexpComparison_expr459
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def abs_MexpComparison_expr459(self):
        return self.__abs_MexpComparison_expr459

    @abs_MexpComparison_expr459.setter
    def abs_MexpComparison_expr459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpComparison_expr__abs_MexpComparison_expr459", None)
        self.__abs_MexpComparison_expr459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp460"):
                opp_val = getattr(old_value, "abs_Mexp460", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp460"):
                opp_val = getattr(value, "abs_Mexp460", None)
                setattr(value, "abs_Mexp460", self)

    @property
    def abs_MexpComparison_expr(self):
        return self.__abs_MexpComparison_expr

    @abs_MexpComparison_expr.setter
    def abs_MexpComparison_expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpComparison_expr__abs_MexpComparison_expr", None)
        self.__abs_MexpComparison_expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp457"):
                opp_val = getattr(old_value, "abs_Mexp457", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp457"):
                opp_val = getattr(value, "abs_Mexp457", None)
                setattr(value, "abs_Mexp457", self)

class abs_MexpPlusOrMinus_expr(Mexp):

    def __init__(self, op: str, abs_MexpPlusOrMinus_expr: "abs_Mexp" = None, abs_MexpPlusOrMinus_expr464: "abs_Mexp" = None):
        self.op = op
        self.abs_MexpPlusOrMinus_expr = abs_MexpPlusOrMinus_expr
        self.abs_MexpPlusOrMinus_expr464 = abs_MexpPlusOrMinus_expr464
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def abs_MexpPlusOrMinus_expr464(self):
        return self.__abs_MexpPlusOrMinus_expr464

    @abs_MexpPlusOrMinus_expr464.setter
    def abs_MexpPlusOrMinus_expr464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpPlusOrMinus_expr__abs_MexpPlusOrMinus_expr464", None)
        self.__abs_MexpPlusOrMinus_expr464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp465"):
                opp_val = getattr(old_value, "abs_Mexp465", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp465", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp465"):
                opp_val = getattr(value, "abs_Mexp465", None)
                setattr(value, "abs_Mexp465", self)

    @property
    def abs_MexpPlusOrMinus_expr(self):
        return self.__abs_MexpPlusOrMinus_expr

    @abs_MexpPlusOrMinus_expr.setter
    def abs_MexpPlusOrMinus_expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_MexpPlusOrMinus_expr__abs_MexpPlusOrMinus_expr", None)
        self.__abs_MexpPlusOrMinus_expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Mexp462"):
                opp_val = getattr(old_value, "abs_Mexp462", None)
                if opp_val == self:
                    setattr(old_value, "abs_Mexp462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Mexp462"):
                opp_val = getattr(value, "abs_Mexp462", None)
                setattr(value, "abs_Mexp462", self)

class abs_MexpPrimary_expr(Mexp):

    pass
class abs_MexpOr_exp(Mexp):

    pass
class Product_expr:

    pass
class abs_ProductAnd_exp(Product_expr):

    pass
class abs_ProductMinus_exp(Product_expr):

    pass
class abs_ProductOr_expr(Product_expr):

    pass
class Application_condition:

    pass
class abs_AppAnd_exp(Application_condition):

    pass
class abs_AppOr_exp(Application_condition):

    pass
class Guard:

    pass
class abs_AndGuard(Guard):

    def __init__(self, op: str, abs_AndGuard: "abs_Guard" = None, abs_AndGuard434: "abs_Guard" = None):
        self.op = op
        self.abs_AndGuard = abs_AndGuard
        self.abs_AndGuard434 = abs_AndGuard434
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def abs_AndGuard(self):
        return self.__abs_AndGuard

    @abs_AndGuard.setter
    def abs_AndGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_AndGuard__abs_AndGuard", None)
        self.__abs_AndGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard432"):
                opp_val = getattr(old_value, "abs_Guard432", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard432"):
                opp_val = getattr(value, "abs_Guard432", None)
                setattr(value, "abs_Guard432", self)

    @property
    def abs_AndGuard434(self):
        return self.__abs_AndGuard434

    @abs_AndGuard434.setter
    def abs_AndGuard434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_AndGuard__abs_AndGuard434", None)
        self.__abs_AndGuard434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard435"):
                opp_val = getattr(old_value, "abs_Guard435", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard435"):
                opp_val = getattr(value, "abs_Guard435", None)
                setattr(value, "abs_Guard435", self)

class abs_Mexp:

    def __init__(self, value: int, abs_Mexp: "abs_Feature_decl_constraint" = None, abs_Mexp450: "abs_MexpImplies_expr" = None, abs_Mexp452: "abs_MexpEquality_expr" = None, abs_Mexp455: "abs_MexpEquality_expr" = None, abs_Mexp437: "abs_MexpOr_exp" = None, abs_Mexp440: "abs_MexpOr_exp" = None, abs_Mexp442: "abs_MexpAnd_expr" = None, abs_Mexp445: "abs_MexpAnd_expr" = None, abs_Mexp447: "abs_MexpImplies_expr" = None, abs_Mexp462: "abs_MexpPlusOrMinus_expr" = None, abs_Mexp465: "abs_MexpPlusOrMinus_expr" = None, abs_Mexp467: "abs_MexpMulDivOrMod_expr" = None, abs_Mexp470: "abs_MexpMulDivOrMod_expr" = None, abs_Mexp457: "abs_MexpComparison_expr" = None, abs_Mexp460: "abs_MexpComparison_expr" = None, abs_Mexp472: "abs_MexpPrimary_expr" = None):
        self.value = value
        self.abs_Mexp = abs_Mexp
        self.abs_Mexp450 = abs_Mexp450
        self.abs_Mexp452 = abs_Mexp452
        self.abs_Mexp455 = abs_Mexp455
        self.abs_Mexp437 = abs_Mexp437
        self.abs_Mexp440 = abs_Mexp440
        self.abs_Mexp442 = abs_Mexp442
        self.abs_Mexp445 = abs_Mexp445
        self.abs_Mexp447 = abs_Mexp447
        self.abs_Mexp462 = abs_Mexp462
        self.abs_Mexp465 = abs_Mexp465
        self.abs_Mexp467 = abs_Mexp467
        self.abs_Mexp470 = abs_Mexp470
        self.abs_Mexp457 = abs_Mexp457
        self.abs_Mexp460 = abs_Mexp460
        self.abs_Mexp472 = abs_Mexp472
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def abs_Mexp437(self):
        return self.__abs_Mexp437

    @abs_Mexp437.setter
    def abs_Mexp437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp437", None)
        self.__abs_Mexp437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpOr_exp"):
                opp_val = getattr(old_value, "abs_MexpOr_exp", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpOr_exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpOr_exp"):
                opp_val = getattr(value, "abs_MexpOr_exp", None)
                setattr(value, "abs_MexpOr_exp", self)

    @property
    def abs_Mexp465(self):
        return self.__abs_Mexp465

    @abs_Mexp465.setter
    def abs_Mexp465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp465", None)
        self.__abs_Mexp465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpPlusOrMinus_expr464"):
                opp_val = getattr(old_value, "abs_MexpPlusOrMinus_expr464", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpPlusOrMinus_expr464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpPlusOrMinus_expr464"):
                opp_val = getattr(value, "abs_MexpPlusOrMinus_expr464", None)
                setattr(value, "abs_MexpPlusOrMinus_expr464", self)

    @property
    def abs_Mexp457(self):
        return self.__abs_Mexp457

    @abs_Mexp457.setter
    def abs_Mexp457(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp457", None)
        self.__abs_Mexp457 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpComparison_expr"):
                opp_val = getattr(old_value, "abs_MexpComparison_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpComparison_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpComparison_expr"):
                opp_val = getattr(value, "abs_MexpComparison_expr", None)
                setattr(value, "abs_MexpComparison_expr", self)

    @property
    def abs_Mexp452(self):
        return self.__abs_Mexp452

    @abs_Mexp452.setter
    def abs_Mexp452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp452", None)
        self.__abs_Mexp452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpEquality_expr"):
                opp_val = getattr(old_value, "abs_MexpEquality_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpEquality_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpEquality_expr"):
                opp_val = getattr(value, "abs_MexpEquality_expr", None)
                setattr(value, "abs_MexpEquality_expr", self)

    @property
    def abs_Mexp447(self):
        return self.__abs_Mexp447

    @abs_Mexp447.setter
    def abs_Mexp447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp447", None)
        self.__abs_Mexp447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpImplies_expr"):
                opp_val = getattr(old_value, "abs_MexpImplies_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpImplies_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpImplies_expr"):
                opp_val = getattr(value, "abs_MexpImplies_expr", None)
                setattr(value, "abs_MexpImplies_expr", self)

    @property
    def abs_Mexp442(self):
        return self.__abs_Mexp442

    @abs_Mexp442.setter
    def abs_Mexp442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp442", None)
        self.__abs_Mexp442 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpAnd_expr"):
                opp_val = getattr(old_value, "abs_MexpAnd_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpAnd_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpAnd_expr"):
                opp_val = getattr(value, "abs_MexpAnd_expr", None)
                setattr(value, "abs_MexpAnd_expr", self)

    @property
    def abs_Mexp462(self):
        return self.__abs_Mexp462

    @abs_Mexp462.setter
    def abs_Mexp462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp462", None)
        self.__abs_Mexp462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpPlusOrMinus_expr"):
                opp_val = getattr(old_value, "abs_MexpPlusOrMinus_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpPlusOrMinus_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpPlusOrMinus_expr"):
                opp_val = getattr(value, "abs_MexpPlusOrMinus_expr", None)
                setattr(value, "abs_MexpPlusOrMinus_expr", self)

    @property
    def abs_Mexp472(self):
        return self.__abs_Mexp472

    @abs_Mexp472.setter
    def abs_Mexp472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp472", None)
        self.__abs_Mexp472 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpPrimary_expr"):
                opp_val = getattr(old_value, "abs_MexpPrimary_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpPrimary_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpPrimary_expr"):
                opp_val = getattr(value, "abs_MexpPrimary_expr", None)
                setattr(value, "abs_MexpPrimary_expr", self)

    @property
    def abs_Mexp450(self):
        return self.__abs_Mexp450

    @abs_Mexp450.setter
    def abs_Mexp450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp450", None)
        self.__abs_Mexp450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpImplies_expr449"):
                opp_val = getattr(old_value, "abs_MexpImplies_expr449", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpImplies_expr449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpImplies_expr449"):
                opp_val = getattr(value, "abs_MexpImplies_expr449", None)
                setattr(value, "abs_MexpImplies_expr449", self)

    @property
    def abs_Mexp455(self):
        return self.__abs_Mexp455

    @abs_Mexp455.setter
    def abs_Mexp455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp455", None)
        self.__abs_Mexp455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpEquality_expr454"):
                opp_val = getattr(old_value, "abs_MexpEquality_expr454", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpEquality_expr454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpEquality_expr454"):
                opp_val = getattr(value, "abs_MexpEquality_expr454", None)
                setattr(value, "abs_MexpEquality_expr454", self)

    @property
    def abs_Mexp440(self):
        return self.__abs_Mexp440

    @abs_Mexp440.setter
    def abs_Mexp440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp440", None)
        self.__abs_Mexp440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpOr_exp439"):
                opp_val = getattr(old_value, "abs_MexpOr_exp439", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpOr_exp439", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpOr_exp439"):
                opp_val = getattr(value, "abs_MexpOr_exp439", None)
                setattr(value, "abs_MexpOr_exp439", self)

    @property
    def abs_Mexp467(self):
        return self.__abs_Mexp467

    @abs_Mexp467.setter
    def abs_Mexp467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp467", None)
        self.__abs_Mexp467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpMulDivOrMod_expr"):
                opp_val = getattr(old_value, "abs_MexpMulDivOrMod_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpMulDivOrMod_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpMulDivOrMod_expr"):
                opp_val = getattr(value, "abs_MexpMulDivOrMod_expr", None)
                setattr(value, "abs_MexpMulDivOrMod_expr", self)

    @property
    def abs_Mexp460(self):
        return self.__abs_Mexp460

    @abs_Mexp460.setter
    def abs_Mexp460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp460", None)
        self.__abs_Mexp460 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpComparison_expr459"):
                opp_val = getattr(old_value, "abs_MexpComparison_expr459", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpComparison_expr459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpComparison_expr459"):
                opp_val = getattr(value, "abs_MexpComparison_expr459", None)
                setattr(value, "abs_MexpComparison_expr459", self)

    @property
    def abs_Mexp470(self):
        return self.__abs_Mexp470

    @abs_Mexp470.setter
    def abs_Mexp470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp470", None)
        self.__abs_Mexp470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpMulDivOrMod_expr469"):
                opp_val = getattr(old_value, "abs_MexpMulDivOrMod_expr469", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpMulDivOrMod_expr469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpMulDivOrMod_expr469"):
                opp_val = getattr(value, "abs_MexpMulDivOrMod_expr469", None)
                setattr(value, "abs_MexpMulDivOrMod_expr469", self)

    @property
    def abs_Mexp(self):
        return self.__abs_Mexp

    @abs_Mexp.setter
    def abs_Mexp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp", None)
        self.__abs_Mexp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Feature_decl_constraint391"):
                opp_val = getattr(old_value, "abs_Feature_decl_constraint391", None)
                if opp_val == self:
                    setattr(old_value, "abs_Feature_decl_constraint391", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Feature_decl_constraint391"):
                opp_val = getattr(value, "abs_Feature_decl_constraint391", None)
                setattr(value, "abs_Feature_decl_constraint391", self)

    @property
    def abs_Mexp445(self):
        return self.__abs_Mexp445

    @abs_Mexp445.setter
    def abs_Mexp445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Mexp__abs_Mexp445", None)
        self.__abs_Mexp445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MexpAnd_expr444"):
                opp_val = getattr(old_value, "abs_MexpAnd_expr444", None)
                if opp_val == self:
                    setattr(old_value, "abs_MexpAnd_expr444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MexpAnd_expr444"):
                opp_val = getattr(value, "abs_MexpAnd_expr444", None)
                setattr(value, "abs_MexpAnd_expr444", self)

class abs_Fnode:

    pass
class abs_Feature_decl_constraint:

    pass
class abs_Feature_decl_attribute:

    def __init__(self, boundary_val: str, lBoundary_int: str, uBoundary_int: str, abs_Feature_decl_attribute: "abs_Feature_decl" = None, abs_Feature_decl_attribute397: "abs_Fextension" = None):
        self.boundary_val = boundary_val
        self.lBoundary_int = lBoundary_int
        self.uBoundary_int = uBoundary_int
        self.abs_Feature_decl_attribute = abs_Feature_decl_attribute
        self.abs_Feature_decl_attribute397 = abs_Feature_decl_attribute397
        
    @property
    def boundary_val(self) -> str:
        return self.__boundary_val

    @boundary_val.setter
    def boundary_val(self, boundary_val: str):
        self.__boundary_val = boundary_val

    @property
    def uBoundary_int(self) -> str:
        return self.__uBoundary_int

    @uBoundary_int.setter
    def uBoundary_int(self, uBoundary_int: str):
        self.__uBoundary_int = uBoundary_int

    @property
    def lBoundary_int(self) -> str:
        return self.__lBoundary_int

    @lBoundary_int.setter
    def lBoundary_int(self, lBoundary_int: str):
        self.__lBoundary_int = lBoundary_int

    @property
    def abs_Feature_decl_attribute397(self):
        return self.__abs_Feature_decl_attribute397

    @abs_Feature_decl_attribute397.setter
    def abs_Feature_decl_attribute397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl_attribute__abs_Feature_decl_attribute397", None)
        self.__abs_Feature_decl_attribute397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Fextension396"):
                opp_val = getattr(old_value, "abs_Fextension396", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Fextension396"):
                opp_val = getattr(value, "abs_Fextension396", None)
                if opp_val is None:
                    setattr(value, "abs_Fextension396", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Feature_decl_attribute(self):
        return self.__abs_Feature_decl_attribute

    @abs_Feature_decl_attribute.setter
    def abs_Feature_decl_attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl_attribute__abs_Feature_decl_attribute", None)
        self.__abs_Feature_decl_attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Feature_decl385"):
                opp_val = getattr(old_value, "abs_Feature_decl385", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Feature_decl385"):
                opp_val = getattr(value, "abs_Feature_decl385", None)
                if opp_val is None:
                    setattr(value, "abs_Feature_decl385", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Feature_decl_group:

    pass
class Fnode:

    pass
class abs_Application_condition:

    pass
class abs_Product_expr:

    pass
class abs_Product_reconfiguration:

    def __init__(self, name: str, update: str, abs_Product_reconfiguration: "abs_Product_decl" = None, abs_Product_reconfiguration381: set["abs_Delta_id"] = None):
        self.name = name
        self.update = update
        self.abs_Product_reconfiguration = abs_Product_reconfiguration
        self.abs_Product_reconfiguration381 = abs_Product_reconfiguration381 if abs_Product_reconfiguration381 is not None else set()
        
    @property
    def update(self) -> str:
        return self.__update

    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Product_reconfiguration381(self):
        return self.__abs_Product_reconfiguration381

    @abs_Product_reconfiguration381.setter
    def abs_Product_reconfiguration381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_reconfiguration__abs_Product_reconfiguration381", None)
        self.__abs_Product_reconfiguration381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Delta_id"):
                    opp_val = getattr(item, "abs_Delta_id", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Delta_id", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Delta_id"):
                    opp_val = getattr(item, "abs_Delta_id", None)
                    
                    setattr(item, "abs_Delta_id", self)
                    

    @property
    def abs_Product_reconfiguration(self):
        return self.__abs_Product_reconfiguration

    @abs_Product_reconfiguration.setter
    def abs_Product_reconfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_reconfiguration__abs_Product_reconfiguration", None)
        self.__abs_Product_reconfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Product_decl365"):
                opp_val = getattr(old_value, "abs_Product_decl365", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Product_decl365"):
                opp_val = getattr(value, "abs_Product_decl365", None)
                if opp_val is None:
                    setattr(value, "abs_Product_decl365", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Delta_clause:

    pass
class abs_Feature:

    def __init__(self, p: str, attr_assignment: str, abs_Feature: "abs_Productline_decl" = None, abs_Feature330: "abs_Feature_decl" = None, abs_Feature363: "abs_Product_decl" = None, abs_Feature354: "abs_Application_condition" = None):
        self.p = p
        self.attr_assignment = attr_assignment
        self.abs_Feature = abs_Feature
        self.abs_Feature330 = abs_Feature330
        self.abs_Feature363 = abs_Feature363
        self.abs_Feature354 = abs_Feature354
        
    @property
    def attr_assignment(self) -> str:
        return self.__attr_assignment

    @attr_assignment.setter
    def attr_assignment(self, attr_assignment: str):
        self.__attr_assignment = attr_assignment

    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

    @property
    def abs_Feature363(self):
        return self.__abs_Feature363

    @abs_Feature363.setter
    def abs_Feature363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature__abs_Feature363", None)
        self.__abs_Feature363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Product_decl362"):
                opp_val = getattr(old_value, "abs_Product_decl362", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Product_decl362"):
                opp_val = getattr(value, "abs_Product_decl362", None)
                if opp_val is None:
                    setattr(value, "abs_Product_decl362", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Feature330(self):
        return self.__abs_Feature330

    @abs_Feature330.setter
    def abs_Feature330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature__abs_Feature330", None)
        self.__abs_Feature330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Feature_decl331"):
                opp_val = getattr(old_value, "abs_Feature_decl331", None)
                if opp_val == self:
                    setattr(old_value, "abs_Feature_decl331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Feature_decl331"):
                opp_val = getattr(value, "abs_Feature_decl331", None)
                setattr(value, "abs_Feature_decl331", self)

    @property
    def abs_Feature354(self):
        return self.__abs_Feature354

    @abs_Feature354.setter
    def abs_Feature354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature__abs_Feature354", None)
        self.__abs_Feature354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Application_condition353"):
                opp_val = getattr(old_value, "abs_Application_condition353", None)
                if opp_val == self:
                    setattr(old_value, "abs_Application_condition353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Application_condition353"):
                opp_val = getattr(value, "abs_Application_condition353", None)
                setattr(value, "abs_Application_condition353", self)

    @property
    def abs_Feature(self):
        return self.__abs_Feature

    @abs_Feature.setter
    def abs_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature__abs_Feature", None)
        self.__abs_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Productline_decl326"):
                opp_val = getattr(old_value, "abs_Productline_decl326", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Productline_decl326"):
                opp_val = getattr(value, "abs_Productline_decl326", None)
                if opp_val is None:
                    setattr(value, "abs_Productline_decl326", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Deltaspec:

    def __init__(self, name: str, deltaspec_param: str):
        self.name = name
        self.deltaspec_param = deltaspec_param
        
    @property
    def deltaspec_param(self) -> str:
        return self.__deltaspec_param

    @deltaspec_param.setter
    def deltaspec_param(self, deltaspec_param: str):
        self.__deltaspec_param = deltaspec_param

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class abs_When_condition:

    pass
class abs_From_condition:

    pass
class abs_After_condition:

    pass
class abs_Object_update:

    pass
class abs_Object_update_assign_stmt:

    pass
class abs_Update_preamble_declaration:

    pass
class Module_modifier:

    pass
class abs_Namespace_modifier(Module_modifier):

    def __init__(self, star: str):
        self.star = star
        
    @property
    def star(self) -> str:
        return self.__star

    @star.setter
    def star(self, star: str):
        self.__star = star

class abs_OO_modifier(Module_modifier):

    pass
class abs_Functional_modifier(Module_modifier):

    pass
class abs_Interface_modifier_fragment:

    pass
class abs_Class_modifier_fragment:

    pass
class abs_Module_modifier:

    pass
class abs_Delta_access:

    pass
class abs_Delta_param:

    pass
class abs_Trait_oper:

    pass
class abs_Guard:

    pass
class abs_Method:

    def __init__(self, name: str, abs_Method: "abs_Class_decl" = None, abs_Method249: "abs_Type_use" = None, abs_Method224: "abs_Trait_expr" = None, abs_Method227: "abs_Trait_expr" = None, abs_Method252: "abs_Param_list" = None, abs_Method255: set["abs_Stmt"] = None):
        self.name = name
        self.abs_Method = abs_Method
        self.abs_Method249 = abs_Method249
        self.abs_Method224 = abs_Method224
        self.abs_Method227 = abs_Method227
        self.abs_Method252 = abs_Method252
        self.abs_Method255 = abs_Method255 if abs_Method255 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Method(self):
        return self.__abs_Method

    @abs_Method.setter
    def abs_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Method__abs_Method", None)
        self.__abs_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Class_decl133"):
                opp_val = getattr(old_value, "abs_Class_decl133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Class_decl133"):
                opp_val = getattr(value, "abs_Class_decl133", None)
                if opp_val is None:
                    setattr(value, "abs_Class_decl133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Method249(self):
        return self.__abs_Method249

    @abs_Method249.setter
    def abs_Method249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Method__abs_Method249", None)
        self.__abs_Method249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use250"):
                opp_val = getattr(old_value, "abs_Type_use250", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_use250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use250"):
                opp_val = getattr(value, "abs_Type_use250", None)
                setattr(value, "abs_Type_use250", self)

    @property
    def abs_Method224(self):
        return self.__abs_Method224

    @abs_Method224.setter
    def abs_Method224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Method__abs_Method224", None)
        self.__abs_Method224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Trait_expr"):
                opp_val = getattr(old_value, "abs_Trait_expr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Trait_expr"):
                opp_val = getattr(value, "abs_Trait_expr", None)
                if opp_val is None:
                    setattr(value, "abs_Trait_expr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Method255(self):
        return self.__abs_Method255

    @abs_Method255.setter
    def abs_Method255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Method__abs_Method255", None)
        self.__abs_Method255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Stmt256"):
                    opp_val = getattr(item, "abs_Stmt256", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Stmt256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Stmt256"):
                    opp_val = getattr(item, "abs_Stmt256", None)
                    
                    setattr(item, "abs_Stmt256", self)
                    

    @property
    def abs_Method227(self):
        return self.__abs_Method227

    @abs_Method227.setter
    def abs_Method227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Method__abs_Method227", None)
        self.__abs_Method227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Trait_expr226"):
                opp_val = getattr(old_value, "abs_Trait_expr226", None)
                if opp_val == self:
                    setattr(old_value, "abs_Trait_expr226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Trait_expr226"):
                opp_val = getattr(value, "abs_Trait_expr226", None)
                setattr(value, "abs_Trait_expr226", self)

    @property
    def abs_Method252(self):
        return self.__abs_Method252

    @abs_Method252.setter
    def abs_Method252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Method__abs_Method252", None)
        self.__abs_Method252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Param_list253"):
                opp_val = getattr(old_value, "abs_Param_list253", None)
                if opp_val == self:
                    setattr(old_value, "abs_Param_list253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Param_list253"):
                opp_val = getattr(value, "abs_Param_list253", None)
                setattr(value, "abs_Param_list253", self)

class abs_Trait_usage:

    pass
class abs_Casestmtbranch:

    pass
class abs_Stmt:

    def __init__(self, name: str, abs_Stmt141: "abs_Type_exp" = None, abs_Stmt144: "abs_Exp" = None, abs_Stmt146: "abs_Var_or_field_ref" = None, abs_Stmt150: "abs_Stmt" = None, abs_Stmt148: set["abs_Stmt"] = None, abs_Stmt152: "abs_Pure_exp" = None, abs_Stmt156: "abs_Stmt" = None, abs_Stmt154: "abs_Stmt" = None, abs_Stmt: "abs_Class_decl" = None, abs_Stmt181: "abs_Pure_exp" = None, abs_Stmt184: "abs_Pure_exp" = None, abs_Stmt187: "abs_Pure_exp" = None, abs_Stmt190: "abs_Pure_exp" = None, abs_Stmt193: "abs_Pure_exp" = None, abs_Stmt196: "abs_Pure_exp" = None, abs_Stmt159: "abs_Stmt" = None, abs_Stmt157: "abs_Stmt" = None, abs_Stmt161: "abs_Pure_exp" = None, abs_Stmt165: "abs_Stmt" = None, abs_Stmt163: "abs_Stmt" = None, abs_Stmt167: "abs_Pure_exp" = None, abs_Stmt171: "abs_Stmt" = None, abs_Stmt169: "abs_Stmt" = None, abs_Stmt174: "abs_Stmt" = None, abs_Stmt172: "abs_Stmt" = None, abs_Stmt176: set["abs_Casestmtbranch"] = None, abs_Stmt179: "abs_Guard" = None, abs_Stmt220: "abs_Casestmtbranch" = None, abs_Stmt256: "abs_Method" = None, abs_Stmt262: "abs_Main_block" = None):
        self.name = name
        self.abs_Stmt141 = abs_Stmt141
        self.abs_Stmt144 = abs_Stmt144
        self.abs_Stmt146 = abs_Stmt146
        self.abs_Stmt150 = abs_Stmt150
        self.abs_Stmt148 = abs_Stmt148 if abs_Stmt148 is not None else set()
        self.abs_Stmt152 = abs_Stmt152
        self.abs_Stmt156 = abs_Stmt156
        self.abs_Stmt154 = abs_Stmt154
        self.abs_Stmt = abs_Stmt
        self.abs_Stmt181 = abs_Stmt181
        self.abs_Stmt184 = abs_Stmt184
        self.abs_Stmt187 = abs_Stmt187
        self.abs_Stmt190 = abs_Stmt190
        self.abs_Stmt193 = abs_Stmt193
        self.abs_Stmt196 = abs_Stmt196
        self.abs_Stmt159 = abs_Stmt159
        self.abs_Stmt157 = abs_Stmt157
        self.abs_Stmt161 = abs_Stmt161
        self.abs_Stmt165 = abs_Stmt165
        self.abs_Stmt163 = abs_Stmt163
        self.abs_Stmt167 = abs_Stmt167
        self.abs_Stmt171 = abs_Stmt171
        self.abs_Stmt169 = abs_Stmt169
        self.abs_Stmt174 = abs_Stmt174
        self.abs_Stmt172 = abs_Stmt172
        self.abs_Stmt176 = abs_Stmt176 if abs_Stmt176 is not None else set()
        self.abs_Stmt179 = abs_Stmt179
        self.abs_Stmt220 = abs_Stmt220
        self.abs_Stmt256 = abs_Stmt256
        self.abs_Stmt262 = abs_Stmt262
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Stmt157(self):
        return self.__abs_Stmt157

    @abs_Stmt157.setter
    def abs_Stmt157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt157", None)
        self.__abs_Stmt157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt159"):
                opp_val = getattr(old_value, "abs_Stmt159", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt159"):
                opp_val = getattr(value, "abs_Stmt159", None)
                setattr(value, "abs_Stmt159", self)

    @property
    def abs_Stmt262(self):
        return self.__abs_Stmt262

    @abs_Stmt262.setter
    def abs_Stmt262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt262", None)
        self.__abs_Stmt262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Main_block261"):
                opp_val = getattr(old_value, "abs_Main_block261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Main_block261"):
                opp_val = getattr(value, "abs_Main_block261", None)
                if opp_val is None:
                    setattr(value, "abs_Main_block261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Stmt165(self):
        return self.__abs_Stmt165

    @abs_Stmt165.setter
    def abs_Stmt165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt165", None)
        self.__abs_Stmt165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt163"):
                opp_val = getattr(old_value, "abs_Stmt163", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt163"):
                opp_val = getattr(value, "abs_Stmt163", None)
                setattr(value, "abs_Stmt163", self)

    @property
    def abs_Stmt179(self):
        return self.__abs_Stmt179

    @abs_Stmt179.setter
    def abs_Stmt179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt179", None)
        self.__abs_Stmt179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard"):
                opp_val = getattr(old_value, "abs_Guard", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard"):
                opp_val = getattr(value, "abs_Guard", None)
                setattr(value, "abs_Guard", self)

    @property
    def abs_Stmt174(self):
        return self.__abs_Stmt174

    @abs_Stmt174.setter
    def abs_Stmt174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt174", None)
        self.__abs_Stmt174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt172"):
                opp_val = getattr(old_value, "abs_Stmt172", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt172"):
                opp_val = getattr(value, "abs_Stmt172", None)
                setattr(value, "abs_Stmt172", self)

    @property
    def abs_Stmt176(self):
        return self.__abs_Stmt176

    @abs_Stmt176.setter
    def abs_Stmt176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt176", None)
        self.__abs_Stmt176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Casestmtbranch177"):
                    opp_val = getattr(item, "abs_Casestmtbranch177", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Casestmtbranch177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Casestmtbranch177"):
                    opp_val = getattr(item, "abs_Casestmtbranch177", None)
                    
                    setattr(item, "abs_Casestmtbranch177", self)
                    

    @property
    def abs_Stmt152(self):
        return self.__abs_Stmt152

    @abs_Stmt152.setter
    def abs_Stmt152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt152", None)
        self.__abs_Stmt152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp153"):
                opp_val = getattr(old_value, "abs_Pure_exp153", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp153"):
                opp_val = getattr(value, "abs_Pure_exp153", None)
                setattr(value, "abs_Pure_exp153", self)

    @property
    def abs_Stmt(self):
        return self.__abs_Stmt

    @abs_Stmt.setter
    def abs_Stmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt", None)
        self.__abs_Stmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Class_decl127"):
                opp_val = getattr(old_value, "abs_Class_decl127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Class_decl127"):
                opp_val = getattr(value, "abs_Class_decl127", None)
                if opp_val is None:
                    setattr(value, "abs_Class_decl127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Stmt193(self):
        return self.__abs_Stmt193

    @abs_Stmt193.setter
    def abs_Stmt193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt193", None)
        self.__abs_Stmt193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp194"):
                opp_val = getattr(old_value, "abs_Pure_exp194", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp194"):
                opp_val = getattr(value, "abs_Pure_exp194", None)
                setattr(value, "abs_Pure_exp194", self)

    @property
    def abs_Stmt144(self):
        return self.__abs_Stmt144

    @abs_Stmt144.setter
    def abs_Stmt144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt144", None)
        self.__abs_Stmt144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Exp"):
                opp_val = getattr(old_value, "abs_Exp", None)
                if opp_val == self:
                    setattr(old_value, "abs_Exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Exp"):
                opp_val = getattr(value, "abs_Exp", None)
                setattr(value, "abs_Exp", self)

    @property
    def abs_Stmt146(self):
        return self.__abs_Stmt146

    @abs_Stmt146.setter
    def abs_Stmt146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt146", None)
        self.__abs_Stmt146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Var_or_field_ref147"):
                opp_val = getattr(old_value, "abs_Var_or_field_ref147", None)
                if opp_val == self:
                    setattr(old_value, "abs_Var_or_field_ref147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Var_or_field_ref147"):
                opp_val = getattr(value, "abs_Var_or_field_ref147", None)
                setattr(value, "abs_Var_or_field_ref147", self)

    @property
    def abs_Stmt141(self):
        return self.__abs_Stmt141

    @abs_Stmt141.setter
    def abs_Stmt141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt141", None)
        self.__abs_Stmt141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_exp142"):
                opp_val = getattr(old_value, "abs_Type_exp142", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_exp142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_exp142"):
                opp_val = getattr(value, "abs_Type_exp142", None)
                setattr(value, "abs_Type_exp142", self)

    @property
    def abs_Stmt196(self):
        return self.__abs_Stmt196

    @abs_Stmt196.setter
    def abs_Stmt196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt196", None)
        self.__abs_Stmt196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp197"):
                opp_val = getattr(old_value, "abs_Pure_exp197", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp197"):
                opp_val = getattr(value, "abs_Pure_exp197", None)
                setattr(value, "abs_Pure_exp197", self)

    @property
    def abs_Stmt256(self):
        return self.__abs_Stmt256

    @abs_Stmt256.setter
    def abs_Stmt256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt256", None)
        self.__abs_Stmt256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Method255"):
                opp_val = getattr(old_value, "abs_Method255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Method255"):
                opp_val = getattr(value, "abs_Method255", None)
                if opp_val is None:
                    setattr(value, "abs_Method255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Stmt161(self):
        return self.__abs_Stmt161

    @abs_Stmt161.setter
    def abs_Stmt161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt161", None)
        self.__abs_Stmt161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp162"):
                opp_val = getattr(old_value, "abs_Pure_exp162", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp162"):
                opp_val = getattr(value, "abs_Pure_exp162", None)
                setattr(value, "abs_Pure_exp162", self)

    @property
    def abs_Stmt167(self):
        return self.__abs_Stmt167

    @abs_Stmt167.setter
    def abs_Stmt167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt167", None)
        self.__abs_Stmt167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp168"):
                opp_val = getattr(old_value, "abs_Pure_exp168", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp168"):
                opp_val = getattr(value, "abs_Pure_exp168", None)
                setattr(value, "abs_Pure_exp168", self)

    @property
    def abs_Stmt171(self):
        return self.__abs_Stmt171

    @abs_Stmt171.setter
    def abs_Stmt171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt171", None)
        self.__abs_Stmt171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt169"):
                opp_val = getattr(old_value, "abs_Stmt169", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt169"):
                opp_val = getattr(value, "abs_Stmt169", None)
                setattr(value, "abs_Stmt169", self)

    @property
    def abs_Stmt156(self):
        return self.__abs_Stmt156

    @abs_Stmt156.setter
    def abs_Stmt156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt156", None)
        self.__abs_Stmt156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt154"):
                opp_val = getattr(old_value, "abs_Stmt154", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt154"):
                opp_val = getattr(value, "abs_Stmt154", None)
                setattr(value, "abs_Stmt154", self)

    @property
    def abs_Stmt163(self):
        return self.__abs_Stmt163

    @abs_Stmt163.setter
    def abs_Stmt163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt163", None)
        self.__abs_Stmt163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt165"):
                opp_val = getattr(old_value, "abs_Stmt165", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt165"):
                opp_val = getattr(value, "abs_Stmt165", None)
                setattr(value, "abs_Stmt165", self)

    @property
    def abs_Stmt148(self):
        return self.__abs_Stmt148

    @abs_Stmt148.setter
    def abs_Stmt148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt148", None)
        self.__abs_Stmt148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Stmt150"):
                    opp_val = getattr(item, "abs_Stmt150", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Stmt150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Stmt150"):
                    opp_val = getattr(item, "abs_Stmt150", None)
                    
                    setattr(item, "abs_Stmt150", self)
                    

    @property
    def abs_Stmt150(self):
        return self.__abs_Stmt150

    @abs_Stmt150.setter
    def abs_Stmt150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt150", None)
        self.__abs_Stmt150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt148"):
                opp_val = getattr(old_value, "abs_Stmt148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt148"):
                opp_val = getattr(value, "abs_Stmt148", None)
                if opp_val is None:
                    setattr(value, "abs_Stmt148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Stmt172(self):
        return self.__abs_Stmt172

    @abs_Stmt172.setter
    def abs_Stmt172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt172", None)
        self.__abs_Stmt172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt174"):
                opp_val = getattr(old_value, "abs_Stmt174", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt174"):
                opp_val = getattr(value, "abs_Stmt174", None)
                setattr(value, "abs_Stmt174", self)

    @property
    def abs_Stmt190(self):
        return self.__abs_Stmt190

    @abs_Stmt190.setter
    def abs_Stmt190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt190", None)
        self.__abs_Stmt190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp191"):
                opp_val = getattr(old_value, "abs_Pure_exp191", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp191"):
                opp_val = getattr(value, "abs_Pure_exp191", None)
                setattr(value, "abs_Pure_exp191", self)

    @property
    def abs_Stmt169(self):
        return self.__abs_Stmt169

    @abs_Stmt169.setter
    def abs_Stmt169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt169", None)
        self.__abs_Stmt169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt171"):
                opp_val = getattr(old_value, "abs_Stmt171", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt171"):
                opp_val = getattr(value, "abs_Stmt171", None)
                setattr(value, "abs_Stmt171", self)

    @property
    def abs_Stmt181(self):
        return self.__abs_Stmt181

    @abs_Stmt181.setter
    def abs_Stmt181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt181", None)
        self.__abs_Stmt181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp182"):
                opp_val = getattr(old_value, "abs_Pure_exp182", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp182"):
                opp_val = getattr(value, "abs_Pure_exp182", None)
                setattr(value, "abs_Pure_exp182", self)

    @property
    def abs_Stmt159(self):
        return self.__abs_Stmt159

    @abs_Stmt159.setter
    def abs_Stmt159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt159", None)
        self.__abs_Stmt159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt157"):
                opp_val = getattr(old_value, "abs_Stmt157", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt157"):
                opp_val = getattr(value, "abs_Stmt157", None)
                setattr(value, "abs_Stmt157", self)

    @property
    def abs_Stmt154(self):
        return self.__abs_Stmt154

    @abs_Stmt154.setter
    def abs_Stmt154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt154", None)
        self.__abs_Stmt154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt156"):
                opp_val = getattr(old_value, "abs_Stmt156", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt156"):
                opp_val = getattr(value, "abs_Stmt156", None)
                setattr(value, "abs_Stmt156", self)

    @property
    def abs_Stmt184(self):
        return self.__abs_Stmt184

    @abs_Stmt184.setter
    def abs_Stmt184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt184", None)
        self.__abs_Stmt184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp185"):
                opp_val = getattr(old_value, "abs_Pure_exp185", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp185"):
                opp_val = getattr(value, "abs_Pure_exp185", None)
                setattr(value, "abs_Pure_exp185", self)

    @property
    def abs_Stmt220(self):
        return self.__abs_Stmt220

    @abs_Stmt220.setter
    def abs_Stmt220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt220", None)
        self.__abs_Stmt220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Casestmtbranch219"):
                opp_val = getattr(old_value, "abs_Casestmtbranch219", None)
                if opp_val == self:
                    setattr(old_value, "abs_Casestmtbranch219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Casestmtbranch219"):
                opp_val = getattr(value, "abs_Casestmtbranch219", None)
                setattr(value, "abs_Casestmtbranch219", self)

    @property
    def abs_Stmt187(self):
        return self.__abs_Stmt187

    @abs_Stmt187.setter
    def abs_Stmt187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Stmt__abs_Stmt187", None)
        self.__abs_Stmt187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp188"):
                opp_val = getattr(old_value, "abs_Pure_exp188", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp188"):
                opp_val = getattr(value, "abs_Pure_exp188", None)
                setattr(value, "abs_Pure_exp188", self)

class abs_Exp:

    pass
class Update_preamble_declaration:

    pass
class abs_Type_exp(Update_preamble_declaration):

    def __init__(self, name: str, abs_Type_exp: "abs_Param_decl" = None, abs_Type_exp94: set["abs_Type_use"] = None, abs_Type_exp142: "abs_Stmt" = None):
        self.name = name
        self.abs_Type_exp = abs_Type_exp
        self.abs_Type_exp94 = abs_Type_exp94 if abs_Type_exp94 is not None else set()
        self.abs_Type_exp142 = abs_Type_exp142
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Type_exp94(self):
        return self.__abs_Type_exp94

    @abs_Type_exp94.setter
    def abs_Type_exp94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_exp__abs_Type_exp94", None)
        self.__abs_Type_exp94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Type_use95"):
                    opp_val = getattr(item, "abs_Type_use95", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Type_use95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Type_use95"):
                    opp_val = getattr(item, "abs_Type_use95", None)
                    
                    setattr(item, "abs_Type_use95", self)
                    

    @property
    def abs_Type_exp142(self):
        return self.__abs_Type_exp142

    @abs_Type_exp142.setter
    def abs_Type_exp142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_exp__abs_Type_exp142", None)
        self.__abs_Type_exp142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt141"):
                opp_val = getattr(old_value, "abs_Stmt141", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt141"):
                opp_val = getattr(value, "abs_Stmt141", None)
                setattr(value, "abs_Stmt141", self)

    @property
    def abs_Type_exp(self):
        return self.__abs_Type_exp

    @abs_Type_exp.setter
    def abs_Type_exp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_exp__abs_Type_exp", None)
        self.__abs_Type_exp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Param_decl92"):
                opp_val = getattr(old_value, "abs_Param_decl92", None)
                if opp_val == self:
                    setattr(old_value, "abs_Param_decl92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Param_decl92"):
                opp_val = getattr(value, "abs_Param_decl92", None)
                setattr(value, "abs_Param_decl92", self)

class Delta_param:

    pass
class abs_Has_condition(Delta_param):

    pass
class abs_Param_decl(Delta_param):

    def __init__(self, name: str, abs_Param_decl: "abs_Param_list" = None, abs_Param_decl92: "abs_Type_exp" = None):
        self.name = name
        self.abs_Param_decl = abs_Param_decl
        self.abs_Param_decl92 = abs_Param_decl92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Param_decl92(self):
        return self.__abs_Param_decl92

    @abs_Param_decl92.setter
    def abs_Param_decl92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Param_decl__abs_Param_decl92", None)
        self.__abs_Param_decl92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_exp"):
                opp_val = getattr(old_value, "abs_Type_exp", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_exp"):
                opp_val = getattr(value, "abs_Type_exp", None)
                setattr(value, "abs_Type_exp", self)

    @property
    def abs_Param_decl(self):
        return self.__abs_Param_decl

    @abs_Param_decl.setter
    def abs_Param_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Param_decl__abs_Param_decl", None)
        self.__abs_Param_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Param_list90"):
                opp_val = getattr(old_value, "abs_Param_list90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Param_list90"):
                opp_val = getattr(value, "abs_Param_list90", None)
                if opp_val is None:
                    setattr(value, "abs_Param_list90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Interface_modifier_fragment:

    pass
class Class_modifier_fragment:

    pass
class abs_Trait_expr(Class_modifier_fragment):

    pass
class abs_Interface_name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class abs_Methodsig(Interface_modifier_fragment, Class_modifier_fragment):

    def __init__(self, name: str, abs_Methodsig: "abs_Interface_decl" = None, abs_Methodsig113: "abs_Type_use" = None, abs_Methodsig116: "abs_Param_list" = None, abs_Methodsig238: "abs_Trait_oper" = None, abs_Methodsig241: "abs_Trait_oper" = None, abs_Methodsig273: "abs_Has_condition" = None, abs_Methodsig306: "abs_Class_modifier_fragment" = None):
        self.name = name
        self.abs_Methodsig = abs_Methodsig
        self.abs_Methodsig113 = abs_Methodsig113
        self.abs_Methodsig116 = abs_Methodsig116
        self.abs_Methodsig238 = abs_Methodsig238
        self.abs_Methodsig241 = abs_Methodsig241
        self.abs_Methodsig273 = abs_Methodsig273
        self.abs_Methodsig306 = abs_Methodsig306
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Methodsig116(self):
        return self.__abs_Methodsig116

    @abs_Methodsig116.setter
    def abs_Methodsig116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig116", None)
        self.__abs_Methodsig116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Param_list117"):
                opp_val = getattr(old_value, "abs_Param_list117", None)
                if opp_val == self:
                    setattr(old_value, "abs_Param_list117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Param_list117"):
                opp_val = getattr(value, "abs_Param_list117", None)
                setattr(value, "abs_Param_list117", self)

    @property
    def abs_Methodsig(self):
        return self.__abs_Methodsig

    @abs_Methodsig.setter
    def abs_Methodsig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig", None)
        self.__abs_Methodsig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Interface_decl111"):
                opp_val = getattr(old_value, "abs_Interface_decl111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Interface_decl111"):
                opp_val = getattr(value, "abs_Interface_decl111", None)
                if opp_val is None:
                    setattr(value, "abs_Interface_decl111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Methodsig238(self):
        return self.__abs_Methodsig238

    @abs_Methodsig238.setter
    def abs_Methodsig238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig238", None)
        self.__abs_Methodsig238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Trait_oper237"):
                opp_val = getattr(old_value, "abs_Trait_oper237", None)
                if opp_val == self:
                    setattr(old_value, "abs_Trait_oper237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Trait_oper237"):
                opp_val = getattr(value, "abs_Trait_oper237", None)
                setattr(value, "abs_Trait_oper237", self)

    @property
    def abs_Methodsig306(self):
        return self.__abs_Methodsig306

    @abs_Methodsig306.setter
    def abs_Methodsig306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig306", None)
        self.__abs_Methodsig306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Class_modifier_fragment305"):
                opp_val = getattr(old_value, "abs_Class_modifier_fragment305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Class_modifier_fragment305"):
                opp_val = getattr(value, "abs_Class_modifier_fragment305", None)
                if opp_val is None:
                    setattr(value, "abs_Class_modifier_fragment305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Methodsig113(self):
        return self.__abs_Methodsig113

    @abs_Methodsig113.setter
    def abs_Methodsig113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig113", None)
        self.__abs_Methodsig113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use114"):
                opp_val = getattr(old_value, "abs_Type_use114", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_use114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use114"):
                opp_val = getattr(value, "abs_Type_use114", None)
                setattr(value, "abs_Type_use114", self)

    @property
    def abs_Methodsig273(self):
        return self.__abs_Methodsig273

    @abs_Methodsig273.setter
    def abs_Methodsig273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig273", None)
        self.__abs_Methodsig273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Has_condition272"):
                opp_val = getattr(old_value, "abs_Has_condition272", None)
                if opp_val == self:
                    setattr(old_value, "abs_Has_condition272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Has_condition272"):
                opp_val = getattr(value, "abs_Has_condition272", None)
                setattr(value, "abs_Has_condition272", self)

    @property
    def abs_Methodsig241(self):
        return self.__abs_Methodsig241

    @abs_Methodsig241.setter
    def abs_Methodsig241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Methodsig__abs_Methodsig241", None)
        self.__abs_Methodsig241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Trait_oper240"):
                opp_val = getattr(old_value, "abs_Trait_oper240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Trait_oper240"):
                opp_val = getattr(value, "abs_Trait_oper240", None)
                if opp_val is None:
                    setattr(value, "abs_Trait_oper240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Case_branch:

    pass
class abs_Pattern(Case_branch):

    pass
class abs_Field_decl(Class_modifier_fragment):

    def __init__(self, name: str, abs_Field_decl: "abs_Var_or_field_ref" = None, abs_Field_decl135: "abs_Type_use" = None, abs_Field_decl138: "abs_Pure_exp" = None, abs_Field_decl125: "abs_Class_decl" = None, abs_Field_decl270: "abs_Has_condition" = None):
        self.name = name
        self.abs_Field_decl = abs_Field_decl
        self.abs_Field_decl135 = abs_Field_decl135
        self.abs_Field_decl138 = abs_Field_decl138
        self.abs_Field_decl125 = abs_Field_decl125
        self.abs_Field_decl270 = abs_Field_decl270
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Field_decl135(self):
        return self.__abs_Field_decl135

    @abs_Field_decl135.setter
    def abs_Field_decl135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Field_decl__abs_Field_decl135", None)
        self.__abs_Field_decl135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use136"):
                opp_val = getattr(old_value, "abs_Type_use136", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_use136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use136"):
                opp_val = getattr(value, "abs_Type_use136", None)
                setattr(value, "abs_Type_use136", self)

    @property
    def abs_Field_decl(self):
        return self.__abs_Field_decl

    @abs_Field_decl.setter
    def abs_Field_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Field_decl__abs_Field_decl", None)
        self.__abs_Field_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Var_or_field_ref"):
                opp_val = getattr(old_value, "abs_Var_or_field_ref", None)
                if opp_val == self:
                    setattr(old_value, "abs_Var_or_field_ref", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Var_or_field_ref"):
                opp_val = getattr(value, "abs_Var_or_field_ref", None)
                setattr(value, "abs_Var_or_field_ref", self)

    @property
    def abs_Field_decl138(self):
        return self.__abs_Field_decl138

    @abs_Field_decl138.setter
    def abs_Field_decl138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Field_decl__abs_Field_decl138", None)
        self.__abs_Field_decl138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp139"):
                opp_val = getattr(old_value, "abs_Pure_exp139", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp139"):
                opp_val = getattr(value, "abs_Pure_exp139", None)
                setattr(value, "abs_Pure_exp139", self)

    @property
    def abs_Field_decl270(self):
        return self.__abs_Field_decl270

    @abs_Field_decl270.setter
    def abs_Field_decl270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Field_decl__abs_Field_decl270", None)
        self.__abs_Field_decl270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Has_condition"):
                opp_val = getattr(old_value, "abs_Has_condition", None)
                if opp_val == self:
                    setattr(old_value, "abs_Has_condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Has_condition"):
                opp_val = getattr(value, "abs_Has_condition", None)
                setattr(value, "abs_Has_condition", self)

    @property
    def abs_Field_decl125(self):
        return self.__abs_Field_decl125

    @abs_Field_decl125.setter
    def abs_Field_decl125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Field_decl__abs_Field_decl125", None)
        self.__abs_Field_decl125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Class_decl124"):
                opp_val = getattr(old_value, "abs_Class_decl124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Class_decl124"):
                opp_val = getattr(value, "abs_Class_decl124", None)
                if opp_val is None:
                    setattr(value, "abs_Class_decl124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Pure_exp:

    pass
class abs_Or_expr(Pure_exp):

    pass
class abs_Equality_expr(Pure_exp):

    pass
class abs_PlusOrMinus_expr(Pure_exp):

    pass
class abs_Comparison_expr(Pure_exp):

    pass
class abs_And_expr(Pure_exp):

    pass
class abs_MulDivOrMod_expr(Pure_exp):

    pass
class abs_Var_or_field_ref(Pure_exp):

    def __init__(self, name: str, abs_Var_or_field_ref: "abs_Field_decl" = None, abs_Var_or_field_ref147: "abs_Stmt" = None, abs_Var_or_field_ref205: "abs_Guard" = None, abs_Var_or_field_ref321: "abs_Object_update_assign_stmt" = None):
        self.name = name
        self.abs_Var_or_field_ref = abs_Var_or_field_ref
        self.abs_Var_or_field_ref147 = abs_Var_or_field_ref147
        self.abs_Var_or_field_ref205 = abs_Var_or_field_ref205
        self.abs_Var_or_field_ref321 = abs_Var_or_field_ref321
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Var_or_field_ref147(self):
        return self.__abs_Var_or_field_ref147

    @abs_Var_or_field_ref147.setter
    def abs_Var_or_field_ref147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Var_or_field_ref__abs_Var_or_field_ref147", None)
        self.__abs_Var_or_field_ref147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt146"):
                opp_val = getattr(old_value, "abs_Stmt146", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt146"):
                opp_val = getattr(value, "abs_Stmt146", None)
                setattr(value, "abs_Stmt146", self)

    @property
    def abs_Var_or_field_ref(self):
        return self.__abs_Var_or_field_ref

    @abs_Var_or_field_ref.setter
    def abs_Var_or_field_ref(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Var_or_field_ref__abs_Var_or_field_ref", None)
        self.__abs_Var_or_field_ref = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Field_decl"):
                opp_val = getattr(old_value, "abs_Field_decl", None)
                if opp_val == self:
                    setattr(old_value, "abs_Field_decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Field_decl"):
                opp_val = getattr(value, "abs_Field_decl", None)
                setattr(value, "abs_Field_decl", self)

    @property
    def abs_Var_or_field_ref205(self):
        return self.__abs_Var_or_field_ref205

    @abs_Var_or_field_ref205.setter
    def abs_Var_or_field_ref205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Var_or_field_ref__abs_Var_or_field_ref205", None)
        self.__abs_Var_or_field_ref205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard204"):
                opp_val = getattr(old_value, "abs_Guard204", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard204"):
                opp_val = getattr(value, "abs_Guard204", None)
                setattr(value, "abs_Guard204", self)

    @property
    def abs_Var_or_field_ref321(self):
        return self.__abs_Var_or_field_ref321

    @abs_Var_or_field_ref321.setter
    def abs_Var_or_field_ref321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Var_or_field_ref__abs_Var_or_field_ref321", None)
        self.__abs_Var_or_field_ref321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Object_update_assign_stmt320"):
                opp_val = getattr(old_value, "abs_Object_update_assign_stmt320", None)
                if opp_val == self:
                    setattr(old_value, "abs_Object_update_assign_stmt320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Object_update_assign_stmt320"):
                opp_val = getattr(value, "abs_Object_update_assign_stmt320", None)
                setattr(value, "abs_Object_update_assign_stmt320", self)

class Function_param:

    pass
class abs_Anon_function_decl(Function_param):

    pass
class abs_Function_name_param_decl(Function_param):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class abs_Function_param:

    pass
class abs_Case_branch:

    pass
class Data_constructor_arg:

    pass
class abs_Annotation:

    pass
class abs_Annotations:

    pass
class abs_Data_constructor_arg:

    pass
class abs_Pure_exp_list:

    pass
class abs_Function_list:

    pass
class Eff_expr:

    pass
class abs_Delta_id(Eff_expr):

    def __init__(self, name: str, abs_Delta_id: "abs_Product_reconfiguration" = None):
        self.name = name
        self.abs_Delta_id = abs_Delta_id
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Delta_id(self):
        return self.__abs_Delta_id

    @abs_Delta_id.setter
    def abs_Delta_id(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_id__abs_Delta_id", None)
        self.__abs_Delta_id = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Product_reconfiguration381"):
                opp_val = getattr(old_value, "abs_Product_reconfiguration381", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Product_reconfiguration381"):
                opp_val = getattr(value, "abs_Product_reconfiguration381", None)
                if opp_val is None:
                    setattr(value, "abs_Product_reconfiguration381", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Exp:

    pass
class abs_Eff_expr(Exp):

    def __init__(self, l: str, abs_Eff_expr: "abs_Pure_exp_list" = None, abs_Eff_expr201: set["abs_Pure_exp_list"] = None):
        self.l = l
        self.abs_Eff_expr = abs_Eff_expr
        self.abs_Eff_expr201 = abs_Eff_expr201 if abs_Eff_expr201 is not None else set()
        
    @property
    def l(self) -> str:
        return self.__l

    @l.setter
    def l(self, l: str):
        self.__l = l

    @property
    def abs_Eff_expr(self):
        return self.__abs_Eff_expr

    @abs_Eff_expr.setter
    def abs_Eff_expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Eff_expr__abs_Eff_expr", None)
        self.__abs_Eff_expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp_list199"):
                opp_val = getattr(old_value, "abs_Pure_exp_list199", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp_list199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp_list199"):
                opp_val = getattr(value, "abs_Pure_exp_list199", None)
                setattr(value, "abs_Pure_exp_list199", self)

    @property
    def abs_Eff_expr201(self):
        return self.__abs_Eff_expr201

    @abs_Eff_expr201.setter
    def abs_Eff_expr201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Eff_expr__abs_Eff_expr201", None)
        self.__abs_Eff_expr201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Pure_exp_list202"):
                    opp_val = getattr(item, "abs_Pure_exp_list202", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Pure_exp_list202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Pure_exp_list202"):
                    opp_val = getattr(item, "abs_Pure_exp_list202", None)
                    
                    setattr(item, "abs_Pure_exp_list202", self)
                    

class Annotation:

    pass
class abs_Pure_exp(Eff_expr, Exp):

    def __init__(self, value: str, op: str, await: str, val: str, abs_Pure_exp: "abs_Par_function_decl" = None, abs_Pure_exp41: set["abs_Function_list"] = None, abs_Pure_exp43: "abs_Pure_exp_list" = None, abs_Pure_exp36: "abs_Annotation" = None, abs_Pure_exp62: "abs_Type_use" = None, abs_Pure_exp66: "abs_Pure_exp" = None, abs_Pure_exp64: "abs_Pure_exp" = None, abs_Pure_exp69: "abs_Pure_exp" = None, abs_Pure_exp67: "abs_Pure_exp" = None, abs_Pure_exp72: "abs_Pure_exp" = None, abs_Pure_exp70: "abs_Pure_exp" = None, abs_Pure_exp45: "abs_Pure_exp_list" = None, abs_Pure_exp49: "abs_Pure_exp" = None, abs_Pure_exp47: "abs_Pure_exp" = None, abs_Pure_exp52: "abs_Pure_exp" = None, abs_Pure_exp50: "abs_Pure_exp" = None, abs_Pure_exp55: "abs_Pure_exp" = None, abs_Pure_exp53: "abs_Pure_exp" = None, abs_Pure_exp58: "abs_Pure_exp" = None, abs_Pure_exp56: "abs_Pure_exp" = None, abs_Pure_exp60: set["abs_Case_branch"] = None, abs_Pure_exp81: "abs_Pure_exp_list" = None, abs_Pure_exp88: "abs_Anon_function_decl" = None, abs_Pure_exp75: "abs_Pattern" = None, abs_Pure_exp103: "abs_Function_decl" = None, abs_Pure_exp139: "abs_Field_decl" = None, abs_Pure_exp153: "abs_Stmt" = None, abs_Pure_exp182: "abs_Stmt" = None, abs_Pure_exp185: "abs_Stmt" = None, abs_Pure_exp188: "abs_Stmt" = None, abs_Pure_exp191: "abs_Stmt" = None, abs_Pure_exp194: "abs_Stmt" = None, abs_Pure_exp197: "abs_Stmt" = None, abs_Pure_exp162: "abs_Stmt" = None, abs_Pure_exp168: "abs_Stmt" = None, abs_Pure_exp208: "abs_Guard" = None, abs_Pure_exp211: "abs_Guard" = None, abs_Pure_exp214: "abs_Guard" = None, abs_Pure_exp402: "abs_Or_expr" = None, abs_Pure_exp405: "abs_Or_expr" = None, abs_Pure_exp412: "abs_Equality_expr" = None, abs_Pure_exp415: "abs_Equality_expr" = None, abs_Pure_exp407: "abs_And_expr" = None, abs_Pure_exp410: "abs_And_expr" = None, abs_Pure_exp430: "abs_MulDivOrMod_expr" = None, abs_Pure_exp417: "abs_Comparison_expr" = None, abs_Pure_exp420: "abs_Comparison_expr" = None, abs_Pure_exp422: "abs_PlusOrMinus_expr" = None, abs_Pure_exp425: "abs_PlusOrMinus_expr" = None, abs_Pure_exp427: "abs_MulDivOrMod_expr" = None):
        self.value = value
        self.op = op
        self.await = await
        self.val = val
        self.abs_Pure_exp = abs_Pure_exp
        self.abs_Pure_exp41 = abs_Pure_exp41 if abs_Pure_exp41 is not None else set()
        self.abs_Pure_exp43 = abs_Pure_exp43
        self.abs_Pure_exp36 = abs_Pure_exp36
        self.abs_Pure_exp62 = abs_Pure_exp62
        self.abs_Pure_exp66 = abs_Pure_exp66
        self.abs_Pure_exp64 = abs_Pure_exp64
        self.abs_Pure_exp69 = abs_Pure_exp69
        self.abs_Pure_exp67 = abs_Pure_exp67
        self.abs_Pure_exp72 = abs_Pure_exp72
        self.abs_Pure_exp70 = abs_Pure_exp70
        self.abs_Pure_exp45 = abs_Pure_exp45
        self.abs_Pure_exp49 = abs_Pure_exp49
        self.abs_Pure_exp47 = abs_Pure_exp47
        self.abs_Pure_exp52 = abs_Pure_exp52
        self.abs_Pure_exp50 = abs_Pure_exp50
        self.abs_Pure_exp55 = abs_Pure_exp55
        self.abs_Pure_exp53 = abs_Pure_exp53
        self.abs_Pure_exp58 = abs_Pure_exp58
        self.abs_Pure_exp56 = abs_Pure_exp56
        self.abs_Pure_exp60 = abs_Pure_exp60 if abs_Pure_exp60 is not None else set()
        self.abs_Pure_exp81 = abs_Pure_exp81
        self.abs_Pure_exp88 = abs_Pure_exp88
        self.abs_Pure_exp75 = abs_Pure_exp75
        self.abs_Pure_exp103 = abs_Pure_exp103
        self.abs_Pure_exp139 = abs_Pure_exp139
        self.abs_Pure_exp153 = abs_Pure_exp153
        self.abs_Pure_exp182 = abs_Pure_exp182
        self.abs_Pure_exp185 = abs_Pure_exp185
        self.abs_Pure_exp188 = abs_Pure_exp188
        self.abs_Pure_exp191 = abs_Pure_exp191
        self.abs_Pure_exp194 = abs_Pure_exp194
        self.abs_Pure_exp197 = abs_Pure_exp197
        self.abs_Pure_exp162 = abs_Pure_exp162
        self.abs_Pure_exp168 = abs_Pure_exp168
        self.abs_Pure_exp208 = abs_Pure_exp208
        self.abs_Pure_exp211 = abs_Pure_exp211
        self.abs_Pure_exp214 = abs_Pure_exp214
        self.abs_Pure_exp402 = abs_Pure_exp402
        self.abs_Pure_exp405 = abs_Pure_exp405
        self.abs_Pure_exp412 = abs_Pure_exp412
        self.abs_Pure_exp415 = abs_Pure_exp415
        self.abs_Pure_exp407 = abs_Pure_exp407
        self.abs_Pure_exp410 = abs_Pure_exp410
        self.abs_Pure_exp430 = abs_Pure_exp430
        self.abs_Pure_exp417 = abs_Pure_exp417
        self.abs_Pure_exp420 = abs_Pure_exp420
        self.abs_Pure_exp422 = abs_Pure_exp422
        self.abs_Pure_exp425 = abs_Pure_exp425
        self.abs_Pure_exp427 = abs_Pure_exp427
        
    @property
    def await(self) -> str:
        return self.__await

    @await.setter
    def await(self, await: str):
        self.__await = await

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def abs_Pure_exp(self):
        return self.__abs_Pure_exp

    @abs_Pure_exp.setter
    def abs_Pure_exp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp", None)
        self.__abs_Pure_exp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Par_function_decl27"):
                opp_val = getattr(old_value, "abs_Par_function_decl27", None)
                if opp_val == self:
                    setattr(old_value, "abs_Par_function_decl27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Par_function_decl27"):
                opp_val = getattr(value, "abs_Par_function_decl27", None)
                setattr(value, "abs_Par_function_decl27", self)

    @property
    def abs_Pure_exp58(self):
        return self.__abs_Pure_exp58

    @abs_Pure_exp58.setter
    def abs_Pure_exp58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp58", None)
        self.__abs_Pure_exp58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp56"):
                opp_val = getattr(old_value, "abs_Pure_exp56", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp56"):
                opp_val = getattr(value, "abs_Pure_exp56", None)
                setattr(value, "abs_Pure_exp56", self)

    @property
    def abs_Pure_exp214(self):
        return self.__abs_Pure_exp214

    @abs_Pure_exp214.setter
    def abs_Pure_exp214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp214", None)
        self.__abs_Pure_exp214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard213"):
                opp_val = getattr(old_value, "abs_Guard213", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard213"):
                opp_val = getattr(value, "abs_Guard213", None)
                setattr(value, "abs_Guard213", self)

    @property
    def abs_Pure_exp53(self):
        return self.__abs_Pure_exp53

    @abs_Pure_exp53.setter
    def abs_Pure_exp53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp53", None)
        self.__abs_Pure_exp53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp55"):
                opp_val = getattr(old_value, "abs_Pure_exp55", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp55"):
                opp_val = getattr(value, "abs_Pure_exp55", None)
                setattr(value, "abs_Pure_exp55", self)

    @property
    def abs_Pure_exp88(self):
        return self.__abs_Pure_exp88

    @abs_Pure_exp88.setter
    def abs_Pure_exp88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp88", None)
        self.__abs_Pure_exp88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Anon_function_decl87"):
                opp_val = getattr(old_value, "abs_Anon_function_decl87", None)
                if opp_val == self:
                    setattr(old_value, "abs_Anon_function_decl87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Anon_function_decl87"):
                opp_val = getattr(value, "abs_Anon_function_decl87", None)
                setattr(value, "abs_Anon_function_decl87", self)

    @property
    def abs_Pure_exp415(self):
        return self.__abs_Pure_exp415

    @abs_Pure_exp415.setter
    def abs_Pure_exp415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp415", None)
        self.__abs_Pure_exp415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Equality_expr414"):
                opp_val = getattr(old_value, "abs_Equality_expr414", None)
                if opp_val == self:
                    setattr(old_value, "abs_Equality_expr414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Equality_expr414"):
                opp_val = getattr(value, "abs_Equality_expr414", None)
                setattr(value, "abs_Equality_expr414", self)

    @property
    def abs_Pure_exp430(self):
        return self.__abs_Pure_exp430

    @abs_Pure_exp430.setter
    def abs_Pure_exp430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp430", None)
        self.__abs_Pure_exp430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MulDivOrMod_expr429"):
                opp_val = getattr(old_value, "abs_MulDivOrMod_expr429", None)
                if opp_val == self:
                    setattr(old_value, "abs_MulDivOrMod_expr429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MulDivOrMod_expr429"):
                opp_val = getattr(value, "abs_MulDivOrMod_expr429", None)
                setattr(value, "abs_MulDivOrMod_expr429", self)

    @property
    def abs_Pure_exp103(self):
        return self.__abs_Pure_exp103

    @abs_Pure_exp103.setter
    def abs_Pure_exp103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp103", None)
        self.__abs_Pure_exp103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Function_decl102"):
                opp_val = getattr(old_value, "abs_Function_decl102", None)
                if opp_val == self:
                    setattr(old_value, "abs_Function_decl102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Function_decl102"):
                opp_val = getattr(value, "abs_Function_decl102", None)
                setattr(value, "abs_Function_decl102", self)

    @property
    def abs_Pure_exp153(self):
        return self.__abs_Pure_exp153

    @abs_Pure_exp153.setter
    def abs_Pure_exp153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp153", None)
        self.__abs_Pure_exp153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt152"):
                opp_val = getattr(old_value, "abs_Stmt152", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt152"):
                opp_val = getattr(value, "abs_Stmt152", None)
                setattr(value, "abs_Stmt152", self)

    @property
    def abs_Pure_exp47(self):
        return self.__abs_Pure_exp47

    @abs_Pure_exp47.setter
    def abs_Pure_exp47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp47", None)
        self.__abs_Pure_exp47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp49"):
                opp_val = getattr(old_value, "abs_Pure_exp49", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp49"):
                opp_val = getattr(value, "abs_Pure_exp49", None)
                setattr(value, "abs_Pure_exp49", self)

    @property
    def abs_Pure_exp168(self):
        return self.__abs_Pure_exp168

    @abs_Pure_exp168.setter
    def abs_Pure_exp168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp168", None)
        self.__abs_Pure_exp168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt167"):
                opp_val = getattr(old_value, "abs_Stmt167", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt167"):
                opp_val = getattr(value, "abs_Stmt167", None)
                setattr(value, "abs_Stmt167", self)

    @property
    def abs_Pure_exp50(self):
        return self.__abs_Pure_exp50

    @abs_Pure_exp50.setter
    def abs_Pure_exp50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp50", None)
        self.__abs_Pure_exp50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp52"):
                opp_val = getattr(old_value, "abs_Pure_exp52", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp52"):
                opp_val = getattr(value, "abs_Pure_exp52", None)
                setattr(value, "abs_Pure_exp52", self)

    @property
    def abs_Pure_exp425(self):
        return self.__abs_Pure_exp425

    @abs_Pure_exp425.setter
    def abs_Pure_exp425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp425", None)
        self.__abs_Pure_exp425 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_PlusOrMinus_expr424"):
                opp_val = getattr(old_value, "abs_PlusOrMinus_expr424", None)
                if opp_val == self:
                    setattr(old_value, "abs_PlusOrMinus_expr424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_PlusOrMinus_expr424"):
                opp_val = getattr(value, "abs_PlusOrMinus_expr424", None)
                setattr(value, "abs_PlusOrMinus_expr424", self)

    @property
    def abs_Pure_exp194(self):
        return self.__abs_Pure_exp194

    @abs_Pure_exp194.setter
    def abs_Pure_exp194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp194", None)
        self.__abs_Pure_exp194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt193"):
                opp_val = getattr(old_value, "abs_Stmt193", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt193"):
                opp_val = getattr(value, "abs_Stmt193", None)
                setattr(value, "abs_Stmt193", self)

    @property
    def abs_Pure_exp69(self):
        return self.__abs_Pure_exp69

    @abs_Pure_exp69.setter
    def abs_Pure_exp69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp69", None)
        self.__abs_Pure_exp69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp67"):
                opp_val = getattr(old_value, "abs_Pure_exp67", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp67"):
                opp_val = getattr(value, "abs_Pure_exp67", None)
                setattr(value, "abs_Pure_exp67", self)

    @property
    def abs_Pure_exp43(self):
        return self.__abs_Pure_exp43

    @abs_Pure_exp43.setter
    def abs_Pure_exp43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp43", None)
        self.__abs_Pure_exp43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp_list"):
                opp_val = getattr(old_value, "abs_Pure_exp_list", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp_list"):
                opp_val = getattr(value, "abs_Pure_exp_list", None)
                setattr(value, "abs_Pure_exp_list", self)

    @property
    def abs_Pure_exp422(self):
        return self.__abs_Pure_exp422

    @abs_Pure_exp422.setter
    def abs_Pure_exp422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp422", None)
        self.__abs_Pure_exp422 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_PlusOrMinus_expr"):
                opp_val = getattr(old_value, "abs_PlusOrMinus_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_PlusOrMinus_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_PlusOrMinus_expr"):
                opp_val = getattr(value, "abs_PlusOrMinus_expr", None)
                setattr(value, "abs_PlusOrMinus_expr", self)

    @property
    def abs_Pure_exp64(self):
        return self.__abs_Pure_exp64

    @abs_Pure_exp64.setter
    def abs_Pure_exp64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp64", None)
        self.__abs_Pure_exp64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp66"):
                opp_val = getattr(old_value, "abs_Pure_exp66", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp66"):
                opp_val = getattr(value, "abs_Pure_exp66", None)
                setattr(value, "abs_Pure_exp66", self)

    @property
    def abs_Pure_exp407(self):
        return self.__abs_Pure_exp407

    @abs_Pure_exp407.setter
    def abs_Pure_exp407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp407", None)
        self.__abs_Pure_exp407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_And_expr"):
                opp_val = getattr(old_value, "abs_And_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_And_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_And_expr"):
                opp_val = getattr(value, "abs_And_expr", None)
                setattr(value, "abs_And_expr", self)

    @property
    def abs_Pure_exp72(self):
        return self.__abs_Pure_exp72

    @abs_Pure_exp72.setter
    def abs_Pure_exp72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp72", None)
        self.__abs_Pure_exp72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp70"):
                opp_val = getattr(old_value, "abs_Pure_exp70", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp70"):
                opp_val = getattr(value, "abs_Pure_exp70", None)
                setattr(value, "abs_Pure_exp70", self)

    @property
    def abs_Pure_exp66(self):
        return self.__abs_Pure_exp66

    @abs_Pure_exp66.setter
    def abs_Pure_exp66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp66", None)
        self.__abs_Pure_exp66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp64"):
                opp_val = getattr(old_value, "abs_Pure_exp64", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp64"):
                opp_val = getattr(value, "abs_Pure_exp64", None)
                setattr(value, "abs_Pure_exp64", self)

    @property
    def abs_Pure_exp188(self):
        return self.__abs_Pure_exp188

    @abs_Pure_exp188.setter
    def abs_Pure_exp188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp188", None)
        self.__abs_Pure_exp188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt187"):
                opp_val = getattr(old_value, "abs_Stmt187", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt187"):
                opp_val = getattr(value, "abs_Stmt187", None)
                setattr(value, "abs_Stmt187", self)

    @property
    def abs_Pure_exp405(self):
        return self.__abs_Pure_exp405

    @abs_Pure_exp405.setter
    def abs_Pure_exp405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp405", None)
        self.__abs_Pure_exp405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Or_expr404"):
                opp_val = getattr(old_value, "abs_Or_expr404", None)
                if opp_val == self:
                    setattr(old_value, "abs_Or_expr404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Or_expr404"):
                opp_val = getattr(value, "abs_Or_expr404", None)
                setattr(value, "abs_Or_expr404", self)

    @property
    def abs_Pure_exp420(self):
        return self.__abs_Pure_exp420

    @abs_Pure_exp420.setter
    def abs_Pure_exp420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp420", None)
        self.__abs_Pure_exp420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Comparison_expr419"):
                opp_val = getattr(old_value, "abs_Comparison_expr419", None)
                if opp_val == self:
                    setattr(old_value, "abs_Comparison_expr419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Comparison_expr419"):
                opp_val = getattr(value, "abs_Comparison_expr419", None)
                setattr(value, "abs_Comparison_expr419", self)

    @property
    def abs_Pure_exp60(self):
        return self.__abs_Pure_exp60

    @abs_Pure_exp60.setter
    def abs_Pure_exp60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp60", None)
        self.__abs_Pure_exp60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Case_branch"):
                    opp_val = getattr(item, "abs_Case_branch", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Case_branch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Case_branch"):
                    opp_val = getattr(item, "abs_Case_branch", None)
                    
                    setattr(item, "abs_Case_branch", self)
                    

    @property
    def abs_Pure_exp185(self):
        return self.__abs_Pure_exp185

    @abs_Pure_exp185.setter
    def abs_Pure_exp185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp185", None)
        self.__abs_Pure_exp185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt184"):
                opp_val = getattr(old_value, "abs_Stmt184", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt184"):
                opp_val = getattr(value, "abs_Stmt184", None)
                setattr(value, "abs_Stmt184", self)

    @property
    def abs_Pure_exp75(self):
        return self.__abs_Pure_exp75

    @abs_Pure_exp75.setter
    def abs_Pure_exp75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp75", None)
        self.__abs_Pure_exp75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pattern"):
                opp_val = getattr(old_value, "abs_Pattern", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pattern"):
                opp_val = getattr(value, "abs_Pattern", None)
                setattr(value, "abs_Pattern", self)

    @property
    def abs_Pure_exp427(self):
        return self.__abs_Pure_exp427

    @abs_Pure_exp427.setter
    def abs_Pure_exp427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp427", None)
        self.__abs_Pure_exp427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_MulDivOrMod_expr"):
                opp_val = getattr(old_value, "abs_MulDivOrMod_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_MulDivOrMod_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_MulDivOrMod_expr"):
                opp_val = getattr(value, "abs_MulDivOrMod_expr", None)
                setattr(value, "abs_MulDivOrMod_expr", self)

    @property
    def abs_Pure_exp45(self):
        return self.__abs_Pure_exp45

    @abs_Pure_exp45.setter
    def abs_Pure_exp45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp45", None)
        self.__abs_Pure_exp45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp_list46"):
                opp_val = getattr(old_value, "abs_Pure_exp_list46", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp_list46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp_list46"):
                opp_val = getattr(value, "abs_Pure_exp_list46", None)
                setattr(value, "abs_Pure_exp_list46", self)

    @property
    def abs_Pure_exp162(self):
        return self.__abs_Pure_exp162

    @abs_Pure_exp162.setter
    def abs_Pure_exp162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp162", None)
        self.__abs_Pure_exp162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt161"):
                opp_val = getattr(old_value, "abs_Stmt161", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt161"):
                opp_val = getattr(value, "abs_Stmt161", None)
                setattr(value, "abs_Stmt161", self)

    @property
    def abs_Pure_exp410(self):
        return self.__abs_Pure_exp410

    @abs_Pure_exp410.setter
    def abs_Pure_exp410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp410", None)
        self.__abs_Pure_exp410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_And_expr409"):
                opp_val = getattr(old_value, "abs_And_expr409", None)
                if opp_val == self:
                    setattr(old_value, "abs_And_expr409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_And_expr409"):
                opp_val = getattr(value, "abs_And_expr409", None)
                setattr(value, "abs_And_expr409", self)

    @property
    def abs_Pure_exp62(self):
        return self.__abs_Pure_exp62

    @abs_Pure_exp62.setter
    def abs_Pure_exp62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp62", None)
        self.__abs_Pure_exp62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use63"):
                opp_val = getattr(old_value, "abs_Type_use63", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_use63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use63"):
                opp_val = getattr(value, "abs_Type_use63", None)
                setattr(value, "abs_Type_use63", self)

    @property
    def abs_Pure_exp56(self):
        return self.__abs_Pure_exp56

    @abs_Pure_exp56.setter
    def abs_Pure_exp56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp56", None)
        self.__abs_Pure_exp56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp58"):
                opp_val = getattr(old_value, "abs_Pure_exp58", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp58"):
                opp_val = getattr(value, "abs_Pure_exp58", None)
                setattr(value, "abs_Pure_exp58", self)

    @property
    def abs_Pure_exp81(self):
        return self.__abs_Pure_exp81

    @abs_Pure_exp81.setter
    def abs_Pure_exp81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp81", None)
        self.__abs_Pure_exp81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp_list80"):
                opp_val = getattr(old_value, "abs_Pure_exp_list80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp_list80"):
                opp_val = getattr(value, "abs_Pure_exp_list80", None)
                if opp_val is None:
                    setattr(value, "abs_Pure_exp_list80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Pure_exp211(self):
        return self.__abs_Pure_exp211

    @abs_Pure_exp211.setter
    def abs_Pure_exp211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp211", None)
        self.__abs_Pure_exp211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard210"):
                opp_val = getattr(old_value, "abs_Guard210", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard210"):
                opp_val = getattr(value, "abs_Guard210", None)
                setattr(value, "abs_Guard210", self)

    @property
    def abs_Pure_exp412(self):
        return self.__abs_Pure_exp412

    @abs_Pure_exp412.setter
    def abs_Pure_exp412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp412", None)
        self.__abs_Pure_exp412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Equality_expr"):
                opp_val = getattr(old_value, "abs_Equality_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_Equality_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Equality_expr"):
                opp_val = getattr(value, "abs_Equality_expr", None)
                setattr(value, "abs_Equality_expr", self)

    @property
    def abs_Pure_exp67(self):
        return self.__abs_Pure_exp67

    @abs_Pure_exp67.setter
    def abs_Pure_exp67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp67", None)
        self.__abs_Pure_exp67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp69"):
                opp_val = getattr(old_value, "abs_Pure_exp69", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp69"):
                opp_val = getattr(value, "abs_Pure_exp69", None)
                setattr(value, "abs_Pure_exp69", self)

    @property
    def abs_Pure_exp52(self):
        return self.__abs_Pure_exp52

    @abs_Pure_exp52.setter
    def abs_Pure_exp52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp52", None)
        self.__abs_Pure_exp52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp50"):
                opp_val = getattr(old_value, "abs_Pure_exp50", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp50"):
                opp_val = getattr(value, "abs_Pure_exp50", None)
                setattr(value, "abs_Pure_exp50", self)

    @property
    def abs_Pure_exp55(self):
        return self.__abs_Pure_exp55

    @abs_Pure_exp55.setter
    def abs_Pure_exp55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp55", None)
        self.__abs_Pure_exp55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp53"):
                opp_val = getattr(old_value, "abs_Pure_exp53", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp53"):
                opp_val = getattr(value, "abs_Pure_exp53", None)
                setattr(value, "abs_Pure_exp53", self)

    @property
    def abs_Pure_exp417(self):
        return self.__abs_Pure_exp417

    @abs_Pure_exp417.setter
    def abs_Pure_exp417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp417", None)
        self.__abs_Pure_exp417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Comparison_expr"):
                opp_val = getattr(old_value, "abs_Comparison_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_Comparison_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Comparison_expr"):
                opp_val = getattr(value, "abs_Comparison_expr", None)
                setattr(value, "abs_Comparison_expr", self)

    @property
    def abs_Pure_exp49(self):
        return self.__abs_Pure_exp49

    @abs_Pure_exp49.setter
    def abs_Pure_exp49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp49", None)
        self.__abs_Pure_exp49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp47"):
                opp_val = getattr(old_value, "abs_Pure_exp47", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp47"):
                opp_val = getattr(value, "abs_Pure_exp47", None)
                setattr(value, "abs_Pure_exp47", self)

    @property
    def abs_Pure_exp402(self):
        return self.__abs_Pure_exp402

    @abs_Pure_exp402.setter
    def abs_Pure_exp402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp402", None)
        self.__abs_Pure_exp402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Or_expr"):
                opp_val = getattr(old_value, "abs_Or_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_Or_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Or_expr"):
                opp_val = getattr(value, "abs_Or_expr", None)
                setattr(value, "abs_Or_expr", self)

    @property
    def abs_Pure_exp41(self):
        return self.__abs_Pure_exp41

    @abs_Pure_exp41.setter
    def abs_Pure_exp41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp41", None)
        self.__abs_Pure_exp41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Function_list"):
                    opp_val = getattr(item, "abs_Function_list", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Function_list", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Function_list"):
                    opp_val = getattr(item, "abs_Function_list", None)
                    
                    setattr(item, "abs_Function_list", self)
                    

    @property
    def abs_Pure_exp70(self):
        return self.__abs_Pure_exp70

    @abs_Pure_exp70.setter
    def abs_Pure_exp70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp70", None)
        self.__abs_Pure_exp70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp72"):
                opp_val = getattr(old_value, "abs_Pure_exp72", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp72"):
                opp_val = getattr(value, "abs_Pure_exp72", None)
                setattr(value, "abs_Pure_exp72", self)

    @property
    def abs_Pure_exp182(self):
        return self.__abs_Pure_exp182

    @abs_Pure_exp182.setter
    def abs_Pure_exp182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp182", None)
        self.__abs_Pure_exp182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt181"):
                opp_val = getattr(old_value, "abs_Stmt181", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt181"):
                opp_val = getattr(value, "abs_Stmt181", None)
                setattr(value, "abs_Stmt181", self)

    @property
    def abs_Pure_exp191(self):
        return self.__abs_Pure_exp191

    @abs_Pure_exp191.setter
    def abs_Pure_exp191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp191", None)
        self.__abs_Pure_exp191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt190"):
                opp_val = getattr(old_value, "abs_Stmt190", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt190"):
                opp_val = getattr(value, "abs_Stmt190", None)
                setattr(value, "abs_Stmt190", self)

    @property
    def abs_Pure_exp36(self):
        return self.__abs_Pure_exp36

    @abs_Pure_exp36.setter
    def abs_Pure_exp36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp36", None)
        self.__abs_Pure_exp36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Annotation35"):
                opp_val = getattr(old_value, "abs_Annotation35", None)
                if opp_val == self:
                    setattr(old_value, "abs_Annotation35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Annotation35"):
                opp_val = getattr(value, "abs_Annotation35", None)
                setattr(value, "abs_Annotation35", self)

    @property
    def abs_Pure_exp197(self):
        return self.__abs_Pure_exp197

    @abs_Pure_exp197.setter
    def abs_Pure_exp197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp197", None)
        self.__abs_Pure_exp197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Stmt196"):
                opp_val = getattr(old_value, "abs_Stmt196", None)
                if opp_val == self:
                    setattr(old_value, "abs_Stmt196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Stmt196"):
                opp_val = getattr(value, "abs_Stmt196", None)
                setattr(value, "abs_Stmt196", self)

    @property
    def abs_Pure_exp208(self):
        return self.__abs_Pure_exp208

    @abs_Pure_exp208.setter
    def abs_Pure_exp208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp208", None)
        self.__abs_Pure_exp208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Guard207"):
                opp_val = getattr(old_value, "abs_Guard207", None)
                if opp_val == self:
                    setattr(old_value, "abs_Guard207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Guard207"):
                opp_val = getattr(value, "abs_Guard207", None)
                setattr(value, "abs_Guard207", self)

    @property
    def abs_Pure_exp139(self):
        return self.__abs_Pure_exp139

    @abs_Pure_exp139.setter
    def abs_Pure_exp139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Pure_exp__abs_Pure_exp139", None)
        self.__abs_Pure_exp139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Field_decl138"):
                opp_val = getattr(old_value, "abs_Field_decl138", None)
                if opp_val == self:
                    setattr(old_value, "abs_Field_decl138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Field_decl138"):
                opp_val = getattr(value, "abs_Field_decl138", None)
                setattr(value, "abs_Field_decl138", self)

class abs_Param_list:

    pass
class abs_Function_name_list:

    pass
class abs_Type_use(Data_constructor_arg, Annotation):

    def __init__(self, name: str, abs_Type_use: "abs_Par_function_decl" = None, abs_Type_use39: "abs_Type_use" = None, abs_Type_use37: set["abs_Type_use"] = None, abs_Type_use63: "abs_Pure_exp" = None, abs_Type_use105: "abs_Typesyn_decl" = None, abs_Type_use114: "abs_Methodsig" = None, abs_Type_use95: "abs_Type_exp" = None, abs_Type_use97: "abs_Function_decl" = None, abs_Type_use136: "abs_Field_decl" = None, abs_Type_use250: "abs_Method" = None):
        self.name = name
        self.abs_Type_use = abs_Type_use
        self.abs_Type_use39 = abs_Type_use39
        self.abs_Type_use37 = abs_Type_use37 if abs_Type_use37 is not None else set()
        self.abs_Type_use63 = abs_Type_use63
        self.abs_Type_use105 = abs_Type_use105
        self.abs_Type_use114 = abs_Type_use114
        self.abs_Type_use95 = abs_Type_use95
        self.abs_Type_use97 = abs_Type_use97
        self.abs_Type_use136 = abs_Type_use136
        self.abs_Type_use250 = abs_Type_use250
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Type_use(self):
        return self.__abs_Type_use

    @abs_Type_use.setter
    def abs_Type_use(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use", None)
        self.__abs_Type_use = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Par_function_decl"):
                opp_val = getattr(old_value, "abs_Par_function_decl", None)
                if opp_val == self:
                    setattr(old_value, "abs_Par_function_decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Par_function_decl"):
                opp_val = getattr(value, "abs_Par_function_decl", None)
                setattr(value, "abs_Par_function_decl", self)

    @property
    def abs_Type_use105(self):
        return self.__abs_Type_use105

    @abs_Type_use105.setter
    def abs_Type_use105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use105", None)
        self.__abs_Type_use105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Typesyn_decl"):
                opp_val = getattr(old_value, "abs_Typesyn_decl", None)
                if opp_val == self:
                    setattr(old_value, "abs_Typesyn_decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Typesyn_decl"):
                opp_val = getattr(value, "abs_Typesyn_decl", None)
                setattr(value, "abs_Typesyn_decl", self)

    @property
    def abs_Type_use63(self):
        return self.__abs_Type_use63

    @abs_Type_use63.setter
    def abs_Type_use63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use63", None)
        self.__abs_Type_use63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp62"):
                opp_val = getattr(old_value, "abs_Pure_exp62", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp62"):
                opp_val = getattr(value, "abs_Pure_exp62", None)
                setattr(value, "abs_Pure_exp62", self)

    @property
    def abs_Type_use114(self):
        return self.__abs_Type_use114

    @abs_Type_use114.setter
    def abs_Type_use114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use114", None)
        self.__abs_Type_use114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Methodsig113"):
                opp_val = getattr(old_value, "abs_Methodsig113", None)
                if opp_val == self:
                    setattr(old_value, "abs_Methodsig113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Methodsig113"):
                opp_val = getattr(value, "abs_Methodsig113", None)
                setattr(value, "abs_Methodsig113", self)

    @property
    def abs_Type_use136(self):
        return self.__abs_Type_use136

    @abs_Type_use136.setter
    def abs_Type_use136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use136", None)
        self.__abs_Type_use136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Field_decl135"):
                opp_val = getattr(old_value, "abs_Field_decl135", None)
                if opp_val == self:
                    setattr(old_value, "abs_Field_decl135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Field_decl135"):
                opp_val = getattr(value, "abs_Field_decl135", None)
                setattr(value, "abs_Field_decl135", self)

    @property
    def abs_Type_use37(self):
        return self.__abs_Type_use37

    @abs_Type_use37.setter
    def abs_Type_use37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use37", None)
        self.__abs_Type_use37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Type_use39"):
                    opp_val = getattr(item, "abs_Type_use39", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Type_use39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Type_use39"):
                    opp_val = getattr(item, "abs_Type_use39", None)
                    
                    setattr(item, "abs_Type_use39", self)
                    

    @property
    def abs_Type_use250(self):
        return self.__abs_Type_use250

    @abs_Type_use250.setter
    def abs_Type_use250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use250", None)
        self.__abs_Type_use250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Method249"):
                opp_val = getattr(old_value, "abs_Method249", None)
                if opp_val == self:
                    setattr(old_value, "abs_Method249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Method249"):
                opp_val = getattr(value, "abs_Method249", None)
                setattr(value, "abs_Method249", self)

    @property
    def abs_Type_use39(self):
        return self.__abs_Type_use39

    @abs_Type_use39.setter
    def abs_Type_use39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use39", None)
        self.__abs_Type_use39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use37"):
                opp_val = getattr(old_value, "abs_Type_use37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use37"):
                opp_val = getattr(value, "abs_Type_use37", None)
                if opp_val is None:
                    setattr(value, "abs_Type_use37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Type_use95(self):
        return self.__abs_Type_use95

    @abs_Type_use95.setter
    def abs_Type_use95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use95", None)
        self.__abs_Type_use95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_exp94"):
                opp_val = getattr(old_value, "abs_Type_exp94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_exp94"):
                opp_val = getattr(value, "abs_Type_exp94", None)
                if opp_val is None:
                    setattr(value, "abs_Type_exp94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Type_use97(self):
        return self.__abs_Type_use97

    @abs_Type_use97.setter
    def abs_Type_use97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Type_use__abs_Type_use97", None)
        self.__abs_Type_use97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Function_decl"):
                opp_val = getattr(old_value, "abs_Function_decl", None)
                if opp_val == self:
                    setattr(old_value, "abs_Function_decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Function_decl"):
                opp_val = getattr(value, "abs_Function_decl", None)
                setattr(value, "abs_Function_decl", self)

class Decl:

    pass
class abs_Interface_decl(Decl):

    pass
class abs_Trait_decl(Decl):

    pass
class abs_Class_decl(Decl):

    pass
class abs_Exception_decl(Decl):

    pass
class abs_Par_function_decl(Decl):

    def __init__(self, p: str, abs_Par_function_decl: "abs_Type_use" = None, abs_Par_function_decl23: "abs_Function_name_list" = None, abs_Par_function_decl25: "abs_Param_list" = None, abs_Par_function_decl27: "abs_Pure_exp" = None):
        self.p = p
        self.abs_Par_function_decl = abs_Par_function_decl
        self.abs_Par_function_decl23 = abs_Par_function_decl23
        self.abs_Par_function_decl25 = abs_Par_function_decl25
        self.abs_Par_function_decl27 = abs_Par_function_decl27
        
    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

    @property
    def abs_Par_function_decl(self):
        return self.__abs_Par_function_decl

    @abs_Par_function_decl.setter
    def abs_Par_function_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Par_function_decl__abs_Par_function_decl", None)
        self.__abs_Par_function_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use"):
                opp_val = getattr(old_value, "abs_Type_use", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_use", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use"):
                opp_val = getattr(value, "abs_Type_use", None)
                setattr(value, "abs_Type_use", self)

    @property
    def abs_Par_function_decl23(self):
        return self.__abs_Par_function_decl23

    @abs_Par_function_decl23.setter
    def abs_Par_function_decl23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Par_function_decl__abs_Par_function_decl23", None)
        self.__abs_Par_function_decl23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Function_name_list"):
                opp_val = getattr(old_value, "abs_Function_name_list", None)
                if opp_val == self:
                    setattr(old_value, "abs_Function_name_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Function_name_list"):
                opp_val = getattr(value, "abs_Function_name_list", None)
                setattr(value, "abs_Function_name_list", self)

    @property
    def abs_Par_function_decl25(self):
        return self.__abs_Par_function_decl25

    @abs_Par_function_decl25.setter
    def abs_Par_function_decl25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Par_function_decl__abs_Par_function_decl25", None)
        self.__abs_Par_function_decl25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Param_list"):
                opp_val = getattr(old_value, "abs_Param_list", None)
                if opp_val == self:
                    setattr(old_value, "abs_Param_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Param_list"):
                opp_val = getattr(value, "abs_Param_list", None)
                setattr(value, "abs_Param_list", self)

    @property
    def abs_Par_function_decl27(self):
        return self.__abs_Par_function_decl27

    @abs_Par_function_decl27.setter
    def abs_Par_function_decl27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Par_function_decl__abs_Par_function_decl27", None)
        self.__abs_Par_function_decl27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp"):
                opp_val = getattr(old_value, "abs_Pure_exp", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp"):
                opp_val = getattr(value, "abs_Pure_exp", None)
                setattr(value, "abs_Pure_exp", self)

class abs_Data_constructor:

    def __init__(self, name: str, abs_Data_constructor: "abs_DataType_decl" = None, abs_Data_constructor32: set["abs_Data_constructor_arg"] = None):
        self.name = name
        self.abs_Data_constructor = abs_Data_constructor
        self.abs_Data_constructor32 = abs_Data_constructor32 if abs_Data_constructor32 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Data_constructor(self):
        return self.__abs_Data_constructor

    @abs_Data_constructor.setter
    def abs_Data_constructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Data_constructor__abs_Data_constructor", None)
        self.__abs_Data_constructor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_DataType_decl"):
                opp_val = getattr(old_value, "abs_DataType_decl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_DataType_decl"):
                opp_val = getattr(value, "abs_DataType_decl", None)
                if opp_val is None:
                    setattr(value, "abs_DataType_decl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Data_constructor32(self):
        return self.__abs_Data_constructor32

    @abs_Data_constructor32.setter
    def abs_Data_constructor32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Data_constructor__abs_Data_constructor32", None)
        self.__abs_Data_constructor32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Data_constructor_arg"):
                    opp_val = getattr(item, "abs_Data_constructor_arg", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Data_constructor_arg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Data_constructor_arg"):
                    opp_val = getattr(item, "abs_Data_constructor_arg", None)
                    
                    setattr(item, "abs_Data_constructor_arg", self)
                    

class Functional_modifier:

    pass
class abs_Typesyn_decl(Decl, Functional_modifier):

    pass
class abs_Function_decl(Decl, Functional_modifier):

    def __init__(self, p: str, abs_Function_decl: "abs_Type_use" = None, abs_Function_decl99: "abs_Param_list" = None, abs_Function_decl102: "abs_Pure_exp" = None):
        self.p = p
        self.abs_Function_decl = abs_Function_decl
        self.abs_Function_decl99 = abs_Function_decl99
        self.abs_Function_decl102 = abs_Function_decl102
        
    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

    @property
    def abs_Function_decl102(self):
        return self.__abs_Function_decl102

    @abs_Function_decl102.setter
    def abs_Function_decl102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Function_decl__abs_Function_decl102", None)
        self.__abs_Function_decl102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Pure_exp103"):
                opp_val = getattr(old_value, "abs_Pure_exp103", None)
                if opp_val == self:
                    setattr(old_value, "abs_Pure_exp103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Pure_exp103"):
                opp_val = getattr(value, "abs_Pure_exp103", None)
                setattr(value, "abs_Pure_exp103", self)

    @property
    def abs_Function_decl99(self):
        return self.__abs_Function_decl99

    @abs_Function_decl99.setter
    def abs_Function_decl99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Function_decl__abs_Function_decl99", None)
        self.__abs_Function_decl99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Param_list100"):
                opp_val = getattr(old_value, "abs_Param_list100", None)
                if opp_val == self:
                    setattr(old_value, "abs_Param_list100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Param_list100"):
                opp_val = getattr(value, "abs_Param_list100", None)
                setattr(value, "abs_Param_list100", self)

    @property
    def abs_Function_decl(self):
        return self.__abs_Function_decl

    @abs_Function_decl.setter
    def abs_Function_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Function_decl__abs_Function_decl", None)
        self.__abs_Function_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Type_use97"):
                opp_val = getattr(old_value, "abs_Type_use97", None)
                if opp_val == self:
                    setattr(old_value, "abs_Type_use97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Type_use97"):
                opp_val = getattr(value, "abs_Type_use97", None)
                setattr(value, "abs_Type_use97", self)

class abs_DataType_decl(Decl, Functional_modifier):

    def __init__(self, p: str, abs_DataType_decl: set["abs_Data_constructor"] = None):
        self.p = p
        self.abs_DataType_decl = abs_DataType_decl if abs_DataType_decl is not None else set()
        
    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

    @property
    def abs_DataType_decl(self):
        return self.__abs_DataType_decl

    @abs_DataType_decl.setter
    def abs_DataType_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_DataType_decl__abs_DataType_decl", None)
        self.__abs_DataType_decl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Data_constructor"):
                    opp_val = getattr(item, "abs_Data_constructor", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Data_constructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Data_constructor"):
                    opp_val = getattr(item, "abs_Data_constructor", None)
                    
                    setattr(item, "abs_Data_constructor", self)
                    

class abs_Function_name_decl:

    def __init__(self, name: str, abs_Function_name_decl: "abs_Function_name_list" = None):
        self.name = name
        self.abs_Function_name_decl = abs_Function_name_decl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Function_name_decl(self):
        return self.__abs_Function_name_decl

    @abs_Function_name_decl.setter
    def abs_Function_name_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Function_name_decl__abs_Function_name_decl", None)
        self.__abs_Function_name_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Function_name_list29"):
                opp_val = getattr(old_value, "abs_Function_name_list29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Function_name_list29"):
                opp_val = getattr(value, "abs_Function_name_list29", None)
                if opp_val is None:
                    setattr(value, "abs_Function_name_list29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Main_block:

    pass
class abs_Decl:

    def __init__(self, name: str, abs_Decl: "abs_Module_decl" = None):
        self.name = name
        self.abs_Decl = abs_Decl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Decl(self):
        return self.__abs_Decl

    @abs_Decl.setter
    def abs_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Decl__abs_Decl", None)
        self.__abs_Decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Module_decl18"):
                opp_val = getattr(old_value, "abs_Module_decl18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Module_decl18"):
                opp_val = getattr(value, "abs_Module_decl18", None)
                if opp_val is None:
                    setattr(value, "abs_Module_decl18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Fextension:

    def __init__(self, name: str, abs_Fextension: "abs_Compilation_Unit" = None, abs_Fextension396: set["abs_Feature_decl_attribute"] = None, abs_Fextension399: set["abs_Feature_decl_constraint"] = None, abs_Fextension393: "abs_Feature_decl_group" = None):
        self.name = name
        self.abs_Fextension = abs_Fextension
        self.abs_Fextension396 = abs_Fextension396 if abs_Fextension396 is not None else set()
        self.abs_Fextension399 = abs_Fextension399 if abs_Fextension399 is not None else set()
        self.abs_Fextension393 = abs_Fextension393
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Fextension(self):
        return self.__abs_Fextension

    @abs_Fextension.setter
    def abs_Fextension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Fextension__abs_Fextension", None)
        self.__abs_Fextension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit12"):
                opp_val = getattr(old_value, "abs_Compilation_Unit12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit12"):
                opp_val = getattr(value, "abs_Compilation_Unit12", None)
                if opp_val is None:
                    setattr(value, "abs_Compilation_Unit12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Fextension393(self):
        return self.__abs_Fextension393

    @abs_Fextension393.setter
    def abs_Fextension393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Fextension__abs_Fextension393", None)
        self.__abs_Fextension393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Feature_decl_group394"):
                opp_val = getattr(old_value, "abs_Feature_decl_group394", None)
                if opp_val == self:
                    setattr(old_value, "abs_Feature_decl_group394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Feature_decl_group394"):
                opp_val = getattr(value, "abs_Feature_decl_group394", None)
                setattr(value, "abs_Feature_decl_group394", self)

    @property
    def abs_Fextension396(self):
        return self.__abs_Fextension396

    @abs_Fextension396.setter
    def abs_Fextension396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Fextension__abs_Fextension396", None)
        self.__abs_Fextension396 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Feature_decl_attribute397"):
                    opp_val = getattr(item, "abs_Feature_decl_attribute397", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Feature_decl_attribute397", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Feature_decl_attribute397"):
                    opp_val = getattr(item, "abs_Feature_decl_attribute397", None)
                    
                    setattr(item, "abs_Feature_decl_attribute397", self)
                    

    @property
    def abs_Fextension399(self):
        return self.__abs_Fextension399

    @abs_Fextension399.setter
    def abs_Fextension399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Fextension__abs_Fextension399", None)
        self.__abs_Fextension399 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Feature_decl_constraint400"):
                    opp_val = getattr(item, "abs_Feature_decl_constraint400", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Feature_decl_constraint400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Feature_decl_constraint400"):
                    opp_val = getattr(item, "abs_Feature_decl_constraint400", None)
                    
                    setattr(item, "abs_Feature_decl_constraint400", self)
                    

class abs_Feature_decl(Fnode):

    def __init__(self, name: str, abs_Feature_decl: "abs_Compilation_Unit" = None, abs_Feature_decl331: "abs_Feature" = None, abs_Feature_decl370: "abs_Product_expr" = None, abs_Feature_decl383: "abs_Feature_decl_group" = None, abs_Feature_decl385: set["abs_Feature_decl_attribute"] = None, abs_Feature_decl387: set["abs_Feature_decl_constraint"] = None):
        self.name = name
        self.abs_Feature_decl = abs_Feature_decl
        self.abs_Feature_decl331 = abs_Feature_decl331
        self.abs_Feature_decl370 = abs_Feature_decl370
        self.abs_Feature_decl383 = abs_Feature_decl383
        self.abs_Feature_decl385 = abs_Feature_decl385 if abs_Feature_decl385 is not None else set()
        self.abs_Feature_decl387 = abs_Feature_decl387 if abs_Feature_decl387 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Feature_decl331(self):
        return self.__abs_Feature_decl331

    @abs_Feature_decl331.setter
    def abs_Feature_decl331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl__abs_Feature_decl331", None)
        self.__abs_Feature_decl331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Feature330"):
                opp_val = getattr(old_value, "abs_Feature330", None)
                if opp_val == self:
                    setattr(old_value, "abs_Feature330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Feature330"):
                opp_val = getattr(value, "abs_Feature330", None)
                setattr(value, "abs_Feature330", self)

    @property
    def abs_Feature_decl385(self):
        return self.__abs_Feature_decl385

    @abs_Feature_decl385.setter
    def abs_Feature_decl385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl__abs_Feature_decl385", None)
        self.__abs_Feature_decl385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Feature_decl_attribute"):
                    opp_val = getattr(item, "abs_Feature_decl_attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Feature_decl_attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Feature_decl_attribute"):
                    opp_val = getattr(item, "abs_Feature_decl_attribute", None)
                    
                    setattr(item, "abs_Feature_decl_attribute", self)
                    

    @property
    def abs_Feature_decl383(self):
        return self.__abs_Feature_decl383

    @abs_Feature_decl383.setter
    def abs_Feature_decl383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl__abs_Feature_decl383", None)
        self.__abs_Feature_decl383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Feature_decl_group"):
                opp_val = getattr(old_value, "abs_Feature_decl_group", None)
                if opp_val == self:
                    setattr(old_value, "abs_Feature_decl_group", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Feature_decl_group"):
                opp_val = getattr(value, "abs_Feature_decl_group", None)
                setattr(value, "abs_Feature_decl_group", self)

    @property
    def abs_Feature_decl387(self):
        return self.__abs_Feature_decl387

    @abs_Feature_decl387.setter
    def abs_Feature_decl387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl__abs_Feature_decl387", None)
        self.__abs_Feature_decl387 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Feature_decl_constraint"):
                    opp_val = getattr(item, "abs_Feature_decl_constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Feature_decl_constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Feature_decl_constraint"):
                    opp_val = getattr(item, "abs_Feature_decl_constraint", None)
                    
                    setattr(item, "abs_Feature_decl_constraint", self)
                    

    @property
    def abs_Feature_decl(self):
        return self.__abs_Feature_decl

    @abs_Feature_decl.setter
    def abs_Feature_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl__abs_Feature_decl", None)
        self.__abs_Feature_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit10"):
                opp_val = getattr(old_value, "abs_Compilation_Unit10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit10"):
                opp_val = getattr(value, "abs_Compilation_Unit10", None)
                if opp_val is None:
                    setattr(value, "abs_Compilation_Unit10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Feature_decl370(self):
        return self.__abs_Feature_decl370

    @abs_Feature_decl370.setter
    def abs_Feature_decl370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Feature_decl__abs_Feature_decl370", None)
        self.__abs_Feature_decl370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Product_expr369"):
                opp_val = getattr(old_value, "abs_Product_expr369", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Product_expr369"):
                opp_val = getattr(value, "abs_Product_expr369", None)
                if opp_val is None:
                    setattr(value, "abs_Product_expr369", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Namespace_modifier:

    pass
class abs_Module_export(Namespace_modifier):

    def __init__(self, anyPackage: str, importedNamespace: str, abs_Module_export: "abs_Module_decl" = None):
        self.anyPackage = anyPackage
        self.importedNamespace = importedNamespace
        self.abs_Module_export = abs_Module_export
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def anyPackage(self) -> str:
        return self.__anyPackage

    @anyPackage.setter
    def anyPackage(self, anyPackage: str):
        self.__anyPackage = anyPackage

    @property
    def abs_Module_export(self):
        return self.__abs_Module_export

    @abs_Module_export.setter
    def abs_Module_export(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_export__abs_Module_export", None)
        self.__abs_Module_export = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Module_decl14"):
                opp_val = getattr(old_value, "abs_Module_decl14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Module_decl14"):
                opp_val = getattr(value, "abs_Module_decl14", None)
                if opp_val is None:
                    setattr(value, "abs_Module_decl14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Module_import(Namespace_modifier):

    def __init__(self, importedNamespace: str, name: str, abs_Module_import: "abs_Module_decl" = None):
        self.importedNamespace = importedNamespace
        self.name = name
        self.abs_Module_import = abs_Module_import
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def abs_Module_import(self):
        return self.__abs_Module_import

    @abs_Module_import.setter
    def abs_Module_import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_import__abs_Module_import", None)
        self.__abs_Module_import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Module_decl16"):
                opp_val = getattr(old_value, "abs_Module_decl16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Module_decl16"):
                opp_val = getattr(value, "abs_Module_decl16", None)
                if opp_val is None:
                    setattr(value, "abs_Module_decl16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Module_decl:

    def __init__(self, name: str, abs_Module_decl: "abs_Compilation_Unit" = None, abs_Module_decl20: set["abs_Main_block"] = None, abs_Module_decl14: set["abs_Module_export"] = None, abs_Module_decl16: set["abs_Module_import"] = None, abs_Module_decl18: set["abs_Decl"] = None, abs_Module_decl279: "abs_Delta_access" = None):
        self.name = name
        self.abs_Module_decl = abs_Module_decl
        self.abs_Module_decl20 = abs_Module_decl20 if abs_Module_decl20 is not None else set()
        self.abs_Module_decl14 = abs_Module_decl14 if abs_Module_decl14 is not None else set()
        self.abs_Module_decl16 = abs_Module_decl16 if abs_Module_decl16 is not None else set()
        self.abs_Module_decl18 = abs_Module_decl18 if abs_Module_decl18 is not None else set()
        self.abs_Module_decl279 = abs_Module_decl279
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Module_decl16(self):
        return self.__abs_Module_decl16

    @abs_Module_decl16.setter
    def abs_Module_decl16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_decl__abs_Module_decl16", None)
        self.__abs_Module_decl16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Module_import"):
                    opp_val = getattr(item, "abs_Module_import", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Module_import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Module_import"):
                    opp_val = getattr(item, "abs_Module_import", None)
                    
                    setattr(item, "abs_Module_import", self)
                    

    @property
    def abs_Module_decl14(self):
        return self.__abs_Module_decl14

    @abs_Module_decl14.setter
    def abs_Module_decl14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_decl__abs_Module_decl14", None)
        self.__abs_Module_decl14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Module_export"):
                    opp_val = getattr(item, "abs_Module_export", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Module_export", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Module_export"):
                    opp_val = getattr(item, "abs_Module_export", None)
                    
                    setattr(item, "abs_Module_export", self)
                    

    @property
    def abs_Module_decl18(self):
        return self.__abs_Module_decl18

    @abs_Module_decl18.setter
    def abs_Module_decl18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_decl__abs_Module_decl18", None)
        self.__abs_Module_decl18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Decl"):
                    opp_val = getattr(item, "abs_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Decl"):
                    opp_val = getattr(item, "abs_Decl", None)
                    
                    setattr(item, "abs_Decl", self)
                    

    @property
    def abs_Module_decl(self):
        return self.__abs_Module_decl

    @abs_Module_decl.setter
    def abs_Module_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_decl__abs_Module_decl", None)
        self.__abs_Module_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit"):
                opp_val = getattr(old_value, "abs_Compilation_Unit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit"):
                opp_val = getattr(value, "abs_Compilation_Unit", None)
                if opp_val is None:
                    setattr(value, "abs_Compilation_Unit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Module_decl20(self):
        return self.__abs_Module_decl20

    @abs_Module_decl20.setter
    def abs_Module_decl20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_decl__abs_Module_decl20", None)
        self.__abs_Module_decl20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Main_block"):
                    opp_val = getattr(item, "abs_Main_block", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Main_block", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Main_block"):
                    opp_val = getattr(item, "abs_Main_block", None)
                    
                    setattr(item, "abs_Main_block", self)
                    

    @property
    def abs_Module_decl279(self):
        return self.__abs_Module_decl279

    @abs_Module_decl279.setter
    def abs_Module_decl279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Module_decl__abs_Module_decl279", None)
        self.__abs_Module_decl279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Delta_access278"):
                opp_val = getattr(old_value, "abs_Delta_access278", None)
                if opp_val == self:
                    setattr(old_value, "abs_Delta_access278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Delta_access278"):
                opp_val = getattr(value, "abs_Delta_access278", None)
                setattr(value, "abs_Delta_access278", self)

class DomainModel:

    pass
class abs_Compilation_Unit(DomainModel):

    pass
class abs_DomainModel:

    pass
class abs_Product_decl:

    def __init__(self, name: str, abs_Product_decl: "abs_Compilation_Unit" = None, abs_Product_decl362: set["abs_Feature"] = None, abs_Product_decl365: set["abs_Product_reconfiguration"] = None, abs_Product_decl367: "abs_Product_expr" = None, abs_Product_decl373: "abs_Product_expr" = None):
        self.name = name
        self.abs_Product_decl = abs_Product_decl
        self.abs_Product_decl362 = abs_Product_decl362 if abs_Product_decl362 is not None else set()
        self.abs_Product_decl365 = abs_Product_decl365 if abs_Product_decl365 is not None else set()
        self.abs_Product_decl367 = abs_Product_decl367
        self.abs_Product_decl373 = abs_Product_decl373
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Product_decl362(self):
        return self.__abs_Product_decl362

    @abs_Product_decl362.setter
    def abs_Product_decl362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_decl__abs_Product_decl362", None)
        self.__abs_Product_decl362 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Feature363"):
                    opp_val = getattr(item, "abs_Feature363", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Feature363", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Feature363"):
                    opp_val = getattr(item, "abs_Feature363", None)
                    
                    setattr(item, "abs_Feature363", self)
                    

    @property
    def abs_Product_decl(self):
        return self.__abs_Product_decl

    @abs_Product_decl.setter
    def abs_Product_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_decl__abs_Product_decl", None)
        self.__abs_Product_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit8"):
                opp_val = getattr(old_value, "abs_Compilation_Unit8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit8"):
                opp_val = getattr(value, "abs_Compilation_Unit8", None)
                if opp_val is None:
                    setattr(value, "abs_Compilation_Unit8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Product_decl373(self):
        return self.__abs_Product_decl373

    @abs_Product_decl373.setter
    def abs_Product_decl373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_decl__abs_Product_decl373", None)
        self.__abs_Product_decl373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Product_expr372"):
                opp_val = getattr(old_value, "abs_Product_expr372", None)
                if opp_val == self:
                    setattr(old_value, "abs_Product_expr372", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Product_expr372"):
                opp_val = getattr(value, "abs_Product_expr372", None)
                setattr(value, "abs_Product_expr372", self)

    @property
    def abs_Product_decl367(self):
        return self.__abs_Product_decl367

    @abs_Product_decl367.setter
    def abs_Product_decl367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_decl__abs_Product_decl367", None)
        self.__abs_Product_decl367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Product_expr"):
                opp_val = getattr(old_value, "abs_Product_expr", None)
                if opp_val == self:
                    setattr(old_value, "abs_Product_expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Product_expr"):
                opp_val = getattr(value, "abs_Product_expr", None)
                setattr(value, "abs_Product_expr", self)

    @property
    def abs_Product_decl365(self):
        return self.__abs_Product_decl365

    @abs_Product_decl365.setter
    def abs_Product_decl365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Product_decl__abs_Product_decl365", None)
        self.__abs_Product_decl365 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Product_reconfiguration"):
                    opp_val = getattr(item, "abs_Product_reconfiguration", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Product_reconfiguration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Product_reconfiguration"):
                    opp_val = getattr(item, "abs_Product_reconfiguration", None)
                    
                    setattr(item, "abs_Product_reconfiguration", self)
                    

class abs_Productline_decl:

    def __init__(self, name: str, abs_Productline_decl: "abs_Compilation_Unit" = None, abs_Productline_decl326: set["abs_Feature"] = None, abs_Productline_decl328: set["abs_Delta_clause"] = None):
        self.name = name
        self.abs_Productline_decl = abs_Productline_decl
        self.abs_Productline_decl326 = abs_Productline_decl326 if abs_Productline_decl326 is not None else set()
        self.abs_Productline_decl328 = abs_Productline_decl328 if abs_Productline_decl328 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Productline_decl328(self):
        return self.__abs_Productline_decl328

    @abs_Productline_decl328.setter
    def abs_Productline_decl328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Productline_decl__abs_Productline_decl328", None)
        self.__abs_Productline_decl328 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Delta_clause"):
                    opp_val = getattr(item, "abs_Delta_clause", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Delta_clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Delta_clause"):
                    opp_val = getattr(item, "abs_Delta_clause", None)
                    
                    setattr(item, "abs_Delta_clause", self)
                    

    @property
    def abs_Productline_decl326(self):
        return self.__abs_Productline_decl326

    @abs_Productline_decl326.setter
    def abs_Productline_decl326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Productline_decl__abs_Productline_decl326", None)
        self.__abs_Productline_decl326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Feature"):
                    opp_val = getattr(item, "abs_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Feature"):
                    opp_val = getattr(item, "abs_Feature", None)
                    
                    setattr(item, "abs_Feature", self)
                    

    @property
    def abs_Productline_decl(self):
        return self.__abs_Productline_decl

    @abs_Productline_decl.setter
    def abs_Productline_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Productline_decl__abs_Productline_decl", None)
        self.__abs_Productline_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit6"):
                opp_val = getattr(old_value, "abs_Compilation_Unit6", None)
                if opp_val == self:
                    setattr(old_value, "abs_Compilation_Unit6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit6"):
                opp_val = getattr(value, "abs_Compilation_Unit6", None)
                setattr(value, "abs_Compilation_Unit6", self)

class abs_Update_decl:

    def __init__(self, name: str, abs_Update_decl: "abs_Compilation_Unit" = None, abs_Update_decl308: set["abs_Object_update"] = None):
        self.name = name
        self.abs_Update_decl = abs_Update_decl
        self.abs_Update_decl308 = abs_Update_decl308 if abs_Update_decl308 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Update_decl308(self):
        return self.__abs_Update_decl308

    @abs_Update_decl308.setter
    def abs_Update_decl308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Update_decl__abs_Update_decl308", None)
        self.__abs_Update_decl308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Object_update"):
                    opp_val = getattr(item, "abs_Object_update", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Object_update", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Object_update"):
                    opp_val = getattr(item, "abs_Object_update", None)
                    
                    setattr(item, "abs_Object_update", self)
                    

    @property
    def abs_Update_decl(self):
        return self.__abs_Update_decl

    @abs_Update_decl.setter
    def abs_Update_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Update_decl__abs_Update_decl", None)
        self.__abs_Update_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit4"):
                opp_val = getattr(old_value, "abs_Compilation_Unit4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit4"):
                opp_val = getattr(value, "abs_Compilation_Unit4", None)
                if opp_val is None:
                    setattr(value, "abs_Compilation_Unit4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abs_Delta_decl:

    def __init__(self, name: str, abs_Delta_decl: "abs_Compilation_Unit" = None, abs_Delta_decl264: set["abs_Delta_param"] = None, abs_Delta_decl266: set["abs_Delta_access"] = None, abs_Delta_decl268: set["abs_Module_modifier"] = None, abs_Delta_decl343: "abs_After_condition" = None, abs_Delta_decl334: "abs_Delta_clause" = None):
        self.name = name
        self.abs_Delta_decl = abs_Delta_decl
        self.abs_Delta_decl264 = abs_Delta_decl264 if abs_Delta_decl264 is not None else set()
        self.abs_Delta_decl266 = abs_Delta_decl266 if abs_Delta_decl266 is not None else set()
        self.abs_Delta_decl268 = abs_Delta_decl268 if abs_Delta_decl268 is not None else set()
        self.abs_Delta_decl343 = abs_Delta_decl343
        self.abs_Delta_decl334 = abs_Delta_decl334
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abs_Delta_decl268(self):
        return self.__abs_Delta_decl268

    @abs_Delta_decl268.setter
    def abs_Delta_decl268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_decl__abs_Delta_decl268", None)
        self.__abs_Delta_decl268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Module_modifier"):
                    opp_val = getattr(item, "abs_Module_modifier", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Module_modifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Module_modifier"):
                    opp_val = getattr(item, "abs_Module_modifier", None)
                    
                    setattr(item, "abs_Module_modifier", self)
                    

    @property
    def abs_Delta_decl343(self):
        return self.__abs_Delta_decl343

    @abs_Delta_decl343.setter
    def abs_Delta_decl343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_decl__abs_Delta_decl343", None)
        self.__abs_Delta_decl343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_After_condition342"):
                opp_val = getattr(old_value, "abs_After_condition342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_After_condition342"):
                opp_val = getattr(value, "abs_After_condition342", None)
                if opp_val is None:
                    setattr(value, "abs_After_condition342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abs_Delta_decl264(self):
        return self.__abs_Delta_decl264

    @abs_Delta_decl264.setter
    def abs_Delta_decl264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_decl__abs_Delta_decl264", None)
        self.__abs_Delta_decl264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Delta_param"):
                    opp_val = getattr(item, "abs_Delta_param", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Delta_param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Delta_param"):
                    opp_val = getattr(item, "abs_Delta_param", None)
                    
                    setattr(item, "abs_Delta_param", self)
                    

    @property
    def abs_Delta_decl334(self):
        return self.__abs_Delta_decl334

    @abs_Delta_decl334.setter
    def abs_Delta_decl334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_decl__abs_Delta_decl334", None)
        self.__abs_Delta_decl334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Delta_clause333"):
                opp_val = getattr(old_value, "abs_Delta_clause333", None)
                if opp_val == self:
                    setattr(old_value, "abs_Delta_clause333", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Delta_clause333"):
                opp_val = getattr(value, "abs_Delta_clause333", None)
                setattr(value, "abs_Delta_clause333", self)

    @property
    def abs_Delta_decl266(self):
        return self.__abs_Delta_decl266

    @abs_Delta_decl266.setter
    def abs_Delta_decl266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_decl__abs_Delta_decl266", None)
        self.__abs_Delta_decl266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abs_Delta_access"):
                    opp_val = getattr(item, "abs_Delta_access", None)
                    
                    if opp_val == self:
                        setattr(item, "abs_Delta_access", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abs_Delta_access"):
                    opp_val = getattr(item, "abs_Delta_access", None)
                    
                    setattr(item, "abs_Delta_access", self)
                    

    @property
    def abs_Delta_decl(self):
        return self.__abs_Delta_decl

    @abs_Delta_decl.setter
    def abs_Delta_decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs_Delta_decl__abs_Delta_decl", None)
        self.__abs_Delta_decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs_Compilation_Unit2"):
                opp_val = getattr(old_value, "abs_Compilation_Unit2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs_Compilation_Unit2"):
                opp_val = getattr(value, "abs_Compilation_Unit2", None)
                if opp_val is None:
                    setattr(value, "abs_Compilation_Unit2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
