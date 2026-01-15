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
TreeDragSource: Enumeration = Enumeration(
    name="TreeDragSource",
    literals={
            EnumerationLiteral(name="TREE"),
			EnumerationLiteral(name="PROJECT_EXPLORER"),
			EnumerationLiteral(name="BOTH")
    }
)

# Classes
tree_DTree = Class(name="tree::DTree")
DRepresentation = Class(name="DRepresentation")
DTreeItemContainer = Class(name="DTreeItemContainer")
tree_EObject = Class(name="tree::EObject")
TreeDescription = Class(name="TreeDescription")
tree_DTreeElement = Class(name="tree::DTreeElement")
DRepresentationElement = Class(name="DRepresentationElement")
TreeMapping = Class(name="TreeMapping")
DSemanticDecorator = Class(name="DSemanticDecorator")
tree_DTreeItem = Class(name="tree::DTreeItem")
DTreeElement = Class(name="DTreeElement")
tree_TreeItemStyle = Class(name="tree::TreeItemStyle")
TreeItemMapping = Class(name="TreeItemMapping")
StyleUpdater = Class(name="StyleUpdater")
TreeItemUpdater = Class(name="TreeItemUpdater")
Style = Class(name="Style")
LabelStyle = Class(name="LabelStyle")
tree_DTreeElementSynchronizer = Class(name="tree::DTreeElementSynchronizer")
IdentifiedElement = Class(name="IdentifiedElement")
tree_DTreeItemContainer = Class(name="tree::DTreeItemContainer", is_abstract=True)
tree_description_TreeDescription = Class(name="tree::description::TreeDescription")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_TreeItemMappingContainer = Class(name="description::TreeItemMappingContainer")
TreeItemCreationTool = Class(name="TreeItemCreationTool")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
tool_RepresentationNavigationDescription = Class(name="tool::RepresentationNavigationDescription")
tree_description_TreeItemMapping = Class(name="tree::description::TreeItemMapping")
description_TreeMapping = Class(name="description::TreeMapping")
description_StyleUpdater = Class(name="description::StyleUpdater")
description_TreeItemUpdater = Class(name="description::TreeItemUpdater")
TreeItemDragTool = Class(name="TreeItemDragTool")
TreePopupMenu = Class(name="TreePopupMenu")
tree_description_TreeItemStyleDescription = Class(name="tree::description::TreeItemStyleDescription")
style_StyleDescription = Class(name="style::StyleDescription")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
ColorDescription = Class(name="ColorDescription")
tree_description_ConditionalTreeItemStyleDescription = Class(name="tree::description::ConditionalTreeItemStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
TreeItemStyleDescription = Class(name="TreeItemStyleDescription")
tree_description_TreeItemTool = Class(name="tree::description::TreeItemTool", is_abstract=True)
AbstractToolDescription = Class(name="AbstractToolDescription")
tool_ModelOperation = Class(name="tool::ModelOperation")
TreeItemDeletionTool = Class(name="TreeItemDeletionTool")
TreeVariable = Class(name="TreeVariable")
tree_description_TreeItemDragTool = Class(name="tree::description::TreeItemDragTool")
tool_MappingBasedToolDescription = Class(name="tool::MappingBasedToolDescription")
description_TreeItemTool = Class(name="description::TreeItemTool")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
tool_ElementDropVariable = Class(name="tool::ElementDropVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
TreeItemMappingContainer = Class(name="TreeItemMappingContainer")
PrecedingSiblingsVariables = Class(name="PrecedingSiblingsVariables")
tree_description_TreeItemContainerDropTool = Class(name="tree::description::TreeItemContainerDropTool")
tree_description_TreeItemCreationTool = Class(name="tree::description::TreeItemCreationTool")
tree_description_TreeItemEditionTool = Class(name="tree::description::TreeItemEditionTool")
TreeItemTool = Class(name="TreeItemTool")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
tree_description_StyleUpdater = Class(name="tree::description::StyleUpdater")
tree_description_TreeItemDeletionTool = Class(name="tree::description::TreeItemDeletionTool")
tree_description_TreeCreationDescription = Class(name="tree::description::TreeCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
tree_description_TreeNavigationDescription = Class(name="tree::description::TreeNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
tree_description_TreeMapping = Class(name="tree::description::TreeMapping")
RepresentationElementMapping = Class(name="RepresentationElementMapping")
tree_description_TreePopupMenu = Class(name="tree::description::TreePopupMenu")
tool_MenuItemOrRef = Class(name="tool::MenuItemOrRef")
ConditionalTreeItemStyleDescription = Class(name="ConditionalTreeItemStyleDescription")
tree_description_TreeVariable = Class(name="tree::description::TreeVariable")
description_AbstractVariable = Class(name="description::AbstractVariable")
tool_VariableContainer = Class(name="tool::VariableContainer")
tree_description_TreeItemUpdater = Class(name="tree::description::TreeItemUpdater")
TreeItemEditionTool = Class(name="TreeItemEditionTool")
tree_description_PrecedingSiblingsVariables = Class(name="tree::description::PrecedingSiblingsVariables")
tree_description_TreeItemMappingContainer = Class(name="tree::description::TreeItemMappingContainer", is_abstract=True)
TreeItemContainerDropTool = Class(name="TreeItemContainerDropTool")

# tree_DTree class attributes and methods

# DRepresentation class attributes and methods

# DTreeItemContainer class attributes and methods

# tree_EObject class attributes and methods

# TreeDescription class attributes and methods

# tree_DTreeElement class attributes and methods

# DRepresentationElement class attributes and methods

# TreeMapping class attributes and methods

# DSemanticDecorator class attributes and methods

# tree_DTreeItem class attributes and methods
tree_DTreeItem_expanded: Property = Property(name="expanded", type=BooleanType)
tree_DTreeItem.attributes={tree_DTreeItem_expanded}

# DTreeElement class attributes and methods

# tree_TreeItemStyle class attributes and methods
tree_TreeItemStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
tree_TreeItemStyle.attributes={tree_TreeItemStyle_backgroundColor}

# TreeItemMapping class attributes and methods

# StyleUpdater class attributes and methods

# TreeItemUpdater class attributes and methods

# Style class attributes and methods

# LabelStyle class attributes and methods

# tree_DTreeElementSynchronizer class attributes and methods
tree_DTreeElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='DTreeItem')})
tree_DTreeElementSynchronizer.methods={tree_DTreeElementSynchronizer_m_refresh}

# IdentifiedElement class attributes and methods

# tree_DTreeItemContainer class attributes and methods

# tree_description_TreeDescription class attributes and methods
tree_description_TreeDescription_domainClass: Property = Property(name="domainClass", type=StringType)
tree_description_TreeDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
tree_description_TreeDescription.attributes={tree_description_TreeDescription_preconditionExpression, tree_description_TreeDescription_domainClass}

# description_RepresentationDescription class attributes and methods

# description_TreeItemMappingContainer class attributes and methods

# TreeItemCreationTool class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# tree_description_TreeItemMapping class attributes and methods
tree_description_TreeItemMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
tree_description_TreeItemMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
tree_description_TreeItemMapping_domainClass: Property = Property(name="domainClass", type=StringType)
tree_description_TreeItemMapping.attributes={tree_description_TreeItemMapping_preconditionExpression, tree_description_TreeItemMapping_semanticCandidatesExpression, tree_description_TreeItemMapping_domainClass}

# description_TreeMapping class attributes and methods

# description_StyleUpdater class attributes and methods

# description_TreeItemUpdater class attributes and methods

# TreeItemDragTool class attributes and methods

# TreePopupMenu class attributes and methods

# tree_description_TreeItemStyleDescription class attributes and methods

# style_StyleDescription class attributes and methods

# style_LabelStyleDescription class attributes and methods

# ColorDescription class attributes and methods

# tree_description_ConditionalTreeItemStyleDescription class attributes and methods

# ConditionalStyleDescription class attributes and methods

# TreeItemStyleDescription class attributes and methods

# tree_description_TreeItemTool class attributes and methods

# AbstractToolDescription class attributes and methods

# tool_ModelOperation class attributes and methods

# TreeItemDeletionTool class attributes and methods

# TreeVariable class attributes and methods

# tree_description_TreeItemDragTool class attributes and methods
tree_description_TreeItemDragTool_dragSourceType: Property = Property(name="dragSourceType", type=StringType)
tree_description_TreeItemDragTool_m_getBestTreeItemMapping: Method = Method(name="getBestTreeItemMapping", parameters={}, type=StringType)
tree_description_TreeItemDragTool.attributes={tree_description_TreeItemDragTool_dragSourceType}
tree_description_TreeItemDragTool.methods={tree_description_TreeItemDragTool_m_getBestTreeItemMapping}

# tool_MappingBasedToolDescription class attributes and methods

# description_TreeItemTool class attributes and methods

# tool_DropContainerVariable class attributes and methods

# tool_ElementDropVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# TreeItemMappingContainer class attributes and methods

# PrecedingSiblingsVariables class attributes and methods

# tree_description_TreeItemContainerDropTool class attributes and methods
tree_description_TreeItemContainerDropTool_dragSource: Property = Property(name="dragSource", type=StringType)
tree_description_TreeItemContainerDropTool.attributes={tree_description_TreeItemContainerDropTool_dragSource}

# tree_description_TreeItemCreationTool class attributes and methods

# tree_description_TreeItemEditionTool class attributes and methods

# TreeItemTool class attributes and methods

# tool_EditMaskVariables class attributes and methods

# tree_description_StyleUpdater class attributes and methods

# tree_description_TreeItemDeletionTool class attributes and methods

# tree_description_TreeCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# tree_description_TreeNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# tree_description_TreeMapping class attributes and methods
tree_description_TreeMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
tree_description_TreeMapping.attributes={tree_description_TreeMapping_semanticElements}

# RepresentationElementMapping class attributes and methods

# tree_description_TreePopupMenu class attributes and methods

# tool_MenuItemOrRef class attributes and methods

# ConditionalTreeItemStyleDescription class attributes and methods

# tree_description_TreeVariable class attributes and methods
tree_description_TreeVariable_documentation: Property = Property(name="documentation", type=StringType)
tree_description_TreeVariable.attributes={tree_description_TreeVariable_documentation}

# description_AbstractVariable class attributes and methods

# tool_VariableContainer class attributes and methods

# tree_description_TreeItemUpdater class attributes and methods
tree_description_TreeItemUpdater_m_getLabelComputationExpression: Method = Method(name="getLabelComputationExpression", parameters={}, type=StringType)
tree_description_TreeItemUpdater_m_getCreateTreeItem: Method = Method(name="getCreateTreeItem", parameters={}, type=StringType)
tree_description_TreeItemUpdater.methods={tree_description_TreeItemUpdater_m_getCreateTreeItem, tree_description_TreeItemUpdater_m_getLabelComputationExpression}

# TreeItemEditionTool class attributes and methods

# tree_description_PrecedingSiblingsVariables class attributes and methods

# tree_description_TreeItemMappingContainer class attributes and methods

# TreeItemContainerDropTool class attributes and methods

# Relationships
semanticElements0: BinaryAssociation = BinaryAssociation(
    name="semanticElements0",
    ends={
        Property(name="tree_EObject", type=tree_DTree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTree", type=tree_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
description1: BinaryAssociation = BinaryAssociation(
    name="description1",
    ends={
        Property(name="TreeDescription", type=tree_DTree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTree2", type=TreeDescription, multiplicity=Multiplicity(1, 1))
    }
)
treeElementMapping3: BinaryAssociation = BinaryAssociation(
    name="treeElementMapping3",
    ends={
        Property(name="TreeMapping", type=tree_DTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTreeElement", type=TreeMapping, multiplicity=Multiplicity(0, 1))
    }
)
ownedTreeItems4: BinaryAssociation = BinaryAssociation(
    name="ownedTreeItems4",
    ends={
        Property(name="DTreeItem", type=tree_DTreeItemContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=tree_DTreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStyle5: BinaryAssociation = BinaryAssociation(
    name="ownedStyle5",
    ends={
        Property(name="tree_TreeItemStyle", type=tree_DTreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTreeItem", type=tree_TreeItemStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualMapping6: BinaryAssociation = BinaryAssociation(
    name="actualMapping6",
    ends={
        Property(name="TreeItemMapping", type=tree_DTreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTreeItem7", type=TreeItemMapping, multiplicity=Multiplicity(1, 1))
    }
)
container8: BinaryAssociation = BinaryAssociation(
    name="container8",
    ends={
        Property(name="DTreeItemContainer", type=tree_DTreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTreeItems", type=tree_DTreeItemContainer, multiplicity=Multiplicity(0, 1))
    }
)
styleUpdater9: BinaryAssociation = BinaryAssociation(
    name="styleUpdater9",
    ends={
        Property(name="StyleUpdater", type=tree_DTreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTreeItem10", type=StyleUpdater, multiplicity=Multiplicity(0, 1))
    }
)
updater11: BinaryAssociation = BinaryAssociation(
    name="updater11",
    ends={
        Property(name="TreeItemUpdater", type=tree_DTreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTreeItem12", type=TreeItemUpdater, multiplicity=Multiplicity(0, 1))
    }
)
createTreeItem13: BinaryAssociation = BinaryAssociation(
    name="createTreeItem13",
    ends={
        Property(name="TreeItemCreationTool", type=tree_description_TreeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeDescription", type=TreeItemCreationTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentationCreationDescriptions14: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationCreationDescriptions14",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=tree_description_TreeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeDescription15", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentationNavigationDescriptions16: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationNavigationDescriptions16",
    ends={
        Property(name="tool_RepresentationNavigationDescription", type=tree_description_TreeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeDescription17", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedTreeItemMappings18: BinaryAssociation = BinaryAssociation(
    name="reusedTreeItemMappings18",
    ends={
        Property(name="TreeItemMapping19", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allSubMappings20: BinaryAssociation = BinaryAssociation(
    name="allSubMappings20",
    ends={
        Property(name="TreeItemMapping22", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping21", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
specialize23: BinaryAssociation = BinaryAssociation(
    name="specialize23",
    ends={
        Property(name="TreeItemMapping25", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping24", type=TreeItemMapping, multiplicity=Multiplicity(0, 1))
    }
)
delete26: BinaryAssociation = BinaryAssociation(
    name="delete26",
    ends={
        Property(name="description", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeItemDeletionTool", type=TreeItemDeletionTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables37: BinaryAssociation = BinaryAssociation(
    name="variables37",
    ends={
        Property(name="TreeVariable", type=tree_description_TreeItemTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemTool38", type=TreeVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
create27: BinaryAssociation = BinaryAssociation(
    name="create27",
    ends={
        Property(name="TreeItemCreationTool29", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping28", type=TreeItemCreationTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dndTools30: BinaryAssociation = BinaryAssociation(
    name="dndTools30",
    ends={
        Property(name="TreeItemDragTool", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping31", type=TreeItemDragTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
popupMenus32: BinaryAssociation = BinaryAssociation(
    name="popupMenus32",
    ends={
        Property(name="TreePopupMenu", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping33", type=TreePopupMenu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
backgroundColor34: BinaryAssociation = BinaryAssociation(
    name="backgroundColor34",
    ends={
        Property(name="ColorDescription", type=tree_description_TreeItemStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
style35: BinaryAssociation = BinaryAssociation(
    name="style35",
    ends={
        Property(name="TreeItemStyleDescription", type=tree_description_ConditionalTreeItemStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_ConditionalTreeItemStyleDescription", type=TreeItemStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstModelOperation36: BinaryAssociation = BinaryAssociation(
    name="firstModelOperation36",
    ends={
        Property(name="tool_ModelOperation", type=tree_description_TreeItemTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemTool", type=tool_ModelOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oldContainer39: BinaryAssociation = BinaryAssociation(
    name="oldContainer39",
    ends={
        Property(name="tool_DropContainerVariable", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer40: BinaryAssociation = BinaryAssociation(
    name="newContainer40",
    ends={
        Property(name="tool_DropContainerVariable42", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool41", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element43: BinaryAssociation = BinaryAssociation(
    name="element43",
    ends={
        Property(name="tool_ElementDropVariable", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool44", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer45: BinaryAssociation = BinaryAssociation(
    name="newViewContainer45",
    ends={
        Property(name="tool_ContainerViewVariable", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool46", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containers47: BinaryAssociation = BinaryAssociation(
    name="containers47",
    ends={
        Property(name="TreeItemMappingContainer", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool48", type=TreeItemMappingContainer, multiplicity=Multiplicity(1, 9999))
    }
)
precedingSiblings49: BinaryAssociation = BinaryAssociation(
    name="precedingSiblings49",
    ends={
        Property(name="PrecedingSiblingsVariables", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool50", type=PrecedingSiblingsVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldContainer51: BinaryAssociation = BinaryAssociation(
    name="oldContainer51",
    ends={
        Property(name="tool_DropContainerVariable52", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer53: BinaryAssociation = BinaryAssociation(
    name="newContainer53",
    ends={
        Property(name="tool_DropContainerVariable55", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool54", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element56: BinaryAssociation = BinaryAssociation(
    name="element56",
    ends={
        Property(name="tool_ElementDropVariable58", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool57", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer59: BinaryAssociation = BinaryAssociation(
    name="newViewContainer59",
    ends={
        Property(name="tool_ContainerViewVariable61", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool60", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
precedingSiblings62: BinaryAssociation = BinaryAssociation(
    name="precedingSiblings62",
    ends={
        Property(name="PrecedingSiblingsVariables64", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool63", type=PrecedingSiblingsVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping65: BinaryAssociation = BinaryAssociation(
    name="mapping65",
    ends={
        Property(name="TreeItemMapping66", type=tree_description_TreeItemCreationTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemCreationTool", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
mask67: BinaryAssociation = BinaryAssociation(
    name="mask67",
    ends={
        Property(name="tool_EditMaskVariables", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultStyle84: BinaryAssociation = BinaryAssociation(
    name="defaultStyle84",
    ends={
        Property(name="TreeItemStyleDescription85", type=tree_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_StyleUpdater", type=TreeItemStyleDescription, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping68: BinaryAssociation = BinaryAssociation(
    name="mapping68",
    ends={
        Property(name="TreeItemMapping70", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool69", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element71: BinaryAssociation = BinaryAssociation(
    name="element71",
    ends={
        Property(name="tool_ElementDropVariable73", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool72", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root74: BinaryAssociation = BinaryAssociation(
    name="root74",
    ends={
        Property(name="tool_ElementDropVariable76", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool75", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping77: BinaryAssociation = BinaryAssociation(
    name="mapping77",
    ends={
        Property(name="description79", type=tree_description_TreeItemDeletionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeItemMapping78", type=TreeItemMapping, multiplicity=Multiplicity(1, 1))
    }
)
treeDescription80: BinaryAssociation = BinaryAssociation(
    name="treeDescription80",
    ends={
        Property(name="TreeDescription81", type=tree_description_TreeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeCreationDescription", type=TreeDescription, multiplicity=Multiplicity(1, 1))
    }
)
treeDescription82: BinaryAssociation = BinaryAssociation(
    name="treeDescription82",
    ends={
        Property(name="TreeDescription83", type=tree_description_TreeNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeNavigationDescription", type=TreeDescription, multiplicity=Multiplicity(1, 1))
    }
)
conditionalStyles86: BinaryAssociation = BinaryAssociation(
    name="conditionalStyles86",
    ends={
        Property(name="ConditionalTreeItemStyleDescription", type=tree_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_StyleUpdater87", type=ConditionalTreeItemStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directEdit88: BinaryAssociation = BinaryAssociation(
    name="directEdit88",
    ends={
        Property(name="TreeItemEditionTool", type=tree_description_TreeItemUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemUpdater", type=TreeItemEditionTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subItemMappings89: BinaryAssociation = BinaryAssociation(
    name="subItemMappings89",
    ends={
        Property(name="TreeItemMapping90", type=tree_description_TreeItemMappingContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMappingContainer", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dropTools91: BinaryAssociation = BinaryAssociation(
    name="dropTools91",
    ends={
        Property(name="TreeItemContainerDropTool", type=tree_description_TreeItemMappingContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMappingContainer92", type=TreeItemContainerDropTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menuItemDescriptions93: BinaryAssociation = BinaryAssociation(
    name="menuItemDescriptions93",
    ends={
        Property(name="tool_MenuItemOrRef", type=tree_description_TreePopupMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreePopupMenu", type=tool_MenuItemOrRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tree_DTree_DRepresentation = Generalization(general=DRepresentation, specific=tree_DTree)
gen_tree_DTree_DTreeItemContainer = Generalization(general=DTreeItemContainer, specific=tree_DTree)
gen_tree_DTreeElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=tree_DTreeElement)
gen_tree_DTreeItemContainer_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=tree_DTreeItemContainer)
gen_tree_DTreeItem_DTreeItemContainer = Generalization(general=DTreeItemContainer, specific=tree_DTreeItem)
gen_tree_DTreeItem_DTreeElement = Generalization(general=DTreeElement, specific=tree_DTreeItem)
gen_tree_TreeItemStyle_Style = Generalization(general=Style, specific=tree_TreeItemStyle)
gen_tree_TreeItemStyle_LabelStyle = Generalization(general=LabelStyle, specific=tree_TreeItemStyle)
gen_tree_DTreeElementSynchronizer_IdentifiedElement = Generalization(general=IdentifiedElement, specific=tree_DTreeElementSynchronizer)
gen_tree_description_TreeDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=tree_description_TreeDescription)
gen_tree_description_TreeDescription_description_TreeItemMappingContainer = Generalization(general=description_TreeItemMappingContainer, specific=tree_description_TreeDescription)
gen_tree_description_TreeItemMapping_description_TreeMapping = Generalization(general=description_TreeMapping, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemMapping_description_TreeItemUpdater = Generalization(general=description_TreeItemUpdater, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemMapping_description_TreeItemMappingContainer = Generalization(general=description_TreeItemMappingContainer, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=tree_description_TreeItemStyleDescription)
gen_tree_description_TreeItemStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=tree_description_TreeItemStyleDescription)
gen_tree_description_ConditionalTreeItemStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=tree_description_ConditionalTreeItemStyleDescription)
gen_tree_description_TreeItemTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=tree_description_TreeItemTool)
gen_tree_description_TreeItemContainerDropTool_tool_MappingBasedToolDescription = Generalization(general=tool_MappingBasedToolDescription, specific=tree_description_TreeItemContainerDropTool)
gen_tree_description_TreeItemContainerDropTool_description_TreeItemTool = Generalization(general=description_TreeItemTool, specific=tree_description_TreeItemContainerDropTool)
gen_tree_description_TreeItemDragTool_tool_MappingBasedToolDescription = Generalization(general=tool_MappingBasedToolDescription, specific=tree_description_TreeItemDragTool)
gen_tree_description_TreeItemDragTool_description_TreeItemTool = Generalization(general=description_TreeItemTool, specific=tree_description_TreeItemDragTool)
gen_tree_description_TreeItemCreationTool_description_TreeItemTool = Generalization(general=description_TreeItemTool, specific=tree_description_TreeItemCreationTool)
gen_tree_description_TreeItemCreationTool_tool_MappingBasedToolDescription = Generalization(general=tool_MappingBasedToolDescription, specific=tree_description_TreeItemCreationTool)
gen_tree_description_TreeItemEditionTool_TreeItemTool = Generalization(general=TreeItemTool, specific=tree_description_TreeItemEditionTool)
gen_tree_description_TreeItemDeletionTool_TreeItemTool = Generalization(general=TreeItemTool, specific=tree_description_TreeItemDeletionTool)
gen_tree_description_TreeCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=tree_description_TreeCreationDescription)
gen_tree_description_TreeNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=tree_description_TreeNavigationDescription)
gen_tree_description_TreeMapping_RepresentationElementMapping = Generalization(general=RepresentationElementMapping, specific=tree_description_TreeMapping)
gen_tree_description_TreePopupMenu_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=tree_description_TreePopupMenu)
gen_tree_description_TreeVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=tree_description_TreeVariable)
gen_tree_description_TreeVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=tree_description_TreeVariable)
gen_tree_description_PrecedingSiblingsVariables_TreeVariable = Generalization(general=TreeVariable, specific=tree_description_PrecedingSiblingsVariables)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_DTree, DRepresentation, DTreeItemContainer, tree_EObject, TreeDescription, tree_DTreeElement, DRepresentationElement, TreeMapping, DSemanticDecorator, tree_DTreeItem, DTreeElement, tree_TreeItemStyle, TreeItemMapping, StyleUpdater, TreeItemUpdater, Style, LabelStyle, tree_DTreeElementSynchronizer, IdentifiedElement, tree_DTreeItemContainer, tree_description_TreeDescription, description_RepresentationDescription, description_TreeItemMappingContainer, TreeItemCreationTool, tool_RepresentationCreationDescription, tool_RepresentationNavigationDescription, tree_description_TreeItemMapping, description_TreeMapping, description_StyleUpdater, description_TreeItemUpdater, TreeItemDragTool, TreePopupMenu, tree_description_TreeItemStyleDescription, style_StyleDescription, style_LabelStyleDescription, ColorDescription, tree_description_ConditionalTreeItemStyleDescription, ConditionalStyleDescription, TreeItemStyleDescription, tree_description_TreeItemTool, AbstractToolDescription, tool_ModelOperation, TreeItemDeletionTool, TreeVariable, tree_description_TreeItemDragTool, tool_MappingBasedToolDescription, description_TreeItemTool, tool_DropContainerVariable, tool_ElementDropVariable, tool_ContainerViewVariable, TreeItemMappingContainer, PrecedingSiblingsVariables, tree_description_TreeItemContainerDropTool, tree_description_TreeItemCreationTool, tree_description_TreeItemEditionTool, TreeItemTool, tool_EditMaskVariables, tree_description_StyleUpdater, tree_description_TreeItemDeletionTool, tree_description_TreeCreationDescription, RepresentationCreationDescription, tree_description_TreeNavigationDescription, RepresentationNavigationDescription, tree_description_TreeMapping, RepresentationElementMapping, tree_description_TreePopupMenu, tool_MenuItemOrRef, ConditionalTreeItemStyleDescription, tree_description_TreeVariable, description_AbstractVariable, tool_VariableContainer, tree_description_TreeItemUpdater, TreeItemEditionTool, tree_description_PrecedingSiblingsVariables, tree_description_TreeItemMappingContainer, TreeItemContainerDropTool, TreeDragSource},
    associations={semanticElements0, description1, treeElementMapping3, ownedTreeItems4, ownedStyle5, actualMapping6, container8, styleUpdater9, updater11, createTreeItem13, ownedRepresentationCreationDescriptions14, ownedRepresentationNavigationDescriptions16, reusedTreeItemMappings18, allSubMappings20, specialize23, delete26, variables37, create27, dndTools30, popupMenus32, backgroundColor34, style35, firstModelOperation36, oldContainer39, newContainer40, element43, newViewContainer45, containers47, precedingSiblings49, oldContainer51, newContainer53, element56, newViewContainer59, precedingSiblings62, mapping65, mask67, defaultStyle84, mapping68, element71, root74, mapping77, treeDescription80, treeDescription82, conditionalStyles86, directEdit88, subItemMappings89, dropTools91, menuItemDescriptions93},
    generalizations={gen_tree_DTree_DRepresentation, gen_tree_DTree_DTreeItemContainer, gen_tree_DTreeElement_DRepresentationElement, gen_tree_DTreeItemContainer_DSemanticDecorator, gen_tree_DTreeItem_DTreeItemContainer, gen_tree_DTreeItem_DTreeElement, gen_tree_TreeItemStyle_Style, gen_tree_TreeItemStyle_LabelStyle, gen_tree_DTreeElementSynchronizer_IdentifiedElement, gen_tree_description_TreeDescription_description_RepresentationDescription, gen_tree_description_TreeDescription_description_TreeItemMappingContainer, gen_tree_description_TreeItemMapping_description_TreeMapping, gen_tree_description_TreeItemMapping_description_StyleUpdater, gen_tree_description_TreeItemMapping_description_TreeItemUpdater, gen_tree_description_TreeItemMapping_description_TreeItemMappingContainer, gen_tree_description_TreeItemStyleDescription_style_StyleDescription, gen_tree_description_TreeItemStyleDescription_style_LabelStyleDescription, gen_tree_description_ConditionalTreeItemStyleDescription_ConditionalStyleDescription, gen_tree_description_TreeItemTool_AbstractToolDescription, gen_tree_description_TreeItemContainerDropTool_tool_MappingBasedToolDescription, gen_tree_description_TreeItemContainerDropTool_description_TreeItemTool, gen_tree_description_TreeItemDragTool_tool_MappingBasedToolDescription, gen_tree_description_TreeItemDragTool_description_TreeItemTool, gen_tree_description_TreeItemCreationTool_description_TreeItemTool, gen_tree_description_TreeItemCreationTool_tool_MappingBasedToolDescription, gen_tree_description_TreeItemEditionTool_TreeItemTool, gen_tree_description_TreeItemDeletionTool_TreeItemTool, gen_tree_description_TreeCreationDescription_RepresentationCreationDescription, gen_tree_description_TreeNavigationDescription_RepresentationNavigationDescription, gen_tree_description_TreeMapping_RepresentationElementMapping, gen_tree_description_TreePopupMenu_AbstractToolDescription, gen_tree_description_TreeVariable_description_AbstractVariable, gen_tree_description_TreeVariable_tool_VariableContainer, gen_tree_description_PrecedingSiblingsVariables_TreeVariable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)