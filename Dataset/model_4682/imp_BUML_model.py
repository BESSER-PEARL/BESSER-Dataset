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
UnaryOp: Enumeration = Enumeration(
    name="UnaryOp",
    literals={
            EnumerationLiteral(name="NEGATE"),
			EnumerationLiteral(name="NOT")
    }
)

BinaryOp: Enumeration = Enumeration(
    name="BinaryOp",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUB"),
			EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LEQ"),
			EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="GEQ"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
imp_Stmt = Class(name="imp::Stmt", is_abstract=True)
imp_Skip = Class(name="imp::Skip")
Stmt = Class(name="Stmt")
imp_Assign = Class(name="imp::Assign")
imp_Expr = Class(name="imp::Expr", is_abstract=True)
imp_Block = Class(name="imp::Block")
imp_If = Class(name="imp::If")
imp_Binary = Class(name="imp::Binary")
imp_Store = Class(name="imp::Store")
imp_StringToValueMap = Class(name="imp::StringToValueMap")
imp_While = Class(name="imp::While")
imp_IntConst = Class(name="imp::IntConst")
Expr = Class(name="Expr")
imp_Var = Class(name="imp::Var")
imp_Unary = Class(name="imp::Unary")
imp_BoolConst = Class(name="imp::BoolConst")
imp_Value = Class(name="imp::Value", is_abstract=True)
imp_IntValue = Class(name="imp::IntValue")
Value = Class(name="Value")
imp_BoolValue = Class(name="imp::BoolValue")
imp_ArrayValue = Class(name="imp::ArrayValue")
imp_ArrayDecl = Class(name="imp::ArrayDecl")

# imp_Stmt class attributes and methods

# imp_Skip class attributes and methods

# Stmt class attributes and methods

# imp_Assign class attributes and methods
imp_Assign_name: Property = Property(name="name", type=StringType)
imp_Assign.attributes={imp_Assign_name}

# imp_Expr class attributes and methods

# imp_Block class attributes and methods

# imp_If class attributes and methods

# imp_Binary class attributes and methods
imp_Binary_op: Property = Property(name="op", type=StringType)
imp_Binary.attributes={imp_Binary_op}

# imp_Store class attributes and methods

# imp_StringToValueMap class attributes and methods
imp_StringToValueMap_key: Property = Property(name="key", type=StringType)
imp_StringToValueMap.attributes={imp_StringToValueMap_key}

# imp_While class attributes and methods

# imp_IntConst class attributes and methods
imp_IntConst_value: Property = Property(name="value", type=IntegerType)
imp_IntConst.attributes={imp_IntConst_value}

# Expr class attributes and methods

# imp_Var class attributes and methods
imp_Var_name: Property = Property(name="name", type=StringType)
imp_Var.attributes={imp_Var_name}

# imp_Unary class attributes and methods
imp_Unary_op: Property = Property(name="op", type=StringType)
imp_Unary.attributes={imp_Unary_op}

# imp_BoolConst class attributes and methods
imp_BoolConst_value: Property = Property(name="value", type=BooleanType)
imp_BoolConst.attributes={imp_BoolConst_value}

# imp_Value class attributes and methods

# imp_IntValue class attributes and methods
imp_IntValue_value: Property = Property(name="value", type=IntegerType)
imp_IntValue.attributes={imp_IntValue_value}

# Value class attributes and methods

# imp_BoolValue class attributes and methods
imp_BoolValue_value: Property = Property(name="value", type=BooleanType)
imp_BoolValue.attributes={imp_BoolValue_value}

# imp_ArrayValue class attributes and methods

# imp_ArrayDecl class attributes and methods

# Relationships
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="imp_Expr", type=imp_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Assign", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index1: BinaryAssociation = BinaryAssociation(
    name="index1",
    ends={
        Property(name="imp_Expr3", type=imp_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Assign2", type=imp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts4: BinaryAssociation = BinaryAssociation(
    name="stmts4",
    ends={
        Property(name="imp_Stmt", type=imp_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Block", type=imp_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond5: BinaryAssociation = BinaryAssociation(
    name="cond5",
    ends={
        Property(name="imp_Expr6", type=imp_If, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_If", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="imp_Stmt9", type=imp_If, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_If8", type=imp_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs10: BinaryAssociation = BinaryAssociation(
    name="rhs10",
    ends={
        Property(name="imp_Stmt12", type=imp_If, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_If11", type=imp_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr20: BinaryAssociation = BinaryAssociation(
    name="expr20",
    ends={
        Property(name="imp_Expr21", type=imp_Unary, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Unary", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs22: BinaryAssociation = BinaryAssociation(
    name="lhs22",
    ends={
        Property(name="imp_Expr23", type=imp_Binary, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Binary", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs24: BinaryAssociation = BinaryAssociation(
    name="rhs24",
    ends={
        Property(name="imp_Expr26", type=imp_Binary, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Binary25", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values27: BinaryAssociation = BinaryAssociation(
    name="values27",
    ends={
        Property(name="imp_StringToValueMap", type=imp_Store, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Store", type=imp_StringToValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond13: BinaryAssociation = BinaryAssociation(
    name="cond13",
    ends={
        Property(name="imp_Expr14", type=imp_While, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_While", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body15: BinaryAssociation = BinaryAssociation(
    name="body15",
    ends={
        Property(name="imp_Stmt17", type=imp_While, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_While16", type=imp_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index18: BinaryAssociation = BinaryAssociation(
    name="index18",
    ends={
        Property(name="imp_Expr19", type=imp_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Var", type=imp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="imp_Value", type=imp_StringToValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_StringToValueMap29", type=imp_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="imp_Value31", type=imp_ArrayValue, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_ArrayValue", type=imp_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values32: BinaryAssociation = BinaryAssociation(
    name="values32",
    ends={
        Property(name="imp_Expr33", type=imp_ArrayDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_ArrayDecl", type=imp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_imp_Skip_Stmt = Generalization(general=Stmt, specific=imp_Skip)
gen_imp_Assign_Stmt = Generalization(general=Stmt, specific=imp_Assign)
gen_imp_Block_Stmt = Generalization(general=Stmt, specific=imp_Block)
gen_imp_If_Stmt = Generalization(general=Stmt, specific=imp_If)
gen_imp_Binary_Expr = Generalization(general=Expr, specific=imp_Binary)
gen_imp_While_Stmt = Generalization(general=Stmt, specific=imp_While)
gen_imp_IntConst_Expr = Generalization(general=Expr, specific=imp_IntConst)
gen_imp_Var_Expr = Generalization(general=Expr, specific=imp_Var)
gen_imp_Unary_Expr = Generalization(general=Expr, specific=imp_Unary)
gen_imp_BoolConst_Expr = Generalization(general=Expr, specific=imp_BoolConst)
gen_imp_IntValue_Value = Generalization(general=Value, specific=imp_IntValue)
gen_imp_BoolValue_Value = Generalization(general=Value, specific=imp_BoolValue)
gen_imp_ArrayValue_Value = Generalization(general=Value, specific=imp_ArrayValue)
gen_imp_ArrayDecl_Expr = Generalization(general=Expr, specific=imp_ArrayDecl)

# Domain Model
domain_model = DomainModel(
    name="imp",
    types={imp_Stmt, imp_Skip, Stmt, imp_Assign, imp_Expr, imp_Block, imp_If, imp_Binary, imp_Store, imp_StringToValueMap, imp_While, imp_IntConst, Expr, imp_Var, imp_Unary, imp_BoolConst, imp_Value, imp_IntValue, Value, imp_BoolValue, imp_ArrayValue, imp_ArrayDecl, UnaryOp, BinaryOp},
    associations={exp0, index1, stmts4, cond5, lhs7, rhs10, expr20, lhs22, rhs24, values27, cond13, body15, index18, value28, values30, values32},
    generalizations={gen_imp_Skip_Stmt, gen_imp_Assign_Stmt, gen_imp_Block_Stmt, gen_imp_If_Stmt, gen_imp_Binary_Expr, gen_imp_While_Stmt, gen_imp_IntConst_Expr, gen_imp_Var_Expr, gen_imp_Unary_Expr, gen_imp_BoolConst_Expr, gen_imp_IntValue_Value, gen_imp_BoolValue_Value, gen_imp_ArrayValue_Value, gen_imp_ArrayDecl_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)