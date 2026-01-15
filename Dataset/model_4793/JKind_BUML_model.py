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
jkind_TypeDef = Class(name="jkind::TypeDef")
jkind_Constant = Class(name="jkind::Constant")
jkind_Function = Class(name="jkind::Function")
jkind_Node = Class(name="jkind::Node")
jkind_EnumValue = Class(name="jkind::EnumValue")
IdRef = Class(name="IdRef")
jkind_Type = Class(name="jkind::Type")
jkind_Field = Class(name="jkind::Field")
jkind_Expr = Class(name="jkind::Expr")
Callable = Class(name="Callable")
jkind_VariableGroup = Class(name="jkind::VariableGroup")
jkind_Equation = Class(name="jkind::Equation")
jkind_File = Class(name="jkind::File")
jkind_CallExpr = Class(name="jkind::CallExpr")
Expr = Class(name="Expr")
jkind_Callable = Class(name="jkind::Callable")
jkind_IdRef = Class(name="jkind::IdRef")
jkind_Assertion = Class(name="jkind::Assertion")
jkind_Property = Class(name="jkind::Property")
jkind_Ivc = Class(name="jkind::Ivc")
jkind_RealizabilityInputs = Class(name="jkind::RealizabilityInputs")
jkind_Variable = Class(name="jkind::Variable")
jkind_IntType = Class(name="jkind::IntType")
jkind_BoolType = Class(name="jkind::BoolType")
jkind_RealType = Class(name="jkind::RealType")
jkind_SubrangeType = Class(name="jkind::SubrangeType")
jkind_UserType = Class(name="jkind::UserType")
jkind_BinaryExpr = Class(name="jkind::BinaryExpr")
jkind_UnaryExpr = Class(name="jkind::UnaryExpr")
jkind_RecordAccessExpr = Class(name="jkind::RecordAccessExpr")
jkind_RecordUpdateExpr = Class(name="jkind::RecordUpdateExpr")
jkind_AbbreviationType = Class(name="jkind::AbbreviationType")
TypeDef = Class(name="TypeDef")
jkind_RecordType = Class(name="jkind::RecordType")
jkind_EnumType = Class(name="jkind::EnumType")
jkind_ArrayType = Class(name="jkind::ArrayType")
Type = Class(name="Type")
jkind_IntExpr = Class(name="jkind::IntExpr")
jkind_RealExpr = Class(name="jkind::RealExpr")
jkind_BoolExpr = Class(name="jkind::BoolExpr")
jkind_IfThenElseExpr = Class(name="jkind::IfThenElseExpr")
jkind_CastExpr = Class(name="jkind::CastExpr")
jkind_CondactExpr = Class(name="jkind::CondactExpr")
jkind_ArrayAccessExpr = Class(name="jkind::ArrayAccessExpr")
jkind_ArrayUpdateExpr = Class(name="jkind::ArrayUpdateExpr")
jkind_IdExpr = Class(name="jkind::IdExpr")
jkind_ArrayExpr = Class(name="jkind::ArrayExpr")
jkind_RecordExpr = Class(name="jkind::RecordExpr")
jkind_TupleExpr = Class(name="jkind::TupleExpr")

# jkind_TypeDef class attributes and methods
jkind_TypeDef_name: Property = Property(name="name", type=StringType)
jkind_TypeDef.attributes={jkind_TypeDef_name}

# jkind_Constant class attributes and methods

# jkind_Function class attributes and methods

# jkind_Node class attributes and methods
jkind_Node_main: Property = Property(name="main", type=StringType)
jkind_Node.attributes={jkind_Node_main}

# jkind_EnumValue class attributes and methods

# IdRef class attributes and methods

# jkind_Type class attributes and methods

# jkind_Field class attributes and methods
jkind_Field_name: Property = Property(name="name", type=StringType)
jkind_Field.attributes={jkind_Field_name}

# jkind_Expr class attributes and methods

# Callable class attributes and methods

# jkind_VariableGroup class attributes and methods

# jkind_Equation class attributes and methods

# jkind_File class attributes and methods

# jkind_CallExpr class attributes and methods

# Expr class attributes and methods

# jkind_Callable class attributes and methods
jkind_Callable_name: Property = Property(name="name", type=StringType)
jkind_Callable.attributes={jkind_Callable_name}

# jkind_IdRef class attributes and methods
jkind_IdRef_name: Property = Property(name="name", type=StringType)
jkind_IdRef.attributes={jkind_IdRef_name}

# jkind_Assertion class attributes and methods

# jkind_Property class attributes and methods

# jkind_Ivc class attributes and methods

# jkind_RealizabilityInputs class attributes and methods

# jkind_Variable class attributes and methods

# jkind_IntType class attributes and methods

# jkind_BoolType class attributes and methods

# jkind_RealType class attributes and methods

# jkind_SubrangeType class attributes and methods
jkind_SubrangeType_low: Property = Property(name="low", type=StringType)
jkind_SubrangeType_high: Property = Property(name="high", type=StringType)
jkind_SubrangeType.attributes={jkind_SubrangeType_low, jkind_SubrangeType_high}

# jkind_UserType class attributes and methods

# jkind_BinaryExpr class attributes and methods
jkind_BinaryExpr_op: Property = Property(name="op", type=StringType)
jkind_BinaryExpr.attributes={jkind_BinaryExpr_op}

# jkind_UnaryExpr class attributes and methods
jkind_UnaryExpr_op: Property = Property(name="op", type=StringType)
jkind_UnaryExpr.attributes={jkind_UnaryExpr_op}

# jkind_RecordAccessExpr class attributes and methods

# jkind_RecordUpdateExpr class attributes and methods

# jkind_AbbreviationType class attributes and methods

# TypeDef class attributes and methods

# jkind_RecordType class attributes and methods

# jkind_EnumType class attributes and methods

# jkind_ArrayType class attributes and methods
jkind_ArrayType_size: Property = Property(name="size", type=StringType)
jkind_ArrayType.attributes={jkind_ArrayType_size}

# Type class attributes and methods

# jkind_IntExpr class attributes and methods
jkind_IntExpr_val: Property = Property(name="val", type=StringType)
jkind_IntExpr.attributes={jkind_IntExpr_val}

# jkind_RealExpr class attributes and methods
jkind_RealExpr_val: Property = Property(name="val", type=StringType)
jkind_RealExpr.attributes={jkind_RealExpr_val}

# jkind_BoolExpr class attributes and methods
jkind_BoolExpr_val: Property = Property(name="val", type=StringType)
jkind_BoolExpr.attributes={jkind_BoolExpr_val}

# jkind_IfThenElseExpr class attributes and methods

# jkind_CastExpr class attributes and methods
jkind_CastExpr_op: Property = Property(name="op", type=StringType)
jkind_CastExpr.attributes={jkind_CastExpr_op}

# jkind_CondactExpr class attributes and methods

# jkind_ArrayAccessExpr class attributes and methods

# jkind_ArrayUpdateExpr class attributes and methods

# jkind_IdExpr class attributes and methods

# jkind_ArrayExpr class attributes and methods

# jkind_RecordExpr class attributes and methods

# jkind_TupleExpr class attributes and methods

# Relationships
typedefs0: BinaryAssociation = BinaryAssociation(
    name="typedefs0",
    ends={
        Property(name="jkind_TypeDef", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File", type=jkind_TypeDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants1: BinaryAssociation = BinaryAssociation(
    name="constants1",
    ends={
        Property(name="jkind_Constant", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File2", type=jkind_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions3: BinaryAssociation = BinaryAssociation(
    name="functions3",
    ends={
        Property(name="jkind_Function", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File4", type=jkind_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes5: BinaryAssociation = BinaryAssociation(
    name="nodes5",
    ends={
        Property(name="jkind_Node", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File6", type=jkind_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="jkind_Type", type=jkind_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Constant8", type=jkind_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr9: BinaryAssociation = BinaryAssociation(
    name="expr9",
    ends={
        Property(name="jkind_Expr", type=jkind_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Constant10", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locals11: BinaryAssociation = BinaryAssociation(
    name="locals11",
    ends={
        Property(name="jkind_VariableGroup", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node12", type=jkind_VariableGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equations13: BinaryAssociation = BinaryAssociation(
    name="equations13",
    ends={
        Property(name="jkind_Equation", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node14", type=jkind_Equation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs28: BinaryAssociation = BinaryAssociation(
    name="lhs28",
    ends={
        Property(name="jkind_Variable30", type=jkind_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Equation29", type=jkind_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
rhs31: BinaryAssociation = BinaryAssociation(
    name="rhs31",
    ends={
        Property(name="jkind_Expr33", type=jkind_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Equation32", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref34: BinaryAssociation = BinaryAssociation(
    name="ref34",
    ends={
        Property(name="jkind_Variable36", type=jkind_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Property35", type=jkind_Variable, multiplicity=Multiplicity(0, 1))
    }
)
ids37: BinaryAssociation = BinaryAssociation(
    name="ids37",
    ends={
        Property(name="jkind_Variable39", type=jkind_Ivc, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Ivc38", type=jkind_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
ids40: BinaryAssociation = BinaryAssociation(
    name="ids40",
    ends={
        Property(name="jkind_Variable42", type=jkind_RealizabilityInputs, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RealizabilityInputs41", type=jkind_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
expr43: BinaryAssociation = BinaryAssociation(
    name="expr43",
    ends={
        Property(name="jkind_Expr45", type=jkind_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Assertion44", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callable46: BinaryAssociation = BinaryAssociation(
    name="callable46",
    ends={
        Property(name="jkind_Callable", type=jkind_CallExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_CallExpr", type=jkind_Callable, multiplicity=Multiplicity(0, 1))
    }
)
args47: BinaryAssociation = BinaryAssociation(
    name="args47",
    ends={
        Property(name="jkind_Expr49", type=jkind_CallExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_CallExpr48", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs50: BinaryAssociation = BinaryAssociation(
    name="inputs50",
    ends={
        Property(name="jkind_VariableGroup52", type=jkind_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Callable51", type=jkind_VariableGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs53: BinaryAssociation = BinaryAssociation(
    name="outputs53",
    ends={
        Property(name="jkind_VariableGroup55", type=jkind_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Callable54", type=jkind_VariableGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assertions15: BinaryAssociation = BinaryAssociation(
    name="assertions15",
    ends={
        Property(name="jkind_Assertion", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node16", type=jkind_Assertion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties17: BinaryAssociation = BinaryAssociation(
    name="properties17",
    ends={
        Property(name="jkind_Property", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node18", type=jkind_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ivc19: BinaryAssociation = BinaryAssociation(
    name="ivc19",
    ends={
        Property(name="jkind_Ivc", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node20", type=jkind_Ivc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizabilityInputs21: BinaryAssociation = BinaryAssociation(
    name="realizabilityInputs21",
    ends={
        Property(name="jkind_RealizabilityInputs", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node22", type=jkind_RealizabilityInputs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables23: BinaryAssociation = BinaryAssociation(
    name="variables23",
    ends={
        Property(name="jkind_Variable", type=jkind_VariableGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_VariableGroup24", type=jkind_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="jkind_Type27", type=jkind_VariableGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_VariableGroup26", type=jkind_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def65: BinaryAssociation = BinaryAssociation(
    name="def65",
    ends={
        Property(name="jkind_TypeDef66", type=jkind_UserType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_UserType", type=jkind_TypeDef, multiplicity=Multiplicity(0, 1))
    }
)
left67: BinaryAssociation = BinaryAssociation(
    name="left67",
    ends={
        Property(name="jkind_Expr68", type=jkind_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_BinaryExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="jkind_Expr71", type=jkind_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_BinaryExpr70", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr72: BinaryAssociation = BinaryAssociation(
    name="expr72",
    ends={
        Property(name="jkind_Expr73", type=jkind_UnaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_UnaryExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record74: BinaryAssociation = BinaryAssociation(
    name="record74",
    ends={
        Property(name="jkind_Expr75", type=jkind_RecordAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordAccessExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field76: BinaryAssociation = BinaryAssociation(
    name="field76",
    ends={
        Property(name="jkind_Field78", type=jkind_RecordAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordAccessExpr77", type=jkind_Field, multiplicity=Multiplicity(0, 1))
    }
)
record79: BinaryAssociation = BinaryAssociation(
    name="record79",
    ends={
        Property(name="jkind_Expr80", type=jkind_RecordUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordUpdateExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field81: BinaryAssociation = BinaryAssociation(
    name="field81",
    ends={
        Property(name="jkind_Field83", type=jkind_RecordUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordUpdateExpr82", type=jkind_Field, multiplicity=Multiplicity(0, 1))
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="jkind_Type57", type=jkind_AbbreviationType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_AbbreviationType", type=jkind_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields58: BinaryAssociation = BinaryAssociation(
    name="fields58",
    ends={
        Property(name="jkind_Field", type=jkind_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordType", type=jkind_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types59: BinaryAssociation = BinaryAssociation(
    name="types59",
    ends={
        Property(name="jkind_Type61", type=jkind_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordType60", type=jkind_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values62: BinaryAssociation = BinaryAssociation(
    name="values62",
    ends={
        Property(name="jkind_EnumValue", type=jkind_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_EnumType", type=jkind_EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base63: BinaryAssociation = BinaryAssociation(
    name="base63",
    ends={
        Property(name="jkind_Type64", type=jkind_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ArrayType", type=jkind_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond98: BinaryAssociation = BinaryAssociation(
    name="cond98",
    ends={
        Property(name="jkind_Expr99", type=jkind_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IfThenElseExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then100: BinaryAssociation = BinaryAssociation(
    name="then100",
    ends={
        Property(name="jkind_Expr102", type=jkind_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IfThenElseExpr101", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else103: BinaryAssociation = BinaryAssociation(
    name="else103",
    ends={
        Property(name="jkind_Expr105", type=jkind_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IfThenElseExpr104", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr106: BinaryAssociation = BinaryAssociation(
    name="expr106",
    ends={
        Property(name="jkind_Expr107", type=jkind_CastExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_CastExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clock108: BinaryAssociation = BinaryAssociation(
    name="clock108",
    ends={
        Property(name="jkind_Expr109", type=jkind_CondactExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_CondactExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call110: BinaryAssociation = BinaryAssociation(
    name="call110",
    ends={
        Property(name="jkind_CallExpr112", type=jkind_CondactExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_CondactExpr111", type=jkind_CallExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args113: BinaryAssociation = BinaryAssociation(
    name="args113",
    ends={
        Property(name="jkind_Expr115", type=jkind_CondactExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_CondactExpr114", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="jkind_Expr86", type=jkind_RecordUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordUpdateExpr85", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array87: BinaryAssociation = BinaryAssociation(
    name="array87",
    ends={
        Property(name="jkind_Expr88", type=jkind_ArrayAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ArrayAccessExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index89: BinaryAssociation = BinaryAssociation(
    name="index89",
    ends={
        Property(name="jkind_Expr91", type=jkind_ArrayAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ArrayAccessExpr90", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
access92: BinaryAssociation = BinaryAssociation(
    name="access92",
    ends={
        Property(name="jkind_ArrayAccessExpr93", type=jkind_ArrayUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ArrayUpdateExpr", type=jkind_ArrayAccessExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value94: BinaryAssociation = BinaryAssociation(
    name="value94",
    ends={
        Property(name="jkind_Expr96", type=jkind_ArrayUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ArrayUpdateExpr95", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id97: BinaryAssociation = BinaryAssociation(
    name="id97",
    ends={
        Property(name="jkind_IdRef", type=jkind_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IdExpr", type=jkind_IdRef, multiplicity=Multiplicity(0, 1))
    }
)
exprs116: BinaryAssociation = BinaryAssociation(
    name="exprs116",
    ends={
        Property(name="jkind_Expr117", type=jkind_ArrayExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ArrayExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type118: BinaryAssociation = BinaryAssociation(
    name="type118",
    ends={
        Property(name="jkind_RecordType119", type=jkind_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordExpr", type=jkind_RecordType, multiplicity=Multiplicity(0, 1))
    }
)
fields120: BinaryAssociation = BinaryAssociation(
    name="fields120",
    ends={
        Property(name="jkind_Field122", type=jkind_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordExpr121", type=jkind_Field, multiplicity=Multiplicity(0, 9999))
    }
)
exprs123: BinaryAssociation = BinaryAssociation(
    name="exprs123",
    ends={
        Property(name="jkind_Expr125", type=jkind_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordExpr124", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs126: BinaryAssociation = BinaryAssociation(
    name="exprs126",
    ends={
        Property(name="jkind_Expr127", type=jkind_TupleExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_TupleExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jkind_EnumValue_IdRef = Generalization(general=IdRef, specific=jkind_EnumValue)
gen_jkind_Constant_IdRef = Generalization(general=IdRef, specific=jkind_Constant)
gen_jkind_Function_Callable = Generalization(general=Callable, specific=jkind_Function)
gen_jkind_Node_Callable = Generalization(general=Callable, specific=jkind_Node)
gen_jkind_Variable_IdRef = Generalization(general=IdRef, specific=jkind_Variable)
gen_jkind_CallExpr_Expr = Generalization(general=Expr, specific=jkind_CallExpr)
gen_jkind_IntType_Type = Generalization(general=Type, specific=jkind_IntType)
gen_jkind_BoolType_Type = Generalization(general=Type, specific=jkind_BoolType)
gen_jkind_RealType_Type = Generalization(general=Type, specific=jkind_RealType)
gen_jkind_SubrangeType_Type = Generalization(general=Type, specific=jkind_SubrangeType)
gen_jkind_UserType_Type = Generalization(general=Type, specific=jkind_UserType)
gen_jkind_BinaryExpr_Expr = Generalization(general=Expr, specific=jkind_BinaryExpr)
gen_jkind_UnaryExpr_Expr = Generalization(general=Expr, specific=jkind_UnaryExpr)
gen_jkind_RecordAccessExpr_Expr = Generalization(general=Expr, specific=jkind_RecordAccessExpr)
gen_jkind_RecordUpdateExpr_Expr = Generalization(general=Expr, specific=jkind_RecordUpdateExpr)
gen_jkind_AbbreviationType_TypeDef = Generalization(general=TypeDef, specific=jkind_AbbreviationType)
gen_jkind_RecordType_TypeDef = Generalization(general=TypeDef, specific=jkind_RecordType)
gen_jkind_EnumType_TypeDef = Generalization(general=TypeDef, specific=jkind_EnumType)
gen_jkind_ArrayType_Type = Generalization(general=Type, specific=jkind_ArrayType)
gen_jkind_IntExpr_Expr = Generalization(general=Expr, specific=jkind_IntExpr)
gen_jkind_RealExpr_Expr = Generalization(general=Expr, specific=jkind_RealExpr)
gen_jkind_BoolExpr_Expr = Generalization(general=Expr, specific=jkind_BoolExpr)
gen_jkind_IfThenElseExpr_Expr = Generalization(general=Expr, specific=jkind_IfThenElseExpr)
gen_jkind_CastExpr_Expr = Generalization(general=Expr, specific=jkind_CastExpr)
gen_jkind_CondactExpr_Expr = Generalization(general=Expr, specific=jkind_CondactExpr)
gen_jkind_ArrayAccessExpr_Expr = Generalization(general=Expr, specific=jkind_ArrayAccessExpr)
gen_jkind_ArrayUpdateExpr_Expr = Generalization(general=Expr, specific=jkind_ArrayUpdateExpr)
gen_jkind_IdExpr_Expr = Generalization(general=Expr, specific=jkind_IdExpr)
gen_jkind_ArrayExpr_Expr = Generalization(general=Expr, specific=jkind_ArrayExpr)
gen_jkind_RecordExpr_Expr = Generalization(general=Expr, specific=jkind_RecordExpr)
gen_jkind_TupleExpr_Expr = Generalization(general=Expr, specific=jkind_TupleExpr)

# Domain Model
domain_model = DomainModel(
    name="jkind",
    types={jkind_TypeDef, jkind_Constant, jkind_Function, jkind_Node, jkind_EnumValue, IdRef, jkind_Type, jkind_Field, jkind_Expr, Callable, jkind_VariableGroup, jkind_Equation, jkind_File, jkind_CallExpr, Expr, jkind_Callable, jkind_IdRef, jkind_Assertion, jkind_Property, jkind_Ivc, jkind_RealizabilityInputs, jkind_Variable, jkind_IntType, jkind_BoolType, jkind_RealType, jkind_SubrangeType, jkind_UserType, jkind_BinaryExpr, jkind_UnaryExpr, jkind_RecordAccessExpr, jkind_RecordUpdateExpr, jkind_AbbreviationType, TypeDef, jkind_RecordType, jkind_EnumType, jkind_ArrayType, Type, jkind_IntExpr, jkind_RealExpr, jkind_BoolExpr, jkind_IfThenElseExpr, jkind_CastExpr, jkind_CondactExpr, jkind_ArrayAccessExpr, jkind_ArrayUpdateExpr, jkind_IdExpr, jkind_ArrayExpr, jkind_RecordExpr, jkind_TupleExpr},
    associations={typedefs0, constants1, functions3, nodes5, type7, expr9, locals11, equations13, lhs28, rhs31, ref34, ids37, ids40, expr43, callable46, args47, inputs50, outputs53, assertions15, properties17, ivc19, realizabilityInputs21, variables23, type25, def65, left67, right69, expr72, record74, field76, record79, field81, type56, fields58, types59, values62, base63, cond98, then100, else103, expr106, clock108, call110, args113, value84, array87, index89, access92, value94, id97, exprs116, type118, fields120, exprs123, exprs126},
    generalizations={gen_jkind_EnumValue_IdRef, gen_jkind_Constant_IdRef, gen_jkind_Function_Callable, gen_jkind_Node_Callable, gen_jkind_Variable_IdRef, gen_jkind_CallExpr_Expr, gen_jkind_IntType_Type, gen_jkind_BoolType_Type, gen_jkind_RealType_Type, gen_jkind_SubrangeType_Type, gen_jkind_UserType_Type, gen_jkind_BinaryExpr_Expr, gen_jkind_UnaryExpr_Expr, gen_jkind_RecordAccessExpr_Expr, gen_jkind_RecordUpdateExpr_Expr, gen_jkind_AbbreviationType_TypeDef, gen_jkind_RecordType_TypeDef, gen_jkind_EnumType_TypeDef, gen_jkind_ArrayType_Type, gen_jkind_IntExpr_Expr, gen_jkind_RealExpr_Expr, gen_jkind_BoolExpr_Expr, gen_jkind_IfThenElseExpr_Expr, gen_jkind_CastExpr_Expr, gen_jkind_CondactExpr_Expr, gen_jkind_ArrayAccessExpr_Expr, gen_jkind_ArrayUpdateExpr_Expr, gen_jkind_IdExpr_Expr, gen_jkind_ArrayExpr_Expr, gen_jkind_RecordExpr_Expr, gen_jkind_TupleExpr_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)