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

# Classes
trnetvisual_TrNetModel = Class(name="trnetvisual::TrNetModel")
trnetvisual_Pattern = Class(name="trnetvisual::Pattern")
trnetvisual_Operator = Class(name="trnetvisual::Operator", is_abstract=True)
trnetvisual_Restriction = Class(name="trnetvisual::Restriction", is_abstract=True)
trnetvisual_Keep = Class(name="trnetvisual::Keep")
trnetvisual_Different = Class(name="trnetvisual::Different")
trnetvisual_Operand = Class(name="trnetvisual::Operand", is_abstract=True)
trnetvisual_Result = Class(name="trnetvisual::Result", is_abstract=True)
trnetvisual_FlowRule = Class(name="trnetvisual::FlowRule", is_abstract=True)
trnetvisual_Calculation = Class(name="trnetvisual::Calculation", is_abstract=True)
trnetvisual_NodePattern = Class(name="trnetvisual::NodePattern", is_abstract=True)
Parameter_ = Class(name="Parameter")
trnetvisual_EdgePattern = Class(name="trnetvisual::EdgePattern")
trnetvisual_Same = Class(name="trnetvisual::Same")
trnetvisual_AttributePattern = Class(name="trnetvisual::AttributePattern")
Restriction = Class(name="Restriction")
trnetvisual_External = Class(name="trnetvisual::External")
trnetvisual_ExternalAttributeCalculationCall = Class(name="trnetvisual::ExternalAttributeCalculationCall")
trnetvisual_MandatoryNode = Class(name="trnetvisual::MandatoryNode")
NodePattern = Class(name="NodePattern")
trnetvisual_OptionalNode = Class(name="trnetvisual::OptionalNode")
trnetvisual_Combinator = Class(name="trnetvisual::Combinator")
Operator = Class(name="Operator")
trnetvisual_AnyOperand = Class(name="trnetvisual::AnyOperand")
Operand = Class(name="Operand")
trnetvisual_SomeOperand = Class(name="trnetvisual::SomeOperand")
trnetvisual_AntiOperand = Class(name="trnetvisual::AntiOperand")
trnetvisual_OptionalOperand = Class(name="trnetvisual::OptionalOperand")
trnetvisual_ApplicationCondition = Class(name="trnetvisual::ApplicationCondition", is_abstract=True)
trnetvisual_Action = Class(name="trnetvisual::Action", is_abstract=True)
trnetvisual_AnyResult = Class(name="trnetvisual::AnyResult")
Result = Class(name="Result")
trnetvisual_SomeResult = Class(name="trnetvisual::SomeResult")
trnetvisual_ExternalActionCallParameter = Class(name="trnetvisual::ExternalActionCallParameter")
trnetvisual_ExternalCalculationCallParameter = Class(name="trnetvisual::ExternalCalculationCallParameter")
trnetvisual_ExternalConditionCall = Class(name="trnetvisual::ExternalConditionCall")
ApplicationCondition = Class(name="ApplicationCondition")
trnetvisual_Next = Class(name="trnetvisual::Next")
FlowRule = Class(name="FlowRule")
trnetvisual_Eventually = Class(name="trnetvisual::Eventually")
trnetvisual_NextDerived = Class(name="trnetvisual::NextDerived")
trnetvisual_AttributeCalculation = Class(name="trnetvisual::AttributeCalculation", is_abstract=True)
AttributeCalculation = Class(name="AttributeCalculation")
trnetvisual_ExternalAttributeCalculationCallParameter = Class(name="trnetvisual::ExternalAttributeCalculationCallParameter")
trnetvisual_Parameter = Class(name="trnetvisual::Parameter", is_abstract=True)
trnetvisual_ExternalConditionCallParameter = Class(name="trnetvisual::ExternalConditionCallParameter")
trnetvisual_ParameterRef = Class(name="trnetvisual::ParameterRef")
trnetvisual_ExternalActionCall = Class(name="trnetvisual::ExternalActionCall")
Action = Class(name="Action")
ParameterRef = Class(name="ParameterRef")
trnetvisual_ExternalCalculationCall = Class(name="trnetvisual::ExternalCalculationCall")
Calculation = Class(name="Calculation")

# trnetvisual_TrNetModel class attributes and methods
trnetvisual_TrNetModel_id: Property = Property(name="id", type=StringType)
trnetvisual_TrNetModel.attributes={trnetvisual_TrNetModel_id}

# trnetvisual_Pattern class attributes and methods
trnetvisual_Pattern_id: Property = Property(name="id", type=StringType)
trnetvisual_Pattern_expected_size: Property = Property(name="expected_size", type=FloatType)
trnetvisual_Pattern.attributes={trnetvisual_Pattern_expected_size, trnetvisual_Pattern_id}

# trnetvisual_Operator class attributes and methods
trnetvisual_Operator_id: Property = Property(name="id", type=StringType)
trnetvisual_Operator.attributes={trnetvisual_Operator_id}

# trnetvisual_Restriction class attributes and methods

# trnetvisual_Keep class attributes and methods

# trnetvisual_Different class attributes and methods

# trnetvisual_Operand class attributes and methods
trnetvisual_Operand_index: Property = Property(name="index", type=IntegerType)
trnetvisual_Operand.attributes={trnetvisual_Operand_index}

# trnetvisual_Result class attributes and methods

# trnetvisual_FlowRule class attributes and methods

# trnetvisual_Calculation class attributes and methods

# trnetvisual_NodePattern class attributes and methods
trnetvisual_NodePattern_name: Property = Property(name="name", type=StringType)
trnetvisual_NodePattern_id: Property = Property(name="id", type=StringType)
trnetvisual_NodePattern_expectedNumberOfDistinctValues: Property = Property(name="expectedNumberOfDistinctValues", type=FloatType)
trnetvisual_NodePattern.attributes={trnetvisual_NodePattern_id, trnetvisual_NodePattern_expectedNumberOfDistinctValues, trnetvisual_NodePattern_name}

# Parameter class attributes and methods

# trnetvisual_EdgePattern class attributes and methods
trnetvisual_EdgePattern_name: Property = Property(name="name", type=StringType)
trnetvisual_EdgePattern.attributes={trnetvisual_EdgePattern_name}

# trnetvisual_Same class attributes and methods

# trnetvisual_AttributePattern class attributes and methods
trnetvisual_AttributePattern_name: Property = Property(name="name", type=StringType)
trnetvisual_AttributePattern_expectedNumberOfDistinctValues: Property = Property(name="expectedNumberOfDistinctValues", type=FloatType)
trnetvisual_AttributePattern.attributes={trnetvisual_AttributePattern_expectedNumberOfDistinctValues, trnetvisual_AttributePattern_name}

# Restriction class attributes and methods

# trnetvisual_External class attributes and methods

# trnetvisual_ExternalAttributeCalculationCall class attributes and methods
trnetvisual_ExternalAttributeCalculationCall_id: Property = Property(name="id", type=StringType)
trnetvisual_ExternalAttributeCalculationCall_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
trnetvisual_ExternalAttributeCalculationCall.attributes={trnetvisual_ExternalAttributeCalculationCall_qualifiedName, trnetvisual_ExternalAttributeCalculationCall_id}

# trnetvisual_MandatoryNode class attributes and methods

# NodePattern class attributes and methods

# trnetvisual_OptionalNode class attributes and methods

# trnetvisual_Combinator class attributes and methods

# Operator class attributes and methods

# trnetvisual_AnyOperand class attributes and methods

# Operand class attributes and methods

# trnetvisual_SomeOperand class attributes and methods
trnetvisual_SomeOperand_count: Property = Property(name="count", type=IntegerType)
trnetvisual_SomeOperand.attributes={trnetvisual_SomeOperand_count}

# trnetvisual_AntiOperand class attributes and methods

# trnetvisual_OptionalOperand class attributes and methods

# trnetvisual_ApplicationCondition class attributes and methods

# trnetvisual_Action class attributes and methods

# trnetvisual_AnyResult class attributes and methods

# Result class attributes and methods

# trnetvisual_SomeResult class attributes and methods
trnetvisual_SomeResult_count: Property = Property(name="count", type=IntegerType)
trnetvisual_SomeResult.attributes={trnetvisual_SomeResult_count}

# trnetvisual_ExternalActionCallParameter class attributes and methods

# trnetvisual_ExternalCalculationCallParameter class attributes and methods

# trnetvisual_ExternalConditionCall class attributes and methods
trnetvisual_ExternalConditionCall_id: Property = Property(name="id", type=StringType)
trnetvisual_ExternalConditionCall_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
trnetvisual_ExternalConditionCall.attributes={trnetvisual_ExternalConditionCall_qualifiedName, trnetvisual_ExternalConditionCall_id}

# ApplicationCondition class attributes and methods

# trnetvisual_Next class attributes and methods

# FlowRule class attributes and methods

# trnetvisual_Eventually class attributes and methods

# trnetvisual_NextDerived class attributes and methods

# trnetvisual_AttributeCalculation class attributes and methods

# AttributeCalculation class attributes and methods

# trnetvisual_ExternalAttributeCalculationCallParameter class attributes and methods

# trnetvisual_Parameter class attributes and methods

# trnetvisual_ExternalConditionCallParameter class attributes and methods

# trnetvisual_ParameterRef class attributes and methods
trnetvisual_ParameterRef_index: Property = Property(name="index", type=IntegerType)
trnetvisual_ParameterRef.attributes={trnetvisual_ParameterRef_index}

# trnetvisual_ExternalActionCall class attributes and methods
trnetvisual_ExternalActionCall_id: Property = Property(name="id", type=StringType)
trnetvisual_ExternalActionCall_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
trnetvisual_ExternalActionCall.attributes={trnetvisual_ExternalActionCall_qualifiedName, trnetvisual_ExternalActionCall_id}

# Action class attributes and methods

# ParameterRef class attributes and methods

# trnetvisual_ExternalCalculationCall class attributes and methods
trnetvisual_ExternalCalculationCall_id: Property = Property(name="id", type=StringType)
trnetvisual_ExternalCalculationCall_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
trnetvisual_ExternalCalculationCall.attributes={trnetvisual_ExternalCalculationCall_id, trnetvisual_ExternalCalculationCall_qualifiedName}

# Calculation class attributes and methods

# Relationships
patterns0: BinaryAssociation = BinaryAssociation(
    name="patterns0",
    ends={
        Property(name="trnetvisual_Pattern", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel", type=trnetvisual_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operators1: BinaryAssociation = BinaryAssociation(
    name="operators1",
    ends={
        Property(name="trnetvisual_Operator", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel2", type=trnetvisual_Operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keepIn23: BinaryAssociation = BinaryAssociation(
    name="keepIn23",
    ends={
        Property(name="Keep", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target24", type=trnetvisual_Keep, multiplicity=Multiplicity(0, 9999))
    }
)
keepOut25: BinaryAssociation = BinaryAssociation(
    name="keepOut25",
    ends={
        Property(name="Keep27", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source26", type=trnetvisual_Keep, multiplicity=Multiplicity(0, 9999))
    }
)
differentIn28: BinaryAssociation = BinaryAssociation(
    name="differentIn28",
    ends={
        Property(name="Different", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target29", type=trnetvisual_Different, multiplicity=Multiplicity(0, 9999))
    }
)
differentOut30: BinaryAssociation = BinaryAssociation(
    name="differentOut30",
    ends={
        Property(name="Different32", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source31", type=trnetvisual_Different, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions3: BinaryAssociation = BinaryAssociation(
    name="restrictions3",
    ends={
        Property(name="trnetvisual_Restriction", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel4", type=trnetvisual_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands5: BinaryAssociation = BinaryAssociation(
    name="operands5",
    ends={
        Property(name="trnetvisual_Operand", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel6", type=trnetvisual_Operand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
results7: BinaryAssociation = BinaryAssociation(
    name="results7",
    ends={
        Property(name="trnetvisual_Result", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel8", type=trnetvisual_Result, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowRules9: BinaryAssociation = BinaryAssociation(
    name="flowRules9",
    ends={
        Property(name="trnetvisual_FlowRule", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel10", type=trnetvisual_FlowRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calculations11: BinaryAssociation = BinaryAssociation(
    name="calculations11",
    ends={
        Property(name="trnetvisual_Calculation", type=trnetvisual_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_TrNetModel12", type=trnetvisual_Calculation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming13: BinaryAssociation = BinaryAssociation(
    name="incoming13",
    ends={
        Property(name="EdgePattern", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=trnetvisual_EdgePattern, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing14: BinaryAssociation = BinaryAssociation(
    name="outgoing14",
    ends={
        Property(name="EdgePattern15", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=trnetvisual_EdgePattern, multiplicity=Multiplicity(0, 9999))
    }
)
sameOut16: BinaryAssociation = BinaryAssociation(
    name="sameOut16",
    ends={
        Property(name="Same", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source17", type=trnetvisual_Same, multiplicity=Multiplicity(0, 9999))
    }
)
sameIn18: BinaryAssociation = BinaryAssociation(
    name="sameIn18",
    ends={
        Property(name="Same20", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target19", type=trnetvisual_Same, multiplicity=Multiplicity(0, 9999))
    }
)
pattern21: BinaryAssociation = BinaryAssociation(
    name="pattern21",
    ends={
        Property(name="Pattern", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
attributes22: BinaryAssociation = BinaryAssociation(
    name="attributes22",
    ends={
        Property(name="AttributePattern", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerNode", type=trnetvisual_AttributePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source47: BinaryAssociation = BinaryAssociation(
    name="source47",
    ends={
        Property(name="NodePattern48", type=trnetvisual_Same, multiplicity=Multiplicity(1, 1)),
        Property(name="sameOut", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target49: BinaryAssociation = BinaryAssociation(
    name="target49",
    ends={
        Property(name="NodePattern50", type=trnetvisual_Same, multiplicity=Multiplicity(1, 1)),
        Property(name="sameIn", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
source51: BinaryAssociation = BinaryAssociation(
    name="source51",
    ends={
        Property(name="NodePattern52", type=trnetvisual_Different, multiplicity=Multiplicity(1, 1)),
        Property(name="differentOut", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="NodePattern", type=trnetvisual_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target34: BinaryAssociation = BinaryAssociation(
    name="target34",
    ends={
        Property(name="NodePattern35", type=trnetvisual_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
pattern36: BinaryAssociation = BinaryAssociation(
    name="pattern36",
    ends={
        Property(name="Pattern37", type=trnetvisual_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
nodes38: BinaryAssociation = BinaryAssociation(
    name="nodes38",
    ends={
        Property(name="NodePattern39", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edges40: BinaryAssociation = BinaryAssociation(
    name="edges40",
    ends={
        Property(name="EdgePattern42", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern41", type=trnetvisual_EdgePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingResults43: BinaryAssociation = BinaryAssociation(
    name="incomingResults43",
    ends={
        Property(name="Result", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern44", type=trnetvisual_Result, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingOperands45: BinaryAssociation = BinaryAssociation(
    name="outgoingOperands45",
    ends={
        Property(name="Operand", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern46", type=trnetvisual_Operand, multiplicity=Multiplicity(0, 9999))
    }
)
operands62: BinaryAssociation = BinaryAssociation(
    name="operands62",
    ends={
        Property(name="Operand63", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operator", type=trnetvisual_Operand, multiplicity=Multiplicity(0, 9999))
    }
)
results64: BinaryAssociation = BinaryAssociation(
    name="results64",
    ends={
        Property(name="Result66", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operator65", type=trnetvisual_Result, multiplicity=Multiplicity(0, 9999))
    }
)
target53: BinaryAssociation = BinaryAssociation(
    name="target53",
    ends={
        Property(name="NodePattern54", type=trnetvisual_Different, multiplicity=Multiplicity(1, 1)),
        Property(name="differentIn", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
attributeExternalCalculationCall55: BinaryAssociation = BinaryAssociation(
    name="attributeExternalCalculationCall55",
    ends={
        Property(name="ExternalAttributeCalculationCall", type=trnetvisual_AttributePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=trnetvisual_ExternalAttributeCalculationCall, multiplicity=Multiplicity(0, 1))
    }
)
ownerNode56: BinaryAssociation = BinaryAssociation(
    name="ownerNode56",
    ends={
        Property(name="NodePattern57", type=trnetvisual_AttributePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
source58: BinaryAssociation = BinaryAssociation(
    name="source58",
    ends={
        Property(name="NodePattern59", type=trnetvisual_Keep, multiplicity=Multiplicity(1, 1)),
        Property(name="keepOut", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target60: BinaryAssociation = BinaryAssociation(
    name="target60",
    ends={
        Property(name="NodePattern61", type=trnetvisual_Keep, multiplicity=Multiplicity(1, 1)),
        Property(name="keepIn", type=trnetvisual_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
operator79: BinaryAssociation = BinaryAssociation(
    name="operator79",
    ends={
        Property(name="operands", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="Operator80", type=trnetvisual_Operand, multiplicity=Multiplicity(1, 1))
    }
)
pattern81: BinaryAssociation = BinaryAssociation(
    name="pattern81",
    ends={
        Property(name="Pattern82", type=trnetvisual_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingOperands", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
flowOut67: BinaryAssociation = BinaryAssociation(
    name="flowOut67",
    ends={
        Property(name="FlowRule", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="source68", type=trnetvisual_FlowRule, multiplicity=Multiplicity(0, 9999))
    }
)
flowIn69: BinaryAssociation = BinaryAssociation(
    name="flowIn69",
    ends={
        Property(name="FlowRule71", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="target70", type=trnetvisual_FlowRule, multiplicity=Multiplicity(0, 9999))
    }
)
conditions72: BinaryAssociation = BinaryAssociation(
    name="conditions72",
    ends={
        Property(name="trnetvisual_ApplicationCondition", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_Operator73", type=trnetvisual_ApplicationCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions74: BinaryAssociation = BinaryAssociation(
    name="actions74",
    ends={
        Property(name="trnetvisual_Action", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="trnetvisual_Operator75", type=trnetvisual_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern76: BinaryAssociation = BinaryAssociation(
    name="pattern76",
    ends={
        Property(name="Pattern77", type=trnetvisual_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingResults", type=trnetvisual_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
operator78: BinaryAssociation = BinaryAssociation(
    name="operator78",
    ends={
        Property(name="Operator", type=trnetvisual_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="results", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1))
    }
)
externalConditionCallRef92: BinaryAssociation = BinaryAssociation(
    name="externalConditionCallRef92",
    ends={
        Property(name="parameter93", type=trnetvisual_ExternalConditionCallParameter, multiplicity=Multiplicity(0, 9999)),
        Property(name="ExternalConditionCallParameter", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
externalActionCallRef94: BinaryAssociation = BinaryAssociation(
    name="externalActionCallRef94",
    ends={
        Property(name="ExternalActionCallParameter", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter95", type=trnetvisual_ExternalActionCallParameter, multiplicity=Multiplicity(0, 9999))
    }
)
externalCalculationCallRef96: BinaryAssociation = BinaryAssociation(
    name="externalCalculationCallRef96",
    ends={
        Property(name="ExternalCalculationCallParameter", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter97", type=trnetvisual_ExternalCalculationCallParameter, multiplicity=Multiplicity(0, 9999))
    }
)
source83: BinaryAssociation = BinaryAssociation(
    name="source83",
    ends={
        Property(name="Operator84", type=trnetvisual_FlowRule, multiplicity=Multiplicity(1, 1)),
        Property(name="flowOut", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1))
    }
)
target85: BinaryAssociation = BinaryAssociation(
    name="target85",
    ends={
        Property(name="Operator86", type=trnetvisual_FlowRule, multiplicity=Multiplicity(1, 1)),
        Property(name="flowIn", type=trnetvisual_Operator, multiplicity=Multiplicity(1, 1))
    }
)
result87: BinaryAssociation = BinaryAssociation(
    name="result87",
    ends={
        Property(name="AttributePattern88", type=trnetvisual_ExternalAttributeCalculationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeExternalCalculationCall", type=trnetvisual_AttributePattern, multiplicity=Multiplicity(1, 1))
    }
)
parameters89: BinaryAssociation = BinaryAssociation(
    name="parameters89",
    ends={
        Property(name="ExternalAttributeCalculationCallParameter", type=trnetvisual_ExternalAttributeCalculationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=trnetvisual_ExternalAttributeCalculationCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalAttributeCalculationCallRef90: BinaryAssociation = BinaryAssociation(
    name="externalAttributeCalculationCallRef90",
    ends={
        Property(name="ExternalAttributeCalculationCallParameter91", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=trnetvisual_ExternalAttributeCalculationCallParameter, multiplicity=Multiplicity(0, 9999))
    }
)
parameter109: BinaryAssociation = BinaryAssociation(
    name="parameter109",
    ends={
        Property(name="Parameter110", type=trnetvisual_ExternalConditionCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="externalConditionCallRef", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
owner111: BinaryAssociation = BinaryAssociation(
    name="owner111",
    ends={
        Property(name="ExternalActionCall", type=trnetvisual_ExternalActionCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters112", type=trnetvisual_ExternalActionCall, multiplicity=Multiplicity(1, 1))
    }
)
parameter113: BinaryAssociation = BinaryAssociation(
    name="parameter113",
    ends={
        Property(name="Parameter114", type=trnetvisual_ExternalActionCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="externalActionCallRef", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
parameters98: BinaryAssociation = BinaryAssociation(
    name="parameters98",
    ends={
        Property(name="ExternalConditionCallParameter100", type=trnetvisual_ExternalConditionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="owner99", type=trnetvisual_ExternalConditionCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters101: BinaryAssociation = BinaryAssociation(
    name="parameters101",
    ends={
        Property(name="ExternalActionCallParameter103", type=trnetvisual_ExternalActionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="owner102", type=trnetvisual_ExternalActionCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner104: BinaryAssociation = BinaryAssociation(
    name="owner104",
    ends={
        Property(name="ExternalAttributeCalculationCall105", type=trnetvisual_ExternalAttributeCalculationCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=trnetvisual_ExternalAttributeCalculationCall, multiplicity=Multiplicity(1, 1))
    }
)
parameter106: BinaryAssociation = BinaryAssociation(
    name="parameter106",
    ends={
        Property(name="Parameter", type=trnetvisual_ExternalAttributeCalculationCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="externalAttributeCalculationCallRef", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
owner107: BinaryAssociation = BinaryAssociation(
    name="owner107",
    ends={
        Property(name="ExternalConditionCall", type=trnetvisual_ExternalConditionCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters108", type=trnetvisual_ExternalConditionCall, multiplicity=Multiplicity(1, 1))
    }
)
parameters115: BinaryAssociation = BinaryAssociation(
    name="parameters115",
    ends={
        Property(name="ExternalCalculationCallParameter117", type=trnetvisual_ExternalCalculationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="owner116", type=trnetvisual_ExternalCalculationCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner118: BinaryAssociation = BinaryAssociation(
    name="owner118",
    ends={
        Property(name="ExternalCalculationCall", type=trnetvisual_ExternalCalculationCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters119", type=trnetvisual_ExternalCalculationCall, multiplicity=Multiplicity(1, 1))
    }
)
parameter120: BinaryAssociation = BinaryAssociation(
    name="parameter120",
    ends={
        Property(name="Parameter121", type=trnetvisual_ExternalCalculationCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="externalCalculationCallRef", type=trnetvisual_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_trnetvisual_NodePattern_Parameter = Generalization(general=Parameter_, specific=trnetvisual_NodePattern)
gen_trnetvisual_Same_Restriction = Generalization(general=Restriction, specific=trnetvisual_Same)
gen_trnetvisual_Different_Restriction = Generalization(general=Restriction, specific=trnetvisual_Different)
gen_trnetvisual_External_Operator = Generalization(general=Operator, specific=trnetvisual_External)
gen_trnetvisual_AttributePattern_Parameter = Generalization(general=Parameter_, specific=trnetvisual_AttributePattern)
gen_trnetvisual_Keep_Restriction = Generalization(general=Restriction, specific=trnetvisual_Keep)
gen_trnetvisual_MandatoryNode_NodePattern = Generalization(general=NodePattern, specific=trnetvisual_MandatoryNode)
gen_trnetvisual_OptionalNode_NodePattern = Generalization(general=NodePattern, specific=trnetvisual_OptionalNode)
gen_trnetvisual_Combinator_Operator = Generalization(general=Operator, specific=trnetvisual_Combinator)
gen_trnetvisual_AnyOperand_Operand = Generalization(general=Operand, specific=trnetvisual_AnyOperand)
gen_trnetvisual_SomeOperand_Operand = Generalization(general=Operand, specific=trnetvisual_SomeOperand)
gen_trnetvisual_AntiOperand_Operand = Generalization(general=Operand, specific=trnetvisual_AntiOperand)
gen_trnetvisual_OptionalOperand_Operand = Generalization(general=Operand, specific=trnetvisual_OptionalOperand)
gen_trnetvisual_AnyResult_Result = Generalization(general=Result, specific=trnetvisual_AnyResult)
gen_trnetvisual_SomeResult_Result = Generalization(general=Result, specific=trnetvisual_SomeResult)
gen_trnetvisual_ExternalConditionCall_ApplicationCondition = Generalization(general=ApplicationCondition, specific=trnetvisual_ExternalConditionCall)
gen_trnetvisual_Next_FlowRule = Generalization(general=FlowRule, specific=trnetvisual_Next)
gen_trnetvisual_Eventually_FlowRule = Generalization(general=FlowRule, specific=trnetvisual_Eventually)
gen_trnetvisual_NextDerived_FlowRule = Generalization(general=FlowRule, specific=trnetvisual_NextDerived)
gen_trnetvisual_AttributeCalculation_Restriction = Generalization(general=Restriction, specific=trnetvisual_AttributeCalculation)
gen_trnetvisual_ExternalAttributeCalculationCall_AttributeCalculation = Generalization(general=AttributeCalculation, specific=trnetvisual_ExternalAttributeCalculationCall)
gen_trnetvisual_ExternalActionCallParameter_ParameterRef = Generalization(general=ParameterRef, specific=trnetvisual_ExternalActionCallParameter)
gen_trnetvisual_Calculation_Parameter = Generalization(general=Parameter_, specific=trnetvisual_Calculation)
gen_trnetvisual_ExternalActionCall_Action = Generalization(general=Action, specific=trnetvisual_ExternalActionCall)
gen_trnetvisual_ExternalAttributeCalculationCallParameter_ParameterRef = Generalization(general=ParameterRef, specific=trnetvisual_ExternalAttributeCalculationCallParameter)
gen_trnetvisual_ExternalConditionCallParameter_ParameterRef = Generalization(general=ParameterRef, specific=trnetvisual_ExternalConditionCallParameter)
gen_trnetvisual_ExternalCalculationCall_Calculation = Generalization(general=Calculation, specific=trnetvisual_ExternalCalculationCall)
gen_trnetvisual_ExternalCalculationCallParameter_ParameterRef = Generalization(general=ParameterRef, specific=trnetvisual_ExternalCalculationCallParameter)

# Domain Model
domain_model = DomainModel(
    name="trnetvisual",
    types={trnetvisual_TrNetModel, trnetvisual_Pattern, trnetvisual_Operator, trnetvisual_Restriction, trnetvisual_Keep, trnetvisual_Different, trnetvisual_Operand, trnetvisual_Result, trnetvisual_FlowRule, trnetvisual_Calculation, trnetvisual_NodePattern, Parameter_, trnetvisual_EdgePattern, trnetvisual_Same, trnetvisual_AttributePattern, Restriction, trnetvisual_External, trnetvisual_ExternalAttributeCalculationCall, trnetvisual_MandatoryNode, NodePattern, trnetvisual_OptionalNode, trnetvisual_Combinator, Operator, trnetvisual_AnyOperand, Operand, trnetvisual_SomeOperand, trnetvisual_AntiOperand, trnetvisual_OptionalOperand, trnetvisual_ApplicationCondition, trnetvisual_Action, trnetvisual_AnyResult, Result, trnetvisual_SomeResult, trnetvisual_ExternalActionCallParameter, trnetvisual_ExternalCalculationCallParameter, trnetvisual_ExternalConditionCall, ApplicationCondition, trnetvisual_Next, FlowRule, trnetvisual_Eventually, trnetvisual_NextDerived, trnetvisual_AttributeCalculation, AttributeCalculation, trnetvisual_ExternalAttributeCalculationCallParameter, trnetvisual_Parameter, trnetvisual_ExternalConditionCallParameter, trnetvisual_ParameterRef, trnetvisual_ExternalActionCall, Action, ParameterRef, trnetvisual_ExternalCalculationCall, Calculation},
    associations={patterns0, operators1, keepIn23, keepOut25, differentIn28, differentOut30, restrictions3, operands5, results7, flowRules9, calculations11, incoming13, outgoing14, sameOut16, sameIn18, pattern21, attributes22, source47, target49, source51, source33, target34, pattern36, nodes38, edges40, incomingResults43, outgoingOperands45, operands62, results64, target53, attributeExternalCalculationCall55, ownerNode56, source58, target60, operator79, pattern81, flowOut67, flowIn69, conditions72, actions74, pattern76, operator78, externalConditionCallRef92, externalActionCallRef94, externalCalculationCallRef96, source83, target85, result87, parameters89, externalAttributeCalculationCallRef90, parameter109, owner111, parameter113, parameters98, parameters101, owner104, parameter106, owner107, parameters115, owner118, parameter120},
    generalizations={gen_trnetvisual_NodePattern_Parameter, gen_trnetvisual_Same_Restriction, gen_trnetvisual_Different_Restriction, gen_trnetvisual_External_Operator, gen_trnetvisual_AttributePattern_Parameter, gen_trnetvisual_Keep_Restriction, gen_trnetvisual_MandatoryNode_NodePattern, gen_trnetvisual_OptionalNode_NodePattern, gen_trnetvisual_Combinator_Operator, gen_trnetvisual_AnyOperand_Operand, gen_trnetvisual_SomeOperand_Operand, gen_trnetvisual_AntiOperand_Operand, gen_trnetvisual_OptionalOperand_Operand, gen_trnetvisual_AnyResult_Result, gen_trnetvisual_SomeResult_Result, gen_trnetvisual_ExternalConditionCall_ApplicationCondition, gen_trnetvisual_Next_FlowRule, gen_trnetvisual_Eventually_FlowRule, gen_trnetvisual_NextDerived_FlowRule, gen_trnetvisual_AttributeCalculation_Restriction, gen_trnetvisual_ExternalAttributeCalculationCall_AttributeCalculation, gen_trnetvisual_ExternalActionCallParameter_ParameterRef, gen_trnetvisual_Calculation_Parameter, gen_trnetvisual_ExternalActionCall_Action, gen_trnetvisual_ExternalAttributeCalculationCallParameter_ParameterRef, gen_trnetvisual_ExternalConditionCallParameter_ParameterRef, gen_trnetvisual_ExternalCalculationCall_Calculation, gen_trnetvisual_ExternalCalculationCallParameter_ParameterRef},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)