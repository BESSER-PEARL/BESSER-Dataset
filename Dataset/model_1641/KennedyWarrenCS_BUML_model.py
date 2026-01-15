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
kwcs_LeafCS = Class(name="kwcs::LeafCS")
kwcs_TopCS = Class(name="kwcs::TopCS")
kwcs_TreeCS = Class(name="kwcs::TreeCS", is_abstract=True)
kwcs_BinCS = Class(name="kwcs::BinCS")
TreeCS = Class(name="TreeCS")

# kwcs_LeafCS class attributes and methods
kwcs_LeafCS_val: Property = Property(name="val", type=IntegerType)
kwcs_LeafCS.attributes={kwcs_LeafCS_val}

# kwcs_TopCS class attributes and methods

# kwcs_TreeCS class attributes and methods

# kwcs_BinCS class attributes and methods

# TreeCS class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="kwcs_TreeCS", type=kwcs_TopCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kwcs_TopCS", type=kwcs_TreeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="kwcs_TreeCS2", type=kwcs_BinCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kwcs_BinCS", type=kwcs_TreeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="kwcs_TreeCS5", type=kwcs_BinCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kwcs_BinCS4", type=kwcs_TreeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kwcs_LeafCS_TreeCS = Generalization(general=TreeCS, specific=kwcs_LeafCS)
gen_kwcs_BinCS_TreeCS = Generalization(general=TreeCS, specific=kwcs_BinCS)

# Domain Model
domain_model = DomainModel(
    name="kwcs",
    types={kwcs_LeafCS, kwcs_TopCS, kwcs_TreeCS, kwcs_BinCS, TreeCS},
    associations={node0, left1, right3},
    generalizations={gen_kwcs_LeafCS_TreeCS, gen_kwcs_BinCS_TreeCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)