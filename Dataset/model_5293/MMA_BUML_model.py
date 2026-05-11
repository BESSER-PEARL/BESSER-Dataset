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
Root = Class(name="Root")
MMA_A = Class(name="MMA_A")
MMA_B = Class(name="MMA_B")
MMA_Root = Class(name="MMA_Root")
Element = Class(name="Element")
MMA_Element = Class(name="MMA_Element", is_abstract=True)

# Root class attributes and methods

# MMA_A class attributes and methods

# MMA_B class attributes and methods

# MMA_Root class attributes and methods

# Element class attributes and methods

# MMA_Element class attributes and methods
MMA_Element_name: Property = Property(name="name", type=StringType)
MMA_Element.attributes={MMA_Element_name}

# Relationships
targets1: BinaryAssociation = BinaryAssociation(
    name="targets1",
    ends={
        Property(name="Element2", type=MMA_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
sources3: BinaryAssociation = BinaryAssociation(
    name="sources3",
    ends={
        Property(name="Element4", type=MMA_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="targets", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="Root", type=MMA_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=Root, multiplicity=Multiplicity(1, 1))
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="Element", type=MMA_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MMA_A_Element = Generalization(general=Element, specific=MMA_A)
gen_MMA_B_Element = Generalization(general=Element, specific=MMA_B)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Root, MMA_A, MMA_B, MMA_Root, Element, MMA_Element},
    associations={targets1, sources3, parent5, children0},
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