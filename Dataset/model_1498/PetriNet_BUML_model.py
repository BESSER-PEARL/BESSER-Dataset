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
ArcType: Enumeration = Enumeration(
    name="ArcType",
    literals={
            EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Read_arc")
    }
)

# Classes
PetriNet_Place = Class(name="PetriNet::Place")
PetriElement = Class(name="PetriElement")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_PetriElement = Class(name="PetriNet::PetriElement")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_ReseauPetri = Class(name="PetriNet::ReseauPetri")

# PetriNet_Place class attributes and methods
PetriNet_Place_borne: Property = Property(name="borne", type=StringType)
PetriNet_Place_nbJeton: Property = Property(name="nbJeton", type=StringType)
PetriNet_Place.attributes={PetriNet_Place_nbJeton, PetriNet_Place_borne}

# PetriElement class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_type: Property = Property(name="type", type=StringType)
PetriNet_Arc_poids: Property = Property(name="poids", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_type, PetriNet_Arc_poids}

# PetriNet_PetriElement class attributes and methods
PetriNet_PetriElement_name: Property = Property(name="name", type=StringType)
PetriNet_PetriElement.attributes={PetriNet_PetriElement_name}

# PetriNet_Transition class attributes and methods

# PetriNet_ReseauPetri class attributes and methods
PetriNet_ReseauPetri_name: Property = Property(name="name", type=StringType)
PetriNet_ReseauPetri.attributes={PetriNet_ReseauPetri_name}

# Relationships
fin1: BinaryAssociation = BinaryAssociation(
    name="fin1",
    ends={
        Property(name="PetriNet_PetriElement3", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc2", type=PetriNet_PetriElement, multiplicity=Multiplicity(1, 1))
    }
)
debut0: BinaryAssociation = BinaryAssociation(
    name="debut0",
    ends={
        Property(name="PetriNet_PetriElement", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc", type=PetriNet_PetriElement, multiplicity=Multiplicity(1, 1))
    }
)
arcs6: BinaryAssociation = BinaryAssociation(
    name="arcs6",
    ends={
        Property(name="PetriNet_Arc8", type=PetriNet_ReseauPetri, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_ReseauPetri7", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="PetriNet_PetriElement5", type=PetriNet_ReseauPetri, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_ReseauPetri", type=PetriNet_PetriElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_Place_PetriElement = Generalization(general=PetriElement, specific=PetriNet_Place)
gen_PetriNet_Transition_PetriElement = Generalization(general=PetriElement, specific=PetriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, PetriElement, PetriNet_Arc, PetriNet_PetriElement, PetriNet_Transition, PetriNet_ReseauPetri, ArcType},
    associations={fin1, debut0, arcs6, elements4},
    generalizations={gen_PetriNet_Place_PetriElement, gen_PetriNet_Transition_PetriElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)