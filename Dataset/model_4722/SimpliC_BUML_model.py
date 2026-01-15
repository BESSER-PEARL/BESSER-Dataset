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
simpliC_Model = Class(name="simpliC::Model")
simpliC_Function = Class(name="simpliC::Function")
simpliC_Type = Class(name="simpliC::Type")
simpliC_Args = Class(name="simpliC::Args")
simpliC_Block = Class(name="simpliC::Block")
Stmt = Class(name="Stmt")
simpliC_Stmt = Class(name="simpliC::Stmt")
simpliC_Call = Class(name="simpliC::Call")
simpliC_Expr = Class(name="simpliC::Expr")
simpliC_ExprCall = Class(name="simpliC::ExprCall")
Factor = Class(name="Factor")
simpliC_Ifstmt = Class(name="simpliC::Ifstmt")
simpliC_Whilestmt = Class(name="simpliC::Whilestmt")
simpliC_Return = Class(name="simpliC::Return")
simpliC_Decl = Class(name="simpliC::Decl")
simpliC_Typedef = Class(name="simpliC::Typedef")
simpliC_Assign = Class(name="simpliC::Assign")
simpliC_EObject = Class(name="simpliC::EObject")
simpliC_TFact = Class(name="simpliC::TFact")
simpliC_Factor = Class(name="simpliC::Factor")
simpliC_IDuse = Class(name="simpliC::IDuse")

# simpliC_Model class attributes and methods

# simpliC_Function class attributes and methods
simpliC_Function_name: Property = Property(name="name", type=StringType)
simpliC_Function.attributes={simpliC_Function_name}

# simpliC_Type class attributes and methods
simpliC_Type_name: Property = Property(name="name", type=StringType)
simpliC_Type.attributes={simpliC_Type_name}

# simpliC_Args class attributes and methods
simpliC_Args_name: Property = Property(name="name", type=StringType)
simpliC_Args.attributes={simpliC_Args_name}

# simpliC_Block class attributes and methods

# Stmt class attributes and methods

# simpliC_Stmt class attributes and methods

# simpliC_Call class attributes and methods

# simpliC_Expr class attributes and methods
simpliC_Expr_op: Property = Property(name="op", type=StringType)
simpliC_Expr.attributes={simpliC_Expr_op}

# simpliC_ExprCall class attributes and methods

# Factor class attributes and methods

# simpliC_Ifstmt class attributes and methods

# simpliC_Whilestmt class attributes and methods

# simpliC_Return class attributes and methods

# simpliC_Decl class attributes and methods
simpliC_Decl_name: Property = Property(name="name", type=StringType)
simpliC_Decl.attributes={simpliC_Decl_name}

# simpliC_Typedef class attributes and methods
simpliC_Typedef_name: Property = Property(name="name", type=StringType)
simpliC_Typedef.attributes={simpliC_Typedef_name}

# simpliC_Assign class attributes and methods
simpliC_Assign_var: Property = Property(name="var", type=StringType)
simpliC_Assign.attributes={simpliC_Assign_var}

# simpliC_EObject class attributes and methods

# simpliC_TFact class attributes and methods
simpliC_TFact_op: Property = Property(name="op", type=StringType)
simpliC_TFact.attributes={simpliC_TFact_op}

# simpliC_Factor class attributes and methods

# simpliC_IDuse class attributes and methods

# Relationships
Else23: BinaryAssociation = BinaryAssociation(
    name="Else23",
    ends={
        Property(name="simpliC_Block25", type=simpliC_Ifstmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Ifstmt24", type=simpliC_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Program0: BinaryAssociation = BinaryAssociation(
    name="Program0",
    ends={
        Property(name="simpliC_Function", type=simpliC_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Model", type=simpliC_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="simpliC_Type", type=simpliC_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Function2", type=simpliC_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Arglist3: BinaryAssociation = BinaryAssociation(
    name="Arglist3",
    ends={
        Property(name="simpliC_Args", type=simpliC_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Function4", type=simpliC_Args, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="simpliC_Block", type=simpliC_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Function6", type=simpliC_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block7: BinaryAssociation = BinaryAssociation(
    name="block7",
    ends={
        Property(name="simpliC_Stmt", type=simpliC_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Block8", type=simpliC_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionID9: BinaryAssociation = BinaryAssociation(
    name="functionID9",
    ends={
        Property(name="simpliC_Function10", type=simpliC_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Call", type=simpliC_Function, multiplicity=Multiplicity(0, 1))
    }
)
Paramlist11: BinaryAssociation = BinaryAssociation(
    name="Paramlist11",
    ends={
        Property(name="simpliC_Expr", type=simpliC_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Call12", type=simpliC_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionID13: BinaryAssociation = BinaryAssociation(
    name="functionID13",
    ends={
        Property(name="simpliC_Function14", type=simpliC_ExprCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_ExprCall", type=simpliC_Function, multiplicity=Multiplicity(0, 1))
    }
)
Paramlist15: BinaryAssociation = BinaryAssociation(
    name="Paramlist15",
    ends={
        Property(name="simpliC_Expr17", type=simpliC_ExprCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_ExprCall16", type=simpliC_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond18: BinaryAssociation = BinaryAssociation(
    name="cond18",
    ends={
        Property(name="simpliC_Expr19", type=simpliC_Ifstmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Ifstmt", type=simpliC_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Then20: BinaryAssociation = BinaryAssociation(
    name="Then20",
    ends={
        Property(name="simpliC_Block22", type=simpliC_Ifstmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Ifstmt21", type=simpliC_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="simpliC_Type56", type=simpliC_Args, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Args55", type=simpliC_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond26: BinaryAssociation = BinaryAssociation(
    name="cond26",
    ends={
        Property(name="simpliC_Expr27", type=simpliC_Whilestmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Whilestmt", type=simpliC_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Then28: BinaryAssociation = BinaryAssociation(
    name="Then28",
    ends={
        Property(name="simpliC_Block30", type=simpliC_Whilestmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Whilestmt29", type=simpliC_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="simpliC_Expr32", type=simpliC_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Return", type=simpliC_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="simpliC_Type34", type=simpliC_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Decl", type=simpliC_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vtype35: BinaryAssociation = BinaryAssociation(
    name="vtype35",
    ends={
        Property(name="simpliC_Typedef", type=simpliC_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Decl36", type=simpliC_Typedef, multiplicity=Multiplicity(0, 1))
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="simpliC_Expr39", type=simpliC_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Decl38", type=simpliC_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value40: BinaryAssociation = BinaryAssociation(
    name="value40",
    ends={
        Property(name="simpliC_Expr41", type=simpliC_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Assign", type=simpliC_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rh42: BinaryAssociation = BinaryAssociation(
    name="rh42",
    ends={
        Property(name="simpliC_EObject", type=simpliC_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Expr43", type=simpliC_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lh44: BinaryAssociation = BinaryAssociation(
    name="lh44",
    ends={
        Property(name="simpliC_EObject46", type=simpliC_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Expr45", type=simpliC_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms47: BinaryAssociation = BinaryAssociation(
    name="terms47",
    ends={
        Property(name="simpliC_TFact", type=simpliC_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Expr48", type=simpliC_TFact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lh49: BinaryAssociation = BinaryAssociation(
    name="lh49",
    ends={
        Property(name="simpliC_Expr51", type=simpliC_TFact, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_TFact50", type=simpliC_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name52: BinaryAssociation = BinaryAssociation(
    name="name52",
    ends={
        Property(name="simpliC_Decl53", type=simpliC_IDuse, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_IDuse", type=simpliC_Decl, multiplicity=Multiplicity(0, 1))
    }
)
oldtype57: BinaryAssociation = BinaryAssociation(
    name="oldtype57",
    ends={
        Property(name="simpliC_EObject59", type=simpliC_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="simpliC_Typedef58", type=simpliC_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simpliC_Block_Stmt = Generalization(general=Stmt, specific=simpliC_Block)
gen_simpliC_Call_Stmt = Generalization(general=Stmt, specific=simpliC_Call)
gen_simpliC_ExprCall_Factor = Generalization(general=Factor, specific=simpliC_ExprCall)
gen_simpliC_Ifstmt_Stmt = Generalization(general=Stmt, specific=simpliC_Ifstmt)
gen_simpliC_Whilestmt_Stmt = Generalization(general=Stmt, specific=simpliC_Whilestmt)
gen_simpliC_Return_Stmt = Generalization(general=Stmt, specific=simpliC_Return)
gen_simpliC_Decl_Stmt = Generalization(general=Stmt, specific=simpliC_Decl)
gen_simpliC_Assign_Stmt = Generalization(general=Stmt, specific=simpliC_Assign)
gen_simpliC_IDuse_Factor = Generalization(general=Factor, specific=simpliC_IDuse)
gen_simpliC_Typedef_Stmt = Generalization(general=Stmt, specific=simpliC_Typedef)

# Domain Model
domain_model = DomainModel(
    name="simpliC",
    types={simpliC_Model, simpliC_Function, simpliC_Type, simpliC_Args, simpliC_Block, Stmt, simpliC_Stmt, simpliC_Call, simpliC_Expr, simpliC_ExprCall, Factor, simpliC_Ifstmt, simpliC_Whilestmt, simpliC_Return, simpliC_Decl, simpliC_Typedef, simpliC_Assign, simpliC_EObject, simpliC_TFact, simpliC_Factor, simpliC_IDuse},
    associations={Else23, Program0, type1, Arglist3, body5, block7, functionID9, Paramlist11, functionID13, Paramlist15, cond18, Then20, type54, cond26, Then28, value31, type33, vtype35, value37, value40, rh42, lh44, terms47, lh49, name52, oldtype57},
    generalizations={gen_simpliC_Block_Stmt, gen_simpliC_Call_Stmt, gen_simpliC_ExprCall_Factor, gen_simpliC_Ifstmt_Stmt, gen_simpliC_Whilestmt_Stmt, gen_simpliC_Return_Stmt, gen_simpliC_Decl_Stmt, gen_simpliC_Assign_Stmt, gen_simpliC_IDuse_Factor, gen_simpliC_Typedef_Stmt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)