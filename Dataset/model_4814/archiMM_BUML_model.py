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
FolderType: Enumeration = Enumeration(
    name="FolderType",
    literals={
            EnumerationLiteral(name="user"),
			EnumerationLiteral(name="business"),
			EnumerationLiteral(name="application"),
			EnumerationLiteral(name="technology"),
			EnumerationLiteral(name="connectors"),
			EnumerationLiteral(name="relations"),
			EnumerationLiteral(name="diagrams"),
			EnumerationLiteral(name="derived"),
			EnumerationLiteral(name="motivation"),
			EnumerationLiteral(name="implementation_migration")
    }
)

# Classes
model_Property = Class(name="model::Property")
model_Properties = Class(name="model::Properties", is_abstract=True)
model_Metadata = Class(name="model::Metadata")
model_Adapter = Class(name="model::Adapter", is_abstract=True)
model_Identifier = Class(name="model::Identifier", is_abstract=True)
model_ArchimateModelElement = Class(name="model::ArchimateModelElement", is_abstract=True)
Adapter = Class(name="Adapter")
model_Nameable = Class(name="model::Nameable", is_abstract=True)
model_TextContent = Class(name="model::TextContent", is_abstract=True)
model_Documentable = Class(name="model::Documentable", is_abstract=True)
model_Cloneable = Class(name="model::Cloneable", is_abstract=True)
model_FolderContainer = Class(name="model::FolderContainer", is_abstract=True)
model_Folder = Class(name="model::Folder")
model_ArchimateModel = Class(name="model::ArchimateModel")
FolderContainer = Class(name="FolderContainer")
Nameable = Class(name="Nameable")
Identifier = Class(name="Identifier")
ArchimateModelElement = Class(name="ArchimateModelElement")
Properties = Class(name="Properties")
model_AssignmentRelationship = Class(name="model::AssignmentRelationship")
model_AssociationRelationship = Class(name="model::AssociationRelationship")
model_CompositionRelationship = Class(name="model::CompositionRelationship")
model_FlowRelationship = Class(name="model::FlowRelationship")
model_RealisationRelationship = Class(name="model::RealisationRelationship")
model_SpecialisationRelationship = Class(name="model::SpecialisationRelationship")
model_TriggeringRelationship = Class(name="model::TriggeringRelationship")
model_UsedByRelationship = Class(name="model::UsedByRelationship")
model_InfluenceRelationship = Class(name="model::InfluenceRelationship")
model_BusinessLayerElement = Class(name="model::BusinessLayerElement", is_abstract=True)
model_BusinessActivity = Class(name="model::BusinessActivity")
BusinessLayerElement = Class(name="BusinessLayerElement")
Documentable = Class(name="Documentable")
model_EObject = Class(name="model::EObject")
model_ArchimateElement = Class(name="model::ArchimateElement", is_abstract=True)
Cloneable = Class(name="Cloneable")
model_JunctionElement = Class(name="model::JunctionElement", is_abstract=True)
ArchimateElement = Class(name="ArchimateElement")
model_InterfaceElement = Class(name="model::InterfaceElement", is_abstract=True)
model_ServiceElement = Class(name="model::ServiceElement", is_abstract=True)
model_Junction = Class(name="model::Junction")
JunctionElement = Class(name="JunctionElement")
model_AndJunction = Class(name="model::AndJunction")
model_OrJunction = Class(name="model::OrJunction")
model_Relationship = Class(name="model::Relationship", is_abstract=True)
model_AccessRelationship = Class(name="model::AccessRelationship")
Relationship = Class(name="Relationship")
model_AggregationRelationship = Class(name="model::AggregationRelationship")
model_InfrastructureService = Class(name="model::InfrastructureService")
model_InfrastructureFunction = Class(name="model::InfrastructureFunction")
model_Node = Class(name="model::Node")
model_SystemSoftware = Class(name="model::SystemSoftware")
model_Device = Class(name="model::Device")
model_MotivationElement = Class(name="model::MotivationElement", is_abstract=True)
model_Stakeholder = Class(name="model::Stakeholder")
MotivationElement = Class(name="MotivationElement")
model_Driver = Class(name="model::Driver")
model_Assessment = Class(name="model::Assessment")
model_Goal = Class(name="model::Goal")
model_Requirement = Class(name="model::Requirement")
model_BusinessActor = Class(name="model::BusinessActor")
model_BusinessCollaboration = Class(name="model::BusinessCollaboration")
model_Contract = Class(name="model::Contract")
model_BusinessEvent = Class(name="model::BusinessEvent")
model_BusinessFunction = Class(name="model::BusinessFunction")
model_BusinessInteraction = Class(name="model::BusinessInteraction")
model_BusinessInterface = Class(name="model::BusinessInterface")
InterfaceElement = Class(name="InterfaceElement")
model_Meaning = Class(name="model::Meaning")
model_BusinessObject = Class(name="model::BusinessObject")
model_BusinessProcess = Class(name="model::BusinessProcess")
model_Product = Class(name="model::Product")
model_Representation = Class(name="model::Representation")
model_BusinessRole = Class(name="model::BusinessRole")
model_BusinessService = Class(name="model::BusinessService")
ServiceElement = Class(name="ServiceElement")
model_Value = Class(name="model::Value")
model_Location = Class(name="model::Location")
model_ApplicationLayerElement = Class(name="model::ApplicationLayerElement", is_abstract=True)
model_ApplicationCollaboration = Class(name="model::ApplicationCollaboration")
ApplicationLayerElement = Class(name="ApplicationLayerElement")
model_ApplicationComponent = Class(name="model::ApplicationComponent")
model_ApplicationFunction = Class(name="model::ApplicationFunction")
model_ApplicationInteraction = Class(name="model::ApplicationInteraction")
model_ApplicationInterface = Class(name="model::ApplicationInterface")
model_DataObject = Class(name="model::DataObject")
model_ApplicationService = Class(name="model::ApplicationService")
model_TechnologyLayerElement = Class(name="model::TechnologyLayerElement", is_abstract=True)
model_Artifact = Class(name="model::Artifact")
TechnologyLayerElement = Class(name="TechnologyLayerElement")
model_CommunicationPath = Class(name="model::CommunicationPath")
model_Network = Class(name="model::Network")
model_InfrastructureInterface = Class(name="model::InfrastructureInterface")
model_Bounds = Class(name="model::Bounds")
model_DiagramModelConnection = Class(name="model::DiagramModelConnection")
model_Constraint = Class(name="model::Constraint")
model_Principle = Class(name="model::Principle")
model_ImplementationMigrationElement = Class(name="model::ImplementationMigrationElement", is_abstract=True)
model_WorkPackage = Class(name="model::WorkPackage")
ImplementationMigrationElement = Class(name="ImplementationMigrationElement")
model_Deliverable = Class(name="model::Deliverable")
model_Plateau = Class(name="model::Plateau")
model_Gap = Class(name="model::Gap")
model_DiagramModelComponent = Class(name="model::DiagramModelComponent", is_abstract=True)
model_DiagramModel = Class(name="model::DiagramModel", is_abstract=True)
model_DiagramModelContainer = Class(name="model::DiagramModelContainer", is_abstract=True)
DiagramModelComponent = Class(name="DiagramModelComponent")
model_DiagramModelObject = Class(name="model::DiagramModelObject", is_abstract=True)
DiagramModelContainer = Class(name="DiagramModelContainer")
model_DiagramModelReference = Class(name="model::DiagramModelReference")
DiagramModelObject = Class(name="DiagramModelObject")
FontAttribute = Class(name="FontAttribute")
LineObject = Class(name="LineObject")
model_BorderObject = Class(name="model::BorderObject", is_abstract=True)
model_DiagramModelImageProvider = Class(name="model::DiagramModelImageProvider", is_abstract=True)
model_DiagramModelGroup = Class(name="model::DiagramModelGroup")
model_DiagramModelNote = Class(name="model::DiagramModelNote")
TextContent = Class(name="TextContent")
model_DiagramModelImage = Class(name="model::DiagramModelImage")
BorderObject = Class(name="BorderObject")
DiagramModelImageProvider = Class(name="DiagramModelImageProvider")
model_DiagramModelBendpoint = Class(name="model::DiagramModelBendpoint")
model_LineObject = Class(name="model::LineObject", is_abstract=True)
model_FontAttribute = Class(name="model::FontAttribute", is_abstract=True)
model_Lockable = Class(name="model::Lockable", is_abstract=True)
model_ArchimateDiagramModel = Class(name="model::ArchimateDiagramModel")
DiagramModel = Class(name="DiagramModel")
model_DiagramModelArchimateObject = Class(name="model::DiagramModelArchimateObject")
model_DiagramModelArchimateConnection = Class(name="model::DiagramModelArchimateConnection")
DiagramModelConnection = Class(name="DiagramModelConnection")
model_SketchModel = Class(name="model::SketchModel")
model_SketchModelSticky = Class(name="model::SketchModelSticky")
model_SketchModelActor = Class(name="model::SketchModelActor")

# model_Property class attributes and methods
model_Property_key: Property = Property(name="key", type=StringType)
model_Property_value: Property = Property(name="value", type=StringType)
model_Property.attributes={model_Property_key, model_Property_value}

# model_Properties class attributes and methods

# model_Metadata class attributes and methods

# model_Adapter class attributes and methods
model_Adapter_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
model_Adapter_m_setAdapter: Method = Method(name="setAdapter", parameters={Parameter(name='object'), Parameter(name='adapter')})
model_Adapter.methods={model_Adapter_m_getAdapter, model_Adapter_m_setAdapter}

# model_Identifier class attributes and methods
model_Identifier_id: Property = Property(name="id", type=StringType)
model_Identifier.attributes={model_Identifier_id}

# model_ArchimateModelElement class attributes and methods

# Adapter class attributes and methods

# model_Nameable class attributes and methods
model_Nameable_name: Property = Property(name="name", type=StringType)
model_Nameable.attributes={model_Nameable_name}

# model_TextContent class attributes and methods
model_TextContent_content: Property = Property(name="content", type=StringType)
model_TextContent.attributes={model_TextContent_content}

# model_Documentable class attributes and methods
model_Documentable_documentation: Property = Property(name="documentation", type=StringType)
model_Documentable.attributes={model_Documentable_documentation}

# model_Cloneable class attributes and methods
model_Cloneable_m_getCopy: Method = Method(name="getCopy", parameters={}, type=StringType)
model_Cloneable.methods={model_Cloneable_m_getCopy}

# model_FolderContainer class attributes and methods

# model_Folder class attributes and methods
model_Folder_type: Property = Property(name="type", type=StringType)
model_Folder.attributes={model_Folder_type}

# model_ArchimateModel class attributes and methods
model_ArchimateModel_purpose: Property = Property(name="purpose", type=StringType)
model_ArchimateModel_file: Property = Property(name="file", type=StringType)
model_ArchimateModel_version: Property = Property(name="version", type=StringType)
model_ArchimateModel_m_getDefaultDiagramModel: Method = Method(name="getDefaultDiagramModel", parameters={}, type=StringType)
model_ArchimateModel_m_getDiagramModels: Method = Method(name="getDiagramModels", parameters={}, type=StringType)
model_ArchimateModel_m_getFolder: Method = Method(name="getFolder", parameters={Parameter(name='type')}, type=StringType)
model_ArchimateModel_m_setDefaults: Method = Method(name="setDefaults", parameters={})
model_ArchimateModel_m_addDerivedRelationsFolder: Method = Method(name="addDerivedRelationsFolder", parameters={}, type=StringType)
model_ArchimateModel_m_removeDerivedRelationsFolder: Method = Method(name="removeDerivedRelationsFolder", parameters={})
model_ArchimateModel_m_getDefaultFolderForElement: Method = Method(name="getDefaultFolderForElement", parameters={Parameter(name='element')}, type=StringType)
model_ArchimateModel.attributes={model_ArchimateModel_version, model_ArchimateModel_file, model_ArchimateModel_purpose}
model_ArchimateModel.methods={model_ArchimateModel_m_addDerivedRelationsFolder, model_ArchimateModel_m_getDiagramModels, model_ArchimateModel_m_getFolder, model_ArchimateModel_m_getDefaultDiagramModel, model_ArchimateModel_m_getDefaultFolderForElement, model_ArchimateModel_m_removeDerivedRelationsFolder, model_ArchimateModel_m_setDefaults}

# FolderContainer class attributes and methods

# Nameable class attributes and methods

# Identifier class attributes and methods

# ArchimateModelElement class attributes and methods

# Properties class attributes and methods

# model_AssignmentRelationship class attributes and methods

# model_AssociationRelationship class attributes and methods

# model_CompositionRelationship class attributes and methods

# model_FlowRelationship class attributes and methods

# model_RealisationRelationship class attributes and methods

# model_SpecialisationRelationship class attributes and methods

# model_TriggeringRelationship class attributes and methods

# model_UsedByRelationship class attributes and methods

# model_InfluenceRelationship class attributes and methods

# model_BusinessLayerElement class attributes and methods

# model_BusinessActivity class attributes and methods

# BusinessLayerElement class attributes and methods

# Documentable class attributes and methods

# model_EObject class attributes and methods

# model_ArchimateElement class attributes and methods

# Cloneable class attributes and methods

# model_JunctionElement class attributes and methods

# ArchimateElement class attributes and methods

# model_InterfaceElement class attributes and methods
model_InterfaceElement_interfaceType: Property = Property(name="interfaceType", type=IntegerType)
model_InterfaceElement.attributes={model_InterfaceElement_interfaceType}

# model_ServiceElement class attributes and methods

# model_Junction class attributes and methods

# JunctionElement class attributes and methods

# model_AndJunction class attributes and methods

# model_OrJunction class attributes and methods

# model_Relationship class attributes and methods

# model_AccessRelationship class attributes and methods
model_AccessRelationship_accessType: Property = Property(name="accessType", type=IntegerType)
model_AccessRelationship.attributes={model_AccessRelationship_accessType}

# Relationship class attributes and methods

# model_AggregationRelationship class attributes and methods

# model_InfrastructureService class attributes and methods

# model_InfrastructureFunction class attributes and methods

# model_Node class attributes and methods

# model_SystemSoftware class attributes and methods

# model_Device class attributes and methods

# model_MotivationElement class attributes and methods

# model_Stakeholder class attributes and methods

# MotivationElement class attributes and methods

# model_Driver class attributes and methods

# model_Assessment class attributes and methods

# model_Goal class attributes and methods

# model_Requirement class attributes and methods

# model_BusinessActor class attributes and methods

# model_BusinessCollaboration class attributes and methods

# model_Contract class attributes and methods

# model_BusinessEvent class attributes and methods

# model_BusinessFunction class attributes and methods

# model_BusinessInteraction class attributes and methods

# model_BusinessInterface class attributes and methods

# InterfaceElement class attributes and methods

# model_Meaning class attributes and methods

# model_BusinessObject class attributes and methods

# model_BusinessProcess class attributes and methods

# model_Product class attributes and methods

# model_Representation class attributes and methods

# model_BusinessRole class attributes and methods

# model_BusinessService class attributes and methods

# ServiceElement class attributes and methods

# model_Value class attributes and methods

# model_Location class attributes and methods

# model_ApplicationLayerElement class attributes and methods

# model_ApplicationCollaboration class attributes and methods

# ApplicationLayerElement class attributes and methods

# model_ApplicationComponent class attributes and methods

# model_ApplicationFunction class attributes and methods

# model_ApplicationInteraction class attributes and methods

# model_ApplicationInterface class attributes and methods

# model_DataObject class attributes and methods

# model_ApplicationService class attributes and methods

# model_TechnologyLayerElement class attributes and methods

# model_Artifact class attributes and methods

# TechnologyLayerElement class attributes and methods

# model_CommunicationPath class attributes and methods

# model_Network class attributes and methods

# model_InfrastructureInterface class attributes and methods

# model_Bounds class attributes and methods
model_Bounds_x: Property = Property(name="x", type=IntegerType)
model_Bounds_y: Property = Property(name="y", type=IntegerType)
model_Bounds_width: Property = Property(name="width", type=IntegerType)
model_Bounds_height: Property = Property(name="height", type=IntegerType)
model_Bounds_m_getCopy: Method = Method(name="getCopy", parameters={}, type=StringType)
model_Bounds.attributes={model_Bounds_width, model_Bounds_x, model_Bounds_height, model_Bounds_y}
model_Bounds.methods={model_Bounds_m_getCopy}

# model_DiagramModelConnection class attributes and methods
model_DiagramModelConnection_text: Property = Property(name="text", type=StringType)
model_DiagramModelConnection_type: Property = Property(name="type", type=IntegerType)
model_DiagramModelConnection_m_connect: Method = Method(name="connect", parameters={Parameter(name='source'), Parameter(name='target')})
model_DiagramModelConnection_m_disconnect: Method = Method(name="disconnect", parameters={})
model_DiagramModelConnection_m_reconnect: Method = Method(name="reconnect", parameters={})
model_DiagramModelConnection.attributes={model_DiagramModelConnection_text, model_DiagramModelConnection_type}
model_DiagramModelConnection.methods={model_DiagramModelConnection_m_reconnect, model_DiagramModelConnection_m_disconnect, model_DiagramModelConnection_m_connect}

# model_Constraint class attributes and methods

# model_Principle class attributes and methods

# model_ImplementationMigrationElement class attributes and methods

# model_WorkPackage class attributes and methods

# ImplementationMigrationElement class attributes and methods

# model_Deliverable class attributes and methods

# model_Plateau class attributes and methods

# model_Gap class attributes and methods

# model_DiagramModelComponent class attributes and methods

# model_DiagramModel class attributes and methods
model_DiagramModel_connectionRouterType: Property = Property(name="connectionRouterType", type=IntegerType)
model_DiagramModel.attributes={model_DiagramModel_connectionRouterType}

# model_DiagramModelContainer class attributes and methods

# DiagramModelComponent class attributes and methods

# model_DiagramModelObject class attributes and methods
model_DiagramModelObject_fillColor: Property = Property(name="fillColor", type=StringType)
model_DiagramModelObject_m_addConnection: Method = Method(name="addConnection", parameters={Parameter(name='connection')})
model_DiagramModelObject_m_removeConnection: Method = Method(name="removeConnection", parameters={Parameter(name='connection')})
model_DiagramModelObject_m_setBounds: Method = Method(name="setBounds", parameters={Parameter(name='x'), Parameter(name='width'), Parameter(name='y'), Parameter(name='height')})
model_DiagramModelObject.attributes={model_DiagramModelObject_fillColor}
model_DiagramModelObject.methods={model_DiagramModelObject_m_removeConnection, model_DiagramModelObject_m_addConnection, model_DiagramModelObject_m_setBounds}

# DiagramModelContainer class attributes and methods

# model_DiagramModelReference class attributes and methods

# DiagramModelObject class attributes and methods

# FontAttribute class attributes and methods

# LineObject class attributes and methods

# model_BorderObject class attributes and methods
model_BorderObject_borderColor: Property = Property(name="borderColor", type=StringType)
model_BorderObject.attributes={model_BorderObject_borderColor}

# model_DiagramModelImageProvider class attributes and methods
model_DiagramModelImageProvider_imagePath: Property = Property(name="imagePath", type=StringType)
model_DiagramModelImageProvider.attributes={model_DiagramModelImageProvider_imagePath}

# model_DiagramModelGroup class attributes and methods

# model_DiagramModelNote class attributes and methods

# TextContent class attributes and methods

# model_DiagramModelImage class attributes and methods

# BorderObject class attributes and methods

# DiagramModelImageProvider class attributes and methods

# model_DiagramModelBendpoint class attributes and methods
model_DiagramModelBendpoint_startX: Property = Property(name="startX", type=IntegerType)
model_DiagramModelBendpoint_startY: Property = Property(name="startY", type=IntegerType)
model_DiagramModelBendpoint_endX: Property = Property(name="endX", type=IntegerType)
model_DiagramModelBendpoint_endY: Property = Property(name="endY", type=IntegerType)
model_DiagramModelBendpoint.attributes={model_DiagramModelBendpoint_endY, model_DiagramModelBendpoint_endX, model_DiagramModelBendpoint_startX, model_DiagramModelBendpoint_startY}

# model_LineObject class attributes and methods
model_LineObject_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
model_LineObject_lineColor: Property = Property(name="lineColor", type=StringType)
model_LineObject.attributes={model_LineObject_lineWidth, model_LineObject_lineColor}

# model_FontAttribute class attributes and methods
model_FontAttribute_font: Property = Property(name="font", type=StringType)
model_FontAttribute_fontColor: Property = Property(name="fontColor", type=StringType)
model_FontAttribute_textAlignment: Property = Property(name="textAlignment", type=IntegerType)
model_FontAttribute_textPosition: Property = Property(name="textPosition", type=IntegerType)
model_FontAttribute_m_getDefaultTextAlignment: Method = Method(name="getDefaultTextAlignment", parameters={}, type=IntegerType)
model_FontAttribute.attributes={model_FontAttribute_font, model_FontAttribute_textAlignment, model_FontAttribute_textPosition, model_FontAttribute_fontColor}
model_FontAttribute.methods={model_FontAttribute_m_getDefaultTextAlignment}

# model_Lockable class attributes and methods
model_Lockable_locked: Property = Property(name="locked", type=BooleanType)
model_Lockable.attributes={model_Lockable_locked}

# model_ArchimateDiagramModel class attributes and methods
model_ArchimateDiagramModel_viewpoint: Property = Property(name="viewpoint", type=IntegerType)
model_ArchimateDiagramModel.attributes={model_ArchimateDiagramModel_viewpoint}

# DiagramModel class attributes and methods

# model_DiagramModelArchimateObject class attributes and methods
model_DiagramModelArchimateObject_type: Property = Property(name="type", type=IntegerType)
model_DiagramModelArchimateObject_m_addArchimateElementToModel: Method = Method(name="addArchimateElementToModel", parameters={Parameter(name='parent')})
model_DiagramModelArchimateObject_m_removeArchimateElementFromModel: Method = Method(name="removeArchimateElementFromModel", parameters={})
model_DiagramModelArchimateObject.attributes={model_DiagramModelArchimateObject_type}
model_DiagramModelArchimateObject.methods={model_DiagramModelArchimateObject_m_addArchimateElementToModel, model_DiagramModelArchimateObject_m_removeArchimateElementFromModel}

# model_DiagramModelArchimateConnection class attributes and methods
model_DiagramModelArchimateConnection_m_addRelationshipToModel: Method = Method(name="addRelationshipToModel", parameters={Parameter(name='parent')})
model_DiagramModelArchimateConnection_m_removeRelationshipFromModel: Method = Method(name="removeRelationshipFromModel", parameters={})
model_DiagramModelArchimateConnection.methods={model_DiagramModelArchimateConnection_m_addRelationshipToModel, model_DiagramModelArchimateConnection_m_removeRelationshipFromModel}

# DiagramModelConnection class attributes and methods

# model_SketchModel class attributes and methods
model_SketchModel_background: Property = Property(name="background", type=IntegerType)
model_SketchModel.attributes={model_SketchModel_background}

# model_SketchModelSticky class attributes and methods

# model_SketchModelActor class attributes and methods

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="model_Property", type=model_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Properties", type=model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries1: BinaryAssociation = BinaryAssociation(
    name="entries1",
    ends={
        Property(name="model_Property2", type=model_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Metadata", type=model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata4: BinaryAssociation = BinaryAssociation(
    name="metadata4",
    ends={
        Property(name="model_Metadata5", type=model_ArchimateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArchimateModel", type=model_Metadata, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
folders3: BinaryAssociation = BinaryAssociation(
    name="folders3",
    ends={
        Property(name="model_Folder", type=model_FolderContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FolderContainer", type=model_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archimateModel6: BinaryAssociation = BinaryAssociation(
    name="archimateModel6",
    ends={
        Property(name="model_ArchimateModel7", type=model_ArchimateModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArchimateModelElement", type=model_ArchimateModel, multiplicity=Multiplicity(0, 1))
    }
)
elements8: BinaryAssociation = BinaryAssociation(
    name="elements8",
    ends={
        Property(name="model_EObject", type=model_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Folder9", type=model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="model_ArchimateElement", type=model_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Relationship", type=model_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="model_ArchimateElement13", type=model_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Relationship12", type=model_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
bounds18: BinaryAssociation = BinaryAssociation(
    name="bounds18",
    ends={
        Property(name="model_Bounds", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject19", type=model_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceConnections20: BinaryAssociation = BinaryAssociation(
    name="sourceConnections20",
    ends={
        Property(name="model_DiagramModelConnection", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject21", type=model_DiagramModelConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetConnections22: BinaryAssociation = BinaryAssociation(
    name="targetConnections22",
    ends={
        Property(name="model_DiagramModelConnection24", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject23", type=model_DiagramModelConnection, multiplicity=Multiplicity(0, 9999))
    }
)
diagramModel14: BinaryAssociation = BinaryAssociation(
    name="diagramModel14",
    ends={
        Property(name="model_DiagramModel", type=model_DiagramModelComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelComponent", type=model_DiagramModel, multiplicity=Multiplicity(0, 1))
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="model_DiagramModelObject", type=model_DiagramModelContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelContainer", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModel16: BinaryAssociation = BinaryAssociation(
    name="referencedModel16",
    ends={
        Property(name="model_DiagramModel17", type=model_DiagramModelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelReference", type=model_DiagramModel, multiplicity=Multiplicity(0, 1))
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="model_DiagramModelObject27", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection26", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="model_DiagramModelObject30", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection29", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 1))
    }
)
bendpoints31: BinaryAssociation = BinaryAssociation(
    name="bendpoints31",
    ends={
        Property(name="model_DiagramModelBendpoint", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection32", type=model_DiagramModelBendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archimateElement33: BinaryAssociation = BinaryAssociation(
    name="archimateElement33",
    ends={
        Property(name="model_ArchimateElement34", type=model_DiagramModelArchimateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelArchimateObject", type=model_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
relationship35: BinaryAssociation = BinaryAssociation(
    name="relationship35",
    ends={
        Property(name="model_Relationship36", type=model_DiagramModelArchimateConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelArchimateConnection", type=model_Relationship, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_ArchimateModelElement_Adapter = Generalization(general=Adapter, specific=model_ArchimateModelElement)
gen_model_ArchimateModel_FolderContainer = Generalization(general=FolderContainer, specific=model_ArchimateModel)
gen_model_ArchimateModel_Nameable = Generalization(general=Nameable, specific=model_ArchimateModel)
gen_model_ArchimateModel_Identifier = Generalization(general=Identifier, specific=model_ArchimateModel)
gen_model_ArchimateModel_ArchimateModelElement = Generalization(general=ArchimateModelElement, specific=model_ArchimateModel)
gen_model_ArchimateModel_Properties = Generalization(general=Properties, specific=model_ArchimateModel)
gen_model_AssignmentRelationship_Relationship = Generalization(general=Relationship, specific=model_AssignmentRelationship)
gen_model_AssociationRelationship_Relationship = Generalization(general=Relationship, specific=model_AssociationRelationship)
gen_model_CompositionRelationship_Relationship = Generalization(general=Relationship, specific=model_CompositionRelationship)
gen_model_FlowRelationship_Relationship = Generalization(general=Relationship, specific=model_FlowRelationship)
gen_model_RealisationRelationship_Relationship = Generalization(general=Relationship, specific=model_RealisationRelationship)
gen_model_SpecialisationRelationship_Relationship = Generalization(general=Relationship, specific=model_SpecialisationRelationship)
gen_model_TriggeringRelationship_Relationship = Generalization(general=Relationship, specific=model_TriggeringRelationship)
gen_model_UsedByRelationship_Relationship = Generalization(general=Relationship, specific=model_UsedByRelationship)
gen_model_InfluenceRelationship_Relationship = Generalization(general=Relationship, specific=model_InfluenceRelationship)
gen_model_BusinessLayerElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_BusinessLayerElement)
gen_model_BusinessActivity_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessActivity)
gen_model_Folder_ArchimateModelElement = Generalization(general=ArchimateModelElement, specific=model_Folder)
gen_model_Folder_FolderContainer = Generalization(general=FolderContainer, specific=model_Folder)
gen_model_Folder_Nameable = Generalization(general=Nameable, specific=model_Folder)
gen_model_Folder_Identifier = Generalization(general=Identifier, specific=model_Folder)
gen_model_Folder_Documentable = Generalization(general=Documentable, specific=model_Folder)
gen_model_Folder_Properties = Generalization(general=Properties, specific=model_Folder)
gen_model_ArchimateElement_ArchimateModelElement = Generalization(general=ArchimateModelElement, specific=model_ArchimateElement)
gen_model_ArchimateElement_Identifier = Generalization(general=Identifier, specific=model_ArchimateElement)
gen_model_ArchimateElement_Cloneable = Generalization(general=Cloneable, specific=model_ArchimateElement)
gen_model_ArchimateElement_Nameable = Generalization(general=Nameable, specific=model_ArchimateElement)
gen_model_ArchimateElement_Documentable = Generalization(general=Documentable, specific=model_ArchimateElement)
gen_model_ArchimateElement_Properties = Generalization(general=Properties, specific=model_ArchimateElement)
gen_model_JunctionElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_JunctionElement)
gen_model_InterfaceElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_InterfaceElement)
gen_model_ServiceElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_ServiceElement)
gen_model_Junction_JunctionElement = Generalization(general=JunctionElement, specific=model_Junction)
gen_model_AndJunction_JunctionElement = Generalization(general=JunctionElement, specific=model_AndJunction)
gen_model_OrJunction_JunctionElement = Generalization(general=JunctionElement, specific=model_OrJunction)
gen_model_Relationship_ArchimateElement = Generalization(general=ArchimateElement, specific=model_Relationship)
gen_model_AccessRelationship_Relationship = Generalization(general=Relationship, specific=model_AccessRelationship)
gen_model_AggregationRelationship_Relationship = Generalization(general=Relationship, specific=model_AggregationRelationship)
gen_model_InfrastructureService_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_InfrastructureService)
gen_model_InfrastructureService_ServiceElement = Generalization(general=ServiceElement, specific=model_InfrastructureService)
gen_model_InfrastructureFunction_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_InfrastructureFunction)
gen_model_Node_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_Node)
gen_model_SystemSoftware_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_SystemSoftware)
gen_model_Device_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_Device)
gen_model_MotivationElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_MotivationElement)
gen_model_Stakeholder_MotivationElement = Generalization(general=MotivationElement, specific=model_Stakeholder)
gen_model_Driver_MotivationElement = Generalization(general=MotivationElement, specific=model_Driver)
gen_model_Assessment_MotivationElement = Generalization(general=MotivationElement, specific=model_Assessment)
gen_model_Goal_MotivationElement = Generalization(general=MotivationElement, specific=model_Goal)
gen_model_Requirement_MotivationElement = Generalization(general=MotivationElement, specific=model_Requirement)
gen_model_BusinessActor_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessActor)
gen_model_BusinessCollaboration_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessCollaboration)
gen_model_Contract_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_Contract)
gen_model_BusinessEvent_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessEvent)
gen_model_BusinessFunction_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessFunction)
gen_model_BusinessInteraction_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessInteraction)
gen_model_BusinessInterface_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessInterface)
gen_model_BusinessInterface_InterfaceElement = Generalization(general=InterfaceElement, specific=model_BusinessInterface)
gen_model_Meaning_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_Meaning)
gen_model_BusinessObject_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessObject)
gen_model_BusinessProcess_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessProcess)
gen_model_Product_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_Product)
gen_model_Representation_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_Representation)
gen_model_BusinessRole_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessRole)
gen_model_BusinessService_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_BusinessService)
gen_model_BusinessService_ServiceElement = Generalization(general=ServiceElement, specific=model_BusinessService)
gen_model_Value_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_Value)
gen_model_Location_BusinessLayerElement = Generalization(general=BusinessLayerElement, specific=model_Location)
gen_model_ApplicationLayerElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_ApplicationLayerElement)
gen_model_ApplicationCollaboration_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_ApplicationCollaboration)
gen_model_ApplicationComponent_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_ApplicationComponent)
gen_model_ApplicationFunction_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_ApplicationFunction)
gen_model_ApplicationInteraction_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_ApplicationInteraction)
gen_model_ApplicationInterface_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_ApplicationInterface)
gen_model_ApplicationInterface_InterfaceElement = Generalization(general=InterfaceElement, specific=model_ApplicationInterface)
gen_model_DataObject_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_DataObject)
gen_model_ApplicationService_ApplicationLayerElement = Generalization(general=ApplicationLayerElement, specific=model_ApplicationService)
gen_model_ApplicationService_ServiceElement = Generalization(general=ServiceElement, specific=model_ApplicationService)
gen_model_TechnologyLayerElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_TechnologyLayerElement)
gen_model_Artifact_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_Artifact)
gen_model_CommunicationPath_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_CommunicationPath)
gen_model_Network_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_Network)
gen_model_InfrastructureInterface_TechnologyLayerElement = Generalization(general=TechnologyLayerElement, specific=model_InfrastructureInterface)
gen_model_InfrastructureInterface_InterfaceElement = Generalization(general=InterfaceElement, specific=model_InfrastructureInterface)
gen_model_Constraint_MotivationElement = Generalization(general=MotivationElement, specific=model_Constraint)
gen_model_Principle_MotivationElement = Generalization(general=MotivationElement, specific=model_Principle)
gen_model_ImplementationMigrationElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_ImplementationMigrationElement)
gen_model_WorkPackage_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_WorkPackage)
gen_model_Deliverable_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_Deliverable)
gen_model_Plateau_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_Plateau)
gen_model_Gap_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_Gap)
gen_model_DiagramModelComponent_Identifier = Generalization(general=Identifier, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Cloneable = Generalization(general=Cloneable, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Adapter = Generalization(general=Adapter, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Nameable = Generalization(general=Nameable, specific=model_DiagramModelComponent)
gen_model_DiagramModelContainer_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_DiagramModelContainer)
gen_model_DiagramModel_ArchimateModelElement = Generalization(general=ArchimateModelElement, specific=model_DiagramModel)
gen_model_DiagramModel_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModel)
gen_model_DiagramModel_Documentable = Generalization(general=Documentable, specific=model_DiagramModel)
gen_model_DiagramModel_Properties = Generalization(general=Properties, specific=model_DiagramModel)
gen_model_DiagramModelReference_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelReference)
gen_model_DiagramModelObject_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_DiagramModelObject)
gen_model_DiagramModelObject_FontAttribute = Generalization(general=FontAttribute, specific=model_DiagramModelObject)
gen_model_DiagramModelObject_LineObject = Generalization(general=LineObject, specific=model_DiagramModelObject)
gen_model_DiagramModelGroup_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelGroup)
gen_model_DiagramModelGroup_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModelGroup)
gen_model_DiagramModelGroup_Documentable = Generalization(general=Documentable, specific=model_DiagramModelGroup)
gen_model_DiagramModelGroup_Properties = Generalization(general=Properties, specific=model_DiagramModelGroup)
gen_model_DiagramModelNote_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelNote)
gen_model_DiagramModelNote_TextContent = Generalization(general=TextContent, specific=model_DiagramModelNote)
gen_model_DiagramModelImage_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelImage)
gen_model_DiagramModelImage_BorderObject = Generalization(general=BorderObject, specific=model_DiagramModelImage)
gen_model_DiagramModelImage_DiagramModelImageProvider = Generalization(general=DiagramModelImageProvider, specific=model_DiagramModelImage)
gen_model_DiagramModelConnection_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_FontAttribute = Generalization(general=FontAttribute, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_Properties = Generalization(general=Properties, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_Documentable = Generalization(general=Documentable, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_LineObject = Generalization(general=LineObject, specific=model_DiagramModelConnection)
gen_model_DiagramModelBendpoint_Cloneable = Generalization(general=Cloneable, specific=model_DiagramModelBendpoint)
gen_model_ArchimateDiagramModel_DiagramModel = Generalization(general=DiagramModel, specific=model_ArchimateDiagramModel)
gen_model_DiagramModelArchimateObject_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelArchimateObject)
gen_model_DiagramModelArchimateObject_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModelArchimateObject)
gen_model_DiagramModelArchimateConnection_DiagramModelConnection = Generalization(general=DiagramModelConnection, specific=model_DiagramModelArchimateConnection)
gen_model_SketchModel_DiagramModel = Generalization(general=DiagramModel, specific=model_SketchModel)
gen_model_SketchModelSticky_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_TextContent = Generalization(general=TextContent, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_Properties = Generalization(general=Properties, specific=model_SketchModelSticky)
gen_model_SketchModelActor_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_SketchModelActor)
gen_model_SketchModelActor_Documentable = Generalization(general=Documentable, specific=model_SketchModelActor)
gen_model_SketchModelActor_Properties = Generalization(general=Properties, specific=model_SketchModelActor)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Property, model_Properties, model_Metadata, model_Adapter, model_Identifier, model_ArchimateModelElement, Adapter, model_Nameable, model_TextContent, model_Documentable, model_Cloneable, model_FolderContainer, model_Folder, model_ArchimateModel, FolderContainer, Nameable, Identifier, ArchimateModelElement, Properties, model_AssignmentRelationship, model_AssociationRelationship, model_CompositionRelationship, model_FlowRelationship, model_RealisationRelationship, model_SpecialisationRelationship, model_TriggeringRelationship, model_UsedByRelationship, model_InfluenceRelationship, model_BusinessLayerElement, model_BusinessActivity, BusinessLayerElement, Documentable, model_EObject, model_ArchimateElement, Cloneable, model_JunctionElement, ArchimateElement, model_InterfaceElement, model_ServiceElement, model_Junction, JunctionElement, model_AndJunction, model_OrJunction, model_Relationship, model_AccessRelationship, Relationship, model_AggregationRelationship, model_InfrastructureService, model_InfrastructureFunction, model_Node, model_SystemSoftware, model_Device, model_MotivationElement, model_Stakeholder, MotivationElement, model_Driver, model_Assessment, model_Goal, model_Requirement, model_BusinessActor, model_BusinessCollaboration, model_Contract, model_BusinessEvent, model_BusinessFunction, model_BusinessInteraction, model_BusinessInterface, InterfaceElement, model_Meaning, model_BusinessObject, model_BusinessProcess, model_Product, model_Representation, model_BusinessRole, model_BusinessService, ServiceElement, model_Value, model_Location, model_ApplicationLayerElement, model_ApplicationCollaboration, ApplicationLayerElement, model_ApplicationComponent, model_ApplicationFunction, model_ApplicationInteraction, model_ApplicationInterface, model_DataObject, model_ApplicationService, model_TechnologyLayerElement, model_Artifact, TechnologyLayerElement, model_CommunicationPath, model_Network, model_InfrastructureInterface, model_Bounds, model_DiagramModelConnection, model_Constraint, model_Principle, model_ImplementationMigrationElement, model_WorkPackage, ImplementationMigrationElement, model_Deliverable, model_Plateau, model_Gap, model_DiagramModelComponent, model_DiagramModel, model_DiagramModelContainer, DiagramModelComponent, model_DiagramModelObject, DiagramModelContainer, model_DiagramModelReference, DiagramModelObject, FontAttribute, LineObject, model_BorderObject, model_DiagramModelImageProvider, model_DiagramModelGroup, model_DiagramModelNote, TextContent, model_DiagramModelImage, BorderObject, DiagramModelImageProvider, model_DiagramModelBendpoint, model_LineObject, model_FontAttribute, model_Lockable, model_ArchimateDiagramModel, DiagramModel, model_DiagramModelArchimateObject, model_DiagramModelArchimateConnection, DiagramModelConnection, model_SketchModel, model_SketchModelSticky, model_SketchModelActor, FolderType},
    associations={properties0, entries1, metadata4, folders3, archimateModel6, elements8, source10, target11, bounds18, sourceConnections20, targetConnections22, diagramModel14, children15, referencedModel16, source25, target28, bendpoints31, archimateElement33, relationship35},
    generalizations={gen_model_ArchimateModelElement_Adapter, gen_model_ArchimateModel_FolderContainer, gen_model_ArchimateModel_Nameable, gen_model_ArchimateModel_Identifier, gen_model_ArchimateModel_ArchimateModelElement, gen_model_ArchimateModel_Properties, gen_model_AssignmentRelationship_Relationship, gen_model_AssociationRelationship_Relationship, gen_model_CompositionRelationship_Relationship, gen_model_FlowRelationship_Relationship, gen_model_RealisationRelationship_Relationship, gen_model_SpecialisationRelationship_Relationship, gen_model_TriggeringRelationship_Relationship, gen_model_UsedByRelationship_Relationship, gen_model_InfluenceRelationship_Relationship, gen_model_BusinessLayerElement_ArchimateElement, gen_model_BusinessActivity_BusinessLayerElement, gen_model_Folder_ArchimateModelElement, gen_model_Folder_FolderContainer, gen_model_Folder_Nameable, gen_model_Folder_Identifier, gen_model_Folder_Documentable, gen_model_Folder_Properties, gen_model_ArchimateElement_ArchimateModelElement, gen_model_ArchimateElement_Identifier, gen_model_ArchimateElement_Cloneable, gen_model_ArchimateElement_Nameable, gen_model_ArchimateElement_Documentable, gen_model_ArchimateElement_Properties, gen_model_JunctionElement_ArchimateElement, gen_model_InterfaceElement_ArchimateElement, gen_model_ServiceElement_ArchimateElement, gen_model_Junction_JunctionElement, gen_model_AndJunction_JunctionElement, gen_model_OrJunction_JunctionElement, gen_model_Relationship_ArchimateElement, gen_model_AccessRelationship_Relationship, gen_model_AggregationRelationship_Relationship, gen_model_InfrastructureService_TechnologyLayerElement, gen_model_InfrastructureService_ServiceElement, gen_model_InfrastructureFunction_TechnologyLayerElement, gen_model_Node_TechnologyLayerElement, gen_model_SystemSoftware_TechnologyLayerElement, gen_model_Device_TechnologyLayerElement, gen_model_MotivationElement_ArchimateElement, gen_model_Stakeholder_MotivationElement, gen_model_Driver_MotivationElement, gen_model_Assessment_MotivationElement, gen_model_Goal_MotivationElement, gen_model_Requirement_MotivationElement, gen_model_BusinessActor_BusinessLayerElement, gen_model_BusinessCollaboration_BusinessLayerElement, gen_model_Contract_BusinessLayerElement, gen_model_BusinessEvent_BusinessLayerElement, gen_model_BusinessFunction_BusinessLayerElement, gen_model_BusinessInteraction_BusinessLayerElement, gen_model_BusinessInterface_BusinessLayerElement, gen_model_BusinessInterface_InterfaceElement, gen_model_Meaning_BusinessLayerElement, gen_model_BusinessObject_BusinessLayerElement, gen_model_BusinessProcess_BusinessLayerElement, gen_model_Product_BusinessLayerElement, gen_model_Representation_BusinessLayerElement, gen_model_BusinessRole_BusinessLayerElement, gen_model_BusinessService_BusinessLayerElement, gen_model_BusinessService_ServiceElement, gen_model_Value_BusinessLayerElement, gen_model_Location_BusinessLayerElement, gen_model_ApplicationLayerElement_ArchimateElement, gen_model_ApplicationCollaboration_ApplicationLayerElement, gen_model_ApplicationComponent_ApplicationLayerElement, gen_model_ApplicationFunction_ApplicationLayerElement, gen_model_ApplicationInteraction_ApplicationLayerElement, gen_model_ApplicationInterface_ApplicationLayerElement, gen_model_ApplicationInterface_InterfaceElement, gen_model_DataObject_ApplicationLayerElement, gen_model_ApplicationService_ApplicationLayerElement, gen_model_ApplicationService_ServiceElement, gen_model_TechnologyLayerElement_ArchimateElement, gen_model_Artifact_TechnologyLayerElement, gen_model_CommunicationPath_TechnologyLayerElement, gen_model_Network_TechnologyLayerElement, gen_model_InfrastructureInterface_TechnologyLayerElement, gen_model_InfrastructureInterface_InterfaceElement, gen_model_Constraint_MotivationElement, gen_model_Principle_MotivationElement, gen_model_ImplementationMigrationElement_ArchimateElement, gen_model_WorkPackage_ImplementationMigrationElement, gen_model_Deliverable_ImplementationMigrationElement, gen_model_Plateau_ImplementationMigrationElement, gen_model_Gap_ImplementationMigrationElement, gen_model_DiagramModelComponent_Identifier, gen_model_DiagramModelComponent_Cloneable, gen_model_DiagramModelComponent_Adapter, gen_model_DiagramModelComponent_Nameable, gen_model_DiagramModelContainer_DiagramModelComponent, gen_model_DiagramModel_ArchimateModelElement, gen_model_DiagramModel_DiagramModelContainer, gen_model_DiagramModel_Documentable, gen_model_DiagramModel_Properties, gen_model_DiagramModelReference_DiagramModelObject, gen_model_DiagramModelObject_DiagramModelComponent, gen_model_DiagramModelObject_FontAttribute, gen_model_DiagramModelObject_LineObject, gen_model_DiagramModelGroup_DiagramModelObject, gen_model_DiagramModelGroup_DiagramModelContainer, gen_model_DiagramModelGroup_Documentable, gen_model_DiagramModelGroup_Properties, gen_model_DiagramModelNote_DiagramModelObject, gen_model_DiagramModelNote_TextContent, gen_model_DiagramModelImage_DiagramModelObject, gen_model_DiagramModelImage_BorderObject, gen_model_DiagramModelImage_DiagramModelImageProvider, gen_model_DiagramModelConnection_DiagramModelComponent, gen_model_DiagramModelConnection_FontAttribute, gen_model_DiagramModelConnection_Properties, gen_model_DiagramModelConnection_Documentable, gen_model_DiagramModelConnection_LineObject, gen_model_DiagramModelBendpoint_Cloneable, gen_model_ArchimateDiagramModel_DiagramModel, gen_model_DiagramModelArchimateObject_DiagramModelObject, gen_model_DiagramModelArchimateObject_DiagramModelContainer, gen_model_DiagramModelArchimateConnection_DiagramModelConnection, gen_model_SketchModel_DiagramModel, gen_model_SketchModelSticky_DiagramModelObject, gen_model_SketchModelSticky_DiagramModelContainer, gen_model_SketchModelSticky_TextContent, gen_model_SketchModelSticky_Properties, gen_model_SketchModelActor_DiagramModelObject, gen_model_SketchModelActor_Documentable, gen_model_SketchModelActor_Properties},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)