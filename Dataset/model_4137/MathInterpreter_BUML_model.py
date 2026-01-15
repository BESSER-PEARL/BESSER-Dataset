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
mathInterpreter_MathExp = Class(name="mathInterpreter::MathExp")
mathInterpreter_Expression = Class(name="mathInterpreter::Expression")
mathInterpreter_Exp = Class(name="mathInterpreter::Exp")
Expression = Class(name="Expression")
mathInterpreter_Plus = Class(name="mathInterpreter::Plus")
mathInterpreter_Minus = Class(name="mathInterpreter::Minus")
mathInterpreter_Multiply = Class(name="mathInterpreter::Multiply")
mathInterpreter_Divide = Class(name="mathInterpreter::Divide")
mathInterpreter_Num = Class(name="mathInterpreter::Num")

# mathInterpreter_MathExp class attributes and methods

# mathInterpreter_Expression class attributes and methods

# mathInterpreter_Exp class attributes and methods

# Expression class attributes and methods

# mathInterpreter_Plus class attributes and methods

# mathInterpreter_Minus class attributes and methods

# mathInterpreter_Multiply class attributes and methods

# mathInterpreter_Divide class attributes and methods

# mathInterpreter_Num class attributes and methods
mathInterpreter_Num_value: Property = Property(name="value", type=IntegerType)
mathInterpreter_Num.attributes={mathInterpreter_Num_value}

# Relationships
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="mathInterpreter_Expression", type=mathInterpreter_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_MathExp", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp2: BinaryAssociation = BinaryAssociation(
    name="exp2",
    ends={
        Property(name="mathInterpreter_Expression3", type=mathInterpreter_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Expression1", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left4: BinaryAssociation = BinaryAssociation(
    name="left4",
    ends={
        Property(name="mathInterpreter_Expression5", type=mathInterpreter_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Exp", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator6: BinaryAssociation = BinaryAssociation(
    name="operator6",
    ends={
        Property(name="mathInterpreter_Expression8", type=mathInterpreter_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Exp7", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right9: BinaryAssociation = BinaryAssociation(
    name="right9",
    ends={
        Property(name="mathInterpreter_Expression11", type=mathInterpreter_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Exp10", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathInterpreter_Exp_Expression = Generalization(general=Expression, specific=mathInterpreter_Exp)
gen_mathInterpreter_Plus_Expression = Generalization(general=Expression, specific=mathInterpreter_Plus)
gen_mathInterpreter_Minus_Expression = Generalization(general=Expression, specific=mathInterpreter_Minus)
gen_mathInterpreter_Multiply_Expression = Generalization(general=Expression, specific=mathInterpreter_Multiply)
gen_mathInterpreter_Divide_Expression = Generalization(general=Expression, specific=mathInterpreter_Divide)
gen_mathInterpreter_Num_Expression = Generalization(general=Expression, specific=mathInterpreter_Num)

# Domain Model
domain_model = DomainModel(
    name="mathInterpreter",
    types={mathInterpreter_MathExp, mathInterpreter_Expression, mathInterpreter_Exp, Expression, mathInterpreter_Plus, mathInterpreter_Minus, mathInterpreter_Multiply, mathInterpreter_Divide, mathInterpreter_Num},
    associations={exp0, exp2, left4, operator6, right9},
    generalizations={gen_mathInterpreter_Exp_Expression, gen_mathInterpreter_Plus_Expression, gen_mathInterpreter_Minus_Expression, gen_mathInterpreter_Multiply_Expression, gen_mathInterpreter_Divide_Expression, gen_mathInterpreter_Num_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)