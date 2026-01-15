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
TreeDescription = Class(name="TreeDescription")
tree_DTreeElementUpdater = Class(name="tree::DTreeElementUpdater")
tree_DTree = Class(name="tree::DTree")
DRepresentation = Class(name="DRepresentation")
DTreeItemContainer = Class(name="DTreeItemContainer")
DTreeElementUpdater = Class(name="DTreeElementUpdater")
tree_EObject = Class(name="tree::EObject")
StyleUpdater = Class(name="StyleUpdater")
TreeItemUpdater = Class(name="TreeItemUpdater")
tree_DTreeElement = Class(name="tree::DTreeElement")
DRepresentationElement = Class(name="DRepresentationElement")
TreeMapping = Class(name="TreeMapping")
tree_DTreeItemContainer = Class(name="tree::DTreeItemContainer", is_abstract=True)
DSemanticDecorator = Class(name="DSemanticDecorator")
tree_DTreeItem = Class(name="tree::DTreeItem")
DTreeElement = Class(name="DTreeElement")
tree_TreeItemStyle = Class(name="tree::TreeItemStyle")
TreeItemMapping = Class(name="TreeItemMapping")
TreeItemCreationTool = Class(name="TreeItemCreationTool")
Style = Class(name="Style")
LabelStyle = Class(name="LabelStyle")
tree_RGBValues = Class(name="tree::RGBValues")
tree_DTreeElementSynchronizer = Class(name="tree::DTreeElementSynchronizer")
tree_description_TreeDescription = Class(name="tree::description::TreeDescription")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_TreeItemMappingContainer = Class(name="description::TreeItemMappingContainer")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
tool_RepresentationNavigationDescription = Class(name="tool::RepresentationNavigationDescription")
tree_description_TreeItemMapping = Class(name="tree::description::TreeItemMapping")
description_TreeMapping = Class(name="description::TreeMapping")
description_StyleUpdater = Class(name="description::StyleUpdater")
description_TreeItemUpdater = Class(name="description::TreeItemUpdater")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
ColorDescription = Class(name="ColorDescription")
tree_description_ConditionalTreeItemStyleDescription = Class(name="tree::description::ConditionalTreeItemStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
TreeItemDeletionTool = Class(name="TreeItemDeletionTool")
TreeItemDragTool = Class(name="TreeItemDragTool")
TreePopupMenu = Class(name="TreePopupMenu")
tree_description_TreeItemStyleDescription = Class(name="tree::description::TreeItemStyleDescription")
style_StyleDescription = Class(name="style::StyleDescription")
tool_ElementDropVariable = Class(name="tool::ElementDropVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
TreeItemStyleDescription = Class(name="TreeItemStyleDescription")
tree_description_TreeItemTool = Class(name="tree::description::TreeItemTool", is_abstract=True)
AbstractToolDescription = Class(name="AbstractToolDescription")
tool_ModelOperation = Class(name="tool::ModelOperation")
TreeVariable = Class(name="TreeVariable")
tree_description_TreeItemDragTool = Class(name="tree::description::TreeItemDragTool")
tool_MappingBasedToolDescription = Class(name="tool::MappingBasedToolDescription")
description_TreeItemTool = Class(name="description::TreeItemTool")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
tree_description_TreeItemCreationTool = Class(name="tree::description::TreeItemCreationTool")
TreeItemMappingContainer = Class(name="TreeItemMappingContainer")
PrecedingSiblingsVariables = Class(name="PrecedingSiblingsVariables")
tree_description_TreeItemContainerDropTool = Class(name="tree::description::TreeItemContainerDropTool")
tree_description_TreeCreationDescription = Class(name="tree::description::TreeCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
tree_description_TreeNavigationDescription = Class(name="tree::description::TreeNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
tree_description_TreeItemEditionTool = Class(name="tree::description::TreeItemEditionTool")
TreeItemTool = Class(name="TreeItemTool")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
tree_description_TreeItemDeletionTool = Class(name="tree::description::TreeItemDeletionTool")
TreeItemEditionTool = Class(name="TreeItemEditionTool")
tree_description_PrecedingSiblingsVariables = Class(name="tree::description::PrecedingSiblingsVariables")
tree_description_TreeMapping = Class(name="tree::description::TreeMapping")
RepresentationElementMapping = Class(name="RepresentationElementMapping")
tree_description_StyleUpdater = Class(name="tree::description::StyleUpdater")
ConditionalTreeItemStyleDescription = Class(name="ConditionalTreeItemStyleDescription")
tree_description_TreeVariable = Class(name="tree::description::TreeVariable")
tool_AbstractVariable = Class(name="tool::AbstractVariable")
tool_VariableContainer = Class(name="tool::VariableContainer")
tree_description_TreeItemUpdater = Class(name="tree::description::TreeItemUpdater")
tree_description_TreeItemMappingContainer = Class(name="tree::description::TreeItemMappingContainer", is_abstract=True)
TreeItemContainerDropTool = Class(name="TreeItemContainerDropTool")
tree_description_TreePopupMenu = Class(name="tree::description::TreePopupMenu")
tool_MenuItemOrRef = Class(name="tool::MenuItemOrRef")

# TreeDescription class attributes and methods

# tree_DTreeElementUpdater class attributes and methods
tree_DTreeElementUpdater_m_activate: Method = Method(name="activate", parameters={Parameter(name='sync')})
tree_DTreeElementUpdater_m_deactivate: Method = Method(name="deactivate", parameters={})
tree_DTreeElementUpdater.methods={tree_DTreeElementUpdater_m_activate, tree_DTreeElementUpdater_m_deactivate}

# tree_DTree class attributes and methods

# DRepresentation class attributes and methods

# DTreeItemContainer class attributes and methods

# DTreeElementUpdater class attributes and methods

# tree_EObject class attributes and methods

# StyleUpdater class attributes and methods

# TreeItemUpdater class attributes and methods

# tree_DTreeElement class attributes and methods

# DRepresentationElement class attributes and methods

# TreeMapping class attributes and methods

# tree_DTreeItemContainer class attributes and methods

# DSemanticDecorator class attributes and methods

# tree_DTreeItem class attributes and methods
tree_DTreeItem_expanded: Property = Property(name="expanded", type=BooleanType)
tree_DTreeItem.attributes={tree_DTreeItem_expanded}

# DTreeElement class attributes and methods

# tree_TreeItemStyle class attributes and methods

# TreeItemMapping class attributes and methods

# TreeItemCreationTool class attributes and methods

# Style class attributes and methods

# LabelStyle class attributes and methods

# tree_RGBValues class attributes and methods

# tree_DTreeElementSynchronizer class attributes and methods
tree_DTreeElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='DTreeItem')})
tree_DTreeElementSynchronizer.methods={tree_DTreeElementSynchronizer_m_refresh}

# tree_description_TreeDescription class attributes and methods
tree_description_TreeDescription_domainClass: Property = Property(name="domainClass", type=StringType)
tree_description_TreeDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
tree_description_TreeDescription.attributes={tree_description_TreeDescription_preconditionExpression, tree_description_TreeDescription_domainClass}

# description_RepresentationDescription class attributes and methods

# description_TreeItemMappingContainer class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# tree_description_TreeItemMapping class attributes and methods
tree_description_TreeItemMapping_domainClass: Property = Property(name="domainClass", type=StringType)
tree_description_TreeItemMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
tree_description_TreeItemMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
tree_description_TreeItemMapping.attributes={tree_description_TreeItemMapping_preconditionExpression, tree_description_TreeItemMapping_domainClass, tree_description_TreeItemMapping_semanticCandidatesExpression}

# description_TreeMapping class attributes and methods

# description_StyleUpdater class attributes and methods

# description_TreeItemUpdater class attributes and methods

# style_LabelStyleDescription class attributes and methods

# ColorDescription class attributes and methods

# tree_description_ConditionalTreeItemStyleDescription class attributes and methods

# ConditionalStyleDescription class attributes and methods

# TreeItemDeletionTool class attributes and methods

# TreeItemDragTool class attributes and methods

# TreePopupMenu class attributes and methods

# tree_description_TreeItemStyleDescription class attributes and methods

# style_StyleDescription class attributes and methods

# tool_ElementDropVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# TreeItemStyleDescription class attributes and methods

# tree_description_TreeItemTool class attributes and methods

# AbstractToolDescription class attributes and methods

# tool_ModelOperation class attributes and methods

# TreeVariable class attributes and methods

# tree_description_TreeItemDragTool class attributes and methods
tree_description_TreeItemDragTool_dragSourceType: Property = Property(name="dragSourceType", type=StringType)
tree_description_TreeItemDragTool_m_getBestTreeItemMapping: Method = Method(name="getBestTreeItemMapping", parameters={}, type=StringType)
tree_description_TreeItemDragTool.attributes={tree_description_TreeItemDragTool_dragSourceType}
tree_description_TreeItemDragTool.methods={tree_description_TreeItemDragTool_m_getBestTreeItemMapping}

# tool_MappingBasedToolDescription class attributes and methods

# description_TreeItemTool class attributes and methods

# tool_DropContainerVariable class attributes and methods

# tree_description_TreeItemCreationTool class attributes and methods

# TreeItemMappingContainer class attributes and methods

# PrecedingSiblingsVariables class attributes and methods

# tree_description_TreeItemContainerDropTool class attributes and methods
tree_description_TreeItemContainerDropTool_dragSource: Property = Property(name="dragSource", type=StringType)
tree_description_TreeItemContainerDropTool.attributes={tree_description_TreeItemContainerDropTool_dragSource}

# tree_description_TreeCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# tree_description_TreeNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# tree_description_TreeItemEditionTool class attributes and methods

# TreeItemTool class attributes and methods

# tool_EditMaskVariables class attributes and methods

# tree_description_TreeItemDeletionTool class attributes and methods

# TreeItemEditionTool class attributes and methods

# tree_description_PrecedingSiblingsVariables class attributes and methods

# tree_description_TreeMapping class attributes and methods
tree_description_TreeMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
tree_description_TreeMapping.attributes={tree_description_TreeMapping_semanticElements}

# RepresentationElementMapping class attributes and methods

# tree_description_StyleUpdater class attributes and methods

# ConditionalTreeItemStyleDescription class attributes and methods

# tree_description_TreeVariable class attributes and methods
tree_description_TreeVariable_documentation: Property = Property(name="documentation", type=StringType)
tree_description_TreeVariable.attributes={tree_description_TreeVariable_documentation}

# tool_AbstractVariable class attributes and methods

# tool_VariableContainer class attributes and methods

# tree_description_TreeItemUpdater class attributes and methods
tree_description_TreeItemUpdater_m_getLabelComputationExpression: Method = Method(name="getLabelComputationExpression", parameters={}, type=StringType)
tree_description_TreeItemUpdater_m_getCreateTreeItem: Method = Method(name="getCreateTreeItem", parameters={}, type=StringType)
tree_description_TreeItemUpdater.methods={tree_description_TreeItemUpdater_m_getCreateTreeItem, tree_description_TreeItemUpdater_m_getLabelComputationExpression}

# tree_description_TreeItemMappingContainer class attributes and methods

# TreeItemContainerDropTool class attributes and methods

# tree_description_TreePopupMenu class attributes and methods

# tool_MenuItemOrRef class attributes and methods

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
createTreeItem15: BinaryAssociation = BinaryAssociation(
    name="createTreeItem15",
    ends={
        Property(name="TreeItemCreationTool", type=tree_description_TreeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeDescription", type=TreeItemCreationTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updater11: BinaryAssociation = BinaryAssociation(
    name="updater11",
    ends={
        Property(name="TreeItemUpdater", type=tree_DTreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_DTreeItem12", type=TreeItemUpdater, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor13: BinaryAssociation = BinaryAssociation(
    name="backgroundColor13",
    ends={
        Property(name="tree_RGBValues", type=tree_TreeItemStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_TreeItemStyle14", type=tree_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedTreeItemMappings20: BinaryAssociation = BinaryAssociation(
    name="reusedTreeItemMappings20",
    ends={
        Property(name="TreeItemMapping21", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRepresentationCreationDescriptions16: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationCreationDescriptions16",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=tree_description_TreeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeDescription17", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentationNavigationDescriptions18: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationNavigationDescriptions18",
    ends={
        Property(name="tool_RepresentationNavigationDescription", type=tree_description_TreeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeDescription19", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
backgroundColor36: BinaryAssociation = BinaryAssociation(
    name="backgroundColor36",
    ends={
        Property(name="ColorDescription", type=tree_description_TreeItemStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
allSubMappings22: BinaryAssociation = BinaryAssociation(
    name="allSubMappings22",
    ends={
        Property(name="TreeItemMapping24", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping23", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
specialize25: BinaryAssociation = BinaryAssociation(
    name="specialize25",
    ends={
        Property(name="TreeItemMapping27", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping26", type=TreeItemMapping, multiplicity=Multiplicity(0, 1))
    }
)
delete28: BinaryAssociation = BinaryAssociation(
    name="delete28",
    ends={
        Property(name="description", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeItemDeletionTool", type=TreeItemDeletionTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
create29: BinaryAssociation = BinaryAssociation(
    name="create29",
    ends={
        Property(name="TreeItemCreationTool31", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping30", type=TreeItemCreationTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dndTools32: BinaryAssociation = BinaryAssociation(
    name="dndTools32",
    ends={
        Property(name="TreeItemDragTool", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping33", type=TreeItemDragTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
popupMenus34: BinaryAssociation = BinaryAssociation(
    name="popupMenus34",
    ends={
        Property(name="TreePopupMenu", type=tree_description_TreeItemMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMapping35", type=TreePopupMenu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element45: BinaryAssociation = BinaryAssociation(
    name="element45",
    ends={
        Property(name="tool_ElementDropVariable", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool46", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer47: BinaryAssociation = BinaryAssociation(
    name="newViewContainer47",
    ends={
        Property(name="tool_ContainerViewVariable", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool48", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
style37: BinaryAssociation = BinaryAssociation(
    name="style37",
    ends={
        Property(name="TreeItemStyleDescription", type=tree_description_ConditionalTreeItemStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_ConditionalTreeItemStyleDescription", type=TreeItemStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstModelOperation38: BinaryAssociation = BinaryAssociation(
    name="firstModelOperation38",
    ends={
        Property(name="tool_ModelOperation", type=tree_description_TreeItemTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemTool", type=tool_ModelOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables39: BinaryAssociation = BinaryAssociation(
    name="variables39",
    ends={
        Property(name="TreeVariable", type=tree_description_TreeItemTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemTool40", type=TreeVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oldContainer41: BinaryAssociation = BinaryAssociation(
    name="oldContainer41",
    ends={
        Property(name="tool_DropContainerVariable", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer42: BinaryAssociation = BinaryAssociation(
    name="newContainer42",
    ends={
        Property(name="tool_DropContainerVariable44", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool43", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
precedingSiblings64: BinaryAssociation = BinaryAssociation(
    name="precedingSiblings64",
    ends={
        Property(name="PrecedingSiblingsVariables66", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool65", type=PrecedingSiblingsVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containers49: BinaryAssociation = BinaryAssociation(
    name="containers49",
    ends={
        Property(name="TreeItemMappingContainer", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool50", type=TreeItemMappingContainer, multiplicity=Multiplicity(1, 9999))
    }
)
precedingSiblings51: BinaryAssociation = BinaryAssociation(
    name="precedingSiblings51",
    ends={
        Property(name="PrecedingSiblingsVariables", type=tree_description_TreeItemDragTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemDragTool52", type=PrecedingSiblingsVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldContainer53: BinaryAssociation = BinaryAssociation(
    name="oldContainer53",
    ends={
        Property(name="tool_DropContainerVariable54", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer55: BinaryAssociation = BinaryAssociation(
    name="newContainer55",
    ends={
        Property(name="tool_DropContainerVariable57", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool56", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element58: BinaryAssociation = BinaryAssociation(
    name="element58",
    ends={
        Property(name="tool_ElementDropVariable60", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool59", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer61: BinaryAssociation = BinaryAssociation(
    name="newViewContainer61",
    ends={
        Property(name="tool_ContainerViewVariable63", type=tree_description_TreeItemContainerDropTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemContainerDropTool62", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
treeDescription82: BinaryAssociation = BinaryAssociation(
    name="treeDescription82",
    ends={
        Property(name="TreeDescription83", type=tree_description_TreeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeCreationDescription", type=TreeDescription, multiplicity=Multiplicity(1, 1))
    }
)
treeDescription84: BinaryAssociation = BinaryAssociation(
    name="treeDescription84",
    ends={
        Property(name="TreeDescription85", type=tree_description_TreeNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeNavigationDescription", type=TreeDescription, multiplicity=Multiplicity(1, 1))
    }
)
mapping67: BinaryAssociation = BinaryAssociation(
    name="mapping67",
    ends={
        Property(name="TreeItemMapping68", type=tree_description_TreeItemCreationTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemCreationTool", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
mask69: BinaryAssociation = BinaryAssociation(
    name="mask69",
    ends={
        Property(name="tool_EditMaskVariables", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping70: BinaryAssociation = BinaryAssociation(
    name="mapping70",
    ends={
        Property(name="TreeItemMapping72", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool71", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element73: BinaryAssociation = BinaryAssociation(
    name="element73",
    ends={
        Property(name="tool_ElementDropVariable75", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool74", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root76: BinaryAssociation = BinaryAssociation(
    name="root76",
    ends={
        Property(name="tool_ElementDropVariable78", type=tree_description_TreeItemEditionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemEditionTool77", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping79: BinaryAssociation = BinaryAssociation(
    name="mapping79",
    ends={
        Property(name="description81", type=tree_description_TreeItemDeletionTool, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeItemMapping80", type=TreeItemMapping, multiplicity=Multiplicity(1, 1))
    }
)
directEdit90: BinaryAssociation = BinaryAssociation(
    name="directEdit90",
    ends={
        Property(name="TreeItemEditionTool", type=tree_description_TreeItemUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemUpdater", type=TreeItemEditionTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultStyle86: BinaryAssociation = BinaryAssociation(
    name="defaultStyle86",
    ends={
        Property(name="TreeItemStyleDescription87", type=tree_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_StyleUpdater", type=TreeItemStyleDescription, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalStyles88: BinaryAssociation = BinaryAssociation(
    name="conditionalStyles88",
    ends={
        Property(name="ConditionalTreeItemStyleDescription", type=tree_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_StyleUpdater89", type=ConditionalTreeItemStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subItemMappings91: BinaryAssociation = BinaryAssociation(
    name="subItemMappings91",
    ends={
        Property(name="TreeItemMapping92", type=tree_description_TreeItemMappingContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMappingContainer", type=TreeItemMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dropTools93: BinaryAssociation = BinaryAssociation(
    name="dropTools93",
    ends={
        Property(name="TreeItemContainerDropTool", type=tree_description_TreeItemMappingContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreeItemMappingContainer94", type=TreeItemContainerDropTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menuItemDescriptions95: BinaryAssociation = BinaryAssociation(
    name="menuItemDescriptions95",
    ends={
        Property(name="tool_MenuItemOrRef", type=tree_description_TreePopupMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_description_TreePopupMenu", type=tool_MenuItemOrRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tree_DTree_DRepresentation = Generalization(general=DRepresentation, specific=tree_DTree)
gen_tree_DTree_DTreeItemContainer = Generalization(general=DTreeItemContainer, specific=tree_DTree)
gen_tree_DTree_DTreeElementUpdater = Generalization(general=DTreeElementUpdater, specific=tree_DTree)
gen_tree_DTreeElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=tree_DTreeElement)
gen_tree_DTreeItemContainer_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=tree_DTreeItemContainer)
gen_tree_DTreeItem_DTreeItemContainer = Generalization(general=DTreeItemContainer, specific=tree_DTreeItem)
gen_tree_DTreeItem_DTreeElement = Generalization(general=DTreeElement, specific=tree_DTreeItem)
gen_tree_DTreeItem_DTreeElementUpdater = Generalization(general=DTreeElementUpdater, specific=tree_DTreeItem)
gen_tree_TreeItemStyle_Style = Generalization(general=Style, specific=tree_TreeItemStyle)
gen_tree_TreeItemStyle_LabelStyle = Generalization(general=LabelStyle, specific=tree_TreeItemStyle)
gen_tree_description_TreeDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=tree_description_TreeDescription)
gen_tree_description_TreeDescription_description_TreeItemMappingContainer = Generalization(general=description_TreeItemMappingContainer, specific=tree_description_TreeDescription)
gen_tree_description_TreeItemMapping_description_TreeMapping = Generalization(general=description_TreeMapping, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemMapping_description_TreeItemUpdater = Generalization(general=description_TreeItemUpdater, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemMapping_description_TreeItemMappingContainer = Generalization(general=description_TreeItemMappingContainer, specific=tree_description_TreeItemMapping)
gen_tree_description_TreeItemStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=tree_description_TreeItemStyleDescription)
gen_tree_description_ConditionalTreeItemStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=tree_description_ConditionalTreeItemStyleDescription)
gen_tree_description_TreeItemStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=tree_description_TreeItemStyleDescription)
gen_tree_description_TreeItemTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=tree_description_TreeItemTool)
gen_tree_description_TreeItemDragTool_tool_MappingBasedToolDescription = Generalization(general=tool_MappingBasedToolDescription, specific=tree_description_TreeItemDragTool)
gen_tree_description_TreeItemDragTool_description_TreeItemTool = Generalization(general=description_TreeItemTool, specific=tree_description_TreeItemDragTool)
gen_tree_description_TreeItemCreationTool_description_TreeItemTool = Generalization(general=description_TreeItemTool, specific=tree_description_TreeItemCreationTool)
gen_tree_description_TreeItemCreationTool_tool_MappingBasedToolDescription = Generalization(general=tool_MappingBasedToolDescription, specific=tree_description_TreeItemCreationTool)
gen_tree_description_TreeItemContainerDropTool_tool_MappingBasedToolDescription = Generalization(general=tool_MappingBasedToolDescription, specific=tree_description_TreeItemContainerDropTool)
gen_tree_description_TreeItemContainerDropTool_description_TreeItemTool = Generalization(general=description_TreeItemTool, specific=tree_description_TreeItemContainerDropTool)
gen_tree_description_TreeCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=tree_description_TreeCreationDescription)
gen_tree_description_TreeNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=tree_description_TreeNavigationDescription)
gen_tree_description_TreeItemEditionTool_TreeItemTool = Generalization(general=TreeItemTool, specific=tree_description_TreeItemEditionTool)
gen_tree_description_TreeItemDeletionTool_TreeItemTool = Generalization(general=TreeItemTool, specific=tree_description_TreeItemDeletionTool)
gen_tree_description_PrecedingSiblingsVariables_TreeVariable = Generalization(general=TreeVariable, specific=tree_description_PrecedingSiblingsVariables)
gen_tree_description_TreeMapping_RepresentationElementMapping = Generalization(general=RepresentationElementMapping, specific=tree_description_TreeMapping)
gen_tree_description_TreeVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=tree_description_TreeVariable)
gen_tree_description_TreeVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=tree_description_TreeVariable)
gen_tree_description_TreePopupMenu_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=tree_description_TreePopupMenu)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={TreeDescription, tree_DTreeElementUpdater, tree_DTree, DRepresentation, DTreeItemContainer, DTreeElementUpdater, tree_EObject, StyleUpdater, TreeItemUpdater, tree_DTreeElement, DRepresentationElement, TreeMapping, tree_DTreeItemContainer, DSemanticDecorator, tree_DTreeItem, DTreeElement, tree_TreeItemStyle, TreeItemMapping, TreeItemCreationTool, Style, LabelStyle, tree_RGBValues, tree_DTreeElementSynchronizer, tree_description_TreeDescription, description_RepresentationDescription, description_TreeItemMappingContainer, tool_RepresentationCreationDescription, tool_RepresentationNavigationDescription, tree_description_TreeItemMapping, description_TreeMapping, description_StyleUpdater, description_TreeItemUpdater, style_LabelStyleDescription, ColorDescription, tree_description_ConditionalTreeItemStyleDescription, ConditionalStyleDescription, TreeItemDeletionTool, TreeItemDragTool, TreePopupMenu, tree_description_TreeItemStyleDescription, style_StyleDescription, tool_ElementDropVariable, tool_ContainerViewVariable, TreeItemStyleDescription, tree_description_TreeItemTool, AbstractToolDescription, tool_ModelOperation, TreeVariable, tree_description_TreeItemDragTool, tool_MappingBasedToolDescription, description_TreeItemTool, tool_DropContainerVariable, tree_description_TreeItemCreationTool, TreeItemMappingContainer, PrecedingSiblingsVariables, tree_description_TreeItemContainerDropTool, tree_description_TreeCreationDescription, RepresentationCreationDescription, tree_description_TreeNavigationDescription, RepresentationNavigationDescription, tree_description_TreeItemEditionTool, TreeItemTool, tool_EditMaskVariables, tree_description_TreeItemDeletionTool, TreeItemEditionTool, tree_description_PrecedingSiblingsVariables, tree_description_TreeMapping, RepresentationElementMapping, tree_description_StyleUpdater, ConditionalTreeItemStyleDescription, tree_description_TreeVariable, tool_AbstractVariable, tool_VariableContainer, tree_description_TreeItemUpdater, tree_description_TreeItemMappingContainer, TreeItemContainerDropTool, tree_description_TreePopupMenu, tool_MenuItemOrRef, TreeDragSource},
    associations={semanticElements0, description1, container8, styleUpdater9, treeElementMapping3, ownedTreeItems4, ownedStyle5, actualMapping6, createTreeItem15, updater11, backgroundColor13, reusedTreeItemMappings20, ownedRepresentationCreationDescriptions16, ownedRepresentationNavigationDescriptions18, backgroundColor36, allSubMappings22, specialize25, delete28, create29, dndTools32, popupMenus34, element45, newViewContainer47, style37, firstModelOperation38, variables39, oldContainer41, newContainer42, precedingSiblings64, containers49, precedingSiblings51, oldContainer53, newContainer55, element58, newViewContainer61, treeDescription82, treeDescription84, mapping67, mask69, mapping70, element73, root76, mapping79, directEdit90, defaultStyle86, conditionalStyles88, subItemMappings91, dropTools93, menuItemDescriptions95},
    generalizations={gen_tree_DTree_DRepresentation, gen_tree_DTree_DTreeItemContainer, gen_tree_DTree_DTreeElementUpdater, gen_tree_DTreeElement_DRepresentationElement, gen_tree_DTreeItemContainer_DSemanticDecorator, gen_tree_DTreeItem_DTreeItemContainer, gen_tree_DTreeItem_DTreeElement, gen_tree_DTreeItem_DTreeElementUpdater, gen_tree_TreeItemStyle_Style, gen_tree_TreeItemStyle_LabelStyle, gen_tree_description_TreeDescription_description_RepresentationDescription, gen_tree_description_TreeDescription_description_TreeItemMappingContainer, gen_tree_description_TreeItemMapping_description_TreeMapping, gen_tree_description_TreeItemMapping_description_StyleUpdater, gen_tree_description_TreeItemMapping_description_TreeItemUpdater, gen_tree_description_TreeItemMapping_description_TreeItemMappingContainer, gen_tree_description_TreeItemStyleDescription_style_LabelStyleDescription, gen_tree_description_ConditionalTreeItemStyleDescription_ConditionalStyleDescription, gen_tree_description_TreeItemStyleDescription_style_StyleDescription, gen_tree_description_TreeItemTool_AbstractToolDescription, gen_tree_description_TreeItemDragTool_tool_MappingBasedToolDescription, gen_tree_description_TreeItemDragTool_description_TreeItemTool, gen_tree_description_TreeItemCreationTool_description_TreeItemTool, gen_tree_description_TreeItemCreationTool_tool_MappingBasedToolDescription, gen_tree_description_TreeItemContainerDropTool_tool_MappingBasedToolDescription, gen_tree_description_TreeItemContainerDropTool_description_TreeItemTool, gen_tree_description_TreeCreationDescription_RepresentationCreationDescription, gen_tree_description_TreeNavigationDescription_RepresentationNavigationDescription, gen_tree_description_TreeItemEditionTool_TreeItemTool, gen_tree_description_TreeItemDeletionTool_TreeItemTool, gen_tree_description_PrecedingSiblingsVariables_TreeVariable, gen_tree_description_TreeMapping_RepresentationElementMapping, gen_tree_description_TreeVariable_tool_AbstractVariable, gen_tree_description_TreeVariable_tool_VariableContainer, gen_tree_description_TreePopupMenu_AbstractToolDescription},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)