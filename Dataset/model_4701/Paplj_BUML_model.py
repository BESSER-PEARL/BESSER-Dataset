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
paplj_Program = Class(name="paplj::Program")
paplj_Import = Class(name="paplj::Import")
paplj_Type = Class(name="paplj::Type")
paplj_Expr = Class(name="paplj::Expr")
paplj_Field = Class(name="paplj::Field")
Member = Class(name="Member")
paplj_Method = Class(name="paplj::Method")
paplj_Param = Class(name="paplj::Param")
paplj_Block2 = Class(name="paplj::Block2")
paplj_Binding = Class(name="paplj::Binding")
Expr = Class(name="Expr")
paplj_If = Class(name="paplj::If")
paplj_Let = Class(name="paplj::Let")
paplj_Assignment = Class(name="paplj::Assignment")
paplj_Or = Class(name="paplj::Or")
paplj_Member = Class(name="paplj::Member")
Symbol = Class(name="Symbol")
paplj_Symbol = Class(name="paplj::Symbol")
paplj_Eq = Class(name="paplj::Eq")
paplj_Neq = Class(name="paplj::Neq")
paplj_Lt = Class(name="paplj::Lt")
paplj_Add = Class(name="paplj::Add")
paplj_Sub = Class(name="paplj::Sub")
paplj_Mul = Class(name="paplj::Mul")
paplj_Div = Class(name="paplj::Div")
paplj_And = Class(name="paplj::And")
paplj_Not = Class(name="paplj::Not")
paplj_Min = Class(name="paplj::Min")
paplj_MemberRef = Class(name="paplj::MemberRef")
paplj_Num = Class(name="paplj::Num")
paplj_Bool = Class(name="paplj::Bool")
paplj_This = Class(name="paplj::This")
paplj_Null = Class(name="paplj::Null")
paplj_New = Class(name="paplj::New")
paplj_Var = Class(name="paplj::Var")
paplj_Cast = Class(name="paplj::Cast")

# paplj_Program class attributes and methods
paplj_Program_name: Property = Property(name="name", type=StringType)
paplj_Program.attributes={paplj_Program_name}

# paplj_Import class attributes and methods
paplj_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
paplj_Import.attributes={paplj_Import_importedNamespace}

# paplj_Type class attributes and methods
paplj_Type_name: Property = Property(name="name", type=StringType)
paplj_Type.attributes={paplj_Type_name}

# paplj_Expr class attributes and methods

# paplj_Field class attributes and methods

# Member class attributes and methods

# paplj_Method class attributes and methods

# paplj_Param class attributes and methods

# paplj_Block2 class attributes and methods

# paplj_Binding class attributes and methods

# Expr class attributes and methods

# paplj_If class attributes and methods

# paplj_Let class attributes and methods

# paplj_Assignment class attributes and methods

# paplj_Or class attributes and methods

# paplj_Member class attributes and methods

# Symbol class attributes and methods

# paplj_Symbol class attributes and methods
paplj_Symbol_name: Property = Property(name="name", type=StringType)
paplj_Symbol.attributes={paplj_Symbol_name}

# paplj_Eq class attributes and methods

# paplj_Neq class attributes and methods

# paplj_Lt class attributes and methods

# paplj_Add class attributes and methods

# paplj_Sub class attributes and methods

# paplj_Mul class attributes and methods

# paplj_Div class attributes and methods

# paplj_And class attributes and methods

# paplj_Not class attributes and methods

# paplj_Min class attributes and methods

# paplj_MemberRef class attributes and methods
paplj_MemberRef_methodInvocation: Property = Property(name="methodInvocation", type=BooleanType)
paplj_MemberRef.attributes={paplj_MemberRef_methodInvocation}

# paplj_Num class attributes and methods
paplj_Num_value: Property = Property(name="value", type=IntegerType)
paplj_Num.attributes={paplj_Num_value}

# paplj_Bool class attributes and methods
paplj_Bool_true: Property = Property(name="true", type=BooleanType)
paplj_Bool.attributes={paplj_Bool_true}

# paplj_This class attributes and methods

# paplj_Null class attributes and methods

# paplj_New class attributes and methods

# paplj_Var class attributes and methods
paplj_Var_methodInvocation: Property = Property(name="methodInvocation", type=BooleanType)
paplj_Var.attributes={paplj_Var_methodInvocation}

# paplj_Cast class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="paplj_Import", type=paplj_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Program", type=paplj_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="paplj_Type", type=paplj_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Program2", type=paplj_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr3: BinaryAssociation = BinaryAssociation(
    name="expr3",
    ends={
        Property(name="paplj_Expr", type=paplj_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Program4", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params12: BinaryAssociation = BinaryAssociation(
    name="params12",
    ends={
        Property(name="paplj_Param", type=paplj_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Method", type=paplj_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body13: BinaryAssociation = BinaryAssociation(
    name="body13",
    ends={
        Property(name="paplj_Block2", type=paplj_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Method14", type=paplj_Block2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="paplj_Expr16", type=paplj_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Binding", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs17: BinaryAssociation = BinaryAssociation(
    name="exprs17",
    ends={
        Property(name="paplj_Expr19", type=paplj_Block2, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Block218", type=paplj_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition20: BinaryAssociation = BinaryAssociation(
    name="condition20",
    ends={
        Property(name="paplj_Expr21", type=paplj_If, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_If", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrue22: BinaryAssociation = BinaryAssociation(
    name="onTrue22",
    ends={
        Property(name="paplj_Expr24", type=paplj_If, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_If23", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalse25: BinaryAssociation = BinaryAssociation(
    name="onFalse25",
    ends={
        Property(name="paplj_Expr27", type=paplj_If, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_If26", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings28: BinaryAssociation = BinaryAssociation(
    name="bindings28",
    ends={
        Property(name="paplj_Binding29", type=paplj_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Let", type=paplj_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr30: BinaryAssociation = BinaryAssociation(
    name="expr30",
    ends={
        Property(name="paplj_Expr32", type=paplj_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Let31", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left33: BinaryAssociation = BinaryAssociation(
    name="left33",
    ends={
        Property(name="paplj_Expr34", type=paplj_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Assignment", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="paplj_Expr37", type=paplj_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Assignment36", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType6: BinaryAssociation = BinaryAssociation(
    name="superType6",
    ends={
        Property(name="paplj_Type7", type=paplj_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Type5", type=paplj_Type, multiplicity=Multiplicity(0, 1))
    }
)
members8: BinaryAssociation = BinaryAssociation(
    name="members8",
    ends={
        Property(name="paplj_Member", type=paplj_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Type9", type=paplj_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="paplj_Type11", type=paplj_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Symbol", type=paplj_Type, multiplicity=Multiplicity(0, 1))
    }
)
left48: BinaryAssociation = BinaryAssociation(
    name="left48",
    ends={
        Property(name="paplj_Expr49", type=paplj_Eq, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Eq", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right50: BinaryAssociation = BinaryAssociation(
    name="right50",
    ends={
        Property(name="paplj_Expr52", type=paplj_Eq, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Eq51", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left53: BinaryAssociation = BinaryAssociation(
    name="left53",
    ends={
        Property(name="paplj_Expr54", type=paplj_Neq, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Neq", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right55: BinaryAssociation = BinaryAssociation(
    name="right55",
    ends={
        Property(name="paplj_Expr57", type=paplj_Neq, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Neq56", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left58: BinaryAssociation = BinaryAssociation(
    name="left58",
    ends={
        Property(name="paplj_Expr59", type=paplj_Lt, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Lt", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right60: BinaryAssociation = BinaryAssociation(
    name="right60",
    ends={
        Property(name="paplj_Expr62", type=paplj_Lt, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Lt61", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left63: BinaryAssociation = BinaryAssociation(
    name="left63",
    ends={
        Property(name="paplj_Expr64", type=paplj_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Add", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right65: BinaryAssociation = BinaryAssociation(
    name="right65",
    ends={
        Property(name="paplj_Expr67", type=paplj_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Add66", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left68: BinaryAssociation = BinaryAssociation(
    name="left68",
    ends={
        Property(name="paplj_Expr69", type=paplj_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Sub", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right70: BinaryAssociation = BinaryAssociation(
    name="right70",
    ends={
        Property(name="paplj_Expr72", type=paplj_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Sub71", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left73: BinaryAssociation = BinaryAssociation(
    name="left73",
    ends={
        Property(name="paplj_Expr74", type=paplj_Mul, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Mul", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right75: BinaryAssociation = BinaryAssociation(
    name="right75",
    ends={
        Property(name="paplj_Expr77", type=paplj_Mul, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Mul76", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left38: BinaryAssociation = BinaryAssociation(
    name="left38",
    ends={
        Property(name="paplj_Expr39", type=paplj_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Or", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right40: BinaryAssociation = BinaryAssociation(
    name="right40",
    ends={
        Property(name="paplj_Expr42", type=paplj_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Or41", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left43: BinaryAssociation = BinaryAssociation(
    name="left43",
    ends={
        Property(name="paplj_Expr44", type=paplj_And, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_And", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right45: BinaryAssociation = BinaryAssociation(
    name="right45",
    ends={
        Property(name="paplj_Expr47", type=paplj_And, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_And46", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="paplj_Type87", type=paplj_Cast, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Cast86", type=paplj_Type, multiplicity=Multiplicity(0, 1))
    }
)
expr88: BinaryAssociation = BinaryAssociation(
    name="expr88",
    ends={
        Property(name="paplj_Expr89", type=paplj_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Not", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr90: BinaryAssociation = BinaryAssociation(
    name="expr90",
    ends={
        Property(name="paplj_Expr91", type=paplj_Min, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Min", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left92: BinaryAssociation = BinaryAssociation(
    name="left92",
    ends={
        Property(name="paplj_Expr93", type=paplj_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_MemberRef", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member94: BinaryAssociation = BinaryAssociation(
    name="member94",
    ends={
        Property(name="paplj_Member96", type=paplj_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_MemberRef95", type=paplj_Member, multiplicity=Multiplicity(0, 1))
    }
)
args97: BinaryAssociation = BinaryAssociation(
    name="args97",
    ends={
        Property(name="paplj_Expr99", type=paplj_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_MemberRef98", type=paplj_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type100: BinaryAssociation = BinaryAssociation(
    name="type100",
    ends={
        Property(name="paplj_Type101", type=paplj_Null, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Null", type=paplj_Type, multiplicity=Multiplicity(0, 1))
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="paplj_Type103", type=paplj_New, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_New", type=paplj_Type, multiplicity=Multiplicity(0, 1))
    }
)
member104: BinaryAssociation = BinaryAssociation(
    name="member104",
    ends={
        Property(name="paplj_Symbol105", type=paplj_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Var", type=paplj_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
args106: BinaryAssociation = BinaryAssociation(
    name="args106",
    ends={
        Property(name="paplj_Expr108", type=paplj_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Var107", type=paplj_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left78: BinaryAssociation = BinaryAssociation(
    name="left78",
    ends={
        Property(name="paplj_Expr79", type=paplj_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Div", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="paplj_Expr82", type=paplj_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Div81", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="paplj_Expr84", type=paplj_Cast, multiplicity=Multiplicity(1, 1)),
        Property(name="paplj_Cast", type=paplj_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_paplj_Field_Member = Generalization(general=Member, specific=paplj_Field)
gen_paplj_Method_Member = Generalization(general=Member, specific=paplj_Method)
gen_paplj_Param_Symbol = Generalization(general=Symbol, specific=paplj_Param)
gen_paplj_Binding_Symbol = Generalization(general=Symbol, specific=paplj_Binding)
gen_paplj_Block2_Expr = Generalization(general=Expr, specific=paplj_Block2)
gen_paplj_If_Expr = Generalization(general=Expr, specific=paplj_If)
gen_paplj_Let_Expr = Generalization(general=Expr, specific=paplj_Let)
gen_paplj_Assignment_Expr = Generalization(general=Expr, specific=paplj_Assignment)
gen_paplj_Or_Expr = Generalization(general=Expr, specific=paplj_Or)
gen_paplj_Member_Symbol = Generalization(general=Symbol, specific=paplj_Member)
gen_paplj_Eq_Expr = Generalization(general=Expr, specific=paplj_Eq)
gen_paplj_Neq_Expr = Generalization(general=Expr, specific=paplj_Neq)
gen_paplj_Lt_Expr = Generalization(general=Expr, specific=paplj_Lt)
gen_paplj_Add_Expr = Generalization(general=Expr, specific=paplj_Add)
gen_paplj_Sub_Expr = Generalization(general=Expr, specific=paplj_Sub)
gen_paplj_Mul_Expr = Generalization(general=Expr, specific=paplj_Mul)
gen_paplj_And_Expr = Generalization(general=Expr, specific=paplj_And)
gen_paplj_Not_Expr = Generalization(general=Expr, specific=paplj_Not)
gen_paplj_Min_Expr = Generalization(general=Expr, specific=paplj_Min)
gen_paplj_MemberRef_Expr = Generalization(general=Expr, specific=paplj_MemberRef)
gen_paplj_Num_Expr = Generalization(general=Expr, specific=paplj_Num)
gen_paplj_Bool_Expr = Generalization(general=Expr, specific=paplj_Bool)
gen_paplj_This_Expr = Generalization(general=Expr, specific=paplj_This)
gen_paplj_Null_Expr = Generalization(general=Expr, specific=paplj_Null)
gen_paplj_New_Expr = Generalization(general=Expr, specific=paplj_New)
gen_paplj_Var_Expr = Generalization(general=Expr, specific=paplj_Var)
gen_paplj_Div_Expr = Generalization(general=Expr, specific=paplj_Div)
gen_paplj_Cast_Expr = Generalization(general=Expr, specific=paplj_Cast)

# Domain Model
domain_model = DomainModel(
    name="paplj",
    types={paplj_Program, paplj_Import, paplj_Type, paplj_Expr, paplj_Field, Member, paplj_Method, paplj_Param, paplj_Block2, paplj_Binding, Expr, paplj_If, paplj_Let, paplj_Assignment, paplj_Or, paplj_Member, Symbol, paplj_Symbol, paplj_Eq, paplj_Neq, paplj_Lt, paplj_Add, paplj_Sub, paplj_Mul, paplj_Div, paplj_And, paplj_Not, paplj_Min, paplj_MemberRef, paplj_Num, paplj_Bool, paplj_This, paplj_Null, paplj_New, paplj_Var, paplj_Cast},
    associations={imports0, classes1, expr3, params12, body13, value15, exprs17, condition20, onTrue22, onFalse25, bindings28, expr30, left33, value35, superType6, members8, type10, left48, right50, left53, right55, left58, right60, left63, right65, left68, right70, left73, right75, left38, right40, left43, right45, type85, expr88, expr90, left92, member94, args97, type100, type102, member104, args106, left78, right80, left83},
    generalizations={gen_paplj_Field_Member, gen_paplj_Method_Member, gen_paplj_Param_Symbol, gen_paplj_Binding_Symbol, gen_paplj_Block2_Expr, gen_paplj_If_Expr, gen_paplj_Let_Expr, gen_paplj_Assignment_Expr, gen_paplj_Or_Expr, gen_paplj_Member_Symbol, gen_paplj_Eq_Expr, gen_paplj_Neq_Expr, gen_paplj_Lt_Expr, gen_paplj_Add_Expr, gen_paplj_Sub_Expr, gen_paplj_Mul_Expr, gen_paplj_And_Expr, gen_paplj_Not_Expr, gen_paplj_Min_Expr, gen_paplj_MemberRef_Expr, gen_paplj_Num_Expr, gen_paplj_Bool_Expr, gen_paplj_This_Expr, gen_paplj_Null_Expr, gen_paplj_New_Expr, gen_paplj_Var_Expr, gen_paplj_Div_Expr, gen_paplj_Cast_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)