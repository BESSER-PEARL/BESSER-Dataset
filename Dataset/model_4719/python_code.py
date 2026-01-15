from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UnaryExpression:

    pass
class rule_UMinus(UnaryExpression):

    pass
class rule_Not(UnaryExpression):

    pass
class rule_CellularAutomata:

    pass
class rule_PopulationRange:

    def __init__(self, lowerRange: int, upperRange: int, rule_PopulationRange: "rule_Rule" = None, rule_PopulationRange14: "rule_NeighborsExpression" = None):
        self.lowerRange = lowerRange
        self.upperRange = upperRange
        self.rule_PopulationRange = rule_PopulationRange
        self.rule_PopulationRange14 = rule_PopulationRange14
        
    @property
    def upperRange(self) -> int:
        return self.__upperRange

    @upperRange.setter
    def upperRange(self, upperRange: int):
        self.__upperRange = upperRange

    @property
    def lowerRange(self) -> int:
        return self.__lowerRange

    @lowerRange.setter
    def lowerRange(self, lowerRange: int):
        self.__lowerRange = lowerRange

    @property
    def rule_PopulationRange14(self):
        return self.__rule_PopulationRange14

    @rule_PopulationRange14.setter
    def rule_PopulationRange14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rule_PopulationRange__rule_PopulationRange14", None)
        self.__rule_PopulationRange14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rule_NeighborsExpression"):
                opp_val = getattr(old_value, "rule_NeighborsExpression", None)
                if opp_val == self:
                    setattr(old_value, "rule_NeighborsExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rule_NeighborsExpression"):
                opp_val = getattr(value, "rule_NeighborsExpression", None)
                setattr(value, "rule_NeighborsExpression", self)

    @property
    def rule_PopulationRange(self):
        return self.__rule_PopulationRange

    @rule_PopulationRange.setter
    def rule_PopulationRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rule_PopulationRange__rule_PopulationRange", None)
        self.__rule_PopulationRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rule_Rule2"):
                opp_val = getattr(old_value, "rule_Rule2", None)
                if opp_val == self:
                    setattr(old_value, "rule_Rule2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rule_Rule2"):
                opp_val = getattr(value, "rule_Rule2", None)
                setattr(value, "rule_Rule2", self)

class rule_IntegerExpression:

    pass
class rule_Rule:

    pass
class IntegerExpression:

    pass
class rule_BinaryExpression(IntegerExpression):

    pass
class rule_Conditional(IntegerExpression):

    pass
class rule_NeighborsExpression(IntegerExpression):

    pass
class rule_IntegerLiteral(IntegerExpression):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class rule_CurrentCellPopulation(IntegerExpression):

    pass
class rule_UnaryExpression(IntegerExpression):

    pass
class BinaryExpression:

    pass
class rule_Minus(BinaryExpression):

    pass
class rule_Lower(BinaryExpression):

    pass
class rule_Equal(BinaryExpression):

    pass
class rule_Div(BinaryExpression):

    pass
class rule_And(BinaryExpression):

    pass
class rule_Greater(BinaryExpression):

    pass
class rule_Mod(BinaryExpression):

    pass
class rule_Or(BinaryExpression):

    pass
class rule_Mult(BinaryExpression):

    pass
class rule_Add(BinaryExpression):

    pass
class NeighborsExpression:

    pass
class rule_Max(NeighborsExpression):

    pass
class rule_Size(NeighborsExpression):

    pass
class rule_Sum(NeighborsExpression):

    pass
class rule_Min(NeighborsExpression):

    pass