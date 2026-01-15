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
table_DTableElementStyle = Class(name="table::DTableElementStyle")
table_DTable = Class(name="table::DTable")
DRepresentation = Class(name="DRepresentation")
LineContainer = Class(name="LineContainer")
table_DColumn = Class(name="table::DColumn", is_abstract=True)
TableDescription = Class(name="TableDescription")
table_DTableElement = Class(name="table::DTableElement", is_abstract=True)
DRepresentationElement = Class(name="DRepresentationElement")
TableMapping = Class(name="TableMapping")
table_LineContainer = Class(name="table::LineContainer", is_abstract=True)
DSemanticDecorator = Class(name="DSemanticDecorator")
table_DLine = Class(name="table::DLine")
DTableElement = Class(name="DTableElement")
LineMapping = Class(name="LineMapping")
table_DCell = Class(name="table::DCell")
table_DTargetColumn = Class(name="table::DTargetColumn")
DColumn = Class(name="DColumn")
table_DFeatureColumn = Class(name="table::DFeatureColumn")
table_DCellStyle = Class(name="table::DCellStyle")
CellUpdater = Class(name="CellUpdater")
IntersectionMapping = Class(name="IntersectionMapping")
DTableElementStyle = Class(name="DTableElementStyle")
ColumnMapping = Class(name="ColumnMapping")
tool_RepresentationNavigationDescription = Class(name="tool::RepresentationNavigationDescription")
table_DTableElementSynchronizer = Class(name="table::DTableElementSynchronizer", is_abstract=True)
table_description_TableDescription = Class(name="table::description::TableDescription", is_abstract=True)
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_DocumentedElement = Class(name="description::DocumentedElement")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
table_description_CrossTableDescription = Class(name="table::description::CrossTableDescription")
ElementColumnMapping = Class(name="ElementColumnMapping")
CreateCrossColumnTool = Class(name="CreateCrossColumnTool")
table_description_TableMapping = Class(name="table::description::TableMapping")
RepresentationElementMapping = Class(name="RepresentationElementMapping")
CreateLineTool = Class(name="CreateLineTool")
description_table_EObject = Class(name="description::table::EObject")
table_description_EditionTableDescription = Class(name="table::description::EditionTableDescription")
FeatureColumnMapping = Class(name="FeatureColumnMapping")
table_description_LineMapping = Class(name="table::description::LineMapping")
description_TableMapping = Class(name="description::TableMapping")
description_StyleUpdater = Class(name="description::StyleUpdater")
DeleteLineTool = Class(name="DeleteLineTool")
table_description_ColumnMapping = Class(name="table::description::ColumnMapping")
table_description_ElementColumnMapping = Class(name="table::description::ElementColumnMapping")
description_ColumnMapping = Class(name="description::ColumnMapping")
CreateColumnTool = Class(name="CreateColumnTool")
DeleteColumnTool = Class(name="DeleteColumnTool")
table_description_FeatureColumnMapping = Class(name="table::description::FeatureColumnMapping")
description_CellUpdater = Class(name="description::CellUpdater")
table_description_CellUpdater = Class(name="table::description::CellUpdater")
LabelEditTool = Class(name="LabelEditTool")
table_description_StyleUpdater = Class(name="table::description::StyleUpdater", is_abstract=True)
ForegroundStyleDescription = Class(name="ForegroundStyleDescription")
ForegroundConditionalStyle = Class(name="ForegroundConditionalStyle")
BackgroundStyleDescription = Class(name="BackgroundStyleDescription")
BackgroundConditionalStyle = Class(name="BackgroundConditionalStyle")
table_description_IntersectionMapping = Class(name="table::description::IntersectionMapping")
CreateCellTool = Class(name="CreateCellTool")
table_description_TableTool = Class(name="table::description::TableTool")
TableVariable = Class(name="TableVariable")
tool_ModelOperation = Class(name="tool::ModelOperation")
table_description_LabelEditTool = Class(name="table::description::LabelEditTool")
TableTool = Class(name="TableTool")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
table_description_CreateTool = Class(name="table::description::CreateTool", is_abstract=True)
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
description_TableTool = Class(name="description::TableTool")
table_description_CreateColumnTool = Class(name="table::description::CreateColumnTool")
CreateTool = Class(name="CreateTool")
table_description_CreateCrossColumnTool = Class(name="table::description::CreateCrossColumnTool")
table_description_CreateLineTool = Class(name="table::description::CreateLineTool")
table_description_CreateCellTool = Class(name="table::description::CreateCellTool")
table_description_BackgroundConditionalStyle = Class(name="table::description::BackgroundConditionalStyle")
table_description_TableVariable = Class(name="table::description::TableVariable")
description_AbstractVariable = Class(name="description::AbstractVariable")
tool_VariableContainer = Class(name="tool::VariableContainer")
table_description_TableCreationDescription = Class(name="table::description::TableCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
table_description_DeleteTool = Class(name="table::description::DeleteTool", is_abstract=True)
table_description_DeleteColumnTool = Class(name="table::description::DeleteColumnTool")
DeleteTool = Class(name="DeleteTool")
table_description_DeleteLineTool = Class(name="table::description::DeleteLineTool")
table_description_ForegroundStyleDescription = Class(name="table::description::ForegroundStyleDescription")
ColorDescription = Class(name="ColorDescription")
table_description_BackgroundStyleDescription = Class(name="table::description::BackgroundStyleDescription")
table_description_ForegroundConditionalStyle = Class(name="table::description::ForegroundConditionalStyle")
table_description_TableNavigationDescription = Class(name="table::description::TableNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")

# table_DTableElementStyle class attributes and methods
table_DTableElementStyle_labelSize: Property = Property(name="labelSize", type=IntegerType)
table_DTableElementStyle_labelFormat: Property = Property(name="labelFormat", type=StringType)
table_DTableElementStyle_defaultForegroundStyle: Property = Property(name="defaultForegroundStyle", type=BooleanType)
table_DTableElementStyle_defaultBackgroundStyle: Property = Property(name="defaultBackgroundStyle", type=BooleanType)
table_DTableElementStyle_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
table_DTableElementStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
table_DTableElementStyle.attributes={table_DTableElementStyle_labelSize, table_DTableElementStyle_backgroundColor, table_DTableElementStyle_defaultBackgroundStyle, table_DTableElementStyle_labelFormat, table_DTableElementStyle_defaultForegroundStyle, table_DTableElementStyle_foregroundColor}

# table_DTable class attributes and methods
table_DTable_headerColumnWidth: Property = Property(name="headerColumnWidth", type=IntegerType)
table_DTable.attributes={table_DTable_headerColumnWidth}

# DRepresentation class attributes and methods

# LineContainer class attributes and methods

# table_DColumn class attributes and methods
table_DColumn_visible: Property = Property(name="visible", type=BooleanType)
table_DColumn_width: Property = Property(name="width", type=IntegerType)
table_DColumn_label: Property = Property(name="label", type=StringType)
table_DColumn.attributes={table_DColumn_visible, table_DColumn_label, table_DColumn_width}

# TableDescription class attributes and methods

# table_DTableElement class attributes and methods

# DRepresentationElement class attributes and methods

# TableMapping class attributes and methods

# table_LineContainer class attributes and methods

# DSemanticDecorator class attributes and methods

# table_DLine class attributes and methods
table_DLine_label: Property = Property(name="label", type=StringType)
table_DLine_visible: Property = Property(name="visible", type=BooleanType)
table_DLine_collapsed: Property = Property(name="collapsed", type=BooleanType)
table_DLine.attributes={table_DLine_label, table_DLine_visible, table_DLine_collapsed}

# DTableElement class attributes and methods

# LineMapping class attributes and methods

# table_DCell class attributes and methods
table_DCell_label: Property = Property(name="label", type=StringType)
table_DCell.attributes={table_DCell_label}

# table_DTargetColumn class attributes and methods

# DColumn class attributes and methods

# table_DFeatureColumn class attributes and methods
table_DFeatureColumn_featureName: Property = Property(name="featureName", type=StringType)
table_DFeatureColumn.attributes={table_DFeatureColumn_featureName}

# table_DCellStyle class attributes and methods

# CellUpdater class attributes and methods

# IntersectionMapping class attributes and methods

# DTableElementStyle class attributes and methods

# ColumnMapping class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# table_DTableElementSynchronizer class attributes and methods
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='cell')})
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='column')})
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='line')})
table_DTableElementSynchronizer.methods={table_DTableElementSynchronizer_m_refresh, table_DTableElementSynchronizer_m_refresh, table_DTableElementSynchronizer_m_refresh}

# table_description_TableDescription class attributes and methods
table_description_TableDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
table_description_TableDescription_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_TableDescription_initialHeaderColumnWidth: Property = Property(name="initialHeaderColumnWidth", type=IntegerType)
table_description_TableDescription.attributes={table_description_TableDescription_initialHeaderColumnWidth, table_description_TableDescription_domainClass, table_description_TableDescription_preconditionExpression}

# description_RepresentationDescription class attributes and methods

# description_DocumentedElement class attributes and methods

# description_EndUserDocumentedElement class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# table_description_CrossTableDescription class attributes and methods

# ElementColumnMapping class attributes and methods

# CreateCrossColumnTool class attributes and methods

# table_description_TableMapping class attributes and methods
table_description_TableMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
table_description_TableMapping.attributes={table_description_TableMapping_semanticElements}

# RepresentationElementMapping class attributes and methods

# CreateLineTool class attributes and methods

# description_table_EObject class attributes and methods

# table_description_EditionTableDescription class attributes and methods

# FeatureColumnMapping class attributes and methods

# table_description_LineMapping class attributes and methods
table_description_LineMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_LineMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_LineMapping_headerLabelExpression: Property = Property(name="headerLabelExpression", type=StringType)
table_description_LineMapping.attributes={table_description_LineMapping_semanticCandidatesExpression, table_description_LineMapping_headerLabelExpression, table_description_LineMapping_domainClass}

# description_TableMapping class attributes and methods

# description_StyleUpdater class attributes and methods

# DeleteLineTool class attributes and methods

# table_description_ColumnMapping class attributes and methods
table_description_ColumnMapping_headerLabelExpression: Property = Property(name="headerLabelExpression", type=StringType)
table_description_ColumnMapping_initialWidth: Property = Property(name="initialWidth", type=IntegerType)
table_description_ColumnMapping.attributes={table_description_ColumnMapping_headerLabelExpression, table_description_ColumnMapping_initialWidth}

# table_description_ElementColumnMapping class attributes and methods
table_description_ElementColumnMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_ElementColumnMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_ElementColumnMapping.attributes={table_description_ElementColumnMapping_semanticCandidatesExpression, table_description_ElementColumnMapping_domainClass}

# description_ColumnMapping class attributes and methods

# CreateColumnTool class attributes and methods

# DeleteColumnTool class attributes and methods

# table_description_FeatureColumnMapping class attributes and methods
table_description_FeatureColumnMapping_labelExpression: Property = Property(name="labelExpression", type=StringType)
table_description_FeatureColumnMapping_featureParentExpression: Property = Property(name="featureParentExpression", type=StringType)
table_description_FeatureColumnMapping_featureName: Property = Property(name="featureName", type=StringType)
table_description_FeatureColumnMapping.attributes={table_description_FeatureColumnMapping_featureParentExpression, table_description_FeatureColumnMapping_labelExpression, table_description_FeatureColumnMapping_featureName}

# description_CellUpdater class attributes and methods

# table_description_CellUpdater class attributes and methods
table_description_CellUpdater_canEdit: Property = Property(name="canEdit", type=StringType)
table_description_CellUpdater_m_getLabelComputationExpression: Method = Method(name="getLabelComputationExpression", parameters={}, type=StringType)
table_description_CellUpdater_m_getCreateCell: Method = Method(name="getCreateCell", parameters={}, type=StringType)
table_description_CellUpdater.attributes={table_description_CellUpdater_canEdit}
table_description_CellUpdater.methods={table_description_CellUpdater_m_getLabelComputationExpression, table_description_CellUpdater_m_getCreateCell}

# LabelEditTool class attributes and methods

# table_description_StyleUpdater class attributes and methods

# ForegroundStyleDescription class attributes and methods

# ForegroundConditionalStyle class attributes and methods

# BackgroundStyleDescription class attributes and methods

# BackgroundConditionalStyle class attributes and methods

# table_description_IntersectionMapping class attributes and methods
table_description_IntersectionMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_IntersectionMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
table_description_IntersectionMapping_labelExpression: Property = Property(name="labelExpression", type=StringType)
table_description_IntersectionMapping_useDomainClass: Property = Property(name="useDomainClass", type=BooleanType)
table_description_IntersectionMapping_columnFinderExpression: Property = Property(name="columnFinderExpression", type=StringType)
table_description_IntersectionMapping_lineFinderExpression: Property = Property(name="lineFinderExpression", type=StringType)
table_description_IntersectionMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_IntersectionMapping.attributes={table_description_IntersectionMapping_semanticCandidatesExpression, table_description_IntersectionMapping_domainClass, table_description_IntersectionMapping_lineFinderExpression, table_description_IntersectionMapping_preconditionExpression, table_description_IntersectionMapping_useDomainClass, table_description_IntersectionMapping_columnFinderExpression, table_description_IntersectionMapping_labelExpression}

# CreateCellTool class attributes and methods

# table_description_TableTool class attributes and methods

# TableVariable class attributes and methods

# tool_ModelOperation class attributes and methods

# table_description_LabelEditTool class attributes and methods

# TableTool class attributes and methods

# tool_EditMaskVariables class attributes and methods

# table_description_CreateTool class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# description_TableTool class attributes and methods

# table_description_CreateColumnTool class attributes and methods

# CreateTool class attributes and methods

# table_description_CreateCrossColumnTool class attributes and methods

# table_description_CreateLineTool class attributes and methods

# table_description_CreateCellTool class attributes and methods

# table_description_BackgroundConditionalStyle class attributes and methods
table_description_BackgroundConditionalStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
table_description_BackgroundConditionalStyle.attributes={table_description_BackgroundConditionalStyle_predicateExpression}

# table_description_TableVariable class attributes and methods
table_description_TableVariable_documentation: Property = Property(name="documentation", type=StringType)
table_description_TableVariable.attributes={table_description_TableVariable_documentation}

# description_AbstractVariable class attributes and methods

# tool_VariableContainer class attributes and methods

# table_description_TableCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# table_description_DeleteTool class attributes and methods

# table_description_DeleteColumnTool class attributes and methods

# DeleteTool class attributes and methods

# table_description_DeleteLineTool class attributes and methods

# table_description_ForegroundStyleDescription class attributes and methods
table_description_ForegroundStyleDescription_labelSize: Property = Property(name="labelSize", type=IntegerType)
table_description_ForegroundStyleDescription_labelFormat: Property = Property(name="labelFormat", type=StringType)
table_description_ForegroundStyleDescription.attributes={table_description_ForegroundStyleDescription_labelFormat, table_description_ForegroundStyleDescription_labelSize}

# ColorDescription class attributes and methods

# table_description_BackgroundStyleDescription class attributes and methods

# table_description_ForegroundConditionalStyle class attributes and methods
table_description_ForegroundConditionalStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
table_description_ForegroundConditionalStyle.attributes={table_description_ForegroundConditionalStyle_predicateExpression}

# table_description_TableNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# Relationships
cells5: BinaryAssociation = BinaryAssociation(
    name="cells5",
    ends={
        Property(name="DCell", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=table_DCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container6: BinaryAssociation = BinaryAssociation(
    name="container6",
    ends={
        Property(name="LineContainer", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="lines", type=table_LineContainer, multiplicity=Multiplicity(0, 1))
    }
)
orderedCells7: BinaryAssociation = BinaryAssociation(
    name="orderedCells7",
    ends={
        Property(name="table_DCell", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DLine8", type=table_DCell, multiplicity=Multiplicity(0, 9999))
    }
)
currentStyle9: BinaryAssociation = BinaryAssociation(
    name="currentStyle9",
    ends={
        Property(name="table_DTableElementStyle", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DLine10", type=table_DTableElementStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="DColumn", type=table_DTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=table_DColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description1: BinaryAssociation = BinaryAssociation(
    name="description1",
    ends={
        Property(name="TableDescription", type=table_DTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DTable", type=TableDescription, multiplicity=Multiplicity(0, 1))
    }
)
tableElementMapping2: BinaryAssociation = BinaryAssociation(
    name="tableElementMapping2",
    ends={
        Property(name="TableMapping", type=table_DTableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DTableElement", type=TableMapping, multiplicity=Multiplicity(0, 1))
    }
)
lines3: BinaryAssociation = BinaryAssociation(
    name="lines3",
    ends={
        Property(name="DLine", type=table_LineContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=table_DLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originMapping4: BinaryAssociation = BinaryAssociation(
    name="originMapping4",
    ends={
        Property(name="LineMapping", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DLine", type=LineMapping, multiplicity=Multiplicity(1, 1))
    }
)
orderedCells32: BinaryAssociation = BinaryAssociation(
    name="orderedCells32",
    ends={
        Property(name="table_DCell34", type=table_DColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DColumn33", type=table_DCell, multiplicity=Multiplicity(0, 9999))
    }
)
currentStyle35: BinaryAssociation = BinaryAssociation(
    name="currentStyle35",
    ends={
        Property(name="table_DTableElementStyle37", type=table_DColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DColumn36", type=table_DTableElementStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line11: BinaryAssociation = BinaryAssociation(
    name="line11",
    ends={
        Property(name="DLine12", type=table_DCell, multiplicity=Multiplicity(1, 1)),
        Property(name="cells", type=table_DLine, multiplicity=Multiplicity(0, 1))
    }
)
column13: BinaryAssociation = BinaryAssociation(
    name="column13",
    ends={
        Property(name="DColumn15", type=table_DCell, multiplicity=Multiplicity(1, 1)),
        Property(name="cells14", type=table_DColumn, multiplicity=Multiplicity(0, 1))
    }
)
currentStyle16: BinaryAssociation = BinaryAssociation(
    name="currentStyle16",
    ends={
        Property(name="table_DCellStyle", type=table_DCell, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DCell17", type=table_DCellStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updater18: BinaryAssociation = BinaryAssociation(
    name="updater18",
    ends={
        Property(name="CellUpdater", type=table_DCell, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DCell19", type=CellUpdater, multiplicity=Multiplicity(0, 1))
    }
)
intersectionMapping20: BinaryAssociation = BinaryAssociation(
    name="intersectionMapping20",
    ends={
        Property(name="IntersectionMapping", type=table_DCell, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DCell21", type=IntersectionMapping, multiplicity=Multiplicity(0, 1))
    }
)
foregroundStyleOrigin22: BinaryAssociation = BinaryAssociation(
    name="foregroundStyleOrigin22",
    ends={
        Property(name="TableMapping24", type=table_DCellStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DCellStyle23", type=TableMapping, multiplicity=Multiplicity(0, 1))
    }
)
backgroundStyleOrigin25: BinaryAssociation = BinaryAssociation(
    name="backgroundStyleOrigin25",
    ends={
        Property(name="TableMapping27", type=table_DCellStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DCellStyle26", type=TableMapping, multiplicity=Multiplicity(0, 1))
    }
)
cells28: BinaryAssociation = BinaryAssociation(
    name="cells28",
    ends={
        Property(name="DCell29", type=table_DColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=table_DCell, multiplicity=Multiplicity(0, 9999))
    }
)
originMapping30: BinaryAssociation = BinaryAssociation(
    name="originMapping30",
    ends={
        Property(name="ColumnMapping", type=table_DColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DColumn", type=ColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
table31: BinaryAssociation = BinaryAssociation(
    name="table31",
    ends={
        Property(name="DTable", type=table_DColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=table_DTable, multiplicity=Multiplicity(0, 1))
    }
)
allRepresentationCreationDescriptions42: BinaryAssociation = BinaryAssociation(
    name="allRepresentationCreationDescriptions42",
    ends={
        Property(name="tool_RepresentationCreationDescription44", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription43", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRepresentationNavigationDescriptions45: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationNavigationDescriptions45",
    ends={
        Property(name="tool_RepresentationNavigationDescription", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription46", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedRepresentationNavigationDescriptions47: BinaryAssociation = BinaryAssociation(
    name="reusedRepresentationNavigationDescriptions47",
    ends={
        Property(name="tool_RepresentationNavigationDescription49", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription48", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRepresentationCreationDescriptions38: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationCreationDescriptions38",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedRepresentationCreationDescriptions39: BinaryAssociation = BinaryAssociation(
    name="reusedRepresentationCreationDescriptions39",
    ends={
        Property(name="tool_RepresentationCreationDescription41", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription40", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedColumnMappings79: BinaryAssociation = BinaryAssociation(
    name="ownedColumnMappings79",
    ends={
        Property(name="ElementColumnMapping", type=table_description_CrossTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CrossTableDescription", type=ElementColumnMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
intersection80: BinaryAssociation = BinaryAssociation(
    name="intersection80",
    ends={
        Property(name="IntersectionMapping82", type=table_description_CrossTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CrossTableDescription81", type=IntersectionMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createColumn83: BinaryAssociation = BinaryAssociation(
    name="createColumn83",
    ends={
        Property(name="CreateCrossColumnTool", type=table_description_CrossTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CrossTableDescription84", type=CreateCrossColumnTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allRepresentationNavigationDescriptions50: BinaryAssociation = BinaryAssociation(
    name="allRepresentationNavigationDescriptions50",
    ends={
        Property(name="tool_RepresentationNavigationDescription52", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription51", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLineMappings53: BinaryAssociation = BinaryAssociation(
    name="ownedLineMappings53",
    ends={
        Property(name="LineMapping55", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription54", type=LineMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reusedLineMappings56: BinaryAssociation = BinaryAssociation(
    name="reusedLineMappings56",
    ends={
        Property(name="LineMapping58", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription57", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allLineMappings59: BinaryAssociation = BinaryAssociation(
    name="allLineMappings59",
    ends={
        Property(name="LineMapping61", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription60", type=LineMapping, multiplicity=Multiplicity(1, 9999))
    }
)
ownedCreateLine62: BinaryAssociation = BinaryAssociation(
    name="ownedCreateLine62",
    ends={
        Property(name="CreateLineTool", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription63", type=CreateLineTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedCreateLine64: BinaryAssociation = BinaryAssociation(
    name="reusedCreateLine64",
    ends={
        Property(name="CreateLineTool66", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription65", type=CreateLineTool, multiplicity=Multiplicity(0, 9999))
    }
)
allCreateLine67: BinaryAssociation = BinaryAssociation(
    name="allCreateLine67",
    ends={
        Property(name="CreateLineTool69", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription68", type=CreateLineTool, multiplicity=Multiplicity(0, 9999))
    }
)
importedElements70: BinaryAssociation = BinaryAssociation(
    name="importedElements70",
    ends={
        Property(name="description_table_EObject", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription71", type=description_table_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedColumnMappings72: BinaryAssociation = BinaryAssociation(
    name="ownedColumnMappings72",
    ends={
        Property(name="FeatureColumnMapping", type=table_description_EditionTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_EditionTableDescription", type=FeatureColumnMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reusedColumnMappings73: BinaryAssociation = BinaryAssociation(
    name="reusedColumnMappings73",
    ends={
        Property(name="FeatureColumnMapping75", type=table_description_EditionTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_EditionTableDescription74", type=FeatureColumnMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allColumnMappings76: BinaryAssociation = BinaryAssociation(
    name="allColumnMappings76",
    ends={
        Property(name="FeatureColumnMapping78", type=table_description_EditionTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_EditionTableDescription77", type=FeatureColumnMapping, multiplicity=Multiplicity(1, 9999))
    }
)
reusedSubLines87: BinaryAssociation = BinaryAssociation(
    name="reusedSubLines87",
    ends={
        Property(name="description", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="LineMapping88", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allSubLines89: BinaryAssociation = BinaryAssociation(
    name="allSubLines89",
    ends={
        Property(name="LineMapping91", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping90", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSubLines85: BinaryAssociation = BinaryAssociation(
    name="ownedSubLines85",
    ends={
        Property(name="LineMapping86", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping", type=LineMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedInMappings92: BinaryAssociation = BinaryAssociation(
    name="reusedInMappings92",
    ends={
        Property(name="description94", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="LineMapping93", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
create95: BinaryAssociation = BinaryAssociation(
    name="create95",
    ends={
        Property(name="CreateLineTool97", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping96", type=CreateLineTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delete98: BinaryAssociation = BinaryAssociation(
    name="delete98",
    ends={
        Property(name="description99", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="DeleteLineTool", type=DeleteLineTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
create100: BinaryAssociation = BinaryAssociation(
    name="create100",
    ends={
        Property(name="description101", type=table_description_ElementColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="CreateColumnTool", type=CreateColumnTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delete102: BinaryAssociation = BinaryAssociation(
    name="delete102",
    ends={
        Property(name="description103", type=table_description_ElementColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="DeleteColumnTool", type=DeleteColumnTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directEdit104: BinaryAssociation = BinaryAssociation(
    name="directEdit104",
    ends={
        Property(name="LabelEditTool", type=table_description_CellUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CellUpdater", type=LabelEditTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultForeground105: BinaryAssociation = BinaryAssociation(
    name="defaultForeground105",
    ends={
        Property(name="ForegroundStyleDescription", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater", type=ForegroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundConditionalStyle106: BinaryAssociation = BinaryAssociation(
    name="foregroundConditionalStyle106",
    ends={
        Property(name="ForegroundConditionalStyle", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater107", type=ForegroundConditionalStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultBackground108: BinaryAssociation = BinaryAssociation(
    name="defaultBackground108",
    ends={
        Property(name="BackgroundStyleDescription", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater109", type=BackgroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundConditionalStyle110: BinaryAssociation = BinaryAssociation(
    name="backgroundConditionalStyle110",
    ends={
        Property(name="BackgroundConditionalStyle", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater111", type=BackgroundConditionalStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineMapping112: BinaryAssociation = BinaryAssociation(
    name="lineMapping112",
    ends={
        Property(name="LineMapping113", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_IntersectionMapping", type=LineMapping, multiplicity=Multiplicity(1, 9999))
    }
)
columnMapping114: BinaryAssociation = BinaryAssociation(
    name="columnMapping114",
    ends={
        Property(name="ColumnMapping116", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_IntersectionMapping115", type=ColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
create117: BinaryAssociation = BinaryAssociation(
    name="create117",
    ends={
        Property(name="description118", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="CreateCellTool", type=CreateCellTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables119: BinaryAssociation = BinaryAssociation(
    name="variables119",
    ends={
        Property(name="TableVariable", type=table_description_TableTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableTool", type=TableVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstModelOperation120: BinaryAssociation = BinaryAssociation(
    name="firstModelOperation120",
    ends={
        Property(name="tool_ModelOperation", type=table_description_TableTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableTool121", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mask122: BinaryAssociation = BinaryAssociation(
    name="mask122",
    ends={
        Property(name="tool_EditMaskVariables", type=table_description_LabelEditTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LabelEditTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping123: BinaryAssociation = BinaryAssociation(
    name="mapping123",
    ends={
        Property(name="description125", type=table_description_CreateColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementColumnMapping124", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping126: BinaryAssociation = BinaryAssociation(
    name="mapping126",
    ends={
        Property(name="ElementColumnMapping127", type=table_description_CreateCrossColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateCrossColumnTool", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping128: BinaryAssociation = BinaryAssociation(
    name="mapping128",
    ends={
        Property(name="LineMapping129", type=table_description_CreateLineTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateLineTool", type=LineMapping, multiplicity=Multiplicity(0, 1))
    }
)
style146: BinaryAssociation = BinaryAssociation(
    name="style146",
    ends={
        Property(name="BackgroundStyleDescription147", type=table_description_BackgroundConditionalStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_BackgroundConditionalStyle", type=BackgroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableDescription148: BinaryAssociation = BinaryAssociation(
    name="tableDescription148",
    ends={
        Property(name="TableDescription149", type=table_description_TableCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableCreationDescription", type=TableDescription, multiplicity=Multiplicity(1, 1))
    }
)
mask130: BinaryAssociation = BinaryAssociation(
    name="mask130",
    ends={
        Property(name="tool_EditMaskVariables131", type=table_description_CreateCellTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateCellTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping132: BinaryAssociation = BinaryAssociation(
    name="mapping132",
    ends={
        Property(name="description134", type=table_description_CreateCellTool, multiplicity=Multiplicity(1, 1)),
        Property(name="IntersectionMapping133", type=IntersectionMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping135: BinaryAssociation = BinaryAssociation(
    name="mapping135",
    ends={
        Property(name="description137", type=table_description_DeleteColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementColumnMapping136", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping138: BinaryAssociation = BinaryAssociation(
    name="mapping138",
    ends={
        Property(name="description140", type=table_description_DeleteLineTool, multiplicity=Multiplicity(1, 1)),
        Property(name="LineMapping139", type=LineMapping, multiplicity=Multiplicity(1, 1))
    }
)
foreGroundColor141: BinaryAssociation = BinaryAssociation(
    name="foreGroundColor141",
    ends={
        Property(name="ColorDescription", type=table_description_ForegroundStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_ForegroundStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor142: BinaryAssociation = BinaryAssociation(
    name="backgroundColor142",
    ends={
        Property(name="ColorDescription143", type=table_description_BackgroundStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_BackgroundStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
style144: BinaryAssociation = BinaryAssociation(
    name="style144",
    ends={
        Property(name="ForegroundStyleDescription145", type=table_description_ForegroundConditionalStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_ForegroundConditionalStyle", type=ForegroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableDescription150: BinaryAssociation = BinaryAssociation(
    name="tableDescription150",
    ends={
        Property(name="TableDescription151", type=table_description_TableNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableNavigationDescription", type=TableDescription, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_table_DTable_DRepresentation = Generalization(general=DRepresentation, specific=table_DTable)
gen_table_DTable_LineContainer = Generalization(general=LineContainer, specific=table_DTable)
gen_table_DTableElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=table_DTableElement)
gen_table_LineContainer_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_LineContainer)
gen_table_DLine_LineContainer = Generalization(general=LineContainer, specific=table_DLine)
gen_table_DLine_DTableElement = Generalization(general=DTableElement, specific=table_DLine)
gen_table_DTargetColumn_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_DTargetColumn)
gen_table_DTargetColumn_DColumn = Generalization(general=DColumn, specific=table_DTargetColumn)
gen_table_DFeatureColumn_DColumn = Generalization(general=DColumn, specific=table_DFeatureColumn)
gen_table_DCell_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_DCell)
gen_table_DCell_DTableElement = Generalization(general=DTableElement, specific=table_DCell)
gen_table_DCellStyle_DTableElementStyle = Generalization(general=DTableElementStyle, specific=table_DCellStyle)
gen_table_DColumn_DTableElement = Generalization(general=DTableElement, specific=table_DColumn)
gen_table_description_TableDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=table_description_TableDescription)
gen_table_description_TableDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=table_description_TableDescription)
gen_table_description_TableDescription_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=table_description_TableDescription)
gen_table_description_CrossTableDescription_TableDescription = Generalization(general=TableDescription, specific=table_description_CrossTableDescription)
gen_table_description_TableMapping_RepresentationElementMapping = Generalization(general=RepresentationElementMapping, specific=table_description_TableMapping)
gen_table_description_EditionTableDescription_TableDescription = Generalization(general=TableDescription, specific=table_description_EditionTableDescription)
gen_table_description_LineMapping_description_TableMapping = Generalization(general=description_TableMapping, specific=table_description_LineMapping)
gen_table_description_LineMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_LineMapping)
gen_table_description_ColumnMapping_TableMapping = Generalization(general=TableMapping, specific=table_description_ColumnMapping)
gen_table_description_ElementColumnMapping_description_ColumnMapping = Generalization(general=description_ColumnMapping, specific=table_description_ElementColumnMapping)
gen_table_description_ElementColumnMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_ElementColumnMapping)
gen_table_description_FeatureColumnMapping_description_ColumnMapping = Generalization(general=description_ColumnMapping, specific=table_description_FeatureColumnMapping)
gen_table_description_FeatureColumnMapping_description_CellUpdater = Generalization(general=description_CellUpdater, specific=table_description_FeatureColumnMapping)
gen_table_description_FeatureColumnMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_FeatureColumnMapping)
gen_table_description_IntersectionMapping_description_TableMapping = Generalization(general=description_TableMapping, specific=table_description_IntersectionMapping)
gen_table_description_IntersectionMapping_description_CellUpdater = Generalization(general=description_CellUpdater, specific=table_description_IntersectionMapping)
gen_table_description_IntersectionMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_IntersectionMapping)
gen_table_description_LabelEditTool_TableTool = Generalization(general=TableTool, specific=table_description_LabelEditTool)
gen_table_description_CreateTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_CreateTool)
gen_table_description_CreateTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_CreateTool)
gen_table_description_CreateColumnTool_CreateTool = Generalization(general=CreateTool, specific=table_description_CreateColumnTool)
gen_table_description_CreateCrossColumnTool_CreateTool = Generalization(general=CreateTool, specific=table_description_CreateCrossColumnTool)
gen_table_description_CreateLineTool_CreateTool = Generalization(general=CreateTool, specific=table_description_CreateLineTool)
gen_table_description_CreateCellTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_CreateCellTool)
gen_table_description_CreateCellTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_CreateCellTool)
gen_table_description_TableVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=table_description_TableVariable)
gen_table_description_TableVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=table_description_TableVariable)
gen_table_description_TableCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=table_description_TableCreationDescription)
gen_table_description_DeleteTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_DeleteTool)
gen_table_description_DeleteTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_DeleteTool)
gen_table_description_DeleteColumnTool_DeleteTool = Generalization(general=DeleteTool, specific=table_description_DeleteColumnTool)
gen_table_description_DeleteLineTool_DeleteTool = Generalization(general=DeleteTool, specific=table_description_DeleteLineTool)
gen_table_description_TableNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=table_description_TableNavigationDescription)

# Domain Model
domain_model = DomainModel(
    name="table",
    types={table_DTableElementStyle, table_DTable, DRepresentation, LineContainer, table_DColumn, TableDescription, table_DTableElement, DRepresentationElement, TableMapping, table_LineContainer, DSemanticDecorator, table_DLine, DTableElement, LineMapping, table_DCell, table_DTargetColumn, DColumn, table_DFeatureColumn, table_DCellStyle, CellUpdater, IntersectionMapping, DTableElementStyle, ColumnMapping, tool_RepresentationNavigationDescription, table_DTableElementSynchronizer, table_description_TableDescription, description_RepresentationDescription, description_DocumentedElement, description_EndUserDocumentedElement, tool_RepresentationCreationDescription, table_description_CrossTableDescription, ElementColumnMapping, CreateCrossColumnTool, table_description_TableMapping, RepresentationElementMapping, CreateLineTool, description_table_EObject, table_description_EditionTableDescription, FeatureColumnMapping, table_description_LineMapping, description_TableMapping, description_StyleUpdater, DeleteLineTool, table_description_ColumnMapping, table_description_ElementColumnMapping, description_ColumnMapping, CreateColumnTool, DeleteColumnTool, table_description_FeatureColumnMapping, description_CellUpdater, table_description_CellUpdater, LabelEditTool, table_description_StyleUpdater, ForegroundStyleDescription, ForegroundConditionalStyle, BackgroundStyleDescription, BackgroundConditionalStyle, table_description_IntersectionMapping, CreateCellTool, table_description_TableTool, TableVariable, tool_ModelOperation, table_description_LabelEditTool, TableTool, tool_EditMaskVariables, table_description_CreateTool, tool_AbstractToolDescription, description_TableTool, table_description_CreateColumnTool, CreateTool, table_description_CreateCrossColumnTool, table_description_CreateLineTool, table_description_CreateCellTool, table_description_BackgroundConditionalStyle, table_description_TableVariable, description_AbstractVariable, tool_VariableContainer, table_description_TableCreationDescription, RepresentationCreationDescription, table_description_DeleteTool, table_description_DeleteColumnTool, DeleteTool, table_description_DeleteLineTool, table_description_ForegroundStyleDescription, ColorDescription, table_description_BackgroundStyleDescription, table_description_ForegroundConditionalStyle, table_description_TableNavigationDescription, RepresentationNavigationDescription},
    associations={cells5, container6, orderedCells7, currentStyle9, columns0, description1, tableElementMapping2, lines3, originMapping4, orderedCells32, currentStyle35, line11, column13, currentStyle16, updater18, intersectionMapping20, foregroundStyleOrigin22, backgroundStyleOrigin25, cells28, originMapping30, table31, allRepresentationCreationDescriptions42, ownedRepresentationNavigationDescriptions45, reusedRepresentationNavigationDescriptions47, ownedRepresentationCreationDescriptions38, reusedRepresentationCreationDescriptions39, ownedColumnMappings79, intersection80, createColumn83, allRepresentationNavigationDescriptions50, ownedLineMappings53, reusedLineMappings56, allLineMappings59, ownedCreateLine62, reusedCreateLine64, allCreateLine67, importedElements70, ownedColumnMappings72, reusedColumnMappings73, allColumnMappings76, reusedSubLines87, allSubLines89, ownedSubLines85, reusedInMappings92, create95, delete98, create100, delete102, directEdit104, defaultForeground105, foregroundConditionalStyle106, defaultBackground108, backgroundConditionalStyle110, lineMapping112, columnMapping114, create117, variables119, firstModelOperation120, mask122, mapping123, mapping126, mapping128, style146, tableDescription148, mask130, mapping132, mapping135, mapping138, foreGroundColor141, backgroundColor142, style144, tableDescription150},
    generalizations={gen_table_DTable_DRepresentation, gen_table_DTable_LineContainer, gen_table_DTableElement_DRepresentationElement, gen_table_LineContainer_DSemanticDecorator, gen_table_DLine_LineContainer, gen_table_DLine_DTableElement, gen_table_DTargetColumn_DSemanticDecorator, gen_table_DTargetColumn_DColumn, gen_table_DFeatureColumn_DColumn, gen_table_DCell_DSemanticDecorator, gen_table_DCell_DTableElement, gen_table_DCellStyle_DTableElementStyle, gen_table_DColumn_DTableElement, gen_table_description_TableDescription_description_RepresentationDescription, gen_table_description_TableDescription_description_DocumentedElement, gen_table_description_TableDescription_description_EndUserDocumentedElement, gen_table_description_CrossTableDescription_TableDescription, gen_table_description_TableMapping_RepresentationElementMapping, gen_table_description_EditionTableDescription_TableDescription, gen_table_description_LineMapping_description_TableMapping, gen_table_description_LineMapping_description_StyleUpdater, gen_table_description_ColumnMapping_TableMapping, gen_table_description_ElementColumnMapping_description_ColumnMapping, gen_table_description_ElementColumnMapping_description_StyleUpdater, gen_table_description_FeatureColumnMapping_description_ColumnMapping, gen_table_description_FeatureColumnMapping_description_CellUpdater, gen_table_description_FeatureColumnMapping_description_StyleUpdater, gen_table_description_IntersectionMapping_description_TableMapping, gen_table_description_IntersectionMapping_description_CellUpdater, gen_table_description_IntersectionMapping_description_StyleUpdater, gen_table_description_LabelEditTool_TableTool, gen_table_description_CreateTool_tool_AbstractToolDescription, gen_table_description_CreateTool_description_TableTool, gen_table_description_CreateColumnTool_CreateTool, gen_table_description_CreateCrossColumnTool_CreateTool, gen_table_description_CreateLineTool_CreateTool, gen_table_description_CreateCellTool_description_TableTool, gen_table_description_CreateCellTool_tool_AbstractToolDescription, gen_table_description_TableVariable_description_AbstractVariable, gen_table_description_TableVariable_tool_VariableContainer, gen_table_description_TableCreationDescription_RepresentationCreationDescription, gen_table_description_DeleteTool_tool_AbstractToolDescription, gen_table_description_DeleteTool_description_TableTool, gen_table_description_DeleteColumnTool_DeleteTool, gen_table_description_DeleteLineTool_DeleteTool, gen_table_description_TableNavigationDescription_RepresentationNavigationDescription},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)