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
jkind_Variable = Class(name="jkind::Variable")
jkind_File = Class(name="jkind::File")
jkind_Typedef = Class(name="jkind::Typedef")
jkind_Constant = Class(name="jkind::Constant")
jkind_Node = Class(name="jkind::Node")
jkind_Type = Class(name="jkind::Type")
jkind_Field = Class(name="jkind::Field")
IdRef = Class(name="IdRef")
jkind_Expr = Class(name="jkind::Expr")
jkind_VariableGroup = Class(name="jkind::VariableGroup")
jkind_Equation = Class(name="jkind::Equation")
jkind_Assertion = Class(name="jkind::Assertion")
jkind_Property = Class(name="jkind::Property")
jkind_UnaryExpr = Class(name="jkind::UnaryExpr")
jkind_ProjectionExpr = Class(name="jkind::ProjectionExpr")
jkind_IdRef = Class(name="jkind::IdRef")
jkind_AbbreviationType = Class(name="jkind::AbbreviationType")
Typedef = Class(name="Typedef")
jkind_RecordType = Class(name="jkind::RecordType")
jkind_IntType = Class(name="jkind::IntType")
Type = Class(name="Type")
jkind_BoolType = Class(name="jkind::BoolType")
jkind_RealType = Class(name="jkind::RealType")
jkind_SubrangeType = Class(name="jkind::SubrangeType")
jkind_UserType = Class(name="jkind::UserType")
jkind_BinaryExpr = Class(name="jkind::BinaryExpr")
Expr = Class(name="Expr")
jkind_IdExpr = Class(name="jkind::IdExpr")
jkind_IntExpr = Class(name="jkind::IntExpr")
jkind_RealExpr = Class(name="jkind::RealExpr")
jkind_BoolExpr = Class(name="jkind::BoolExpr")
jkind_IfThenElseExpr = Class(name="jkind::IfThenElseExpr")
jkind_NodeCallExpr = Class(name="jkind::NodeCallExpr")
jkind_RecordExpr = Class(name="jkind::RecordExpr")

# jkind_Variable class attributes and methods

# jkind_File class attributes and methods

# jkind_Typedef class attributes and methods
jkind_Typedef_name: Property = Property(name="name", type=StringType)
jkind_Typedef.attributes={jkind_Typedef_name}

# jkind_Constant class attributes and methods

# jkind_Node class attributes and methods
jkind_Node_main: Property = Property(name="main", type=StringType)
jkind_Node_name: Property = Property(name="name", type=StringType)
jkind_Node.attributes={jkind_Node_main, jkind_Node_name}

# jkind_Type class attributes and methods

# jkind_Field class attributes and methods
jkind_Field_name: Property = Property(name="name", type=StringType)
jkind_Field.attributes={jkind_Field_name}

# IdRef class attributes and methods

# jkind_Expr class attributes and methods

# jkind_VariableGroup class attributes and methods

# jkind_Equation class attributes and methods

# jkind_Assertion class attributes and methods

# jkind_Property class attributes and methods

# jkind_UnaryExpr class attributes and methods
jkind_UnaryExpr_op: Property = Property(name="op", type=StringType)
jkind_UnaryExpr.attributes={jkind_UnaryExpr_op}

# jkind_ProjectionExpr class attributes and methods

# jkind_IdRef class attributes and methods
jkind_IdRef_name: Property = Property(name="name", type=StringType)
jkind_IdRef.attributes={jkind_IdRef_name}

# jkind_AbbreviationType class attributes and methods

# Typedef class attributes and methods

# jkind_RecordType class attributes and methods

# jkind_IntType class attributes and methods

# Type class attributes and methods

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

# Expr class attributes and methods

# jkind_IdExpr class attributes and methods

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

# jkind_NodeCallExpr class attributes and methods

# jkind_RecordExpr class attributes and methods

# Relationships
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
typedefs0: BinaryAssociation = BinaryAssociation(
    name="typedefs0",
    ends={
        Property(name="jkind_Typedef", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File", type=jkind_Typedef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants1: BinaryAssociation = BinaryAssociation(
    name="constants1",
    ends={
        Property(name="jkind_Constant", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File2", type=jkind_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes3: BinaryAssociation = BinaryAssociation(
    name="nodes3",
    ends={
        Property(name="jkind_Node", type=jkind_File, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_File4", type=jkind_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="jkind_Type", type=jkind_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Constant6", type=jkind_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr7: BinaryAssociation = BinaryAssociation(
    name="expr7",
    ends={
        Property(name="jkind_Expr", type=jkind_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Constant8", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs9: BinaryAssociation = BinaryAssociation(
    name="inputs9",
    ends={
        Property(name="jkind_VariableGroup", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node10", type=jkind_VariableGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs11: BinaryAssociation = BinaryAssociation(
    name="outputs11",
    ends={
        Property(name="jkind_VariableGroup13", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node12", type=jkind_VariableGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals14: BinaryAssociation = BinaryAssociation(
    name="locals14",
    ends={
        Property(name="jkind_VariableGroup16", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node15", type=jkind_VariableGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equations17: BinaryAssociation = BinaryAssociation(
    name="equations17",
    ends={
        Property(name="jkind_Equation", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node18", type=jkind_Equation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assertions19: BinaryAssociation = BinaryAssociation(
    name="assertions19",
    ends={
        Property(name="jkind_Assertion", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node20", type=jkind_Assertion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties21: BinaryAssociation = BinaryAssociation(
    name="properties21",
    ends={
        Property(name="jkind_Property", type=jkind_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Node22", type=jkind_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr53: BinaryAssociation = BinaryAssociation(
    name="expr53",
    ends={
        Property(name="jkind_Expr54", type=jkind_UnaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_UnaryExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr55: BinaryAssociation = BinaryAssociation(
    name="expr55",
    ends={
        Property(name="jkind_Expr56", type=jkind_ProjectionExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ProjectionExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
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
expr37: BinaryAssociation = BinaryAssociation(
    name="expr37",
    ends={
        Property(name="jkind_Expr39", type=jkind_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_Assertion38", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type40: BinaryAssociation = BinaryAssociation(
    name="type40",
    ends={
        Property(name="jkind_Type41", type=jkind_AbbreviationType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_AbbreviationType", type=jkind_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields42: BinaryAssociation = BinaryAssociation(
    name="fields42",
    ends={
        Property(name="jkind_Field", type=jkind_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordType", type=jkind_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types43: BinaryAssociation = BinaryAssociation(
    name="types43",
    ends={
        Property(name="jkind_Type45", type=jkind_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordType44", type=jkind_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
def46: BinaryAssociation = BinaryAssociation(
    name="def46",
    ends={
        Property(name="jkind_Typedef47", type=jkind_UserType, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_UserType", type=jkind_Typedef, multiplicity=Multiplicity(0, 1))
    }
)
left48: BinaryAssociation = BinaryAssociation(
    name="left48",
    ends={
        Property(name="jkind_Expr49", type=jkind_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_BinaryExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right50: BinaryAssociation = BinaryAssociation(
    name="right50",
    ends={
        Property(name="jkind_Expr52", type=jkind_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_BinaryExpr51", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field57: BinaryAssociation = BinaryAssociation(
    name="field57",
    ends={
        Property(name="jkind_Field59", type=jkind_ProjectionExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_ProjectionExpr58", type=jkind_Field, multiplicity=Multiplicity(0, 1))
    }
)
id60: BinaryAssociation = BinaryAssociation(
    name="id60",
    ends={
        Property(name="jkind_IdRef", type=jkind_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IdExpr", type=jkind_IdRef, multiplicity=Multiplicity(0, 1))
    }
)
cond61: BinaryAssociation = BinaryAssociation(
    name="cond61",
    ends={
        Property(name="jkind_Expr62", type=jkind_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IfThenElseExpr", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then63: BinaryAssociation = BinaryAssociation(
    name="then63",
    ends={
        Property(name="jkind_Expr65", type=jkind_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IfThenElseExpr64", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else66: BinaryAssociation = BinaryAssociation(
    name="else66",
    ends={
        Property(name="jkind_Expr68", type=jkind_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_IfThenElseExpr67", type=jkind_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node69: BinaryAssociation = BinaryAssociation(
    name="node69",
    ends={
        Property(name="jkind_Node70", type=jkind_NodeCallExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_NodeCallExpr", type=jkind_Node, multiplicity=Multiplicity(0, 1))
    }
)
args71: BinaryAssociation = BinaryAssociation(
    name="args71",
    ends={
        Property(name="jkind_Expr73", type=jkind_NodeCallExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_NodeCallExpr72", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type74: BinaryAssociation = BinaryAssociation(
    name="type74",
    ends={
        Property(name="jkind_RecordType75", type=jkind_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordExpr", type=jkind_RecordType, multiplicity=Multiplicity(0, 1))
    }
)
fields76: BinaryAssociation = BinaryAssociation(
    name="fields76",
    ends={
        Property(name="jkind_Field78", type=jkind_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordExpr77", type=jkind_Field, multiplicity=Multiplicity(0, 9999))
    }
)
exprs79: BinaryAssociation = BinaryAssociation(
    name="exprs79",
    ends={
        Property(name="jkind_Expr81", type=jkind_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="jkind_RecordExpr80", type=jkind_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jkind_Constant_IdRef = Generalization(general=IdRef, specific=jkind_Constant)
gen_jkind_UnaryExpr_Expr = Generalization(general=Expr, specific=jkind_UnaryExpr)
gen_jkind_ProjectionExpr_Expr = Generalization(general=Expr, specific=jkind_ProjectionExpr)
gen_jkind_Variable_IdRef = Generalization(general=IdRef, specific=jkind_Variable)
gen_jkind_AbbreviationType_Typedef = Generalization(general=Typedef, specific=jkind_AbbreviationType)
gen_jkind_RecordType_Typedef = Generalization(general=Typedef, specific=jkind_RecordType)
gen_jkind_IntType_Type = Generalization(general=Type, specific=jkind_IntType)
gen_jkind_BoolType_Type = Generalization(general=Type, specific=jkind_BoolType)
gen_jkind_RealType_Type = Generalization(general=Type, specific=jkind_RealType)
gen_jkind_SubrangeType_Type = Generalization(general=Type, specific=jkind_SubrangeType)
gen_jkind_UserType_Type = Generalization(general=Type, specific=jkind_UserType)
gen_jkind_BinaryExpr_Expr = Generalization(general=Expr, specific=jkind_BinaryExpr)
gen_jkind_IdExpr_Expr = Generalization(general=Expr, specific=jkind_IdExpr)
gen_jkind_IntExpr_Expr = Generalization(general=Expr, specific=jkind_IntExpr)
gen_jkind_RealExpr_Expr = Generalization(general=Expr, specific=jkind_RealExpr)
gen_jkind_BoolExpr_Expr = Generalization(general=Expr, specific=jkind_BoolExpr)
gen_jkind_IfThenElseExpr_Expr = Generalization(general=Expr, specific=jkind_IfThenElseExpr)
gen_jkind_NodeCallExpr_Expr = Generalization(general=Expr, specific=jkind_NodeCallExpr)
gen_jkind_RecordExpr_Expr = Generalization(general=Expr, specific=jkind_RecordExpr)

# Domain Model
domain_model = DomainModel(
    name="jkind",
    types={jkind_Variable, jkind_File, jkind_Typedef, jkind_Constant, jkind_Node, jkind_Type, jkind_Field, IdRef, jkind_Expr, jkind_VariableGroup, jkind_Equation, jkind_Assertion, jkind_Property, jkind_UnaryExpr, jkind_ProjectionExpr, jkind_IdRef, jkind_AbbreviationType, Typedef, jkind_RecordType, jkind_IntType, Type, jkind_BoolType, jkind_RealType, jkind_SubrangeType, jkind_UserType, jkind_BinaryExpr, Expr, jkind_IdExpr, jkind_IntExpr, jkind_RealExpr, jkind_BoolExpr, jkind_IfThenElseExpr, jkind_NodeCallExpr, jkind_RecordExpr},
    associations={variables23, type25, typedefs0, constants1, nodes3, type5, expr7, inputs9, outputs11, locals14, equations17, assertions19, properties21, expr53, expr55, lhs28, rhs31, ref34, expr37, type40, fields42, types43, def46, left48, right50, field57, id60, cond61, then63, else66, node69, args71, type74, fields76, exprs79},
    generalizations={gen_jkind_Constant_IdRef, gen_jkind_UnaryExpr_Expr, gen_jkind_ProjectionExpr_Expr, gen_jkind_Variable_IdRef, gen_jkind_AbbreviationType_Typedef, gen_jkind_RecordType_Typedef, gen_jkind_IntType_Type, gen_jkind_BoolType_Type, gen_jkind_RealType_Type, gen_jkind_SubrangeType_Type, gen_jkind_UserType_Type, gen_jkind_BinaryExpr_Expr, gen_jkind_IdExpr_Expr, gen_jkind_IntExpr_Expr, gen_jkind_RealExpr_Expr, gen_jkind_BoolExpr_Expr, gen_jkind_IfThenElseExpr_Expr, gen_jkind_NodeCallExpr_Expr, gen_jkind_RecordExpr_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)