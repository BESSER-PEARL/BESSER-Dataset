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
PetriNet_Transition = Class(name="PetriNet_Transition")
PetriNet_ReseauPetri = Class(name="PetriNet_ReseauPetri")
PetriNet_PetriElement = Class(name="PetriNet_PetriElement", is_abstract=True)
PetriNet_Place = Class(name="PetriNet_Place")
Noeud = Class(name="Noeud")
PetriNet_Arc = Class(name="PetriNet_Arc")
PetriElement = Class(name="PetriElement")
PetriNet_Noeud = Class(name="PetriNet_Noeud", is_abstract=True)

# PetriNet_Transition class attributes and methods

# PetriNet_ReseauPetri class attributes and methods
PetriNet_ReseauPetri_name: Property = Property(name="name", type=StringType)
PetriNet_ReseauPetri.attributes={PetriNet_ReseauPetri_name}

# PetriNet_PetriElement class attributes and methods

# PetriNet_Place class attributes and methods
PetriNet_Place_jeton: Property = Property(name="jeton", type=IntegerType)
PetriNet_Place.attributes={PetriNet_Place_jeton}

# Noeud class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_isReadArc: Property = Property(name="isReadArc", type=BooleanType)
PetriNet_Arc_poids: Property = Property(name="poids", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_isReadArc, PetriNet_Arc_poids}

# PetriElement class attributes and methods

# PetriNet_Noeud class attributes and methods
PetriNet_Noeud_name: Property = Property(name="name", type=StringType)
PetriNet_Noeud.attributes={PetriNet_Noeud_name}

# Relationships
petrielement3: BinaryAssociation = BinaryAssociation(
    name="petrielement3",
    ends={
        Property(name="PetriNet_PetriElement", type=PetriNet_ReseauPetri, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_ReseauPetri", type=PetriNet_PetriElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reseauPetri4: BinaryAssociation = BinaryAssociation(
    name="reseauPetri4",
    ends={
        Property(name="PetriNet_ReseauPetri6", type=PetriNet_PetriElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriElement5", type=PetriNet_ReseauPetri, multiplicity=Multiplicity(0, 1))
    }
)
linksToPredecessors7: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors7",
    ends={
        Property(name="Arc", type=PetriNet_Noeud, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
successor0: BinaryAssociation = BinaryAssociation(
    name="successor0",
    ends={
        Property(name="Noeud", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=PetriNet_Noeud, multiplicity=Multiplicity(1, 1))
    }
)
predecessor1: BinaryAssociation = BinaryAssociation(
    name="predecessor1",
    ends={
        Property(name="Noeud2", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="LinksToSuccessors", type=PetriNet_Noeud, multiplicity=Multiplicity(1, 1))
    }
)
LinksToSuccessors8: BinaryAssociation = BinaryAssociation(
    name="LinksToSuccessors8",
    ends={
        Property(name="Arc9", type=PetriNet_Noeud, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNet_Transition_Noeud = Generalization(general=Noeud, specific=PetriNet_Transition)
gen_PetriNet_Noeud_PetriElement = Generalization(general=PetriElement, specific=PetriNet_Noeud)
gen_PetriNet_Place_Noeud = Generalization(general=Noeud, specific=PetriNet_Place)
gen_PetriNet_Arc_PetriElement = Generalization(general=PetriElement, specific=PetriNet_Arc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Transition, PetriNet_ReseauPetri, PetriNet_PetriElement, PetriNet_Place, Noeud, PetriNet_Arc, PetriElement, PetriNet_Noeud},
    associations={petrielement3, reseauPetri4, linksToPredecessors7, successor0, predecessor1, LinksToSuccessors8},
    generalizations={gen_PetriNet_Transition_Noeud, gen_PetriNet_Noeud_PetriElement, gen_PetriNet_Place_Noeud, gen_PetriNet_Arc_PetriElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)