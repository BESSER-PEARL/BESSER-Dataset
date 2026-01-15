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
whileLanguage_Affectation = Class(name="whileLanguage::Affectation")
whileLanguage_Expr = Class(name="whileLanguage::Expr")
whileLanguage_Nop = Class(name="whileLanguage::Nop")
whileLanguage_Command = Class(name="whileLanguage::Command")
whileLanguage_EObject = Class(name="whileLanguage::EObject")
whileLanguage_Program = Class(name="whileLanguage::Program")
whileLanguage_Function = Class(name="whileLanguage::Function")
whileLanguage_Definition = Class(name="whileLanguage::Definition")
whileLanguage_Read = Class(name="whileLanguage::Read")
whileLanguage_Commands = Class(name="whileLanguage::Commands")
whileLanguage_Write = Class(name="whileLanguage::Write")
whileLanguage_Foreach = Class(name="whileLanguage::Foreach")
whileLanguage_If = Class(name="whileLanguage::If")
whileLanguage_For = Class(name="whileLanguage::For")
whileLanguage_While = Class(name="whileLanguage::While")
whileLanguage_Lexpr = Class(name="whileLanguage::Lexpr")

# whileLanguage_Affectation class attributes and methods
whileLanguage_Affectation_affectations: Property = Property(name="affectations", type=StringType)
whileLanguage_Affectation.attributes={whileLanguage_Affectation_affectations}

# whileLanguage_Expr class attributes and methods
whileLanguage_Expr_valeur: Property = Property(name="valeur", type=StringType)
whileLanguage_Expr_ope: Property = Property(name="ope", type=StringType)
whileLanguage_Expr.attributes={whileLanguage_Expr_valeur, whileLanguage_Expr_ope}

# whileLanguage_Nop class attributes and methods
whileLanguage_Nop_nop: Property = Property(name="nop", type=StringType)
whileLanguage_Nop.attributes={whileLanguage_Nop_nop}

# whileLanguage_Command class attributes and methods

# whileLanguage_EObject class attributes and methods

# whileLanguage_Program class attributes and methods

# whileLanguage_Function class attributes and methods
whileLanguage_Function_name: Property = Property(name="name", type=StringType)
whileLanguage_Function.attributes={whileLanguage_Function_name}

# whileLanguage_Definition class attributes and methods

# whileLanguage_Read class attributes and methods
whileLanguage_Read_variable: Property = Property(name="variable", type=StringType)
whileLanguage_Read.attributes={whileLanguage_Read_variable}

# whileLanguage_Commands class attributes and methods

# whileLanguage_Write class attributes and methods
whileLanguage_Write_variable: Property = Property(name="variable", type=StringType)
whileLanguage_Write.attributes={whileLanguage_Write_variable}

# whileLanguage_Foreach class attributes and methods

# whileLanguage_If class attributes and methods

# whileLanguage_For class attributes and methods

# whileLanguage_While class attributes and methods

# whileLanguage_Lexpr class attributes and methods

# Relationships
valeurs9: BinaryAssociation = BinaryAssociation(
    name="valeurs9",
    ends={
        Property(name="whileLanguage_Expr", type=whileLanguage_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Affectation", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands10: BinaryAssociation = BinaryAssociation(
    name="commands10",
    ends={
        Property(name="whileLanguage_Command", type=whileLanguage_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Commands11", type=whileLanguage_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
command12: BinaryAssociation = BinaryAssociation(
    name="command12",
    ends={
        Property(name="whileLanguage_EObject", type=whileLanguage_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Command13", type=whileLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions0: BinaryAssociation = BinaryAssociation(
    name="functions0",
    ends={
        Property(name="whileLanguage_Function", type=whileLanguage_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Program", type=whileLanguage_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition1: BinaryAssociation = BinaryAssociation(
    name="definition1",
    ends={
        Property(name="whileLanguage_Definition", type=whileLanguage_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Function2", type=whileLanguage_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
read3: BinaryAssociation = BinaryAssociation(
    name="read3",
    ends={
        Property(name="whileLanguage_Read", type=whileLanguage_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Definition4", type=whileLanguage_Read, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands5: BinaryAssociation = BinaryAssociation(
    name="commands5",
    ends={
        Property(name="whileLanguage_Commands", type=whileLanguage_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Definition6", type=whileLanguage_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
write7: BinaryAssociation = BinaryAssociation(
    name="write7",
    ends={
        Property(name="whileLanguage_Write", type=whileLanguage_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Definition8", type=whileLanguage_Write, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex146: BinaryAssociation = BinaryAssociation(
    name="ex146",
    ends={
        Property(name="whileLanguage_Expr47", type=whileLanguage_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Expr45", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex249: BinaryAssociation = BinaryAssociation(
    name="ex249",
    ends={
        Property(name="whileLanguage_Expr50", type=whileLanguage_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Expr48", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs51: BinaryAssociation = BinaryAssociation(
    name="exprs51",
    ends={
        Property(name="whileLanguage_Expr53", type=whileLanguage_Lexpr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Lexpr52", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr114: BinaryAssociation = BinaryAssociation(
    name="expr114",
    ends={
        Property(name="whileLanguage_Expr15", type=whileLanguage_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Foreach", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr216: BinaryAssociation = BinaryAssociation(
    name="expr216",
    ends={
        Property(name="whileLanguage_Expr18", type=whileLanguage_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Foreach17", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands19: BinaryAssociation = BinaryAssociation(
    name="commands19",
    ends={
        Property(name="whileLanguage_Commands21", type=whileLanguage_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Foreach20", type=whileLanguage_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr22: BinaryAssociation = BinaryAssociation(
    name="expr22",
    ends={
        Property(name="whileLanguage_Expr23", type=whileLanguage_If, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_If", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands124: BinaryAssociation = BinaryAssociation(
    name="commands124",
    ends={
        Property(name="whileLanguage_Commands26", type=whileLanguage_If, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_If25", type=whileLanguage_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands227: BinaryAssociation = BinaryAssociation(
    name="commands227",
    ends={
        Property(name="whileLanguage_Commands29", type=whileLanguage_If, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_If28", type=whileLanguage_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr30: BinaryAssociation = BinaryAssociation(
    name="expr30",
    ends={
        Property(name="whileLanguage_Expr31", type=whileLanguage_For, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_For", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands32: BinaryAssociation = BinaryAssociation(
    name="commands32",
    ends={
        Property(name="whileLanguage_Commands34", type=whileLanguage_For, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_For33", type=whileLanguage_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr35: BinaryAssociation = BinaryAssociation(
    name="expr35",
    ends={
        Property(name="whileLanguage_Expr36", type=whileLanguage_While, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_While", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands37: BinaryAssociation = BinaryAssociation(
    name="commands37",
    ends={
        Property(name="whileLanguage_Commands39", type=whileLanguage_While, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_While38", type=whileLanguage_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lexpr40: BinaryAssociation = BinaryAssociation(
    name="lexpr40",
    ends={
        Property(name="whileLanguage_Lexpr", type=whileLanguage_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Expr41", type=whileLanguage_Lexpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr43: BinaryAssociation = BinaryAssociation(
    name="expr43",
    ends={
        Property(name="whileLanguage_Expr44", type=whileLanguage_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="whileLanguage_Expr42", type=whileLanguage_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="whileLanguage",
    types={whileLanguage_Affectation, whileLanguage_Expr, whileLanguage_Nop, whileLanguage_Command, whileLanguage_EObject, whileLanguage_Program, whileLanguage_Function, whileLanguage_Definition, whileLanguage_Read, whileLanguage_Commands, whileLanguage_Write, whileLanguage_Foreach, whileLanguage_If, whileLanguage_For, whileLanguage_While, whileLanguage_Lexpr},
    associations={valeurs9, commands10, command12, functions0, definition1, read3, commands5, write7, ex146, ex249, exprs51, expr114, expr216, commands19, expr22, commands124, commands227, expr30, commands32, expr35, commands37, lexpr40, expr43},
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