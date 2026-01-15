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
EIntOneOp: Enumeration = Enumeration(
    name="EIntOneOp",
    literals={
            EnumerationLiteral(name="MIN")
    }
)

EIntTwoOp: Enumeration = Enumeration(
    name="EIntTwoOp",
    literals={
            EnumerationLiteral(name="SUB"),
			EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="DIV")
    }
)

EBoolVal: Enumeration = Enumeration(
    name="EBoolVal",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

EBoolTwoOp: Enumeration = Enumeration(
    name="EBoolTwoOp",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR")
    }
)

ECompOp: Enumeration = Enumeration(
    name="ECompOp",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="LT")
    }
)

EBoolOneOp: Enumeration = Enumeration(
    name="EBoolOneOp",
    literals={
            EnumerationLiteral(name="NOT")
    }
)

# Classes
flinkie2_Variable = Class(name="flinkie2::Variable")
flinkie2_BooleanEvaluation = Class(name="flinkie2::BooleanEvaluation")
Node = Class(name="Node")
flinkie2_AssignStat = Class(name="flinkie2::AssignStat")
flinkie2_Node = Class(name="flinkie2::Node", is_abstract=True)
flinkie2_Init = Class(name="flinkie2::Init")
flinkie2_DeclStat = Class(name="flinkie2::DeclStat")
flinkie2_TwoOpInt = Class(name="flinkie2::TwoOpInt")
flinkie2_BoolExpr = Class(name="flinkie2::BoolExpr", is_abstract=True)
flinkie2_Question = Class(name="flinkie2::Question")
flinkie2_Option = Class(name="flinkie2::Option")
flinkie2_Message = Class(name="flinkie2::Message")
flinkie2_IntExpr = Class(name="flinkie2::IntExpr", is_abstract=True)
flinkie2_OneOpInt = Class(name="flinkie2::OneOpInt")
IntExpr = Class(name="IntExpr")
flinkie2_VariableExpr = Class(name="flinkie2::VariableExpr")
flinkie2_Number = Class(name="flinkie2::Number")
flinkie2_FlowChart = Class(name="flinkie2::FlowChart")
flinkie2_BracExprInt = Class(name="flinkie2::BracExprInt")
flinkie2_OneOpBool = Class(name="flinkie2::OneOpBool")
BoolExpr = Class(name="BoolExpr")
flinkie2_TwoOpBool = Class(name="flinkie2::TwoOpBool")
flinkie2_BoolVal = Class(name="flinkie2::BoolVal")
flinkie2_BracExprBool = Class(name="flinkie2::BracExprBool")
flinkie2_Comparison = Class(name="flinkie2::Comparison")

# flinkie2_Variable class attributes and methods
flinkie2_Variable_name: Property = Property(name="name", type=StringType)
flinkie2_Variable.attributes={flinkie2_Variable_name}

# flinkie2_BooleanEvaluation class attributes and methods

# Node class attributes and methods

# flinkie2_AssignStat class attributes and methods

# flinkie2_Node class attributes and methods

# flinkie2_Init class attributes and methods

# flinkie2_DeclStat class attributes and methods

# flinkie2_TwoOpInt class attributes and methods
flinkie2_TwoOpInt_operator: Property = Property(name="operator", type=StringType)
flinkie2_TwoOpInt.attributes={flinkie2_TwoOpInt_operator}

# flinkie2_BoolExpr class attributes and methods

# flinkie2_Question class attributes and methods
flinkie2_Question_text: Property = Property(name="text", type=StringType)
flinkie2_Question.attributes={flinkie2_Question_text}

# flinkie2_Option class attributes and methods
flinkie2_Option_text: Property = Property(name="text", type=StringType)
flinkie2_Option.attributes={flinkie2_Option_text}

# flinkie2_Message class attributes and methods
flinkie2_Message_text: Property = Property(name="text", type=StringType)
flinkie2_Message.attributes={flinkie2_Message_text}

# flinkie2_IntExpr class attributes and methods

# flinkie2_OneOpInt class attributes and methods
flinkie2_OneOpInt_operator: Property = Property(name="operator", type=StringType)
flinkie2_OneOpInt.attributes={flinkie2_OneOpInt_operator}

# IntExpr class attributes and methods

# flinkie2_VariableExpr class attributes and methods

# flinkie2_Number class attributes and methods
flinkie2_Number_value: Property = Property(name="value", type=IntegerType)
flinkie2_Number.attributes={flinkie2_Number_value}

# flinkie2_FlowChart class attributes and methods

# flinkie2_BracExprInt class attributes and methods

# flinkie2_OneOpBool class attributes and methods
flinkie2_OneOpBool_operator: Property = Property(name="operator", type=StringType)
flinkie2_OneOpBool.attributes={flinkie2_OneOpBool_operator}

# BoolExpr class attributes and methods

# flinkie2_TwoOpBool class attributes and methods
flinkie2_TwoOpBool_operator: Property = Property(name="operator", type=StringType)
flinkie2_TwoOpBool.attributes={flinkie2_TwoOpBool_operator}

# flinkie2_BoolVal class attributes and methods
flinkie2_BoolVal_value: Property = Property(name="value", type=BooleanType)
flinkie2_BoolVal.attributes={flinkie2_BoolVal_value}

# flinkie2_BracExprBool class attributes and methods

# flinkie2_Comparison class attributes and methods
flinkie2_Comparison_operator: Property = Property(name="operator", type=StringType)
flinkie2_Comparison.attributes={flinkie2_Comparison_operator}

# Relationships
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="flinkie2_Variable", type=flinkie2_DeclStat, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_DeclStat4", type=flinkie2_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignstats5: BinaryAssociation = BinaryAssociation(
    name="assignstats5",
    ends={
        Property(name="flinkie2_AssignStat", type=flinkie2_BooleanEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_BooleanEvaluation", type=flinkie2_AssignStat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declstats0: BinaryAssociation = BinaryAssociation(
    name="declstats0",
    ends={
        Property(name="flinkie2_DeclStat", type=flinkie2_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Init", type=flinkie2_DeclStat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node1: BinaryAssociation = BinaryAssociation(
    name="node1",
    ends={
        Property(name="flinkie2_Node", type=flinkie2_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Init2", type=flinkie2_Node, multiplicity=Multiplicity(1, 1))
    }
)
intexpr29: BinaryAssociation = BinaryAssociation(
    name="intexpr29",
    ends={
        Property(name="flinkie2_IntExpr", type=flinkie2_OneOpInt, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_OneOpInt", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
true6: BinaryAssociation = BinaryAssociation(
    name="true6",
    ends={
        Property(name="flinkie2_Node8", type=flinkie2_BooleanEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_BooleanEvaluation7", type=flinkie2_Node, multiplicity=Multiplicity(0, 1))
    }
)
false9: BinaryAssociation = BinaryAssociation(
    name="false9",
    ends={
        Property(name="flinkie2_Node11", type=flinkie2_BooleanEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_BooleanEvaluation10", type=flinkie2_Node, multiplicity=Multiplicity(0, 1))
    }
)
boolexpr12: BinaryAssociation = BinaryAssociation(
    name="boolexpr12",
    ends={
        Property(name="flinkie2_BoolExpr", type=flinkie2_BooleanEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_BooleanEvaluation13", type=flinkie2_BoolExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
options14: BinaryAssociation = BinaryAssociation(
    name="options14",
    ends={
        Property(name="flinkie2_Option", type=flinkie2_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Question", type=flinkie2_Option, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
assignstats15: BinaryAssociation = BinaryAssociation(
    name="assignstats15",
    ends={
        Property(name="flinkie2_AssignStat17", type=flinkie2_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Question16", type=flinkie2_AssignStat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignstats18: BinaryAssociation = BinaryAssociation(
    name="assignstats18",
    ends={
        Property(name="flinkie2_AssignStat19", type=flinkie2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Message", type=flinkie2_AssignStat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node20: BinaryAssociation = BinaryAssociation(
    name="node20",
    ends={
        Property(name="flinkie2_Node22", type=flinkie2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Message21", type=flinkie2_Node, multiplicity=Multiplicity(0, 1))
    }
)
assignstats23: BinaryAssociation = BinaryAssociation(
    name="assignstats23",
    ends={
        Property(name="flinkie2_AssignStat25", type=flinkie2_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Option24", type=flinkie2_AssignStat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node26: BinaryAssociation = BinaryAssociation(
    name="node26",
    ends={
        Property(name="flinkie2_Node28", type=flinkie2_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Option27", type=flinkie2_Node, multiplicity=Multiplicity(0, 1))
    }
)
variableexpr35: BinaryAssociation = BinaryAssociation(
    name="variableexpr35",
    ends={
        Property(name="flinkie2_VariableExpr", type=flinkie2_AssignStat, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_AssignStat36", type=flinkie2_VariableExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intexpr37: BinaryAssociation = BinaryAssociation(
    name="intexpr37",
    ends={
        Property(name="flinkie2_IntExpr39", type=flinkie2_AssignStat, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_AssignStat38", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left30: BinaryAssociation = BinaryAssociation(
    name="left30",
    ends={
        Property(name="flinkie2_IntExpr31", type=flinkie2_TwoOpInt, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_TwoOpInt", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="flinkie2_IntExpr34", type=flinkie2_TwoOpInt, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_TwoOpInt33", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="flinkie2_Comparison", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="flinkie2_IntExpr60", type=flinkie2_Comparison, multiplicity=Multiplicity(1, 1))
    }
)
left61: BinaryAssociation = BinaryAssociation(
    name="left61",
    ends={
        Property(name="flinkie2_IntExpr63", type=flinkie2_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_Comparison62", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodes40: BinaryAssociation = BinaryAssociation(
    name="nodes40",
    ends={
        Property(name="flinkie2_Node41", type=flinkie2_FlowChart, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_FlowChart", type=flinkie2_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialisation42: BinaryAssociation = BinaryAssociation(
    name="initialisation42",
    ends={
        Property(name="flinkie2_Init44", type=flinkie2_FlowChart, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_FlowChart43", type=flinkie2_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intexpr45: BinaryAssociation = BinaryAssociation(
    name="intexpr45",
    ends={
        Property(name="flinkie2_IntExpr46", type=flinkie2_BracExprInt, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_BracExprInt", type=flinkie2_IntExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable47: BinaryAssociation = BinaryAssociation(
    name="variable47",
    ends={
        Property(name="flinkie2_Variable49", type=flinkie2_VariableExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_VariableExpr48", type=flinkie2_Variable, multiplicity=Multiplicity(1, 1))
    }
)
boolexpr50: BinaryAssociation = BinaryAssociation(
    name="boolexpr50",
    ends={
        Property(name="flinkie2_BoolExpr51", type=flinkie2_OneOpBool, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_OneOpBool", type=flinkie2_BoolExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left52: BinaryAssociation = BinaryAssociation(
    name="left52",
    ends={
        Property(name="flinkie2_BoolExpr53", type=flinkie2_TwoOpBool, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_TwoOpBool", type=flinkie2_BoolExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right54: BinaryAssociation = BinaryAssociation(
    name="right54",
    ends={
        Property(name="flinkie2_BoolExpr56", type=flinkie2_TwoOpBool, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_TwoOpBool55", type=flinkie2_BoolExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolexpr57: BinaryAssociation = BinaryAssociation(
    name="boolexpr57",
    ends={
        Property(name="flinkie2_BoolExpr58", type=flinkie2_BracExprBool, multiplicity=Multiplicity(1, 1)),
        Property(name="flinkie2_BracExprBool", type=flinkie2_BoolExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_flinkie2_BooleanEvaluation_Node = Generalization(general=Node, specific=flinkie2_BooleanEvaluation)
gen_flinkie2_TwoOpInt_IntExpr = Generalization(general=IntExpr, specific=flinkie2_TwoOpInt)
gen_flinkie2_Question_Node = Generalization(general=Node, specific=flinkie2_Question)
gen_flinkie2_Message_Node = Generalization(general=Node, specific=flinkie2_Message)
gen_flinkie2_OneOpInt_IntExpr = Generalization(general=IntExpr, specific=flinkie2_OneOpInt)
gen_flinkie2_Number_IntExpr = Generalization(general=IntExpr, specific=flinkie2_Number)
gen_flinkie2_BracExprInt_IntExpr = Generalization(general=IntExpr, specific=flinkie2_BracExprInt)
gen_flinkie2_VariableExpr_IntExpr = Generalization(general=IntExpr, specific=flinkie2_VariableExpr)
gen_flinkie2_OneOpBool_BoolExpr = Generalization(general=BoolExpr, specific=flinkie2_OneOpBool)
gen_flinkie2_TwoOpBool_BoolExpr = Generalization(general=BoolExpr, specific=flinkie2_TwoOpBool)
gen_flinkie2_BoolVal_BoolExpr = Generalization(general=BoolExpr, specific=flinkie2_BoolVal)
gen_flinkie2_BracExprBool_BoolExpr = Generalization(general=BoolExpr, specific=flinkie2_BracExprBool)
gen_flinkie2_Comparison_BoolExpr = Generalization(general=BoolExpr, specific=flinkie2_Comparison)

# Domain Model
domain_model = DomainModel(
    name="flinkie2",
    types={flinkie2_Variable, flinkie2_BooleanEvaluation, Node, flinkie2_AssignStat, flinkie2_Node, flinkie2_Init, flinkie2_DeclStat, flinkie2_TwoOpInt, flinkie2_BoolExpr, flinkie2_Question, flinkie2_Option, flinkie2_Message, flinkie2_IntExpr, flinkie2_OneOpInt, IntExpr, flinkie2_VariableExpr, flinkie2_Number, flinkie2_FlowChart, flinkie2_BracExprInt, flinkie2_OneOpBool, BoolExpr, flinkie2_TwoOpBool, flinkie2_BoolVal, flinkie2_BracExprBool, flinkie2_Comparison, EIntOneOp, EIntTwoOp, EBoolVal, EBoolTwoOp, ECompOp, EBoolOneOp},
    associations={variable3, assignstats5, declstats0, node1, intexpr29, true6, false9, boolexpr12, options14, assignstats15, assignstats18, node20, assignstats23, node26, variableexpr35, intexpr37, left30, right32, right59, left61, nodes40, initialisation42, intexpr45, variable47, boolexpr50, left52, right54, boolexpr57},
    generalizations={gen_flinkie2_BooleanEvaluation_Node, gen_flinkie2_TwoOpInt_IntExpr, gen_flinkie2_Question_Node, gen_flinkie2_Message_Node, gen_flinkie2_OneOpInt_IntExpr, gen_flinkie2_Number_IntExpr, gen_flinkie2_BracExprInt_IntExpr, gen_flinkie2_VariableExpr_IntExpr, gen_flinkie2_OneOpBool_BoolExpr, gen_flinkie2_TwoOpBool_BoolExpr, gen_flinkie2_BoolVal_BoolExpr, gen_flinkie2_BracExprBool_BoolExpr, gen_flinkie2_Comparison_BoolExpr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)