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
Kind: Enumeration = Enumeration(
    name="Kind",
    literals={
            EnumerationLiteral(name="Nice"),
			EnumerationLiteral(name="NotNice")
    }
)

# Classes
test_StateMachine = Class(name="test::StateMachine")
NamedElement = Class(name="NamedElement")
test_Transition = Class(name="test::Transition")
test_State = Class(name="test::State")
test_NamedElement = Class(name="test::NamedElement", is_abstract=True)

# test_StateMachine class attributes and methods
test_StateMachine_name: Property = Property(name="name", type=StringType)
test_StateMachine.attributes={test_StateMachine_name}

# NamedElement class attributes and methods

# test_Transition class attributes and methods
test_Transition_m_fire: Method = Method(name="fire", parameters={}, type=BooleanType)
test_Transition.methods={test_Transition_m_fire}

# test_State class attributes and methods
test_State_kind: Property = Property(name="kind", type=StringType)
test_State.attributes={test_State_kind}

# test_NamedElement class attributes and methods

# Relationships
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="test_State5", type=test_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Transition4", type=test_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="test_Transition", type=test_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="test_StateMachine", type=test_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="test_State", type=test_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="test_StateMachine2", type=test_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="test_State8", type=test_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Transition7", type=test_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_test_Transition_NamedElement = Generalization(general=NamedElement, specific=test_Transition)
gen_test_StateMachine_NamedElement = Generalization(general=NamedElement, specific=test_StateMachine)
gen_test_State_NamedElement = Generalization(general=NamedElement, specific=test_State)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_StateMachine, NamedElement, test_Transition, test_State, test_NamedElement, Kind},
    associations={source3, transitions0, states1, target6},
    generalizations={gen_test_Transition_NamedElement, gen_test_StateMachine_NamedElement, gen_test_State_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)