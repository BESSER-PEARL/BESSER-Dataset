from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UnaryExpression:

    pass
class ca_rule_Not(UnaryExpression):

    pass
class ca_rule_UMinus(UnaryExpression):

    pass
class ca_rule_CellularAutomata:

    pass
class ca_rule_IntegerExpression:

    pass
class ca_rule_Rule:

    pass
class IntegerExpression:

    pass
class ca_rule_CurrentCellPopulation(IntegerExpression):

    pass
class ca_rule_Conditional(IntegerExpression):

    pass
class ca_rule_NeighborsExpression(IntegerExpression):

    pass
class ca_rule_IntegerLiteral(IntegerExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ca_rule_BinaryExpression(IntegerExpression):

    pass
class ca_rule_UnaryExpression(IntegerExpression):

    pass
class BinaryExpression:

    pass
class ca_rule_Div(BinaryExpression):

    pass
class ca_rule_Or(BinaryExpression):

    pass
class ca_rule_Equal(BinaryExpression):

    pass
class ca_rule_Greater(BinaryExpression):

    pass
class ca_rule_Lower(BinaryExpression):

    pass
class ca_rule_Minus(BinaryExpression):

    pass
class ca_rule_Mod(BinaryExpression):

    pass
class ca_rule_Mult(BinaryExpression):

    pass
class ca_rule_And(BinaryExpression):

    pass
class ca_rule_Add(BinaryExpression):

    pass
class NeighborsExpression:

    pass
class ca_rule_Size(NeighborsExpression):

    pass
class ca_rule_Min(NeighborsExpression):

    pass
class ca_rule_Sum(NeighborsExpression):

    pass
class ca_rule_Max(NeighborsExpression):

    pass
class ca_rule_PopulationRange:

    def __init__(self, lowerRange: int, upperRange: int, ca_rule_PopulationRange: "ca_rule_Rule" = None, ca_rule_PopulationRange14: "ca_rule_NeighborsExpression" = None):
        self.lowerRange = lowerRange
        self.upperRange = upperRange
        self.ca_rule_PopulationRange = ca_rule_PopulationRange
        self.ca_rule_PopulationRange14 = ca_rule_PopulationRange14
        
    @property
    def lowerRange(self) -> int:
        return self.__lowerRange

    @lowerRange.setter
    def lowerRange(self, lowerRange: int):
        self.__lowerRange = lowerRange

    @property
    def upperRange(self) -> int:
        return self.__upperRange

    @upperRange.setter
    def upperRange(self, upperRange: int):
        self.__upperRange = upperRange

    @property
    def ca_rule_PopulationRange(self):
        return self.__ca_rule_PopulationRange

    @ca_rule_PopulationRange.setter
    def ca_rule_PopulationRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ca_rule_PopulationRange__ca_rule_PopulationRange", None)
        self.__ca_rule_PopulationRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ca_rule_Rule2"):
                opp_val = getattr(old_value, "ca_rule_Rule2", None)
                if opp_val == self:
                    setattr(old_value, "ca_rule_Rule2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ca_rule_Rule2"):
                opp_val = getattr(value, "ca_rule_Rule2", None)
                setattr(value, "ca_rule_Rule2", self)

    @property
    def ca_rule_PopulationRange14(self):
        return self.__ca_rule_PopulationRange14

    @ca_rule_PopulationRange14.setter
    def ca_rule_PopulationRange14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ca_rule_PopulationRange__ca_rule_PopulationRange14", None)
        self.__ca_rule_PopulationRange14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ca_rule_NeighborsExpression"):
                opp_val = getattr(old_value, "ca_rule_NeighborsExpression", None)
                if opp_val == self:
                    setattr(old_value, "ca_rule_NeighborsExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ca_rule_NeighborsExpression"):
                opp_val = getattr(value, "ca_rule_NeighborsExpression", None)
                setattr(value, "ca_rule_NeighborsExpression", self)
