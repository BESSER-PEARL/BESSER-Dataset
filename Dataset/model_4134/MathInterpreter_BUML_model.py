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
mathInterpreter_Mult = Class(name="mathInterpreter::Mult")
mathInterpreter_Div = Class(name="mathInterpreter::Div")
mathInterpreter_MathExp = Class(name="mathInterpreter::MathExp")
mathInterpreter_Exp = Class(name="mathInterpreter::Exp")
mathInterpreter_Plus = Class(name="mathInterpreter::Plus")
Exp = Class(name="Exp")
mathInterpreter_Minus = Class(name="mathInterpreter::Minus")

# mathInterpreter_Mult class attributes and methods
mathInterpreter_Mult_op: Property = Property(name="op", type=StringType)
mathInterpreter_Mult.attributes={mathInterpreter_Mult_op}

# mathInterpreter_Div class attributes and methods
mathInterpreter_Div_op: Property = Property(name="op", type=StringType)
mathInterpreter_Div.attributes={mathInterpreter_Div_op}

# mathInterpreter_MathExp class attributes and methods

# mathInterpreter_Exp class attributes and methods
mathInterpreter_Exp_value: Property = Property(name="value", type=IntegerType)
mathInterpreter_Exp.attributes={mathInterpreter_Exp_value}

# mathInterpreter_Plus class attributes and methods

# Exp class attributes and methods

# mathInterpreter_Minus class attributes and methods

# Relationships
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="mathInterpreter_Exp", type=mathInterpreter_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_MathExp", type=mathInterpreter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp2: BinaryAssociation = BinaryAssociation(
    name="exp2",
    ends={
        Property(name="mathInterpreter_Exp3", type=mathInterpreter_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Exp1", type=mathInterpreter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="mathInterpreter_Exp6", type=mathInterpreter_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Exp4", type=mathInterpreter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="mathInterpreter_Exp9", type=mathInterpreter_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Exp7", type=mathInterpreter_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathInterpreter_Minus_Exp = Generalization(general=Exp, specific=mathInterpreter_Minus)
gen_mathInterpreter_Mult_Exp = Generalization(general=Exp, specific=mathInterpreter_Mult)
gen_mathInterpreter_Div_Exp = Generalization(general=Exp, specific=mathInterpreter_Div)
gen_mathInterpreter_Plus_Exp = Generalization(general=Exp, specific=mathInterpreter_Plus)

# Domain Model
domain_model = DomainModel(
    name="mathInterpreter",
    types={mathInterpreter_Mult, mathInterpreter_Div, mathInterpreter_MathExp, mathInterpreter_Exp, mathInterpreter_Plus, Exp, mathInterpreter_Minus},
    associations={exp0, exp2, left5, right8},
    generalizations={gen_mathInterpreter_Minus_Exp, gen_mathInterpreter_Mult_Exp, gen_mathInterpreter_Div_Exp, gen_mathInterpreter_Plus_Exp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)