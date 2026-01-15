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

# Enumerations
TreeMapType: Enumeration = Enumeration(
    name="TreeMapType",
    literals={
            EnumerationLiteral(name="Ordred"),
			EnumerationLiteral(name="Quantum"),
			EnumerationLiteral(name="Linear")
    }
)

# Classes
TreeMapViewer_TreeMapViewer = Class(name="TreeMapViewer::TreeMapViewer")
TreeMapViewer_TreeMapItem = Class(name="TreeMapViewer::TreeMapItem")
TreeMapViewer_TreeMapContainer = Class(name="TreeMapViewer::TreeMapContainer")
TreeMapItem = Class(name="TreeMapItem")

# TreeMapViewer_TreeMapViewer class attributes and methods
TreeMapViewer_TreeMapViewer_childLayoutStrategy: Property = Property(name="childLayoutStrategy", type=StringType)
TreeMapViewer_TreeMapViewer.attributes={TreeMapViewer_TreeMapViewer_childLayoutStrategy}

# TreeMapViewer_TreeMapItem class attributes and methods
TreeMapViewer_TreeMapItem_label: Property = Property(name="label", type=StringType)
TreeMapViewer_TreeMapItem_value: Property = Property(name="value", type=FloatType)
TreeMapViewer_TreeMapItem.attributes={TreeMapViewer_TreeMapItem_label, TreeMapViewer_TreeMapItem_value}

# TreeMapViewer_TreeMapContainer class attributes and methods

# TreeMapItem class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="TreeMapViewer_TreeMapItem", type=TreeMapViewer_TreeMapViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeMapViewer_TreeMapViewer", type=TreeMapViewer_TreeMapItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="TreeMapViewer_TreeMapViewer3", type=TreeMapViewer_TreeMapItem, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeMapViewer_TreeMapItem2", type=TreeMapViewer_TreeMapViewer, multiplicity=Multiplicity(0, 1))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="TreeMapViewer_TreeMapItem5", type=TreeMapViewer_TreeMapContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeMapViewer_TreeMapContainer", type=TreeMapViewer_TreeMapItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TreeMapViewer_TreeMapContainer_TreeMapItem = Generalization(general=TreeMapItem, specific=TreeMapViewer_TreeMapContainer)

# Domain Model
domain_model = DomainModel(
    name="TreeMapViewer",
    types={TreeMapViewer_TreeMapViewer, TreeMapViewer_TreeMapItem, TreeMapViewer_TreeMapContainer, TreeMapItem, TreeMapType},
    associations={children0, parent1, children4},
    generalizations={gen_TreeMapViewer_TreeMapContainer_TreeMapItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)