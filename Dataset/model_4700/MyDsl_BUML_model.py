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
myDsl_File = Class(name="myDsl::File")
myDsl_TopLevelCmd = Class(name="myDsl::TopLevelCmd")
myDsl_Expr = Class(name="myDsl::Expr")
myDsl_Def = Class(name="myDsl::Def")
TopLevelCmd = Class(name="TopLevelCmd")
myDsl_App = Class(name="myDsl::App")
Expr = Class(name="Expr")
myDsl_Project = Class(name="myDsl::Project")
myDsl_BObject = Class(name="myDsl::BObject")
myDsl_Field = Class(name="myDsl::Field")
myDsl_Copy = Class(name="myDsl::Copy")
myDsl_With = Class(name="myDsl::With")
myDsl_Not = Class(name="myDsl::Not")
myDsl_If = Class(name="myDsl::If")
myDsl_Var = Class(name="myDsl::Var")
myDsl_This = Class(name="myDsl::This")
myDsl_Bool = Class(name="myDsl::Bool")
myDsl_Int = Class(name="myDsl::Int")
myDsl_Skip = Class(name="myDsl::Skip")
myDsl_Fun = Class(name="myDsl::Fun")
myDsl_Assign = Class(name="myDsl::Assign")
myDsl_ArithOpPlus = Class(name="myDsl::ArithOpPlus")
myDsl_Let = Class(name="myDsl::Let")
myDsl_ArithOpDivide = Class(name="myDsl::ArithOpDivide")
myDsl_ArithOpRemainder = Class(name="myDsl::ArithOpRemainder")
myDsl_BoolOpAnd = Class(name="myDsl::BoolOpAnd")
myDsl_ArithOpMinus = Class(name="myDsl::ArithOpMinus")
myDsl_ArithOpTimes = Class(name="myDsl::ArithOpTimes")
myDsl_CmpOpEqual = Class(name="myDsl::CmpOpEqual")
myDsl_CmpOpUnequal = Class(name="myDsl::CmpOpUnequal")
myDsl_CmpOpLess = Class(name="myDsl::CmpOpLess")
myDsl_BoolOpOr = Class(name="myDsl::BoolOpOr")
myDsl_Seq = Class(name="myDsl::Seq")

# myDsl_File class attributes and methods

# myDsl_TopLevelCmd class attributes and methods

# myDsl_Expr class attributes and methods

# myDsl_Def class attributes and methods
myDsl_Def_name: Property = Property(name="name", type=StringType)
myDsl_Def.attributes={myDsl_Def_name}

# TopLevelCmd class attributes and methods

# myDsl_App class attributes and methods

# Expr class attributes and methods

# myDsl_Project class attributes and methods
myDsl_Project_name: Property = Property(name="name", type=StringType)
myDsl_Project.attributes={myDsl_Project_name}

# myDsl_BObject class attributes and methods

# myDsl_Field class attributes and methods
myDsl_Field_name: Property = Property(name="name", type=StringType)
myDsl_Field.attributes={myDsl_Field_name}

# myDsl_Copy class attributes and methods

# myDsl_With class attributes and methods

# myDsl_Not class attributes and methods

# myDsl_If class attributes and methods

# myDsl_Var class attributes and methods
myDsl_Var_name: Property = Property(name="name", type=StringType)
myDsl_Var.attributes={myDsl_Var_name}

# myDsl_This class attributes and methods

# myDsl_Bool class attributes and methods
myDsl_Bool_value: Property = Property(name="value", type=BooleanType)
myDsl_Bool.attributes={myDsl_Bool_value}

# myDsl_Int class attributes and methods
myDsl_Int_value: Property = Property(name="value", type=IntegerType)
myDsl_Int.attributes={myDsl_Int_value}

# myDsl_Skip class attributes and methods

# myDsl_Fun class attributes and methods
myDsl_Fun_name: Property = Property(name="name", type=StringType)
myDsl_Fun.attributes={myDsl_Fun_name}

# myDsl_Assign class attributes and methods
myDsl_Assign_name: Property = Property(name="name", type=StringType)
myDsl_Assign.attributes={myDsl_Assign_name}

# myDsl_ArithOpPlus class attributes and methods

# myDsl_Let class attributes and methods
myDsl_Let_name: Property = Property(name="name", type=StringType)
myDsl_Let.attributes={myDsl_Let_name}

# myDsl_ArithOpDivide class attributes and methods

# myDsl_ArithOpRemainder class attributes and methods

# myDsl_BoolOpAnd class attributes and methods

# myDsl_ArithOpMinus class attributes and methods

# myDsl_ArithOpTimes class attributes and methods

# myDsl_CmpOpEqual class attributes and methods

# myDsl_CmpOpUnequal class attributes and methods

# myDsl_CmpOpLess class attributes and methods

# myDsl_BoolOpOr class attributes and methods

# myDsl_Seq class attributes and methods

# Relationships
commands0: BinaryAssociation = BinaryAssociation(
    name="commands0",
    ends={
        Property(name="myDsl_TopLevelCmd", type=myDsl_File, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_File", type=myDsl_TopLevelCmd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr1: BinaryAssociation = BinaryAssociation(
    name="expr1",
    ends={
        Property(name="myDsl_Expr", type=myDsl_Def, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Def", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp7: BinaryAssociation = BinaryAssociation(
    name="exp7",
    ends={
        Property(name="myDsl_Expr8", type=myDsl_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Project", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields9: BinaryAssociation = BinaryAssociation(
    name="fields9",
    ends={
        Property(name="myDsl_Field", type=myDsl_BObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BObject", type=myDsl_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copy10: BinaryAssociation = BinaryAssociation(
    name="copy10",
    ends={
        Property(name="myDsl_Expr11", type=myDsl_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Copy", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs12: BinaryAssociation = BinaryAssociation(
    name="lhs12",
    ends={
        Property(name="myDsl_Expr13", type=myDsl_With, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_With", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs14: BinaryAssociation = BinaryAssociation(
    name="rhs14",
    ends={
        Property(name="myDsl_Expr16", type=myDsl_With, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_With15", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="myDsl_Expr18", type=myDsl_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Not", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs2: BinaryAssociation = BinaryAssociation(
    name="lhs2",
    ends={
        Property(name="myDsl_Expr3", type=myDsl_App, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_App", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs4: BinaryAssociation = BinaryAssociation(
    name="rhs4",
    ends={
        Property(name="myDsl_Expr6", type=myDsl_App, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_App5", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="myDsl_Expr33", type=myDsl_Fun, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fun", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs34: BinaryAssociation = BinaryAssociation(
    name="lhs34",
    ends={
        Property(name="myDsl_Expr35", type=myDsl_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Assign", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs36: BinaryAssociation = BinaryAssociation(
    name="rhs36",
    ends={
        Property(name="myDsl_Expr38", type=myDsl_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Assign37", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs39: BinaryAssociation = BinaryAssociation(
    name="lhs39",
    ends={
        Property(name="myDsl_Expr40", type=myDsl_ArithOpPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpPlus", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond19: BinaryAssociation = BinaryAssociation(
    name="cond19",
    ends={
        Property(name="myDsl_Expr20", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thn21: BinaryAssociation = BinaryAssociation(
    name="thn21",
    ends={
        Property(name="myDsl_Expr23", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If22", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
els24: BinaryAssociation = BinaryAssociation(
    name="els24",
    ends={
        Property(name="myDsl_Expr26", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If25", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs27: BinaryAssociation = BinaryAssociation(
    name="lhs27",
    ends={
        Property(name="myDsl_Expr28", type=myDsl_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Let", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs29: BinaryAssociation = BinaryAssociation(
    name="rhs29",
    ends={
        Property(name="myDsl_Expr31", type=myDsl_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Let30", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs49: BinaryAssociation = BinaryAssociation(
    name="lhs49",
    ends={
        Property(name="myDsl_Expr50", type=myDsl_ArithOpTimes, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpTimes", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs51: BinaryAssociation = BinaryAssociation(
    name="rhs51",
    ends={
        Property(name="myDsl_Expr53", type=myDsl_ArithOpTimes, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpTimes52", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs54: BinaryAssociation = BinaryAssociation(
    name="lhs54",
    ends={
        Property(name="myDsl_Expr55", type=myDsl_ArithOpDivide, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpDivide", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs56: BinaryAssociation = BinaryAssociation(
    name="rhs56",
    ends={
        Property(name="myDsl_Expr58", type=myDsl_ArithOpDivide, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpDivide57", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs59: BinaryAssociation = BinaryAssociation(
    name="lhs59",
    ends={
        Property(name="myDsl_Expr60", type=myDsl_ArithOpRemainder, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpRemainder", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs61: BinaryAssociation = BinaryAssociation(
    name="rhs61",
    ends={
        Property(name="myDsl_Expr63", type=myDsl_ArithOpRemainder, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpRemainder62", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs64: BinaryAssociation = BinaryAssociation(
    name="lhs64",
    ends={
        Property(name="myDsl_Expr65", type=myDsl_BoolOpAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BoolOpAnd", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs41: BinaryAssociation = BinaryAssociation(
    name="rhs41",
    ends={
        Property(name="myDsl_Expr43", type=myDsl_ArithOpPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpPlus42", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs44: BinaryAssociation = BinaryAssociation(
    name="lhs44",
    ends={
        Property(name="myDsl_Expr45", type=myDsl_ArithOpMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpMinus", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs46: BinaryAssociation = BinaryAssociation(
    name="rhs46",
    ends={
        Property(name="myDsl_Expr48", type=myDsl_ArithOpMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArithOpMinus47", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs76: BinaryAssociation = BinaryAssociation(
    name="rhs76",
    ends={
        Property(name="myDsl_Expr78", type=myDsl_Seq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Seq77", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs79: BinaryAssociation = BinaryAssociation(
    name="lhs79",
    ends={
        Property(name="myDsl_Expr80", type=myDsl_CmpOpEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CmpOpEqual", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs81: BinaryAssociation = BinaryAssociation(
    name="rhs81",
    ends={
        Property(name="myDsl_Expr83", type=myDsl_CmpOpEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CmpOpEqual82", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs84: BinaryAssociation = BinaryAssociation(
    name="lhs84",
    ends={
        Property(name="myDsl_Expr85", type=myDsl_CmpOpUnequal, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CmpOpUnequal", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs86: BinaryAssociation = BinaryAssociation(
    name="rhs86",
    ends={
        Property(name="myDsl_Expr88", type=myDsl_CmpOpUnequal, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CmpOpUnequal87", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs89: BinaryAssociation = BinaryAssociation(
    name="lhs89",
    ends={
        Property(name="myDsl_Expr90", type=myDsl_CmpOpLess, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CmpOpLess", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs66: BinaryAssociation = BinaryAssociation(
    name="rhs66",
    ends={
        Property(name="myDsl_Expr68", type=myDsl_BoolOpAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BoolOpAnd67", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs69: BinaryAssociation = BinaryAssociation(
    name="lhs69",
    ends={
        Property(name="myDsl_Expr70", type=myDsl_BoolOpOr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BoolOpOr", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs71: BinaryAssociation = BinaryAssociation(
    name="rhs71",
    ends={
        Property(name="myDsl_Expr73", type=myDsl_BoolOpOr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BoolOpOr72", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs74: BinaryAssociation = BinaryAssociation(
    name="lhs74",
    ends={
        Property(name="myDsl_Expr75", type=myDsl_Seq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Seq", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs91: BinaryAssociation = BinaryAssociation(
    name="rhs91",
    ends={
        Property(name="myDsl_Expr93", type=myDsl_CmpOpLess, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CmpOpLess92", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value94: BinaryAssociation = BinaryAssociation(
    name="value94",
    ends={
        Property(name="myDsl_Expr96", type=myDsl_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Field95", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Def_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Def)
gen_myDsl_App_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_App)
gen_myDsl_App_Expr = Generalization(general=Expr, specific=myDsl_App)
gen_myDsl_Skip_Expr = Generalization(general=Expr, specific=myDsl_Skip)
gen_myDsl_Project_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Project)
gen_myDsl_Project_Expr = Generalization(general=Expr, specific=myDsl_Project)
gen_myDsl_BObject_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_BObject)
gen_myDsl_BObject_Expr = Generalization(general=Expr, specific=myDsl_BObject)
gen_myDsl_Copy_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Copy)
gen_myDsl_Copy_Expr = Generalization(general=Expr, specific=myDsl_Copy)
gen_myDsl_With_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_With)
gen_myDsl_With_Expr = Generalization(general=Expr, specific=myDsl_With)
gen_myDsl_Not_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Not)
gen_myDsl_Not_Expr = Generalization(general=Expr, specific=myDsl_Not)
gen_myDsl_If_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_If)
gen_myDsl_If_Expr = Generalization(general=Expr, specific=myDsl_If)
gen_myDsl_Var_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Var)
gen_myDsl_Var_Expr = Generalization(general=Expr, specific=myDsl_Var)
gen_myDsl_This_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_This)
gen_myDsl_This_Expr = Generalization(general=Expr, specific=myDsl_This)
gen_myDsl_Bool_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Bool)
gen_myDsl_Bool_Expr = Generalization(general=Expr, specific=myDsl_Bool)
gen_myDsl_Int_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Int)
gen_myDsl_Int_Expr = Generalization(general=Expr, specific=myDsl_Int)
gen_myDsl_Skip_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Skip)
gen_myDsl_Fun_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Fun)
gen_myDsl_Fun_Expr = Generalization(general=Expr, specific=myDsl_Fun)
gen_myDsl_Assign_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Assign)
gen_myDsl_Assign_Expr = Generalization(general=Expr, specific=myDsl_Assign)
gen_myDsl_ArithOpPlus_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_ArithOpPlus)
gen_myDsl_ArithOpPlus_Expr = Generalization(general=Expr, specific=myDsl_ArithOpPlus)
gen_myDsl_Let_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Let)
gen_myDsl_Let_Expr = Generalization(general=Expr, specific=myDsl_Let)
gen_myDsl_ArithOpTimes_Expr = Generalization(general=Expr, specific=myDsl_ArithOpTimes)
gen_myDsl_ArithOpDivide_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_ArithOpDivide)
gen_myDsl_ArithOpDivide_Expr = Generalization(general=Expr, specific=myDsl_ArithOpDivide)
gen_myDsl_ArithOpRemainder_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_ArithOpRemainder)
gen_myDsl_ArithOpRemainder_Expr = Generalization(general=Expr, specific=myDsl_ArithOpRemainder)
gen_myDsl_BoolOpAnd_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_BoolOpAnd)
gen_myDsl_BoolOpAnd_Expr = Generalization(general=Expr, specific=myDsl_BoolOpAnd)
gen_myDsl_ArithOpMinus_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_ArithOpMinus)
gen_myDsl_ArithOpMinus_Expr = Generalization(general=Expr, specific=myDsl_ArithOpMinus)
gen_myDsl_ArithOpTimes_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_ArithOpTimes)
gen_myDsl_CmpOpEqual_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_CmpOpEqual)
gen_myDsl_CmpOpEqual_Expr = Generalization(general=Expr, specific=myDsl_CmpOpEqual)
gen_myDsl_CmpOpUnequal_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_CmpOpUnequal)
gen_myDsl_CmpOpUnequal_Expr = Generalization(general=Expr, specific=myDsl_CmpOpUnequal)
gen_myDsl_CmpOpLess_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_CmpOpLess)
gen_myDsl_CmpOpLess_Expr = Generalization(general=Expr, specific=myDsl_CmpOpLess)
gen_myDsl_BoolOpOr_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_BoolOpOr)
gen_myDsl_BoolOpOr_Expr = Generalization(general=Expr, specific=myDsl_BoolOpOr)
gen_myDsl_Seq_TopLevelCmd = Generalization(general=TopLevelCmd, specific=myDsl_Seq)
gen_myDsl_Seq_Expr = Generalization(general=Expr, specific=myDsl_Seq)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_File, myDsl_TopLevelCmd, myDsl_Expr, myDsl_Def, TopLevelCmd, myDsl_App, Expr, myDsl_Project, myDsl_BObject, myDsl_Field, myDsl_Copy, myDsl_With, myDsl_Not, myDsl_If, myDsl_Var, myDsl_This, myDsl_Bool, myDsl_Int, myDsl_Skip, myDsl_Fun, myDsl_Assign, myDsl_ArithOpPlus, myDsl_Let, myDsl_ArithOpDivide, myDsl_ArithOpRemainder, myDsl_BoolOpAnd, myDsl_ArithOpMinus, myDsl_ArithOpTimes, myDsl_CmpOpEqual, myDsl_CmpOpUnequal, myDsl_CmpOpLess, myDsl_BoolOpOr, myDsl_Seq},
    associations={commands0, expr1, exp7, fields9, copy10, lhs12, rhs14, value17, lhs2, rhs4, body32, lhs34, rhs36, lhs39, cond19, thn21, els24, lhs27, rhs29, lhs49, rhs51, lhs54, rhs56, lhs59, rhs61, lhs64, rhs41, lhs44, rhs46, rhs76, lhs79, rhs81, lhs84, rhs86, lhs89, rhs66, lhs69, rhs71, lhs74, rhs91, value94},
    generalizations={gen_myDsl_Def_TopLevelCmd, gen_myDsl_App_TopLevelCmd, gen_myDsl_App_Expr, gen_myDsl_Skip_Expr, gen_myDsl_Project_TopLevelCmd, gen_myDsl_Project_Expr, gen_myDsl_BObject_TopLevelCmd, gen_myDsl_BObject_Expr, gen_myDsl_Copy_TopLevelCmd, gen_myDsl_Copy_Expr, gen_myDsl_With_TopLevelCmd, gen_myDsl_With_Expr, gen_myDsl_Not_TopLevelCmd, gen_myDsl_Not_Expr, gen_myDsl_If_TopLevelCmd, gen_myDsl_If_Expr, gen_myDsl_Var_TopLevelCmd, gen_myDsl_Var_Expr, gen_myDsl_This_TopLevelCmd, gen_myDsl_This_Expr, gen_myDsl_Bool_TopLevelCmd, gen_myDsl_Bool_Expr, gen_myDsl_Int_TopLevelCmd, gen_myDsl_Int_Expr, gen_myDsl_Skip_TopLevelCmd, gen_myDsl_Fun_TopLevelCmd, gen_myDsl_Fun_Expr, gen_myDsl_Assign_TopLevelCmd, gen_myDsl_Assign_Expr, gen_myDsl_ArithOpPlus_TopLevelCmd, gen_myDsl_ArithOpPlus_Expr, gen_myDsl_Let_TopLevelCmd, gen_myDsl_Let_Expr, gen_myDsl_ArithOpTimes_Expr, gen_myDsl_ArithOpDivide_TopLevelCmd, gen_myDsl_ArithOpDivide_Expr, gen_myDsl_ArithOpRemainder_TopLevelCmd, gen_myDsl_ArithOpRemainder_Expr, gen_myDsl_BoolOpAnd_TopLevelCmd, gen_myDsl_BoolOpAnd_Expr, gen_myDsl_ArithOpMinus_TopLevelCmd, gen_myDsl_ArithOpMinus_Expr, gen_myDsl_ArithOpTimes_TopLevelCmd, gen_myDsl_CmpOpEqual_TopLevelCmd, gen_myDsl_CmpOpEqual_Expr, gen_myDsl_CmpOpUnequal_TopLevelCmd, gen_myDsl_CmpOpUnequal_Expr, gen_myDsl_CmpOpLess_TopLevelCmd, gen_myDsl_CmpOpLess_Expr, gen_myDsl_BoolOpOr_TopLevelCmd, gen_myDsl_BoolOpOr_Expr, gen_myDsl_Seq_TopLevelCmd, gen_myDsl_Seq_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)