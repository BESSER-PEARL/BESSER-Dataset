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
fsa_Transition = Class(name="fsa::Transition")
fsa_State = Class(name="fsa::State")
fsa_FSA = Class(name="fsa::FSA")

# fsa_Transition class attributes and methods
fsa_Transition_description: Property = Property(name="description", type=StringType)
fsa_Transition.attributes={fsa_Transition_description}

# fsa_State class attributes and methods
fsa_State_temporalProperties: Property = Property(name="temporalProperties", type=StringType)
fsa_State_name: Property = Property(name="name", type=StringType)
fsa_State_final: Property = Property(name="final", type=BooleanType)
fsa_State.attributes={fsa_State_name, fsa_State_temporalProperties, fsa_State_final}

# fsa_FSA class attributes and methods
fsa_FSA_temporalFormula: Property = Property(name="temporalFormula", type=StringType)
fsa_FSA.attributes={fsa_FSA_temporalFormula}

# Relationships
fsa0: BinaryAssociation = BinaryAssociation(
    name="fsa0",
    ends={
        Property(name="fsa_FSA", type=fsa_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_State", type=fsa_FSA, multiplicity=Multiplicity(1, 1))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="fsa_State2", type=fsa_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_Transition", type=fsa_State, multiplicity=Multiplicity(1, 1))
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="fsa_State5", type=fsa_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_Transition4", type=fsa_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="fsa_Transition8", type=fsa_FSA, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_FSA7", type=fsa_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState9: BinaryAssociation = BinaryAssociation(
    name="initialState9",
    ends={
        Property(name="fsa_State11", type=fsa_FSA, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_FSA10", type=fsa_State, multiplicity=Multiplicity(1, 1))
    }
)
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="fsa_State14", type=fsa_FSA, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_FSA13", type=fsa_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsa",
    types={fsa_Transition, fsa_State, fsa_FSA},
    associations={fsa0, to1, from3, transitions6, initialState9, states12},
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