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
coom_ComponentOnOffManifest = Class(name="coom::ComponentOnOffManifest")
coom_Version = Class(name="coom::Version")
coom_State = Class(name="coom::State")
coom_Transition = Class(name="coom::Transition")

# coom_ComponentOnOffManifest class attributes and methods
coom_ComponentOnOffManifest_name: Property = Property(name="name", type=StringType)
coom_ComponentOnOffManifest.attributes={coom_ComponentOnOffManifest_name}

# coom_Version class attributes and methods
coom_Version_majorMalue: Property = Property(name="majorMalue", type=IntegerType)
coom_Version_minorValue: Property = Property(name="minorValue", type=IntegerType)
coom_Version.attributes={coom_Version_minorValue, coom_Version_majorMalue}

# coom_State class attributes and methods
coom_State_initial: Property = Property(name="initial", type=BooleanType)
coom_State_name: Property = Property(name="name", type=StringType)
coom_State.attributes={coom_State_name, coom_State_initial}

# coom_Transition class attributes and methods
coom_Transition_name: Property = Property(name="name", type=StringType)
coom_Transition.attributes={coom_Transition_name}

# Relationships
version0: BinaryAssociation = BinaryAssociation(
    name="version0",
    ends={
        Property(name="coom_Version", type=coom_ComponentOnOffManifest, multiplicity=Multiplicity(1, 1)),
        Property(name="coom_ComponentOnOffManifest", type=coom_Version, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="coom_State", type=coom_ComponentOnOffManifest, multiplicity=Multiplicity(1, 1)),
        Property(name="coom_ComponentOnOffManifest2", type=coom_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="coom_Transition", type=coom_ComponentOnOffManifest, multiplicity=Multiplicity(1, 1)),
        Property(name="coom_ComponentOnOffManifest4", type=coom_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromState5: BinaryAssociation = BinaryAssociation(
    name="fromState5",
    ends={
        Property(name="coom_State7", type=coom_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="coom_Transition6", type=coom_State, multiplicity=Multiplicity(0, 1))
    }
)
toState8: BinaryAssociation = BinaryAssociation(
    name="toState8",
    ends={
        Property(name="coom_State10", type=coom_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="coom_Transition9", type=coom_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="coom",
    types={coom_ComponentOnOffManifest, coom_Version, coom_State, coom_Transition},
    associations={version0, states1, transitions3, fromState5, toState8},
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