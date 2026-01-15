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
petrinet_Place = Class(name="petrinet::Place")
Element = Class(name="Element")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_ArcSortant = Class(name="petrinet::ArcSortant")
petrinet_ArcEntrant = Class(name="petrinet::ArcEntrant")
Arc = Class(name="Arc")
petrinet_ReadArc = Class(name="petrinet::ReadArc")
ArcSortant = Class(name="ArcSortant")
petrinet_Element = Class(name="petrinet::Element", is_abstract=True)
petrinet_Reseau = Class(name="petrinet::Reseau")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)

# petrinet_Place class attributes and methods
petrinet_Place_jetons: Property = Property(name="jetons", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_jetons}

# Element class attributes and methods

# petrinet_Transition class attributes and methods

# petrinet_ArcSortant class attributes and methods

# petrinet_ArcEntrant class attributes and methods

# Arc class attributes and methods

# petrinet_ReadArc class attributes and methods

# ArcSortant class attributes and methods

# petrinet_Element class attributes and methods
petrinet_Element_nom: Property = Property(name="nom", type=StringType)
petrinet_Element.attributes={petrinet_Element_nom}

# petrinet_Reseau class attributes and methods
petrinet_Reseau_nom: Property = Property(name="nom", type=StringType)
petrinet_Reseau.attributes={petrinet_Reseau_nom}

# petrinet_Arc class attributes and methods
petrinet_Arc_nbJetons: Property = Property(name="nbJetons", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_nbJetons}

# Relationships
predecesseurs0: BinaryAssociation = BinaryAssociation(
    name="predecesseurs0",
    ends={
        Property(name="ArcSortant", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="successeur", type=petrinet_ArcSortant, multiplicity=Multiplicity(1, 9999))
    }
)
successeurs1: BinaryAssociation = BinaryAssociation(
    name="successeurs1",
    ends={
        Property(name="ArcEntrant", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecesseur", type=petrinet_ArcEntrant, multiplicity=Multiplicity(1, 9999))
    }
)
successeur2: BinaryAssociation = BinaryAssociation(
    name="successeur2",
    ends={
        Property(name="Transition", type=petrinet_ArcSortant, multiplicity=Multiplicity(1, 1)),
        Property(name="predecesseurs", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
predecesseur3: BinaryAssociation = BinaryAssociation(
    name="predecesseur3",
    ends={
        Property(name="petrinet_Place", type=petrinet_ArcSortant, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_ArcSortant", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
predecesseur6: BinaryAssociation = BinaryAssociation(
    name="predecesseur6",
    ends={
        Property(name="Transition7", type=petrinet_ArcEntrant, multiplicity=Multiplicity(1, 1)),
        Property(name="successeurs", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
elements8: BinaryAssociation = BinaryAssociation(
    name="elements8",
    ends={
        Property(name="petrinet_Element", type=petrinet_Reseau, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Reseau", type=petrinet_Element, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arcs9: BinaryAssociation = BinaryAssociation(
    name="arcs9",
    ends={
        Property(name="petrinet_Arc", type=petrinet_Reseau, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Reseau10", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successeur4: BinaryAssociation = BinaryAssociation(
    name="successeur4",
    ends={
        Property(name="petrinet_Place5", type=petrinet_ArcEntrant, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_ArcEntrant", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Place_Element = Generalization(general=Element, specific=petrinet_Place)
gen_petrinet_Transition_Element = Generalization(general=Element, specific=petrinet_Transition)
gen_petrinet_ArcSortant_Arc = Generalization(general=Arc, specific=petrinet_ArcSortant)
gen_petrinet_ReadArc_ArcSortant = Generalization(general=ArcSortant, specific=petrinet_ReadArc)
gen_petrinet_ArcEntrant_Arc = Generalization(general=Arc, specific=petrinet_ArcEntrant)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Place, Element, petrinet_Transition, petrinet_ArcSortant, petrinet_ArcEntrant, Arc, petrinet_ReadArc, ArcSortant, petrinet_Element, petrinet_Reseau, petrinet_Arc},
    associations={predecesseurs0, successeurs1, successeur2, predecesseur3, predecesseur6, elements8, arcs9, successeur4},
    generalizations={gen_petrinet_Place_Element, gen_petrinet_Transition_Element, gen_petrinet_ArcSortant_Arc, gen_petrinet_ReadArc_ArcSortant, gen_petrinet_ArcEntrant_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)