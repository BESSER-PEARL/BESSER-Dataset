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
TypeEnum: Enumeration = Enumeration(
    name="TypeEnum",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="location"),
			EnumerationLiteral(name="locationset"),
			EnumerationLiteral(name="entity"),
			EnumerationLiteral(name="entityset")
    }
)

LocationPrimiveEnum: Enumeration = Enumeration(
    name="LocationPrimiveEnum",
    literals={
            EnumerationLiteral(name="here"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="bottom")
    }
)

EntitySetPrimiveEnum: Enumeration = Enumeration(
    name="EntitySetPrimiveEnum",
    literals={
            EnumerationLiteral(name="all"),
			EnumerationLiteral(name="neighbours")
    }
)

EntityPrimitiveEnum: Enumeration = Enumeration(
    name="EntityPrimitiveEnum",
    literals={
            EnumerationLiteral(name="oneOf")
    }
)

LocationSetPrimiveEnum: Enumeration = Enumeration(
    name="LocationSetPrimiveEnum",
    literals={
            EnumerationLiteral(name="neighbourhood"),
			EnumerationLiteral(name="space")
    }
)

BooleanPrimitiveEnum: Enumeration = Enumeration(
    name="BooleanPrimitiveEnum",
    literals={
            EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false")
    }
)

UnaryEntityFunctionEnum: Enumeration = Enumeration(
    name="UnaryEntityFunctionEnum",
    literals={
            EnumerationLiteral(name="oneof")
    }
)

ArithmeticFunctionEnum: Enumeration = Enumeration(
    name="ArithmeticFunctionEnum",
    literals={
            EnumerationLiteral(name="Sum"),
			EnumerationLiteral(name="Minus"),
			EnumerationLiteral(name="Times"),
			EnumerationLiteral(name="Division")
    }
)

UnaryNumericFunctionEnum: Enumeration = Enumeration(
    name="UnaryNumericFunctionEnum",
    literals={
            EnumerationLiteral(name="random")
    }
)

ComparisonBooleanFunctionEnum: Enumeration = Enumeration(
    name="ComparisonBooleanFunctionEnum",
    literals={
            EnumerationLiteral(name="GreaterOrEequalThan"),
			EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="NotEqual"),
			EnumerationLiteral(name="LessThan"),
			EnumerationLiteral(name="LessOrEqualThan"),
			EnumerationLiteral(name="Equal")
    }
)

OccupationBooleanFunctionEnum: Enumeration = Enumeration(
    name="OccupationBooleanFunctionEnum",
    literals={
            EnumerationLiteral(name="Occupied")
    }
)

UnaryStringFunctionEnum: Enumeration = Enumeration(
    name="UnaryStringFunctionEnum",
    literals={
            EnumerationLiteral(name="Get")
    }
)

UnaryLocationFunctionEnum: Enumeration = Enumeration(
    name="UnaryLocationFunctionEnum",
    literals={
            EnumerationLiteral(name="RandomLocation"),
			EnumerationLiteral(name="RandomNeighbourhoodLocation"),
			EnumerationLiteral(name="TopLocation"),
			EnumerationLiteral(name="TopLeftLocation"),
			EnumerationLiteral(name="TopRightLocation"),
			EnumerationLiteral(name="BottomLocation"),
			EnumerationLiteral(name="BottomLeftLocation"),
			EnumerationLiteral(name="BottomRightLocation"),
			EnumerationLiteral(name="RightLocation"),
			EnumerationLiteral(name="LeftLocation"),
			EnumerationLiteral(name="OneOf")
    }
)

DurationTypeEnum: Enumeration = Enumeration(
    name="DurationTypeEnum",
    literals={
            EnumerationLiteral(name="weekly"),
			EnumerationLiteral(name="monthly")
    }
)

WeekDaysEnum: Enumeration = Enumeration(
    name="WeekDaysEnum",
    literals={
            EnumerationLiteral(name="monday"),
			EnumerationLiteral(name="tuesday"),
			EnumerationLiteral(name="wednesday"),
			EnumerationLiteral(name="thursday"),
			EnumerationLiteral(name="friday"),
			EnumerationLiteral(name="saturday"),
			EnumerationLiteral(name="sunday")
    }
)

MonthsEnum: Enumeration = Enumeration(
    name="MonthsEnum",
    literals={
            EnumerationLiteral(name="January"),
			EnumerationLiteral(name="Februrary"),
			EnumerationLiteral(name="March"),
			EnumerationLiteral(name="April"),
			EnumerationLiteral(name="May"),
			EnumerationLiteral(name="June"),
			EnumerationLiteral(name="July"),
			EnumerationLiteral(name="August"),
			EnumerationLiteral(name="September"),
			EnumerationLiteral(name="October"),
			EnumerationLiteral(name="November"),
			EnumerationLiteral(name="December")
    }
)

UnaryLocationEnum: Enumeration = Enumeration(
    name="UnaryLocationEnum",
    literals={
            EnumerationLiteral(name="oneof"),
			EnumerationLiteral(name="oneofneighbour"),
			EnumerationLiteral(name="toplocation")
    }
)

LogicBooleanFunctionEnum: Enumeration = Enumeration(
    name="LogicBooleanFunctionEnum",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NOT")
    }
)

# Classes
behaviour_AttributeClass = Class(name="behaviour::AttributeClass")
VariableClass = Class(name="VariableClass")
behaviour_ParameterClass = Class(name="behaviour::ParameterClass")
behaviour_FunctionCallExpression = Class(name="behaviour::FunctionCallExpression")
behaviour_Function = Class(name="behaviour::Function")
behaviour_ConstantExpression = Class(name="behaviour::ConstantExpression")
behaviour_IntConstantExpression = Class(name="behaviour::IntConstantExpression")
ConstantExpression = Class(name="ConstantExpression")
behaviour_StringConstantExpression = Class(name="behaviour::StringConstantExpression")
behaviour_FloatConstantExpression = Class(name="behaviour::FloatConstantExpression")
behaviour_PrimitiveExpression = Class(name="behaviour::PrimitiveExpression")
behaviour_EntityPrimive = Class(name="behaviour::EntityPrimive")
PrimitiveExpression = Class(name="PrimitiveExpression")
behaviour_Expression = Class(name="behaviour::Expression", is_abstract=True)
behaviour_VariableClass = Class(name="behaviour::VariableClass", is_abstract=True)
Expression = Class(name="Expression")
behaviour_Type = Class(name="behaviour::Type")
behaviour_BooleanPrimitive = Class(name="behaviour::BooleanPrimitive")
behaviour_EntityClass = Class(name="behaviour::EntityClass")
behaviour_Behavior = Class(name="behaviour::Behavior", is_abstract=True)
behaviour_LocationExpression = Class(name="behaviour::LocationExpression", is_abstract=True)
behaviour_Duration = Class(name="behaviour::Duration", is_abstract=True)
behaviour_EquationBehaviour = Class(name="behaviour::EquationBehaviour")
Behavior = Class(name="Behavior")
behaviour_Equation = Class(name="behaviour::Equation")
behaviour_ActivityDiagramBehavior = Class(name="behaviour::ActivityDiagramBehavior")
ExecutableNode = Class(name="ExecutableNode")
behaviour_Start = Class(name="behaviour::Start")
behaviour_End = Class(name="behaviour::End")
behaviour_LocationPrimitive = Class(name="behaviour::LocationPrimitive")
behaviour_LocationSetPrimitive = Class(name="behaviour::LocationSetPrimitive")
behaviour_EntitySetPrimitive = Class(name="behaviour::EntitySetPrimitive")
behaviour_AnonymousFunction = Class(name="behaviour::AnonymousFunction")
Function = Class(name="Function")
behaviour_NamedFunction = Class(name="behaviour::NamedFunction")
behaviour_UnconditionedEdge = Class(name="behaviour::UnconditionedEdge")
Edge = Class(name="Edge")
behaviour_UnaryStringFunction = Class(name="behaviour::UnaryStringFunction")
UnaryFunction = Class(name="UnaryFunction")
behaviour_UnaryLocationFunction = Class(name="behaviour::UnaryLocationFunction")
behaviour_BinaryBooleanFunction = Class(name="behaviour::BinaryBooleanFunction", is_abstract=True)
BinaryFunction = Class(name="BinaryFunction")
behaviour_BinaryArithmeticFunction = Class(name="behaviour::BinaryArithmeticFunction")
behaviour_UnaryNumericFunction = Class(name="behaviour::UnaryNumericFunction")
behaviour_ComparisonBooleanFunction = Class(name="behaviour::ComparisonBooleanFunction")
BinaryBooleanFunction = Class(name="BinaryBooleanFunction")
behaviour_OccupationBooleanFunction = Class(name="behaviour::OccupationBooleanFunction")
behaviour_LogicBooleanFunction = Class(name="behaviour::LogicBooleanFunction")
behaviour_ControlNode = Class(name="behaviour::ControlNode", is_abstract=True)
Node = Class(name="Node")
behaviour_ExecutableNode = Class(name="behaviour::ExecutableNode", is_abstract=True)
behaviour_TimeExpression = Class(name="behaviour::TimeExpression", is_abstract=True)
ControlNode = Class(name="ControlNode")
behaviour_Decision = Class(name="behaviour::Decision")
behaviour_Edge = Class(name="behaviour::Edge", is_abstract=True)
behaviour_Node = Class(name="behaviour::Node", is_abstract=True)
behaviour_Die = Class(name="behaviour::Die")
behaviour_Reproduce = Class(name="behaviour::Reproduce")
behaviour_Add = Class(name="behaviour::Add")
behaviour_Remove = Class(name="behaviour::Remove")
behaviour_While = Class(name="behaviour::While")
TimeExpression = Class(name="TimeExpression")
behaviour_TrueEdge = Class(name="behaviour::TrueEdge")
behaviour_FalseEdge = Class(name="behaviour::FalseEdge")
behaviour_UnaryEntityFunction = Class(name="behaviour::UnaryEntityFunction")
behaviour_Join = Class(name="behaviour::Join")
behaviour_Fork = Class(name="behaviour::Fork")
behaviour_Merge = Class(name="behaviour::Merge")
behaviour_PrimitiveActivity = Class(name="behaviour::PrimitiveActivity", is_abstract=True)
behaviour_Move = Class(name="behaviour::Move")
PrimitiveActivity = Class(name="PrimitiveActivity")
behaviour_CoordinateLocationExpression = Class(name="behaviour::CoordinateLocationExpression")
behaviour_MonthDuration = Class(name="behaviour::MonthDuration")
Duration = Class(name="Duration")
behaviour_BinaryFunction = Class(name="behaviour::BinaryFunction")
NamedFunction = Class(name="NamedFunction")
behaviour_UnaryFunction = Class(name="behaviour::UnaryFunction")
behaviour_BinaryLocationFunction = Class(name="behaviour::BinaryLocationFunction")
behaviour_NumericPrimitive = Class(name="behaviour::NumericPrimitive")
behaviour_NameLocationExpression = Class(name="behaviour::NameLocationExpression")
LocationExpression = Class(name="LocationExpression")

# behaviour_AttributeClass class attributes and methods

# VariableClass class attributes and methods

# behaviour_ParameterClass class attributes and methods

# behaviour_FunctionCallExpression class attributes and methods

# behaviour_Function class attributes and methods

# behaviour_ConstantExpression class attributes and methods

# behaviour_IntConstantExpression class attributes and methods
behaviour_IntConstantExpression_value: Property = Property(name="value", type=IntegerType)
behaviour_IntConstantExpression.attributes={behaviour_IntConstantExpression_value}

# ConstantExpression class attributes and methods

# behaviour_StringConstantExpression class attributes and methods
behaviour_StringConstantExpression_value: Property = Property(name="value", type=StringType)
behaviour_StringConstantExpression.attributes={behaviour_StringConstantExpression_value}

# behaviour_FloatConstantExpression class attributes and methods
behaviour_FloatConstantExpression_value: Property = Property(name="value", type=FloatType)
behaviour_FloatConstantExpression.attributes={behaviour_FloatConstantExpression_value}

# behaviour_PrimitiveExpression class attributes and methods

# behaviour_EntityPrimive class attributes and methods
behaviour_EntityPrimive_primitive: Property = Property(name="primitive", type=StringType)
behaviour_EntityPrimive.attributes={behaviour_EntityPrimive_primitive}

# PrimitiveExpression class attributes and methods

# behaviour_Expression class attributes and methods

# behaviour_VariableClass class attributes and methods
behaviour_VariableClass_variableName: Property = Property(name="variableName", type=StringType)
behaviour_VariableClass.attributes={behaviour_VariableClass_variableName}

# Expression class attributes and methods

# behaviour_Type class attributes and methods
behaviour_Type_type: Property = Property(name="type", type=StringType)
behaviour_Type.attributes={behaviour_Type_type}

# behaviour_BooleanPrimitive class attributes and methods
behaviour_BooleanPrimitive_primitive: Property = Property(name="primitive", type=StringType)
behaviour_BooleanPrimitive.attributes={behaviour_BooleanPrimitive_primitive}

# behaviour_EntityClass class attributes and methods
behaviour_EntityClass_entityName: Property = Property(name="entityName", type=StringType)
behaviour_EntityClass.attributes={behaviour_EntityClass_entityName}

# behaviour_Behavior class attributes and methods
behaviour_Behavior_behaviorName: Property = Property(name="behaviorName", type=StringType)
behaviour_Behavior_frequency: Property = Property(name="frequency", type=StringType)
behaviour_Behavior.attributes={behaviour_Behavior_frequency, behaviour_Behavior_behaviorName}

# behaviour_LocationExpression class attributes and methods

# behaviour_Duration class attributes and methods
behaviour_Duration_durationTime: Property = Property(name="durationTime", type=IntegerType)
behaviour_Duration.attributes={behaviour_Duration_durationTime}

# behaviour_EquationBehaviour class attributes and methods

# Behavior class attributes and methods

# behaviour_Equation class attributes and methods

# behaviour_ActivityDiagramBehavior class attributes and methods

# ExecutableNode class attributes and methods

# behaviour_Start class attributes and methods

# behaviour_End class attributes and methods

# behaviour_LocationPrimitive class attributes and methods
behaviour_LocationPrimitive_primitive: Property = Property(name="primitive", type=StringType)
behaviour_LocationPrimitive.attributes={behaviour_LocationPrimitive_primitive}

# behaviour_LocationSetPrimitive class attributes and methods
behaviour_LocationSetPrimitive_primitive: Property = Property(name="primitive", type=StringType)
behaviour_LocationSetPrimitive.attributes={behaviour_LocationSetPrimitive_primitive}

# behaviour_EntitySetPrimitive class attributes and methods
behaviour_EntitySetPrimitive_primitive: Property = Property(name="primitive", type=StringType)
behaviour_EntitySetPrimitive.attributes={behaviour_EntitySetPrimitive_primitive}

# behaviour_AnonymousFunction class attributes and methods

# Function class attributes and methods

# behaviour_NamedFunction class attributes and methods

# behaviour_UnconditionedEdge class attributes and methods

# Edge class attributes and methods

# behaviour_UnaryStringFunction class attributes and methods
behaviour_UnaryStringFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_UnaryStringFunction.attributes={behaviour_UnaryStringFunction_functionName}

# UnaryFunction class attributes and methods

# behaviour_UnaryLocationFunction class attributes and methods
behaviour_UnaryLocationFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_UnaryLocationFunction.attributes={behaviour_UnaryLocationFunction_functionName}

# behaviour_BinaryBooleanFunction class attributes and methods

# BinaryFunction class attributes and methods

# behaviour_BinaryArithmeticFunction class attributes and methods
behaviour_BinaryArithmeticFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_BinaryArithmeticFunction.attributes={behaviour_BinaryArithmeticFunction_functionName}

# behaviour_UnaryNumericFunction class attributes and methods
behaviour_UnaryNumericFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_UnaryNumericFunction.attributes={behaviour_UnaryNumericFunction_functionName}

# behaviour_ComparisonBooleanFunction class attributes and methods
behaviour_ComparisonBooleanFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_ComparisonBooleanFunction.attributes={behaviour_ComparisonBooleanFunction_functionName}

# BinaryBooleanFunction class attributes and methods

# behaviour_OccupationBooleanFunction class attributes and methods
behaviour_OccupationBooleanFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_OccupationBooleanFunction.attributes={behaviour_OccupationBooleanFunction_functionName}

# behaviour_LogicBooleanFunction class attributes and methods
behaviour_LogicBooleanFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_LogicBooleanFunction.attributes={behaviour_LogicBooleanFunction_functionName}

# behaviour_ControlNode class attributes and methods

# Node class attributes and methods

# behaviour_ExecutableNode class attributes and methods

# behaviour_TimeExpression class attributes and methods

# ControlNode class attributes and methods

# behaviour_Decision class attributes and methods

# behaviour_Edge class attributes and methods

# behaviour_Node class attributes and methods

# behaviour_Die class attributes and methods

# behaviour_Reproduce class attributes and methods

# behaviour_Add class attributes and methods

# behaviour_Remove class attributes and methods

# behaviour_While class attributes and methods

# TimeExpression class attributes and methods

# behaviour_TrueEdge class attributes and methods

# behaviour_FalseEdge class attributes and methods

# behaviour_UnaryEntityFunction class attributes and methods
behaviour_UnaryEntityFunction_functionName: Property = Property(name="functionName", type=StringType)
behaviour_UnaryEntityFunction.attributes={behaviour_UnaryEntityFunction_functionName}

# behaviour_Join class attributes and methods

# behaviour_Fork class attributes and methods

# behaviour_Merge class attributes and methods

# behaviour_PrimitiveActivity class attributes and methods

# behaviour_Move class attributes and methods

# PrimitiveActivity class attributes and methods

# behaviour_CoordinateLocationExpression class attributes and methods
behaviour_CoordinateLocationExpression_x: Property = Property(name="x", type=FloatType)
behaviour_CoordinateLocationExpression_y: Property = Property(name="y", type=FloatType)
behaviour_CoordinateLocationExpression.attributes={behaviour_CoordinateLocationExpression_x, behaviour_CoordinateLocationExpression_y}

# behaviour_MonthDuration class attributes and methods
behaviour_MonthDuration_month: Property = Property(name="month", type=StringType)
behaviour_MonthDuration.attributes={behaviour_MonthDuration_month}

# Duration class attributes and methods

# behaviour_BinaryFunction class attributes and methods

# NamedFunction class attributes and methods

# behaviour_UnaryFunction class attributes and methods

# behaviour_BinaryLocationFunction class attributes and methods

# behaviour_NumericPrimitive class attributes and methods

# behaviour_NameLocationExpression class attributes and methods
behaviour_NameLocationExpression_name: Property = Property(name="name", type=StringType)
behaviour_NameLocationExpression.attributes={behaviour_NameLocationExpression_name}

# LocationExpression class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="behaviour_VariableClass", type=behaviour_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Type", type=behaviour_VariableClass, multiplicity=Multiplicity(1, 1))
    }
)
arguments1: BinaryAssociation = BinaryAssociation(
    name="arguments1",
    ends={
        Property(name="behaviour_VariableClass2", type=behaviour_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_FunctionCallExpression", type=behaviour_VariableClass, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
function3: BinaryAssociation = BinaryAssociation(
    name="function3",
    ends={
        Property(name="behaviour_Function", type=behaviour_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_FunctionCallExpression4", type=behaviour_Function, multiplicity=Multiplicity(1, 1))
    }
)
domaine5: BinaryAssociation = BinaryAssociation(
    name="domaine5",
    ends={
        Property(name="behaviour_Type7", type=behaviour_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Function6", type=behaviour_Type, multiplicity=Multiplicity(1, 1))
    }
)
codomaine8: BinaryAssociation = BinaryAssociation(
    name="codomaine8",
    ends={
        Property(name="behaviour_Type10", type=behaviour_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Function9", type=behaviour_Type, multiplicity=Multiplicity(1, 1))
    }
)
behaviour11: BinaryAssociation = BinaryAssociation(
    name="behaviour11",
    ends={
        Property(name="behaviour_Behavior", type=behaviour_EntityClass, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_EntityClass", type=behaviour_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute12: BinaryAssociation = BinaryAssociation(
    name="attribute12",
    ends={
        Property(name="behaviour_AttributeClass", type=behaviour_EntityClass, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_EntityClass13", type=behaviour_AttributeClass, multiplicity=Multiplicity(0, 9999))
    }
)
startTime14: BinaryAssociation = BinaryAssociation(
    name="startTime14",
    ends={
        Property(name="behaviour_Duration", type=behaviour_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Behavior15", type=behaviour_Duration, multiplicity=Multiplicity(1, 1))
    }
)
endTime16: BinaryAssociation = BinaryAssociation(
    name="endTime16",
    ends={
        Property(name="behaviour_Duration18", type=behaviour_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Behavior17", type=behaviour_Duration, multiplicity=Multiplicity(1, 1))
    }
)
parameters19: BinaryAssociation = BinaryAssociation(
    name="parameters19",
    ends={
        Property(name="behaviour_ParameterClass", type=behaviour_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Behavior20", type=behaviour_ParameterClass, multiplicity=Multiplicity(1, 9999))
    }
)
equation21: BinaryAssociation = BinaryAssociation(
    name="equation21",
    ends={
        Property(name="behaviour_Equation", type=behaviour_EquationBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_EquationBehaviour", type=behaviour_Equation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start22: BinaryAssociation = BinaryAssociation(
    name="start22",
    ends={
        Property(name="behaviour_Start", type=behaviour_ActivityDiagramBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_ActivityDiagramBehavior", type=behaviour_Start, multiplicity=Multiplicity(1, 1))
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="behaviour_Expression", type=behaviour_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Equation33", type=behaviour_Expression, multiplicity=Multiplicity(1, 9999))
    }
)
source34: BinaryAssociation = BinaryAssociation(
    name="source34",
    ends={
        Property(name="behaviour_Node36", type=behaviour_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Edge35", type=behaviour_Node, multiplicity=Multiplicity(1, 1))
    }
)
target37: BinaryAssociation = BinaryAssociation(
    name="target37",
    ends={
        Property(name="behaviour_Node39", type=behaviour_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Edge38", type=behaviour_Node, multiplicity=Multiplicity(1, 1))
    }
)
expression40: BinaryAssociation = BinaryAssociation(
    name="expression40",
    ends={
        Property(name="behaviour_Expression41", type=behaviour_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TimeExpression", type=behaviour_Expression, multiplicity=Multiplicity(1, 1))
    }
)
expression42: BinaryAssociation = BinaryAssociation(
    name="expression42",
    ends={
        Property(name="behaviour_Expression43", type=behaviour_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Decision", type=behaviour_Expression, multiplicity=Multiplicity(1, 1))
    }
)
end23: BinaryAssociation = BinaryAssociation(
    name="end23",
    ends={
        Property(name="behaviour_End", type=behaviour_ActivityDiagramBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_ActivityDiagramBehavior24", type=behaviour_End, multiplicity=Multiplicity(1, 9999))
    }
)
edge25: BinaryAssociation = BinaryAssociation(
    name="edge25",
    ends={
        Property(name="behaviour_Edge", type=behaviour_ActivityDiagramBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_ActivityDiagramBehavior26", type=behaviour_Edge, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
node27: BinaryAssociation = BinaryAssociation(
    name="node27",
    ends={
        Property(name="behaviour_Node", type=behaviour_ActivityDiagramBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_ActivityDiagramBehavior28", type=behaviour_Node, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
left29: BinaryAssociation = BinaryAssociation(
    name="left29",
    ends={
        Property(name="behaviour_AttributeClass31", type=behaviour_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Equation30", type=behaviour_AttributeClass, multiplicity=Multiplicity(0, 1))
    }
)
expression44: BinaryAssociation = BinaryAssociation(
    name="expression44",
    ends={
        Property(name="behaviour_Expression45", type=behaviour_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Move", type=behaviour_Expression, multiplicity=Multiplicity(1, 9999))
    }
)
to46: BinaryAssociation = BinaryAssociation(
    name="to46",
    ends={
        Property(name="behaviour_AttributeClass47", type=behaviour_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Add", type=behaviour_AttributeClass, multiplicity=Multiplicity(1, 1))
    }
)
from48: BinaryAssociation = BinaryAssociation(
    name="from48",
    ends={
        Property(name="behaviour_AttributeClass49", type=behaviour_Remove, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Remove", type=behaviour_AttributeClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_behaviour_AttributeClass_VariableClass = Generalization(general=VariableClass, specific=behaviour_AttributeClass)
gen_behaviour_ParameterClass_VariableClass = Generalization(general=VariableClass, specific=behaviour_ParameterClass)
gen_behaviour_FunctionCallExpression_Expression = Generalization(general=Expression, specific=behaviour_FunctionCallExpression)
gen_behaviour_ConstantExpression_Expression = Generalization(general=Expression, specific=behaviour_ConstantExpression)
gen_behaviour_IntConstantExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=behaviour_IntConstantExpression)
gen_behaviour_StringConstantExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=behaviour_StringConstantExpression)
gen_behaviour_FloatConstantExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=behaviour_FloatConstantExpression)
gen_behaviour_PrimitiveExpression_Expression = Generalization(general=Expression, specific=behaviour_PrimitiveExpression)
gen_behaviour_EntityPrimive_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=behaviour_EntityPrimive)
gen_behaviour_VariableClass_Expression = Generalization(general=Expression, specific=behaviour_VariableClass)
gen_behaviour_BooleanPrimitive_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=behaviour_BooleanPrimitive)
gen_behaviour_LocationExpression_Expression = Generalization(general=Expression, specific=behaviour_LocationExpression)
gen_behaviour_EquationBehaviour_Behavior = Generalization(general=Behavior, specific=behaviour_EquationBehaviour)
gen_behaviour_ActivityDiagramBehavior_Behavior = Generalization(general=Behavior, specific=behaviour_ActivityDiagramBehavior)
gen_behaviour_ActivityDiagramBehavior_ExecutableNode = Generalization(general=ExecutableNode, specific=behaviour_ActivityDiagramBehavior)
gen_behaviour_LocationPrimitive_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=behaviour_LocationPrimitive)
gen_behaviour_LocationSetPrimitive_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=behaviour_LocationSetPrimitive)
gen_behaviour_EntitySetPrimitive_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=behaviour_EntitySetPrimitive)
gen_behaviour_AnonymousFunction_Function = Generalization(general=Function, specific=behaviour_AnonymousFunction)
gen_behaviour_NamedFunction_Function = Generalization(general=Function, specific=behaviour_NamedFunction)
gen_behaviour_UnconditionedEdge_Edge = Generalization(general=Edge, specific=behaviour_UnconditionedEdge)
gen_behaviour_UnaryStringFunction_UnaryFunction = Generalization(general=UnaryFunction, specific=behaviour_UnaryStringFunction)
gen_behaviour_UnaryLocationFunction_UnaryFunction = Generalization(general=UnaryFunction, specific=behaviour_UnaryLocationFunction)
gen_behaviour_BinaryBooleanFunction_BinaryFunction = Generalization(general=BinaryFunction, specific=behaviour_BinaryBooleanFunction)
gen_behaviour_BinaryArithmeticFunction_BinaryFunction = Generalization(general=BinaryFunction, specific=behaviour_BinaryArithmeticFunction)
gen_behaviour_UnaryNumericFunction_UnaryFunction = Generalization(general=UnaryFunction, specific=behaviour_UnaryNumericFunction)
gen_behaviour_ComparisonBooleanFunction_BinaryBooleanFunction = Generalization(general=BinaryBooleanFunction, specific=behaviour_ComparisonBooleanFunction)
gen_behaviour_OccupationBooleanFunction_BinaryBooleanFunction = Generalization(general=BinaryBooleanFunction, specific=behaviour_OccupationBooleanFunction)
gen_behaviour_LogicBooleanFunction_BinaryBooleanFunction = Generalization(general=BinaryBooleanFunction, specific=behaviour_LogicBooleanFunction)
gen_behaviour_ControlNode_Node = Generalization(general=Node, specific=behaviour_ControlNode)
gen_behaviour_ExecutableNode_Node = Generalization(general=Node, specific=behaviour_ExecutableNode)
gen_behaviour_TimeExpression_ControlNode = Generalization(general=ControlNode, specific=behaviour_TimeExpression)
gen_behaviour_Decision_ControlNode = Generalization(general=ControlNode, specific=behaviour_Decision)
gen_behaviour_Move_PrimitiveActivity = Generalization(general=PrimitiveActivity, specific=behaviour_Move)
gen_behaviour_Die_PrimitiveActivity = Generalization(general=PrimitiveActivity, specific=behaviour_Die)
gen_behaviour_Reproduce_PrimitiveActivity = Generalization(general=PrimitiveActivity, specific=behaviour_Reproduce)
gen_behaviour_Add_PrimitiveActivity = Generalization(general=PrimitiveActivity, specific=behaviour_Add)
gen_behaviour_Remove_PrimitiveActivity = Generalization(general=PrimitiveActivity, specific=behaviour_Remove)
gen_behaviour_While_TimeExpression = Generalization(general=TimeExpression, specific=behaviour_While)
gen_behaviour_TrueEdge_Edge = Generalization(general=Edge, specific=behaviour_TrueEdge)
gen_behaviour_FalseEdge_Edge = Generalization(general=Edge, specific=behaviour_FalseEdge)
gen_behaviour_UnaryEntityFunction_UnaryFunction = Generalization(general=UnaryFunction, specific=behaviour_UnaryEntityFunction)
gen_behaviour_Join_ControlNode = Generalization(general=ControlNode, specific=behaviour_Join)
gen_behaviour_Start_ControlNode = Generalization(general=ControlNode, specific=behaviour_Start)
gen_behaviour_End_ControlNode = Generalization(general=ControlNode, specific=behaviour_End)
gen_behaviour_Fork_ControlNode = Generalization(general=ControlNode, specific=behaviour_Fork)
gen_behaviour_Merge_ControlNode = Generalization(general=ControlNode, specific=behaviour_Merge)
gen_behaviour_PrimitiveActivity_ExecutableNode = Generalization(general=ExecutableNode, specific=behaviour_PrimitiveActivity)
gen_behaviour_CoordinateLocationExpression_LocationExpression = Generalization(general=LocationExpression, specific=behaviour_CoordinateLocationExpression)
gen_behaviour_MonthDuration_Duration = Generalization(general=Duration, specific=behaviour_MonthDuration)
gen_behaviour_BinaryFunction_NamedFunction = Generalization(general=NamedFunction, specific=behaviour_BinaryFunction)
gen_behaviour_UnaryFunction_NamedFunction = Generalization(general=NamedFunction, specific=behaviour_UnaryFunction)
gen_behaviour_BinaryLocationFunction_BinaryFunction = Generalization(general=BinaryFunction, specific=behaviour_BinaryLocationFunction)
gen_behaviour_NameLocationExpression_LocationExpression = Generalization(general=LocationExpression, specific=behaviour_NameLocationExpression)

# Domain Model
domain_model = DomainModel(
    name="behaviour",
    types={behaviour_AttributeClass, VariableClass, behaviour_ParameterClass, behaviour_FunctionCallExpression, behaviour_Function, behaviour_ConstantExpression, behaviour_IntConstantExpression, ConstantExpression, behaviour_StringConstantExpression, behaviour_FloatConstantExpression, behaviour_PrimitiveExpression, behaviour_EntityPrimive, PrimitiveExpression, behaviour_Expression, behaviour_VariableClass, Expression, behaviour_Type, behaviour_BooleanPrimitive, behaviour_EntityClass, behaviour_Behavior, behaviour_LocationExpression, behaviour_Duration, behaviour_EquationBehaviour, Behavior, behaviour_Equation, behaviour_ActivityDiagramBehavior, ExecutableNode, behaviour_Start, behaviour_End, behaviour_LocationPrimitive, behaviour_LocationSetPrimitive, behaviour_EntitySetPrimitive, behaviour_AnonymousFunction, Function, behaviour_NamedFunction, behaviour_UnconditionedEdge, Edge, behaviour_UnaryStringFunction, UnaryFunction, behaviour_UnaryLocationFunction, behaviour_BinaryBooleanFunction, BinaryFunction, behaviour_BinaryArithmeticFunction, behaviour_UnaryNumericFunction, behaviour_ComparisonBooleanFunction, BinaryBooleanFunction, behaviour_OccupationBooleanFunction, behaviour_LogicBooleanFunction, behaviour_ControlNode, Node, behaviour_ExecutableNode, behaviour_TimeExpression, ControlNode, behaviour_Decision, behaviour_Edge, behaviour_Node, behaviour_Die, behaviour_Reproduce, behaviour_Add, behaviour_Remove, behaviour_While, TimeExpression, behaviour_TrueEdge, behaviour_FalseEdge, behaviour_UnaryEntityFunction, behaviour_Join, behaviour_Fork, behaviour_Merge, behaviour_PrimitiveActivity, behaviour_Move, PrimitiveActivity, behaviour_CoordinateLocationExpression, behaviour_MonthDuration, Duration, behaviour_BinaryFunction, NamedFunction, behaviour_UnaryFunction, behaviour_BinaryLocationFunction, behaviour_NumericPrimitive, behaviour_NameLocationExpression, LocationExpression, TypeEnum, LocationPrimiveEnum, EntitySetPrimiveEnum, EntityPrimitiveEnum, LocationSetPrimiveEnum, BooleanPrimitiveEnum, UnaryEntityFunctionEnum, ArithmeticFunctionEnum, UnaryNumericFunctionEnum, ComparisonBooleanFunctionEnum, OccupationBooleanFunctionEnum, UnaryStringFunctionEnum, UnaryLocationFunctionEnum, DurationTypeEnum, WeekDaysEnum, MonthsEnum, UnaryLocationEnum, LogicBooleanFunctionEnum},
    associations={type0, arguments1, function3, domaine5, codomaine8, behaviour11, attribute12, startTime14, endTime16, parameters19, equation21, start22, right32, source34, target37, expression40, expression42, end23, edge25, node27, left29, expression44, to46, from48},
    generalizations={gen_behaviour_AttributeClass_VariableClass, gen_behaviour_ParameterClass_VariableClass, gen_behaviour_FunctionCallExpression_Expression, gen_behaviour_ConstantExpression_Expression, gen_behaviour_IntConstantExpression_ConstantExpression, gen_behaviour_StringConstantExpression_ConstantExpression, gen_behaviour_FloatConstantExpression_ConstantExpression, gen_behaviour_PrimitiveExpression_Expression, gen_behaviour_EntityPrimive_PrimitiveExpression, gen_behaviour_VariableClass_Expression, gen_behaviour_BooleanPrimitive_PrimitiveExpression, gen_behaviour_LocationExpression_Expression, gen_behaviour_EquationBehaviour_Behavior, gen_behaviour_ActivityDiagramBehavior_Behavior, gen_behaviour_ActivityDiagramBehavior_ExecutableNode, gen_behaviour_LocationPrimitive_PrimitiveExpression, gen_behaviour_LocationSetPrimitive_PrimitiveExpression, gen_behaviour_EntitySetPrimitive_PrimitiveExpression, gen_behaviour_AnonymousFunction_Function, gen_behaviour_NamedFunction_Function, gen_behaviour_UnconditionedEdge_Edge, gen_behaviour_UnaryStringFunction_UnaryFunction, gen_behaviour_UnaryLocationFunction_UnaryFunction, gen_behaviour_BinaryBooleanFunction_BinaryFunction, gen_behaviour_BinaryArithmeticFunction_BinaryFunction, gen_behaviour_UnaryNumericFunction_UnaryFunction, gen_behaviour_ComparisonBooleanFunction_BinaryBooleanFunction, gen_behaviour_OccupationBooleanFunction_BinaryBooleanFunction, gen_behaviour_LogicBooleanFunction_BinaryBooleanFunction, gen_behaviour_ControlNode_Node, gen_behaviour_ExecutableNode_Node, gen_behaviour_TimeExpression_ControlNode, gen_behaviour_Decision_ControlNode, gen_behaviour_Move_PrimitiveActivity, gen_behaviour_Die_PrimitiveActivity, gen_behaviour_Reproduce_PrimitiveActivity, gen_behaviour_Add_PrimitiveActivity, gen_behaviour_Remove_PrimitiveActivity, gen_behaviour_While_TimeExpression, gen_behaviour_TrueEdge_Edge, gen_behaviour_FalseEdge_Edge, gen_behaviour_UnaryEntityFunction_UnaryFunction, gen_behaviour_Join_ControlNode, gen_behaviour_Start_ControlNode, gen_behaviour_End_ControlNode, gen_behaviour_Fork_ControlNode, gen_behaviour_Merge_ControlNode, gen_behaviour_PrimitiveActivity_ExecutableNode, gen_behaviour_CoordinateLocationExpression_LocationExpression, gen_behaviour_MonthDuration_Duration, gen_behaviour_BinaryFunction_NamedFunction, gen_behaviour_UnaryFunction_NamedFunction, gen_behaviour_BinaryLocationFunction_BinaryFunction, gen_behaviour_NameLocationExpression_LocationExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)