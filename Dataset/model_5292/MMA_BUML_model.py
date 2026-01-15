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
MMA_Root = Class(name="MMA::Root")
Element = Class(name="Element")
MMA_Element = Class(name="MMA::Element", is_abstract=True)
Root = Class(name="Root")
MMA_A = Class(name="MMA::A")
MMA_B = Class(name="MMA::B")

# MMA_Root class attributes and methods

# Element class attributes and methods

# MMA_Element class attributes and methods
MMA_Element_name: Property = Property(name="name", type=StringType)
MMA_Element.attributes={MMA_Element_name}

# Root class attributes and methods

# MMA_A class attributes and methods

# MMA_B class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="", type=MMA_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources4: BinaryAssociation = BinaryAssociation(
    name="sources4",
    ends={
        Property(name="6", type=MMA_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="9", type=MMA_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
targets1: BinaryAssociation = BinaryAssociation(
    name="targets1",
    ends={
        Property(name="3", type=MMA_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_MMA_A_Element = Generalization(general=Element, specific=MMA_A)
gen_MMA_B_Element = Generalization(general=Element, specific=MMA_B)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={MMA_Root, Element, MMA_Element, Root, MMA_A, MMA_B},
    associations={children0, sources4, parent7, targets1},
    generalizations={gen_MMA_A_Element, gen_MMA_B_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)