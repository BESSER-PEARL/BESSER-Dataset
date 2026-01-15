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
edd_Diagram = Class(name="edd::Diagram")
edd_Model = Class(name="edd::Model")
edd_Block = Class(name="edd::Block")
edd_TreeElement = Class(name="edd::TreeElement")

# edd_Diagram class attributes and methods

# edd_Model class attributes and methods
edd_Model_name: Property = Property(name="name", type=StringType)
edd_Model.attributes={edd_Model_name}

# edd_Block class attributes and methods
edd_Block_name: Property = Property(name="name", type=StringType)
edd_Block_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
edd_Block.attributes={edd_Block_name}
edd_Block.methods={edd_Block_m_validate}

# edd_TreeElement class attributes and methods
edd_TreeElement_index: Property = Property(name="index", type=StringType)
edd_TreeElement_name: Property = Property(name="name", type=StringType)
edd_TreeElement_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
edd_TreeElement.attributes={edd_TreeElement_index, edd_TreeElement_name}
edd_TreeElement.methods={edd_TreeElement_m_validate}

# Relationships
items5: BinaryAssociation = BinaryAssociation(
    name="items5",
    ends={
        Property(name="edd_TreeElement7", type=edd_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="edd_Block6", type=edd_TreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="edd_Model", type=edd_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="edd_Diagram", type=edd_Model, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocks1: BinaryAssociation = BinaryAssociation(
    name="blocks1",
    ends={
        Property(name="edd_Block", type=edd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="edd_Model2", type=edd_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links4: BinaryAssociation = BinaryAssociation(
    name="links4",
    ends={
        Property(name="edd_TreeElement", type=edd_TreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="edd_TreeElement3", type=edd_TreeElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="edd",
    types={edd_Diagram, edd_Model, edd_Block, edd_TreeElement},
    associations={items5, model0, blocks1, links4},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)