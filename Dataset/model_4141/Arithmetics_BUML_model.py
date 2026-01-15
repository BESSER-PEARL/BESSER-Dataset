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
arithmetics_Evaluation = Class(name="arithmetics::Evaluation")
arithmetics_Expression = Class(name="arithmetics::Expression")
arithmetics_Plus = Class(name="arithmetics::Plus")
Expression = Class(name="Expression")
arithmetics_Minus = Class(name="arithmetics::Minus")
arithmetics_Multi = Class(name="arithmetics::Multi")
arithmetics_Div = Class(name="arithmetics::Div")
arithmetics_NumberLiteral = Class(name="arithmetics::NumberLiteral")

# arithmetics_Evaluation class attributes and methods

# arithmetics_Expression class attributes and methods

# arithmetics_Plus class attributes and methods

# Expression class attributes and methods

# arithmetics_Minus class attributes and methods

# arithmetics_Multi class attributes and methods

# arithmetics_Div class attributes and methods

# arithmetics_NumberLiteral class attributes and methods
arithmetics_NumberLiteral_value: Property = Property(name="value", type=StringType)
arithmetics_NumberLiteral.attributes={arithmetics_NumberLiteral_value}

# Relationships
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="arithmetics_Expression", type=arithmetics_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Evaluation", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="arithmetics_Expression2", type=arithmetics_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Plus", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="arithmetics_Expression5", type=arithmetics_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Plus4", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="arithmetics_Expression7", type=arithmetics_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Minus", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="arithmetics_Expression10", type=arithmetics_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Minus9", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="arithmetics_Expression12", type=arithmetics_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Multi", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="arithmetics_Expression15", type=arithmetics_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Multi14", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="arithmetics_Expression17", type=arithmetics_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Div", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="arithmetics_Expression20", type=arithmetics_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Div19", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_arithmetics_Plus_Expression = Generalization(general=Expression, specific=arithmetics_Plus)
gen_arithmetics_Minus_Expression = Generalization(general=Expression, specific=arithmetics_Minus)
gen_arithmetics_Multi_Expression = Generalization(general=Expression, specific=arithmetics_Multi)
gen_arithmetics_Div_Expression = Generalization(general=Expression, specific=arithmetics_Div)
gen_arithmetics_NumberLiteral_Expression = Generalization(general=Expression, specific=arithmetics_NumberLiteral)

# Domain Model
domain_model = DomainModel(
    name="arithmetics",
    types={arithmetics_Evaluation, arithmetics_Expression, arithmetics_Plus, Expression, arithmetics_Minus, arithmetics_Multi, arithmetics_Div, arithmetics_NumberLiteral},
    associations={expression0, left1, right3, left6, right8, left11, right13, left16, right18},
    generalizations={gen_arithmetics_Plus_Expression, gen_arithmetics_Minus_Expression, gen_arithmetics_Multi_Expression, gen_arithmetics_Div_Expression, gen_arithmetics_NumberLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)