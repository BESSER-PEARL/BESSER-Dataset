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
			EnumerationLiteral(name="strategy"),
			EnumerationLiteral(name="business"),
			EnumerationLiteral(name="application"),
			EnumerationLiteral(name="technology"),
			EnumerationLiteral(name="relations"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="diagrams"),
			EnumerationLiteral(name="motivation"),
			EnumerationLiteral(name="implementation_migration")
    }
)

# Classes
model_Adapter = Class(name="model::Adapter", is_abstract=True)
model_Identifier = Class(name="model::Identifier", is_abstract=True)
model_Property = Class(name="model::Property")
model_Properties = Class(name="model::Properties", is_abstract=True)
model_Metadata = Class(name="model::Metadata")
model_Nameable = Class(name="model::Nameable", is_abstract=True)
model_TextContent = Class(name="model::TextContent", is_abstract=True)
model_Documentable = Class(name="model::Documentable", is_abstract=True)
model_Cloneable = Class(name="model::Cloneable", is_abstract=True)
model_FolderContainer = Class(name="model::FolderContainer", is_abstract=True)
model_Folder = Class(name="model::Folder")
ArchimateModelObject = Class(name="ArchimateModelObject")
FolderContainer = Class(name="FolderContainer")
Documentable = Class(name="Documentable")
Properties = Class(name="Properties")
model_EObject = Class(name="model::EObject")
model_ArchimateModelObject = Class(name="model::ArchimateModelObject", is_abstract=True)
Adapter = Class(name="Adapter")
Nameable = Class(name="Nameable")
Identifier = Class(name="Identifier")
model_ArchimateConcept = Class(name="model::ArchimateConcept", is_abstract=True)
Cloneable = Class(name="Cloneable")
model_ArchimateElement = Class(name="model::ArchimateElement", is_abstract=True)
ArchimateConcept = Class(name="ArchimateConcept")
model_ArchimateRelationship = Class(name="model::ArchimateRelationship", is_abstract=True)
model_StrategyElement = Class(name="model::StrategyElement", is_abstract=True)
ArchimateElement = Class(name="ArchimateElement")
model_BusinessElement = Class(name="model::BusinessElement", is_abstract=True)
model_ApplicationElement = Class(name="model::ApplicationElement", is_abstract=True)
model_TechnologyElement = Class(name="model::TechnologyElement", is_abstract=True)
model_TechnologyObject = Class(name="model::TechnologyObject", is_abstract=True)
TechnologyElement = Class(name="TechnologyElement")
PassiveStructureElement = Class(name="PassiveStructureElement")
model_PhysicalElement = Class(name="model::PhysicalElement", is_abstract=True)
model_MotivationElement = Class(name="model::MotivationElement", is_abstract=True)
model_ImplementationMigrationElement = Class(name="model::ImplementationMigrationElement", is_abstract=True)
model_CompositeElement = Class(name="model::CompositeElement", is_abstract=True)
model_BehaviorElement = Class(name="model::BehaviorElement", is_abstract=True)
model_StructureElement = Class(name="model::StructureElement", is_abstract=True)
model_ActiveStructureElement = Class(name="model::ActiveStructureElement", is_abstract=True)
StructureElement = Class(name="StructureElement")
model_PassiveStructureElement = Class(name="model::PassiveStructureElement", is_abstract=True)
model_StructuralRelationship = Class(name="model::StructuralRelationship", is_abstract=True)
ArchimateRelationship = Class(name="ArchimateRelationship")
model_DependendencyRelationship = Class(name="model::DependendencyRelationship", is_abstract=True)
model_DynamicRelationship = Class(name="model::DynamicRelationship", is_abstract=True)
model_OtherRelationship = Class(name="model::OtherRelationship", is_abstract=True)
model_ArchimateModel = Class(name="model::ArchimateModel")
model_DataObject = Class(name="model::DataObject")
model_Junction = Class(name="model::Junction")
model_ApplicationCollaboration = Class(name="model::ApplicationCollaboration")
ApplicationElement = Class(name="ApplicationElement")
ActiveStructureElement = Class(name="ActiveStructureElement")
model_ApplicationComponent = Class(name="model::ApplicationComponent")
model_ApplicationEvent = Class(name="model::ApplicationEvent")
BehaviorElement = Class(name="BehaviorElement")
model_ApplicationFunction = Class(name="model::ApplicationFunction")
model_ApplicationInteraction = Class(name="model::ApplicationInteraction")
model_ApplicationInterface = Class(name="model::ApplicationInterface")
model_ApplicationProcess = Class(name="model::ApplicationProcess")
model_ApplicationService = Class(name="model::ApplicationService")
model_Artifact = Class(name="model::Artifact")
TechnologyObject = Class(name="TechnologyObject")
model_Assessment = Class(name="model::Assessment")
MotivationElement = Class(name="MotivationElement")
model_BusinessActor = Class(name="model::BusinessActor")
BusinessElement = Class(name="BusinessElement")
model_BusinessCollaboration = Class(name="model::BusinessCollaboration")
model_BusinessEvent = Class(name="model::BusinessEvent")
model_BusinessFunction = Class(name="model::BusinessFunction")
model_BusinessInteraction = Class(name="model::BusinessInteraction")
model_BusinessInterface = Class(name="model::BusinessInterface")
model_BusinessObject = Class(name="model::BusinessObject")
model_BusinessProcess = Class(name="model::BusinessProcess")
model_BusinessRole = Class(name="model::BusinessRole")
model_BusinessService = Class(name="model::BusinessService")
model_Capability = Class(name="model::Capability")
StrategyElement = Class(name="StrategyElement")
model_CommunicationNetwork = Class(name="model::CommunicationNetwork")
model_Contract = Class(name="model::Contract")
model_Constraint = Class(name="model::Constraint")
model_CourseOfAction = Class(name="model::CourseOfAction")
model_WorkPackage = Class(name="model::WorkPackage")
model_AccessRelationship = Class(name="model::AccessRelationship")
DependendencyRelationship = Class(name="DependendencyRelationship")
model_Deliverable = Class(name="model::Deliverable")
ImplementationMigrationElement = Class(name="ImplementationMigrationElement")
model_Device = Class(name="model::Device")
model_DistributionNetwork = Class(name="model::DistributionNetwork")
PhysicalElement = Class(name="PhysicalElement")
model_Driver = Class(name="model::Driver")
model_Equipment = Class(name="model::Equipment")
model_Facility = Class(name="model::Facility")
model_Gap = Class(name="model::Gap")
model_Goal = Class(name="model::Goal")
model_Grouping = Class(name="model::Grouping")
CompositeElement = Class(name="CompositeElement")
model_ImplementationEvent = Class(name="model::ImplementationEvent")
model_Location = Class(name="model::Location")
model_Material = Class(name="model::Material")
model_Meaning = Class(name="model::Meaning")
model_Node = Class(name="model::Node")
model_Outcome = Class(name="model::Outcome")
model_Path = Class(name="model::Path")
model_Plateau = Class(name="model::Plateau")
model_Principle = Class(name="model::Principle")
model_Product = Class(name="model::Product")
model_Representation = Class(name="model::Representation")
model_Resource = Class(name="model::Resource")
model_Requirement = Class(name="model::Requirement")
model_Stakeholder = Class(name="model::Stakeholder")
model_SystemSoftware = Class(name="model::SystemSoftware")
model_TechnologyCollaboration = Class(name="model::TechnologyCollaboration")
model_TechnologyEvent = Class(name="model::TechnologyEvent")
model_TechnologyFunction = Class(name="model::TechnologyFunction")
model_TechnologyInterface = Class(name="model::TechnologyInterface")
model_TechnologyInteraction = Class(name="model::TechnologyInteraction")
model_TechnologyProcess = Class(name="model::TechnologyProcess")
model_TechnologyService = Class(name="model::TechnologyService")
model_Value = Class(name="model::Value")
model_AggregationRelationship = Class(name="model::AggregationRelationship")
StructuralRelationship = Class(name="StructuralRelationship")
model_AssignmentRelationship = Class(name="model::AssignmentRelationship")
model_AssociationRelationship = Class(name="model::AssociationRelationship")
OtherRelationship = Class(name="OtherRelationship")
model_CompositionRelationship = Class(name="model::CompositionRelationship")
model_FlowRelationship = Class(name="model::FlowRelationship")
DynamicRelationship = Class(name="DynamicRelationship")
model_InfluenceRelationship = Class(name="model::InfluenceRelationship")
model_RealizationRelationship = Class(name="model::RealizationRelationship")
model_ServingRelationship = Class(name="model::ServingRelationship")
model_SpecializationRelationship = Class(name="model::SpecializationRelationship")
model_TriggeringRelationship = Class(name="model::TriggeringRelationship")
model_DiagramModelComponent = Class(name="model::DiagramModelComponent", is_abstract=True)
model_Connectable = Class(name="model::Connectable", is_abstract=True)
DiagramModelComponent = Class(name="DiagramModelComponent")
model_DiagramModelConnection = Class(name="model::DiagramModelConnection")
model_DiagramModelContainer = Class(name="model::DiagramModelContainer", is_abstract=True)
model_DiagramModelObject = Class(name="model::DiagramModelObject", is_abstract=True)
model_DiagramModel = Class(name="model::DiagramModel", is_abstract=True)
DiagramModelContainer = Class(name="DiagramModelContainer")
model_DiagramModelReference = Class(name="model::DiagramModelReference")
DiagramModelObject = Class(name="DiagramModelObject")
TextPosition = Class(name="TextPosition")
Connectable = Class(name="Connectable")
FontAttribute = Class(name="FontAttribute")
LineObject = Class(name="LineObject")
TextAlignment = Class(name="TextAlignment")
model_Bounds = Class(name="model::Bounds")
model_DiagramModelGroup = Class(name="model::DiagramModelGroup")
model_DiagramModelNote = Class(name="model::DiagramModelNote")
TextContent = Class(name="TextContent")
model_DiagramModelImage = Class(name="model::DiagramModelImage")
BorderObject = Class(name="BorderObject")
DiagramModelImageProvider = Class(name="DiagramModelImageProvider")
model_DiagramModelBendpoint = Class(name="model::DiagramModelBendpoint")
model_LineObject = Class(name="model::LineObject", is_abstract=True)
model_FontAttribute = Class(name="model::FontAttribute", is_abstract=True)
model_TextPosition = Class(name="model::TextPosition", is_abstract=True)
model_TextAlignment = Class(name="model::TextAlignment", is_abstract=True)
model_BorderObject = Class(name="model::BorderObject", is_abstract=True)
model_DiagramModelImageProvider = Class(name="model::DiagramModelImageProvider", is_abstract=True)
model_Lockable = Class(name="model::Lockable", is_abstract=True)
model_ArchimateDiagramModel = Class(name="model::ArchimateDiagramModel")
DiagramModel = Class(name="DiagramModel")
model_DiagramModelArchimateObject = Class(name="model::DiagramModelArchimateObject")
DiagramModelArchimateComponent = Class(name="DiagramModelArchimateComponent")
model_DiagramModelArchimateConnection = Class(name="model::DiagramModelArchimateConnection")
DiagramModelConnection = Class(name="DiagramModelConnection")
model_SketchModel = Class(name="model::SketchModel")
model_SketchModelSticky = Class(name="model::SketchModelSticky")
model_SketchModelActor = Class(name="model::SketchModelActor")
model_DiagramModelArchimateComponent = Class(name="model::DiagramModelArchimateComponent", is_abstract=True)

# model_Adapter class attributes and methods
model_Adapter_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
model_Adapter_m_setAdapter: Method = Method(name="setAdapter", parameters={Parameter(name='object'), Parameter(name='adapter')})
model_Adapter.methods={model_Adapter_m_setAdapter, model_Adapter_m_getAdapter}

# model_Identifier class attributes and methods
model_Identifier_id: Property = Property(name="id", type=StringType)
model_Identifier.attributes={model_Identifier_id}

# model_Property class attributes and methods
model_Property_key: Property = Property(name="key", type=StringType)
model_Property_value: Property = Property(name="value", type=StringType)
model_Property.attributes={model_Property_key, model_Property_value}

# model_Properties class attributes and methods

# model_Metadata class attributes and methods

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

# ArchimateModelObject class attributes and methods

# FolderContainer class attributes and methods

# Documentable class attributes and methods

# Properties class attributes and methods

# model_EObject class attributes and methods

# model_ArchimateModelObject class attributes and methods
model_ArchimateModelObject_m_getArchimateModel: Method = Method(name="getArchimateModel", parameters={}, type=StringType)
model_ArchimateModelObject.methods={model_ArchimateModelObject_m_getArchimateModel}

# Adapter class attributes and methods

# Nameable class attributes and methods

# Identifier class attributes and methods

# model_ArchimateConcept class attributes and methods

# Cloneable class attributes and methods

# model_ArchimateElement class attributes and methods

# ArchimateConcept class attributes and methods

# model_ArchimateRelationship class attributes and methods
model_ArchimateRelationship_m_connect: Method = Method(name="connect", parameters={Parameter(name='source'), Parameter(name='target')})
model_ArchimateRelationship_m_reconnect: Method = Method(name="reconnect", parameters={})
model_ArchimateRelationship_m_disconnect: Method = Method(name="disconnect", parameters={})
model_ArchimateRelationship.methods={model_ArchimateRelationship_m_connect, model_ArchimateRelationship_m_reconnect, model_ArchimateRelationship_m_disconnect}

# model_StrategyElement class attributes and methods

# ArchimateElement class attributes and methods

# model_BusinessElement class attributes and methods

# model_ApplicationElement class attributes and methods

# model_TechnologyElement class attributes and methods

# model_TechnologyObject class attributes and methods

# TechnologyElement class attributes and methods

# PassiveStructureElement class attributes and methods

# model_PhysicalElement class attributes and methods

# model_MotivationElement class attributes and methods

# model_ImplementationMigrationElement class attributes and methods

# model_CompositeElement class attributes and methods

# model_BehaviorElement class attributes and methods

# model_StructureElement class attributes and methods

# model_ActiveStructureElement class attributes and methods

# StructureElement class attributes and methods

# model_PassiveStructureElement class attributes and methods

# model_StructuralRelationship class attributes and methods

# ArchimateRelationship class attributes and methods

# model_DependendencyRelationship class attributes and methods

# model_DynamicRelationship class attributes and methods

# model_OtherRelationship class attributes and methods

# model_ArchimateModel class attributes and methods
model_ArchimateModel_purpose: Property = Property(name="purpose", type=StringType)
model_ArchimateModel_file: Property = Property(name="file", type=StringType)
model_ArchimateModel_version: Property = Property(name="version", type=StringType)
model_ArchimateModel_m_setDefaults: Method = Method(name="setDefaults", parameters={})
model_ArchimateModel_m_getDefaultFolderForObject: Method = Method(name="getDefaultFolderForObject", parameters={Parameter(name='object')}, type=StringType)
model_ArchimateModel_m_getDefaultDiagramModel: Method = Method(name="getDefaultDiagramModel", parameters={}, type=StringType)
model_ArchimateModel_m_getDiagramModels: Method = Method(name="getDiagramModels", parameters={}, type=StringType)
model_ArchimateModel_m_getFolder: Method = Method(name="getFolder", parameters={Parameter(name='type')}, type=StringType)
model_ArchimateModel.attributes={model_ArchimateModel_version, model_ArchimateModel_file, model_ArchimateModel_purpose}
model_ArchimateModel.methods={model_ArchimateModel_m_getDiagramModels, model_ArchimateModel_m_getFolder, model_ArchimateModel_m_setDefaults, model_ArchimateModel_m_getDefaultDiagramModel, model_ArchimateModel_m_getDefaultFolderForObject}

# model_DataObject class attributes and methods

# model_Junction class attributes and methods
model_Junction_type: Property = Property(name="type", type=StringType)
model_Junction.attributes={model_Junction_type}

# model_ApplicationCollaboration class attributes and methods

# ApplicationElement class attributes and methods

# ActiveStructureElement class attributes and methods

# model_ApplicationComponent class attributes and methods

# model_ApplicationEvent class attributes and methods

# BehaviorElement class attributes and methods

# model_ApplicationFunction class attributes and methods

# model_ApplicationInteraction class attributes and methods

# model_ApplicationInterface class attributes and methods

# model_ApplicationProcess class attributes and methods

# model_ApplicationService class attributes and methods

# model_Artifact class attributes and methods

# TechnologyObject class attributes and methods

# model_Assessment class attributes and methods

# MotivationElement class attributes and methods

# model_BusinessActor class attributes and methods

# BusinessElement class attributes and methods

# model_BusinessCollaboration class attributes and methods

# model_BusinessEvent class attributes and methods

# model_BusinessFunction class attributes and methods

# model_BusinessInteraction class attributes and methods

# model_BusinessInterface class attributes and methods

# model_BusinessObject class attributes and methods

# model_BusinessProcess class attributes and methods

# model_BusinessRole class attributes and methods

# model_BusinessService class attributes and methods

# model_Capability class attributes and methods

# StrategyElement class attributes and methods

# model_CommunicationNetwork class attributes and methods

# model_Contract class attributes and methods

# model_Constraint class attributes and methods

# model_CourseOfAction class attributes and methods

# model_WorkPackage class attributes and methods

# model_AccessRelationship class attributes and methods
model_AccessRelationship_accessType: Property = Property(name="accessType", type=IntegerType)
model_AccessRelationship.attributes={model_AccessRelationship_accessType}

# DependendencyRelationship class attributes and methods

# model_Deliverable class attributes and methods

# ImplementationMigrationElement class attributes and methods

# model_Device class attributes and methods

# model_DistributionNetwork class attributes and methods

# PhysicalElement class attributes and methods

# model_Driver class attributes and methods

# model_Equipment class attributes and methods

# model_Facility class attributes and methods

# model_Gap class attributes and methods

# model_Goal class attributes and methods

# model_Grouping class attributes and methods

# CompositeElement class attributes and methods

# model_ImplementationEvent class attributes and methods

# model_Location class attributes and methods

# model_Material class attributes and methods

# model_Meaning class attributes and methods

# model_Node class attributes and methods

# model_Outcome class attributes and methods

# model_Path class attributes and methods

# model_Plateau class attributes and methods

# model_Principle class attributes and methods

# model_Product class attributes and methods

# model_Representation class attributes and methods

# model_Resource class attributes and methods

# model_Requirement class attributes and methods

# model_Stakeholder class attributes and methods

# model_SystemSoftware class attributes and methods

# model_TechnologyCollaboration class attributes and methods

# model_TechnologyEvent class attributes and methods

# model_TechnologyFunction class attributes and methods

# model_TechnologyInterface class attributes and methods

# model_TechnologyInteraction class attributes and methods

# model_TechnologyProcess class attributes and methods

# model_TechnologyService class attributes and methods

# model_Value class attributes and methods

# model_AggregationRelationship class attributes and methods

# StructuralRelationship class attributes and methods

# model_AssignmentRelationship class attributes and methods

# model_AssociationRelationship class attributes and methods

# OtherRelationship class attributes and methods

# model_CompositionRelationship class attributes and methods

# model_FlowRelationship class attributes and methods

# DynamicRelationship class attributes and methods

# model_InfluenceRelationship class attributes and methods
model_InfluenceRelationship_strength: Property = Property(name="strength", type=StringType)
model_InfluenceRelationship.attributes={model_InfluenceRelationship_strength}

# model_RealizationRelationship class attributes and methods

# model_ServingRelationship class attributes and methods

# model_SpecializationRelationship class attributes and methods

# model_TriggeringRelationship class attributes and methods

# model_DiagramModelComponent class attributes and methods
model_DiagramModelComponent_m_getDiagramModel: Method = Method(name="getDiagramModel", parameters={}, type=StringType)
model_DiagramModelComponent.methods={model_DiagramModelComponent_m_getDiagramModel}

# model_Connectable class attributes and methods
model_Connectable_m_addConnection: Method = Method(name="addConnection", parameters={Parameter(name='connection')})
model_Connectable_m_removeConnection: Method = Method(name="removeConnection", parameters={Parameter(name='connection')})
model_Connectable.methods={model_Connectable_m_addConnection, model_Connectable_m_removeConnection}

# DiagramModelComponent class attributes and methods

# model_DiagramModelConnection class attributes and methods
model_DiagramModelConnection_text: Property = Property(name="text", type=StringType)
model_DiagramModelConnection_textPosition: Property = Property(name="textPosition", type=IntegerType)
model_DiagramModelConnection_type: Property = Property(name="type", type=IntegerType)
model_DiagramModelConnection_m_connect: Method = Method(name="connect", parameters={Parameter(name='target'), Parameter(name='source')})
model_DiagramModelConnection_m_disconnect: Method = Method(name="disconnect", parameters={})
model_DiagramModelConnection_m_reconnect: Method = Method(name="reconnect", parameters={})
model_DiagramModelConnection.attributes={model_DiagramModelConnection_textPosition, model_DiagramModelConnection_type, model_DiagramModelConnection_text}
model_DiagramModelConnection.methods={model_DiagramModelConnection_m_reconnect, model_DiagramModelConnection_m_connect, model_DiagramModelConnection_m_disconnect}

# model_DiagramModelContainer class attributes and methods

# model_DiagramModelObject class attributes and methods
model_DiagramModelObject_fillColor: Property = Property(name="fillColor", type=StringType)
model_DiagramModelObject_alpha: Property = Property(name="alpha", type=IntegerType)
model_DiagramModelObject_m_setBounds: Method = Method(name="setBounds", parameters={Parameter(name='height'), Parameter(name='width'), Parameter(name='x'), Parameter(name='y')})
model_DiagramModelObject.attributes={model_DiagramModelObject_fillColor, model_DiagramModelObject_alpha}
model_DiagramModelObject.methods={model_DiagramModelObject_m_setBounds}

# model_DiagramModel class attributes and methods
model_DiagramModel_connectionRouterType: Property = Property(name="connectionRouterType", type=IntegerType)
model_DiagramModel.attributes={model_DiagramModel_connectionRouterType}

# DiagramModelContainer class attributes and methods

# model_DiagramModelReference class attributes and methods

# DiagramModelObject class attributes and methods

# TextPosition class attributes and methods

# Connectable class attributes and methods

# FontAttribute class attributes and methods

# LineObject class attributes and methods

# TextAlignment class attributes and methods

# model_Bounds class attributes and methods
model_Bounds_x: Property = Property(name="x", type=IntegerType)
model_Bounds_y: Property = Property(name="y", type=IntegerType)
model_Bounds_width: Property = Property(name="width", type=IntegerType)
model_Bounds_height: Property = Property(name="height", type=IntegerType)
model_Bounds_m_setLocation: Method = Method(name="setLocation", parameters={Parameter(name='x'), Parameter(name='y')})
model_Bounds_m_setSize: Method = Method(name="setSize", parameters={Parameter(name='width'), Parameter(name='height')})
model_Bounds_m_getCopy: Method = Method(name="getCopy", parameters={}, type=StringType)
model_Bounds.attributes={model_Bounds_y, model_Bounds_x, model_Bounds_width, model_Bounds_height}
model_Bounds.methods={model_Bounds_m_getCopy, model_Bounds_m_setSize, model_Bounds_m_setLocation}

# model_DiagramModelGroup class attributes and methods

# model_DiagramModelNote class attributes and methods
model_DiagramModelNote_borderType: Property = Property(name="borderType", type=IntegerType)
model_DiagramModelNote.attributes={model_DiagramModelNote_borderType}

# TextContent class attributes and methods

# model_DiagramModelImage class attributes and methods

# BorderObject class attributes and methods

# DiagramModelImageProvider class attributes and methods

# model_DiagramModelBendpoint class attributes and methods
model_DiagramModelBendpoint_startX: Property = Property(name="startX", type=IntegerType)
model_DiagramModelBendpoint_startY: Property = Property(name="startY", type=IntegerType)
model_DiagramModelBendpoint_endX: Property = Property(name="endX", type=IntegerType)
model_DiagramModelBendpoint_endY: Property = Property(name="endY", type=IntegerType)
model_DiagramModelBendpoint.attributes={model_DiagramModelBendpoint_startX, model_DiagramModelBendpoint_endX, model_DiagramModelBendpoint_startY, model_DiagramModelBendpoint_endY}

# model_LineObject class attributes and methods
model_LineObject_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
model_LineObject_lineColor: Property = Property(name="lineColor", type=StringType)
model_LineObject.attributes={model_LineObject_lineWidth, model_LineObject_lineColor}

# model_FontAttribute class attributes and methods
model_FontAttribute_font: Property = Property(name="font", type=StringType)
model_FontAttribute_fontColor: Property = Property(name="fontColor", type=StringType)
model_FontAttribute.attributes={model_FontAttribute_fontColor, model_FontAttribute_font}

# model_TextPosition class attributes and methods
model_TextPosition_textPosition: Property = Property(name="textPosition", type=IntegerType)
model_TextPosition.attributes={model_TextPosition_textPosition}

# model_TextAlignment class attributes and methods
model_TextAlignment_textAlignment: Property = Property(name="textAlignment", type=IntegerType)
model_TextAlignment.attributes={model_TextAlignment_textAlignment}

# model_BorderObject class attributes and methods
model_BorderObject_borderColor: Property = Property(name="borderColor", type=StringType)
model_BorderObject.attributes={model_BorderObject_borderColor}

# model_DiagramModelImageProvider class attributes and methods
model_DiagramModelImageProvider_imagePath: Property = Property(name="imagePath", type=StringType)
model_DiagramModelImageProvider.attributes={model_DiagramModelImageProvider_imagePath}

# model_Lockable class attributes and methods
model_Lockable_locked: Property = Property(name="locked", type=BooleanType)
model_Lockable.attributes={model_Lockable_locked}

# model_ArchimateDiagramModel class attributes and methods
model_ArchimateDiagramModel_viewpoint: Property = Property(name="viewpoint", type=StringType)
model_ArchimateDiagramModel.attributes={model_ArchimateDiagramModel_viewpoint}

# DiagramModel class attributes and methods

# model_DiagramModelArchimateObject class attributes and methods
model_DiagramModelArchimateObject_type: Property = Property(name="type", type=IntegerType)
model_DiagramModelArchimateObject.attributes={model_DiagramModelArchimateObject_type}

# DiagramModelArchimateComponent class attributes and methods

# model_DiagramModelArchimateConnection class attributes and methods

# DiagramModelConnection class attributes and methods

# model_SketchModel class attributes and methods
model_SketchModel_background: Property = Property(name="background", type=IntegerType)
model_SketchModel.attributes={model_SketchModel_background}

# model_SketchModelSticky class attributes and methods

# model_SketchModelActor class attributes and methods

# model_DiagramModelArchimateComponent class attributes and methods
model_DiagramModelArchimateComponent_m_getArchimateConcept: Method = Method(name="getArchimateConcept", parameters={}, type=ArchimateConcept)
model_DiagramModelArchimateComponent_m_setArchimateConcept: Method = Method(name="setArchimateConcept", parameters={Parameter(name='concept')})
model_DiagramModelArchimateComponent_m_addArchimateConceptToModel: Method = Method(name="addArchimateConceptToModel", parameters={Parameter(name='parent')})
model_DiagramModelArchimateComponent_m_removeArchimateConceptFromModel: Method = Method(name="removeArchimateConceptFromModel", parameters={})
model_DiagramModelArchimateComponent.methods={model_DiagramModelArchimateComponent_m_getArchimateConcept, model_DiagramModelArchimateComponent_m_removeArchimateConceptFromModel, model_DiagramModelArchimateComponent_m_setArchimateConcept, model_DiagramModelArchimateComponent_m_addArchimateConceptToModel}

# Relationships
entries1: BinaryAssociation = BinaryAssociation(
    name="entries1",
    ends={
        Property(name="model_Property2", type=model_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Metadata", type=model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
folders3: BinaryAssociation = BinaryAssociation(
    name="folders3",
    ends={
        Property(name="model_Folder", type=model_FolderContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FolderContainer", type=model_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="model_EObject", type=model_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Folder5", type=model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="model_Property", type=model_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Properties", type=model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="model_ArchimateConcept", type=model_ArchimateRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArchimateRelationship", type=model_ArchimateConcept, multiplicity=Multiplicity(0, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="model_ArchimateConcept9", type=model_ArchimateRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArchimateRelationship8", type=model_ArchimateConcept, multiplicity=Multiplicity(0, 1))
    }
)
metadata10: BinaryAssociation = BinaryAssociation(
    name="metadata10",
    ends={
        Property(name="model_Metadata11", type=model_ArchimateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ArchimateModel", type=model_Metadata, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceConnections12: BinaryAssociation = BinaryAssociation(
    name="sourceConnections12",
    ends={
        Property(name="model_DiagramModelConnection", type=model_Connectable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Connectable", type=model_DiagramModelConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetConnections13: BinaryAssociation = BinaryAssociation(
    name="targetConnections13",
    ends={
        Property(name="model_DiagramModelConnection15", type=model_Connectable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Connectable14", type=model_DiagramModelConnection, multiplicity=Multiplicity(0, 9999))
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="model_DiagramModelObject", type=model_DiagramModelContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelContainer", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModel17: BinaryAssociation = BinaryAssociation(
    name="referencedModel17",
    ends={
        Property(name="model_DiagramModel", type=model_DiagramModelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelReference", type=model_DiagramModel, multiplicity=Multiplicity(0, 1))
    }
)
bounds18: BinaryAssociation = BinaryAssociation(
    name="bounds18",
    ends={
        Property(name="model_Bounds", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject19", type=model_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="model_Connectable22", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection21", type=model_Connectable, multiplicity=Multiplicity(0, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="model_Connectable25", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection24", type=model_Connectable, multiplicity=Multiplicity(0, 1))
    }
)
bendpoints26: BinaryAssociation = BinaryAssociation(
    name="bendpoints26",
    ends={
        Property(name="model_DiagramModelBendpoint", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection27", type=model_DiagramModelBendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archimateElement28: BinaryAssociation = BinaryAssociation(
    name="archimateElement28",
    ends={
        Property(name="model_ArchimateElement", type=model_DiagramModelArchimateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelArchimateObject", type=model_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
archimateRelationship29: BinaryAssociation = BinaryAssociation(
    name="archimateRelationship29",
    ends={
        Property(name="model_ArchimateRelationship30", type=model_DiagramModelArchimateConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelArchimateConnection", type=model_ArchimateRelationship, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_Folder_ArchimateModelObject = Generalization(general=ArchimateModelObject, specific=model_Folder)
gen_model_Folder_FolderContainer = Generalization(general=FolderContainer, specific=model_Folder)
gen_model_Folder_Documentable = Generalization(general=Documentable, specific=model_Folder)
gen_model_Folder_Properties = Generalization(general=Properties, specific=model_Folder)
gen_model_ArchimateModelObject_Adapter = Generalization(general=Adapter, specific=model_ArchimateModelObject)
gen_model_ArchimateModelObject_Nameable = Generalization(general=Nameable, specific=model_ArchimateModelObject)
gen_model_ArchimateModelObject_Identifier = Generalization(general=Identifier, specific=model_ArchimateModelObject)
gen_model_ArchimateConcept_ArchimateModelObject = Generalization(general=ArchimateModelObject, specific=model_ArchimateConcept)
gen_model_ArchimateConcept_Cloneable = Generalization(general=Cloneable, specific=model_ArchimateConcept)
gen_model_ArchimateConcept_Documentable = Generalization(general=Documentable, specific=model_ArchimateConcept)
gen_model_ArchimateConcept_Properties = Generalization(general=Properties, specific=model_ArchimateConcept)
gen_model_ArchimateElement_ArchimateConcept = Generalization(general=ArchimateConcept, specific=model_ArchimateElement)
gen_model_ArchimateRelationship_ArchimateConcept = Generalization(general=ArchimateConcept, specific=model_ArchimateRelationship)
gen_model_StrategyElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_StrategyElement)
gen_model_BusinessElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_BusinessElement)
gen_model_ApplicationElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_ApplicationElement)
gen_model_TechnologyElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_TechnologyElement)
gen_model_TechnologyObject_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyObject)
gen_model_TechnologyObject_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_TechnologyObject)
gen_model_PhysicalElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_PhysicalElement)
gen_model_MotivationElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_MotivationElement)
gen_model_ImplementationMigrationElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_ImplementationMigrationElement)
gen_model_CompositeElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_CompositeElement)
gen_model_BehaviorElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_BehaviorElement)
gen_model_StructureElement_ArchimateElement = Generalization(general=ArchimateElement, specific=model_StructureElement)
gen_model_ActiveStructureElement_StructureElement = Generalization(general=StructureElement, specific=model_ActiveStructureElement)
gen_model_PassiveStructureElement_StructureElement = Generalization(general=StructureElement, specific=model_PassiveStructureElement)
gen_model_StructuralRelationship_ArchimateRelationship = Generalization(general=ArchimateRelationship, specific=model_StructuralRelationship)
gen_model_DependendencyRelationship_ArchimateRelationship = Generalization(general=ArchimateRelationship, specific=model_DependendencyRelationship)
gen_model_DynamicRelationship_ArchimateRelationship = Generalization(general=ArchimateRelationship, specific=model_DynamicRelationship)
gen_model_OtherRelationship_ArchimateRelationship = Generalization(general=ArchimateRelationship, specific=model_OtherRelationship)
gen_model_ArchimateModel_FolderContainer = Generalization(general=FolderContainer, specific=model_ArchimateModel)
gen_model_ArchimateModel_ArchimateModelObject = Generalization(general=ArchimateModelObject, specific=model_ArchimateModel)
gen_model_ArchimateModel_Properties = Generalization(general=Properties, specific=model_ArchimateModel)
gen_model_DataObject_ApplicationElement = Generalization(general=ApplicationElement, specific=model_DataObject)
gen_model_DataObject_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_DataObject)
gen_model_Junction_ArchimateElement = Generalization(general=ArchimateElement, specific=model_Junction)
gen_model_ApplicationCollaboration_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationCollaboration)
gen_model_ApplicationCollaboration_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_ApplicationCollaboration)
gen_model_ApplicationComponent_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationComponent)
gen_model_ApplicationComponent_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_ApplicationComponent)
gen_model_ApplicationEvent_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationEvent)
gen_model_ApplicationEvent_BehaviorElement = Generalization(general=BehaviorElement, specific=model_ApplicationEvent)
gen_model_ApplicationFunction_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationFunction)
gen_model_ApplicationFunction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_ApplicationFunction)
gen_model_ApplicationInteraction_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationInteraction)
gen_model_ApplicationInteraction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_ApplicationInteraction)
gen_model_ApplicationInterface_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationInterface)
gen_model_ApplicationInterface_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_ApplicationInterface)
gen_model_ApplicationProcess_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationProcess)
gen_model_ApplicationProcess_BehaviorElement = Generalization(general=BehaviorElement, specific=model_ApplicationProcess)
gen_model_ApplicationService_ApplicationElement = Generalization(general=ApplicationElement, specific=model_ApplicationService)
gen_model_ApplicationService_BehaviorElement = Generalization(general=BehaviorElement, specific=model_ApplicationService)
gen_model_Artifact_TechnologyObject = Generalization(general=TechnologyObject, specific=model_Artifact)
gen_model_Assessment_MotivationElement = Generalization(general=MotivationElement, specific=model_Assessment)
gen_model_BusinessActor_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessActor)
gen_model_BusinessActor_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_BusinessActor)
gen_model_BusinessCollaboration_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessCollaboration)
gen_model_BusinessCollaboration_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_BusinessCollaboration)
gen_model_BusinessEvent_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessEvent)
gen_model_BusinessEvent_BehaviorElement = Generalization(general=BehaviorElement, specific=model_BusinessEvent)
gen_model_BusinessFunction_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessFunction)
gen_model_BusinessFunction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_BusinessFunction)
gen_model_BusinessInteraction_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessInteraction)
gen_model_BusinessInteraction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_BusinessInteraction)
gen_model_BusinessInterface_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessInterface)
gen_model_BusinessInterface_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_BusinessInterface)
gen_model_BusinessObject_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessObject)
gen_model_BusinessObject_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_BusinessObject)
gen_model_BusinessProcess_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessProcess)
gen_model_BusinessProcess_BehaviorElement = Generalization(general=BehaviorElement, specific=model_BusinessProcess)
gen_model_BusinessRole_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessRole)
gen_model_BusinessRole_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_BusinessRole)
gen_model_BusinessService_BusinessElement = Generalization(general=BusinessElement, specific=model_BusinessService)
gen_model_BusinessService_BehaviorElement = Generalization(general=BehaviorElement, specific=model_BusinessService)
gen_model_Capability_StrategyElement = Generalization(general=StrategyElement, specific=model_Capability)
gen_model_Capability_BehaviorElement = Generalization(general=BehaviorElement, specific=model_Capability)
gen_model_CommunicationNetwork_TechnologyElement = Generalization(general=TechnologyElement, specific=model_CommunicationNetwork)
gen_model_CommunicationNetwork_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_CommunicationNetwork)
gen_model_Contract_BusinessElement = Generalization(general=BusinessElement, specific=model_Contract)
gen_model_Contract_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_Contract)
gen_model_Constraint_MotivationElement = Generalization(general=MotivationElement, specific=model_Constraint)
gen_model_CourseOfAction_StrategyElement = Generalization(general=StrategyElement, specific=model_CourseOfAction)
gen_model_CourseOfAction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_CourseOfAction)
gen_model_WorkPackage_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_WorkPackage)
gen_model_WorkPackage_BehaviorElement = Generalization(general=BehaviorElement, specific=model_WorkPackage)
gen_model_Deliverable_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_Deliverable)
gen_model_Deliverable_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_Deliverable)
gen_model_Device_TechnologyElement = Generalization(general=TechnologyElement, specific=model_Device)
gen_model_Device_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_Device)
gen_model_DistributionNetwork_PhysicalElement = Generalization(general=PhysicalElement, specific=model_DistributionNetwork)
gen_model_DistributionNetwork_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_DistributionNetwork)
gen_model_Driver_MotivationElement = Generalization(general=MotivationElement, specific=model_Driver)
gen_model_Equipment_PhysicalElement = Generalization(general=PhysicalElement, specific=model_Equipment)
gen_model_Equipment_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_Equipment)
gen_model_Facility_PhysicalElement = Generalization(general=PhysicalElement, specific=model_Facility)
gen_model_Facility_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_Facility)
gen_model_Gap_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_Gap)
gen_model_Gap_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_Gap)
gen_model_Goal_MotivationElement = Generalization(general=MotivationElement, specific=model_Goal)
gen_model_Grouping_CompositeElement = Generalization(general=CompositeElement, specific=model_Grouping)
gen_model_ImplementationEvent_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_ImplementationEvent)
gen_model_Location_CompositeElement = Generalization(general=CompositeElement, specific=model_Location)
gen_model_Material_PhysicalElement = Generalization(general=PhysicalElement, specific=model_Material)
gen_model_Material_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_Material)
gen_model_Meaning_MotivationElement = Generalization(general=MotivationElement, specific=model_Meaning)
gen_model_Node_TechnologyElement = Generalization(general=TechnologyElement, specific=model_Node)
gen_model_Node_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_Node)
gen_model_Outcome_MotivationElement = Generalization(general=MotivationElement, specific=model_Outcome)
gen_model_Path_TechnologyElement = Generalization(general=TechnologyElement, specific=model_Path)
gen_model_Plateau_ImplementationMigrationElement = Generalization(general=ImplementationMigrationElement, specific=model_Plateau)
gen_model_Plateau_CompositeElement = Generalization(general=CompositeElement, specific=model_Plateau)
gen_model_Principle_MotivationElement = Generalization(general=MotivationElement, specific=model_Principle)
gen_model_Product_BusinessElement = Generalization(general=BusinessElement, specific=model_Product)
gen_model_Product_CompositeElement = Generalization(general=CompositeElement, specific=model_Product)
gen_model_Representation_BusinessElement = Generalization(general=BusinessElement, specific=model_Representation)
gen_model_Representation_PassiveStructureElement = Generalization(general=PassiveStructureElement, specific=model_Representation)
gen_model_Resource_StrategyElement = Generalization(general=StrategyElement, specific=model_Resource)
gen_model_Resource_StructureElement = Generalization(general=StructureElement, specific=model_Resource)
gen_model_Requirement_MotivationElement = Generalization(general=MotivationElement, specific=model_Requirement)
gen_model_Stakeholder_MotivationElement = Generalization(general=MotivationElement, specific=model_Stakeholder)
gen_model_Stakeholder_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_Stakeholder)
gen_model_SystemSoftware_TechnologyElement = Generalization(general=TechnologyElement, specific=model_SystemSoftware)
gen_model_SystemSoftware_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_SystemSoftware)
gen_model_TechnologyCollaboration_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyCollaboration)
gen_model_TechnologyCollaboration_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_TechnologyCollaboration)
gen_model_TechnologyEvent_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyEvent)
gen_model_TechnologyEvent_BehaviorElement = Generalization(general=BehaviorElement, specific=model_TechnologyEvent)
gen_model_TechnologyFunction_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyFunction)
gen_model_TechnologyFunction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_TechnologyFunction)
gen_model_TechnologyInterface_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyInterface)
gen_model_TechnologyInterface_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=model_TechnologyInterface)
gen_model_TechnologyInteraction_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyInteraction)
gen_model_TechnologyInteraction_BehaviorElement = Generalization(general=BehaviorElement, specific=model_TechnologyInteraction)
gen_model_TechnologyProcess_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyProcess)
gen_model_TechnologyProcess_BehaviorElement = Generalization(general=BehaviorElement, specific=model_TechnologyProcess)
gen_model_TechnologyService_TechnologyElement = Generalization(general=TechnologyElement, specific=model_TechnologyService)
gen_model_TechnologyService_BehaviorElement = Generalization(general=BehaviorElement, specific=model_TechnologyService)
gen_model_Value_MotivationElement = Generalization(general=MotivationElement, specific=model_Value)
gen_model_AccessRelationship_DependendencyRelationship = Generalization(general=DependendencyRelationship, specific=model_AccessRelationship)
gen_model_AggregationRelationship_StructuralRelationship = Generalization(general=StructuralRelationship, specific=model_AggregationRelationship)
gen_model_AssignmentRelationship_StructuralRelationship = Generalization(general=StructuralRelationship, specific=model_AssignmentRelationship)
gen_model_AssociationRelationship_OtherRelationship = Generalization(general=OtherRelationship, specific=model_AssociationRelationship)
gen_model_CompositionRelationship_StructuralRelationship = Generalization(general=StructuralRelationship, specific=model_CompositionRelationship)
gen_model_FlowRelationship_DynamicRelationship = Generalization(general=DynamicRelationship, specific=model_FlowRelationship)
gen_model_InfluenceRelationship_DependendencyRelationship = Generalization(general=DependendencyRelationship, specific=model_InfluenceRelationship)
gen_model_RealizationRelationship_StructuralRelationship = Generalization(general=StructuralRelationship, specific=model_RealizationRelationship)
gen_model_ServingRelationship_DependendencyRelationship = Generalization(general=DependendencyRelationship, specific=model_ServingRelationship)
gen_model_SpecializationRelationship_OtherRelationship = Generalization(general=OtherRelationship, specific=model_SpecializationRelationship)
gen_model_TriggeringRelationship_DynamicRelationship = Generalization(general=DynamicRelationship, specific=model_TriggeringRelationship)
gen_model_DiagramModelComponent_Identifier = Generalization(general=Identifier, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Cloneable = Generalization(general=Cloneable, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Adapter = Generalization(general=Adapter, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Nameable = Generalization(general=Nameable, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_ArchimateModelObject = Generalization(general=ArchimateModelObject, specific=model_DiagramModelComponent)
gen_model_Connectable_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_Connectable)
gen_model_DiagramModelContainer_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_DiagramModelContainer)
gen_model_DiagramModel_ArchimateModelObject = Generalization(general=ArchimateModelObject, specific=model_DiagramModel)
gen_model_DiagramModel_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModel)
gen_model_DiagramModel_Documentable = Generalization(general=Documentable, specific=model_DiagramModel)
gen_model_DiagramModel_Properties = Generalization(general=Properties, specific=model_DiagramModel)
gen_model_DiagramModelReference_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelReference)
gen_model_DiagramModelReference_TextPosition = Generalization(general=TextPosition, specific=model_DiagramModelReference)
gen_model_DiagramModelObject_Connectable = Generalization(general=Connectable, specific=model_DiagramModelObject)
gen_model_DiagramModelObject_FontAttribute = Generalization(general=FontAttribute, specific=model_DiagramModelObject)
gen_model_DiagramModelObject_LineObject = Generalization(general=LineObject, specific=model_DiagramModelObject)
gen_model_DiagramModelObject_TextAlignment = Generalization(general=TextAlignment, specific=model_DiagramModelObject)
gen_model_DiagramModelGroup_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelGroup)
gen_model_DiagramModelGroup_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModelGroup)
gen_model_DiagramModelGroup_Documentable = Generalization(general=Documentable, specific=model_DiagramModelGroup)
gen_model_DiagramModelGroup_Properties = Generalization(general=Properties, specific=model_DiagramModelGroup)
gen_model_DiagramModelNote_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelNote)
gen_model_DiagramModelNote_TextContent = Generalization(general=TextContent, specific=model_DiagramModelNote)
gen_model_DiagramModelNote_TextPosition = Generalization(general=TextPosition, specific=model_DiagramModelNote)
gen_model_DiagramModelImage_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelImage)
gen_model_DiagramModelImage_BorderObject = Generalization(general=BorderObject, specific=model_DiagramModelImage)
gen_model_DiagramModelImage_DiagramModelImageProvider = Generalization(general=DiagramModelImageProvider, specific=model_DiagramModelImage)
gen_model_DiagramModelConnection_Connectable = Generalization(general=Connectable, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_FontAttribute = Generalization(general=FontAttribute, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_Properties = Generalization(general=Properties, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_Documentable = Generalization(general=Documentable, specific=model_DiagramModelConnection)
gen_model_DiagramModelConnection_LineObject = Generalization(general=LineObject, specific=model_DiagramModelConnection)
gen_model_DiagramModelBendpoint_Cloneable = Generalization(general=Cloneable, specific=model_DiagramModelBendpoint)
gen_model_ArchimateDiagramModel_DiagramModel = Generalization(general=DiagramModel, specific=model_ArchimateDiagramModel)
gen_model_DiagramModelArchimateObject_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelArchimateObject)
gen_model_DiagramModelArchimateObject_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModelArchimateObject)
gen_model_DiagramModelArchimateObject_DiagramModelArchimateComponent = Generalization(general=DiagramModelArchimateComponent, specific=model_DiagramModelArchimateObject)
gen_model_DiagramModelArchimateObject_TextPosition = Generalization(general=TextPosition, specific=model_DiagramModelArchimateObject)
gen_model_DiagramModelArchimateConnection_DiagramModelConnection = Generalization(general=DiagramModelConnection, specific=model_DiagramModelArchimateConnection)
gen_model_DiagramModelArchimateConnection_DiagramModelArchimateComponent = Generalization(general=DiagramModelArchimateComponent, specific=model_DiagramModelArchimateConnection)
gen_model_SketchModel_DiagramModel = Generalization(general=DiagramModel, specific=model_SketchModel)
gen_model_SketchModelSticky_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_TextContent = Generalization(general=TextContent, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_Properties = Generalization(general=Properties, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_TextPosition = Generalization(general=TextPosition, specific=model_SketchModelSticky)
gen_model_SketchModelActor_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_SketchModelActor)
gen_model_SketchModelActor_Documentable = Generalization(general=Documentable, specific=model_SketchModelActor)
gen_model_SketchModelActor_Properties = Generalization(general=Properties, specific=model_SketchModelActor)
gen_model_DiagramModelArchimateComponent_Connectable = Generalization(general=Connectable, specific=model_DiagramModelArchimateComponent)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Adapter, model_Identifier, model_Property, model_Properties, model_Metadata, model_Nameable, model_TextContent, model_Documentable, model_Cloneable, model_FolderContainer, model_Folder, ArchimateModelObject, FolderContainer, Documentable, Properties, model_EObject, model_ArchimateModelObject, Adapter, Nameable, Identifier, model_ArchimateConcept, Cloneable, model_ArchimateElement, ArchimateConcept, model_ArchimateRelationship, model_StrategyElement, ArchimateElement, model_BusinessElement, model_ApplicationElement, model_TechnologyElement, model_TechnologyObject, TechnologyElement, PassiveStructureElement, model_PhysicalElement, model_MotivationElement, model_ImplementationMigrationElement, model_CompositeElement, model_BehaviorElement, model_StructureElement, model_ActiveStructureElement, StructureElement, model_PassiveStructureElement, model_StructuralRelationship, ArchimateRelationship, model_DependendencyRelationship, model_DynamicRelationship, model_OtherRelationship, model_ArchimateModel, model_DataObject, model_Junction, model_ApplicationCollaboration, ApplicationElement, ActiveStructureElement, model_ApplicationComponent, model_ApplicationEvent, BehaviorElement, model_ApplicationFunction, model_ApplicationInteraction, model_ApplicationInterface, model_ApplicationProcess, model_ApplicationService, model_Artifact, TechnologyObject, model_Assessment, MotivationElement, model_BusinessActor, BusinessElement, model_BusinessCollaboration, model_BusinessEvent, model_BusinessFunction, model_BusinessInteraction, model_BusinessInterface, model_BusinessObject, model_BusinessProcess, model_BusinessRole, model_BusinessService, model_Capability, StrategyElement, model_CommunicationNetwork, model_Contract, model_Constraint, model_CourseOfAction, model_WorkPackage, model_AccessRelationship, DependendencyRelationship, model_Deliverable, ImplementationMigrationElement, model_Device, model_DistributionNetwork, PhysicalElement, model_Driver, model_Equipment, model_Facility, model_Gap, model_Goal, model_Grouping, CompositeElement, model_ImplementationEvent, model_Location, model_Material, model_Meaning, model_Node, model_Outcome, model_Path, model_Plateau, model_Principle, model_Product, model_Representation, model_Resource, model_Requirement, model_Stakeholder, model_SystemSoftware, model_TechnologyCollaboration, model_TechnologyEvent, model_TechnologyFunction, model_TechnologyInterface, model_TechnologyInteraction, model_TechnologyProcess, model_TechnologyService, model_Value, model_AggregationRelationship, StructuralRelationship, model_AssignmentRelationship, model_AssociationRelationship, OtherRelationship, model_CompositionRelationship, model_FlowRelationship, DynamicRelationship, model_InfluenceRelationship, model_RealizationRelationship, model_ServingRelationship, model_SpecializationRelationship, model_TriggeringRelationship, model_DiagramModelComponent, model_Connectable, DiagramModelComponent, model_DiagramModelConnection, model_DiagramModelContainer, model_DiagramModelObject, model_DiagramModel, DiagramModelContainer, model_DiagramModelReference, DiagramModelObject, TextPosition, Connectable, FontAttribute, LineObject, TextAlignment, model_Bounds, model_DiagramModelGroup, model_DiagramModelNote, TextContent, model_DiagramModelImage, BorderObject, DiagramModelImageProvider, model_DiagramModelBendpoint, model_LineObject, model_FontAttribute, model_TextPosition, model_TextAlignment, model_BorderObject, model_DiagramModelImageProvider, model_Lockable, model_ArchimateDiagramModel, DiagramModel, model_DiagramModelArchimateObject, DiagramModelArchimateComponent, model_DiagramModelArchimateConnection, DiagramModelConnection, model_SketchModel, model_SketchModelSticky, model_SketchModelActor, model_DiagramModelArchimateComponent, FolderType},
    associations={entries1, folders3, elements4, properties0, source6, target7, metadata10, sourceConnections12, targetConnections13, children16, referencedModel17, bounds18, source20, target23, bendpoints26, archimateElement28, archimateRelationship29},
    generalizations={gen_model_Folder_ArchimateModelObject, gen_model_Folder_FolderContainer, gen_model_Folder_Documentable, gen_model_Folder_Properties, gen_model_ArchimateModelObject_Adapter, gen_model_ArchimateModelObject_Nameable, gen_model_ArchimateModelObject_Identifier, gen_model_ArchimateConcept_ArchimateModelObject, gen_model_ArchimateConcept_Cloneable, gen_model_ArchimateConcept_Documentable, gen_model_ArchimateConcept_Properties, gen_model_ArchimateElement_ArchimateConcept, gen_model_ArchimateRelationship_ArchimateConcept, gen_model_StrategyElement_ArchimateElement, gen_model_BusinessElement_ArchimateElement, gen_model_ApplicationElement_ArchimateElement, gen_model_TechnologyElement_ArchimateElement, gen_model_TechnologyObject_TechnologyElement, gen_model_TechnologyObject_PassiveStructureElement, gen_model_PhysicalElement_ArchimateElement, gen_model_MotivationElement_ArchimateElement, gen_model_ImplementationMigrationElement_ArchimateElement, gen_model_CompositeElement_ArchimateElement, gen_model_BehaviorElement_ArchimateElement, gen_model_StructureElement_ArchimateElement, gen_model_ActiveStructureElement_StructureElement, gen_model_PassiveStructureElement_StructureElement, gen_model_StructuralRelationship_ArchimateRelationship, gen_model_DependendencyRelationship_ArchimateRelationship, gen_model_DynamicRelationship_ArchimateRelationship, gen_model_OtherRelationship_ArchimateRelationship, gen_model_ArchimateModel_FolderContainer, gen_model_ArchimateModel_ArchimateModelObject, gen_model_ArchimateModel_Properties, gen_model_DataObject_ApplicationElement, gen_model_DataObject_PassiveStructureElement, gen_model_Junction_ArchimateElement, gen_model_ApplicationCollaboration_ApplicationElement, gen_model_ApplicationCollaboration_ActiveStructureElement, gen_model_ApplicationComponent_ApplicationElement, gen_model_ApplicationComponent_ActiveStructureElement, gen_model_ApplicationEvent_ApplicationElement, gen_model_ApplicationEvent_BehaviorElement, gen_model_ApplicationFunction_ApplicationElement, gen_model_ApplicationFunction_BehaviorElement, gen_model_ApplicationInteraction_ApplicationElement, gen_model_ApplicationInteraction_BehaviorElement, gen_model_ApplicationInterface_ApplicationElement, gen_model_ApplicationInterface_ActiveStructureElement, gen_model_ApplicationProcess_ApplicationElement, gen_model_ApplicationProcess_BehaviorElement, gen_model_ApplicationService_ApplicationElement, gen_model_ApplicationService_BehaviorElement, gen_model_Artifact_TechnologyObject, gen_model_Assessment_MotivationElement, gen_model_BusinessActor_BusinessElement, gen_model_BusinessActor_ActiveStructureElement, gen_model_BusinessCollaboration_BusinessElement, gen_model_BusinessCollaboration_ActiveStructureElement, gen_model_BusinessEvent_BusinessElement, gen_model_BusinessEvent_BehaviorElement, gen_model_BusinessFunction_BusinessElement, gen_model_BusinessFunction_BehaviorElement, gen_model_BusinessInteraction_BusinessElement, gen_model_BusinessInteraction_BehaviorElement, gen_model_BusinessInterface_BusinessElement, gen_model_BusinessInterface_ActiveStructureElement, gen_model_BusinessObject_BusinessElement, gen_model_BusinessObject_PassiveStructureElement, gen_model_BusinessProcess_BusinessElement, gen_model_BusinessProcess_BehaviorElement, gen_model_BusinessRole_BusinessElement, gen_model_BusinessRole_ActiveStructureElement, gen_model_BusinessService_BusinessElement, gen_model_BusinessService_BehaviorElement, gen_model_Capability_StrategyElement, gen_model_Capability_BehaviorElement, gen_model_CommunicationNetwork_TechnologyElement, gen_model_CommunicationNetwork_ActiveStructureElement, gen_model_Contract_BusinessElement, gen_model_Contract_PassiveStructureElement, gen_model_Constraint_MotivationElement, gen_model_CourseOfAction_StrategyElement, gen_model_CourseOfAction_BehaviorElement, gen_model_WorkPackage_ImplementationMigrationElement, gen_model_WorkPackage_BehaviorElement, gen_model_Deliverable_ImplementationMigrationElement, gen_model_Deliverable_PassiveStructureElement, gen_model_Device_TechnologyElement, gen_model_Device_ActiveStructureElement, gen_model_DistributionNetwork_PhysicalElement, gen_model_DistributionNetwork_ActiveStructureElement, gen_model_Driver_MotivationElement, gen_model_Equipment_PhysicalElement, gen_model_Equipment_ActiveStructureElement, gen_model_Facility_PhysicalElement, gen_model_Facility_ActiveStructureElement, gen_model_Gap_ImplementationMigrationElement, gen_model_Gap_PassiveStructureElement, gen_model_Goal_MotivationElement, gen_model_Grouping_CompositeElement, gen_model_ImplementationEvent_ImplementationMigrationElement, gen_model_Location_CompositeElement, gen_model_Material_PhysicalElement, gen_model_Material_PassiveStructureElement, gen_model_Meaning_MotivationElement, gen_model_Node_TechnologyElement, gen_model_Node_ActiveStructureElement, gen_model_Outcome_MotivationElement, gen_model_Path_TechnologyElement, gen_model_Plateau_ImplementationMigrationElement, gen_model_Plateau_CompositeElement, gen_model_Principle_MotivationElement, gen_model_Product_BusinessElement, gen_model_Product_CompositeElement, gen_model_Representation_BusinessElement, gen_model_Representation_PassiveStructureElement, gen_model_Resource_StrategyElement, gen_model_Resource_StructureElement, gen_model_Requirement_MotivationElement, gen_model_Stakeholder_MotivationElement, gen_model_Stakeholder_ActiveStructureElement, gen_model_SystemSoftware_TechnologyElement, gen_model_SystemSoftware_ActiveStructureElement, gen_model_TechnologyCollaboration_TechnologyElement, gen_model_TechnologyCollaboration_ActiveStructureElement, gen_model_TechnologyEvent_TechnologyElement, gen_model_TechnologyEvent_BehaviorElement, gen_model_TechnologyFunction_TechnologyElement, gen_model_TechnologyFunction_BehaviorElement, gen_model_TechnologyInterface_TechnologyElement, gen_model_TechnologyInterface_ActiveStructureElement, gen_model_TechnologyInteraction_TechnologyElement, gen_model_TechnologyInteraction_BehaviorElement, gen_model_TechnologyProcess_TechnologyElement, gen_model_TechnologyProcess_BehaviorElement, gen_model_TechnologyService_TechnologyElement, gen_model_TechnologyService_BehaviorElement, gen_model_Value_MotivationElement, gen_model_AccessRelationship_DependendencyRelationship, gen_model_AggregationRelationship_StructuralRelationship, gen_model_AssignmentRelationship_StructuralRelationship, gen_model_AssociationRelationship_OtherRelationship, gen_model_CompositionRelationship_StructuralRelationship, gen_model_FlowRelationship_DynamicRelationship, gen_model_InfluenceRelationship_DependendencyRelationship, gen_model_RealizationRelationship_StructuralRelationship, gen_model_ServingRelationship_DependendencyRelationship, gen_model_SpecializationRelationship_OtherRelationship, gen_model_TriggeringRelationship_DynamicRelationship, gen_model_DiagramModelComponent_Identifier, gen_model_DiagramModelComponent_Cloneable, gen_model_DiagramModelComponent_Adapter, gen_model_DiagramModelComponent_Nameable, gen_model_DiagramModelComponent_ArchimateModelObject, gen_model_Connectable_DiagramModelComponent, gen_model_DiagramModelContainer_DiagramModelComponent, gen_model_DiagramModel_ArchimateModelObject, gen_model_DiagramModel_DiagramModelContainer, gen_model_DiagramModel_Documentable, gen_model_DiagramModel_Properties, gen_model_DiagramModelReference_DiagramModelObject, gen_model_DiagramModelReference_TextPosition, gen_model_DiagramModelObject_Connectable, gen_model_DiagramModelObject_FontAttribute, gen_model_DiagramModelObject_LineObject, gen_model_DiagramModelObject_TextAlignment, gen_model_DiagramModelGroup_DiagramModelObject, gen_model_DiagramModelGroup_DiagramModelContainer, gen_model_DiagramModelGroup_Documentable, gen_model_DiagramModelGroup_Properties, gen_model_DiagramModelNote_DiagramModelObject, gen_model_DiagramModelNote_TextContent, gen_model_DiagramModelNote_TextPosition, gen_model_DiagramModelImage_DiagramModelObject, gen_model_DiagramModelImage_BorderObject, gen_model_DiagramModelImage_DiagramModelImageProvider, gen_model_DiagramModelConnection_Connectable, gen_model_DiagramModelConnection_FontAttribute, gen_model_DiagramModelConnection_Properties, gen_model_DiagramModelConnection_Documentable, gen_model_DiagramModelConnection_LineObject, gen_model_DiagramModelBendpoint_Cloneable, gen_model_ArchimateDiagramModel_DiagramModel, gen_model_DiagramModelArchimateObject_DiagramModelObject, gen_model_DiagramModelArchimateObject_DiagramModelContainer, gen_model_DiagramModelArchimateObject_DiagramModelArchimateComponent, gen_model_DiagramModelArchimateObject_TextPosition, gen_model_DiagramModelArchimateConnection_DiagramModelConnection, gen_model_DiagramModelArchimateConnection_DiagramModelArchimateComponent, gen_model_SketchModel_DiagramModel, gen_model_SketchModelSticky_DiagramModelObject, gen_model_SketchModelSticky_DiagramModelContainer, gen_model_SketchModelSticky_TextContent, gen_model_SketchModelSticky_Properties, gen_model_SketchModelSticky_TextPosition, gen_model_SketchModelActor_DiagramModelObject, gen_model_SketchModelActor_Documentable, gen_model_SketchModelActor_Properties, gen_model_DiagramModelArchimateComponent_Connectable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)