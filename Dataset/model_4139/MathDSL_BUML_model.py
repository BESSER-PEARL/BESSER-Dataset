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
mathDSL_Minus = Class(name="mathDSL::Minus")
mathDSL_Multi = Class(name="mathDSL::Multi")
mathDSL_Div = Class(name="mathDSL::Div")
mathDSL_Math = Class(name="mathDSL::Math")
mathDSL_Expression = Class(name="mathDSL::Expression")
mathDSL_Plus = Class(name="mathDSL::Plus")
Expression = Class(name="Expression")
mathDSL_NumberLiteral = Class(name="mathDSL::NumberLiteral")

# mathDSL_Minus class attributes and methods

# mathDSL_Multi class attributes and methods

# mathDSL_Div class attributes and methods

# mathDSL_Math class attributes and methods

# mathDSL_Expression class attributes and methods

# mathDSL_Plus class attributes and methods

# Expression class attributes and methods

# mathDSL_NumberLiteral class attributes and methods
mathDSL_NumberLiteral_value: Property = Property(name="value", type=StringType)
mathDSL_NumberLiteral.attributes={mathDSL_NumberLiteral_value}

# Relationships
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="mathDSL_Plus", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="mathDSL_Expression2", type=mathDSL_Plus, multiplicity=Multiplicity(1, 1))
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="mathDSL_Expression5", type=mathDSL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Plus4", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="mathDSL_Expression7", type=mathDSL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Minus", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="mathDSL_Expression10", type=mathDSL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Minus9", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="mathDSL_Expression12", type=mathDSL_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Multi", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="mathDSL_Expression15", type=mathDSL_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Multi14", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="mathDSL_Expression17", type=mathDSL_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Div", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="mathDSL_Expression", type=mathDSL_Math, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Math", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="mathDSL_Expression20", type=mathDSL_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mathDSL_Div19", type=mathDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathDSL_Minus_Expression = Generalization(general=Expression, specific=mathDSL_Minus)
gen_mathDSL_Multi_Expression = Generalization(general=Expression, specific=mathDSL_Multi)
gen_mathDSL_Div_Expression = Generalization(general=Expression, specific=mathDSL_Div)
gen_mathDSL_Plus_Expression = Generalization(general=Expression, specific=mathDSL_Plus)
gen_mathDSL_NumberLiteral_Expression = Generalization(general=Expression, specific=mathDSL_NumberLiteral)

# Domain Model
domain_model = DomainModel(
    name="mathDSL",
    types={mathDSL_Minus, mathDSL_Multi, mathDSL_Div, mathDSL_Math, mathDSL_Expression, mathDSL_Plus, Expression, mathDSL_NumberLiteral},
    associations={left1, right3, left6, right8, left11, right13, left16, expression0, right18},
    generalizations={gen_mathDSL_Minus_Expression, gen_mathDSL_Multi_Expression, gen_mathDSL_Div_Expression, gen_mathDSL_Plus_Expression, gen_mathDSL_NumberLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)