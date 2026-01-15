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
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
IdentifiableElement = Class(name="IdentifiableElement")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
PetriNet_Type = Class(name="PetriNet::Type")
PetriNet_PrimitiveAttribute = Class(name="PetriNet::PrimitiveAttribute")
PetriNet_Token = Class(name="PetriNet::Token")
PetriNet_PlaceToTransArc = Class(name="PetriNet::PlaceToTransArc")
Arc = Class(name="Arc")
PetriNet_TransToPlaceArc = Class(name="PetriNet::TransToPlaceArc")
PetriNet_IdentifiableElement = Class(name="PetriNet::IdentifiableElement", is_abstract=True)

# PetriNet_PetriNet class attributes and methods

# IdentifiableElement class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_Type class attributes and methods
PetriNet_Type_name: Property = Property(name="name", type=StringType)
PetriNet_Type.attributes={PetriNet_Type_name}

# PetriNet_PrimitiveAttribute class attributes and methods
PetriNet_PrimitiveAttribute_name: Property = Property(name="name", type=StringType)
PetriNet_PrimitiveAttribute_primType: Property = Property(name="primType", type=StringType)
PetriNet_PrimitiveAttribute.attributes={PetriNet_PrimitiveAttribute_name, PetriNet_PrimitiveAttribute_primType}

# PetriNet_Token class attributes and methods
PetriNet_Token_values: Property = Property(name="values", type=StringType)
PetriNet_Token.attributes={PetriNet_Token_values}

# PetriNet_PlaceToTransArc class attributes and methods

# Arc class attributes and methods

# PetriNet_TransToPlaceArc class attributes and methods

# PetriNet_IdentifiableElement class attributes and methods
PetriNet_IdentifiableElement_name: Property = Property(name="name", type=StringType)
PetriNet_IdentifiableElement_author: Property = Property(name="author", type=StringType)
PetriNet_IdentifiableElement.attributes={PetriNet_IdentifiableElement_name, PetriNet_IdentifiableElement_author}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="PetriNet_Place", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="PetriNet_Transition", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="PetriNet_Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet4", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types5: BinaryAssociation = BinaryAssociation(
    name="types5",
    ends={
        Property(name="PetriNet_Type", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet6", type=PetriNet_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components7: BinaryAssociation = BinaryAssociation(
    name="components7",
    ends={
        Property(name="PetriNet_PrimitiveAttribute", type=PetriNet_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Type8", type=PetriNet_PrimitiveAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="PetriNet_Type13", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place12", type=PetriNet_Type, multiplicity=Multiplicity(1, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="PetriNet_Place15", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PlaceToTransArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="PetriNet_Transition18", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PlaceToTransArc17", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="PetriNet_Transition20", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TransToPlaceArc", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="PetriNet_Place23", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TransToPlaceArc22", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
tokens9: BinaryAssociation = BinaryAssociation(
    name="tokens9",
    ends={
        Property(name="PetriNet_Token", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place10", type=PetriNet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_PetriNet_IdentifiableElement = Generalization(general=IdentifiableElement, specific=PetriNet_PetriNet)
gen_PetriNet_Transition_IdentifiableElement = Generalization(general=IdentifiableElement, specific=PetriNet_Transition)
gen_PetriNet_PlaceToTransArc_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransArc)
gen_PetriNet_TransToPlaceArc_Arc = Generalization(general=Arc, specific=PetriNet_TransToPlaceArc)
gen_PetriNet_Place_IdentifiableElement = Generalization(general=IdentifiableElement, specific=PetriNet_Place)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNet, IdentifiableElement, PetriNet_Place, PetriNet_Transition, PetriNet_Arc, PetriNet_Type, PetriNet_PrimitiveAttribute, PetriNet_Token, PetriNet_PlaceToTransArc, Arc, PetriNet_TransToPlaceArc, PetriNet_IdentifiableElement},
    associations={places0, transitions1, arcs3, types5, components7, type11, source14, target16, source19, target21, tokens9},
    generalizations={gen_PetriNet_PetriNet_IdentifiableElement, gen_PetriNet_Transition_IdentifiableElement, gen_PetriNet_PlaceToTransArc_Arc, gen_PetriNet_TransToPlaceArc_Arc, gen_PetriNet_Place_IdentifiableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)