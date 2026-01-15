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
            EnumerationLiteral(name="Arc"),
			EnumerationLiteral(name="ReadArc")
    }
)

# Classes
PetriNet_Place = Class(name="PetriNet::Place")
PetriElement = Class(name="PetriElement")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_PetriElement = Class(name="PetriNet::PetriElement")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")

# PetriNet_Place class attributes and methods
PetriNet_Place_nbJetons: Property = Property(name="nbJetons", type=IntegerType)
PetriNet_Place.attributes={PetriNet_Place_nbJetons}

# PetriElement class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_poids: Property = Property(name="poids", type=IntegerType)
PetriNet_Arc_arcType: Property = Property(name="arcType", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_arcType, PetriNet_Arc_poids}

# PetriNet_PetriElement class attributes and methods
PetriNet_PetriElement_nom: Property = Property(name="nom", type=StringType)
PetriNet_PetriElement.attributes={PetriNet_PetriElement_nom}

# PetriNet_PetriNet class attributes and methods
PetriNet_PetriNet_name: Property = Property(name="name", type=StringType)
PetriNet_PetriNet.attributes={PetriNet_PetriNet_name}

# Relationships
dbt0: BinaryAssociation = BinaryAssociation(
    name="dbt0",
    ends={
        Property(name="PetriNet_PetriElement", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc", type=PetriNet_PetriElement, multiplicity=Multiplicity(1, 1))
    }
)
fin1: BinaryAssociation = BinaryAssociation(
    name="fin1",
    ends={
        Property(name="PetriNet_PetriElement3", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc2", type=PetriNet_PetriElement, multiplicity=Multiplicity(1, 1))
    }
)
arcs4: BinaryAssociation = BinaryAssociation(
    name="arcs4",
    ends={
        Property(name="PetriNet_Arc5", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petriElements6: BinaryAssociation = BinaryAssociation(
    name="petriElements6",
    ends={
        Property(name="PetriNet_PetriElement8", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet7", type=PetriNet_PetriElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_Place_PetriElement = Generalization(general=PetriElement, specific=PetriNet_Place)
gen_PetriNet_Transition_PetriElement = Generalization(general=PetriElement, specific=PetriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, PetriElement, PetriNet_Transition, PetriNet_Arc, PetriNet_PetriElement, PetriNet_PetriNet, ArcType},
    associations={dbt0, fin1, arcs4, petriElements6},
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