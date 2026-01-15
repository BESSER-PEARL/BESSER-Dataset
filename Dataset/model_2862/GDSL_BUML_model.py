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
gDSL_Model = Class(name="gDSL::Model")
gDSL_Decl = Class(name="gDSL::Decl")
gDSL_DeclExport = Class(name="gDSL::DeclExport")
Decl = Class(name="Decl")
gDSL_Val = Class(name="gDSL::Val")
gDSL_Exp = Class(name="gDSL::Exp")
gDSL_TyVars = Class(name="gDSL::TyVars")
gDSL_Ty = Class(name="gDSL::Ty")
gDSL_Type = Class(name="gDSL::Type")
gDSL_ConDecl = Class(name="gDSL::ConDecl")
gDSL_TyElement = Class(name="gDSL::TyElement")
gDSL_CONS = Class(name="gDSL::CONS")
gDSL_TyBind = Class(name="gDSL::TyBind")
gDSL_CaseExp = Class(name="gDSL::CaseExp")
gDSL_MonadicExp = Class(name="gDSL::MonadicExp")
gDSL_OrElseExp = Class(name="gDSL::OrElseExp")
ClosedExp = Class(name="ClosedExp")
gDSL_ClosedExp = Class(name="gDSL::ClosedExp")
gDSL_PAT = Class(name="gDSL::PAT")
CaseExp = Class(name="CaseExp")
gDSL_SelectExp = Class(name="gDSL::SelectExp")
MExp = Class(name="MExp")
gDSL_ApplyExp = Class(name="gDSL::ApplyExp")
gDSL_AndAlsoExp = Class(name="gDSL::AndAlsoExp")
SelectExp = Class(name="SelectExp")
OrElseExp = Class(name="OrElseExp")
gDSL_RExp = Class(name="gDSL::RExp")
AndAlsoExp = Class(name="AndAlsoExp")
gDSL_AExp = Class(name="gDSL::AExp")
RExp = Class(name="RExp")
gDSL_MExp = Class(name="gDSL::MExp")
AExp = Class(name="AExp")
gDSL_ValueDecl = Class(name="gDSL::ValueDecl")
gDSL_AtomicExp = Class(name="gDSL::AtomicExp")
gDSL_Args = Class(name="gDSL::Args")
ApplyExp = Class(name="ApplyExp")
gDSL_Field = Class(name="gDSL::Field")

# gDSL_Model class attributes and methods

# gDSL_Decl class attributes and methods

# gDSL_DeclExport class attributes and methods

# Decl class attributes and methods

# gDSL_Val class attributes and methods
gDSL_Val_name: Property = Property(name="name", type=StringType)
gDSL_Val_attr: Property = Property(name="attr", type=StringType)
gDSL_Val_mid: Property = Property(name="mid", type=StringType)
gDSL_Val_decPat: Property = Property(name="decPat", type=StringType)
gDSL_Val.attributes={gDSL_Val_name, gDSL_Val_mid, gDSL_Val_decPat, gDSL_Val_attr}

# gDSL_Exp class attributes and methods
gDSL_Exp_mid: Property = Property(name="mid", type=StringType)
gDSL_Exp.attributes={gDSL_Exp_mid}

# gDSL_TyVars class attributes and methods

# gDSL_Ty class attributes and methods
gDSL_Ty_value: Property = Property(name="value", type=StringType)
gDSL_Ty_type: Property = Property(name="type", type=StringType)
gDSL_Ty.attributes={gDSL_Ty_type, gDSL_Ty_value}

# gDSL_Type class attributes and methods
gDSL_Type_name: Property = Property(name="name", type=StringType)
gDSL_Type.attributes={gDSL_Type_name}

# gDSL_ConDecl class attributes and methods

# gDSL_TyElement class attributes and methods
gDSL_TyElement_name: Property = Property(name="name", type=StringType)
gDSL_TyElement.attributes={gDSL_TyElement_name}

# gDSL_CONS class attributes and methods
gDSL_CONS_conName: Property = Property(name="conName", type=StringType)
gDSL_CONS.attributes={gDSL_CONS_conName}

# gDSL_TyBind class attributes and methods
gDSL_TyBind_name: Property = Property(name="name", type=StringType)
gDSL_TyBind.attributes={gDSL_TyBind_name}

# gDSL_CaseExp class attributes and methods
gDSL_CaseExp_name: Property = Property(name="name", type=StringType)
gDSL_CaseExp.attributes={gDSL_CaseExp_name}

# gDSL_MonadicExp class attributes and methods
gDSL_MonadicExp_name: Property = Property(name="name", type=StringType)
gDSL_MonadicExp.attributes={gDSL_MonadicExp_name}

# gDSL_OrElseExp class attributes and methods

# ClosedExp class attributes and methods

# gDSL_ClosedExp class attributes and methods

# gDSL_PAT class attributes and methods
gDSL_PAT_uscore: Property = Property(name="uscore", type=StringType)
gDSL_PAT_int: Property = Property(name="int", type=StringType)
gDSL_PAT_id: Property = Property(name="id", type=StringType)
gDSL_PAT_bitpat: Property = Property(name="bitpat", type=StringType)
gDSL_PAT.attributes={gDSL_PAT_uscore, gDSL_PAT_bitpat, gDSL_PAT_id, gDSL_PAT_int}

# CaseExp class attributes and methods

# gDSL_SelectExp class attributes and methods
gDSL_SelectExp_symbol: Property = Property(name="symbol", type=StringType)
gDSL_SelectExp.attributes={gDSL_SelectExp_symbol}

# MExp class attributes and methods

# gDSL_ApplyExp class attributes and methods

# gDSL_AndAlsoExp class attributes and methods

# SelectExp class attributes and methods

# OrElseExp class attributes and methods

# gDSL_RExp class attributes and methods

# AndAlsoExp class attributes and methods

# gDSL_AExp class attributes and methods
gDSL_AExp_sym: Property = Property(name="sym", type=StringType)
gDSL_AExp.attributes={gDSL_AExp_sym}

# RExp class attributes and methods

# gDSL_MExp class attributes and methods
gDSL_MExp_sign: Property = Property(name="sign", type=StringType)
gDSL_MExp.attributes={gDSL_MExp_sign}

# AExp class attributes and methods

# gDSL_ValueDecl class attributes and methods
gDSL_ValueDecl_name: Property = Property(name="name", type=StringType)
gDSL_ValueDecl_ids: Property = Property(name="ids", type=StringType)
gDSL_ValueDecl.attributes={gDSL_ValueDecl_ids, gDSL_ValueDecl_name}

# gDSL_AtomicExp class attributes and methods
gDSL_AtomicExp_id: Property = Property(name="id", type=StringType)
gDSL_AtomicExp.attributes={gDSL_AtomicExp_id}

# gDSL_Args class attributes and methods

# ApplyExp class attributes and methods

# gDSL_Field class attributes and methods
gDSL_Field_name: Property = Property(name="name", type=StringType)
gDSL_Field.attributes={gDSL_Field_name}

# Relationships
decl0: BinaryAssociation = BinaryAssociation(
    name="decl0",
    ends={
        Property(name="gDSL_Decl", type=gDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Model", type=gDSL_Decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp13: BinaryAssociation = BinaryAssociation(
    name="exp13",
    ends={
        Property(name="gDSL_Exp", type=gDSL_Val, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Val14", type=gDSL_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name1: BinaryAssociation = BinaryAssociation(
    name="name1",
    ends={
        Property(name="gDSL_Val", type=gDSL_DeclExport, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_DeclExport", type=gDSL_Val, multiplicity=Multiplicity(0, 1))
    }
)
tyVars2: BinaryAssociation = BinaryAssociation(
    name="tyVars2",
    ends={
        Property(name="gDSL_TyVars", type=gDSL_DeclExport, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_DeclExport3", type=gDSL_TyVars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="gDSL_Ty", type=gDSL_DeclExport, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_DeclExport5", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tyVars6: BinaryAssociation = BinaryAssociation(
    name="tyVars6",
    ends={
        Property(name="gDSL_TyVars7", type=gDSL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Type", type=gDSL_TyVars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conDecl8: BinaryAssociation = BinaryAssociation(
    name="conDecl8",
    ends={
        Property(name="gDSL_ConDecl", type=gDSL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Type9", type=gDSL_ConDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="gDSL_Ty12", type=gDSL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Type11", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tyBind29: BinaryAssociation = BinaryAssociation(
    name="tyBind29",
    ends={
        Property(name="gDSL_Ty30", type=gDSL_TyBind, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="gDSL_TyBind", type=gDSL_Ty, multiplicity=Multiplicity(1, 1))
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="gDSL_TyElement", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty32", type=gDSL_TyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param34: BinaryAssociation = BinaryAssociation(
    name="param34",
    ends={
        Property(name="gDSL_Ty35", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty33", type=gDSL_Ty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resType37: BinaryAssociation = BinaryAssociation(
    name="resType37",
    ends={
        Property(name="gDSL_Ty38", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty36", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps15: BinaryAssociation = BinaryAssociation(
    name="exps15",
    ends={
        Property(name="gDSL_Exp17", type=gDSL_Val, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Val16", type=gDSL_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attr18: BinaryAssociation = BinaryAssociation(
    name="attr18",
    ends={
        Property(name="gDSL_Type20", type=gDSL_TyVars, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_TyVars19", type=gDSL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name21: BinaryAssociation = BinaryAssociation(
    name="name21",
    ends={
        Property(name="gDSL_CONS", type=gDSL_ConDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ConDecl22", type=gDSL_CONS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ty23: BinaryAssociation = BinaryAssociation(
    name="ty23",
    ends={
        Property(name="gDSL_Ty25", type=gDSL_ConDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ConDecl24", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef26: BinaryAssociation = BinaryAssociation(
    name="typeRef26",
    ends={
        Property(name="gDSL_Type28", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty27", type=gDSL_Type, multiplicity=Multiplicity(0, 1))
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="gDSL_Ty53", type=gDSL_TyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_TyElement52", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name54: BinaryAssociation = BinaryAssociation(
    name="name54",
    ends={
        Property(name="gDSL_CaseExp", type=gDSL_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Exp55", type=gDSL_CaseExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseExps56: BinaryAssociation = BinaryAssociation(
    name="caseExps56",
    ends={
        Property(name="gDSL_CaseExp58", type=gDSL_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Exp57", type=gDSL_CaseExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r40: BinaryAssociation = BinaryAssociation(
    name="r40",
    ends={
        Property(name="gDSL_Ty41", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty39", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in43: BinaryAssociation = BinaryAssociation(
    name="in43",
    ends={
        Property(name="gDSL_Ty44", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty42", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out46: BinaryAssociation = BinaryAssociation(
    name="out46",
    ends={
        Property(name="gDSL_Ty47", type=gDSL_Ty, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Ty45", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value48: BinaryAssociation = BinaryAssociation(
    name="value48",
    ends={
        Property(name="gDSL_Ty50", type=gDSL_TyBind, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_TyBind49", type=gDSL_Ty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doExp75: BinaryAssociation = BinaryAssociation(
    name="doExp75",
    ends={
        Property(name="gDSL_MonadicExp", type=gDSL_ClosedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ClosedExp76", type=gDSL_MonadicExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp77: BinaryAssociation = BinaryAssociation(
    name="exp77",
    ends={
        Property(name="gDSL_Exp79", type=gDSL_MonadicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_MonadicExp78", type=gDSL_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
closedExp59: BinaryAssociation = BinaryAssociation(
    name="closedExp59",
    ends={
        Property(name="gDSL_ClosedExp", type=gDSL_CaseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_CaseExp60", type=gDSL_ClosedExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pat61: BinaryAssociation = BinaryAssociation(
    name="pat61",
    ends={
        Property(name="gDSL_PAT", type=gDSL_CaseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_CaseExp62", type=gDSL_PAT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp63: BinaryAssociation = BinaryAssociation(
    name="exp63",
    ends={
        Property(name="gDSL_Exp65", type=gDSL_CaseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_CaseExp64", type=gDSL_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifCaseExp66: BinaryAssociation = BinaryAssociation(
    name="ifCaseExp66",
    ends={
        Property(name="gDSL_CaseExp68", type=gDSL_ClosedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ClosedExp67", type=gDSL_CaseExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenCaseExp69: BinaryAssociation = BinaryAssociation(
    name="thenCaseExp69",
    ends={
        Property(name="gDSL_CaseExp71", type=gDSL_ClosedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ClosedExp70", type=gDSL_CaseExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseCaseExp72: BinaryAssociation = BinaryAssociation(
    name="elseCaseExp72",
    ends={
        Property(name="gDSL_CaseExp74", type=gDSL_ClosedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ClosedExp73", type=gDSL_CaseExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mexps87: BinaryAssociation = BinaryAssociation(
    name="mexps87",
    ends={
        Property(name="gDSL_MExp", type=gDSL_MExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_MExp86", type=gDSL_MExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applyexps88: BinaryAssociation = BinaryAssociation(
    name="applyexps88",
    ends={
        Property(name="gDSL_ApplyExp", type=gDSL_SelectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_SelectExp", type=gDSL_ApplyExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="gDSL_AndAlsoExp", type=gDSL_OrElseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_OrElseExp", type=gDSL_AndAlsoExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right81: BinaryAssociation = BinaryAssociation(
    name="right81",
    ends={
        Property(name="gDSL_AndAlsoExp83", type=gDSL_OrElseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_OrElseExp82", type=gDSL_AndAlsoExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aexps85: BinaryAssociation = BinaryAssociation(
    name="aexps85",
    ends={
        Property(name="gDSL_AExp", type=gDSL_AExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_AExp84", type=gDSL_AExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr98: BinaryAssociation = BinaryAssociation(
    name="expr98",
    ends={
        Property(name="gDSL_AtomicExp99", type=gDSL_Exp, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="gDSL_Exp100", type=gDSL_AtomicExp, multiplicity=Multiplicity(1, 1))
    }
)
exps101: BinaryAssociation = BinaryAssociation(
    name="exps101",
    ends={
        Property(name="gDSL_Exp103", type=gDSL_AtomicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_AtomicExp102", type=gDSL_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valDecl104: BinaryAssociation = BinaryAssociation(
    name="valDecl104",
    ends={
        Property(name="gDSL_ValueDecl", type=gDSL_AtomicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_AtomicExp105", type=gDSL_ValueDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atomicExp89: BinaryAssociation = BinaryAssociation(
    name="atomicExp89",
    ends={
        Property(name="gDSL_AtomicExp", type=gDSL_ApplyExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ApplyExp90", type=gDSL_AtomicExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args91: BinaryAssociation = BinaryAssociation(
    name="args91",
    ends={
        Property(name="gDSL_Args", type=gDSL_ApplyExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ApplyExp92", type=gDSL_Args, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args93: BinaryAssociation = BinaryAssociation(
    name="args93",
    ends={
        Property(name="gDSL_AtomicExp95", type=gDSL_Args, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Args94", type=gDSL_AtomicExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields96: BinaryAssociation = BinaryAssociation(
    name="fields96",
    ends={
        Property(name="gDSL_Field", type=gDSL_AtomicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_AtomicExp97", type=gDSL_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp106: BinaryAssociation = BinaryAssociation(
    name="exp106",
    ends={
        Property(name="gDSL_Exp108", type=gDSL_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_Field107", type=gDSL_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp109: BinaryAssociation = BinaryAssociation(
    name="exp109",
    ends={
        Property(name="gDSL_Exp111", type=gDSL_ValueDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_ValueDecl110", type=gDSL_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pat113: BinaryAssociation = BinaryAssociation(
    name="pat113",
    ends={
        Property(name="gDSL_PAT114", type=gDSL_PAT, multiplicity=Multiplicity(1, 1)),
        Property(name="gDSL_PAT112", type=gDSL_PAT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_gDSL_DeclExport_Decl = Generalization(general=Decl, specific=gDSL_DeclExport)
gen_gDSL_Val_Decl = Generalization(general=Decl, specific=gDSL_Val)
gen_gDSL_Type_Decl = Generalization(general=Decl, specific=gDSL_Type)
gen_gDSL_OrElseExp_ClosedExp = Generalization(general=ClosedExp, specific=gDSL_OrElseExp)
gen_gDSL_ClosedExp_CaseExp = Generalization(general=CaseExp, specific=gDSL_ClosedExp)
gen_gDSL_SelectExp_MExp = Generalization(general=MExp, specific=gDSL_SelectExp)
gen_gDSL_ApplyExp_SelectExp = Generalization(general=SelectExp, specific=gDSL_ApplyExp)
gen_gDSL_AndAlsoExp_OrElseExp = Generalization(general=OrElseExp, specific=gDSL_AndAlsoExp)
gen_gDSL_RExp_AndAlsoExp = Generalization(general=AndAlsoExp, specific=gDSL_RExp)
gen_gDSL_AExp_RExp = Generalization(general=RExp, specific=gDSL_AExp)
gen_gDSL_MExp_AExp = Generalization(general=AExp, specific=gDSL_MExp)
gen_gDSL_AtomicExp_ApplyExp = Generalization(general=ApplyExp, specific=gDSL_AtomicExp)

# Domain Model
domain_model = DomainModel(
    name="gDSL",
    types={gDSL_Model, gDSL_Decl, gDSL_DeclExport, Decl, gDSL_Val, gDSL_Exp, gDSL_TyVars, gDSL_Ty, gDSL_Type, gDSL_ConDecl, gDSL_TyElement, gDSL_CONS, gDSL_TyBind, gDSL_CaseExp, gDSL_MonadicExp, gDSL_OrElseExp, ClosedExp, gDSL_ClosedExp, gDSL_PAT, CaseExp, gDSL_SelectExp, MExp, gDSL_ApplyExp, gDSL_AndAlsoExp, SelectExp, OrElseExp, gDSL_RExp, AndAlsoExp, gDSL_AExp, RExp, gDSL_MExp, AExp, gDSL_ValueDecl, gDSL_AtomicExp, gDSL_Args, ApplyExp, gDSL_Field},
    associations={decl0, exp13, name1, tyVars2, type4, tyVars6, conDecl8, value10, tyBind29, elements31, param34, resType37, exps15, attr18, name21, ty23, typeRef26, value51, name54, caseExps56, r40, in43, out46, value48, doExp75, exp77, closedExp59, pat61, exp63, ifCaseExp66, thenCaseExp69, elseCaseExp72, mexps87, applyexps88, left80, right81, aexps85, expr98, exps101, valDecl104, atomicExp89, args91, args93, fields96, exp106, exp109, pat113},
    generalizations={gen_gDSL_DeclExport_Decl, gen_gDSL_Val_Decl, gen_gDSL_Type_Decl, gen_gDSL_OrElseExp_ClosedExp, gen_gDSL_ClosedExp_CaseExp, gen_gDSL_SelectExp_MExp, gen_gDSL_ApplyExp_SelectExp, gen_gDSL_AndAlsoExp_OrElseExp, gen_gDSL_RExp_AndAlsoExp, gen_gDSL_AExp_RExp, gen_gDSL_MExp_AExp, gen_gDSL_AtomicExp_ApplyExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)