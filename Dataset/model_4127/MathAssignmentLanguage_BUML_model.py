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
mathAssignmentLanguage_ExpOp = Class(name="mathAssignmentLanguage::ExpOp")
mathAssignmentLanguage_MathExp = Class(name="mathAssignmentLanguage::MathExp")
mathAssignmentLanguage_Exp = Class(name="mathAssignmentLanguage::Exp")
mathAssignmentLanguage_Mult = Class(name="mathAssignmentLanguage::Mult")
ExpOp = Class(name="ExpOp")
mathAssignmentLanguage_Div = Class(name="mathAssignmentLanguage::Div")
mathAssignmentLanguage_Plus = Class(name="mathAssignmentLanguage::Plus")
mathAssignmentLanguage_Minus = Class(name="mathAssignmentLanguage::Minus")
mathAssignmentLanguage_Number = Class(name="mathAssignmentLanguage::Number")
Exp = Class(name="Exp")
mathAssignmentLanguage_Parenthesis = Class(name="mathAssignmentLanguage::Parenthesis")

# mathAssignmentLanguage_ExpOp class attributes and methods

# mathAssignmentLanguage_MathExp class attributes and methods

# mathAssignmentLanguage_Exp class attributes and methods

# mathAssignmentLanguage_Mult class attributes and methods

# ExpOp class attributes and methods

# mathAssignmentLanguage_Div class attributes and methods

# mathAssignmentLanguage_Plus class attributes and methods

# mathAssignmentLanguage_Minus class attributes and methods

# mathAssignmentLanguage_Number class attributes and methods
mathAssignmentLanguage_Number_value: Property = Property(name="value", type=IntegerType)
mathAssignmentLanguage_Number.attributes={mathAssignmentLanguage_Number_value}

# Exp class attributes and methods

# mathAssignmentLanguage_Parenthesis class attributes and methods

# Relationships
left2: BinaryAssociation = BinaryAssociation(
    name="left2",
    ends={
        Property(name="mathAssignmentLanguage_Exp3", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathAssignmentLanguage_Exp1", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator4: BinaryAssociation = BinaryAssociation(
    name="operator4",
    ends={
        Property(name="mathAssignmentLanguage_ExpOp", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathAssignmentLanguage_Exp5", type=mathAssignmentLanguage_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right7: BinaryAssociation = BinaryAssociation(
    name="right7",
    ends={
        Property(name="mathAssignmentLanguage_Exp8", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathAssignmentLanguage_Exp6", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="mathAssignmentLanguage_Exp", type=mathAssignmentLanguage_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathAssignmentLanguage_MathExp", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp9: BinaryAssociation = BinaryAssociation(
    name="exp9",
    ends={
        Property(name="mathAssignmentLanguage_Exp10", type=mathAssignmentLanguage_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="mathAssignmentLanguage_Parenthesis", type=mathAssignmentLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathAssignmentLanguage_Mult_ExpOp = Generalization(general=ExpOp, specific=mathAssignmentLanguage_Mult)
gen_mathAssignmentLanguage_Div_ExpOp = Generalization(general=ExpOp, specific=mathAssignmentLanguage_Div)
gen_mathAssignmentLanguage_Plus_ExpOp = Generalization(general=ExpOp, specific=mathAssignmentLanguage_Plus)
gen_mathAssignmentLanguage_Minus_ExpOp = Generalization(general=ExpOp, specific=mathAssignmentLanguage_Minus)
gen_mathAssignmentLanguage_Number_Exp = Generalization(general=Exp, specific=mathAssignmentLanguage_Number)
gen_mathAssignmentLanguage_Parenthesis_Exp = Generalization(general=Exp, specific=mathAssignmentLanguage_Parenthesis)

# Domain Model
domain_model = DomainModel(
    name="mathAssignmentLanguage",
    types={mathAssignmentLanguage_ExpOp, mathAssignmentLanguage_MathExp, mathAssignmentLanguage_Exp, mathAssignmentLanguage_Mult, ExpOp, mathAssignmentLanguage_Div, mathAssignmentLanguage_Plus, mathAssignmentLanguage_Minus, mathAssignmentLanguage_Number, Exp, mathAssignmentLanguage_Parenthesis},
    associations={left2, operator4, right7, exp0, exp9},
    generalizations={gen_mathAssignmentLanguage_Mult_ExpOp, gen_mathAssignmentLanguage_Div_ExpOp, gen_mathAssignmentLanguage_Plus_ExpOp, gen_mathAssignmentLanguage_Minus_ExpOp, gen_mathAssignmentLanguage_Number_Exp, gen_mathAssignmentLanguage_Parenthesis_Exp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)