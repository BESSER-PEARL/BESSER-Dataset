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
boa_File = Class(name="boa::File")
boa_TopLevelCmd = Class(name="boa::TopLevelCmd", is_abstract=True)
boa_Expr = Class(name="boa::Expr", is_abstract=True)
TopLevelCmd = Class(name="TopLevelCmd")
boa_Def = Class(name="boa::Def")
boa_Copy = Class(name="boa::Copy")
boa_With = Class(name="boa::With")
boa_App = Class(name="boa::App")
Expr = Class(name="Expr")
boa_Var = Class(name="boa::Var")
boa_This = Class(name="boa::This")
boa_Bool = Class(name="boa::Bool")
boa_Int = Class(name="boa::Int")
boa_Skip = Class(name="boa::Skip")
boa_Project = Class(name="boa::Project")
boa_BObject = Class(name="boa::BObject")
boa_Field = Class(name="boa::Field")
boa_Let = Class(name="boa::Let")
boa_Fun = Class(name="boa::Fun")
boa_Assign = Class(name="boa::Assign")
boa_ArithOp = Class(name="boa::ArithOp", is_abstract=True)
boa_Not = Class(name="boa::Not")
boa_CmpOp = Class(name="boa::CmpOp", is_abstract=True)
boa_BoolOp = Class(name="boa::BoolOp", is_abstract=True)
boa_If = Class(name="boa::If")
boa_Seq = Class(name="boa::Seq")
boa_CmpOpEqual = Class(name="boa::CmpOpEqual")
CmpOp = Class(name="CmpOp")
boa_CmpOpUnequal = Class(name="boa::CmpOpUnequal")
boa_CmpOpLess = Class(name="boa::CmpOpLess")
boa_Ctx = Class(name="boa::Ctx")
boa_StringToEvalResMap = Class(name="boa::StringToEvalResMap")
boa_ArithOpPlus = Class(name="boa::ArithOpPlus")
ArithOp = Class(name="ArithOp")
boa_ArithOpMinus = Class(name="boa::ArithOpMinus")
boa_ArithOpTimes = Class(name="boa::ArithOpTimes")
boa_ArithOpDivide = Class(name="boa::ArithOpDivide")
boa_ArithOpRemainder = Class(name="boa::ArithOpRemainder")
boa_BoolOpAnd = Class(name="boa::BoolOpAnd")
BoolOp = Class(name="BoolOp")
boa_BoolOpOr = Class(name="boa::BoolOpOr")
boa_EvalBoolRes = Class(name="boa::EvalBoolRes")
boa_EvalRes = Class(name="boa::EvalRes", is_abstract=True)
boa_EvalMapRes = Class(name="boa::EvalMapRes")
EvalRes = Class(name="EvalRes")
boa_EvalFunRes = Class(name="boa::EvalFunRes")
boa_EvalBoundFunRes = Class(name="boa::EvalBoundFunRes")
EvalFunRes = Class(name="EvalFunRes")
boa_EvalIntRes = Class(name="boa::EvalIntRes")

# boa_File class attributes and methods

# boa_TopLevelCmd class attributes and methods

# boa_Expr class attributes and methods

# TopLevelCmd class attributes and methods

# boa_Def class attributes and methods
boa_Def_name: Property = Property(name="name", type=StringType)
boa_Def.attributes={boa_Def_name}

# boa_Copy class attributes and methods

# boa_With class attributes and methods

# boa_App class attributes and methods

# Expr class attributes and methods

# boa_Var class attributes and methods
boa_Var_name: Property = Property(name="name", type=StringType)
boa_Var.attributes={boa_Var_name}

# boa_This class attributes and methods

# boa_Bool class attributes and methods
boa_Bool_value: Property = Property(name="value", type=BooleanType)
boa_Bool.attributes={boa_Bool_value}

# boa_Int class attributes and methods
boa_Int_value: Property = Property(name="value", type=IntegerType)
boa_Int.attributes={boa_Int_value}

# boa_Skip class attributes and methods

# boa_Project class attributes and methods
boa_Project_name: Property = Property(name="name", type=StringType)
boa_Project.attributes={boa_Project_name}

# boa_BObject class attributes and methods

# boa_Field class attributes and methods
boa_Field_name: Property = Property(name="name", type=StringType)
boa_Field.attributes={boa_Field_name}

# boa_Let class attributes and methods
boa_Let_name: Property = Property(name="name", type=StringType)
boa_Let.attributes={boa_Let_name}

# boa_Fun class attributes and methods
boa_Fun_name: Property = Property(name="name", type=StringType)
boa_Fun.attributes={boa_Fun_name}

# boa_Assign class attributes and methods
boa_Assign_name: Property = Property(name="name", type=StringType)
boa_Assign.attributes={boa_Assign_name}

# boa_ArithOp class attributes and methods

# boa_Not class attributes and methods

# boa_CmpOp class attributes and methods

# boa_BoolOp class attributes and methods

# boa_If class attributes and methods

# boa_Seq class attributes and methods

# boa_CmpOpEqual class attributes and methods

# CmpOp class attributes and methods

# boa_CmpOpUnequal class attributes and methods

# boa_CmpOpLess class attributes and methods

# boa_Ctx class attributes and methods

# boa_StringToEvalResMap class attributes and methods
boa_StringToEvalResMap_key: Property = Property(name="key", type=StringType)
boa_StringToEvalResMap.attributes={boa_StringToEvalResMap_key}

# boa_ArithOpPlus class attributes and methods

# ArithOp class attributes and methods

# boa_ArithOpMinus class attributes and methods

# boa_ArithOpTimes class attributes and methods

# boa_ArithOpDivide class attributes and methods

# boa_ArithOpRemainder class attributes and methods

# boa_BoolOpAnd class attributes and methods

# BoolOp class attributes and methods

# boa_BoolOpOr class attributes and methods

# boa_EvalBoolRes class attributes and methods
boa_EvalBoolRes_value: Property = Property(name="value", type=BooleanType)
boa_EvalBoolRes.attributes={boa_EvalBoolRes_value}

# boa_EvalRes class attributes and methods

# boa_EvalMapRes class attributes and methods

# EvalRes class attributes and methods

# boa_EvalFunRes class attributes and methods
boa_EvalFunRes_name: Property = Property(name="name", type=StringType)
boa_EvalFunRes.attributes={boa_EvalFunRes_name}

# boa_EvalBoundFunRes class attributes and methods

# EvalFunRes class attributes and methods

# boa_EvalIntRes class attributes and methods
boa_EvalIntRes_value: Property = Property(name="value", type=IntegerType)
boa_EvalIntRes.attributes={boa_EvalIntRes_value}

# Relationships
commands0: BinaryAssociation = BinaryAssociation(
    name="commands0",
    ends={
        Property(name="boa_TopLevelCmd", type=boa_File, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_File", type=boa_TopLevelCmd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="boa_Expr12", type=boa_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Field11", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copy13: BinaryAssociation = BinaryAssociation(
    name="copy13",
    ends={
        Property(name="boa_Expr14", type=boa_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Copy", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs15: BinaryAssociation = BinaryAssociation(
    name="lhs15",
    ends={
        Property(name="boa_Expr16", type=boa_With, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_With", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs17: BinaryAssociation = BinaryAssociation(
    name="rhs17",
    ends={
        Property(name="boa_Expr19", type=boa_With, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_With18", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr1: BinaryAssociation = BinaryAssociation(
    name="expr1",
    ends={
        Property(name="boa_Expr", type=boa_Def, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Def", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs2: BinaryAssociation = BinaryAssociation(
    name="lhs2",
    ends={
        Property(name="boa_Expr3", type=boa_App, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_App", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs4: BinaryAssociation = BinaryAssociation(
    name="rhs4",
    ends={
        Property(name="boa_Expr6", type=boa_App, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_App5", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp7: BinaryAssociation = BinaryAssociation(
    name="exp7",
    ends={
        Property(name="boa_Expr8", type=boa_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Project", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fields9: BinaryAssociation = BinaryAssociation(
    name="fields9",
    ends={
        Property(name="boa_Field", type=boa_BObject, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_BObject", type=boa_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs40: BinaryAssociation = BinaryAssociation(
    name="lhs40",
    ends={
        Property(name="boa_Expr41", type=boa_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Let", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs42: BinaryAssociation = BinaryAssociation(
    name="rhs42",
    ends={
        Property(name="boa_Expr44", type=boa_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Let43", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body45: BinaryAssociation = BinaryAssociation(
    name="body45",
    ends={
        Property(name="boa_Expr46", type=boa_Fun, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Fun", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs20: BinaryAssociation = BinaryAssociation(
    name="lhs20",
    ends={
        Property(name="boa_Expr21", type=boa_ArithOp, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_ArithOp", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs22: BinaryAssociation = BinaryAssociation(
    name="rhs22",
    ends={
        Property(name="boa_Expr24", type=boa_ArithOp, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_ArithOp23", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="boa_Expr26", type=boa_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Not", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs27: BinaryAssociation = BinaryAssociation(
    name="lhs27",
    ends={
        Property(name="boa_Expr28", type=boa_CmpOp, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_CmpOp", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs29: BinaryAssociation = BinaryAssociation(
    name="rhs29",
    ends={
        Property(name="boa_Expr31", type=boa_CmpOp, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_CmpOp30", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cond32: BinaryAssociation = BinaryAssociation(
    name="cond32",
    ends={
        Property(name="boa_Expr33", type=boa_If, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_If", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thn34: BinaryAssociation = BinaryAssociation(
    name="thn34",
    ends={
        Property(name="boa_Expr36", type=boa_If, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_If35", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
els37: BinaryAssociation = BinaryAssociation(
    name="els37",
    ends={
        Property(name="boa_Expr39", type=boa_If, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_If38", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs62: BinaryAssociation = BinaryAssociation(
    name="lhs62",
    ends={
        Property(name="boa_Expr63", type=boa_Seq, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Seq", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs64: BinaryAssociation = BinaryAssociation(
    name="rhs64",
    ends={
        Property(name="boa_Expr66", type=boa_Seq, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Seq65", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
env67: BinaryAssociation = BinaryAssociation(
    name="env67",
    ends={
        Property(name="boa_StringToEvalResMap", type=boa_Ctx, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Ctx", type=boa_StringToEvalResMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs47: BinaryAssociation = BinaryAssociation(
    name="lhs47",
    ends={
        Property(name="boa_Expr48", type=boa_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Assign", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs49: BinaryAssociation = BinaryAssociation(
    name="rhs49",
    ends={
        Property(name="boa_Expr51", type=boa_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Assign50", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs52: BinaryAssociation = BinaryAssociation(
    name="lhs52",
    ends={
        Property(name="boa_Expr53", type=boa_BoolOpAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_BoolOpAnd", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs54: BinaryAssociation = BinaryAssociation(
    name="rhs54",
    ends={
        Property(name="boa_Expr56", type=boa_BoolOpAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_BoolOpAnd55", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs57: BinaryAssociation = BinaryAssociation(
    name="lhs57",
    ends={
        Property(name="boa_Expr58", type=boa_BoolOpOr, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_BoolOpOr", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs59: BinaryAssociation = BinaryAssociation(
    name="rhs59",
    ends={
        Property(name="boa_Expr61", type=boa_BoolOpOr, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_BoolOpOr60", type=boa_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
th68: BinaryAssociation = BinaryAssociation(
    name="th68",
    ends={
        Property(name="boa_StringToEvalResMap70", type=boa_Ctx, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_Ctx69", type=boa_StringToEvalResMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="boa_EvalRes", type=boa_StringToEvalResMap, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_StringToEvalResMap72", type=boa_EvalRes, multiplicity=Multiplicity(1, 1))
    }
)
values73: BinaryAssociation = BinaryAssociation(
    name="values73",
    ends={
        Property(name="boa_StringToEvalResMap74", type=boa_EvalMapRes, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_EvalMapRes", type=boa_StringToEvalResMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp75: BinaryAssociation = BinaryAssociation(
    name="exp75",
    ends={
        Property(name="boa_Expr76", type=boa_EvalFunRes, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_EvalFunRes", type=boa_Expr, multiplicity=Multiplicity(1, 1))
    }
)
ctx77: BinaryAssociation = BinaryAssociation(
    name="ctx77",
    ends={
        Property(name="boa_Ctx79", type=boa_EvalFunRes, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_EvalFunRes78", type=boa_Ctx, multiplicity=Multiplicity(1, 1))
    }
)
th80: BinaryAssociation = BinaryAssociation(
    name="th80",
    ends={
        Property(name="boa_StringToEvalResMap81", type=boa_EvalBoundFunRes, multiplicity=Multiplicity(1, 1)),
        Property(name="boa_EvalBoundFunRes", type=boa_StringToEvalResMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_boa_Expr_TopLevelCmd = Generalization(general=TopLevelCmd, specific=boa_Expr)
gen_boa_Def_TopLevelCmd = Generalization(general=TopLevelCmd, specific=boa_Def)
gen_boa_Copy_Expr = Generalization(general=Expr, specific=boa_Copy)
gen_boa_With_Expr = Generalization(general=Expr, specific=boa_With)
gen_boa_App_Expr = Generalization(general=Expr, specific=boa_App)
gen_boa_Var_Expr = Generalization(general=Expr, specific=boa_Var)
gen_boa_This_Expr = Generalization(general=Expr, specific=boa_This)
gen_boa_Bool_Expr = Generalization(general=Expr, specific=boa_Bool)
gen_boa_Int_Expr = Generalization(general=Expr, specific=boa_Int)
gen_boa_Skip_Expr = Generalization(general=Expr, specific=boa_Skip)
gen_boa_Project_Expr = Generalization(general=Expr, specific=boa_Project)
gen_boa_BObject_Expr = Generalization(general=Expr, specific=boa_BObject)
gen_boa_Let_Expr = Generalization(general=Expr, specific=boa_Let)
gen_boa_Fun_Expr = Generalization(general=Expr, specific=boa_Fun)
gen_boa_Assign_Expr = Generalization(general=Expr, specific=boa_Assign)
gen_boa_ArithOp_Expr = Generalization(general=Expr, specific=boa_ArithOp)
gen_boa_Not_Expr = Generalization(general=Expr, specific=boa_Not)
gen_boa_CmpOp_Expr = Generalization(general=Expr, specific=boa_CmpOp)
gen_boa_BoolOp_Expr = Generalization(general=Expr, specific=boa_BoolOp)
gen_boa_If_Expr = Generalization(general=Expr, specific=boa_If)
gen_boa_Seq_Expr = Generalization(general=Expr, specific=boa_Seq)
gen_boa_CmpOpEqual_CmpOp = Generalization(general=CmpOp, specific=boa_CmpOpEqual)
gen_boa_CmpOpUnequal_CmpOp = Generalization(general=CmpOp, specific=boa_CmpOpUnequal)
gen_boa_CmpOpLess_CmpOp = Generalization(general=CmpOp, specific=boa_CmpOpLess)
gen_boa_ArithOpPlus_ArithOp = Generalization(general=ArithOp, specific=boa_ArithOpPlus)
gen_boa_ArithOpMinus_ArithOp = Generalization(general=ArithOp, specific=boa_ArithOpMinus)
gen_boa_ArithOpTimes_ArithOp = Generalization(general=ArithOp, specific=boa_ArithOpTimes)
gen_boa_ArithOpDivide_ArithOp = Generalization(general=ArithOp, specific=boa_ArithOpDivide)
gen_boa_ArithOpRemainder_ArithOp = Generalization(general=ArithOp, specific=boa_ArithOpRemainder)
gen_boa_BoolOpAnd_BoolOp = Generalization(general=BoolOp, specific=boa_BoolOpAnd)
gen_boa_BoolOpOr_BoolOp = Generalization(general=BoolOp, specific=boa_BoolOpOr)
gen_boa_EvalBoolRes_EvalRes = Generalization(general=EvalRes, specific=boa_EvalBoolRes)
gen_boa_EvalMapRes_EvalRes = Generalization(general=EvalRes, specific=boa_EvalMapRes)
gen_boa_EvalFunRes_EvalRes = Generalization(general=EvalRes, specific=boa_EvalFunRes)
gen_boa_EvalBoundFunRes_EvalFunRes = Generalization(general=EvalFunRes, specific=boa_EvalBoundFunRes)
gen_boa_EvalIntRes_EvalRes = Generalization(general=EvalRes, specific=boa_EvalIntRes)

# Domain Model
domain_model = DomainModel(
    name="boa",
    types={boa_File, boa_TopLevelCmd, boa_Expr, TopLevelCmd, boa_Def, boa_Copy, boa_With, boa_App, Expr, boa_Var, boa_This, boa_Bool, boa_Int, boa_Skip, boa_Project, boa_BObject, boa_Field, boa_Let, boa_Fun, boa_Assign, boa_ArithOp, boa_Not, boa_CmpOp, boa_BoolOp, boa_If, boa_Seq, boa_CmpOpEqual, CmpOp, boa_CmpOpUnequal, boa_CmpOpLess, boa_Ctx, boa_StringToEvalResMap, boa_ArithOpPlus, ArithOp, boa_ArithOpMinus, boa_ArithOpTimes, boa_ArithOpDivide, boa_ArithOpRemainder, boa_BoolOpAnd, BoolOp, boa_BoolOpOr, boa_EvalBoolRes, boa_EvalRes, boa_EvalMapRes, EvalRes, boa_EvalFunRes, boa_EvalBoundFunRes, EvalFunRes, boa_EvalIntRes},
    associations={commands0, value10, copy13, lhs15, rhs17, expr1, lhs2, rhs4, exp7, fields9, lhs40, rhs42, body45, lhs20, rhs22, value25, lhs27, rhs29, cond32, thn34, els37, lhs62, rhs64, env67, lhs47, rhs49, lhs52, rhs54, lhs57, rhs59, th68, value71, values73, exp75, ctx77, th80},
    generalizations={gen_boa_Expr_TopLevelCmd, gen_boa_Def_TopLevelCmd, gen_boa_Copy_Expr, gen_boa_With_Expr, gen_boa_App_Expr, gen_boa_Var_Expr, gen_boa_This_Expr, gen_boa_Bool_Expr, gen_boa_Int_Expr, gen_boa_Skip_Expr, gen_boa_Project_Expr, gen_boa_BObject_Expr, gen_boa_Let_Expr, gen_boa_Fun_Expr, gen_boa_Assign_Expr, gen_boa_ArithOp_Expr, gen_boa_Not_Expr, gen_boa_CmpOp_Expr, gen_boa_BoolOp_Expr, gen_boa_If_Expr, gen_boa_Seq_Expr, gen_boa_CmpOpEqual_CmpOp, gen_boa_CmpOpUnequal_CmpOp, gen_boa_CmpOpLess_CmpOp, gen_boa_ArithOpPlus_ArithOp, gen_boa_ArithOpMinus_ArithOp, gen_boa_ArithOpTimes_ArithOp, gen_boa_ArithOpDivide_ArithOp, gen_boa_ArithOpRemainder_ArithOp, gen_boa_BoolOpAnd_BoolOp, gen_boa_BoolOpOr_BoolOp, gen_boa_EvalBoolRes_EvalRes, gen_boa_EvalMapRes_EvalRes, gen_boa_EvalFunRes_EvalRes, gen_boa_EvalBoundFunRes_EvalFunRes, gen_boa_EvalIntRes_EvalRes},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)