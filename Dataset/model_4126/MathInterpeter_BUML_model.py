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
mathInterpeter_MathExp = Class(name="mathInterpeter::MathExp")
mathInterpeter_Exp = Class(name="mathInterpeter::Exp")
mathInterpeter_Mult = Class(name="mathInterpeter::Mult")
mathInterpeter_Div = Class(name="mathInterpeter::Div")
mathInterpeter_Primary = Class(name="mathInterpeter::Primary")
Exp = Class(name="Exp")
mathInterpeter_Parenthesis = Class(name="mathInterpeter::Parenthesis")
Primary = Class(name="Primary")
mathInterpeter_Number = Class(name="mathInterpeter::Number")
mathInterpeter_Plus = Class(name="mathInterpeter::Plus")
mathInterpeter_Minus = Class(name="mathInterpeter::Minus")

# mathInterpeter_MathExp class attributes and methods

# mathInterpeter_Exp class attributes and methods

# mathInterpeter_Mult class attributes and methods

# mathInterpeter_Div class attributes and methods

# mathInterpeter_Primary class attributes and methods

# Exp class attributes and methods

# mathInterpeter_Parenthesis class attributes and methods

# Primary class attributes and methods

# mathInterpeter_Number class attributes and methods
mathInterpeter_Number_value: Property = Property(name="value", type=IntegerType)
mathInterpeter_Number.attributes={mathInterpeter_Number_value}

# mathInterpeter_Plus class attributes and methods

# mathInterpeter_Minus class attributes and methods

# Relationships
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="mathInterpeter_Exp14", type=mathInterpeter_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Mult", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="mathInterpeter_Primary", type=mathInterpeter_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Mult16", type=mathInterpeter_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="mathInterpeter_Exp18", type=mathInterpeter_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Div", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="mathInterpeter_Primary21", type=mathInterpeter_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Div20", type=mathInterpeter_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="mathInterpeter_Exp", type=mathInterpeter_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_MathExp", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp1: BinaryAssociation = BinaryAssociation(
    name="exp1",
    ends={
        Property(name="mathInterpeter_Exp2", type=mathInterpeter_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Parenthesis", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left3: BinaryAssociation = BinaryAssociation(
    name="left3",
    ends={
        Property(name="mathInterpeter_Exp4", type=mathInterpeter_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Plus", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right5: BinaryAssociation = BinaryAssociation(
    name="right5",
    ends={
        Property(name="mathInterpeter_Exp7", type=mathInterpeter_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Plus6", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="mathInterpeter_Exp9", type=mathInterpeter_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Minus", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="mathInterpeter_Exp12", type=mathInterpeter_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpeter_Minus11", type=mathInterpeter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathInterpeter_Mult_Exp = Generalization(general=Exp, specific=mathInterpeter_Mult)
gen_mathInterpeter_Div_Exp = Generalization(general=Exp, specific=mathInterpeter_Div)
gen_mathInterpeter_Primary_Exp = Generalization(general=Exp, specific=mathInterpeter_Primary)
gen_mathInterpeter_Parenthesis_Primary = Generalization(general=Primary, specific=mathInterpeter_Parenthesis)
gen_mathInterpeter_Number_Primary = Generalization(general=Primary, specific=mathInterpeter_Number)
gen_mathInterpeter_Plus_Exp = Generalization(general=Exp, specific=mathInterpeter_Plus)
gen_mathInterpeter_Minus_Exp = Generalization(general=Exp, specific=mathInterpeter_Minus)

# Domain Model
domain_model = DomainModel(
    name="mathInterpeter",
    types={mathInterpeter_MathExp, mathInterpeter_Exp, mathInterpeter_Mult, mathInterpeter_Div, mathInterpeter_Primary, Exp, mathInterpeter_Parenthesis, Primary, mathInterpeter_Number, mathInterpeter_Plus, mathInterpeter_Minus},
    associations={left13, right15, left17, right19, exp0, exp1, left3, right5, left8, right10},
    generalizations={gen_mathInterpeter_Mult_Exp, gen_mathInterpeter_Div_Exp, gen_mathInterpeter_Primary_Exp, gen_mathInterpeter_Parenthesis_Primary, gen_mathInterpeter_Number_Primary, gen_mathInterpeter_Plus_Exp, gen_mathInterpeter_Minus_Exp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)