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
whileCpp_Commands = Class(name="whileCpp::Commands")
whileCpp_Output = Class(name="whileCpp::Output")
whileCpp_Vars = Class(name="whileCpp::Vars")
whileCpp_Command = Class(name="whileCpp::Command")
whileCpp_Program = Class(name="whileCpp::Program")
whileCpp_Function = Class(name="whileCpp::Function")
whileCpp_Definition = Class(name="whileCpp::Definition")
whileCpp_Input = Class(name="whileCpp::Input")
whileCpp_ExprSimple = Class(name="whileCpp::ExprSimple")
whileCpp_ExprAnd = Class(name="whileCpp::ExprAnd")
whileCpp_Exprs = Class(name="whileCpp::Exprs")
whileCpp_CommandWhile = Class(name="whileCpp::CommandWhile")
whileCpp_CommandIf = Class(name="whileCpp::CommandIf")
whileCpp_CommandForEach = Class(name="whileCpp::CommandForEach")
whileCpp_Expr = Class(name="whileCpp::Expr")
whileCpp_ExprOr = Class(name="whileCpp::ExprOr")
whileCpp_ExprNot = Class(name="whileCpp::ExprNot")
whileCpp_ExprEq = Class(name="whileCpp::ExprEq")
whileCpp_Cons = Class(name="whileCpp::Cons")

# whileCpp_Commands class attributes and methods

# whileCpp_Output class attributes and methods
whileCpp_Output_varOut: Property = Property(name="varOut", type=StringType)
whileCpp_Output.attributes={whileCpp_Output_varOut}

# whileCpp_Vars class attributes and methods
whileCpp_Vars_varGen: Property = Property(name="varGen", type=StringType)
whileCpp_Vars.attributes={whileCpp_Vars_varGen}

# whileCpp_Command class attributes and methods
whileCpp_Command_nop: Property = Property(name="nop", type=StringType)
whileCpp_Command.attributes={whileCpp_Command_nop}

# whileCpp_Program class attributes and methods

# whileCpp_Function class attributes and methods
whileCpp_Function_nom: Property = Property(name="nom", type=StringType)
whileCpp_Function.attributes={whileCpp_Function_nom}

# whileCpp_Definition class attributes and methods

# whileCpp_Input class attributes and methods
whileCpp_Input_varIn: Property = Property(name="varIn", type=StringType)
whileCpp_Input.attributes={whileCpp_Input_varIn}

# whileCpp_ExprSimple class attributes and methods
whileCpp_ExprSimple_nil: Property = Property(name="nil", type=StringType)
whileCpp_ExprSimple_vari: Property = Property(name="vari", type=StringType)
whileCpp_ExprSimple_symb: Property = Property(name="symb", type=StringType)
whileCpp_ExprSimple_exprHead: Property = Property(name="exprHead", type=StringType)
whileCpp_ExprSimple_exprTail: Property = Property(name="exprTail", type=StringType)
whileCpp_ExprSimple_nomSymb: Property = Property(name="nomSymb", type=StringType)
whileCpp_ExprSimple.attributes={whileCpp_ExprSimple_vari, whileCpp_ExprSimple_nomSymb, whileCpp_ExprSimple_exprHead, whileCpp_ExprSimple_exprTail, whileCpp_ExprSimple_symb, whileCpp_ExprSimple_nil}

# whileCpp_ExprAnd class attributes and methods
whileCpp_ExprAnd_exprAnd: Property = Property(name="exprAnd", type=StringType)
whileCpp_ExprAnd.attributes={whileCpp_ExprAnd_exprAnd}

# whileCpp_Exprs class attributes and methods

# whileCpp_CommandWhile class attributes and methods
whileCpp_CommandWhile_w: Property = Property(name="w", type=StringType)
whileCpp_CommandWhile.attributes={whileCpp_CommandWhile_w}

# whileCpp_CommandIf class attributes and methods

# whileCpp_CommandForEach class attributes and methods

# whileCpp_Expr class attributes and methods

# whileCpp_ExprOr class attributes and methods
whileCpp_ExprOr_exprOr: Property = Property(name="exprOr", type=StringType)
whileCpp_ExprOr.attributes={whileCpp_ExprOr_exprOr}

# whileCpp_ExprNot class attributes and methods
whileCpp_ExprNot_not: Property = Property(name="not", type=StringType)
whileCpp_ExprNot.attributes={whileCpp_ExprNot_not}

# whileCpp_ExprEq class attributes and methods

# whileCpp_Cons class attributes and methods
whileCpp_Cons_exprCons: Property = Property(name="exprCons", type=StringType)
whileCpp_Cons.attributes={whileCpp_Cons_exprCons}

# Relationships
commandes5: BinaryAssociation = BinaryAssociation(
    name="commandes5",
    ends={
        Property(name="whileCpp_Commands", type=whileCpp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Definition6", type=whileCpp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs7: BinaryAssociation = BinaryAssociation(
    name="outputs7",
    ends={
        Property(name="whileCpp_Output", type=whileCpp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Definition8", type=whileCpp_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commande9: BinaryAssociation = BinaryAssociation(
    name="commande9",
    ends={
        Property(name="whileCpp_Command", type=whileCpp_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Commands10", type=whileCpp_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fonctions0: BinaryAssociation = BinaryAssociation(
    name="fonctions0",
    ends={
        Property(name="whileCpp_Function", type=whileCpp_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Program", type=whileCpp_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition1: BinaryAssociation = BinaryAssociation(
    name="definition1",
    ends={
        Property(name="whileCpp_Definition", type=whileCpp_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Function2", type=whileCpp_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ensemb38: BinaryAssociation = BinaryAssociation(
    name="ensemb38",
    ends={
        Property(name="whileCpp_Expr40", type=whileCpp_CommandForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandForEach39", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds41: BinaryAssociation = BinaryAssociation(
    name="cmds41",
    ends={
        Property(name="whileCpp_Commands43", type=whileCpp_CommandForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandForEach42", type=whileCpp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs3: BinaryAssociation = BinaryAssociation(
    name="inputs3",
    ends={
        Property(name="whileCpp_Input", type=whileCpp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Definition4", type=whileCpp_Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expGen44: BinaryAssociation = BinaryAssociation(
    name="expGen44",
    ends={
        Property(name="whileCpp_Expr46", type=whileCpp_Exprs, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Exprs45", type=whileCpp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprSimp47: BinaryAssociation = BinaryAssociation(
    name="exprSimp47",
    ends={
        Property(name="whileCpp_ExprSimple", type=whileCpp_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Expr48", type=whileCpp_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprAnd49: BinaryAssociation = BinaryAssociation(
    name="exprAnd49",
    ends={
        Property(name="whileCpp_ExprAnd", type=whileCpp_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Expr50", type=whileCpp_ExprAnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars11: BinaryAssociation = BinaryAssociation(
    name="vars11",
    ends={
        Property(name="whileCpp_Vars", type=whileCpp_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Command12", type=whileCpp_Vars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs13: BinaryAssociation = BinaryAssociation(
    name="exprs13",
    ends={
        Property(name="whileCpp_Exprs", type=whileCpp_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Command14", type=whileCpp_Exprs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdWhile15: BinaryAssociation = BinaryAssociation(
    name="cmdWhile15",
    ends={
        Property(name="whileCpp_CommandWhile", type=whileCpp_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Command16", type=whileCpp_CommandWhile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdIf17: BinaryAssociation = BinaryAssociation(
    name="cmdIf17",
    ends={
        Property(name="whileCpp_CommandIf", type=whileCpp_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Command18", type=whileCpp_CommandIf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdForEach19: BinaryAssociation = BinaryAssociation(
    name="cmdForEach19",
    ends={
        Property(name="whileCpp_CommandForEach", type=whileCpp_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Command20", type=whileCpp_CommandForEach, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr21: BinaryAssociation = BinaryAssociation(
    name="expr21",
    ends={
        Property(name="whileCpp_Expr", type=whileCpp_CommandWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandWhile22", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmds23: BinaryAssociation = BinaryAssociation(
    name="cmds23",
    ends={
        Property(name="whileCpp_Commands25", type=whileCpp_CommandWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandWhile24", type=whileCpp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond26: BinaryAssociation = BinaryAssociation(
    name="cond26",
    ends={
        Property(name="whileCpp_Expr28", type=whileCpp_CommandIf, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandIf27", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsThen29: BinaryAssociation = BinaryAssociation(
    name="cmdsThen29",
    ends={
        Property(name="whileCpp_Commands31", type=whileCpp_CommandIf, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandIf30", type=whileCpp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsElse32: BinaryAssociation = BinaryAssociation(
    name="cmdsElse32",
    ends={
        Property(name="whileCpp_Commands34", type=whileCpp_CommandIf, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandIf33", type=whileCpp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elem35: BinaryAssociation = BinaryAssociation(
    name="elem35",
    ends={
        Property(name="whileCpp_Expr37", type=whileCpp_CommandForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_CommandForEach36", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbAtt59: BinaryAssociation = BinaryAssociation(
    name="symbAtt59",
    ends={
        Property(name="whileCpp_Expr61", type=whileCpp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprSimple60", type=whileCpp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprOr62: BinaryAssociation = BinaryAssociation(
    name="exprOr62",
    ends={
        Property(name="whileCpp_ExprOr", type=whileCpp_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprAnd63", type=whileCpp_ExprOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprAndAtt65: BinaryAssociation = BinaryAssociation(
    name="exprAndAtt65",
    ends={
        Property(name="whileCpp_ExprAnd66", type=whileCpp_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprAnd64", type=whileCpp_ExprAnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprNot67: BinaryAssociation = BinaryAssociation(
    name="exprNot67",
    ends={
        Property(name="whileCpp_ExprNot", type=whileCpp_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprOr68", type=whileCpp_ExprNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprOrAtt70: BinaryAssociation = BinaryAssociation(
    name="exprOrAtt70",
    ends={
        Property(name="whileCpp_ExprOr71", type=whileCpp_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprOr69", type=whileCpp_ExprOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprEq72: BinaryAssociation = BinaryAssociation(
    name="exprEq72",
    ends={
        Property(name="whileCpp_ExprEq", type=whileCpp_ExprNot, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprNot73", type=whileCpp_ExprEq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr74: BinaryAssociation = BinaryAssociation(
    name="expr74",
    ends={
        Property(name="whileCpp_Expr76", type=whileCpp_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprEq75", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSim177: BinaryAssociation = BinaryAssociation(
    name="exprSim177",
    ends={
        Property(name="whileCpp_ExprSimple79", type=whileCpp_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprEq78", type=whileCpp_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprCons51: BinaryAssociation = BinaryAssociation(
    name="exprCons51",
    ends={
        Property(name="whileCpp_Cons", type=whileCpp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprSimple52", type=whileCpp_Cons, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprHeadAtt53: BinaryAssociation = BinaryAssociation(
    name="exprHeadAtt53",
    ends={
        Property(name="whileCpp_Expr55", type=whileCpp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprSimple54", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprTailAtt56: BinaryAssociation = BinaryAssociation(
    name="exprTailAtt56",
    ends={
        Property(name="whileCpp_Expr58", type=whileCpp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprSimple57", type=whileCpp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSim280: BinaryAssociation = BinaryAssociation(
    name="exprSim280",
    ends={
        Property(name="whileCpp_ExprSimple82", type=whileCpp_ExprEq, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_ExprEq81", type=whileCpp_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprConsAttList83: BinaryAssociation = BinaryAssociation(
    name="exprConsAttList83",
    ends={
        Property(name="whileCpp_Expr85", type=whileCpp_Cons, multiplicity=Multiplicity(1, 1)),
        Property(name="whileCpp_Cons84", type=whileCpp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="whileCpp",
    types={whileCpp_Commands, whileCpp_Output, whileCpp_Vars, whileCpp_Command, whileCpp_Program, whileCpp_Function, whileCpp_Definition, whileCpp_Input, whileCpp_ExprSimple, whileCpp_ExprAnd, whileCpp_Exprs, whileCpp_CommandWhile, whileCpp_CommandIf, whileCpp_CommandForEach, whileCpp_Expr, whileCpp_ExprOr, whileCpp_ExprNot, whileCpp_ExprEq, whileCpp_Cons},
    associations={commandes5, outputs7, commande9, fonctions0, definition1, ensemb38, cmds41, inputs3, expGen44, exprSimp47, exprAnd49, vars11, exprs13, cmdWhile15, cmdIf17, cmdForEach19, expr21, cmds23, cond26, cmdsThen29, cmdsElse32, elem35, symbAtt59, exprOr62, exprAndAtt65, exprNot67, exprOrAtt70, exprEq72, expr74, exprSim177, exprCons51, exprHeadAtt53, exprTailAtt56, exprSim280, exprConsAttList83},
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