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
viewers_ListViewerInput = Class(name="viewers::ListViewerInput")
viewers_ListViewerElement = Class(name="viewers::ListViewerElement")
viewers_TableViewerInput = Class(name="viewers::TableViewerInput")
viewers_TableViewerElement = Class(name="viewers::TableViewerElement")
viewers_TreeViewerInput = Class(name="viewers::TreeViewerInput")
viewers_TreeViewerElement = Class(name="viewers::TreeViewerElement")
viewers_ViewerInputs = Class(name="viewers::ViewerInputs")

# viewers_ListViewerInput class attributes and methods

# viewers_ListViewerElement class attributes and methods
viewers_ListViewerElement_label: Property = Property(name="label", type=StringType)
viewers_ListViewerElement.attributes={viewers_ListViewerElement_label}

# viewers_TableViewerInput class attributes and methods

# viewers_TableViewerElement class attributes and methods
viewers_TableViewerElement_name: Property = Property(name="name", type=StringType)
viewers_TableViewerElement_label: Property = Property(name="label", type=StringType)
viewers_TableViewerElement.attributes={viewers_TableViewerElement_name, viewers_TableViewerElement_label}

# viewers_TreeViewerInput class attributes and methods

# viewers_TreeViewerElement class attributes and methods
viewers_TreeViewerElement_label: Property = Property(name="label", type=StringType)
viewers_TreeViewerElement.attributes={viewers_TreeViewerElement_label}

# viewers_ViewerInputs class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="viewers_ListViewerElement", type=viewers_ListViewerInput, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_ListViewerInput", type=viewers_ListViewerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableInputs8: BinaryAssociation = BinaryAssociation(
    name="tableInputs8",
    ends={
        Property(name="viewers_TableViewerInput10", type=viewers_ViewerInputs, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_ViewerInputs9", type=viewers_TableViewerInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
treeInputs11: BinaryAssociation = BinaryAssociation(
    name="treeInputs11",
    ends={
        Property(name="viewers_TreeViewerInput13", type=viewers_ViewerInputs, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_ViewerInputs12", type=viewers_TreeViewerInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="viewers_TableViewerElement", type=viewers_TableViewerInput, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_TableViewerInput", type=viewers_TableViewerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements2: BinaryAssociation = BinaryAssociation(
    name="elements2",
    ends={
        Property(name="viewers_TreeViewerElement", type=viewers_TreeViewerInput, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_TreeViewerInput", type=viewers_TreeViewerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="viewers_TreeViewerElement5", type=viewers_TreeViewerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_TreeViewerElement3", type=viewers_TreeViewerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listInputs6: BinaryAssociation = BinaryAssociation(
    name="listInputs6",
    ends={
        Property(name="viewers_ListViewerInput7", type=viewers_ViewerInputs, multiplicity=Multiplicity(1, 1)),
        Property(name="viewers_ViewerInputs", type=viewers_ListViewerInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="viewers",
    types={viewers_ListViewerInput, viewers_ListViewerElement, viewers_TableViewerInput, viewers_TableViewerElement, viewers_TreeViewerInput, viewers_TreeViewerElement, viewers_ViewerInputs},
    associations={elements0, tableInputs8, treeInputs11, elements1, elements2, children4, listInputs6},
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