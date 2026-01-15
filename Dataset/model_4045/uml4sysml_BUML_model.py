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
UML_Feature = Class(name="UML::Feature")
uml_UML_StructuralFeature = Class(name="uml::UML::StructuralFeature")
UML_TypedElement = Class(name="UML::TypedElement")
uml_UML_Type = Class(name="uml::UML::Type")
UML_PackageableElement = Class(name="UML::PackageableElement")
uml_UML_TypedElement = Class(name="uml::UML::TypedElement")
uml_UML_Classifier = Class(name="uml::UML::Classifier")
UML_Type = Class(name="UML::Type")
uml_UML_Interface = Class(name="uml::UML::Interface")
UML_Classifier = Class(name="UML::Classifier")
uml_UML_Operation = Class(name="uml::UML::Operation")
uml_UML_Property = Class(name="uml::UML::Property")
uml_UML_InterfaceRealization = Class(name="uml::UML::InterfaceRealization")
uml_UML_NamedElement = Class(name="uml::UML::NamedElement")
uml_UML_RedefinableElement = Class(name="uml::UML::RedefinableElement")
UML_NamedElement = Class(name="UML::NamedElement")
uml_UML_Feature = Class(name="uml::UML::Feature")
UML_RedefinableElement = Class(name="UML::RedefinableElement")
uml_UML_Namespace = Class(name="uml::UML::Namespace")
uml_UML_Constraint = Class(name="uml::UML::Constraint")
uml_UML_Package = Class(name="uml::UML::Package")
UML_Namespace = Class(name="UML::Namespace")
uml_UML_PackageableElement = Class(name="uml::UML::PackageableElement")
uml_UML_BehavioralFeature = Class(name="uml::UML::BehavioralFeature")
uml_UML_ConnectableElement = Class(name="uml::UML::ConnectableElement")
uml_UML_Connector = Class(name="uml::UML::Connector")
uml_UML_ConnectorEnd = Class(name="uml::UML::ConnectorEnd")
uml_UML_CallOperationAction = Class(name="uml::UML::CallOperationAction")
UML_Action = Class(name="UML::Action")
uml_UML_Action = Class(name="uml::UML::Action")
UML_ActivityNode = Class(name="UML::ActivityNode")
uml_UML_BehavioredClassifier = Class(name="uml::UML::BehavioredClassifier")
uml_UML_Behavior = Class(name="uml::UML::Behavior")
UML_BehavioralFeature = Class(name="UML::BehavioralFeature")
uml_UML_Class = Class(name="uml::UML::Class")
UML_BehavioredClassifier = Class(name="UML::BehavioredClassifier")
UML_StructuralFeature = Class(name="UML::StructuralFeature")
UML_ConnectableElement = Class(name="UML::ConnectableElement")
uml_UML_Port = Class(name="uml::UML::Port")
UML_Property = Class(name="UML::Property")
UML_Class = Class(name="UML::Class")
uml_UML_Activity = Class(name="uml::UML::Activity")
UML_Behavior = Class(name="UML::Behavior")
uml_UML_ActivityEdge = Class(name="uml::UML::ActivityEdge")
uml_UML_ActivityNode = Class(name="uml::UML::ActivityNode")
uml_UML_ValueSpecification = Class(name="uml::UML::ValueSpecification")
uml_UML_OpaqueExpression = Class(name="uml::UML::OpaqueExpression")
UML_ValueSpecification = Class(name="UML::ValueSpecification")

# UML_Feature class attributes and methods

# uml_UML_StructuralFeature class attributes and methods

# UML_TypedElement class attributes and methods

# uml_UML_Type class attributes and methods

# UML_PackageableElement class attributes and methods

# uml_UML_TypedElement class attributes and methods

# uml_UML_Classifier class attributes and methods

# UML_Type class attributes and methods

# uml_UML_Interface class attributes and methods

# UML_Classifier class attributes and methods

# uml_UML_Operation class attributes and methods

# uml_UML_Property class attributes and methods

# uml_UML_InterfaceRealization class attributes and methods

# uml_UML_NamedElement class attributes and methods
uml_UML_NamedElement_name: Property = Property(name="name", type=StringType)
uml_UML_NamedElement.attributes={uml_UML_NamedElement_name}

# uml_UML_RedefinableElement class attributes and methods

# UML_NamedElement class attributes and methods

# uml_UML_Feature class attributes and methods

# UML_RedefinableElement class attributes and methods

# uml_UML_Namespace class attributes and methods

# uml_UML_Constraint class attributes and methods

# uml_UML_Package class attributes and methods

# UML_Namespace class attributes and methods

# uml_UML_PackageableElement class attributes and methods

# uml_UML_BehavioralFeature class attributes and methods

# uml_UML_ConnectableElement class attributes and methods

# uml_UML_Connector class attributes and methods

# uml_UML_ConnectorEnd class attributes and methods

# uml_UML_CallOperationAction class attributes and methods

# UML_Action class attributes and methods

# uml_UML_Action class attributes and methods

# UML_ActivityNode class attributes and methods

# uml_UML_BehavioredClassifier class attributes and methods

# uml_UML_Behavior class attributes and methods

# UML_BehavioralFeature class attributes and methods

# uml_UML_Class class attributes and methods

# UML_BehavioredClassifier class attributes and methods

# UML_StructuralFeature class attributes and methods

# UML_ConnectableElement class attributes and methods

# uml_UML_Port class attributes and methods

# UML_Property class attributes and methods

# UML_Class class attributes and methods

# uml_UML_Activity class attributes and methods

# UML_Behavior class attributes and methods

# uml_UML_ActivityEdge class attributes and methods

# uml_UML_ActivityNode class attributes and methods
uml_UML_ActivityNode_name: Property = Property(name="name", type=StringType)
uml_UML_ActivityNode.attributes={uml_UML_ActivityNode_name}

# uml_UML_ValueSpecification class attributes and methods

# uml_UML_OpaqueExpression class attributes and methods
uml_UML_OpaqueExpression_body: Property = Property(name="body", type=StringType)
uml_UML_OpaqueExpression_language: Property = Property(name="language", type=StringType)
uml_UML_OpaqueExpression.attributes={uml_UML_OpaqueExpression_body, uml_UML_OpaqueExpression_language}

# UML_ValueSpecification class attributes and methods

# Relationships
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="uml_UML_Type", type=uml_UML_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_TypedElement", type=uml_UML_Type, multiplicity=Multiplicity(1, 1))
    }
)
feature3: BinaryAssociation = BinaryAssociation(
    name="feature3",
    ends={
        Property(name="uml_UML_Feature", type=uml_UML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Classifier", type=uml_UML_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation4: BinaryAssociation = BinaryAssociation(
    name="ownedOperation4",
    ends={
        Property(name="uml_UML_Operation", type=uml_UML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Interface", type=uml_UML_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute5: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute5",
    ends={
        Property(name="uml_UML_Property", type=uml_UML_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Interface6", type=uml_UML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule0: BinaryAssociation = BinaryAssociation(
    name="ownedRule0",
    ends={
        Property(name="uml_UML_Constraint", type=uml_UML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Namespace", type=uml_UML_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElements1: BinaryAssociation = BinaryAssociation(
    name="packagedElements1",
    ends={
        Property(name="uml_UML_PackageableElement", type=uml_UML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Package", type=uml_UML_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node22: BinaryAssociation = BinaryAssociation(
    name="node22",
    ends={
        Property(name="uml_UML_ActivityNode", type=uml_UML_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Activity23", type=uml_UML_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectorEnd24: BinaryAssociation = BinaryAssociation(
    name="connectorEnd24",
    ends={
        Property(name="uml_UML_ConnectorEnd", type=uml_UML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Connector", type=uml_UML_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
operation25: BinaryAssociation = BinaryAssociation(
    name="operation25",
    ends={
        Property(name="uml_UML_Operation26", type=uml_UML_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_CallOperationAction", type=uml_UML_Operation, multiplicity=Multiplicity(1, 1))
    }
)
incoming28: BinaryAssociation = BinaryAssociation(
    name="incoming28",
    ends={
        Property(name="uml_UML_ActivityNode29", type=uml_UML_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_ActivityNode27", type=uml_UML_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing30: BinaryAssociation = BinaryAssociation(
    name="outgoing30",
    ends={
        Property(name="uml_UML_ActivityEdge32", type=uml_UML_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_ActivityNode31", type=uml_UML_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="uml_UML_ActivityNode35", type=uml_UML_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_ActivityEdge34", type=uml_UML_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
contract7: BinaryAssociation = BinaryAssociation(
    name="contract7",
    ends={
        Property(name="uml_UML_Interface8", type=uml_UML_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_InterfaceRealization", type=uml_UML_Interface, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRealization9: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization9",
    ends={
        Property(name="uml_UML_InterfaceRealization10", type=uml_UML_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_BehavioredClassifier", type=uml_UML_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior11: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior11",
    ends={
        Property(name="uml_UML_Behavior", type=uml_UML_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_BehavioredClassifier12", type=uml_UML_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation13: BinaryAssociation = BinaryAssociation(
    name="ownedOperation13",
    ends={
        Property(name="uml_UML_Operation14", type=uml_UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Class", type=uml_UML_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier15: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier15",
    ends={
        Property(name="uml_UML_Classifier17", type=uml_UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Class16", type=uml_UML_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute18: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute18",
    ends={
        Property(name="uml_UML_Property20", type=uml_UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Class19", type=uml_UML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge21: BinaryAssociation = BinaryAssociation(
    name="edge21",
    ends={
        Property(name="uml_UML_ActivityEdge", type=uml_UML_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Activity", type=uml_UML_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target36: BinaryAssociation = BinaryAssociation(
    name="target36",
    ends={
        Property(name="uml_UML_ActivityNode38", type=uml_UML_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_ActivityEdge37", type=uml_UML_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
specification39: BinaryAssociation = BinaryAssociation(
    name="specification39",
    ends={
        Property(name="uml_UML_OpaqueExpression", type=uml_UML_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_Constraint40", type=uml_UML_OpaqueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
role41: BinaryAssociation = BinaryAssociation(
    name="role41",
    ends={
        Property(name="uml_UML_ConnectableElement", type=uml_UML_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML_ConnectorEnd42", type=uml_UML_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_uml_UML_BehavioralFeature_UML_Feature = Generalization(general=UML_Feature, specific=uml_UML_BehavioralFeature)
gen_uml_UML_StructuralFeature_UML_Feature = Generalization(general=UML_Feature, specific=uml_UML_StructuralFeature)
gen_uml_UML_StructuralFeature_UML_TypedElement = Generalization(general=UML_TypedElement, specific=uml_UML_StructuralFeature)
gen_uml_UML_Type_UML_PackageableElement = Generalization(general=UML_PackageableElement, specific=uml_UML_Type)
gen_uml_UML_TypedElement_UML_NamedElement = Generalization(general=UML_NamedElement, specific=uml_UML_TypedElement)
gen_uml_UML_Classifier_UML_Namespace = Generalization(general=UML_Namespace, specific=uml_UML_Classifier)
gen_uml_UML_Classifier_UML_Type = Generalization(general=UML_Type, specific=uml_UML_Classifier)
gen_uml_UML_Interface_UML_Classifier = Generalization(general=UML_Classifier, specific=uml_UML_Interface)
gen_uml_UML_RedefinableElement_UML_NamedElement = Generalization(general=UML_NamedElement, specific=uml_UML_RedefinableElement)
gen_uml_UML_Feature_UML_RedefinableElement = Generalization(general=UML_RedefinableElement, specific=uml_UML_Feature)
gen_uml_UML_Namespace_UML_NamedElement = Generalization(general=UML_NamedElement, specific=uml_UML_Namespace)
gen_uml_UML_Package_UML_Namespace = Generalization(general=UML_Namespace, specific=uml_UML_Package)
gen_uml_UML_PackageableElement_UML_NamedElement = Generalization(general=UML_NamedElement, specific=uml_UML_PackageableElement)
gen_uml_UML_BehavioralFeature_UML_Namespace = Generalization(general=UML_Namespace, specific=uml_UML_BehavioralFeature)
gen_uml_UML_ConnectableElement_UML_TypedElement = Generalization(general=UML_TypedElement, specific=uml_UML_ConnectableElement)
gen_uml_UML_Connector_UML_Feature = Generalization(general=UML_Feature, specific=uml_UML_Connector)
gen_uml_UML_CallOperationAction_UML_Action = Generalization(general=UML_Action, specific=uml_UML_CallOperationAction)
gen_uml_UML_Action_UML_ActivityNode = Generalization(general=UML_ActivityNode, specific=uml_UML_Action)
gen_uml_UML_BehavioredClassifier_UML_Classifier = Generalization(general=UML_Classifier, specific=uml_UML_BehavioredClassifier)
gen_uml_UML_Operation_UML_BehavioralFeature = Generalization(general=UML_BehavioralFeature, specific=uml_UML_Operation)
gen_uml_UML_Class_UML_BehavioredClassifier = Generalization(general=UML_BehavioredClassifier, specific=uml_UML_Class)
gen_uml_UML_Property_UML_StructuralFeature = Generalization(general=UML_StructuralFeature, specific=uml_UML_Property)
gen_uml_UML_Property_UML_ConnectableElement = Generalization(general=UML_ConnectableElement, specific=uml_UML_Property)
gen_uml_UML_Port_UML_Property = Generalization(general=UML_Property, specific=uml_UML_Port)
gen_uml_UML_Behavior_UML_Class = Generalization(general=UML_Class, specific=uml_UML_Behavior)
gen_uml_UML_Activity_UML_Behavior = Generalization(general=UML_Behavior, specific=uml_UML_Activity)
gen_uml_UML_OpaqueExpression_UML_ValueSpecification = Generalization(general=UML_ValueSpecification, specific=uml_UML_OpaqueExpression)
gen_uml_UML_Constraint_UML_PackageableElement = Generalization(general=UML_PackageableElement, specific=uml_UML_Constraint)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={UML_Feature, uml_UML_StructuralFeature, UML_TypedElement, uml_UML_Type, UML_PackageableElement, uml_UML_TypedElement, uml_UML_Classifier, UML_Type, uml_UML_Interface, UML_Classifier, uml_UML_Operation, uml_UML_Property, uml_UML_InterfaceRealization, uml_UML_NamedElement, uml_UML_RedefinableElement, UML_NamedElement, uml_UML_Feature, UML_RedefinableElement, uml_UML_Namespace, uml_UML_Constraint, uml_UML_Package, UML_Namespace, uml_UML_PackageableElement, uml_UML_BehavioralFeature, uml_UML_ConnectableElement, uml_UML_Connector, uml_UML_ConnectorEnd, uml_UML_CallOperationAction, UML_Action, uml_UML_Action, UML_ActivityNode, uml_UML_BehavioredClassifier, uml_UML_Behavior, UML_BehavioralFeature, uml_UML_Class, UML_BehavioredClassifier, UML_StructuralFeature, UML_ConnectableElement, uml_UML_Port, UML_Property, UML_Class, uml_UML_Activity, UML_Behavior, uml_UML_ActivityEdge, uml_UML_ActivityNode, uml_UML_ValueSpecification, uml_UML_OpaqueExpression, UML_ValueSpecification},
    associations={type2, feature3, ownedOperation4, ownedAttribute5, ownedRule0, packagedElements1, node22, connectorEnd24, operation25, incoming28, outgoing30, source33, contract7, interfaceRealization9, ownedBehavior11, ownedOperation13, nestedClassifier15, ownedAttribute18, edge21, target36, specification39, role41},
    generalizations={gen_uml_UML_BehavioralFeature_UML_Feature, gen_uml_UML_StructuralFeature_UML_Feature, gen_uml_UML_StructuralFeature_UML_TypedElement, gen_uml_UML_Type_UML_PackageableElement, gen_uml_UML_TypedElement_UML_NamedElement, gen_uml_UML_Classifier_UML_Namespace, gen_uml_UML_Classifier_UML_Type, gen_uml_UML_Interface_UML_Classifier, gen_uml_UML_RedefinableElement_UML_NamedElement, gen_uml_UML_Feature_UML_RedefinableElement, gen_uml_UML_Namespace_UML_NamedElement, gen_uml_UML_Package_UML_Namespace, gen_uml_UML_PackageableElement_UML_NamedElement, gen_uml_UML_BehavioralFeature_UML_Namespace, gen_uml_UML_ConnectableElement_UML_TypedElement, gen_uml_UML_Connector_UML_Feature, gen_uml_UML_CallOperationAction_UML_Action, gen_uml_UML_Action_UML_ActivityNode, gen_uml_UML_BehavioredClassifier_UML_Classifier, gen_uml_UML_Operation_UML_BehavioralFeature, gen_uml_UML_Class_UML_BehavioredClassifier, gen_uml_UML_Property_UML_StructuralFeature, gen_uml_UML_Property_UML_ConnectableElement, gen_uml_UML_Port_UML_Property, gen_uml_UML_Behavior_UML_Class, gen_uml_UML_Activity_UML_Behavior, gen_uml_UML_OpaqueExpression_UML_ValueSpecification, gen_uml_UML_Constraint_UML_PackageableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)