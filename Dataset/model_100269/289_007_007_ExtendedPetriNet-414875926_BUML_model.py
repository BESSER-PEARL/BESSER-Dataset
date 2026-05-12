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
extendedpetrinet_InteractiveInput = Class(name="extendedpetrinet_InteractiveInput")
extendedpetrinet_ExtendedPetriNet = Class(name="extendedpetrinet_ExtendedPetriNet")
PetriNetType = Class(name="PetriNetType")
extendedpetrinet_Arc = Class(name="extendedpetrinet_Arc")
Arc = Class(name="Arc")
extendedpetrinet_Identity = Class(name="extendedpetrinet_Identity")
extendedpetrinet_Place = Class(name="extendedpetrinet_Place")
Place = Class(name="Place")
extendedpetrinet_AnimationLabel = Class(name="extendedpetrinet_AnimationLabel")
extendedpetrinet_Token = Class(name="extendedpetrinet_Token")
extendedpetrinet_InputPlaceAppearance = Class(name="extendedpetrinet_InputPlaceAppearance")
extendedpetrinet_GeometryLabel = Class(name="extendedpetrinet_GeometryLabel")
Attribute = Class(name="Attribute")
Label = Class(name="Label")
StructuredLabel = Class(name="StructuredLabel")
extendedpetrinet_Animation = Class(name="extendedpetrinet_Animation")

# extendedpetrinet_InteractiveInput class attributes and methods
extendedpetrinet_InteractiveInput_text: Property = Property(name="text", type=BooleanType)
extendedpetrinet_InteractiveInput.attributes={extendedpetrinet_InteractiveInput_text}

# extendedpetrinet_ExtendedPetriNet class attributes and methods

# PetriNetType class attributes and methods

# extendedpetrinet_Arc class attributes and methods

# Arc class attributes and methods

# extendedpetrinet_Identity class attributes and methods
extendedpetrinet_Identity_text: Property = Property(name="text", type=IntegerType)
extendedpetrinet_Identity.attributes={extendedpetrinet_Identity_text}

# extendedpetrinet_Place class attributes and methods

# Place class attributes and methods

# extendedpetrinet_AnimationLabel class attributes and methods

# extendedpetrinet_Token class attributes and methods
extendedpetrinet_Token_text: Property = Property(name="text", type=StringType)
extendedpetrinet_Token.attributes={extendedpetrinet_Token_text}

# extendedpetrinet_InputPlaceAppearance class attributes and methods
extendedpetrinet_InputPlaceAppearance_text: Property = Property(name="text", type=StringType)
extendedpetrinet_InputPlaceAppearance.attributes={extendedpetrinet_InputPlaceAppearance_text}

# extendedpetrinet_GeometryLabel class attributes and methods
extendedpetrinet_GeometryLabel_text: Property = Property(name="text", type=StringType)
extendedpetrinet_GeometryLabel.attributes={extendedpetrinet_GeometryLabel_text}

# Attribute class attributes and methods

# Label class attributes and methods

# StructuredLabel class attributes and methods

# extendedpetrinet_Animation class attributes and methods

# Relationships
interactiveInput1: BinaryAssociation = BinaryAssociation(
    name="interactiveInput1",
    ends={
        Property(name="extendedpetrinet_InteractiveInput", type=extendedpetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_Place", type=extendedpetrinet_InteractiveInput, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identity0: BinaryAssociation = BinaryAssociation(
    name="identity0",
    ends={
        Property(name="extendedpetrinet_Identity", type=extendedpetrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_Arc", type=extendedpetrinet_Identity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
animations2: BinaryAssociation = BinaryAssociation(
    name="animations2",
    ends={
        Property(name="extendedpetrinet_AnimationLabel", type=extendedpetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_Place3", type=extendedpetrinet_AnimationLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokens4: BinaryAssociation = BinaryAssociation(
    name="tokens4",
    ends={
        Property(name="extendedpetrinet_Token", type=extendedpetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_Place5", type=extendedpetrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appearance6: BinaryAssociation = BinaryAssociation(
    name="appearance6",
    ends={
        Property(name="extendedpetrinet_InputPlaceAppearance", type=extendedpetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_Place7", type=extendedpetrinet_InputPlaceAppearance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
geometryLabel8: BinaryAssociation = BinaryAssociation(
    name="geometryLabel8",
    ends={
        Property(name="extendedpetrinet_GeometryLabel", type=extendedpetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_Place9", type=extendedpetrinet_GeometryLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure10: BinaryAssociation = BinaryAssociation(
    name="structure10",
    ends={
        Property(name="extendedpetrinet_Animation", type=extendedpetrinet_AnimationLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedpetrinet_AnimationLabel11", type=extendedpetrinet_Animation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_extendedpetrinet_ExtendedPetriNet_PetriNetType = Generalization(general=PetriNetType, specific=extendedpetrinet_ExtendedPetriNet)
gen_extendedpetrinet_Arc_Arc = Generalization(general=Arc, specific=extendedpetrinet_Arc)
gen_extendedpetrinet_Place_Place = Generalization(general=Place, specific=extendedpetrinet_Place)
gen_extendedpetrinet_InputPlaceAppearance_Label = Generalization(general=Label, specific=extendedpetrinet_InputPlaceAppearance)
gen_extendedpetrinet_Identity_Attribute = Generalization(general=Attribute, specific=extendedpetrinet_Identity)
gen_extendedpetrinet_InteractiveInput_Attribute = Generalization(general=Attribute, specific=extendedpetrinet_InteractiveInput)
gen_extendedpetrinet_Token_Label = Generalization(general=Label, specific=extendedpetrinet_Token)
gen_extendedpetrinet_AnimationLabel_StructuredLabel = Generalization(general=StructuredLabel, specific=extendedpetrinet_AnimationLabel)
gen_extendedpetrinet_GeometryLabel_Label = Generalization(general=Label, specific=extendedpetrinet_GeometryLabel)

# Domain Model
domain_model = DomainModel(
    name="extendedpetrinet",
    types={extendedpetrinet_InteractiveInput, extendedpetrinet_ExtendedPetriNet, PetriNetType, extendedpetrinet_Arc, Arc, extendedpetrinet_Identity, extendedpetrinet_Place, Place, extendedpetrinet_AnimationLabel, extendedpetrinet_Token, extendedpetrinet_InputPlaceAppearance, extendedpetrinet_GeometryLabel, Attribute, Label, StructuredLabel, extendedpetrinet_Animation},
    associations={interactiveInput1, identity0, animations2, tokens4, appearance6, geometryLabel8, structure10},
    generalizations={gen_extendedpetrinet_ExtendedPetriNet_PetriNetType, gen_extendedpetrinet_Arc_Arc, gen_extendedpetrinet_Place_Place, gen_extendedpetrinet_InputPlaceAppearance_Label, gen_extendedpetrinet_Identity_Attribute, gen_extendedpetrinet_InteractiveInput_Attribute, gen_extendedpetrinet_Token_Label, gen_extendedpetrinet_AnimationLabel_StructuredLabel, gen_extendedpetrinet_GeometryLabel_Label},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)