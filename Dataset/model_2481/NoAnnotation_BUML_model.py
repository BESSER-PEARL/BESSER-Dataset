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
fsm_NoAnnotationSuper = Class(name="fsm::NoAnnotationSuper")
fsm_NoAnnotation = Class(name="fsm::NoAnnotation")
NoAnnotationSuper = Class(name="NoAnnotationSuper")
fsm_State = Class(name="fsm::State")
fsm_FSM = Class(name="fsm::FSM")
fsm_Transition = Class(name="fsm::Transition")

# fsm_NoAnnotationSuper class attributes and methods

# fsm_NoAnnotation class attributes and methods
fsm_NoAnnotation_a: Property = Property(name="a", type=StringType)
fsm_NoAnnotation_b: Property = Property(name="b", type=StringType)
fsm_NoAnnotation_m_j: Method = Method(name="j", parameters={Parameter(name='arg0'), Parameter(name='arg1')})
fsm_NoAnnotation_m_k: Method = Method(name="k", parameters={Parameter(name='arg0')}, type=StringType)
fsm_NoAnnotation.attributes={fsm_NoAnnotation_b, fsm_NoAnnotation_a}
fsm_NoAnnotation.methods={fsm_NoAnnotation_m_j, fsm_NoAnnotation_m_k}

# NoAnnotationSuper class attributes and methods

# fsm_State class attributes and methods

# fsm_FSM class attributes and methods

# fsm_Transition class attributes and methods

# Relationships
ls0: BinaryAssociation = BinaryAssociation(
    name="ls0",
    ends={
        Property(name="fsm_State", type=fsm_NoAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_NoAnnotation", type=fsm_State, multiplicity=Multiplicity(0, 9999))
    }
)
f1: BinaryAssociation = BinaryAssociation(
    name="f1",
    ends={
        Property(name="fsm_FSM", type=fsm_NoAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_NoAnnotation2", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_fsm_NoAnnotation_NoAnnotationSuper = Generalization(general=NoAnnotationSuper, specific=fsm_NoAnnotation)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_NoAnnotationSuper, fsm_NoAnnotation, NoAnnotationSuper, fsm_State, fsm_FSM, fsm_Transition},
    associations={ls0, f1},
    generalizations={gen_fsm_NoAnnotation_NoAnnotationSuper},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)