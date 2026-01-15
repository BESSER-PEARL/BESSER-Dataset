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
myDsl_Program = Class(name="myDsl::Program")
myDsl_Fonction = Class(name="myDsl::Fonction")
myDsl_Input = Class(name="myDsl::Input")
myDsl_Commandes = Class(name="myDsl::Commandes")
myDsl_Affectation = Class(name="myDsl::Affectation")
myDsl_Variable = Class(name="myDsl::Variable")
myDsl_Expression = Class(name="myDsl::Expression")
myDsl_If = Class(name="myDsl::If")
myDsl_While = Class(name="myDsl::While")
myDsl_For = Class(name="myDsl::For")
myDsl_Output = Class(name="myDsl::Output")
myDsl_Commande = Class(name="myDsl::Commande")
myDsl_EObject = Class(name="myDsl::EObject")
myDsl_AccSucc = Class(name="myDsl::AccSucc")
myDsl_ElemSimple = Class(name="myDsl::ElemSimple")
myDsl_Lexpr = Class(name="myDsl::Lexpr")
myDsl_COMPARATEUR = Class(name="myDsl::COMPARATEUR")
myDsl_ForEach = Class(name="myDsl::ForEach")
myDsl_Nop = Class(name="myDsl::Nop")
myDsl_Condition = Class(name="myDsl::Condition")
myDsl_ExprSimple = Class(name="myDsl::ExprSimple")
myDsl_Nill = Class(name="myDsl::Nill")
myDsl_ABin = Class(name="myDsl::ABin")
myDsl_Not = Class(name="myDsl::Not")
Condition = Class(name="Condition")
myDsl_OpConstructeur = Class(name="myDsl::OpConstructeur")
myDsl_OpAccSucc = Class(name="myDsl::OpAccSucc")

# myDsl_Program class attributes and methods

# myDsl_Fonction class attributes and methods
myDsl_Fonction_nom: Property = Property(name="nom", type=StringType)
myDsl_Fonction.attributes={myDsl_Fonction_nom}

# myDsl_Input class attributes and methods
myDsl_Input_in: Property = Property(name="in", type=StringType)
myDsl_Input.attributes={myDsl_Input_in}

# myDsl_Commandes class attributes and methods

# myDsl_Affectation class attributes and methods

# myDsl_Variable class attributes and methods
myDsl_Variable_variable: Property = Property(name="variable", type=StringType)
myDsl_Variable.attributes={myDsl_Variable_variable}

# myDsl_Expression class attributes and methods

# myDsl_If class attributes and methods

# myDsl_While class attributes and methods

# myDsl_For class attributes and methods

# myDsl_Output class attributes and methods
myDsl_Output_out: Property = Property(name="out", type=StringType)
myDsl_Output.attributes={myDsl_Output_out}

# myDsl_Commande class attributes and methods

# myDsl_EObject class attributes and methods

# myDsl_AccSucc class attributes and methods

# myDsl_ElemSimple class attributes and methods
myDsl_ElemSimple_symb: Property = Property(name="symb", type=StringType)
myDsl_ElemSimple.attributes={myDsl_ElemSimple_symb}

# myDsl_Lexpr class attributes and methods

# myDsl_COMPARATEUR class attributes and methods
myDsl_COMPARATEUR_comparateur: Property = Property(name="comparateur", type=StringType)
myDsl_COMPARATEUR.attributes={myDsl_COMPARATEUR_comparateur}

# myDsl_ForEach class attributes and methods

# myDsl_Nop class attributes and methods
myDsl_Nop_nop: Property = Property(name="nop", type=StringType)
myDsl_Nop.attributes={myDsl_Nop_nop}

# myDsl_Condition class attributes and methods

# myDsl_ExprSimple class attributes and methods
myDsl_ExprSimple_symb: Property = Property(name="symb", type=StringType)
myDsl_ExprSimple.attributes={myDsl_ExprSimple_symb}

# myDsl_Nill class attributes and methods
myDsl_Nill_nil: Property = Property(name="nil", type=StringType)
myDsl_Nill.attributes={myDsl_Nill_nil}

# myDsl_ABin class attributes and methods

# myDsl_Not class attributes and methods
myDsl_Not_not: Property = Property(name="not", type=StringType)
myDsl_Not.attributes={myDsl_Not_not}

# Condition class attributes and methods

# myDsl_OpConstructeur class attributes and methods
myDsl_OpConstructeur_op: Property = Property(name="op", type=StringType)
myDsl_OpConstructeur.attributes={myDsl_OpConstructeur_op}

# myDsl_OpAccSucc class attributes and methods
myDsl_OpAccSucc_op: Property = Property(name="op", type=StringType)
myDsl_OpAccSucc.attributes={myDsl_OpAccSucc_op}

# Relationships
fonctions0: BinaryAssociation = BinaryAssociation(
    name="fonctions0",
    ends={
        Property(name="myDsl_Fonction", type=myDsl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Program", type=myDsl_Fonction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in1: BinaryAssociation = BinaryAssociation(
    name="in1",
    ends={
        Property(name="myDsl_Input", type=myDsl_Fonction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fonction2", type=myDsl_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commandes3: BinaryAssociation = BinaryAssociation(
    name="commandes3",
    ends={
        Property(name="myDsl_Commandes", type=myDsl_Fonction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fonction4", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commande12: BinaryAssociation = BinaryAssociation(
    name="commande12",
    ends={
        Property(name="myDsl_Commande13", type=myDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_EObject", type=myDsl_Commande, multiplicity=Multiplicity(1, 1))
    }
)
variable14: BinaryAssociation = BinaryAssociation(
    name="variable14",
    ends={
        Property(name="myDsl_Variable", type=myDsl_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Affectation", type=myDsl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elm15: BinaryAssociation = BinaryAssociation(
    name="elm15",
    ends={
        Property(name="myDsl_Expression", type=myDsl_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Affectation16", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond17: BinaryAssociation = BinaryAssociation(
    name="cond17",
    ends={
        Property(name="myDsl_Expression18", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsIf19: BinaryAssociation = BinaryAssociation(
    name="cmdsIf19",
    ends={
        Property(name="myDsl_Commandes21", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If20", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsElse22: BinaryAssociation = BinaryAssociation(
    name="cmdsElse22",
    ends={
        Property(name="myDsl_Commandes24", type=myDsl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If23", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond25: BinaryAssociation = BinaryAssociation(
    name="cond25",
    ends={
        Property(name="myDsl_Expression26", type=myDsl_While, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_While", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsWh27: BinaryAssociation = BinaryAssociation(
    name="cmdsWh27",
    ends={
        Property(name="myDsl_Commandes29", type=myDsl_While, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_While28", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond30: BinaryAssociation = BinaryAssociation(
    name="cond30",
    ends={
        Property(name="myDsl_Expression31", type=myDsl_For, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsFor32: BinaryAssociation = BinaryAssociation(
    name="cmdsFor32",
    ends={
        Property(name="myDsl_Commandes34", type=myDsl_For, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For33", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out5: BinaryAssociation = BinaryAssociation(
    name="out5",
    ends={
        Property(name="myDsl_Output", type=myDsl_Fonction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Fonction6", type=myDsl_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commande7: BinaryAssociation = BinaryAssociation(
    name="commande7",
    ends={
        Property(name="myDsl_Commande", type=myDsl_Commandes, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commandes8", type=myDsl_Commande, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commandes9: BinaryAssociation = BinaryAssociation(
    name="commandes9",
    ends={
        Property(name="myDsl_Commande11", type=myDsl_Commandes, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Commandes10", type=myDsl_Commande, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accsucc54: BinaryAssociation = BinaryAssociation(
    name="accsucc54",
    ends={
        Property(name="myDsl_AccSucc", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple55", type=myDsl_AccSucc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elemSimple56: BinaryAssociation = BinaryAssociation(
    name="elemSimple56",
    ends={
        Property(name="myDsl_ElemSimple", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple57", type=myDsl_ElemSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e158: BinaryAssociation = BinaryAssociation(
    name="e158",
    ends={
        Property(name="myDsl_ExprSimple59", type=myDsl_Lexpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Lexpr", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr61: BinaryAssociation = BinaryAssociation(
    name="lexpr61",
    ends={
        Property(name="myDsl_Lexpr62", type=myDsl_Lexpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Lexpr60", type=myDsl_Lexpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr63: BinaryAssociation = BinaryAssociation(
    name="lexpr63",
    ends={
        Property(name="myDsl_Lexpr65", type=myDsl_ElemSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ElemSimple64", type=myDsl_Lexpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e166: BinaryAssociation = BinaryAssociation(
    name="e166",
    ends={
        Property(name="myDsl_ExprSimple68", type=myDsl_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Condition67", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comp69: BinaryAssociation = BinaryAssociation(
    name="comp69",
    ends={
        Property(name="myDsl_COMPARATEUR", type=myDsl_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Condition70", type=myDsl_COMPARATEUR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elem35: BinaryAssociation = BinaryAssociation(
    name="elem35",
    ends={
        Property(name="myDsl_Expression36", type=myDsl_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForEach", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ensemble37: BinaryAssociation = BinaryAssociation(
    name="ensemble37",
    ends={
        Property(name="myDsl_Expression39", type=myDsl_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForEach38", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsFor40: BinaryAssociation = BinaryAssociation(
    name="cmdsFor40",
    ends={
        Property(name="myDsl_Commandes42", type=myDsl_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForEach41", type=myDsl_Commandes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond43: BinaryAssociation = BinaryAssociation(
    name="cond43",
    ends={
        Property(name="myDsl_Condition", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression44", type=myDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs45: BinaryAssociation = BinaryAssociation(
    name="exprs45",
    ends={
        Property(name="myDsl_ExprSimple", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression46", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nil47: BinaryAssociation = BinaryAssociation(
    name="nil47",
    ends={
        Property(name="myDsl_Nill", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple48", type=myDsl_Nill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable49: BinaryAssociation = BinaryAssociation(
    name="variable49",
    ends={
        Property(name="myDsl_Variable51", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple50", type=myDsl_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abin52: BinaryAssociation = BinaryAssociation(
    name="abin52",
    ends={
        Property(name="myDsl_ABin", type=myDsl_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSimple53", type=myDsl_ABin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr87: BinaryAssociation = BinaryAssociation(
    name="expr87",
    ends={
        Property(name="myDsl_Expression88", type=myDsl_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Not", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e271: BinaryAssociation = BinaryAssociation(
    name="e271",
    ends={
        Property(name="myDsl_Expression73", type=myDsl_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Condition72", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op74: BinaryAssociation = BinaryAssociation(
    name="op74",
    ends={
        Property(name="myDsl_OpConstructeur", type=myDsl_ABin, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ABin75", type=myDsl_OpConstructeur, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e176: BinaryAssociation = BinaryAssociation(
    name="e176",
    ends={
        Property(name="myDsl_Expression78", type=myDsl_ABin, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ABin77", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e279: BinaryAssociation = BinaryAssociation(
    name="e279",
    ends={
        Property(name="myDsl_Expression81", type=myDsl_ABin, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ABin80", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op82: BinaryAssociation = BinaryAssociation(
    name="op82",
    ends={
        Property(name="myDsl_OpAccSucc", type=myDsl_AccSucc, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AccSucc83", type=myDsl_OpAccSucc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr84: BinaryAssociation = BinaryAssociation(
    name="expr84",
    ends={
        Property(name="myDsl_ExprSimple86", type=myDsl_AccSucc, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AccSucc85", type=myDsl_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Not_Condition = Generalization(general=Condition, specific=myDsl_Not)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Program, myDsl_Fonction, myDsl_Input, myDsl_Commandes, myDsl_Affectation, myDsl_Variable, myDsl_Expression, myDsl_If, myDsl_While, myDsl_For, myDsl_Output, myDsl_Commande, myDsl_EObject, myDsl_AccSucc, myDsl_ElemSimple, myDsl_Lexpr, myDsl_COMPARATEUR, myDsl_ForEach, myDsl_Nop, myDsl_Condition, myDsl_ExprSimple, myDsl_Nill, myDsl_ABin, myDsl_Not, Condition, myDsl_OpConstructeur, myDsl_OpAccSucc},
    associations={fonctions0, in1, commandes3, commande12, variable14, elm15, cond17, cmdsIf19, cmdsElse22, cond25, cmdsWh27, cond30, cmdsFor32, out5, commande7, commandes9, accsucc54, elemSimple56, e158, lexpr61, lexpr63, e166, comp69, elem35, ensemble37, cmdsFor40, cond43, exprs45, nil47, variable49, abin52, expr87, e271, op74, e176, e279, op82, expr84},
    generalizations={gen_myDsl_Not_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)