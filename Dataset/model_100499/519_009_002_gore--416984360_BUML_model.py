####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
DefinableRequirementState: Enumeration = Enumeration(
    name="DefinableRequirementState",
    literals={
            EnumerationLiteral(name="UNDEFINED"),
			EnumerationLiteral(name="STARTED"),
			EnumerationLiteral(name="SUCCEEDED"),
			EnumerationLiteral(name="FAILED"),
			EnumerationLiteral(name="CANCELED")
    }
)

DifferentialRelationOperator: Enumeration = Enumeration(
    name="DifferentialRelationOperator",
    literals={
            EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="FEWER_THAN")
    }
)

MonitorableMethod: Enumeration = Enumeration(
    name="MonitorableMethod",
    literals={
            EnumerationLiteral(name="START"),
			EnumerationLiteral(name="END"),
			EnumerationLiteral(name="SUCCESS"),
			EnumerationLiteral(name="FAIL"),
			EnumerationLiteral(name="CANCEL")
    }
)

ParameterMetric: Enumeration = Enumeration(
    name="ParameterMetric",
    literals={
            EnumerationLiteral(name="ENUMERATED"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="REAL")
    }
)

ParameterType: Enumeration = Enumeration(
    name="ParameterType",
    literals={
            EnumerationLiteral(name="VARIATION_POINT"),
			EnumerationLiteral(name="ENUMERATED_CONTROL_VARIABLE"),
			EnumerationLiteral(name="NUMERIC_CONTROL_VARIABLE")
    }
)

RefinementType: Enumeration = Enumeration(
    name="RefinementType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

AggregationLevel: Enumeration = Enumeration(
    name="AggregationLevel",
    literals={
            EnumerationLiteral(name="INSTANCE"),
			EnumerationLiteral(name="CLASS"),
			EnumerationLiteral(name="BOTH")
    }
)

# Classes
gore_Requirement = Class(name="gore_Requirement")
OclAny = Class(name="OclAny")
gore_DefinableRequirement = Class(name="gore_DefinableRequirement")
Requirement = Class(name="Requirement")
gore_Softgoal = Class(name="gore_Softgoal")
gore_QualityConstraint = Class(name="gore_QualityConstraint")
gore_PerformativeRequirement = Class(name="gore_PerformativeRequirement")
DefinableRequirement = Class(name="DefinableRequirement")
gore_AwReq = Class(name="gore_AwReq")
gore_DomainAssumption = Class(name="gore_DomainAssumption")
gore_Goal = Class(name="gore_Goal")
PerformativeRequirement = Class(name="PerformativeRequirement")
gore_Actor = Class(name="gore_Actor")
gore_Configuration = Class(name="gore_Configuration")
gore_Parameter = Class(name="gore_Parameter")
gore_DifferentialRelation = Class(name="gore_DifferentialRelation")
gore_GoalModel = Class(name="gore_GoalModel")
gore_Task = Class(name="gore_Task")

# gore_Requirement class attributes and methods
gore_Requirement_refinementType: Property = Property(name="refinementType", type=StringType)
gore_Requirement_m_getChildrenStateCount: Method = Method(name="getChildrenStateCount", parameters={}, type=IntegerType)
gore_Requirement_m_replaceWith: Method = Method(name="replaceWith", parameters={Parameter(name='gore_newRequirement', type=StringType)})
gore_Requirement_m_findGoalModel: Method = Method(name="findGoalModel", parameters={}, type=StringType)
gore_Requirement.attributes={gore_Requirement_refinementType}
gore_Requirement.methods={gore_Requirement_m_getChildrenStateCount, gore_Requirement_m_findGoalModel, gore_Requirement_m_replaceWith}

# OclAny class attributes and methods

# gore_DefinableRequirement class attributes and methods
gore_DefinableRequirement_time: Property = Property(name="time", type=DateType)
gore_DefinableRequirement_state: Property = Property(name="state", type=StringType)
gore_DefinableRequirement_m_start: Method = Method(name="start", parameters={})
gore_DefinableRequirement_m_end: Method = Method(name="end", parameters={})
gore_DefinableRequirement_m_success: Method = Method(name="success", parameters={})
gore_DefinableRequirement_m_fail: Method = Method(name="fail", parameters={})
gore_DefinableRequirement_m_checkState: Method = Method(name="checkState", parameters={})
gore_DefinableRequirement.attributes={gore_DefinableRequirement_state, gore_DefinableRequirement_time}
gore_DefinableRequirement.methods={gore_DefinableRequirement_m_success, gore_DefinableRequirement_m_fail, gore_DefinableRequirement_m_end, gore_DefinableRequirement_m_checkState, gore_DefinableRequirement_m_start}

# Requirement class attributes and methods

# gore_Softgoal class attributes and methods

# gore_QualityConstraint class attributes and methods
gore_QualityConstraint_m_replaceWith: Method = Method(name="replaceWith", parameters={Parameter(name='gore_newRequirement', type=StringType)})
gore_QualityConstraint.methods={gore_QualityConstraint_m_replaceWith}

# gore_PerformativeRequirement class attributes and methods
gore_PerformativeRequirement_startTime: Property = Property(name="startTime", type=DateType)
gore_PerformativeRequirement_m_cancel: Method = Method(name="cancel", parameters={})
gore_PerformativeRequirement_m_checkState: Method = Method(name="checkState", parameters={})
gore_PerformativeRequirement.attributes={gore_PerformativeRequirement_startTime}
gore_PerformativeRequirement.methods={gore_PerformativeRequirement_m_checkState, gore_PerformativeRequirement_m_cancel}

# DefinableRequirement class attributes and methods

# gore_AwReq class attributes and methods
gore_AwReq_incrementCoefficient: Property = Property(name="incrementCoefficient", type=FloatType)
gore_AwReq.attributes={gore_AwReq_incrementCoefficient}

# gore_DomainAssumption class attributes and methods

# gore_Goal class attributes and methods

# PerformativeRequirement class attributes and methods

# gore_Actor class attributes and methods

# gore_Configuration class attributes and methods

# gore_Parameter class attributes and methods
gore_Parameter_type: Property = Property(name="type", type=StringType)
gore_Parameter_unit: Property = Property(name="unit", type=StringType)
gore_Parameter_value: Property = Property(name="value", type=StringType)
gore_Parameter_metric: Property = Property(name="metric", type=StringType)
gore_Parameter_m_greaterThan: Method = Method(name="greaterThan", parameters={Parameter(name='gore_value', type=StringType)}, type=StringType)
gore_Parameter_m_fewerThan: Method = Method(name="fewerThan", parameters={Parameter(name='gore_value', type=StringType)}, type=StringType)
gore_Parameter_m_equalTo: Method = Method(name="equalTo", parameters={Parameter(name='gore_value', type=StringType)}, type=StringType)
gore_Parameter_m_addedTo: Method = Method(name="addedTo", parameters={Parameter(name='gore_value', type=StringType)}, type=StringType)
gore_Parameter_m_multipliedBy: Method = Method(name="multipliedBy", parameters={Parameter(name='gore_value', type=StringType)}, type=StringType)
gore_Parameter_m_subtractedFrom: Method = Method(name="subtractedFrom", parameters={Parameter(name='gore_value', type=StringType)}, type=StringType)
gore_Parameter_m_withinBoundsOf: Method = Method(name="withinBoundsOf", parameters={Parameter(name='gore_relation', type=StringType)}, type=StringType)
gore_Parameter_m_incrementableIn: Method = Method(name="incrementableIn", parameters={Parameter(name='gore_relation', type=StringType)}, type=StringType)
gore_Parameter_m_createCopy: Method = Method(name="createCopy", parameters={}, type=StringType)
gore_Parameter_m_increment: Method = Method(name="increment", parameters={Parameter(name='gore_value', type=StringType), Parameter(name='gore_relation', type=StringType)})
gore_Parameter.attributes={gore_Parameter_type, gore_Parameter_metric, gore_Parameter_unit, gore_Parameter_value}
gore_Parameter.methods={gore_Parameter_m_createCopy, gore_Parameter_m_increment, gore_Parameter_m_withinBoundsOf, gore_Parameter_m_equalTo, gore_Parameter_m_subtractedFrom, gore_Parameter_m_incrementableIn, gore_Parameter_m_multipliedBy, gore_Parameter_m_fewerThan, gore_Parameter_m_greaterThan, gore_Parameter_m_addedTo}

# gore_DifferentialRelation class attributes and methods
gore_DifferentialRelation_lowerBound: Property = Property(name="lowerBound", type=StringType)
gore_DifferentialRelation_upperBound: Property = Property(name="upperBound", type=StringType)
gore_DifferentialRelation_operator: Property = Property(name="operator", type=StringType)
gore_DifferentialRelation_value: Property = Property(name="value", type=FloatType)
gore_DifferentialRelation.attributes={gore_DifferentialRelation_operator, gore_DifferentialRelation_value, gore_DifferentialRelation_lowerBound, gore_DifferentialRelation_upperBound}

# gore_GoalModel class attributes and methods
gore_GoalModel_internalId: Property = Property(name="internalId", type=StringType)
gore_GoalModel_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
gore_GoalModel_m_filterRelations: Method = Method(name="filterRelations", parameters={Parameter(name='gore_indicator', type=StringType)}, type=StringType)
gore_GoalModel_m_filterRelations: Method = Method(name="filterRelations", parameters={Parameter(name='gore_parameter', type=StringType)}, type=StringType)
gore_GoalModel_m_filterRelations: Method = Method(name="filterRelations", parameters={Parameter(name='gore_parameter', type=StringType), Parameter(name='gore_indicator', type=StringType)}, type=StringType)
gore_GoalModel_m_filterRelations: Method = Method(name="filterRelations", parameters={Parameter(name='gore_value', type=StringType), Parameter(name='gore_parameter', type=StringType), Parameter(name='gore_indicator', type=StringType)}, type=StringType)
gore_GoalModel.attributes={gore_GoalModel_internalId}
gore_GoalModel.methods={gore_GoalModel_m_getId, gore_GoalModel_m_filterRelations, gore_GoalModel_m_filterRelations, gore_GoalModel_m_filterRelations, gore_GoalModel_m_filterRelations}

# gore_Task class attributes and methods

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="Requirement", type=gore_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=gore_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="Requirement4", type=gore_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=gore_Requirement, multiplicity=Multiplicity(0, 1))
    }
)
constraints5: BinaryAssociation = BinaryAssociation(
    name="constraints5",
    ends={
        Property(name="QualityConstraint", type=gore_Softgoal, multiplicity=Multiplicity(1, 1)),
        Property(name="softgoal", type=gore_QualityConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
softgoal6: BinaryAssociation = BinaryAssociation(
    name="softgoal6",
    ends={
        Property(name="Softgoal", type=gore_QualityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=gore_Softgoal, multiplicity=Multiplicity(1, 1))
    }
)
otherTargets7: BinaryAssociation = BinaryAssociation(
    name="otherTargets7",
    ends={
        Property(name="gore_DefinableRequirement", type=gore_AwReq, multiplicity=Multiplicity(1, 1)),
        Property(name="gore_AwReq", type=gore_DefinableRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="gore_DefinableRequirement10", type=gore_AwReq, multiplicity=Multiplicity(1, 1)),
        Property(name="gore_AwReq9", type=gore_DefinableRequirement, multiplicity=Multiplicity(1, 1))
    }
)
goalModel12: BinaryAssociation = BinaryAssociation(
    name="goalModel12",
    ends={
        Property(name="GoalModel13", type=gore_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=gore_GoalModel, multiplicity=Multiplicity(0, 1))
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="Parameter", type=gore_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=gore_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goalModel15: BinaryAssociation = BinaryAssociation(
    name="goalModel15",
    ends={
        Property(name="GoalModel17", type=gore_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration16", type=gore_GoalModel, multiplicity=Multiplicity(0, 1))
    }
)
indicator18: BinaryAssociation = BinaryAssociation(
    name="indicator18",
    ends={
        Property(name="gore_AwReq19", type=gore_DifferentialRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="gore_DifferentialRelation", type=gore_AwReq, multiplicity=Multiplicity(0, 1))
    }
)
parameter20: BinaryAssociation = BinaryAssociation(
    name="parameter20",
    ends={
        Property(name="gore_Parameter", type=gore_DifferentialRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="gore_DifferentialRelation21", type=gore_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
goalModel11: BinaryAssociation = BinaryAssociation(
    name="goalModel11",
    ends={
        Property(name="GoalModel", type=gore_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="rootGoal", type=gore_GoalModel, multiplicity=Multiplicity(0, 1))
    }
)
rootGoal22: BinaryAssociation = BinaryAssociation(
    name="rootGoal22",
    ends={
        Property(name="Goal", type=gore_GoalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="goalModel", type=gore_Goal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actors23: BinaryAssociation = BinaryAssociation(
    name="actors23",
    ends={
        Property(name="Actor", type=gore_GoalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="goalModel24", type=gore_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration25: BinaryAssociation = BinaryAssociation(
    name="configuration25",
    ends={
        Property(name="Configuration", type=gore_GoalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="goalModel26", type=gore_Configuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relations27: BinaryAssociation = BinaryAssociation(
    name="relations27",
    ends={
        Property(name="gore_DifferentialRelation28", type=gore_GoalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gore_GoalModel", type=gore_DifferentialRelation, multiplicity=Multiplicity(0, 9999))
    }
)
configuration29: BinaryAssociation = BinaryAssociation(
    name="configuration29",
    ends={
        Property(name="Configuration30", type=gore_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=gore_Configuration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gore_Requirement_OclAny = Generalization(general=OclAny, specific=gore_Requirement)
gen_gore_DefinableRequirement_Requirement = Generalization(general=Requirement, specific=gore_DefinableRequirement)
gen_gore_Softgoal_Requirement = Generalization(general=Requirement, specific=gore_Softgoal)
gen_gore_PerformativeRequirement_DefinableRequirement = Generalization(general=DefinableRequirement, specific=gore_PerformativeRequirement)
gen_gore_QualityConstraint_DefinableRequirement = Generalization(general=DefinableRequirement, specific=gore_QualityConstraint)
gen_gore_AwReq_DefinableRequirement = Generalization(general=DefinableRequirement, specific=gore_AwReq)
gen_gore_DomainAssumption_DefinableRequirement = Generalization(general=DefinableRequirement, specific=gore_DomainAssumption)
gen_gore_Goal_PerformativeRequirement = Generalization(general=PerformativeRequirement, specific=gore_Goal)
gen_gore_Task_PerformativeRequirement = Generalization(general=PerformativeRequirement, specific=gore_Task)

# Domain Model
domain_model = DomainModel(
    name="gore",
    types={gore_Requirement, OclAny, gore_DefinableRequirement, Requirement, gore_Softgoal, gore_QualityConstraint, gore_PerformativeRequirement, DefinableRequirement, gore_AwReq, gore_DomainAssumption, gore_Goal, PerformativeRequirement, gore_Actor, gore_Configuration, gore_Parameter, gore_DifferentialRelation, gore_GoalModel, gore_Task, DefinableRequirementState, DifferentialRelationOperator, MonitorableMethod, ParameterMetric, ParameterType, RefinementType, AggregationLevel},
    associations={children1, parent3, constraints5, softgoal6, otherTargets7, target8, goalModel12, parameters14, goalModel15, indicator18, parameter20, goalModel11, rootGoal22, actors23, configuration25, relations27, configuration29},
    generalizations={gen_gore_Requirement_OclAny, gen_gore_DefinableRequirement_Requirement, gen_gore_Softgoal_Requirement, gen_gore_PerformativeRequirement_DefinableRequirement, gen_gore_QualityConstraint_DefinableRequirement, gen_gore_AwReq_DefinableRequirement, gen_gore_DomainAssumption_DefinableRequirement, gen_gore_Goal_PerformativeRequirement, gen_gore_Task_PerformativeRequirement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)