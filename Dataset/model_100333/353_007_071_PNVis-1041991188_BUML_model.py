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
OurPNVis_Place = Class(name="OurPNVis_Place")
Place = Class(name="Place")
OurPNVis_Tokens = Class(name="OurPNVis_Tokens")
OurPNVis_CanChange = Class(name="OurPNVis_CanChange")
OurPNVis_Shape = Class(name="OurPNVis_Shape")
OurPNVis_Activities = Class(name="OurPNVis_Activities")
OurPNVis_Geometry = Class(name="OurPNVis_Geometry")
OurPNVis_Transition = Class(name="OurPNVis_Transition")
Transition = Class(name="Transition")
OurPNVis_PNVis = Class(name="OurPNVis_PNVis")
PetriNetType = Class(name="PetriNetType")
OurPNVis_Arc = Class(name="OurPNVis_Arc")
Arc = Class(name="Arc")
OurPNVis_Finished = Class(name="OurPNVis_Finished")
OurPNVis_KeepAnim = Class(name="OurPNVis_KeepAnim")
OurPNVis_ident = Class(name="OurPNVis_ident")
Attribute = Class(name="Attribute")
StructuredLabel = Class(name="StructuredLabel")
OurPNVis_Sequence = Class(name="OurPNVis_Sequence")
Label = Class(name="Label")

# OurPNVis_Place class attributes and methods

# Place class attributes and methods

# OurPNVis_Tokens class attributes and methods
OurPNVis_Tokens_text: Property = Property(name="text", type=StringType)
OurPNVis_Tokens.attributes={OurPNVis_Tokens_text}

# OurPNVis_CanChange class attributes and methods
OurPNVis_CanChange_text: Property = Property(name="text", type=BooleanType)
OurPNVis_CanChange.attributes={OurPNVis_CanChange_text}

# OurPNVis_Shape class attributes and methods
OurPNVis_Shape_text: Property = Property(name="text", type=StringType)
OurPNVis_Shape.attributes={OurPNVis_Shape_text}

# OurPNVis_Activities class attributes and methods

# OurPNVis_Geometry class attributes and methods
OurPNVis_Geometry_text: Property = Property(name="text", type=StringType)
OurPNVis_Geometry.attributes={OurPNVis_Geometry_text}

# OurPNVis_Transition class attributes and methods

# Transition class attributes and methods

# OurPNVis_PNVis class attributes and methods

# PetriNetType class attributes and methods

# OurPNVis_Arc class attributes and methods

# Arc class attributes and methods

# OurPNVis_Finished class attributes and methods
OurPNVis_Finished_text: Property = Property(name="text", type=BooleanType)
OurPNVis_Finished.attributes={OurPNVis_Finished_text}

# OurPNVis_KeepAnim class attributes and methods
OurPNVis_KeepAnim_text: Property = Property(name="text", type=BooleanType)
OurPNVis_KeepAnim.attributes={OurPNVis_KeepAnim_text}

# OurPNVis_ident class attributes and methods
OurPNVis_ident_text: Property = Property(name="text", type=StringType)
OurPNVis_ident.attributes={OurPNVis_ident_text}

# Attribute class attributes and methods

# StructuredLabel class attributes and methods

# OurPNVis_Sequence class attributes and methods

# Label class attributes and methods

# Relationships
tokens5: BinaryAssociation = BinaryAssociation(
    name="tokens5",
    ends={
        Property(name="OurPNVis_Tokens", type=OurPNVis_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Place", type=OurPNVis_Tokens, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
canchange6: BinaryAssociation = BinaryAssociation(
    name="canchange6",
    ends={
        Property(name="OurPNVis_CanChange", type=OurPNVis_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Place7", type=OurPNVis_CanChange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shape8: BinaryAssociation = BinaryAssociation(
    name="shape8",
    ends={
        Property(name="OurPNVis_Shape", type=OurPNVis_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Place9", type=OurPNVis_Shape, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activities10: BinaryAssociation = BinaryAssociation(
    name="activities10",
    ends={
        Property(name="OurPNVis_Activities", type=OurPNVis_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Place11", type=OurPNVis_Activities, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
geo12: BinaryAssociation = BinaryAssociation(
    name="geo12",
    ends={
        Property(name="OurPNVis_Geometry", type=OurPNVis_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Place13", type=OurPNVis_Geometry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finished0: BinaryAssociation = BinaryAssociation(
    name="finished0",
    ends={
        Property(name="OurPNVis_Finished", type=OurPNVis_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Arc", type=OurPNVis_Finished, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keepanm1: BinaryAssociation = BinaryAssociation(
    name="keepanm1",
    ends={
        Property(name="OurPNVis_KeepAnim", type=OurPNVis_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Arc2", type=OurPNVis_KeepAnim, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
idnt3: BinaryAssociation = BinaryAssociation(
    name="idnt3",
    ends={
        Property(name="OurPNVis_ident", type=OurPNVis_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Arc4", type=OurPNVis_ident, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure14: BinaryAssociation = BinaryAssociation(
    name="structure14",
    ends={
        Property(name="OurPNVis_Sequence", type=OurPNVis_Activities, multiplicity=Multiplicity(1, 1)),
        Property(name="OurPNVis_Activities15", type=OurPNVis_Sequence, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_OurPNVis_Place_Place = Generalization(general=Place, specific=OurPNVis_Place)
gen_OurPNVis_Transition_Transition = Generalization(general=Transition, specific=OurPNVis_Transition)
gen_OurPNVis_PNVis_PetriNetType = Generalization(general=PetriNetType, specific=OurPNVis_PNVis)
gen_OurPNVis_Arc_Arc = Generalization(general=Arc, specific=OurPNVis_Arc)
gen_OurPNVis_Finished_Attribute = Generalization(general=Attribute, specific=OurPNVis_Finished)
gen_OurPNVis_Tokens_Attribute = Generalization(general=Attribute, specific=OurPNVis_Tokens)
gen_OurPNVis_CanChange_Attribute = Generalization(general=Attribute, specific=OurPNVis_CanChange)
gen_OurPNVis_Shape_Attribute = Generalization(general=Attribute, specific=OurPNVis_Shape)
gen_OurPNVis_Activities_StructuredLabel = Generalization(general=StructuredLabel, specific=OurPNVis_Activities)
gen_OurPNVis_Geometry_Label = Generalization(general=Label, specific=OurPNVis_Geometry)
gen_OurPNVis_KeepAnim_Attribute = Generalization(general=Attribute, specific=OurPNVis_KeepAnim)
gen_OurPNVis_ident_Label = Generalization(general=Label, specific=OurPNVis_ident)

# Domain Model
domain_model = DomainModel(
    name="OurPNVis",
    types={OurPNVis_Place, Place, OurPNVis_Tokens, OurPNVis_CanChange, OurPNVis_Shape, OurPNVis_Activities, OurPNVis_Geometry, OurPNVis_Transition, Transition, OurPNVis_PNVis, PetriNetType, OurPNVis_Arc, Arc, OurPNVis_Finished, OurPNVis_KeepAnim, OurPNVis_ident, Attribute, StructuredLabel, OurPNVis_Sequence, Label},
    associations={tokens5, canchange6, shape8, activities10, geo12, finished0, keepanm1, idnt3, structure14},
    generalizations={gen_OurPNVis_Place_Place, gen_OurPNVis_Transition_Transition, gen_OurPNVis_PNVis_PetriNetType, gen_OurPNVis_Arc_Arc, gen_OurPNVis_Finished_Attribute, gen_OurPNVis_Tokens_Attribute, gen_OurPNVis_CanChange_Attribute, gen_OurPNVis_Shape_Attribute, gen_OurPNVis_Activities_StructuredLabel, gen_OurPNVis_Geometry_Label, gen_OurPNVis_KeepAnim_Attribute, gen_OurPNVis_ident_Label},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)