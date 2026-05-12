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
petrinet_ExtendedPetriNet = Class(name="petrinet_ExtendedPetriNet")
PetriNetType = Class(name="PetriNetType")
petrinet_Place = Class(name="petrinet_Place")
Place = Class(name="Place")
petrinet_GeometryLabel = Class(name="petrinet_GeometryLabel")
petrinet_Token = Class(name="petrinet_Token")
petrinet_InputPlace = Class(name="petrinet_InputPlace")
Label = Class(name="Label")
StructuredLabel = Class(name="StructuredLabel")
petrinet_Animation = Class(name="petrinet_Animation")
Attribute = Class(name="Attribute")
petrinet_Arc = Class(name="petrinet_Arc")
Arc = Class(name="Arc")
petrinet_Identity = Class(name="petrinet_Identity")
petrinet_AnimationLabel = Class(name="petrinet_AnimationLabel")

# petrinet_ExtendedPetriNet class attributes and methods

# PetriNetType class attributes and methods

# petrinet_Place class attributes and methods

# Place class attributes and methods

# petrinet_GeometryLabel class attributes and methods
petrinet_GeometryLabel_text: Property = Property(name="text", type=StringType)
petrinet_GeometryLabel.attributes={petrinet_GeometryLabel_text}

# petrinet_Token class attributes and methods
petrinet_Token_text: Property = Property(name="text", type=StringType)
petrinet_Token.attributes={petrinet_Token_text}

# petrinet_InputPlace class attributes and methods
petrinet_InputPlace_text: Property = Property(name="text", type=BooleanType)
petrinet_InputPlace.attributes={petrinet_InputPlace_text}

# Label class attributes and methods

# StructuredLabel class attributes and methods

# petrinet_Animation class attributes and methods

# Attribute class attributes and methods

# petrinet_Arc class attributes and methods

# Arc class attributes and methods

# petrinet_Identity class attributes and methods
petrinet_Identity_text: Property = Property(name="text", type=StringType)
petrinet_Identity.attributes={petrinet_Identity_text}

# petrinet_AnimationLabel class attributes and methods

# Relationships
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="petrinet_Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place4", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPlaceLabel5: BinaryAssociation = BinaryAssociation(
    name="inputPlaceLabel5",
    ends={
        Property(name="petrinet_InputPlace", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place6", type=petrinet_InputPlace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure7: BinaryAssociation = BinaryAssociation(
    name="structure7",
    ends={
        Property(name="petrinet_Animation", type=petrinet_AnimationLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_AnimationLabel8", type=petrinet_Animation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identity9: BinaryAssociation = BinaryAssociation(
    name="identity9",
    ends={
        Property(name="petrinet_Identity", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc", type=petrinet_Identity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
geometryLabel0: BinaryAssociation = BinaryAssociation(
    name="geometryLabel0",
    ends={
        Property(name="petrinet_GeometryLabel", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_GeometryLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
animationLabel1: BinaryAssociation = BinaryAssociation(
    name="animationLabel1",
    ends={
        Property(name="petrinet_AnimationLabel", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place2", type=petrinet_AnimationLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_petrinet_ExtendedPetriNet_PetriNetType = Generalization(general=PetriNetType, specific=petrinet_ExtendedPetriNet)
gen_petrinet_Place_Place = Generalization(general=Place, specific=petrinet_Place)
gen_petrinet_GeometryLabel_Label = Generalization(general=Label, specific=petrinet_GeometryLabel)
gen_petrinet_AnimationLabel_StructuredLabel = Generalization(general=StructuredLabel, specific=petrinet_AnimationLabel)
gen_petrinet_Token_Attribute = Generalization(general=Attribute, specific=petrinet_Token)
gen_petrinet_Arc_Arc = Generalization(general=Arc, specific=petrinet_Arc)
gen_petrinet_Identity_Attribute = Generalization(general=Attribute, specific=petrinet_Identity)
gen_petrinet_InputPlace_Attribute = Generalization(general=Attribute, specific=petrinet_InputPlace)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_ExtendedPetriNet, PetriNetType, petrinet_Place, Place, petrinet_GeometryLabel, petrinet_Token, petrinet_InputPlace, Label, StructuredLabel, petrinet_Animation, Attribute, petrinet_Arc, Arc, petrinet_Identity, petrinet_AnimationLabel},
    associations={tokens3, inputPlaceLabel5, structure7, identity9, geometryLabel0, animationLabel1},
    generalizations={gen_petrinet_ExtendedPetriNet_PetriNetType, gen_petrinet_Place_Place, gen_petrinet_GeometryLabel_Label, gen_petrinet_AnimationLabel_StructuredLabel, gen_petrinet_Token_Attribute, gen_petrinet_Arc_Arc, gen_petrinet_Identity_Attribute, gen_petrinet_InputPlace_Attribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)