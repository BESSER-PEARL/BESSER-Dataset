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
DShape: Enumeration = Enumeration(
    name="DShape",
    literals={
            EnumerationLiteral(name="rectangle"),
			EnumerationLiteral(name="vee"),
			EnumerationLiteral(name="triangle"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="circle"),
			EnumerationLiteral(name="roundedRect")
    }
)

# Classes
diagraph_DEdge = Class(name="diagraph::DEdge", is_abstract=True)
DGraphElement = Class(name="DGraphElement")
diagraph_DNode = Class(name="diagraph::DNode")
diagraph_EReference = Class(name="diagraph::EReference")
diagraph_DGraphElement = Class(name="diagraph::DGraphElement", is_abstract=True)
diagraph_ENamedElement = Class(name="diagraph::ENamedElement")
DLabeledElement = Class(name="DLabeledElement")
DOwnedElement = Class(name="DOwnedElement")
diagraph_DViewNavigation = Class(name="diagraph::DViewNavigation")
diagraph_DContainment = Class(name="diagraph::DContainment")
diagraph_DLabeledEdge = Class(name="diagraph::DLabeledEdge")
DOwnedEdge = Class(name="DOwnedEdge")
DLineEdge = Class(name="DLineEdge")
diagraph_DReference = Class(name="diagraph::DReference")
diagraph_DNestedEdge = Class(name="diagraph::DNestedEdge")
diagraph_DGraph = Class(name="diagraph::DGraph")
diagraph_DLabeledElement = Class(name="diagraph::DLabeledElement", is_abstract=True)
diagraph_EClass = Class(name="diagraph::EClass")
diagraph_DLabel = Class(name="diagraph::DLabel")
diagraph_DOwnedElement = Class(name="diagraph::DOwnedElement", is_abstract=True)
diagraph_DOwnedEdge = Class(name="diagraph::DOwnedEdge", is_abstract=True)
DEdge = Class(name="DEdge")
diagraph_DCompartmentEdge = Class(name="diagraph::DCompartmentEdge")
DNestedEdge = Class(name="DNestedEdge")
diagraph_DPointOfView = Class(name="diagraph::DPointOfView")
diagraph_DAffixedEdge = Class(name="diagraph::DAffixedEdge")
diagraph_EAttribute = Class(name="diagraph::EAttribute")
diagraph_DLineEdge = Class(name="diagraph::DLineEdge", is_abstract=True)
DSimpleEdge = Class(name="DSimpleEdge")
diagraph_DNavigationEdge = Class(name="diagraph::DNavigationEdge")
diagraph_DGeneric = Class(name="diagraph::DGeneric")
DNode = Class(name="DNode")
diagraph_DSimpleEdge = Class(name="diagraph::DSimpleEdge", is_abstract=True)

# diagraph_DEdge class attributes and methods
diagraph_DEdge_propagated: Property = Property(name="propagated", type=BooleanType)
diagraph_DEdge.attributes={diagraph_DEdge_propagated}

# DGraphElement class attributes and methods

# diagraph_DNode class attributes and methods
diagraph_DNode_shape: Property = Property(name="shape", type=StringType)
diagraph_DNode_layout: Property = Property(name="layout", type=BooleanType)
diagraph_DNode_navigationLink: Property = Property(name="navigationLink", type=StringType)
diagraph_DNode.attributes={diagraph_DNode_navigationLink, diagraph_DNode_shape, diagraph_DNode_layout}

# diagraph_EReference class attributes and methods

# diagraph_DGraphElement class attributes and methods
diagraph_DGraphElement_name: Property = Property(name="name", type=StringType)
diagraph_DGraphElement_icon: Property = Property(name="icon", type=StringType)
diagraph_DGraphElement_abztract: Property = Property(name="abztract", type=BooleanType)
diagraph_DGraphElement.attributes={diagraph_DGraphElement_abztract, diagraph_DGraphElement_name, diagraph_DGraphElement_icon}

# diagraph_ENamedElement class attributes and methods

# DLabeledElement class attributes and methods

# DOwnedElement class attributes and methods

# diagraph_DViewNavigation class attributes and methods
diagraph_DViewNavigation_id: Property = Property(name="id", type=StringType)
diagraph_DViewNavigation.attributes={diagraph_DViewNavigation_id}

# diagraph_DContainment class attributes and methods
diagraph_DContainment_name: Property = Property(name="name", type=StringType)
diagraph_DContainment.attributes={diagraph_DContainment_name}

# diagraph_DLabeledEdge class attributes and methods

# DOwnedEdge class attributes and methods

# DLineEdge class attributes and methods

# diagraph_DReference class attributes and methods

# diagraph_DNestedEdge class attributes and methods

# diagraph_DGraph class attributes and methods
diagraph_DGraph_viewName: Property = Property(name="viewName", type=StringType)
diagraph_DGraph_facade1: Property = Property(name="facade1", type=StringType)
diagraph_DGraph_facade2: Property = Property(name="facade2", type=StringType)
diagraph_DGraph.attributes={diagraph_DGraph_facade2, diagraph_DGraph_viewName, diagraph_DGraph_facade1}

# diagraph_DLabeledElement class attributes and methods
diagraph_DLabeledElement_labls: Property = Property(name="labls", type=StringType)
diagraph_DLabeledElement_expression: Property = Property(name="expression", type=StringType)
diagraph_DLabeledElement.attributes={diagraph_DLabeledElement_labls, diagraph_DLabeledElement_expression}

# diagraph_EClass class attributes and methods

# diagraph_DLabel class attributes and methods
diagraph_DLabel_propagated: Property = Property(name="propagated", type=BooleanType)
diagraph_DLabel_inferred: Property = Property(name="inferred", type=BooleanType)
diagraph_DLabel_abztract: Property = Property(name="abztract", type=BooleanType)
diagraph_DLabel.attributes={diagraph_DLabel_abztract, diagraph_DLabel_propagated, diagraph_DLabel_inferred}

# diagraph_DOwnedElement class attributes and methods

# diagraph_DOwnedEdge class attributes and methods

# DEdge class attributes and methods

# diagraph_DCompartmentEdge class attributes and methods
diagraph_DCompartmentEdge_partitionName: Property = Property(name="partitionName", type=StringType)
diagraph_DCompartmentEdge_depth: Property = Property(name="depth", type=IntegerType)
diagraph_DCompartmentEdge.attributes={diagraph_DCompartmentEdge_partitionName, diagraph_DCompartmentEdge_depth}

# DNestedEdge class attributes and methods

# diagraph_DPointOfView class attributes and methods

# diagraph_DAffixedEdge class attributes and methods

# diagraph_EAttribute class attributes and methods

# diagraph_DLineEdge class attributes and methods
diagraph_DLineEdge_arrows: Property = Property(name="arrows", type=StringType)
diagraph_DLineEdge.attributes={diagraph_DLineEdge_arrows}

# DSimpleEdge class attributes and methods

# diagraph_DNavigationEdge class attributes and methods

# diagraph_DGeneric class attributes and methods

# DNode class attributes and methods

# diagraph_DSimpleEdge class attributes and methods

# Relationships
target0: BinaryAssociation = BinaryAssociation(
    name="target0",
    ends={
        Property(name="diagraph_DNode", type=diagraph_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DEdge", type=diagraph_DNode, multiplicity=Multiplicity(1, 1))
    }
)
targetReference1: BinaryAssociation = BinaryAssociation(
    name="targetReference1",
    ends={
        Property(name="diagraph_EReference", type=diagraph_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DEdge2", type=diagraph_EReference, multiplicity=Multiplicity(0, 1))
    }
)
viewNavigation5: BinaryAssociation = BinaryAssociation(
    name="viewNavigation5",
    ends={
        Property(name="DViewNavigation", type=diagraph_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="navigationSource", type=diagraph_DViewNavigation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containments6: BinaryAssociation = BinaryAssociation(
    name="containments6",
    ends={
        Property(name="DContainment", type=diagraph_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=diagraph_DContainment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceReference7: BinaryAssociation = BinaryAssociation(
    name="sourceReference7",
    ends={
        Property(name="diagraph_EReference8", type=diagraph_DLabeledEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DLabeledEdge", type=diagraph_EReference, multiplicity=Multiplicity(0, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="diagraph_DContainment", type=diagraph_DNestedEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DNestedEdge", type=diagraph_DContainment, multiplicity=Multiplicity(1, 1))
    }
)
semanticRole3: BinaryAssociation = BinaryAssociation(
    name="semanticRole3",
    ends={
        Property(name="diagraph_ENamedElement", type=diagraph_DGraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DGraphElement", type=diagraph_ENamedElement, multiplicity=Multiplicity(0, 1))
    }
)
graph4: BinaryAssociation = BinaryAssociation(
    name="graph4",
    ends={
        Property(name="DGraph", type=diagraph_DGraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=diagraph_DGraph, multiplicity=Multiplicity(0, 1))
    }
)
eClaz12: BinaryAssociation = BinaryAssociation(
    name="eClaz12",
    ends={
        Property(name="diagraph_EClass", type=diagraph_DLabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DLabeledElement", type=diagraph_EClass, multiplicity=Multiplicity(0, 1))
    }
)
dlabels13: BinaryAssociation = BinaryAssociation(
    name="dlabels13",
    ends={
        Property(name="diagraph_DLabel", type=diagraph_DLabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DLabeledElement14", type=diagraph_DLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="diagraph_DNode16", type=diagraph_DOwnedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DOwnedElement", type=diagraph_DNode, multiplicity=Multiplicity(0, 1))
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="DGraphElement", type=diagraph_DGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=diagraph_DGraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointOfView11: BinaryAssociation = BinaryAssociation(
    name="pointOfView11",
    ends={
        Property(name="diagraph_DPointOfView", type=diagraph_DGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DGraph", type=diagraph_DPointOfView, multiplicity=Multiplicity(1, 1))
    }
)
navigationTarget17: BinaryAssociation = BinaryAssociation(
    name="navigationTarget17",
    ends={
        Property(name="diagraph_DGraph18", type=diagraph_DViewNavigation, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DViewNavigation", type=diagraph_DGraph, multiplicity=Multiplicity(0, 1))
    }
)
navigationSource19: BinaryAssociation = BinaryAssociation(
    name="navigationSource19",
    ends={
        Property(name="DNode", type=diagraph_DViewNavigation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewNavigation", type=diagraph_DNode, multiplicity=Multiplicity(0, 1))
    }
)
attribute20: BinaryAssociation = BinaryAssociation(
    name="attribute20",
    ends={
        Property(name="diagraph_EAttribute", type=diagraph_DLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DLabel21", type=diagraph_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
edges24: BinaryAssociation = BinaryAssociation(
    name="edges24",
    ends={
        Property(name="diagraph_DNestedEdge26", type=diagraph_DContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DContainment25", type=diagraph_DNestedEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source27: BinaryAssociation = BinaryAssociation(
    name="source27",
    ends={
        Property(name="diagraph_DNode28", type=diagraph_DSimpleEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagraph_DSimpleEdge", type=diagraph_DNode, multiplicity=Multiplicity(1, 1))
    }
)
node22: BinaryAssociation = BinaryAssociation(
    name="node22",
    ends={
        Property(name="DNode23", type=diagraph_DContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="containments", type=diagraph_DNode, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_diagraph_DEdge_DGraphElement = Generalization(general=DGraphElement, specific=diagraph_DEdge)
gen_diagraph_DNode_DLabeledElement = Generalization(general=DLabeledElement, specific=diagraph_DNode)
gen_diagraph_DNode_DOwnedElement = Generalization(general=DOwnedElement, specific=diagraph_DNode)
gen_diagraph_DLabeledEdge_DOwnedEdge = Generalization(general=DOwnedEdge, specific=diagraph_DLabeledEdge)
gen_diagraph_DLabeledEdge_DLabeledElement = Generalization(general=DLabeledElement, specific=diagraph_DLabeledEdge)
gen_diagraph_DLabeledEdge_DLineEdge = Generalization(general=DLineEdge, specific=diagraph_DLabeledEdge)
gen_diagraph_DReference_DLineEdge = Generalization(general=DLineEdge, specific=diagraph_DReference)
gen_diagraph_DNestedEdge_DOwnedEdge = Generalization(general=DOwnedEdge, specific=diagraph_DNestedEdge)
gen_diagraph_DLabeledElement_DGraphElement = Generalization(general=DGraphElement, specific=diagraph_DLabeledElement)
gen_diagraph_DOwnedEdge_DOwnedElement = Generalization(general=DOwnedElement, specific=diagraph_DOwnedEdge)
gen_diagraph_DOwnedEdge_DEdge = Generalization(general=DEdge, specific=diagraph_DOwnedEdge)
gen_diagraph_DCompartmentEdge_DNestedEdge = Generalization(general=DNestedEdge, specific=diagraph_DCompartmentEdge)
gen_diagraph_DAffixedEdge_DNestedEdge = Generalization(general=DNestedEdge, specific=diagraph_DAffixedEdge)
gen_diagraph_DLineEdge_DSimpleEdge = Generalization(general=DSimpleEdge, specific=diagraph_DLineEdge)
gen_diagraph_DNavigationEdge_DSimpleEdge = Generalization(general=DSimpleEdge, specific=diagraph_DNavigationEdge)
gen_diagraph_DGeneric_DLabeledElement = Generalization(general=DLabeledElement, specific=diagraph_DGeneric)
gen_diagraph_DPointOfView_DNode = Generalization(general=DNode, specific=diagraph_DPointOfView)
gen_diagraph_DSimpleEdge_DEdge = Generalization(general=DEdge, specific=diagraph_DSimpleEdge)

# Domain Model
domain_model = DomainModel(
    name="diagraph",
    types={diagraph_DEdge, DGraphElement, diagraph_DNode, diagraph_EReference, diagraph_DGraphElement, diagraph_ENamedElement, DLabeledElement, DOwnedElement, diagraph_DViewNavigation, diagraph_DContainment, diagraph_DLabeledEdge, DOwnedEdge, DLineEdge, diagraph_DReference, diagraph_DNestedEdge, diagraph_DGraph, diagraph_DLabeledElement, diagraph_EClass, diagraph_DLabel, diagraph_DOwnedElement, diagraph_DOwnedEdge, DEdge, diagraph_DCompartmentEdge, DNestedEdge, diagraph_DPointOfView, diagraph_DAffixedEdge, diagraph_EAttribute, diagraph_DLineEdge, DSimpleEdge, diagraph_DNavigationEdge, diagraph_DGeneric, DNode, diagraph_DSimpleEdge, DShape},
    associations={target0, targetReference1, viewNavigation5, containments6, sourceReference7, source9, semanticRole3, graph4, eClaz12, dlabels13, owner15, elements10, pointOfView11, navigationTarget17, navigationSource19, attribute20, edges24, source27, node22},
    generalizations={gen_diagraph_DEdge_DGraphElement, gen_diagraph_DNode_DLabeledElement, gen_diagraph_DNode_DOwnedElement, gen_diagraph_DLabeledEdge_DOwnedEdge, gen_diagraph_DLabeledEdge_DLabeledElement, gen_diagraph_DLabeledEdge_DLineEdge, gen_diagraph_DReference_DLineEdge, gen_diagraph_DNestedEdge_DOwnedEdge, gen_diagraph_DLabeledElement_DGraphElement, gen_diagraph_DOwnedEdge_DOwnedElement, gen_diagraph_DOwnedEdge_DEdge, gen_diagraph_DCompartmentEdge_DNestedEdge, gen_diagraph_DAffixedEdge_DNestedEdge, gen_diagraph_DLineEdge_DSimpleEdge, gen_diagraph_DNavigationEdge_DSimpleEdge, gen_diagraph_DGeneric_DLabeledElement, gen_diagraph_DPointOfView_DNode, gen_diagraph_DSimpleEdge_DEdge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)