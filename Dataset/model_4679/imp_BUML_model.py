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
imp_Declaration = Class(name="imp::Declaration")
Stmt = Class(name="Stmt")
Symbol = Class(name="Symbol")
imp_Expr = Class(name="imp::Expr", is_abstract=True)
imp_Block = Class(name="imp::Block")
imp_IntConst = Class(name="imp::IntConst")
Expr = Class(name="Expr")
imp_Unary = Class(name="imp::Unary")
imp_Binary = Class(name="imp::Binary")
imp_Store = Class(name="imp::Store")
imp_StringToValueMap = Class(name="imp::StringToValueMap")
imp_Value = Class(name="imp::Value", is_abstract=True)
imp_IntValue = Class(name="imp::IntValue")
Value = Class(name="Value")
imp_If = Class(name="imp::If")
imp_While = Class(name="imp::While")
imp_BoolConst = Class(name="imp::BoolConst")
imp_Program = Class(name="imp::Program")
imp_MethodDecl = Class(name="imp::MethodDecl")
imp_Class = Class(name="imp::Class")
Member = Class(name="Member")
imp_ParamDecl = Class(name="imp::ParamDecl")
imp_Return = Class(name="imp::Return")
imp_Print = Class(name="imp::Print")
imp_StringConst = Class(name="imp::StringConst")
imp_BoolValue = Class(name="imp::BoolValue")
imp_ArrayValue = Class(name="imp::ArrayValue")
imp_ArrayDecl = Class(name="imp::ArrayDecl")
imp_AttributeDecl = Class(name="imp::AttributeDecl")
imp_This = Class(name="imp::This")
imp_NewClass = Class(name="imp::NewClass")
imp_Assignment = Class(name="imp::Assignment")
imp_Project = Class(name="imp::Project")
imp_Member = Class(name="imp::Member", is_abstract=True)
imp_Symbol = Class(name="imp::Symbol", is_abstract=True)
imp_VarRef = Class(name="imp::VarRef")
imp_StringValue = Class(name="imp::StringValue")
imp_NamedElement = Class(name="imp::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")

# imp_Stmt class attributes and methods

# imp_Declaration class attributes and methods
imp_Declaration_name: Property = Property(name="name", type=StringType)
imp_Declaration.attributes={imp_Declaration_name}

# Stmt class attributes and methods

# Symbol class attributes and methods

# imp_Expr class attributes and methods

# imp_Block class attributes and methods

# imp_IntConst class attributes and methods
imp_IntConst_value: Property = Property(name="value", type=IntegerType)
imp_IntConst.attributes={imp_IntConst_value}

# Expr class attributes and methods

# imp_Unary class attributes and methods
imp_Unary_op: Property = Property(name="op", type=StringType)
imp_Unary.attributes={imp_Unary_op}

# imp_Binary class attributes and methods
imp_Binary_op: Property = Property(name="op", type=StringType)
imp_Binary.attributes={imp_Binary_op}

# imp_Store class attributes and methods

# imp_StringToValueMap class attributes and methods
imp_StringToValueMap_key: Property = Property(name="key", type=StringType)
imp_StringToValueMap.attributes={imp_StringToValueMap_key}

# imp_Value class attributes and methods

# imp_IntValue class attributes and methods
imp_IntValue_value: Property = Property(name="value", type=IntegerType)
imp_IntValue.attributes={imp_IntValue_value}

# Value class attributes and methods

# imp_If class attributes and methods

# imp_While class attributes and methods

# imp_BoolConst class attributes and methods
imp_BoolConst_value: Property = Property(name="value", type=BooleanType)
imp_BoolConst.attributes={imp_BoolConst_value}

# imp_Program class attributes and methods

# imp_MethodDecl class attributes and methods
imp_MethodDecl_name: Property = Property(name="name", type=StringType)
imp_MethodDecl.attributes={imp_MethodDecl_name}

# imp_Class class attributes and methods
imp_Class_name: Property = Property(name="name", type=StringType)
imp_Class.attributes={imp_Class_name}

# Member class attributes and methods

# imp_ParamDecl class attributes and methods
imp_ParamDecl_name: Property = Property(name="name", type=StringType)
imp_ParamDecl.attributes={imp_ParamDecl_name}

# imp_Return class attributes and methods

# imp_Print class attributes and methods

# imp_StringConst class attributes and methods
imp_StringConst_value: Property = Property(name="value", type=StringType)
imp_StringConst.attributes={imp_StringConst_value}

# imp_BoolValue class attributes and methods
imp_BoolValue_value: Property = Property(name="value", type=BooleanType)
imp_BoolValue.attributes={imp_BoolValue_value}

# imp_ArrayValue class attributes and methods

# imp_ArrayDecl class attributes and methods

# imp_AttributeDecl class attributes and methods
imp_AttributeDecl_name: Property = Property(name="name", type=StringType)
imp_AttributeDecl.attributes={imp_AttributeDecl_name}

# imp_This class attributes and methods

# imp_NewClass class attributes and methods

# imp_Assignment class attributes and methods

# imp_Project class attributes and methods
imp_Project_ismethodcall: Property = Property(name="ismethodcall", type=BooleanType)
imp_Project.attributes={imp_Project_ismethodcall}

# imp_Member class attributes and methods

# imp_Symbol class attributes and methods

# imp_VarRef class attributes and methods

# imp_StringValue class attributes and methods
imp_StringValue_value: Property = Property(name="value", type=StringType)
imp_StringValue.attributes={imp_StringValue_value}

# imp_NamedElement class attributes and methods

# NamedElement class attributes and methods

# Relationships
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="imp_Expr", type=imp_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Declaration", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index1: BinaryAssociation = BinaryAssociation(
    name="index1",
    ends={
        Property(name="imp_Expr3", type=imp_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Declaration2", type=imp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts4: BinaryAssociation = BinaryAssociation(
    name="stmts4",
    ends={
        Property(name="imp_Stmt", type=imp_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Block", type=imp_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body15: BinaryAssociation = BinaryAssociation(
    name="body15",
    ends={
        Property(name="imp_Stmt17", type=imp_While, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_While16", type=imp_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr18: BinaryAssociation = BinaryAssociation(
    name="expr18",
    ends={
        Property(name="imp_Expr19", type=imp_Unary, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Unary", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs20: BinaryAssociation = BinaryAssociation(
    name="lhs20",
    ends={
        Property(name="imp_Expr21", type=imp_Binary, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Binary", type=imp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs22: BinaryAssociation = BinaryAssociation(
    name="rhs22",
    ends={
        Property(name="imp_Expr24", type=imp_Binary, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Binary23", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values25: BinaryAssociation = BinaryAssociation(
    name="values25",
    ends={
        Property(name="imp_StringToValueMap", type=imp_Store, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Store", type=imp_StringToValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="imp_Value", type=imp_StringToValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_StringToValueMap27", type=imp_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
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
cond13: BinaryAssociation = BinaryAssociation(
    name="cond13",
    ends={
        Property(name="imp_Expr14", type=imp_While, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_While", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="imp_Expr31", type=imp_ArrayDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_ArrayDecl", type=imp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods32: BinaryAssociation = BinaryAssociation(
    name="methods32",
    ends={
        Property(name="imp_MethodDecl", type=imp_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Program", type=imp_MethodDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes33: BinaryAssociation = BinaryAssociation(
    name="classes33",
    ends={
        Property(name="imp_Class", type=imp_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Program34", type=imp_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmt35: BinaryAssociation = BinaryAssociation(
    name="stmt35",
    ends={
        Property(name="imp_Stmt37", type=imp_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_MethodDecl36", type=imp_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
params38: BinaryAssociation = BinaryAssociation(
    name="params38",
    ends={
        Property(name="imp_ParamDecl", type=imp_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_MethodDecl39", type=imp_ParamDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr40: BinaryAssociation = BinaryAssociation(
    name="expr40",
    ends={
        Property(name="imp_Expr41", type=imp_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Return", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr42: BinaryAssociation = BinaryAssociation(
    name="expr42",
    ends={
        Property(name="imp_Expr43", type=imp_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Print", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values28: BinaryAssociation = BinaryAssociation(
    name="values28",
    ends={
        Property(name="imp_Value29", type=imp_ArrayValue, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_ArrayValue", type=imp_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes44: BinaryAssociation = BinaryAssociation(
    name="attributes44",
    ends={
        Property(name="imp_AttributeDecl", type=imp_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Class45", type=imp_AttributeDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods46: BinaryAssociation = BinaryAssociation(
    name="methods46",
    ends={
        Property(name="imp_MethodDecl48", type=imp_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Class47", type=imp_MethodDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class49: BinaryAssociation = BinaryAssociation(
    name="class49",
    ends={
        Property(name="imp_Class50", type=imp_NewClass, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_NewClass", type=imp_Class, multiplicity=Multiplicity(1, 1))
    }
)
lhs51: BinaryAssociation = BinaryAssociation(
    name="lhs51",
    ends={
        Property(name="imp_Expr52", type=imp_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Assignment", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs53: BinaryAssociation = BinaryAssociation(
    name="rhs53",
    ends={
        Property(name="imp_Expr55", type=imp_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Assignment54", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs56: BinaryAssociation = BinaryAssociation(
    name="lhs56",
    ends={
        Property(name="imp_Expr57", type=imp_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Project", type=imp_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs58: BinaryAssociation = BinaryAssociation(
    name="rhs58",
    ends={
        Property(name="imp_Member", type=imp_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Project59", type=imp_Member, multiplicity=Multiplicity(1, 1))
    }
)
params60: BinaryAssociation = BinaryAssociation(
    name="params60",
    ends={
        Property(name="imp_Expr62", type=imp_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_Project61", type=imp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref63: BinaryAssociation = BinaryAssociation(
    name="ref63",
    ends={
        Property(name="imp_Symbol", type=imp_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="imp_VarRef", type=imp_Symbol, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_imp_Declaration_Stmt = Generalization(general=Stmt, specific=imp_Declaration)
gen_imp_Declaration_Symbol = Generalization(general=Symbol, specific=imp_Declaration)
gen_imp_Expr_Stmt = Generalization(general=Stmt, specific=imp_Expr)
gen_imp_Block_Stmt = Generalization(general=Stmt, specific=imp_Block)
gen_imp_IntConst_Expr = Generalization(general=Expr, specific=imp_IntConst)
gen_imp_Unary_Expr = Generalization(general=Expr, specific=imp_Unary)
gen_imp_Binary_Expr = Generalization(general=Expr, specific=imp_Binary)
gen_imp_IntValue_Value = Generalization(general=Value, specific=imp_IntValue)
gen_imp_If_Stmt = Generalization(general=Stmt, specific=imp_If)
gen_imp_While_Stmt = Generalization(general=Stmt, specific=imp_While)
gen_imp_BoolConst_Expr = Generalization(general=Expr, specific=imp_BoolConst)
gen_imp_MethodDecl_Member = Generalization(general=Member, specific=imp_MethodDecl)
gen_imp_Return_Stmt = Generalization(general=Stmt, specific=imp_Return)
gen_imp_Print_Stmt = Generalization(general=Stmt, specific=imp_Print)
gen_imp_StringConst_Expr = Generalization(general=Expr, specific=imp_StringConst)
gen_imp_BoolValue_Value = Generalization(general=Value, specific=imp_BoolValue)
gen_imp_ArrayValue_Value = Generalization(general=Value, specific=imp_ArrayValue)
gen_imp_ArrayDecl_Expr = Generalization(general=Expr, specific=imp_ArrayDecl)
gen_imp_AttributeDecl_Member = Generalization(general=Member, specific=imp_AttributeDecl)
gen_imp_This_Expr = Generalization(general=Expr, specific=imp_This)
gen_imp_NewClass_Expr = Generalization(general=Expr, specific=imp_NewClass)
gen_imp_Assignment_Stmt = Generalization(general=Stmt, specific=imp_Assignment)
gen_imp_Project_Expr = Generalization(general=Expr, specific=imp_Project)
gen_imp_Symbol_NamedElement = Generalization(general=NamedElement, specific=imp_Symbol)
gen_imp_VarRef_Expr = Generalization(general=Expr, specific=imp_VarRef)
gen_imp_StringValue_Value = Generalization(general=Value, specific=imp_StringValue)
gen_imp_ParamDecl_Symbol = Generalization(general=Symbol, specific=imp_ParamDecl)
gen_imp_Class_NamedElement = Generalization(general=NamedElement, specific=imp_Class)

# Domain Model
domain_model = DomainModel(
    name="imp",
    types={imp_Stmt, imp_Declaration, Stmt, Symbol, imp_Expr, imp_Block, imp_IntConst, Expr, imp_Unary, imp_Binary, imp_Store, imp_StringToValueMap, imp_Value, imp_IntValue, Value, imp_If, imp_While, imp_BoolConst, imp_Program, imp_MethodDecl, imp_Class, Member, imp_ParamDecl, imp_Return, imp_Print, imp_StringConst, imp_BoolValue, imp_ArrayValue, imp_ArrayDecl, imp_AttributeDecl, imp_This, imp_NewClass, imp_Assignment, imp_Project, imp_Member, imp_Symbol, imp_VarRef, imp_StringValue, imp_NamedElement, NamedElement, UnaryOp, BinaryOp},
    associations={exp0, index1, stmts4, body15, expr18, lhs20, rhs22, values25, value26, cond5, lhs7, rhs10, cond13, values30, methods32, classes33, stmt35, params38, expr40, expr42, values28, attributes44, methods46, class49, lhs51, rhs53, lhs56, rhs58, params60, ref63},
    generalizations={gen_imp_Declaration_Stmt, gen_imp_Declaration_Symbol, gen_imp_Expr_Stmt, gen_imp_Block_Stmt, gen_imp_IntConst_Expr, gen_imp_Unary_Expr, gen_imp_Binary_Expr, gen_imp_IntValue_Value, gen_imp_If_Stmt, gen_imp_While_Stmt, gen_imp_BoolConst_Expr, gen_imp_MethodDecl_Member, gen_imp_Return_Stmt, gen_imp_Print_Stmt, gen_imp_StringConst_Expr, gen_imp_BoolValue_Value, gen_imp_ArrayValue_Value, gen_imp_ArrayDecl_Expr, gen_imp_AttributeDecl_Member, gen_imp_This_Expr, gen_imp_NewClass_Expr, gen_imp_Assignment_Stmt, gen_imp_Project_Expr, gen_imp_Symbol_NamedElement, gen_imp_VarRef_Expr, gen_imp_StringValue_Value, gen_imp_ParamDecl_Symbol, gen_imp_Class_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)