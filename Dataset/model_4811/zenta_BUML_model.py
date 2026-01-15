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
model_Adapter = Class(name="model::Adapter", is_abstract=True)
model_Documentable = Class(name="model::Documentable", is_abstract=True)
model_Cloneable = Class(name="model::Cloneable", is_abstract=True)
model_FolderContainer = Class(name="model::FolderContainer", is_abstract=True)
model_Folder = Class(name="model::Folder")
model_ZentaModelElement = Class(name="model::ZentaModelElement", is_abstract=True)
Adapter = Class(name="Adapter")
model_ZentaModel = Class(name="model::ZentaModel")
ZentaModelElement = Class(name="ZentaModelElement")
FolderContainer = Class(name="FolderContainer")
Identifier = Class(name="Identifier")
Documentable = Class(name="Documentable")
Properties = Class(name="Properties")
model_Identifier = Class(name="model::Identifier", is_abstract=True)
Nameable = Class(name="Nameable")
model_Property = Class(name="model::Property")
model_Properties = Class(name="model::Properties", is_abstract=True)
model_Nameable = Class(name="model::Nameable", is_abstract=True)
model_TextContent = Class(name="model::TextContent", is_abstract=True)
model_DiagramModelContainer = Class(name="model::DiagramModelContainer", is_abstract=True)
DiagramModelComponent = Class(name="DiagramModelComponent")
model_DiagramModelObject = Class(name="model::DiagramModelObject", is_abstract=True)
model_DiagramModelReference = Class(name="model::DiagramModelReference")
DiagramModelObject = Class(name="DiagramModelObject")
FontAttribute = Class(name="FontAttribute")
model_Bounds = Class(name="model::Bounds")
model_DiagramModelConnection = Class(name="model::DiagramModelConnection")
model_JunctionElement = Class(name="model::JunctionElement", is_abstract=True)
ZentaElement = Class(name="ZentaElement")
model_InterfaceElement = Class(name="model::InterfaceElement", is_abstract=True)
model_Junction = Class(name="model::Junction")
JunctionElement = Class(name="JunctionElement")
model_AndJunction = Class(name="model::AndJunction")
model_OrJunction = Class(name="model::OrJunction")
model_DiagramModelComponent = Class(name="model::DiagramModelComponent", is_abstract=True)
Cloneable = Class(name="Cloneable")
model_DiagramModel = Class(name="model::DiagramModel", is_abstract=True)
model_DiagramModelBendpoint = Class(name="model::DiagramModelBendpoint")
model_FontAttribute = Class(name="model::FontAttribute", is_abstract=True)
model_BorderObject = Class(name="model::BorderObject", is_abstract=True)
model_DiagramModelImageProvider = Class(name="model::DiagramModelImageProvider", is_abstract=True)
model_DiagramModelGroup = Class(name="model::DiagramModelGroup")
DiagramModelContainer = Class(name="DiagramModelContainer")
model_DiagramModelNote = Class(name="model::DiagramModelNote")
TextContent = Class(name="TextContent")
model_DiagramModelImage = Class(name="model::DiagramModelImage")
BorderObject = Class(name="BorderObject")
DiagramModelImageProvider = Class(name="DiagramModelImageProvider")
model_SketchModelSticky = Class(name="model::SketchModelSticky")
model_SketchModelActor = Class(name="model::SketchModelActor")
Folder = Class(name="Folder")
model_Metamodel = Class(name="model::Metamodel")
model_Template = Class(name="model::Template")
model_BasicObject = Class(name="model::BasicObject")
model_Lockable = Class(name="model::Lockable", is_abstract=True)
model_ZentaDiagramModel = Class(name="model::ZentaDiagramModel")
DiagramModel = Class(name="DiagramModel")
model_DiagramModelZentaObject = Class(name="model::DiagramModelZentaObject")
model_ZentaElement = Class(name="model::ZentaElement", is_abstract=True)
model_DiagramModelZentaConnection = Class(name="model::DiagramModelZentaConnection")
DiagramModelConnection = Class(name="DiagramModelConnection")
model_BasicRelationship = Class(name="model::BasicRelationship")
model_SketchModel = Class(name="model::SketchModel")
BasicObject = Class(name="BasicObject")
model_Attribute = Class(name="model::Attribute")

# model_Adapter class attributes and methods
model_Adapter_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
model_Adapter_m_setAdapter: Method = Method(name="setAdapter", parameters={Parameter(name='object'), Parameter(name='adapter')})
model_Adapter.methods={model_Adapter_m_getAdapter, model_Adapter_m_setAdapter}

# model_Documentable class attributes and methods
model_Documentable_documentation: Property = Property(name="documentation", type=StringType)
model_Documentable.attributes={model_Documentable_documentation}

# model_Cloneable class attributes and methods
model_Cloneable_m_getCopy: Method = Method(name="getCopy", parameters={}, type=StringType)
model_Cloneable.methods={model_Cloneable_m_getCopy}

# model_FolderContainer class attributes and methods

# model_Folder class attributes and methods

# model_ZentaModelElement class attributes and methods

# Adapter class attributes and methods

# model_ZentaModel class attributes and methods
model_ZentaModel_file: Property = Property(name="file", type=StringType)
model_ZentaModel_version: Property = Property(name="version", type=StringType)
model_ZentaModel_m_getDefaultFolderForElement: Method = Method(name="getDefaultFolderForElement", parameters={Parameter(name='element')}, type=Folder)
model_ZentaModel_m_getDefaultDiagramModel: Method = Method(name="getDefaultDiagramModel", parameters={}, type=DiagramModel)
model_ZentaModel_m_getDiagramModels: Method = Method(name="getDiagramModels", parameters={}, type=DiagramModel)
model_ZentaModel.attributes={model_ZentaModel_file, model_ZentaModel_version}
model_ZentaModel.methods={model_ZentaModel_m_getDiagramModels, model_ZentaModel_m_getDefaultFolderForElement, model_ZentaModel_m_getDefaultDiagramModel}

# ZentaModelElement class attributes and methods

# FolderContainer class attributes and methods

# Identifier class attributes and methods

# Documentable class attributes and methods

# Properties class attributes and methods

# model_Identifier class attributes and methods
model_Identifier_id: Property = Property(name="id", type=StringType)
model_Identifier.attributes={model_Identifier_id}

# Nameable class attributes and methods

# model_Property class attributes and methods
model_Property_key: Property = Property(name="key", type=StringType)
model_Property_value: Property = Property(name="value", type=StringType)
model_Property_generated: Property = Property(name="generated", type=BooleanType)
model_Property.attributes={model_Property_key, model_Property_generated, model_Property_value}

# model_Properties class attributes and methods

# model_Nameable class attributes and methods
model_Nameable_name: Property = Property(name="name", type=StringType)
model_Nameable.attributes={model_Nameable_name}

# model_TextContent class attributes and methods
model_TextContent_content: Property = Property(name="content", type=StringType)
model_TextContent.attributes={model_TextContent_content}

# model_DiagramModelContainer class attributes and methods

# DiagramModelComponent class attributes and methods

# model_DiagramModelObject class attributes and methods
model_DiagramModelObject_fillColor: Property = Property(name="fillColor", type=StringType)
model_DiagramModelObject_elementShape: Property = Property(name="elementShape", type=StringType)
model_DiagramModelObject_m_addConnection: Method = Method(name="addConnection", parameters={Parameter(name='connection')})
model_DiagramModelObject_m_removeConnection: Method = Method(name="removeConnection", parameters={Parameter(name='connection')})
model_DiagramModelObject_m_setBounds: Method = Method(name="setBounds", parameters={Parameter(name='width'), Parameter(name='height'), Parameter(name='y'), Parameter(name='x')})
model_DiagramModelObject.attributes={model_DiagramModelObject_elementShape, model_DiagramModelObject_fillColor}
model_DiagramModelObject.methods={model_DiagramModelObject_m_setBounds, model_DiagramModelObject_m_addConnection, model_DiagramModelObject_m_removeConnection}

# model_DiagramModelReference class attributes and methods

# DiagramModelObject class attributes and methods

# FontAttribute class attributes and methods

# model_Bounds class attributes and methods
model_Bounds_x: Property = Property(name="x", type=IntegerType)
model_Bounds_y: Property = Property(name="y", type=IntegerType)
model_Bounds_width: Property = Property(name="width", type=IntegerType)
model_Bounds_height: Property = Property(name="height", type=IntegerType)
model_Bounds_m_getCopy: Method = Method(name="getCopy", parameters={}, type=StringType)
model_Bounds.attributes={model_Bounds_y, model_Bounds_height, model_Bounds_x, model_Bounds_width}
model_Bounds.methods={model_Bounds_m_getCopy}

# model_DiagramModelConnection class attributes and methods
model_DiagramModelConnection_lineDecoration: Property = Property(name="lineDecoration", type=StringType)
model_DiagramModelConnection_type: Property = Property(name="type", type=IntegerType)
model_DiagramModelConnection_text: Property = Property(name="text", type=StringType)
model_DiagramModelConnection_m_connect: Method = Method(name="connect", parameters={Parameter(name='source'), Parameter(name='target')})
model_DiagramModelConnection_m_disconnect: Method = Method(name="disconnect", parameters={})
model_DiagramModelConnection_m_reconnect: Method = Method(name="reconnect", parameters={})
model_DiagramModelConnection.attributes={model_DiagramModelConnection_type, model_DiagramModelConnection_lineDecoration, model_DiagramModelConnection_text}
model_DiagramModelConnection.methods={model_DiagramModelConnection_m_disconnect, model_DiagramModelConnection_m_connect, model_DiagramModelConnection_m_reconnect}

# model_JunctionElement class attributes and methods

# ZentaElement class attributes and methods

# model_InterfaceElement class attributes and methods
model_InterfaceElement_interfaceType: Property = Property(name="interfaceType", type=IntegerType)
model_InterfaceElement.attributes={model_InterfaceElement_interfaceType}

# model_Junction class attributes and methods

# JunctionElement class attributes and methods

# model_AndJunction class attributes and methods

# model_OrJunction class attributes and methods

# model_DiagramModelComponent class attributes and methods
model_DiagramModelComponent_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
model_DiagramModelComponent_lineColor: Property = Property(name="lineColor", type=StringType)
model_DiagramModelComponent.attributes={model_DiagramModelComponent_lineColor, model_DiagramModelComponent_lineWidth}

# Cloneable class attributes and methods

# model_DiagramModel class attributes and methods
model_DiagramModel_connectionRouterType: Property = Property(name="connectionRouterType", type=IntegerType)
model_DiagramModel.attributes={model_DiagramModel_connectionRouterType}

# model_DiagramModelBendpoint class attributes and methods
model_DiagramModelBendpoint_startX: Property = Property(name="startX", type=IntegerType)
model_DiagramModelBendpoint_startY: Property = Property(name="startY", type=IntegerType)
model_DiagramModelBendpoint_endX: Property = Property(name="endX", type=IntegerType)
model_DiagramModelBendpoint_endY: Property = Property(name="endY", type=IntegerType)
model_DiagramModelBendpoint.attributes={model_DiagramModelBendpoint_endY, model_DiagramModelBendpoint_endX, model_DiagramModelBendpoint_startX, model_DiagramModelBendpoint_startY}

# model_FontAttribute class attributes and methods
model_FontAttribute_font: Property = Property(name="font", type=StringType)
model_FontAttribute_fontColor: Property = Property(name="fontColor", type=StringType)
model_FontAttribute_textAlignment: Property = Property(name="textAlignment", type=IntegerType)
model_FontAttribute_textPosition: Property = Property(name="textPosition", type=IntegerType)
model_FontAttribute_m_getDefaultTextAlignment: Method = Method(name="getDefaultTextAlignment", parameters={}, type=IntegerType)
model_FontAttribute.attributes={model_FontAttribute_font, model_FontAttribute_fontColor, model_FontAttribute_textPosition, model_FontAttribute_textAlignment}
model_FontAttribute.methods={model_FontAttribute_m_getDefaultTextAlignment}

# model_BorderObject class attributes and methods
model_BorderObject_borderColor: Property = Property(name="borderColor", type=StringType)
model_BorderObject.attributes={model_BorderObject_borderColor}

# model_DiagramModelImageProvider class attributes and methods
model_DiagramModelImageProvider_imagePath: Property = Property(name="imagePath", type=StringType)
model_DiagramModelImageProvider.attributes={model_DiagramModelImageProvider_imagePath}

# model_DiagramModelGroup class attributes and methods

# DiagramModelContainer class attributes and methods

# model_DiagramModelNote class attributes and methods

# TextContent class attributes and methods

# model_DiagramModelImage class attributes and methods

# BorderObject class attributes and methods

# DiagramModelImageProvider class attributes and methods

# model_SketchModelSticky class attributes and methods

# model_SketchModelActor class attributes and methods

# Folder class attributes and methods

# model_Metamodel class attributes and methods

# model_Template class attributes and methods
model_Template_path: Property = Property(name="path", type=StringType)
model_Template.attributes={model_Template_path}

# model_BasicObject class attributes and methods

# model_Lockable class attributes and methods
model_Lockable_locked: Property = Property(name="locked", type=BooleanType)
model_Lockable.attributes={model_Lockable_locked}

# model_ZentaDiagramModel class attributes and methods
model_ZentaDiagramModel_viewpoint: Property = Property(name="viewpoint", type=IntegerType)
model_ZentaDiagramModel.attributes={model_ZentaDiagramModel_viewpoint}

# DiagramModel class attributes and methods

# model_DiagramModelZentaObject class attributes and methods
model_DiagramModelZentaObject_type: Property = Property(name="type", type=IntegerType)
model_DiagramModelZentaObject_m_addZentaElementToModel: Method = Method(name="addZentaElementToModel", parameters={Parameter(name='parent')})
model_DiagramModelZentaObject_m_removeZentaElementFromModel: Method = Method(name="removeZentaElementFromModel", parameters={})
model_DiagramModelZentaObject.attributes={model_DiagramModelZentaObject_type}
model_DiagramModelZentaObject.methods={model_DiagramModelZentaObject_m_removeZentaElementFromModel, model_DiagramModelZentaObject_m_addZentaElementToModel}

# model_ZentaElement class attributes and methods

# model_DiagramModelZentaConnection class attributes and methods
model_DiagramModelZentaConnection_m_addRelationshipToModel: Method = Method(name="addRelationshipToModel", parameters={Parameter(name='parent')})
model_DiagramModelZentaConnection_m_removeRelationshipFromModel: Method = Method(name="removeRelationshipFromModel", parameters={})
model_DiagramModelZentaConnection.methods={model_DiagramModelZentaConnection_m_removeRelationshipFromModel, model_DiagramModelZentaConnection_m_addRelationshipToModel}

# DiagramModelConnection class attributes and methods

# model_BasicRelationship class attributes and methods

# model_SketchModel class attributes and methods
model_SketchModel_background: Property = Property(name="background", type=IntegerType)
model_SketchModel.attributes={model_SketchModel_background}

# BasicObject class attributes and methods

# model_Attribute class attributes and methods
model_Attribute_minOccurs: Property = Property(name="minOccurs", type=IntegerType)
model_Attribute_maxOccurs: Property = Property(name="maxOccurs", type=IntegerType)
model_Attribute.attributes={model_Attribute_minOccurs, model_Attribute_maxOccurs}

# Relationships
folders1: BinaryAssociation = BinaryAssociation(
    name="folders1",
    ends={
        Property(name="model_Folder", type=model_FolderContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FolderContainer", type=model_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zentaModel2: BinaryAssociation = BinaryAssociation(
    name="zentaModel2",
    ends={
        Property(name="model_ZentaModel", type=model_ZentaModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ZentaModelElement", type=model_ZentaModel, multiplicity=Multiplicity(0, 1))
    }
)
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="model_Property", type=model_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Properties", type=model_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="model_DiagramModelObject", type=model_DiagramModelContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelContainer", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModel7: BinaryAssociation = BinaryAssociation(
    name="referencedModel7",
    ends={
        Property(name="model_DiagramModel8", type=model_DiagramModelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelReference", type=model_DiagramModel, multiplicity=Multiplicity(0, 1))
    }
)
bounds9: BinaryAssociation = BinaryAssociation(
    name="bounds9",
    ends={
        Property(name="model_Bounds", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject10", type=model_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceConnections11: BinaryAssociation = BinaryAssociation(
    name="sourceConnections11",
    ends={
        Property(name="model_DiagramModelConnection", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject12", type=model_DiagramModelConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="model_Nameable", type=model_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Folder4", type=model_Nameable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramModel5: BinaryAssociation = BinaryAssociation(
    name="diagramModel5",
    ends={
        Property(name="model_DiagramModel", type=model_DiagramModelComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelComponent", type=model_DiagramModel, multiplicity=Multiplicity(0, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="model_DiagramModelObject21", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection20", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 1))
    }
)
bendpoints22: BinaryAssociation = BinaryAssociation(
    name="bendpoints22",
    ends={
        Property(name="model_DiagramModelBendpoint", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection23", type=model_DiagramModelBendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetConnections13: BinaryAssociation = BinaryAssociation(
    name="targetConnections13",
    ends={
        Property(name="model_DiagramModelConnection15", type=model_DiagramModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelObject14", type=model_DiagramModelConnection, multiplicity=Multiplicity(0, 9999))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="model_DiagramModelObject18", type=model_DiagramModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramModelConnection17", type=model_DiagramModelObject, multiplicity=Multiplicity(0, 1))
    }
)
templates26: BinaryAssociation = BinaryAssociation(
    name="templates26",
    ends={
        Property(name="Template", type=model_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=model_Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes27: BinaryAssociation = BinaryAssociation(
    name="classes27",
    ends={
        Property(name="BasicObject", type=model_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=model_BasicObject, multiplicity=Multiplicity(0, 9999))
    }
)
zentaElement24: BinaryAssociation = BinaryAssociation(
    name="zentaElement24",
    ends={
        Property(name="ZentaElement", type=model_DiagramModelZentaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="diagObjects", type=model_ZentaElement, multiplicity=Multiplicity(0, 1))
    }
)
relationship25: BinaryAssociation = BinaryAssociation(
    name="relationship25",
    ends={
        Property(name="BasicRelationship", type=model_DiagramModelZentaConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagConnections", type=model_BasicRelationship, multiplicity=Multiplicity(0, 1))
    }
)
attributes32: BinaryAssociation = BinaryAssociation(
    name="attributes32",
    ends={
        Property(name="model_BasicObject", type=model_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="model_Attribute", type=model_BasicObject, multiplicity=Multiplicity(1, 1))
    }
)
ancestor34: BinaryAssociation = BinaryAssociation(
    name="ancestor34",
    ends={
        Property(name="BasicObject35", type=model_BasicObject, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=model_BasicObject, multiplicity=Multiplicity(1, 1))
    }
)
children37: BinaryAssociation = BinaryAssociation(
    name="children37",
    ends={
        Property(name="BasicObject38", type=model_BasicObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ancestor", type=model_BasicObject, multiplicity=Multiplicity(0, 9999))
    }
)
template39: BinaryAssociation = BinaryAssociation(
    name="template39",
    ends={
        Property(name="Template40", type=model_BasicObject, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=model_Template, multiplicity=Multiplicity(0, 1))
    }
)
source41: BinaryAssociation = BinaryAssociation(
    name="source41",
    ends={
        Property(name="model_ZentaElement", type=model_BasicRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicRelationship", type=model_ZentaElement, multiplicity=Multiplicity(0, 1))
    }
)
target42: BinaryAssociation = BinaryAssociation(
    name="target42",
    ends={
        Property(name="model_ZentaElement44", type=model_BasicRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicRelationship43", type=model_ZentaElement, multiplicity=Multiplicity(0, 1))
    }
)
diagConnections45: BinaryAssociation = BinaryAssociation(
    name="diagConnections45",
    ends={
        Property(name="DiagramModelZentaConnection", type=model_BasicRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationship", type=model_DiagramModelZentaConnection, multiplicity=Multiplicity(0, 9999))
    }
)
relation46: BinaryAssociation = BinaryAssociation(
    name="relation46",
    ends={
        Property(name="model_BasicRelationship48", type=model_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Attribute47", type=model_BasicRelationship, multiplicity=Multiplicity(1, 1))
    }
)
connectedObject49: BinaryAssociation = BinaryAssociation(
    name="connectedObject49",
    ends={
        Property(name="model_BasicObject51", type=model_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Attribute50", type=model_BasicObject, multiplicity=Multiplicity(1, 1))
    }
)
metamodel28: BinaryAssociation = BinaryAssociation(
    name="metamodel28",
    ends={
        Property(name="Metamodel", type=model_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="templates", type=model_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
diagram29: BinaryAssociation = BinaryAssociation(
    name="diagram29",
    ends={
        Property(name="model_DiagramModel30", type=model_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Template", type=model_DiagramModel, multiplicity=Multiplicity(0, 1))
    }
)
diagObjects31: BinaryAssociation = BinaryAssociation(
    name="diagObjects31",
    ends={
        Property(name="DiagramModelZentaObject", type=model_ZentaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="zentaElement", type=model_DiagramModelZentaObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_model_ZentaModelElement_Adapter = Generalization(general=Adapter, specific=model_ZentaModelElement)
gen_model_Folder_ZentaModelElement = Generalization(general=ZentaModelElement, specific=model_Folder)
gen_model_Folder_FolderContainer = Generalization(general=FolderContainer, specific=model_Folder)
gen_model_Folder_Nameable = Generalization(general=Nameable, specific=model_Folder)
gen_model_Folder_Identifier = Generalization(general=Identifier, specific=model_Folder)
gen_model_Folder_Documentable = Generalization(general=Documentable, specific=model_Folder)
gen_model_Folder_Properties = Generalization(general=Properties, specific=model_Folder)
gen_model_Identifier_Nameable = Generalization(general=Nameable, specific=model_Identifier)
gen_model_DiagramModelContainer_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_DiagramModelContainer)
gen_model_DiagramModelReference_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelReference)
gen_model_DiagramModelObject_DiagramModelComponent = Generalization(general=DiagramModelComponent, specific=model_DiagramModelObject)
gen_model_DiagramModelObject_FontAttribute = Generalization(general=FontAttribute, specific=model_DiagramModelObject)
gen_model_JunctionElement_ZentaElement = Generalization(general=ZentaElement, specific=model_JunctionElement)
gen_model_InterfaceElement_ZentaElement = Generalization(general=ZentaElement, specific=model_InterfaceElement)
gen_model_Junction_JunctionElement = Generalization(general=JunctionElement, specific=model_Junction)
gen_model_AndJunction_JunctionElement = Generalization(general=JunctionElement, specific=model_AndJunction)
gen_model_OrJunction_JunctionElement = Generalization(general=JunctionElement, specific=model_OrJunction)
gen_model_DiagramModelComponent_Identifier = Generalization(general=Identifier, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Cloneable = Generalization(general=Cloneable, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Adapter = Generalization(general=Adapter, specific=model_DiagramModelComponent)
gen_model_DiagramModelComponent_Nameable = Generalization(general=Nameable, specific=model_DiagramModelComponent)
gen_model_DiagramModelBendpoint_Cloneable = Generalization(general=Cloneable, specific=model_DiagramModelBendpoint)
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
gen_model_SketchModelSticky_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_TextContent = Generalization(general=TextContent, specific=model_SketchModelSticky)
gen_model_SketchModelSticky_Properties = Generalization(general=Properties, specific=model_SketchModelSticky)
gen_model_SketchModelActor_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_SketchModelActor)
gen_model_SketchModelActor_Documentable = Generalization(general=Documentable, specific=model_SketchModelActor)
gen_model_SketchModelActor_Properties = Generalization(general=Properties, specific=model_SketchModelActor)
gen_model_DiagramModel_ZentaModelElement = Generalization(general=ZentaModelElement, specific=model_DiagramModel)
gen_model_DiagramModel_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModel)
gen_model_DiagramModel_Documentable = Generalization(general=Documentable, specific=model_DiagramModel)
gen_model_DiagramModel_Properties = Generalization(general=Properties, specific=model_DiagramModel)
gen_model_ZentaModel_FolderContainer = Generalization(general=FolderContainer, specific=model_ZentaModel)
gen_model_ZentaModel_Nameable = Generalization(general=Nameable, specific=model_ZentaModel)
gen_model_ZentaModel_Identifier = Generalization(general=Identifier, specific=model_ZentaModel)
gen_model_ZentaModel_ZentaModelElement = Generalization(general=ZentaModelElement, specific=model_ZentaModel)
gen_model_ZentaModel_Properties = Generalization(general=Properties, specific=model_ZentaModel)
gen_model_ZentaModel_Documentable = Generalization(general=Documentable, specific=model_ZentaModel)
gen_model_ZentaModel_Folder = Generalization(general=Folder, specific=model_ZentaModel)
gen_model_ZentaDiagramModel_DiagramModel = Generalization(general=DiagramModel, specific=model_ZentaDiagramModel)
gen_model_DiagramModelZentaObject_DiagramModelObject = Generalization(general=DiagramModelObject, specific=model_DiagramModelZentaObject)
gen_model_DiagramModelZentaObject_DiagramModelContainer = Generalization(general=DiagramModelContainer, specific=model_DiagramModelZentaObject)
gen_model_DiagramModelZentaConnection_DiagramModelConnection = Generalization(general=DiagramModelConnection, specific=model_DiagramModelZentaConnection)
gen_model_SketchModel_DiagramModel = Generalization(general=DiagramModel, specific=model_SketchModel)
gen_model_BasicRelationship_BasicObject = Generalization(general=BasicObject, specific=model_BasicRelationship)
gen_model_ZentaElement_ZentaModelElement = Generalization(general=ZentaModelElement, specific=model_ZentaElement)
gen_model_ZentaElement_Identifier = Generalization(general=Identifier, specific=model_ZentaElement)
gen_model_ZentaElement_Cloneable = Generalization(general=Cloneable, specific=model_ZentaElement)
gen_model_ZentaElement_Nameable = Generalization(general=Nameable, specific=model_ZentaElement)
gen_model_ZentaElement_Documentable = Generalization(general=Documentable, specific=model_ZentaElement)
gen_model_ZentaElement_Properties = Generalization(general=Properties, specific=model_ZentaElement)
gen_model_BasicObject_ZentaElement = Generalization(general=ZentaElement, specific=model_BasicObject)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Adapter, model_Documentable, model_Cloneable, model_FolderContainer, model_Folder, model_ZentaModelElement, Adapter, model_ZentaModel, ZentaModelElement, FolderContainer, Identifier, Documentable, Properties, model_Identifier, Nameable, model_Property, model_Properties, model_Nameable, model_TextContent, model_DiagramModelContainer, DiagramModelComponent, model_DiagramModelObject, model_DiagramModelReference, DiagramModelObject, FontAttribute, model_Bounds, model_DiagramModelConnection, model_JunctionElement, ZentaElement, model_InterfaceElement, model_Junction, JunctionElement, model_AndJunction, model_OrJunction, model_DiagramModelComponent, Cloneable, model_DiagramModel, model_DiagramModelBendpoint, model_FontAttribute, model_BorderObject, model_DiagramModelImageProvider, model_DiagramModelGroup, DiagramModelContainer, model_DiagramModelNote, TextContent, model_DiagramModelImage, BorderObject, DiagramModelImageProvider, model_SketchModelSticky, model_SketchModelActor, Folder, model_Metamodel, model_Template, model_BasicObject, model_Lockable, model_ZentaDiagramModel, DiagramModel, model_DiagramModelZentaObject, model_ZentaElement, model_DiagramModelZentaConnection, DiagramModelConnection, model_BasicRelationship, model_SketchModel, BasicObject, model_Attribute},
    associations={folders1, zentaModel2, properties0, children6, referencedModel7, bounds9, sourceConnections11, elements3, diagramModel5, target19, bendpoints22, targetConnections13, source16, templates26, classes27, zentaElement24, relationship25, attributes32, ancestor34, children37, template39, source41, target42, diagConnections45, relation46, connectedObject49, metamodel28, diagram29, diagObjects31},
    generalizations={gen_model_ZentaModelElement_Adapter, gen_model_Folder_ZentaModelElement, gen_model_Folder_FolderContainer, gen_model_Folder_Nameable, gen_model_Folder_Identifier, gen_model_Folder_Documentable, gen_model_Folder_Properties, gen_model_Identifier_Nameable, gen_model_DiagramModelContainer_DiagramModelComponent, gen_model_DiagramModelReference_DiagramModelObject, gen_model_DiagramModelObject_DiagramModelComponent, gen_model_DiagramModelObject_FontAttribute, gen_model_JunctionElement_ZentaElement, gen_model_InterfaceElement_ZentaElement, gen_model_Junction_JunctionElement, gen_model_AndJunction_JunctionElement, gen_model_OrJunction_JunctionElement, gen_model_DiagramModelComponent_Identifier, gen_model_DiagramModelComponent_Cloneable, gen_model_DiagramModelComponent_Adapter, gen_model_DiagramModelComponent_Nameable, gen_model_DiagramModelBendpoint_Cloneable, gen_model_DiagramModelGroup_DiagramModelObject, gen_model_DiagramModelGroup_DiagramModelContainer, gen_model_DiagramModelGroup_Documentable, gen_model_DiagramModelGroup_Properties, gen_model_DiagramModelNote_DiagramModelObject, gen_model_DiagramModelNote_TextContent, gen_model_DiagramModelImage_DiagramModelObject, gen_model_DiagramModelImage_BorderObject, gen_model_DiagramModelImage_DiagramModelImageProvider, gen_model_DiagramModelConnection_DiagramModelComponent, gen_model_DiagramModelConnection_FontAttribute, gen_model_DiagramModelConnection_Properties, gen_model_DiagramModelConnection_Documentable, gen_model_SketchModelSticky_DiagramModelObject, gen_model_SketchModelSticky_DiagramModelContainer, gen_model_SketchModelSticky_TextContent, gen_model_SketchModelSticky_Properties, gen_model_SketchModelActor_DiagramModelObject, gen_model_SketchModelActor_Documentable, gen_model_SketchModelActor_Properties, gen_model_DiagramModel_ZentaModelElement, gen_model_DiagramModel_DiagramModelContainer, gen_model_DiagramModel_Documentable, gen_model_DiagramModel_Properties, gen_model_ZentaModel_FolderContainer, gen_model_ZentaModel_Nameable, gen_model_ZentaModel_Identifier, gen_model_ZentaModel_ZentaModelElement, gen_model_ZentaModel_Properties, gen_model_ZentaModel_Documentable, gen_model_ZentaModel_Folder, gen_model_ZentaDiagramModel_DiagramModel, gen_model_DiagramModelZentaObject_DiagramModelObject, gen_model_DiagramModelZentaObject_DiagramModelContainer, gen_model_DiagramModelZentaConnection_DiagramModelConnection, gen_model_SketchModel_DiagramModel, gen_model_BasicRelationship_BasicObject, gen_model_ZentaElement_ZentaModelElement, gen_model_ZentaElement_Identifier, gen_model_ZentaElement_Cloneable, gen_model_ZentaElement_Nameable, gen_model_ZentaElement_Documentable, gen_model_ZentaElement_Properties, gen_model_BasicObject_ZentaElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)