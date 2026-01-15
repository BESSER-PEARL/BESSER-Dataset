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
whileComp_Program = Class(name="whileComp::Program")
whileComp_Function = Class(name="whileComp::Function")
whileComp_Definition = Class(name="whileComp::Definition")
whileComp_Read = Class(name="whileComp::Read")
whileComp_Commands = Class(name="whileComp::Commands")
whileComp_Write = Class(name="whileComp::Write")
whileComp_Expr = Class(name="whileComp::Expr")
whileComp_Nop = Class(name="whileComp::Nop")
whileComp_Command = Class(name="whileComp::Command")
whileComp_EObject = Class(name="whileComp::EObject")
whileComp_Foreach = Class(name="whileComp::Foreach")
whileComp_If = Class(name="whileComp::If")
whileComp_For = Class(name="whileComp::For")
whileComp_While = Class(name="whileComp::While")
whileComp_ExprSimple = Class(name="whileComp::ExprSimple")
whileComp_Affectation = Class(name="whileComp::Affectation")
whileComp_Not = Class(name="whileComp::Not")
whileComp_Cons = Class(name="whileComp::Cons")
whileComp_List = Class(name="whileComp::List")
whileComp_Hd = Class(name="whileComp::Hd")
whileComp_Tl = Class(name="whileComp::Tl")
whileComp_Nil2 = Class(name="whileComp::Nil2")
whileComp_Lexpr = Class(name="whileComp::Lexpr")

# whileComp_Program class attributes and methods

# whileComp_Function class attributes and methods
whileComp_Function_function: Property = Property(name="function", type=StringType)
whileComp_Function.attributes={whileComp_Function_function}

# whileComp_Definition class attributes and methods

# whileComp_Read class attributes and methods
whileComp_Read_variable: Property = Property(name="variable", type=StringType)
whileComp_Read.attributes={whileComp_Read_variable}

# whileComp_Commands class attributes and methods

# whileComp_Write class attributes and methods
whileComp_Write_variable: Property = Property(name="variable", type=StringType)
whileComp_Write.attributes={whileComp_Write_variable}

# whileComp_Expr class attributes and methods

# whileComp_Nop class attributes and methods
whileComp_Nop_nop: Property = Property(name="nop", type=StringType)
whileComp_Nop.attributes={whileComp_Nop_nop}

# whileComp_Command class attributes and methods

# whileComp_EObject class attributes and methods

# whileComp_Foreach class attributes and methods

# whileComp_If class attributes and methods

# whileComp_For class attributes and methods

# whileComp_While class attributes and methods

# whileComp_ExprSimple class attributes and methods
whileComp_ExprSimple_valeur: Property = Property(name="valeur", type=StringType)
whileComp_ExprSimple_call: Property = Property(name="call", type=StringType)
whileComp_ExprSimple_ope: Property = Property(name="ope", type=StringType)
whileComp_ExprSimple.attributes={whileComp_ExprSimple_valeur, whileComp_ExprSimple_ope, whileComp_ExprSimple_call}

# whileComp_Affectation class attributes and methods
whileComp_Affectation_affectations: Property = Property(name="affectations", type=StringType)
whileComp_Affectation.attributes={whileComp_Affectation_affectations}

# whileComp_Not class attributes and methods
whileComp_Not_not: Property = Property(name="not", type=StringType)
whileComp_Not.attributes={whileComp_Not_not}

# whileComp_Cons class attributes and methods
whileComp_Cons_cons: Property = Property(name="cons", type=StringType)
whileComp_Cons.attributes={whileComp_Cons_cons}

# whileComp_List class attributes and methods
whileComp_List_list: Property = Property(name="list", type=StringType)
whileComp_List.attributes={whileComp_List_list}

# whileComp_Hd class attributes and methods
whileComp_Hd_hd: Property = Property(name="hd", type=StringType)
whileComp_Hd.attributes={whileComp_Hd_hd}

# whileComp_Tl class attributes and methods
whileComp_Tl_tl: Property = Property(name="tl", type=StringType)
whileComp_Tl.attributes={whileComp_Tl_tl}

# whileComp_Nil2 class attributes and methods
whileComp_Nil2_nil: Property = Property(name="nil", type=StringType)
whileComp_Nil2.attributes={whileComp_Nil2_nil}

# whileComp_Lexpr class attributes and methods

# Relationships
functions0: BinaryAssociation = BinaryAssociation(
    name="functions0",
    ends={
        Property(name="whileComp_Function", type=whileComp_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Program", type=whileComp_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition1: BinaryAssociation = BinaryAssociation(
    name="definition1",
    ends={
        Property(name="whileComp_Definition", type=whileComp_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Function2", type=whileComp_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
read3: BinaryAssociation = BinaryAssociation(
    name="read3",
    ends={
        Property(name="whileComp_Read", type=whileComp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Definition4", type=whileComp_Read, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands5: BinaryAssociation = BinaryAssociation(
    name="commands5",
    ends={
        Property(name="whileComp_Commands", type=whileComp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Definition6", type=whileComp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
write7: BinaryAssociation = BinaryAssociation(
    name="write7",
    ends={
        Property(name="whileComp_Write", type=whileComp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Definition8", type=whileComp_Write, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valeurs9: BinaryAssociation = BinaryAssociation(
    name="valeurs9",
    ends={
        Property(name="whileComp_Expr", type=whileComp_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Affectation", type=whileComp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
command10: BinaryAssociation = BinaryAssociation(
    name="command10",
    ends={
        Property(name="whileComp_Command", type=whileComp_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Commands11", type=whileComp_Command, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands12: BinaryAssociation = BinaryAssociation(
    name="commands12",
    ends={
        Property(name="whileComp_Command14", type=whileComp_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Commands13", type=whileComp_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
command15: BinaryAssociation = BinaryAssociation(
    name="command15",
    ends={
        Property(name="whileComp_EObject", type=whileComp_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Command16", type=whileComp_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr117: BinaryAssociation = BinaryAssociation(
    name="expr117",
    ends={
        Property(name="whileComp_Expr18", type=whileComp_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Foreach", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr219: BinaryAssociation = BinaryAssociation(
    name="expr219",
    ends={
        Property(name="whileComp_Expr21", type=whileComp_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Foreach20", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands22: BinaryAssociation = BinaryAssociation(
    name="commands22",
    ends={
        Property(name="whileComp_Commands24", type=whileComp_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Foreach23", type=whileComp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr25: BinaryAssociation = BinaryAssociation(
    name="expr25",
    ends={
        Property(name="whileComp_Expr26", type=whileComp_If, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_If", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands127: BinaryAssociation = BinaryAssociation(
    name="commands127",
    ends={
        Property(name="whileComp_Commands29", type=whileComp_If, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_If28", type=whileComp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands230: BinaryAssociation = BinaryAssociation(
    name="commands230",
    ends={
        Property(name="whileComp_Commands32", type=whileComp_If, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_If31", type=whileComp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr33: BinaryAssociation = BinaryAssociation(
    name="expr33",
    ends={
        Property(name="whileComp_Expr34", type=whileComp_For, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_For", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands35: BinaryAssociation = BinaryAssociation(
    name="commands35",
    ends={
        Property(name="whileComp_Commands37", type=whileComp_For, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_For36", type=whileComp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr38: BinaryAssociation = BinaryAssociation(
    name="expr38",
    ends={
        Property(name="whileComp_Expr39", type=whileComp_While, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_While", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands40: BinaryAssociation = BinaryAssociation(
    name="commands40",
    ends={
        Property(name="whileComp_Commands42", type=whileComp_While, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_While41", type=whileComp_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprsimple43: BinaryAssociation = BinaryAssociation(
    name="exprsimple43",
    ends={
        Property(name="whileComp_ExprSimple", type=whileComp_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Expr44", type=whileComp_ExprSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr45: BinaryAssociation = BinaryAssociation(
    name="lexpr45",
    ends={
        Property(name="whileComp_Lexpr", type=whileComp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_ExprSimple46", type=whileComp_Lexpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr47: BinaryAssociation = BinaryAssociation(
    name="expr47",
    ends={
        Property(name="whileComp_Expr49", type=whileComp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_ExprSimple48", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
n50: BinaryAssociation = BinaryAssociation(
    name="n50",
    ends={
        Property(name="whileComp_Not", type=whileComp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_ExprSimple51", type=whileComp_Not, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex152: BinaryAssociation = BinaryAssociation(
    name="ex152",
    ends={
        Property(name="whileComp_Expr54", type=whileComp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_ExprSimple53", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex255: BinaryAssociation = BinaryAssociation(
    name="ex255",
    ends={
        Property(name="whileComp_Expr57", type=whileComp_ExprSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_ExprSimple56", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr58: BinaryAssociation = BinaryAssociation(
    name="expr58",
    ends={
        Property(name="whileComp_Expr60", type=whileComp_Lexpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Lexpr59", type=whileComp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr62: BinaryAssociation = BinaryAssociation(
    name="lexpr62",
    ends={
        Property(name="whileComp_Lexpr63", type=whileComp_Lexpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileComp_Lexpr61", type=whileComp_Lexpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="whileComp",
    types={whileComp_Program, whileComp_Function, whileComp_Definition, whileComp_Read, whileComp_Commands, whileComp_Write, whileComp_Expr, whileComp_Nop, whileComp_Command, whileComp_EObject, whileComp_Foreach, whileComp_If, whileComp_For, whileComp_While, whileComp_ExprSimple, whileComp_Affectation, whileComp_Not, whileComp_Cons, whileComp_List, whileComp_Hd, whileComp_Tl, whileComp_Nil2, whileComp_Lexpr},
    associations={functions0, definition1, read3, commands5, write7, valeurs9, command10, commands12, command15, expr117, expr219, commands22, expr25, commands127, commands230, expr33, commands35, expr38, commands40, exprsimple43, lexpr45, expr47, n50, ex152, ex255, expr58, lexpr62},
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