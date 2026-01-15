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
TypeArc: Enumeration = Enumeration(
    name="TypeArc",
    literals={
            EnumerationLiteral(name="ArcSimple"),
			EnumerationLiteral(name="ReadArc")
    }
)

# Classes
petriNet_Transition = Class(name="petriNet::Transition")
petriNet_Noeud = Class(name="petriNet::Noeud", is_abstract=True)
PetriNetElt = Class(name="PetriNetElt")
petriNet_Arc = Class(name="petriNet::Arc")
petriNet_Place = Class(name="petriNet::Place")
Noeud = Class(name="Noeud")
petriNet_PetriNet = Class(name="petriNet::PetriNet")
petriNet_PetriNetElt = Class(name="petriNet::PetriNetElt", is_abstract=True)

# petriNet_Transition class attributes and methods

# petriNet_Noeud class attributes and methods
petriNet_Noeud_name: Property = Property(name="name", type=StringType)
petriNet_Noeud.attributes={petriNet_Noeud_name}

# PetriNetElt class attributes and methods

# petriNet_Arc class attributes and methods
petriNet_Arc_poids: Property = Property(name="poids", type=IntegerType)
petriNet_Arc_typeArc: Property = Property(name="typeArc", type=StringType)
petriNet_Arc.attributes={petriNet_Arc_typeArc, petriNet_Arc_poids}

# petriNet_Place class attributes and methods
petriNet_Place_jeton: Property = Property(name="jeton", type=IntegerType)
petriNet_Place.attributes={petriNet_Place_jeton}

# Noeud class attributes and methods

# petriNet_PetriNet class attributes and methods
petriNet_PetriNet_name: Property = Property(name="name", type=StringType)
petriNet_PetriNet.attributes={petriNet_PetriNet_name}

# petriNet_PetriNetElt class attributes and methods

# Relationships
noeudsSuccesseurs0: BinaryAssociation = BinaryAssociation(
    name="noeudsSuccesseurs0",
    ends={
        Property(name="Arc", type=petriNet_Noeud, multiplicity=Multiplicity(1, 1)),
        Property(name="predecesseur", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
noeudsPredecesseurs1: BinaryAssociation = BinaryAssociation(
    name="noeudsPredecesseurs1",
    ends={
        Property(name="Arc2", type=petriNet_Noeud, multiplicity=Multiplicity(1, 1)),
        Property(name="successeur", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
net6: BinaryAssociation = BinaryAssociation(
    name="net6",
    ends={
        Property(name="petriNet_PetriNet", type=petriNet_PetriNetElt, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_PetriNetElt", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
petrinetelt7: BinaryAssociation = BinaryAssociation(
    name="petrinetelt7",
    ends={
        Property(name="petriNet_PetriNetElt9", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_PetriNet8", type=petriNet_PetriNetElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecesseur3: BinaryAssociation = BinaryAssociation(
    name="predecesseur3",
    ends={
        Property(name="Noeud", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="noeudsSuccesseurs", type=petriNet_Noeud, multiplicity=Multiplicity(0, 1))
    }
)
successeur4: BinaryAssociation = BinaryAssociation(
    name="successeur4",
    ends={
        Property(name="Noeud5", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="noeudsPredecesseurs", type=petriNet_Noeud, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petriNet_Transition_Noeud = Generalization(general=Noeud, specific=petriNet_Transition)
gen_petriNet_Noeud_PetriNetElt = Generalization(general=PetriNetElt, specific=petriNet_Noeud)
gen_petriNet_Arc_PetriNetElt = Generalization(general=PetriNetElt, specific=petriNet_Arc)
gen_petriNet_Place_Noeud = Generalization(general=Noeud, specific=petriNet_Place)

# Domain Model
domain_model = DomainModel(
    name="petriNet",
    types={petriNet_Transition, petriNet_Noeud, PetriNetElt, petriNet_Arc, petriNet_Place, Noeud, petriNet_PetriNet, petriNet_PetriNetElt, TypeArc},
    associations={noeudsSuccesseurs0, noeudsPredecesseurs1, net6, petrinetelt7, predecesseur3, successeur4},
    generalizations={gen_petriNet_Transition_Noeud, gen_petriNet_Noeud_PetriNetElt, gen_petriNet_Arc_PetriNetElt, gen_petriNet_Place_Noeud},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)