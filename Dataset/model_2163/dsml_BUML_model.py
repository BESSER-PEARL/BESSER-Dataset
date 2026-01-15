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
dsml_DReferenceBridge = Class(name="dsml::DReferenceBridge")
dsml_DGraphElement = Class(name="dsml::DGraphElement", is_abstract=True)
dsml_DEdge = Class(name="dsml::DEdge", is_abstract=True)
DGraphElement = Class(name="DGraphElement")
dsml_DNode = Class(name="dsml::DNode")
dsml_EReference = Class(name="dsml::EReference")
dsml_DReference = Class(name="dsml::DReference")
DEdge = Class(name="DEdge")
dsml_DContainment = Class(name="dsml::DContainment")
DClassElement = Class(name="DClassElement")
DContainedElement = Class(name="DContainedElement")
dsml_DLabel = Class(name="dsml::DLabel")
dsml_DLink = Class(name="dsml::DLink")
DContainedEdge = Class(name="DContainedEdge")
dsml_Diagraph = Class(name="dsml::Diagraph")
dsml_DSemanticBridge = Class(name="dsml::DSemanticBridge")
dsml_DGraph = Class(name="dsml::DGraph")
dsml_DClassElement = Class(name="dsml::DClassElement", is_abstract=True)
dsml_EClass = Class(name="dsml::EClass")
dsml_EAttribute = Class(name="dsml::EAttribute")
dsml_DClassBridge = Class(name="dsml::DClassBridge")
dsml_DContainedElement = Class(name="dsml::DContainedElement", is_abstract=True)
dsml_DContainedEdge = Class(name="dsml::DContainedEdge", is_abstract=True)
dsml_DAttributeBridge = Class(name="dsml::DAttributeBridge")
DModelElementBridge = Class(name="DModelElementBridge")
dsml_DModelElementBridge = Class(name="dsml::DModelElementBridge")

# dsml_DReferenceBridge class attributes and methods

# dsml_DGraphElement class attributes and methods
dsml_DGraphElement_name: Property = Property(name="name", type=StringType)
dsml_DGraphElement.attributes={dsml_DGraphElement_name}

# dsml_DEdge class attributes and methods

# DGraphElement class attributes and methods

# dsml_DNode class attributes and methods
dsml_DNode_pointOfView: Property = Property(name="pointOfView", type=BooleanType)
dsml_DNode_pointOfViewName: Property = Property(name="pointOfViewName", type=StringType)
dsml_DNode.attributes={dsml_DNode_pointOfViewName, dsml_DNode_pointOfView}

# dsml_EReference class attributes and methods

# dsml_DReference class attributes and methods
dsml_DReference_nonGraphicalProperty: Property = Property(name="nonGraphicalProperty", type=BooleanType)
dsml_DReference.attributes={dsml_DReference_nonGraphicalProperty}

# DEdge class attributes and methods

# dsml_DContainment class attributes and methods
dsml_DContainment_compartment: Property = Property(name="compartment", type=BooleanType)
dsml_DContainment.attributes={dsml_DContainment_compartment}

# DClassElement class attributes and methods

# DContainedElement class attributes and methods

# dsml_DLabel class attributes and methods
dsml_DLabel_name: Property = Property(name="name", type=StringType)
dsml_DLabel.attributes={dsml_DLabel_name}

# dsml_DLink class attributes and methods

# DContainedEdge class attributes and methods

# dsml_Diagraph class attributes and methods

# dsml_DSemanticBridge class attributes and methods

# dsml_DGraph class attributes and methods

# dsml_DClassElement class attributes and methods

# dsml_EClass class attributes and methods

# dsml_EAttribute class attributes and methods

# dsml_DClassBridge class attributes and methods

# dsml_DContainedElement class attributes and methods

# dsml_DContainedEdge class attributes and methods

# dsml_DAttributeBridge class attributes and methods

# DModelElementBridge class attributes and methods

# dsml_DModelElementBridge class attributes and methods
dsml_DModelElementBridge_ecoreName: Property = Property(name="ecoreName", type=StringType)
dsml_DModelElementBridge_ecorePath: Property = Property(name="ecorePath", type=StringType)
dsml_DModelElementBridge.attributes={dsml_DModelElementBridge_ecorePath, dsml_DModelElementBridge_ecoreName}

# Relationships
sourceNode3: BinaryAssociation = BinaryAssociation(
    name="sourceNode3",
    ends={
        Property(name="dsml_DNode5", type=dsml_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DEdge4", type=dsml_DNode, multiplicity=Multiplicity(0, 1))
    }
)
eTargetReferenceBridge6: BinaryAssociation = BinaryAssociation(
    name="eTargetReferenceBridge6",
    ends={
        Property(name="dsml_DReferenceBridge", type=dsml_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DEdge7", type=dsml_DReferenceBridge, multiplicity=Multiplicity(0, 1))
    }
)
targetNode0: BinaryAssociation = BinaryAssociation(
    name="targetNode0",
    ends={
        Property(name="dsml_DNode", type=dsml_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DEdge", type=dsml_DNode, multiplicity=Multiplicity(0, 1))
    }
)
targetReference1: BinaryAssociation = BinaryAssociation(
    name="targetReference1",
    ends={
        Property(name="dsml_EReference", type=dsml_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DEdge2", type=dsml_EReference, multiplicity=Multiplicity(0, 1))
    }
)
edges8: BinaryAssociation = BinaryAssociation(
    name="edges8",
    ends={
        Property(name="dsml_DEdge10", type=dsml_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DNode9", type=dsml_DEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentPointOfView12: BinaryAssociation = BinaryAssociation(
    name="parentPointOfView12",
    ends={
        Property(name="DNode", type=dsml_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="childrenPointOfView", type=dsml_DNode, multiplicity=Multiplicity(0, 1))
    }
)
childrenPointOfView14: BinaryAssociation = BinaryAssociation(
    name="childrenPointOfView14",
    ends={
        Property(name="DNode15", type=dsml_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parentPointOfView", type=dsml_DNode, multiplicity=Multiplicity(0, 9999))
    }
)
labels16: BinaryAssociation = BinaryAssociation(
    name="labels16",
    ends={
        Property(name="dsml_DLabel", type=dsml_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DNode17", type=dsml_DLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceReference18: BinaryAssociation = BinaryAssociation(
    name="sourceReference18",
    ends={
        Property(name="dsml_EReference19", type=dsml_DLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DLink", type=dsml_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eSourceReferenceBridge20: BinaryAssociation = BinaryAssociation(
    name="eSourceReferenceBridge20",
    ends={
        Property(name="dsml_DReferenceBridge22", type=dsml_DLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DLink21", type=dsml_DReferenceBridge, multiplicity=Multiplicity(0, 1))
    }
)
linkLabels23: BinaryAssociation = BinaryAssociation(
    name="linkLabels23",
    ends={
        Property(name="dsml_DLabel25", type=dsml_DLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DLink24", type=dsml_DLabel, multiplicity=Multiplicity(0, 9999))
    }
)
dConcreteSyntax41: BinaryAssociation = BinaryAssociation(
    name="dConcreteSyntax41",
    ends={
        Property(name="dsml_DGraph42", type=dsml_Diagraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_Diagraph", type=dsml_DGraph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dAbstractSyntax43: BinaryAssociation = BinaryAssociation(
    name="dAbstractSyntax43",
    ends={
        Property(name="dsml_DSemanticBridge", type=dsml_Diagraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_Diagraph44", type=dsml_DSemanticBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodes26: BinaryAssociation = BinaryAssociation(
    name="nodes26",
    ends={
        Property(name="dsml_DNode27", type=dsml_DGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DGraph", type=dsml_DNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootPointOfView28: BinaryAssociation = BinaryAssociation(
    name="rootPointOfView28",
    ends={
        Property(name="dsml_DNode30", type=dsml_DGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DGraph29", type=dsml_DNode, multiplicity=Multiplicity(1, 1))
    }
)
eClass31: BinaryAssociation = BinaryAssociation(
    name="eClass31",
    ends={
        Property(name="dsml_EClass", type=dsml_DClassElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DClassElement", type=dsml_EClass, multiplicity=Multiplicity(0, 1))
    }
)
labelAttribute32: BinaryAssociation = BinaryAssociation(
    name="labelAttribute32",
    ends={
        Property(name="dsml_EAttribute", type=dsml_DClassElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DClassElement33", type=dsml_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eClassBridge34: BinaryAssociation = BinaryAssociation(
    name="eClassBridge34",
    ends={
        Property(name="dsml_DClassBridge", type=dsml_DClassElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DClassElement35", type=dsml_DClassBridge, multiplicity=Multiplicity(0, 1))
    }
)
containment36: BinaryAssociation = BinaryAssociation(
    name="containment36",
    ends={
        Property(name="dsml_DNode37", type=dsml_DContainedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DContainedElement", type=dsml_DNode, multiplicity=Multiplicity(0, 1))
    }
)
eContainmentReferenceBridge38: BinaryAssociation = BinaryAssociation(
    name="eContainmentReferenceBridge38",
    ends={
        Property(name="dsml_DReferenceBridge40", type=dsml_DContainedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DContainedElement39", type=dsml_DReferenceBridge, multiplicity=Multiplicity(0, 1))
    }
)
dModelElements45: BinaryAssociation = BinaryAssociation(
    name="dModelElements45",
    ends={
        Property(name="dsml_DModelElementBridge", type=dsml_DSemanticBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DSemanticBridge46", type=dsml_DModelElementBridge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAttributeBridge47: BinaryAssociation = BinaryAssociation(
    name="eAttributeBridge47",
    ends={
        Property(name="dsml_DAttributeBridge", type=dsml_DLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_DLabel48", type=dsml_DAttributeBridge, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dsml_DNode_DGraphElement = Generalization(general=DGraphElement, specific=dsml_DNode)
gen_dsml_DEdge_DGraphElement = Generalization(general=DGraphElement, specific=dsml_DEdge)
gen_dsml_DReference_DEdge = Generalization(general=DEdge, specific=dsml_DReference)
gen_dsml_DContainment_DContainedEdge = Generalization(general=DContainedEdge, specific=dsml_DContainment)
gen_dsml_DNode_DClassElement = Generalization(general=DClassElement, specific=dsml_DNode)
gen_dsml_DNode_DContainedElement = Generalization(general=DContainedElement, specific=dsml_DNode)
gen_dsml_DLink_DContainedEdge = Generalization(general=DContainedEdge, specific=dsml_DLink)
gen_dsml_DLink_DClassElement = Generalization(general=DClassElement, specific=dsml_DLink)
gen_dsml_DReferenceBridge_DModelElementBridge = Generalization(general=DModelElementBridge, specific=dsml_DReferenceBridge)
gen_dsml_DClassBridge_DModelElementBridge = Generalization(general=DModelElementBridge, specific=dsml_DClassBridge)
gen_dsml_DContainedElement_DGraphElement = Generalization(general=DGraphElement, specific=dsml_DContainedElement)
gen_dsml_DContainedEdge_DContainedElement = Generalization(general=DContainedElement, specific=dsml_DContainedEdge)
gen_dsml_DContainedEdge_DEdge = Generalization(general=DEdge, specific=dsml_DContainedEdge)
gen_dsml_DAttributeBridge_DModelElementBridge = Generalization(general=DModelElementBridge, specific=dsml_DAttributeBridge)

# Domain Model
domain_model = DomainModel(
    name="dsml",
    types={dsml_DReferenceBridge, dsml_DGraphElement, dsml_DEdge, DGraphElement, dsml_DNode, dsml_EReference, dsml_DReference, DEdge, dsml_DContainment, DClassElement, DContainedElement, dsml_DLabel, dsml_DLink, DContainedEdge, dsml_Diagraph, dsml_DSemanticBridge, dsml_DGraph, dsml_DClassElement, dsml_EClass, dsml_EAttribute, dsml_DClassBridge, dsml_DContainedElement, dsml_DContainedEdge, dsml_DAttributeBridge, DModelElementBridge, dsml_DModelElementBridge},
    associations={sourceNode3, eTargetReferenceBridge6, targetNode0, targetReference1, edges8, parentPointOfView12, childrenPointOfView14, labels16, sourceReference18, eSourceReferenceBridge20, linkLabels23, dConcreteSyntax41, dAbstractSyntax43, nodes26, rootPointOfView28, eClass31, labelAttribute32, eClassBridge34, containment36, eContainmentReferenceBridge38, dModelElements45, eAttributeBridge47},
    generalizations={gen_dsml_DNode_DGraphElement, gen_dsml_DEdge_DGraphElement, gen_dsml_DReference_DEdge, gen_dsml_DContainment_DContainedEdge, gen_dsml_DNode_DClassElement, gen_dsml_DNode_DContainedElement, gen_dsml_DLink_DContainedEdge, gen_dsml_DLink_DClassElement, gen_dsml_DReferenceBridge_DModelElementBridge, gen_dsml_DClassBridge_DModelElementBridge, gen_dsml_DContainedElement_DGraphElement, gen_dsml_DContainedEdge_DContainedElement, gen_dsml_DContainedEdge_DEdge, gen_dsml_DAttributeBridge_DModelElementBridge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)