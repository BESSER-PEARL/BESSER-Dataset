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

# Enumerations
RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="greaterEqual"),
			EnumerationLiteral(name="lessEqual"),
			EnumerationLiteral(name="and_")
    }
)

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="mult"),
			EnumerationLiteral(name="div")
    }
)

# Classes
fmpl_Policy = Class(name="fmpl_Policy")
fmpl_Automata = Class(name="fmpl_Automata")
fmpl_Expression = Class(name="fmpl_Expression", is_abstract=True)
fmpl_State = Class(name="fmpl_State")
fmpl_Transition = Class(name="fmpl_Transition")
fmpl_Exec = Class(name="fmpl_Exec")
Expression = Class(name="Expression")
fmpl_Cond = Class(name="fmpl_Cond")
fmpl_Relational = Class(name="fmpl_Relational")
fmpl_Write = Class(name="fmpl_Write")
fmpl_VarReference = Class(name="fmpl_VarReference")
fmpl_Init = Class(name="fmpl_Init")
fmpl_Read = Class(name="fmpl_Read")
fmpl_ArithmeticExpression = Class(name="fmpl_ArithmeticExpression")
fmpl_Literal = Class(name="fmpl_Literal", is_abstract=True)
fmpl_IntegerLit = Class(name="fmpl_IntegerLit")
Literal = Class(name="Literal")
fmpl_StringLit = Class(name="fmpl_StringLit")
fmpl_Field = Class(name="fmpl_Field", is_abstract=True)
fmpl_VarDeclaration = Class(name="fmpl_VarDeclaration")

# fmpl_Policy class attributes and methods
fmpl_Policy_name: Property = Property(name="name", type=StringType)
fmpl_Policy_parserURI: Property = Property(name="parserURI", type=StringType)
fmpl_Policy.attributes={fmpl_Policy_name, fmpl_Policy_parserURI}

# fmpl_Automata class attributes and methods
fmpl_Automata_name: Property = Property(name="name", type=StringType)
fmpl_Automata.attributes={fmpl_Automata_name}

# fmpl_Expression class attributes and methods

# fmpl_State class attributes and methods
fmpl_State_name: Property = Property(name="name", type=StringType)
fmpl_State.attributes={fmpl_State_name}

# fmpl_Transition class attributes and methods
fmpl_Transition_name: Property = Property(name="name", type=StringType)
fmpl_Transition.attributes={fmpl_Transition_name}

# fmpl_Exec class attributes and methods

# Expression class attributes and methods

# fmpl_Cond class attributes and methods

# fmpl_Relational class attributes and methods
fmpl_Relational_operator: Property = Property(name="operator", type=StringType)
fmpl_Relational.attributes={fmpl_Relational_operator}

# fmpl_Write class attributes and methods
fmpl_Write_initBit: Property = Property(name="initBit", type=IntegerType)
fmpl_Write_length: Property = Property(name="length", type=IntegerType)
fmpl_Write.attributes={fmpl_Write_initBit, fmpl_Write_length}

# fmpl_VarReference class attributes and methods

# fmpl_Init class attributes and methods

# fmpl_Read class attributes and methods
fmpl_Read_initBit: Property = Property(name="initBit", type=IntegerType)
fmpl_Read_length: Property = Property(name="length", type=IntegerType)
fmpl_Read.attributes={fmpl_Read_initBit, fmpl_Read_length}

# fmpl_ArithmeticExpression class attributes and methods
fmpl_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
fmpl_ArithmeticExpression.attributes={fmpl_ArithmeticExpression_operator}

# fmpl_Literal class attributes and methods

# fmpl_IntegerLit class attributes and methods
fmpl_IntegerLit_value: Property = Property(name="value", type=IntegerType)
fmpl_IntegerLit.attributes={fmpl_IntegerLit_value}

# Literal class attributes and methods

# fmpl_StringLit class attributes and methods
fmpl_StringLit_value: Property = Property(name="value", type=StringType)
fmpl_StringLit.attributes={fmpl_StringLit_value}

# fmpl_Field class attributes and methods

# fmpl_VarDeclaration class attributes and methods
fmpl_VarDeclaration_name: Property = Property(name="name", type=StringType)
fmpl_VarDeclaration.attributes={fmpl_VarDeclaration_name}

# Relationships
automatas0: BinaryAssociation = BinaryAssociation(
    name="automatas0",
    ends={
        Property(name="fmpl_Automata", type=fmpl_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Policy", type=fmpl_Automata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="fmpl_State", type=fmpl_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Automata4", type=fmpl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="fmpl_Transition", type=fmpl_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Automata6", type=fmpl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init7: BinaryAssociation = BinaryAssociation(
    name="init7",
    ends={
        Property(name="fmpl_State9", type=fmpl_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Automata8", type=fmpl_State, multiplicity=Multiplicity(1, 1))
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="fmpl_Expression", type=fmpl_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Policy2", type=fmpl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition16: BinaryAssociation = BinaryAssociation(
    name="transition16",
    ends={
        Property(name="fmpl_Transition17", type=fmpl_Exec, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Exec", type=fmpl_Transition, multiplicity=Multiplicity(1, 1))
    }
)
if_18: BinaryAssociation = BinaryAssociation(
    name="if_18",
    ends={
        Property(name="fmpl_Relational", type=fmpl_Cond, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Cond", type=fmpl_Relational, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from_10: BinaryAssociation = BinaryAssociation(
    name="from_10",
    ends={
        Property(name="fmpl_State12", type=fmpl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Transition11", type=fmpl_State, multiplicity=Multiplicity(1, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="fmpl_State15", type=fmpl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Transition14", type=fmpl_State, multiplicity=Multiplicity(1, 1))
    }
)
var22: BinaryAssociation = BinaryAssociation(
    name="var22",
    ends={
        Property(name="fmpl_VarReference", type=fmpl_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Write", type=fmpl_VarReference, multiplicity=Multiplicity(1, 1))
    }
)
then19: BinaryAssociation = BinaryAssociation(
    name="then19",
    ends={
        Property(name="fmpl_Expression21", type=fmpl_Cond, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Cond20", type=fmpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
automata23: BinaryAssociation = BinaryAssociation(
    name="automata23",
    ends={
        Property(name="fmpl_Automata24", type=fmpl_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Init", type=fmpl_Automata, multiplicity=Multiplicity(1, 1))
    }
)
left25: BinaryAssociation = BinaryAssociation(
    name="left25",
    ends={
        Property(name="fmpl_Expression27", type=fmpl_Relational, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Relational26", type=fmpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="fmpl_Expression30", type=fmpl_Relational, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_Relational29", type=fmpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="fmpl_Expression32", type=fmpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_ArithmeticExpression", type=fmpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right33: BinaryAssociation = BinaryAssociation(
    name="right33",
    ends={
        Property(name="fmpl_Expression35", type=fmpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_ArithmeticExpression34", type=fmpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr36: BinaryAssociation = BinaryAssociation(
    name="expr36",
    ends={
        Property(name="fmpl_Expression37", type=fmpl_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_VarDeclaration", type=fmpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name38: BinaryAssociation = BinaryAssociation(
    name="name38",
    ends={
        Property(name="fmpl_VarDeclaration40", type=fmpl_VarReference, multiplicity=Multiplicity(1, 1)),
        Property(name="fmpl_VarReference39", type=fmpl_VarDeclaration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_fmpl_Exec_Expression = Generalization(general=Expression, specific=fmpl_Exec)
gen_fmpl_Cond_Expression = Generalization(general=Expression, specific=fmpl_Cond)
gen_fmpl_Write_Expression = Generalization(general=Expression, specific=fmpl_Write)
gen_fmpl_Init_Expression = Generalization(general=Expression, specific=fmpl_Init)
gen_fmpl_Read_Expression = Generalization(general=Expression, specific=fmpl_Read)
gen_fmpl_ArithmeticExpression_Expression = Generalization(general=Expression, specific=fmpl_ArithmeticExpression)
gen_fmpl_Relational_Expression = Generalization(general=Expression, specific=fmpl_Relational)
gen_fmpl_Literal_Expression = Generalization(general=Expression, specific=fmpl_Literal)
gen_fmpl_IntegerLit_Literal = Generalization(general=Literal, specific=fmpl_IntegerLit)
gen_fmpl_StringLit_Literal = Generalization(general=Literal, specific=fmpl_StringLit)
gen_fmpl_VarReference_Expression = Generalization(general=Expression, specific=fmpl_VarReference)
gen_fmpl_Field_Literal = Generalization(general=Literal, specific=fmpl_Field)
gen_fmpl_VarDeclaration_Expression = Generalization(general=Expression, specific=fmpl_VarDeclaration)

# Domain Model
domain_model = DomainModel(
    name="fmpl",
    types={fmpl_Policy, fmpl_Automata, fmpl_Expression, fmpl_State, fmpl_Transition, fmpl_Exec, Expression, fmpl_Cond, fmpl_Relational, fmpl_Write, fmpl_VarReference, fmpl_Init, fmpl_Read, fmpl_ArithmeticExpression, fmpl_Literal, fmpl_IntegerLit, Literal, fmpl_StringLit, fmpl_Field, fmpl_VarDeclaration, RelationalOperator, ArithmeticOperator},
    associations={automatas0, states3, transitions5, init7, statements1, transition16, if_18, from_10, to13, var22, then19, automata23, left25, right28, left31, right33, expr36, name38},
    generalizations={gen_fmpl_Exec_Expression, gen_fmpl_Cond_Expression, gen_fmpl_Write_Expression, gen_fmpl_Init_Expression, gen_fmpl_Read_Expression, gen_fmpl_ArithmeticExpression_Expression, gen_fmpl_Relational_Expression, gen_fmpl_Literal_Expression, gen_fmpl_IntegerLit_Literal, gen_fmpl_StringLit_Literal, gen_fmpl_VarReference_Expression, gen_fmpl_Field_Literal, gen_fmpl_VarDeclaration_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)