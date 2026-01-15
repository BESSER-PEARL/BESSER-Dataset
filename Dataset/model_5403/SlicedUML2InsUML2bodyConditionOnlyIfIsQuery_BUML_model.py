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
UML2_DurationConstraint = Class(name="UML2::DurationConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
UML2_TimeConstraint = Class(name="UML2::TimeConstraint")
UML2_Constraint = Class(name="UML2::Constraint")
UML2_Operation = Class(name="UML2::Operation")
UML2_InteractionConstraint = Class(name="UML2::InteractionConstraint")
Constraint = Class(name="Constraint")
UML2_IntervalConstraint = Class(name="UML2::IntervalConstraint")

# UML2_DurationConstraint class attributes and methods

# IntervalConstraint class attributes and methods

# UML2_TimeConstraint class attributes and methods

# UML2_Constraint class attributes and methods

# UML2_Operation class attributes and methods
UML2_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
UML2_Operation.attributes={UML2_Operation_isQuery}

# UML2_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# UML2_IntervalConstraint class attributes and methods

# Relationships
bodyCondition0: BinaryAssociation = BinaryAssociation(
    name="bodyCondition0",
    ends={
        Property(name="UML2_Constraint", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation", type=UML2_Constraint, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML2_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2_DurationConstraint)
gen_UML2_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2_TimeConstraint)
gen_UML2_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=UML2_InteractionConstraint)
gen_UML2_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=UML2_IntervalConstraint)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_DurationConstraint, IntervalConstraint, UML2_TimeConstraint, UML2_Constraint, UML2_Operation, UML2_InteractionConstraint, Constraint, UML2_IntervalConstraint},
    associations={bodyCondition0},
    generalizations={gen_UML2_DurationConstraint_IntervalConstraint, gen_UML2_TimeConstraint_IntervalConstraint, gen_UML2_InteractionConstraint_Constraint, gen_UML2_IntervalConstraint_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)