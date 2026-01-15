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
myDsl_Output = Class(name="myDsl::Output")
myDsl_Model = Class(name="myDsl::Model")
myDsl_Programme = Class(name="myDsl::Programme")
myDsl_Fonction = Class(name="myDsl::Fonction")
myDsl_Input = Class(name="myDsl::Input")
myDsl_Commandes = Class(name="myDsl::Commandes")
myDsl_Commande = Class(name="myDsl::Commande")
myDsl_AffectVar = Class(name="myDsl::AffectVar")
myDsl_While = Class(name="myDsl::While")
myDsl_For = Class(name="myDsl::For")
myDsl_If = Class(name="myDsl::If")
myDsl_Foreach = Class(name="myDsl::Foreach")
myDsl_Vars = Class(name="myDsl::Vars")
myDsl_Exprs = Class(name="myDsl::Exprs")
myDsl_Expr = Class(name="myDsl::Expr")
myDsl_LExpr = Class(name="myDsl::LExpr")
myDsl_ExprAnd = Class(name="myDsl::ExprAnd")
myDsl_ExprSimple = Class(name="myDsl::ExprSimple")
myDsl_Cons = Class(name="myDsl::Cons")
myDsl_Liste = Class(name="myDsl::Liste")
myDsl_Hd = Class(name="myDsl::Hd")
myDsl_Tl = Class(name="myDsl::Tl")
myDsl_SymboleEx = Class(name="myDsl::SymboleEx")
myDsl_ExprOr = Class(name="myDsl::ExprOr")
myDsl_ExprNot = Class(name="myDsl::ExprNot")
myDsl_ExprNotNot = Class(name="myDsl::ExprNotNot")
myDsl_ExprNotDo = Class(name="myDsl::ExprNotDo")
myDsl_ExprEq = Class(name="myDsl::ExprEq")

# myDsl_Output class attributes and methods
myDsl_Output_var1: Property = Property(name="var1", type=StringType)
myDsl_Output_var2: Property = Property(name="var2", type=StringType)
myDsl_Output.attributes={myDsl_Output_var1, myDsl_Output_var2}

# myDsl_Model class attributes and methods

# myDsl_Programme class attributes and methods

# myDsl_Fonction class attributes and methods
myDsl_Fonction_symbole: Property = Property(name="symbole", type=StringType)
myDsl_Fonction.attributes={myDsl_Fonction_symbole}

# myDsl_Input class attributes and methods
myDsl_Input_var1: Property = Property(name="var1", type=StringType)
myDsl_Input_var2: Property = Property(name="var2", type=StringType)
myDsl_Input.attributes={myDsl_Input_var1, myDsl_Input_var2}

# myDsl_Commandes class attributes and methods

# myDsl_Commande class attributes and methods
myDsl_Commande_nop: Property = Property(name="nop", type=StringType)
myDsl_Commande.attributes={myDsl_Commande_nop}

# myDsl_AffectVar class attributes and methods

# myDsl_While class attributes and methods

# myDsl_For class attributes and methods

# myDsl_If class attributes and methods

# myDsl_Foreach class attributes and methods

# myDsl_Vars class attributes and methods
myDsl_Vars_var2: Property = Property(name="var2", type=StringType)
myDsl_Vars_var3: Property = Property(name="var3", type=StringType)
myDsl_Vars.attributes={myDsl_Vars_var2, myDsl_Vars_var3}

# myDsl_Exprs class attributes and methods

# myDsl_Expr class attributes and methods

# myDsl_LExpr class attributes and methods

# myDsl_ExprAnd class attributes and methods

# myDsl_ExprSimple class attributes and methods
myDsl_ExprSimple_vide: Property = Property(name="vide", type=StringType)
myDsl_ExprSimple_variable: Property = Property(name="variable", type=StringType)
myDsl_ExprSimple_symbole: Property = Property(name="symbole", type=StringType)
myDsl_ExprSimple.attributes={myDsl_ExprSimple_variable, myDsl_ExprSimple_vide, myDsl_ExprSimple_symbole}

# myDsl_Cons class attributes and methods

# myDsl_Liste class attributes and methods

# myDsl_Hd class attributes and methods

# myDsl_Tl class attributes and methods

# myDsl_SymboleEx class attributes and methods
myDsl_SymboleEx_p: Property = Property(name="p", type=StringType)
myDsl_SymboleEx.attributes={myDsl_SymboleEx_p}

# myDsl_ExprOr class attributes and methods

# myDsl_ExprNot class attributes and methods

# myDsl_ExprNotNot class attributes and methods

# myDsl_ExprNotDo class attributes and methods

# myDsl_ExprEq class attributes and methods

# Relationships
out7: BinaryAssociation = BinaryAssociation(
    name="out7",
    ends={
        Property(name="myDsl_Output", type=myDsl_Fonction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fonction8", type=myDsl_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
programme0: BinaryAssociation = BinaryAssociation(
    name="programme0",
    ends={
        Property(name="myDsl_Programme", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Programme, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fonct1: BinaryAssociation = BinaryAssociation(
    name="fonct1",
    ends={
        Property(name="myDsl_Fonction", type=myDsl_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Programme2", type=myDsl_Fonction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in3: BinaryAssociation = BinaryAssociation(
    name="in3",
    ends={
        Property(name="myDsl_Input", type=myDsl_Fonction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fonction4", type=myDsl_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com5: BinaryAssociation = BinaryAssociation(
    name="com5",
    ends={
        Property(name="myDsl_Commandes", type=myDsl_Fonction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fonction6", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp439: BinaryAssociation = BinaryAssociation(
    name="exp439",
    ends={
        Property(name="myDsl_Expr41", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If40", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com542: BinaryAssociation = BinaryAssociation(
    name="com542",
    ends={
        Property(name="myDsl_Commandes44", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If43", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com645: BinaryAssociation = BinaryAssociation(
    name="com645",
    ends={
        Property(name="myDsl_Commandes47", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If46", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com19: BinaryAssociation = BinaryAssociation(
    name="com19",
    ends={
        Property(name="myDsl_Commande", type=myDsl_Commandes, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commandes10", type=myDsl_Commande, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com211: BinaryAssociation = BinaryAssociation(
    name="com211",
    ends={
        Property(name="myDsl_Commande13", type=myDsl_Commandes, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commandes12", type=myDsl_Commande, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
affectVar14: BinaryAssociation = BinaryAssociation(
    name="affectVar14",
    ends={
        Property(name="myDsl_AffectVar", type=myDsl_Commande, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commande15", type=myDsl_AffectVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileC16: BinaryAssociation = BinaryAssociation(
    name="whileC16",
    ends={
        Property(name="myDsl_While", type=myDsl_Commande, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commande17", type=myDsl_While, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forC18: BinaryAssociation = BinaryAssociation(
    name="forC18",
    ends={
        Property(name="myDsl_For", type=myDsl_Commande, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commande19", type=myDsl_For, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifC20: BinaryAssociation = BinaryAssociation(
    name="ifC20",
    ends={
        Property(name="myDsl_If", type=myDsl_Commande, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commande21", type=myDsl_If, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreachC22: BinaryAssociation = BinaryAssociation(
    name="foreachC22",
    ends={
        Property(name="myDsl_Foreach", type=myDsl_Commande, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commande23", type=myDsl_Foreach, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var124: BinaryAssociation = BinaryAssociation(
    name="var124",
    ends={
        Property(name="myDsl_Vars", type=myDsl_AffectVar, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AffectVar25", type=myDsl_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp26: BinaryAssociation = BinaryAssociation(
    name="exp26",
    ends={
        Property(name="myDsl_Exprs", type=myDsl_AffectVar, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AffectVar27", type=myDsl_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp228: BinaryAssociation = BinaryAssociation(
    name="exp228",
    ends={
        Property(name="myDsl_Expr", type=myDsl_While, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_While29", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com330: BinaryAssociation = BinaryAssociation(
    name="com330",
    ends={
        Property(name="myDsl_Commandes32", type=myDsl_While, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_While31", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp333: BinaryAssociation = BinaryAssociation(
    name="exp333",
    ends={
        Property(name="myDsl_Expr35", type=myDsl_For, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For34", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com436: BinaryAssociation = BinaryAssociation(
    name="com436",
    ends={
        Property(name="myDsl_Commandes38", type=myDsl_For, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For37", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
le177: BinaryAssociation = BinaryAssociation(
    name="le177",
    ends={
        Property(name="myDsl_LExpr", type=myDsl_Cons, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Cons78", type=myDsl_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
le279: BinaryAssociation = BinaryAssociation(
    name="le279",
    ends={
        Property(name="myDsl_LExpr81", type=myDsl_Liste, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Liste80", type=myDsl_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
le382: BinaryAssociation = BinaryAssociation(
    name="le382",
    ends={
        Property(name="myDsl_Expr84", type=myDsl_Hd, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Hd83", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp548: BinaryAssociation = BinaryAssociation(
    name="exp548",
    ends={
        Property(name="myDsl_Expr50", type=myDsl_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Foreach49", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp651: BinaryAssociation = BinaryAssociation(
    name="exp651",
    ends={
        Property(name="myDsl_Expr53", type=myDsl_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Foreach52", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
com754: BinaryAssociation = BinaryAssociation(
    name="com754",
    ends={
        Property(name="myDsl_Commandes56", type=myDsl_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Foreach55", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprS57: BinaryAssociation = BinaryAssociation(
    name="exprS57",
    ends={
        Property(name="myDsl_Expr59", type=myDsl_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Exprs58", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprS260: BinaryAssociation = BinaryAssociation(
    name="exprS260",
    ends={
        Property(name="myDsl_Expr62", type=myDsl_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Exprs61", type=myDsl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expA63: BinaryAssociation = BinaryAssociation(
    name="expA63",
    ends={
        Property(name="myDsl_ExprAnd", type=myDsl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expr64", type=myDsl_ExprAnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expS65: BinaryAssociation = BinaryAssociation(
    name="expS65",
    ends={
        Property(name="myDsl_ExprSimple", type=myDsl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expr66", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cons67: BinaryAssociation = BinaryAssociation(
    name="cons67",
    ends={
        Property(name="myDsl_Cons", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple68", type=myDsl_Cons, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
liste69: BinaryAssociation = BinaryAssociation(
    name="liste69",
    ends={
        Property(name="myDsl_Liste", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple70", type=myDsl_Liste, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hd71: BinaryAssociation = BinaryAssociation(
    name="hd71",
    ends={
        Property(name="myDsl_Hd", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple72", type=myDsl_Hd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tl73: BinaryAssociation = BinaryAssociation(
    name="tl73",
    ends={
        Property(name="myDsl_Tl", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple74", type=myDsl_Tl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbolEx75: BinaryAssociation = BinaryAssociation(
    name="symbolEx75",
    ends={
        Property(name="myDsl_SymboleEx", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple76", type=myDsl_SymboleEx, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expR119: BinaryAssociation = BinaryAssociation(
    name="expR119",
    ends={
        Property(name="myDsl_Expr121", type=myDsl_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprEq120", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
le485: BinaryAssociation = BinaryAssociation(
    name="le485",
    ends={
        Property(name="myDsl_Expr87", type=myDsl_Tl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Tl86", type=myDsl_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
le588: BinaryAssociation = BinaryAssociation(
    name="le588",
    ends={
        Property(name="myDsl_LExpr90", type=myDsl_SymboleEx, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SymboleEx89", type=myDsl_LExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expLe91: BinaryAssociation = BinaryAssociation(
    name="expLe91",
    ends={
        Property(name="myDsl_Expr93", type=myDsl_LExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LExpr92", type=myDsl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expO94: BinaryAssociation = BinaryAssociation(
    name="expO94",
    ends={
        Property(name="myDsl_ExprOr", type=myDsl_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprAnd95", type=myDsl_ExprOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expO296: BinaryAssociation = BinaryAssociation(
    name="expO296",
    ends={
        Property(name="myDsl_ExprOr98", type=myDsl_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprAnd97", type=myDsl_ExprOr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expN99: BinaryAssociation = BinaryAssociation(
    name="expN99",
    ends={
        Property(name="myDsl_ExprNot", type=myDsl_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprOr100", type=myDsl_ExprNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expN2101: BinaryAssociation = BinaryAssociation(
    name="expN2101",
    ends={
        Property(name="myDsl_ExprNot103", type=myDsl_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprOr102", type=myDsl_ExprNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprNotNot104: BinaryAssociation = BinaryAssociation(
    name="exprNotNot104",
    ends={
        Property(name="myDsl_ExprNotNot", type=myDsl_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprNot105", type=myDsl_ExprNotNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprNotDo106: BinaryAssociation = BinaryAssociation(
    name="exprNotDo106",
    ends={
        Property(name="myDsl_ExprNotDo", type=myDsl_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprNot107", type=myDsl_ExprNotDo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expEq1108: BinaryAssociation = BinaryAssociation(
    name="expEq1108",
    ends={
        Property(name="myDsl_ExprEq", type=myDsl_ExprNotNot, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprNotNot109", type=myDsl_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expEq2110: BinaryAssociation = BinaryAssociation(
    name="expEq2110",
    ends={
        Property(name="myDsl_ExprEq112", type=myDsl_ExprNotDo, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprNotDo111", type=myDsl_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expS1113: BinaryAssociation = BinaryAssociation(
    name="expS1113",
    ends={
        Property(name="myDsl_ExprSimple115", type=myDsl_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprEq114", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expS2116: BinaryAssociation = BinaryAssociation(
    name="expS2116",
    ends={
        Property(name="myDsl_ExprSimple118", type=myDsl_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprEq117", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Output, myDsl_Model, myDsl_Programme, myDsl_Fonction, myDsl_Input, myDsl_Commandes, myDsl_Commande, myDsl_AffectVar, myDsl_While, myDsl_For, myDsl_If, myDsl_Foreach, myDsl_Vars, myDsl_Exprs, myDsl_Expr, myDsl_LExpr, myDsl_ExprAnd, myDsl_ExprSimple, myDsl_Cons, myDsl_Liste, myDsl_Hd, myDsl_Tl, myDsl_SymboleEx, myDsl_ExprOr, myDsl_ExprNot, myDsl_ExprNotNot, myDsl_ExprNotDo, myDsl_ExprEq},
    associations={out7, programme0, fonct1, in3, com5, exp439, com542, com645, com19, com211, affectVar14, whileC16, forC18, ifC20, foreachC22, var124, exp26, exp228, com330, exp333, com436, le177, le279, le382, exp548, exp651, com754, exprS57, exprS260, expA63, expS65, cons67, liste69, hd71, tl73, symbolEx75, expR119, le485, le588, expLe91, expO94, expO296, expN99, expN2101, exprNotNot104, exprNotDo106, expEq1108, expEq2110, expS1113, expS2116},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)