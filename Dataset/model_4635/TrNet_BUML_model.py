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
trnet_TrNetModel = Class(name="trnet::TrNetModel")
trnet_Pattern = Class(name="trnet::Pattern")
trnet_Operator = Class(name="trnet::Operator", is_abstract=True)
trnet_FlowRule = Class(name="trnet::FlowRule", is_abstract=True)
trnet_NodePattern = Class(name="trnet::NodePattern", is_abstract=True)
trnet_EdgePattern = Class(name="trnet::EdgePattern")
trnet_AttributePattern = Class(name="trnet::AttributePattern")
trnet_Different = Class(name="trnet::Different")
trnet_Keep = Class(name="trnet::Keep")
trnet_Operand = Class(name="trnet::Operand", is_abstract=True)
trnet_Result = Class(name="trnet::Result", is_abstract=True)
trnet_Same = Class(name="trnet::Same")
trnet_Combinator = Class(name="trnet::Combinator")
Operator = Class(name="Operator")
trnet_Restriction = Class(name="trnet::Restriction", is_abstract=True)
Restriction = Class(name="Restriction")
trnet_Expression = Class(name="trnet::Expression", is_abstract=True)
trnet_ExpressionOperator = Class(name="trnet::ExpressionOperator", is_abstract=True)
trnet_StringLiteral = Class(name="trnet::StringLiteral")
Expression = Class(name="Expression")
trnet_SomeOperand = Class(name="trnet::SomeOperand")
Operand = Class(name="Operand")
trnet_AntiOperand = Class(name="trnet::AntiOperand")
trnet_AnyOperand = Class(name="trnet::AnyOperand")
trnet_SomeResult = Class(name="trnet::SomeResult")
Result = Class(name="Result")
trnet_AnyResult = Class(name="trnet::AnyResult")
trnet_External = Class(name="trnet::External")
trnet_Union = Class(name="trnet::Union")
trnet_MandatoryNode = Class(name="trnet::MandatoryNode")
NodePattern = Class(name="NodePattern")
trnet_OptionalNode = Class(name="trnet::OptionalNode")
trnet_Equality = Class(name="trnet::Equality")
ExpressionOperator = Class(name="ExpressionOperator")
trnet_OptionalOperand = Class(name="trnet::OptionalOperand")
trnet_Next = Class(name="trnet::Next")
FlowRule = Class(name="FlowRule")
trnet_Eventually = Class(name="trnet::Eventually")
trnet_NextDerived = Class(name="trnet::NextDerived")

# trnet_TrNetModel class attributes and methods
trnet_TrNetModel_id: Property = Property(name="id", type=StringType)
trnet_TrNetModel.attributes={trnet_TrNetModel_id}

# trnet_Pattern class attributes and methods
trnet_Pattern_id: Property = Property(name="id", type=StringType)
trnet_Pattern_expected_size: Property = Property(name="expected_size", type=IntegerType)
trnet_Pattern.attributes={trnet_Pattern_id, trnet_Pattern_expected_size}

# trnet_Operator class attributes and methods
trnet_Operator_id: Property = Property(name="id", type=StringType)
trnet_Operator.attributes={trnet_Operator_id}

# trnet_FlowRule class attributes and methods

# trnet_NodePattern class attributes and methods
trnet_NodePattern_name: Property = Property(name="name", type=StringType)
trnet_NodePattern_id: Property = Property(name="id", type=StringType)
trnet_NodePattern.attributes={trnet_NodePattern_name, trnet_NodePattern_id}

# trnet_EdgePattern class attributes and methods
trnet_EdgePattern_name: Property = Property(name="name", type=StringType)
trnet_EdgePattern.attributes={trnet_EdgePattern_name}

# trnet_AttributePattern class attributes and methods
trnet_AttributePattern_name: Property = Property(name="name", type=StringType)
trnet_AttributePattern.attributes={trnet_AttributePattern_name}

# trnet_Different class attributes and methods

# trnet_Keep class attributes and methods

# trnet_Operand class attributes and methods
trnet_Operand_index: Property = Property(name="index", type=IntegerType)
trnet_Operand.attributes={trnet_Operand_index}

# trnet_Result class attributes and methods

# trnet_Same class attributes and methods

# trnet_Combinator class attributes and methods

# Operator class attributes and methods

# trnet_Restriction class attributes and methods

# Restriction class attributes and methods

# trnet_Expression class attributes and methods

# trnet_ExpressionOperator class attributes and methods

# trnet_StringLiteral class attributes and methods
trnet_StringLiteral_value: Property = Property(name="value", type=StringType)
trnet_StringLiteral.attributes={trnet_StringLiteral_value}

# Expression class attributes and methods

# trnet_SomeOperand class attributes and methods
trnet_SomeOperand_count: Property = Property(name="count", type=IntegerType)
trnet_SomeOperand.attributes={trnet_SomeOperand_count}

# Operand class attributes and methods

# trnet_AntiOperand class attributes and methods

# trnet_AnyOperand class attributes and methods

# trnet_SomeResult class attributes and methods
trnet_SomeResult_count: Property = Property(name="count", type=IntegerType)
trnet_SomeResult.attributes={trnet_SomeResult_count}

# Result class attributes and methods

# trnet_AnyResult class attributes and methods

# trnet_External class attributes and methods

# trnet_Union class attributes and methods

# trnet_MandatoryNode class attributes and methods

# NodePattern class attributes and methods

# trnet_OptionalNode class attributes and methods

# trnet_Equality class attributes and methods

# ExpressionOperator class attributes and methods

# trnet_OptionalOperand class attributes and methods

# trnet_Next class attributes and methods

# FlowRule class attributes and methods

# trnet_Eventually class attributes and methods

# trnet_NextDerived class attributes and methods

# Relationships
patterns0: BinaryAssociation = BinaryAssociation(
    name="patterns0",
    ends={
        Property(name="trnet_Pattern", type=trnet_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_TrNetModel", type=trnet_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operators1: BinaryAssociation = BinaryAssociation(
    name="operators1",
    ends={
        Property(name="trnet_Operator", type=trnet_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_TrNetModel2", type=trnet_Operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowRules3: BinaryAssociation = BinaryAssociation(
    name="flowRules3",
    ends={
        Property(name="trnet_FlowRule", type=trnet_TrNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_TrNetModel4", type=trnet_FlowRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="EdgePattern", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=trnet_EdgePattern, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="EdgePattern7", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=trnet_EdgePattern, multiplicity=Multiplicity(0, 9999))
    }
)
pattern13: BinaryAssociation = BinaryAssociation(
    name="pattern13",
    ends={
        Property(name="Pattern", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=trnet_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
attributes14: BinaryAssociation = BinaryAssociation(
    name="attributes14",
    ends={
        Property(name="trnet_AttributePattern", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_NodePattern", type=trnet_AttributePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
differentIn15: BinaryAssociation = BinaryAssociation(
    name="differentIn15",
    ends={
        Property(name="Different", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target16", type=trnet_Different, multiplicity=Multiplicity(0, 9999))
    }
)
differentOut17: BinaryAssociation = BinaryAssociation(
    name="differentOut17",
    ends={
        Property(name="Different19", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source18", type=trnet_Different, multiplicity=Multiplicity(0, 9999))
    }
)
keepIn20: BinaryAssociation = BinaryAssociation(
    name="keepIn20",
    ends={
        Property(name="Keep", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target21", type=trnet_Keep, multiplicity=Multiplicity(0, 9999))
    }
)
keepOut22: BinaryAssociation = BinaryAssociation(
    name="keepOut22",
    ends={
        Property(name="Keep24", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source23", type=trnet_Keep, multiplicity=Multiplicity(0, 9999))
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="NodePattern", type=trnet_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="NodePattern27", type=trnet_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
pattern28: BinaryAssociation = BinaryAssociation(
    name="pattern28",
    ends={
        Property(name="Pattern29", type=trnet_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=trnet_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
nodes30: BinaryAssociation = BinaryAssociation(
    name="nodes30",
    ends={
        Property(name="NodePattern31", type=trnet_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=trnet_NodePattern, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edges32: BinaryAssociation = BinaryAssociation(
    name="edges32",
    ends={
        Property(name="EdgePattern34", type=trnet_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern33", type=trnet_EdgePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingOperands35: BinaryAssociation = BinaryAssociation(
    name="outgoingOperands35",
    ends={
        Property(name="Operand", type=trnet_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern36", type=trnet_Operand, multiplicity=Multiplicity(0, 9999))
    }
)
incommingResults37: BinaryAssociation = BinaryAssociation(
    name="incommingResults37",
    ends={
        Property(name="Result", type=trnet_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern38", type=trnet_Result, multiplicity=Multiplicity(0, 9999))
    }
)
sameOut8: BinaryAssociation = BinaryAssociation(
    name="sameOut8",
    ends={
        Property(name="Same", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source9", type=trnet_Same, multiplicity=Multiplicity(0, 9999))
    }
)
sameIn10: BinaryAssociation = BinaryAssociation(
    name="sameIn10",
    ends={
        Property(name="Same12", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target11", type=trnet_Same, multiplicity=Multiplicity(0, 9999))
    }
)
results41: BinaryAssociation = BinaryAssociation(
    name="results41",
    ends={
        Property(name="Result43", type=trnet_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operator42", type=trnet_Result, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
restrictions44: BinaryAssociation = BinaryAssociation(
    name="restrictions44",
    ends={
        Property(name="trnet_Restriction", type=trnet_Combinator, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_Combinator", type=trnet_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source45: BinaryAssociation = BinaryAssociation(
    name="source45",
    ends={
        Property(name="NodePattern46", type=trnet_Same, multiplicity=Multiplicity(1, 1)),
        Property(name="sameOut", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target47: BinaryAssociation = BinaryAssociation(
    name="target47",
    ends={
        Property(name="NodePattern48", type=trnet_Same, multiplicity=Multiplicity(1, 1)),
        Property(name="sameIn", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
expression49: BinaryAssociation = BinaryAssociation(
    name="expression49",
    ends={
        Property(name="trnet_Expression", type=trnet_AttributePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_AttributePattern50", type=trnet_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator51: BinaryAssociation = BinaryAssociation(
    name="operator51",
    ends={
        Property(name="trnet_ExpressionOperator", type=trnet_AttributePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_AttributePattern52", type=trnet_ExpressionOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source53: BinaryAssociation = BinaryAssociation(
    name="source53",
    ends={
        Property(name="NodePattern54", type=trnet_Keep, multiplicity=Multiplicity(1, 1)),
        Property(name="keepOut", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target55: BinaryAssociation = BinaryAssociation(
    name="target55",
    ends={
        Property(name="NodePattern56", type=trnet_Keep, multiplicity=Multiplicity(1, 1)),
        Property(name="keepIn", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
pattern57: BinaryAssociation = BinaryAssociation(
    name="pattern57",
    ends={
        Property(name="Pattern58", type=trnet_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingOperands", type=trnet_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
operator59: BinaryAssociation = BinaryAssociation(
    name="operator59",
    ends={
        Property(name="Operator", type=trnet_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="operands", type=trnet_Operator, multiplicity=Multiplicity(1, 1))
    }
)
operands39: BinaryAssociation = BinaryAssociation(
    name="operands39",
    ends={
        Property(name="Operand40", type=trnet_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operator", type=trnet_Operand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source64: BinaryAssociation = BinaryAssociation(
    name="source64",
    ends={
        Property(name="NodePattern65", type=trnet_Different, multiplicity=Multiplicity(1, 1)),
        Property(name="differentOut", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
target66: BinaryAssociation = BinaryAssociation(
    name="target66",
    ends={
        Property(name="NodePattern67", type=trnet_Different, multiplicity=Multiplicity(1, 1)),
        Property(name="differentIn", type=trnet_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
restrictions68: BinaryAssociation = BinaryAssociation(
    name="restrictions68",
    ends={
        Property(name="trnet_Restriction69", type=trnet_Union, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_Union", type=trnet_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="trnet_TrNetModel72", type=trnet_FlowRule, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_FlowRule71", type=trnet_TrNetModel, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="trnet_TrNetModel75", type=trnet_FlowRule, multiplicity=Multiplicity(1, 1)),
        Property(name="trnet_FlowRule74", type=trnet_TrNetModel, multiplicity=Multiplicity(1, 1))
    }
)
pattern60: BinaryAssociation = BinaryAssociation(
    name="pattern60",
    ends={
        Property(name="Pattern61", type=trnet_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="incommingResults", type=trnet_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
operator62: BinaryAssociation = BinaryAssociation(
    name="operator62",
    ends={
        Property(name="Operator63", type=trnet_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="results", type=trnet_Operator, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_trnet_Combinator_Operator = Generalization(general=Operator, specific=trnet_Combinator)
gen_trnet_Same_Restriction = Generalization(general=Restriction, specific=trnet_Same)
gen_trnet_StringLiteral_Expression = Generalization(general=Expression, specific=trnet_StringLiteral)
gen_trnet_Keep_Restriction = Generalization(general=Restriction, specific=trnet_Keep)
gen_trnet_SomeOperand_Operand = Generalization(general=Operand, specific=trnet_SomeOperand)
gen_trnet_AntiOperand_Operand = Generalization(general=Operand, specific=trnet_AntiOperand)
gen_trnet_AnyOperand_Operand = Generalization(general=Operand, specific=trnet_AnyOperand)
gen_trnet_SomeResult_Result = Generalization(general=Result, specific=trnet_SomeResult)
gen_trnet_AnyResult_Result = Generalization(general=Result, specific=trnet_AnyResult)
gen_trnet_Different_Restriction = Generalization(general=Restriction, specific=trnet_Different)
gen_trnet_External_Operator = Generalization(general=Operator, specific=trnet_External)
gen_trnet_Union_Operator = Generalization(general=Operator, specific=trnet_Union)
gen_trnet_MandatoryNode_NodePattern = Generalization(general=NodePattern, specific=trnet_MandatoryNode)
gen_trnet_OptionalNode_NodePattern = Generalization(general=NodePattern, specific=trnet_OptionalNode)
gen_trnet_Equality_ExpressionOperator = Generalization(general=ExpressionOperator, specific=trnet_Equality)
gen_trnet_OptionalOperand_Operand = Generalization(general=Operand, specific=trnet_OptionalOperand)
gen_trnet_Next_FlowRule = Generalization(general=FlowRule, specific=trnet_Next)
gen_trnet_Eventually_FlowRule = Generalization(general=FlowRule, specific=trnet_Eventually)
gen_trnet_NextDerived_FlowRule = Generalization(general=FlowRule, specific=trnet_NextDerived)

# Domain Model
domain_model = DomainModel(
    name="trnet",
    types={trnet_TrNetModel, trnet_Pattern, trnet_Operator, trnet_FlowRule, trnet_NodePattern, trnet_EdgePattern, trnet_AttributePattern, trnet_Different, trnet_Keep, trnet_Operand, trnet_Result, trnet_Same, trnet_Combinator, Operator, trnet_Restriction, Restriction, trnet_Expression, trnet_ExpressionOperator, trnet_StringLiteral, Expression, trnet_SomeOperand, Operand, trnet_AntiOperand, trnet_AnyOperand, trnet_SomeResult, Result, trnet_AnyResult, trnet_External, trnet_Union, trnet_MandatoryNode, NodePattern, trnet_OptionalNode, trnet_Equality, ExpressionOperator, trnet_OptionalOperand, trnet_Next, FlowRule, trnet_Eventually, trnet_NextDerived},
    associations={patterns0, operators1, flowRules3, incoming5, outgoing6, pattern13, attributes14, differentIn15, differentOut17, keepIn20, keepOut22, source25, target26, pattern28, nodes30, edges32, outgoingOperands35, incommingResults37, sameOut8, sameIn10, results41, restrictions44, source45, target47, expression49, operator51, source53, target55, pattern57, operator59, operands39, source64, target66, restrictions68, source70, target73, pattern60, operator62},
    generalizations={gen_trnet_Combinator_Operator, gen_trnet_Same_Restriction, gen_trnet_StringLiteral_Expression, gen_trnet_Keep_Restriction, gen_trnet_SomeOperand_Operand, gen_trnet_AntiOperand_Operand, gen_trnet_AnyOperand_Operand, gen_trnet_SomeResult_Result, gen_trnet_AnyResult_Result, gen_trnet_Different_Restriction, gen_trnet_External_Operator, gen_trnet_Union_Operator, gen_trnet_MandatoryNode_NodePattern, gen_trnet_OptionalNode_NodePattern, gen_trnet_Equality_ExpressionOperator, gen_trnet_OptionalOperand_Operand, gen_trnet_Next_FlowRule, gen_trnet_Eventually_FlowRule, gen_trnet_NextDerived_FlowRule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)