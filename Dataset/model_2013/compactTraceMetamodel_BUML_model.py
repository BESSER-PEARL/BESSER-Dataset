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
ParamterKindEnum: Enumeration = Enumeration(
    name="ParamterKindEnum",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="RETURN")
    }
)

# Classes
trace_State = Class(name="trace::State")
trace_StepType = Class(name="trace::StepType")
trace_StepPattern = Class(name="trace::StepPattern")
trace_ObjectState = Class(name="trace::ObjectState", is_abstract=True)
trace_RepeatingStep = Class(name="trace::RepeatingStep")
trace_Step = Class(name="trace::Step", is_abstract=True)
trace_ParameterValue = Class(name="trace::ParameterValue")
trace_ParameterList = Class(name="trace::ParameterList", is_abstract=True)
trace_LiteralValue = Class(name="trace::LiteralValue", is_abstract=True)
Value = Class(name="Value")
trace_Value = Class(name="trace::Value", is_abstract=True)
trace_TransientObject = Class(name="trace::TransientObject", is_abstract=True)
trace_Trace = Class(name="trace::Trace")
trace_NormalStep = Class(name="trace::NormalStep")
Step = Class(name="Step")
StepSpec = Class(name="StepSpec")
trace_PatternOcurrence = Class(name="trace::PatternOcurrence")
trace_PatternOccurrenceStepData = Class(name="trace::PatternOccurrenceStepData")
trace_RefValue = Class(name="trace::RefValue")
trace_EObject = Class(name="trace::EObject")
trace_TransientObjectState = Class(name="trace::TransientObjectState")
trace_LiteralBoolean = Class(name="trace::LiteralBoolean")
trace_LiteralInteger = Class(name="trace::LiteralInteger")
trace_LiteralFloat = Class(name="trace::LiteralFloat")
trace_EStructuralFeature = Class(name="trace::EStructuralFeature")
trace_LeafObjectState = Class(name="trace::LeafObjectState")
ObjectState = Class(name="ObjectState")
trace_StepSpec = Class(name="trace::StepSpec", is_abstract=True)
trace_LiteralString = Class(name="trace::LiteralString")
LiteralValue = Class(name="LiteralValue")
trace_EClass = Class(name="trace::EClass")
trace_CompositParameterList = Class(name="trace::CompositParameterList")
ParameterList = Class(name="ParameterList")
trace_LeafParameterList = Class(name="trace::LeafParameterList")
trace_CompositeObjectState = Class(name="trace::CompositeObjectState")
trace_StaticTransientObject = Class(name="trace::StaticTransientObject")
TransientObject = Class(name="TransientObject")
trace_DynamicTransientObject = Class(name="trace::DynamicTransientObject")

# trace_State class attributes and methods

# trace_StepType class attributes and methods
trace_StepType_stepName: Property = Property(name="stepName", type=StringType)
trace_StepType.attributes={trace_StepType_stepName}

# trace_StepPattern class attributes and methods

# trace_ObjectState class attributes and methods

# trace_RepeatingStep class attributes and methods

# trace_Step class attributes and methods

# trace_ParameterValue class attributes and methods
trace_ParameterValue_DirectionKind: Property = Property(name="DirectionKind", type=StringType)
trace_ParameterValue.attributes={trace_ParameterValue_DirectionKind}

# trace_ParameterList class attributes and methods

# trace_LiteralValue class attributes and methods

# Value class attributes and methods

# trace_Value class attributes and methods

# trace_TransientObject class attributes and methods

# trace_Trace class attributes and methods

# trace_NormalStep class attributes and methods

# Step class attributes and methods

# StepSpec class attributes and methods

# trace_PatternOcurrence class attributes and methods
trace_PatternOcurrence_repet: Property = Property(name="repet", type=IntegerType)
trace_PatternOcurrence.attributes={trace_PatternOcurrence_repet}

# trace_PatternOccurrenceStepData class attributes and methods

# trace_RefValue class attributes and methods

# trace_EObject class attributes and methods

# trace_TransientObjectState class attributes and methods

# trace_LiteralBoolean class attributes and methods
trace_LiteralBoolean_boolvalue: Property = Property(name="boolvalue", type=BooleanType)
trace_LiteralBoolean.attributes={trace_LiteralBoolean_boolvalue}

# trace_LiteralInteger class attributes and methods
trace_LiteralInteger_intvalue: Property = Property(name="intvalue", type=IntegerType)
trace_LiteralInteger.attributes={trace_LiteralInteger_intvalue}

# trace_LiteralFloat class attributes and methods
trace_LiteralFloat_floatvalue: Property = Property(name="floatvalue", type=FloatType)
trace_LiteralFloat.attributes={trace_LiteralFloat_floatvalue}

# trace_EStructuralFeature class attributes and methods

# trace_LeafObjectState class attributes and methods

# ObjectState class attributes and methods

# trace_StepSpec class attributes and methods

# trace_LiteralString class attributes and methods
trace_LiteralString_stringvalue: Property = Property(name="stringvalue", type=StringType)
trace_LiteralString.attributes={trace_LiteralString_stringvalue}

# LiteralValue class attributes and methods

# trace_EClass class attributes and methods

# trace_CompositParameterList class attributes and methods
trace_CompositParameterList_paramtervaluesOrder: Property = Property(name="paramtervaluesOrder", type=IntegerType)
trace_CompositParameterList.attributes={trace_CompositParameterList_paramtervaluesOrder}

# ParameterList class attributes and methods

# trace_LeafParameterList class attributes and methods

# trace_CompositeObjectState class attributes and methods
trace_CompositeObjectState_objectstatesOrder: Property = Property(name="objectstatesOrder", type=IntegerType)
trace_CompositeObjectState.attributes={trace_CompositeObjectState_objectstatesOrder}

# trace_StaticTransientObject class attributes and methods

# TransientObject class attributes and methods

# trace_DynamicTransientObject class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="trace_State", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transientobject1: BinaryAssociation = BinaryAssociation(
    name="transientobject1",
    ends={
        Property(name="trace_TransientObject", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_TransientObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steptype3: BinaryAssociation = BinaryAssociation(
    name="steptype3",
    ends={
        Property(name="trace_StepType", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_StepType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steppattern5: BinaryAssociation = BinaryAssociation(
    name="steppattern5",
    ends={
        Property(name="trace_StepPattern", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace6", type=trace_StepPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="trace_Value", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace8", type=trace_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectstate9: BinaryAssociation = BinaryAssociation(
    name="objectstate9",
    ends={
        Property(name="trace_ObjectState", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace10", type=trace_ObjectState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repeatingstep11: BinaryAssociation = BinaryAssociation(
    name="repeatingstep11",
    ends={
        Property(name="trace_RepeatingStep", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace12", type=trace_RepeatingStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
step13: BinaryAssociation = BinaryAssociation(
    name="step13",
    ends={
        Property(name="trace_Step", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace14", type=trace_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValues15: BinaryAssociation = BinaryAssociation(
    name="parameterValues15",
    ends={
        Property(name="trace_ParameterValue", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace16", type=trace_ParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterlist17: BinaryAssociation = BinaryAssociation(
    name="parameterlist17",
    ends={
        Property(name="trace_ParameterList", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace18", type=trace_ParameterList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transientObjectsStates32: BinaryAssociation = BinaryAssociation(
    name="transientObjectsStates32",
    ends={
        Property(name="trace_State33", type=trace_TransientObjectState, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="trace_TransientObjectState", type=trace_State, multiplicity=Multiplicity(1, 1))
    }
)
children34: BinaryAssociation = BinaryAssociation(
    name="children34",
    ends={
        Property(name="Step", type=trace_NormalStep, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=trace_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state35: BinaryAssociation = BinaryAssociation(
    name="state35",
    ends={
        Property(name="trace_State37", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Step36", type=trace_State, multiplicity=Multiplicity(0, 1))
    }
)
parent38: BinaryAssociation = BinaryAssociation(
    name="parent38",
    ends={
        Property(name="NormalStep", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=trace_NormalStep, multiplicity=Multiplicity(0, 1))
    }
)
parameterlist39: BinaryAssociation = BinaryAssociation(
    name="parameterlist39",
    ends={
        Property(name="trace_ParameterList41", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Step40", type=trace_ParameterList, multiplicity=Multiplicity(0, 1))
    }
)
pattern42: BinaryAssociation = BinaryAssociation(
    name="pattern42",
    ends={
        Property(name="trace_StepPattern43", type=trace_PatternOcurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_PatternOcurrence", type=trace_StepPattern, multiplicity=Multiplicity(1, 1))
    }
)
stepdata44: BinaryAssociation = BinaryAssociation(
    name="stepdata44",
    ends={
        Property(name="trace_PatternOccurrenceStepData", type=trace_PatternOcurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_PatternOcurrence45", type=trace_PatternOccurrenceStepData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repeatingstep46: BinaryAssociation = BinaryAssociation(
    name="repeatingstep46",
    ends={
        Property(name="trace_RepeatingStep48", type=trace_StepPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StepPattern47", type=trace_RepeatingStep, multiplicity=Multiplicity(0, 9999))
    }
)
states49: BinaryAssociation = BinaryAssociation(
    name="states49",
    ends={
        Property(name="trace_State51", type=trace_PatternOccurrenceStepData, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_PatternOccurrenceStepData50", type=trace_State, multiplicity=Multiplicity(0, 9999))
    }
)
value19: BinaryAssociation = BinaryAssociation(
    name="value19",
    ends={
        Property(name="trace_Value21", type=trace_ObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ObjectState20", type=trace_Value, multiplicity=Multiplicity(0, 9999))
    }
)
step52: BinaryAssociation = BinaryAssociation(
    name="step52",
    ends={
        Property(name="trace_RepeatingStep54", type=trace_PatternOccurrenceStepData, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_PatternOccurrenceStepData53", type=trace_RepeatingStep, multiplicity=Multiplicity(0, 1))
    }
)
parameterlists55: BinaryAssociation = BinaryAssociation(
    name="parameterlists55",
    ends={
        Property(name="trace_ParameterList57", type=trace_PatternOccurrenceStepData, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_PatternOccurrenceStepData56", type=trace_ParameterList, multiplicity=Multiplicity(0, 9999))
    }
)
originalobject22: BinaryAssociation = BinaryAssociation(
    name="originalobject22",
    ends={
        Property(name="trace_EObject", type=trace_RefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_RefValue", type=trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
newobjects23: BinaryAssociation = BinaryAssociation(
    name="newobjects23",
    ends={
        Property(name="trace_TransientObject25", type=trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_State24", type=trace_TransientObject, multiplicity=Multiplicity(0, 9999))
    }
)
deletedobjects26: BinaryAssociation = BinaryAssociation(
    name="deletedobjects26",
    ends={
        Property(name="trace_TransientObject28", type=trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_State27", type=trace_TransientObject, multiplicity=Multiplicity(0, 9999))
    }
)
basestate30: BinaryAssociation = BinaryAssociation(
    name="basestate30",
    ends={
        Property(name="trace_State31", type=trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_State29", type=trace_State, multiplicity=Multiplicity(0, 1))
    }
)
children61: BinaryAssociation = BinaryAssociation(
    name="children61",
    ends={
        Property(name="RepeatingStep", type=trace_RepeatingStep, multiplicity=Multiplicity(1, 1)),
        Property(name="parent62", type=trace_RepeatingStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent64: BinaryAssociation = BinaryAssociation(
    name="parent64",
    ends={
        Property(name="RepeatingStep66", type=trace_RepeatingStep, multiplicity=Multiplicity(1, 1)),
        Property(name="children65", type=trace_RepeatingStep, multiplicity=Multiplicity(0, 1))
    }
)
values67: BinaryAssociation = BinaryAssociation(
    name="values67",
    ends={
        Property(name="trace_Value69", type=trace_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ParameterValue68", type=trace_Value, multiplicity=Multiplicity(0, 9999))
    }
)
transientobject70: BinaryAssociation = BinaryAssociation(
    name="transientobject70",
    ends={
        Property(name="trace_TransientObject72", type=trace_TransientObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TransientObjectState71", type=trace_TransientObject, multiplicity=Multiplicity(1, 1))
    }
)
objectstate73: BinaryAssociation = BinaryAssociation(
    name="objectstate73",
    ends={
        Property(name="trace_ObjectState75", type=trace_TransientObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TransientObjectState74", type=trace_ObjectState, multiplicity=Multiplicity(1, 1))
    }
)
estructuralfeature76: BinaryAssociation = BinaryAssociation(
    name="estructuralfeature76",
    ends={
        Property(name="trace_EStructuralFeature", type=trace_TransientObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TransientObjectState77", type=trace_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
steptype58: BinaryAssociation = BinaryAssociation(
    name="steptype58",
    ends={
        Property(name="trace_StepType59", type=trace_StepSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StepSpec", type=trace_StepType, multiplicity=Multiplicity(1, 1))
    }
)
type82: BinaryAssociation = BinaryAssociation(
    name="type82",
    ends={
        Property(name="trace_EClass", type=trace_DynamicTransientObject, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_DynamicTransientObject", type=trace_EClass, multiplicity=Multiplicity(0, 1))
    }
)
parameterlist83: BinaryAssociation = BinaryAssociation(
    name="parameterlist83",
    ends={
        Property(name="trace_ParameterList84", type=trace_CompositParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_CompositParameterList", type=trace_ParameterList, multiplicity=Multiplicity(0, 9999))
    }
)
parametervalue85: BinaryAssociation = BinaryAssociation(
    name="parametervalue85",
    ends={
        Property(name="trace_ParameterValue87", type=trace_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ParameterList86", type=trace_ParameterValue, multiplicity=Multiplicity(0, 9999))
    }
)
objectstates78: BinaryAssociation = BinaryAssociation(
    name="objectstates78",
    ends={
        Property(name="trace_ObjectState79", type=trace_CompositeObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_CompositeObjectState", type=trace_ObjectState, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject80: BinaryAssociation = BinaryAssociation(
    name="originalObject80",
    ends={
        Property(name="trace_EObject81", type=trace_StaticTransientObject, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticTransientObject", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_trace_LiteralValue_Value = Generalization(general=Value, specific=trace_LiteralValue)
gen_trace_NormalStep_Step = Generalization(general=Step, specific=trace_NormalStep)
gen_trace_NormalStep_StepSpec = Generalization(general=StepSpec, specific=trace_NormalStep)
gen_trace_PatternOcurrence_Step = Generalization(general=Step, specific=trace_PatternOcurrence)
gen_trace_RefValue_Value = Generalization(general=Value, specific=trace_RefValue)
gen_trace_LiteralBoolean_LiteralValue = Generalization(general=LiteralValue, specific=trace_LiteralBoolean)
gen_trace_LiteralInteger_LiteralValue = Generalization(general=LiteralValue, specific=trace_LiteralInteger)
gen_trace_LiteralFloat_LiteralValue = Generalization(general=LiteralValue, specific=trace_LiteralFloat)
gen_trace_RepeatingStep_StepSpec = Generalization(general=StepSpec, specific=trace_RepeatingStep)
gen_trace_LeafObjectState_ObjectState = Generalization(general=ObjectState, specific=trace_LeafObjectState)
gen_trace_LiteralString_LiteralValue = Generalization(general=LiteralValue, specific=trace_LiteralString)
gen_trace_CompositParameterList_ParameterList = Generalization(general=ParameterList, specific=trace_CompositParameterList)
gen_trace_LeafParameterList_ParameterList = Generalization(general=ParameterList, specific=trace_LeafParameterList)
gen_trace_CompositeObjectState_ObjectState = Generalization(general=ObjectState, specific=trace_CompositeObjectState)
gen_trace_StaticTransientObject_TransientObject = Generalization(general=TransientObject, specific=trace_StaticTransientObject)
gen_trace_DynamicTransientObject_TransientObject = Generalization(general=TransientObject, specific=trace_DynamicTransientObject)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_State, trace_StepType, trace_StepPattern, trace_ObjectState, trace_RepeatingStep, trace_Step, trace_ParameterValue, trace_ParameterList, trace_LiteralValue, Value, trace_Value, trace_TransientObject, trace_Trace, trace_NormalStep, Step, StepSpec, trace_PatternOcurrence, trace_PatternOccurrenceStepData, trace_RefValue, trace_EObject, trace_TransientObjectState, trace_LiteralBoolean, trace_LiteralInteger, trace_LiteralFloat, trace_EStructuralFeature, trace_LeafObjectState, ObjectState, trace_StepSpec, trace_LiteralString, LiteralValue, trace_EClass, trace_CompositParameterList, ParameterList, trace_LeafParameterList, trace_CompositeObjectState, trace_StaticTransientObject, TransientObject, trace_DynamicTransientObject, ParamterKindEnum},
    associations={state0, transientobject1, steptype3, steppattern5, value7, objectstate9, repeatingstep11, step13, parameterValues15, parameterlist17, transientObjectsStates32, children34, state35, parent38, parameterlist39, pattern42, stepdata44, repeatingstep46, states49, value19, step52, parameterlists55, originalobject22, newobjects23, deletedobjects26, basestate30, children61, parent64, values67, transientobject70, objectstate73, estructuralfeature76, steptype58, type82, parameterlist83, parametervalue85, objectstates78, originalObject80},
    generalizations={gen_trace_LiteralValue_Value, gen_trace_NormalStep_Step, gen_trace_NormalStep_StepSpec, gen_trace_PatternOcurrence_Step, gen_trace_RefValue_Value, gen_trace_LiteralBoolean_LiteralValue, gen_trace_LiteralInteger_LiteralValue, gen_trace_LiteralFloat_LiteralValue, gen_trace_RepeatingStep_StepSpec, gen_trace_LeafObjectState_ObjectState, gen_trace_LiteralString_LiteralValue, gen_trace_CompositParameterList_ParameterList, gen_trace_LeafParameterList_ParameterList, gen_trace_CompositeObjectState_ObjectState, gen_trace_StaticTransientObject_TransientObject, gen_trace_DynamicTransientObject_TransientObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)