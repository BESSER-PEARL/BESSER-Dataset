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
C: Enumeration = Enumeration(
    name="C",
    literals={
            EnumerationLiteral(name="X"),
			EnumerationLiteral(name="Y"),
			EnumerationLiteral(name="Z")
    }
)

# Classes
fsm_Transition = Class(name="fsm::Transition")

# fsm_Transition class attributes and methods
fsm_Transition_a: Property = Property(name="a", type=StringType)
fsm_Transition_b: Property = Property(name="b", type=StringType)
fsm_Transition_c: Property = Property(name="c", type=StringType)
fsm_Transition_m_foo: Method = Method(name="foo", parameters={Parameter(name='arg1'), Parameter(name='arg2')}, type=StringType)
fsm_Transition.attributes={fsm_Transition_c, fsm_Transition_a, fsm_Transition_b}
fsm_Transition.methods={fsm_Transition_m_foo}

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition, C},
    associations={},
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