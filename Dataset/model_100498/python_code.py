from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DifferentialRelationOperator(Enum):
    FEWER_THAN = "FEWER_THAN"
    GREATER_THAN = "GREATER_THAN"
class MonitorableMethod(Enum):
    START = "START"
    END = "END"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    CANCEL = "CANCEL"
class ParameterType(Enum):
    VARIATION_POINT = "VARIATION_POINT"
    ENUMERATED_CONTROL_VARIABLE = "ENUMERATED_CONTROL_VARIABLE"
    NUMERIC_CONTROL_VARIABLE = "NUMERIC_CONTROL_VARIABLE"
class AggregationLevel(Enum):
    INSTANCE = "INSTANCE"
    CLASS = "CLASS"
    BOTH = "BOTH"
class RefinementType(Enum):
    AND = "AND"
    OR = "OR"
class ParameterMetric(Enum):
    ENUMERATED = "ENUMERATED"
    INTEGER = "INTEGER"
    REAL = "REAL"
class DefinableRequirementState(Enum):
    UNDEFINED = "UNDEFINED"
    STARTED = "STARTED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


############################################
# Definition of Classes
############################################

class gore_Configuration:

    pass
class gore_Actor:

    pass
class gore_DifferentialRelation:

    def __init__(self, lowerBound: str, upperBound: str, operator: str, value: float, gore_DifferentialRelation: "gore_AwReq" = None, gore_DifferentialRelation21: "gore_Parameter" = None, gore_DifferentialRelation28: "gore_GoalModel" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.operator = operator
        self.value = value
        self.gore_DifferentialRelation = gore_DifferentialRelation
        self.gore_DifferentialRelation21 = gore_DifferentialRelation21
        self.gore_DifferentialRelation28 = gore_DifferentialRelation28
        
        pass
    @property
    def upperBound(self):
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def lowerBound(self):
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    @property
    def gore_DifferentialRelation28(self):
        return self.__gore_DifferentialRelation28

    @gore_DifferentialRelation28.setter
    def gore_DifferentialRelation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_DifferentialRelation__gore_DifferentialRelation28", None)
        self.__gore_DifferentialRelation28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_GoalModel"):
                opp_val = getattr(old_value, "gore_GoalModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_GoalModel"):
                opp_val = getattr(value, "gore_GoalModel", None)
                if opp_val is None:
                    setattr(value, "gore_GoalModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gore_DifferentialRelation(self):
        return self.__gore_DifferentialRelation

    @gore_DifferentialRelation.setter
    def gore_DifferentialRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_DifferentialRelation__gore_DifferentialRelation", None)
        self.__gore_DifferentialRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_AwReq19"):
                opp_val = getattr(old_value, "gore_AwReq19", None)
                if opp_val == self:
                    setattr(old_value, "gore_AwReq19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_AwReq19"):
                opp_val = getattr(value, "gore_AwReq19", None)
                setattr(value, "gore_AwReq19", self)

    @property
    def gore_DifferentialRelation21(self):
        return self.__gore_DifferentialRelation21

    @gore_DifferentialRelation21.setter
    def gore_DifferentialRelation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_DifferentialRelation__gore_DifferentialRelation21", None)
        self.__gore_DifferentialRelation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_Parameter"):
                opp_val = getattr(old_value, "gore_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "gore_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_Parameter"):
                opp_val = getattr(value, "gore_Parameter", None)
                setattr(value, "gore_Parameter", self)

class gore_Parameter:

    def __init__(self, type: str, unit: str, value: str, metric: str, Parameter: "gore_Configuration" = None, gore_Parameter: "gore_DifferentialRelation" = None, parameters: "gore_Configuration" = None):
        self.type = type
        self.unit = unit
        self.value = value
        self.metric = metric
        self.Parameter = Parameter
        self.gore_Parameter = gore_Parameter
        self.parameters = parameters
        
        pass
    @property
    def metric(self):
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configuration"):
                opp_val = getattr(old_value, "configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configuration"):
                opp_val = getattr(value, "configuration", None)
                if opp_val is None:
                    setattr(value, "configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Parameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration30"):
                opp_val = getattr(old_value, "Configuration30", None)
                if opp_val == self:
                    setattr(old_value, "Configuration30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration30"):
                opp_val = getattr(value, "Configuration30", None)
                setattr(value, "Configuration30", self)

    @property
    def gore_Parameter(self):
        return self.__gore_Parameter

    @gore_Parameter.setter
    def gore_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Parameter__gore_Parameter", None)
        self.__gore_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_DifferentialRelation21"):
                opp_val = getattr(old_value, "gore_DifferentialRelation21", None)
                if opp_val == self:
                    setattr(old_value, "gore_DifferentialRelation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_DifferentialRelation21"):
                opp_val = getattr(value, "gore_DifferentialRelation21", None)
                setattr(value, "gore_DifferentialRelation21", self)

    def increment(self, gore_relation, gore_value):
        # TODO: Implement increment method
        pass

    def fewerThan(self, gore_value) :
        # TODO: Implement fewerThan method
        pass

    def withinBoundsOf(self, gore_relation) :
        # TODO: Implement withinBoundsOf method
        pass

    def createCopy(self) :
        # TODO: Implement createCopy method
        pass

    def addedTo(self, gore_value) :
        # TODO: Implement addedTo method
        pass

    def greaterThan(self, gore_value) :
        # TODO: Implement greaterThan method
        pass

    def multipliedBy(self, gore_value) :
        # TODO: Implement multipliedBy method
        pass

    def equalTo(self, gore_value) :
        # TODO: Implement equalTo method
        pass

    def incrementableIn(self, gore_relation) :
        # TODO: Implement incrementableIn method
        pass

    def subtractedFrom(self, gore_value) :
        # TODO: Implement subtractedFrom method
        pass

class gore_GoalModel:

    def __init__(self, internalId: str, GoalModel: "gore_Goal" = None, GoalModel17: "gore_Configuration" = None, GoalModel13: "gore_Actor" = None, goalModel: "gore_Goal" = None, goalModel24: set["gore_Actor"] = None, goalModel26: "gore_Configuration" = None, gore_GoalModel: set["gore_DifferentialRelation"] = None):
        self.internalId = internalId
        self.GoalModel = GoalModel
        self.GoalModel17 = GoalModel17
        self.GoalModel13 = GoalModel13
        self.goalModel = goalModel
        self.goalModel24 = goalModel24 if goalModel24 is not None else set()
        self.goalModel26 = goalModel26
        self.gore_GoalModel = gore_GoalModel if gore_GoalModel is not None else set()
        
        pass
    @property
    def internalId(self):
        return self.__internalId

    @internalId.setter
    def internalId(self, internalId: str):
        self.__internalId = internalId


    @property
    def goalModel(self):
        return self.__goalModel

    @goalModel.setter
    def goalModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__goalModel", None)
        self.__goalModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Goal"):
                opp_val = getattr(old_value, "Goal", None)
                if opp_val == self:
                    setattr(old_value, "Goal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal"):
                opp_val = getattr(value, "Goal", None)
                setattr(value, "Goal", self)

    @property
    def goalModel26(self):
        return self.__goalModel26

    @goalModel26.setter
    def goalModel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__goalModel26", None)
        self.__goalModel26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration"):
                opp_val = getattr(old_value, "Configuration", None)
                if opp_val == self:
                    setattr(old_value, "Configuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration"):
                opp_val = getattr(value, "Configuration", None)
                setattr(value, "Configuration", self)

    @property
    def GoalModel17(self):
        return self.__GoalModel17

    @GoalModel17.setter
    def GoalModel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__GoalModel17", None)
        self.__GoalModel17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configuration16"):
                opp_val = getattr(old_value, "configuration16", None)
                if opp_val == self:
                    setattr(old_value, "configuration16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configuration16"):
                opp_val = getattr(value, "configuration16", None)
                setattr(value, "configuration16", self)

    @property
    def goalModel24(self):
        return self.__goalModel24

    @goalModel24.setter
    def goalModel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__goalModel24", None)
        self.__goalModel24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    setattr(item, "Actor", self)
                    

    @property
    def gore_GoalModel(self):
        return self.__gore_GoalModel

    @gore_GoalModel.setter
    def gore_GoalModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__gore_GoalModel", None)
        self.__gore_GoalModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gore_DifferentialRelation28"):
                    opp_val = getattr(item, "gore_DifferentialRelation28", None)
                    
                    if opp_val == self:
                        setattr(item, "gore_DifferentialRelation28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gore_DifferentialRelation28"):
                    opp_val = getattr(item, "gore_DifferentialRelation28", None)
                    
                    setattr(item, "gore_DifferentialRelation28", self)
                    

    @property
    def GoalModel13(self):
        return self.__GoalModel13

    @GoalModel13.setter
    def GoalModel13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__GoalModel13", None)
        self.__GoalModel13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actors"):
                opp_val = getattr(old_value, "actors", None)
                if opp_val == self:
                    setattr(old_value, "actors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actors"):
                opp_val = getattr(value, "actors", None)
                setattr(value, "actors", self)

    @property
    def GoalModel(self):
        return self.__GoalModel

    @GoalModel.setter
    def GoalModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_GoalModel__GoalModel", None)
        self.__GoalModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rootGoal"):
                opp_val = getattr(old_value, "rootGoal", None)
                if opp_val == self:
                    setattr(old_value, "rootGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rootGoal"):
                opp_val = getattr(value, "rootGoal", None)
                setattr(value, "rootGoal", self)

    def filterRelations(self, gore_parameter, gore_indicator) :
        # TODO: Implement filterRelations method
        pass

    def getId(self) :
        # TODO: Implement getId method
        pass

class PerformativeRequirement:

    pass
class gore_Task(PerformativeRequirement):

    pass
class gore_Goal(PerformativeRequirement):

    pass
class DefinableRequirement:

    pass
class gore_DomainAssumption(DefinableRequirement):

    pass
class gore_PerformativeRequirement(DefinableRequirement):

    def __init__(self, startTime: date):
        self.startTime = startTime
        
        pass
    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: date):
        self.__startTime = startTime


    def checkState(self):
        # TODO: Implement checkState method
        pass

    def cancel(self):
        # TODO: Implement cancel method
        pass

class gore_QualityConstraint(DefinableRequirement):

    def __init__(self, constraints: "gore_Softgoal" = None, QualityConstraint: "gore_Softgoal" = None):
        self.constraints = constraints
        self.QualityConstraint = QualityConstraint
        
        pass
    @property
    def QualityConstraint(self):
        return self.__QualityConstraint

    @QualityConstraint.setter
    def QualityConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_QualityConstraint__QualityConstraint", None)
        self.__QualityConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softgoal"):
                opp_val = getattr(old_value, "softgoal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softgoal"):
                opp_val = getattr(value, "softgoal", None)
                if opp_val is None:
                    setattr(value, "softgoal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_QualityConstraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Softgoal"):
                opp_val = getattr(old_value, "Softgoal", None)
                if opp_val == self:
                    setattr(old_value, "Softgoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Softgoal"):
                opp_val = getattr(value, "Softgoal", None)
                setattr(value, "Softgoal", self)

    def replaceWith(self, gore_newRequirement):
        # TODO: Implement replaceWith method
        pass

class gore_AwReq(DefinableRequirement):

    def __init__(self, incrementCoefficient: float, gore_AwReq: set["gore_DefinableRequirement"] = None, gore_AwReq9: "gore_DefinableRequirement" = None, gore_AwReq19: "gore_DifferentialRelation" = None):
        self.incrementCoefficient = incrementCoefficient
        self.gore_AwReq = gore_AwReq if gore_AwReq is not None else set()
        self.gore_AwReq9 = gore_AwReq9
        self.gore_AwReq19 = gore_AwReq19
        
        pass
    @property
    def incrementCoefficient(self):
        return self.__incrementCoefficient

    @incrementCoefficient.setter
    def incrementCoefficient(self, incrementCoefficient: float):
        self.__incrementCoefficient = incrementCoefficient


    @property
    def gore_AwReq9(self):
        return self.__gore_AwReq9

    @gore_AwReq9.setter
    def gore_AwReq9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_AwReq__gore_AwReq9", None)
        self.__gore_AwReq9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_DefinableRequirement10"):
                opp_val = getattr(old_value, "gore_DefinableRequirement10", None)
                if opp_val == self:
                    setattr(old_value, "gore_DefinableRequirement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_DefinableRequirement10"):
                opp_val = getattr(value, "gore_DefinableRequirement10", None)
                setattr(value, "gore_DefinableRequirement10", self)

    @property
    def gore_AwReq(self):
        return self.__gore_AwReq

    @gore_AwReq.setter
    def gore_AwReq(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_AwReq__gore_AwReq", None)
        self.__gore_AwReq = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gore_DefinableRequirement"):
                    opp_val = getattr(item, "gore_DefinableRequirement", None)
                    
                    if opp_val == self:
                        setattr(item, "gore_DefinableRequirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gore_DefinableRequirement"):
                    opp_val = getattr(item, "gore_DefinableRequirement", None)
                    
                    setattr(item, "gore_DefinableRequirement", self)
                    

    @property
    def gore_AwReq19(self):
        return self.__gore_AwReq19

    @gore_AwReq19.setter
    def gore_AwReq19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_AwReq__gore_AwReq19", None)
        self.__gore_AwReq19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_DifferentialRelation"):
                opp_val = getattr(old_value, "gore_DifferentialRelation", None)
                if opp_val == self:
                    setattr(old_value, "gore_DifferentialRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_DifferentialRelation"):
                opp_val = getattr(value, "gore_DifferentialRelation", None)
                setattr(value, "gore_DifferentialRelation", self)

class OclAny:

    pass
class gore_Requirement(OclAny):

    def __init__(self, refinementType: str, Requirement4: "gore_Requirement" = None, children: "gore_Requirement" = None, Requirement: "gore_Requirement" = None, parent: set["gore_Requirement"] = None):
        self.refinementType = refinementType
        self.Requirement4 = Requirement4
        self.children = children
        self.Requirement = Requirement
        self.parent = parent if parent is not None else set()
        
        pass
    @property
    def refinementType(self):
        return self.__refinementType

    @refinementType.setter
    def refinementType(self, refinementType: str):
        self.__refinementType = refinementType


    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Requirement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Requirement4"):
                opp_val = getattr(old_value, "Requirement4", None)
                if opp_val == self:
                    setattr(old_value, "Requirement4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Requirement4"):
                opp_val = getattr(value, "Requirement4", None)
                setattr(value, "Requirement4", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Requirement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    setattr(item, "Requirement", self)
                    

    @property
    def Requirement(self):
        return self.__Requirement

    @Requirement.setter
    def Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Requirement__Requirement", None)
        self.__Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Requirement4(self):
        return self.__Requirement4

    @Requirement4.setter
    def Requirement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_Requirement__Requirement4", None)
        self.__Requirement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    def replaceWith(self, gore_newRequirement):
        # TODO: Implement replaceWith method
        pass

    def findGoalModel(self) :
        # TODO: Implement findGoalModel method
        pass

    def getChildrenStateCount(self) :
        # TODO: Implement getChildrenStateCount method
        pass

class Requirement:

    pass
class gore_Softgoal(Requirement):

    pass
class gore_DefinableRequirement(Requirement):

    def __init__(self, time: date, state: str, gore_DefinableRequirement: "gore_AwReq" = None, gore_DefinableRequirement10: "gore_AwReq" = None):
        self.time = time
        self.state = state
        self.gore_DefinableRequirement = gore_DefinableRequirement
        self.gore_DefinableRequirement10 = gore_DefinableRequirement10
        
        pass
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: date):
        self.__time = time


    @property
    def gore_DefinableRequirement(self):
        return self.__gore_DefinableRequirement

    @gore_DefinableRequirement.setter
    def gore_DefinableRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_DefinableRequirement__gore_DefinableRequirement", None)
        self.__gore_DefinableRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_AwReq"):
                opp_val = getattr(old_value, "gore_AwReq", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_AwReq"):
                opp_val = getattr(value, "gore_AwReq", None)
                if opp_val is None:
                    setattr(value, "gore_AwReq", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gore_DefinableRequirement10(self):
        return self.__gore_DefinableRequirement10

    @gore_DefinableRequirement10.setter
    def gore_DefinableRequirement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gore_DefinableRequirement__gore_DefinableRequirement10", None)
        self.__gore_DefinableRequirement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gore_AwReq9"):
                opp_val = getattr(old_value, "gore_AwReq9", None)
                if opp_val == self:
                    setattr(old_value, "gore_AwReq9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gore_AwReq9"):
                opp_val = getattr(value, "gore_AwReq9", None)
                setattr(value, "gore_AwReq9", self)

    def success(self):
        # TODO: Implement success method
        pass

    def start(self):
        # TODO: Implement start method
        pass

    def checkState(self):
        # TODO: Implement checkState method
        pass

    def end(self):
        # TODO: Implement end method
        pass

    def fail(self):
        # TODO: Implement fail method
        pass
