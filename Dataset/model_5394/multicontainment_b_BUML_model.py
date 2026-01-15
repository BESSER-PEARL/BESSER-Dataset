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
multicontainment_b_ChildB2 = Class(name="multicontainment::b::ChildB2")
multicontainment_b_Identified = Class(name="multicontainment::b::Identified", is_abstract=True)
multicontainment_b_RootB = Class(name="multicontainment::b::RootB")
Identified = Class(name="Identified")
multicontainment_b_ChildB1 = Class(name="multicontainment::b::ChildB1")

# multicontainment_b_ChildB2 class attributes and methods
multicontainment_b_ChildB2_name: Property = Property(name="name", type=StringType)
multicontainment_b_ChildB2.attributes={multicontainment_b_ChildB2_name}

# multicontainment_b_Identified class attributes and methods
multicontainment_b_Identified_id: Property = Property(name="id", type=StringType)
multicontainment_b_Identified.attributes={multicontainment_b_Identified_id}

# multicontainment_b_RootB class attributes and methods

# Identified class attributes and methods

# multicontainment_b_ChildB1 class attributes and methods
multicontainment_b_ChildB1_name: Property = Property(name="name", type=StringType)
multicontainment_b_ChildB1.attributes={multicontainment_b_ChildB1_name}

# Relationships
childrenB2a4: BinaryAssociation = BinaryAssociation(
    name="childrenB2a4",
    ends={
        Property(name="multicontainment_b_ChildB2", type=multicontainment_b_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="multicontainment_b_RootB5", type=multicontainment_b_ChildB2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childrenB1a0: BinaryAssociation = BinaryAssociation(
    name="childrenB1a0",
    ends={
        Property(name="multicontainment_b_ChildB1", type=multicontainment_b_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="multicontainment_b_RootB", type=multicontainment_b_ChildB1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childrenB1b1: BinaryAssociation = BinaryAssociation(
    name="childrenB1b1",
    ends={
        Property(name="multicontainment_b_ChildB13", type=multicontainment_b_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="multicontainment_b_RootB2", type=multicontainment_b_ChildB1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_multicontainment_b_ChildB1_Identified = Generalization(general=Identified, specific=multicontainment_b_ChildB1)
gen_multicontainment_b_ChildB2_Identified = Generalization(general=Identified, specific=multicontainment_b_ChildB2)
gen_multicontainment_b_RootB_Identified = Generalization(general=Identified, specific=multicontainment_b_RootB)

# Domain Model
domain_model = DomainModel(
    name="multicontainment_b",
    types={multicontainment_b_ChildB2, multicontainment_b_Identified, multicontainment_b_RootB, Identified, multicontainment_b_ChildB1},
    associations={childrenB2a4, childrenB1a0, childrenB1b1},
    generalizations={gen_multicontainment_b_ChildB1_Identified, gen_multicontainment_b_ChildB2_Identified, gen_multicontainment_b_RootB_Identified},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)