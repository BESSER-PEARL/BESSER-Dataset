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
table_DTable = Class(name="table::DTable")
DRepresentation = Class(name="DRepresentation")
LineContainer = Class(name="LineContainer")
DTableElementUpdater = Class(name="DTableElementUpdater")
table_DColumn = Class(name="table::DColumn", is_abstract=True)
TableDescription = Class(name="TableDescription")
table_DTableElementUpdater = Class(name="table::DTableElementUpdater", is_abstract=True)
table_DTableElement = Class(name="table::DTableElement", is_abstract=True)
DRepresentationElement = Class(name="DRepresentationElement")
TableMapping = Class(name="TableMapping")
table_LineContainer = Class(name="table::LineContainer", is_abstract=True)
DSemanticDecorator = Class(name="DSemanticDecorator")
table_DLine = Class(name="table::DLine")
table_DCell = Class(name="table::DCell")
table_DTableElementStyle = Class(name="table::DTableElementStyle")
table_DCellStyle = Class(name="table::DCellStyle")
CellUpdater = Class(name="CellUpdater")
IntersectionMapping = Class(name="IntersectionMapping")
DTableElementStyle = Class(name="DTableElementStyle")
DTableElement = Class(name="DTableElement")
LineMapping = Class(name="LineMapping")
ColumnMapping = Class(name="ColumnMapping")
table_DTargetColumn = Class(name="table::DTargetColumn")
DColumn = Class(name="DColumn")
table_DFeatureColumn = Class(name="table::DFeatureColumn")
table_DTableElementSynchronizer = Class(name="table::DTableElementSynchronizer", is_abstract=True)
table_RGBValues = Class(name="table::RGBValues")
description_DocumentedElement = Class(name="description::DocumentedElement")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
tool_RepresentationNavigationDescription = Class(name="tool::RepresentationNavigationDescription")
CreateLineTool = Class(name="CreateLineTool")
table_description_TableDescription = Class(name="table::description::TableDescription", is_abstract=True)
description_RepresentationDescription = Class(name="description::RepresentationDescription")
table_description_EditionTableDescription = Class(name="table::description::EditionTableDescription")
FeatureColumnMapping = Class(name="FeatureColumnMapping")
table_description_CrossTableDescription = Class(name="table::description::CrossTableDescription")
ElementColumnMapping = Class(name="ElementColumnMapping")
CreateCrossColumnTool = Class(name="CreateCrossColumnTool")
table_description_TableMapping = Class(name="table::description::TableMapping")
RepresentationElementMapping = Class(name="RepresentationElementMapping")
table_description_LineMapping = Class(name="table::description::LineMapping")
description_TableMapping = Class(name="description::TableMapping")
description_StyleUpdater = Class(name="description::StyleUpdater")
description_table_EObject = Class(name="description::table::EObject")
table_description_ColumnMapping = Class(name="table::description::ColumnMapping")
table_description_ElementColumnMapping = Class(name="table::description::ElementColumnMapping")
description_ColumnMapping = Class(name="description::ColumnMapping")
CreateColumnTool = Class(name="CreateColumnTool")
DeleteColumnTool = Class(name="DeleteColumnTool")
table_description_FeatureColumnMapping = Class(name="table::description::FeatureColumnMapping")
description_CellUpdater = Class(name="description::CellUpdater")
table_description_CellUpdater = Class(name="table::description::CellUpdater")
DeleteLineTool = Class(name="DeleteLineTool")
table_description_StyleUpdater = Class(name="table::description::StyleUpdater", is_abstract=True)
ForegroundStyleDescription = Class(name="ForegroundStyleDescription")
ForegroundConditionalStyle = Class(name="ForegroundConditionalStyle")
BackgroundStyleDescription = Class(name="BackgroundStyleDescription")
BackgroundConditionalStyle = Class(name="BackgroundConditionalStyle")
table_description_IntersectionMapping = Class(name="table::description::IntersectionMapping")
LabelEditTool = Class(name="LabelEditTool")
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
table_description_DeleteTool = Class(name="table::description::DeleteTool", is_abstract=True)
table_description_DeleteColumnTool = Class(name="table::description::DeleteColumnTool")
DeleteTool = Class(name="DeleteTool")
table_description_DeleteLineTool = Class(name="table::description::DeleteLineTool")
table_description_ForegroundStyleDescription = Class(name="table::description::ForegroundStyleDescription")
ColorDescription = Class(name="ColorDescription")
CreateCellTool = Class(name="CreateCellTool")
table_description_TableTool = Class(name="table::description::TableTool")
TableVariable = Class(name="TableVariable")
tool_ModelOperation = Class(name="tool::ModelOperation")
table_description_LabelEditTool = Class(name="table::description::LabelEditTool")
table_description_BackgroundConditionalStyle = Class(name="table::description::BackgroundConditionalStyle")
table_description_TableVariable = Class(name="table::description::TableVariable")
tool_AbstractVariable = Class(name="tool::AbstractVariable")
tool_VariableContainer = Class(name="tool::VariableContainer")
table_description_TableCreationDescription = Class(name="table::description::TableCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
table_description_TableNavigationDescription = Class(name="table::description::TableNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
table_description_BackgroundStyleDescription = Class(name="table::description::BackgroundStyleDescription")
table_description_ForegroundConditionalStyle = Class(name="table::description::ForegroundConditionalStyle")

# table_DTable class attributes and methods
table_DTable_headerColumnWidth: Property = Property(name="headerColumnWidth", type=IntegerType)
table_DTable.attributes={table_DTable_headerColumnWidth}

# DRepresentation class attributes and methods

# LineContainer class attributes and methods

# DTableElementUpdater class attributes and methods

# table_DColumn class attributes and methods
table_DColumn_visible: Property = Property(name="visible", type=BooleanType)
table_DColumn_width: Property = Property(name="width", type=IntegerType)
table_DColumn_label: Property = Property(name="label", type=StringType)
table_DColumn.attributes={table_DColumn_label, table_DColumn_visible, table_DColumn_width}

# TableDescription class attributes and methods

# table_DTableElementUpdater class attributes and methods
table_DTableElementUpdater_m_activate: Method = Method(name="activate", parameters={Parameter(name='sync')})
table_DTableElementUpdater_m_deactivate: Method = Method(name="deactivate", parameters={})
table_DTableElementUpdater.methods={table_DTableElementUpdater_m_activate, table_DTableElementUpdater_m_deactivate}

# table_DTableElement class attributes and methods

# DRepresentationElement class attributes and methods

# TableMapping class attributes and methods

# table_LineContainer class attributes and methods

# DSemanticDecorator class attributes and methods

# table_DLine class attributes and methods
table_DLine_visible: Property = Property(name="visible", type=BooleanType)
table_DLine_collapsed: Property = Property(name="collapsed", type=BooleanType)
table_DLine_label: Property = Property(name="label", type=StringType)
table_DLine.attributes={table_DLine_label, table_DLine_collapsed, table_DLine_visible}

# table_DCell class attributes and methods
table_DCell_label: Property = Property(name="label", type=StringType)
table_DCell.attributes={table_DCell_label}

# table_DTableElementStyle class attributes and methods
table_DTableElementStyle_labelSize: Property = Property(name="labelSize", type=IntegerType)
table_DTableElementStyle_labelFormat: Property = Property(name="labelFormat", type=StringType)
table_DTableElementStyle_defaultForegroundStyle: Property = Property(name="defaultForegroundStyle", type=BooleanType)
table_DTableElementStyle_defaultBackgroundStyle: Property = Property(name="defaultBackgroundStyle", type=BooleanType)
table_DTableElementStyle.attributes={table_DTableElementStyle_labelFormat, table_DTableElementStyle_defaultBackgroundStyle, table_DTableElementStyle_defaultForegroundStyle, table_DTableElementStyle_labelSize}

# table_DCellStyle class attributes and methods

# CellUpdater class attributes and methods

# IntersectionMapping class attributes and methods

# DTableElementStyle class attributes and methods

# DTableElement class attributes and methods

# LineMapping class attributes and methods

# ColumnMapping class attributes and methods

# table_DTargetColumn class attributes and methods

# DColumn class attributes and methods

# table_DFeatureColumn class attributes and methods
table_DFeatureColumn_featureName: Property = Property(name="featureName", type=StringType)
table_DFeatureColumn.attributes={table_DFeatureColumn_featureName}

# table_DTableElementSynchronizer class attributes and methods
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='cell')})
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='column')})
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='line')})
table_DTableElementSynchronizer.methods={table_DTableElementSynchronizer_m_refresh, table_DTableElementSynchronizer_m_refresh, table_DTableElementSynchronizer_m_refresh}

# table_RGBValues class attributes and methods

# description_DocumentedElement class attributes and methods

# description_EndUserDocumentedElement class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# CreateLineTool class attributes and methods

# table_description_TableDescription class attributes and methods
table_description_TableDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
table_description_TableDescription_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_TableDescription_initialHeaderColumnWidth: Property = Property(name="initialHeaderColumnWidth", type=IntegerType)
table_description_TableDescription.attributes={table_description_TableDescription_preconditionExpression, table_description_TableDescription_domainClass, table_description_TableDescription_initialHeaderColumnWidth}

# description_RepresentationDescription class attributes and methods

# table_description_EditionTableDescription class attributes and methods

# FeatureColumnMapping class attributes and methods

# table_description_CrossTableDescription class attributes and methods

# ElementColumnMapping class attributes and methods

# CreateCrossColumnTool class attributes and methods

# table_description_TableMapping class attributes and methods
table_description_TableMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
table_description_TableMapping.attributes={table_description_TableMapping_semanticElements}

# RepresentationElementMapping class attributes and methods

# table_description_LineMapping class attributes and methods
table_description_LineMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_LineMapping_headerLabelExpression: Property = Property(name="headerLabelExpression", type=StringType)
table_description_LineMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_LineMapping.attributes={table_description_LineMapping_headerLabelExpression, table_description_LineMapping_domainClass, table_description_LineMapping_semanticCandidatesExpression}

# description_TableMapping class attributes and methods

# description_StyleUpdater class attributes and methods

# description_table_EObject class attributes and methods

# table_description_ColumnMapping class attributes and methods
table_description_ColumnMapping_headerLabelExpression: Property = Property(name="headerLabelExpression", type=StringType)
table_description_ColumnMapping_initialWidth: Property = Property(name="initialWidth", type=IntegerType)
table_description_ColumnMapping.attributes={table_description_ColumnMapping_initialWidth, table_description_ColumnMapping_headerLabelExpression}

# table_description_ElementColumnMapping class attributes and methods
table_description_ElementColumnMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_ElementColumnMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_ElementColumnMapping.attributes={table_description_ElementColumnMapping_domainClass, table_description_ElementColumnMapping_semanticCandidatesExpression}

# description_ColumnMapping class attributes and methods

# CreateColumnTool class attributes and methods

# DeleteColumnTool class attributes and methods

# table_description_FeatureColumnMapping class attributes and methods
table_description_FeatureColumnMapping_featureName: Property = Property(name="featureName", type=StringType)
table_description_FeatureColumnMapping_labelExpression: Property = Property(name="labelExpression", type=StringType)
table_description_FeatureColumnMapping_featureParentExpression: Property = Property(name="featureParentExpression", type=StringType)
table_description_FeatureColumnMapping.attributes={table_description_FeatureColumnMapping_labelExpression, table_description_FeatureColumnMapping_featureParentExpression, table_description_FeatureColumnMapping_featureName}

# description_CellUpdater class attributes and methods

# table_description_CellUpdater class attributes and methods
table_description_CellUpdater_canEdit: Property = Property(name="canEdit", type=StringType)
table_description_CellUpdater_m_getLabelComputationExpression: Method = Method(name="getLabelComputationExpression", parameters={}, type=StringType)
table_description_CellUpdater_m_getCreateCell: Method = Method(name="getCreateCell", parameters={}, type=StringType)
table_description_CellUpdater.attributes={table_description_CellUpdater_canEdit}
table_description_CellUpdater.methods={table_description_CellUpdater_m_getLabelComputationExpression, table_description_CellUpdater_m_getCreateCell}

# DeleteLineTool class attributes and methods

# table_description_StyleUpdater class attributes and methods

# ForegroundStyleDescription class attributes and methods

# ForegroundConditionalStyle class attributes and methods

# BackgroundStyleDescription class attributes and methods

# BackgroundConditionalStyle class attributes and methods

# table_description_IntersectionMapping class attributes and methods
table_description_IntersectionMapping_labelExpression: Property = Property(name="labelExpression", type=StringType)
table_description_IntersectionMapping_useDomainClass: Property = Property(name="useDomainClass", type=BooleanType)
table_description_IntersectionMapping_columnFinderExpression: Property = Property(name="columnFinderExpression", type=StringType)
table_description_IntersectionMapping_lineFinderExpression: Property = Property(name="lineFinderExpression", type=StringType)
table_description_IntersectionMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_IntersectionMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_IntersectionMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
table_description_IntersectionMapping.attributes={table_description_IntersectionMapping_lineFinderExpression, table_description_IntersectionMapping_labelExpression, table_description_IntersectionMapping_columnFinderExpression, table_description_IntersectionMapping_domainClass, table_description_IntersectionMapping_semanticCandidatesExpression, table_description_IntersectionMapping_preconditionExpression, table_description_IntersectionMapping_useDomainClass}

# LabelEditTool class attributes and methods

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

# table_description_DeleteTool class attributes and methods

# table_description_DeleteColumnTool class attributes and methods

# DeleteTool class attributes and methods

# table_description_DeleteLineTool class attributes and methods

# table_description_ForegroundStyleDescription class attributes and methods
table_description_ForegroundStyleDescription_labelSize: Property = Property(name="labelSize", type=IntegerType)
table_description_ForegroundStyleDescription_labelFormat: Property = Property(name="labelFormat", type=StringType)
table_description_ForegroundStyleDescription.attributes={table_description_ForegroundStyleDescription_labelSize, table_description_ForegroundStyleDescription_labelFormat}

# ColorDescription class attributes and methods

# CreateCellTool class attributes and methods

# table_description_TableTool class attributes and methods

# TableVariable class attributes and methods

# tool_ModelOperation class attributes and methods

# table_description_LabelEditTool class attributes and methods

# table_description_BackgroundConditionalStyle class attributes and methods
table_description_BackgroundConditionalStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
table_description_BackgroundConditionalStyle.attributes={table_description_BackgroundConditionalStyle_predicateExpression}

# table_description_TableVariable class attributes and methods
table_description_TableVariable_documentation: Property = Property(name="documentation", type=StringType)
table_description_TableVariable.attributes={table_description_TableVariable_documentation}

# tool_AbstractVariable class attributes and methods

# tool_VariableContainer class attributes and methods

# table_description_TableCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# table_description_TableNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# table_description_BackgroundStyleDescription class attributes and methods

# table_description_ForegroundConditionalStyle class attributes and methods
table_description_ForegroundConditionalStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
table_description_ForegroundConditionalStyle.attributes={table_description_ForegroundConditionalStyle_predicateExpression}

# Relationships
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
originMapping4: BinaryAssociation = BinaryAssociation(
    name="originMapping4",
    ends={
        Property(name="LineMapping", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DLine", type=LineMapping, multiplicity=Multiplicity(1, 1))
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
foregroundColor38: BinaryAssociation = BinaryAssociation(
    name="foregroundColor38",
    ends={
        Property(name="table_RGBValues", type=table_DTableElementStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DTableElementStyle39", type=table_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor40: BinaryAssociation = BinaryAssociation(
    name="backgroundColor40",
    ends={
        Property(name="table_RGBValues42", type=table_DTableElementStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DTableElementStyle41", type=table_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
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
ownedRepresentationCreationDescriptions43: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationCreationDescriptions43",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedRepresentationCreationDescriptions44: BinaryAssociation = BinaryAssociation(
    name="reusedRepresentationCreationDescriptions44",
    ends={
        Property(name="tool_RepresentationCreationDescription46", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription45", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
allRepresentationCreationDescriptions47: BinaryAssociation = BinaryAssociation(
    name="allRepresentationCreationDescriptions47",
    ends={
        Property(name="tool_RepresentationCreationDescription49", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription48", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRepresentationNavigationDescriptions50: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationNavigationDescriptions50",
    ends={
        Property(name="tool_RepresentationNavigationDescription", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription51", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedRepresentationNavigationDescriptions52: BinaryAssociation = BinaryAssociation(
    name="reusedRepresentationNavigationDescriptions52",
    ends={
        Property(name="tool_RepresentationNavigationDescription54", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription53", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
allRepresentationNavigationDescriptions55: BinaryAssociation = BinaryAssociation(
    name="allRepresentationNavigationDescriptions55",
    ends={
        Property(name="tool_RepresentationNavigationDescription57", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription56", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLineMappings58: BinaryAssociation = BinaryAssociation(
    name="ownedLineMappings58",
    ends={
        Property(name="LineMapping60", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription59", type=LineMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reusedLineMappings61: BinaryAssociation = BinaryAssociation(
    name="reusedLineMappings61",
    ends={
        Property(name="LineMapping63", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription62", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allLineMappings64: BinaryAssociation = BinaryAssociation(
    name="allLineMappings64",
    ends={
        Property(name="LineMapping66", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription65", type=LineMapping, multiplicity=Multiplicity(1, 9999))
    }
)
ownedCreateLine67: BinaryAssociation = BinaryAssociation(
    name="ownedCreateLine67",
    ends={
        Property(name="CreateLineTool", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription68", type=CreateLineTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedCreateLine69: BinaryAssociation = BinaryAssociation(
    name="reusedCreateLine69",
    ends={
        Property(name="CreateLineTool71", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription70", type=CreateLineTool, multiplicity=Multiplicity(0, 9999))
    }
)
ownedColumnMappings77: BinaryAssociation = BinaryAssociation(
    name="ownedColumnMappings77",
    ends={
        Property(name="FeatureColumnMapping", type=table_description_EditionTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_EditionTableDescription", type=FeatureColumnMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reusedColumnMappings78: BinaryAssociation = BinaryAssociation(
    name="reusedColumnMappings78",
    ends={
        Property(name="FeatureColumnMapping80", type=table_description_EditionTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_EditionTableDescription79", type=FeatureColumnMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allColumnMappings81: BinaryAssociation = BinaryAssociation(
    name="allColumnMappings81",
    ends={
        Property(name="FeatureColumnMapping83", type=table_description_EditionTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_EditionTableDescription82", type=FeatureColumnMapping, multiplicity=Multiplicity(1, 9999))
    }
)
ownedColumnMappings84: BinaryAssociation = BinaryAssociation(
    name="ownedColumnMappings84",
    ends={
        Property(name="ElementColumnMapping", type=table_description_CrossTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CrossTableDescription", type=ElementColumnMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
intersection85: BinaryAssociation = BinaryAssociation(
    name="intersection85",
    ends={
        Property(name="IntersectionMapping87", type=table_description_CrossTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CrossTableDescription86", type=IntersectionMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createColumn88: BinaryAssociation = BinaryAssociation(
    name="createColumn88",
    ends={
        Property(name="CreateCrossColumnTool", type=table_description_CrossTableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CrossTableDescription89", type=CreateCrossColumnTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubLines90: BinaryAssociation = BinaryAssociation(
    name="ownedSubLines90",
    ends={
        Property(name="LineMapping91", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping", type=LineMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedSubLines92: BinaryAssociation = BinaryAssociation(
    name="reusedSubLines92",
    ends={
        Property(name="description", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="LineMapping93", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allSubLines94: BinaryAssociation = BinaryAssociation(
    name="allSubLines94",
    ends={
        Property(name="LineMapping96", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping95", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedInMappings97: BinaryAssociation = BinaryAssociation(
    name="reusedInMappings97",
    ends={
        Property(name="description99", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="LineMapping98", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
create100: BinaryAssociation = BinaryAssociation(
    name="create100",
    ends={
        Property(name="CreateLineTool102", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping101", type=CreateLineTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allCreateLine72: BinaryAssociation = BinaryAssociation(
    name="allCreateLine72",
    ends={
        Property(name="CreateLineTool74", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription73", type=CreateLineTool, multiplicity=Multiplicity(0, 9999))
    }
)
importedElements75: BinaryAssociation = BinaryAssociation(
    name="importedElements75",
    ends={
        Property(name="description_table_EObject", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription76", type=description_table_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
create105: BinaryAssociation = BinaryAssociation(
    name="create105",
    ends={
        Property(name="description106", type=table_description_ElementColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="CreateColumnTool", type=CreateColumnTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delete107: BinaryAssociation = BinaryAssociation(
    name="delete107",
    ends={
        Property(name="description108", type=table_description_ElementColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="DeleteColumnTool", type=DeleteColumnTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delete103: BinaryAssociation = BinaryAssociation(
    name="delete103",
    ends={
        Property(name="description104", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="DeleteLineTool", type=DeleteLineTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultForeground110: BinaryAssociation = BinaryAssociation(
    name="defaultForeground110",
    ends={
        Property(name="ForegroundStyleDescription", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater", type=ForegroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundConditionalStyle111: BinaryAssociation = BinaryAssociation(
    name="foregroundConditionalStyle111",
    ends={
        Property(name="ForegroundConditionalStyle", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater112", type=ForegroundConditionalStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultBackground113: BinaryAssociation = BinaryAssociation(
    name="defaultBackground113",
    ends={
        Property(name="BackgroundStyleDescription", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater114", type=BackgroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundConditionalStyle115: BinaryAssociation = BinaryAssociation(
    name="backgroundConditionalStyle115",
    ends={
        Property(name="BackgroundConditionalStyle", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater116", type=BackgroundConditionalStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineMapping117: BinaryAssociation = BinaryAssociation(
    name="lineMapping117",
    ends={
        Property(name="LineMapping118", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_IntersectionMapping", type=LineMapping, multiplicity=Multiplicity(1, 9999))
    }
)
columnMapping119: BinaryAssociation = BinaryAssociation(
    name="columnMapping119",
    ends={
        Property(name="ColumnMapping121", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_IntersectionMapping120", type=ColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
directEdit109: BinaryAssociation = BinaryAssociation(
    name="directEdit109",
    ends={
        Property(name="LabelEditTool", type=table_description_CellUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CellUpdater", type=LabelEditTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mask127: BinaryAssociation = BinaryAssociation(
    name="mask127",
    ends={
        Property(name="tool_EditMaskVariables", type=table_description_LabelEditTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LabelEditTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping128: BinaryAssociation = BinaryAssociation(
    name="mapping128",
    ends={
        Property(name="description130", type=table_description_CreateColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementColumnMapping129", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping131: BinaryAssociation = BinaryAssociation(
    name="mapping131",
    ends={
        Property(name="ElementColumnMapping132", type=table_description_CreateCrossColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateCrossColumnTool", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping133: BinaryAssociation = BinaryAssociation(
    name="mapping133",
    ends={
        Property(name="LineMapping134", type=table_description_CreateLineTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateLineTool", type=LineMapping, multiplicity=Multiplicity(0, 1))
    }
)
mask135: BinaryAssociation = BinaryAssociation(
    name="mask135",
    ends={
        Property(name="tool_EditMaskVariables136", type=table_description_CreateCellTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateCellTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping137: BinaryAssociation = BinaryAssociation(
    name="mapping137",
    ends={
        Property(name="description139", type=table_description_CreateCellTool, multiplicity=Multiplicity(1, 1)),
        Property(name="IntersectionMapping138", type=IntersectionMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping140: BinaryAssociation = BinaryAssociation(
    name="mapping140",
    ends={
        Property(name="description142", type=table_description_DeleteColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementColumnMapping141", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping143: BinaryAssociation = BinaryAssociation(
    name="mapping143",
    ends={
        Property(name="description145", type=table_description_DeleteLineTool, multiplicity=Multiplicity(1, 1)),
        Property(name="LineMapping144", type=LineMapping, multiplicity=Multiplicity(1, 1))
    }
)
foreGroundColor146: BinaryAssociation = BinaryAssociation(
    name="foreGroundColor146",
    ends={
        Property(name="ColorDescription", type=table_description_ForegroundStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_ForegroundStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
create122: BinaryAssociation = BinaryAssociation(
    name="create122",
    ends={
        Property(name="description123", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="CreateCellTool", type=CreateCellTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables124: BinaryAssociation = BinaryAssociation(
    name="variables124",
    ends={
        Property(name="TableVariable", type=table_description_TableTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableTool", type=TableVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstModelOperation125: BinaryAssociation = BinaryAssociation(
    name="firstModelOperation125",
    ends={
        Property(name="tool_ModelOperation", type=table_description_TableTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableTool126", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
style149: BinaryAssociation = BinaryAssociation(
    name="style149",
    ends={
        Property(name="ForegroundStyleDescription150", type=table_description_ForegroundConditionalStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_ForegroundConditionalStyle", type=ForegroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style151: BinaryAssociation = BinaryAssociation(
    name="style151",
    ends={
        Property(name="BackgroundStyleDescription152", type=table_description_BackgroundConditionalStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_BackgroundConditionalStyle", type=BackgroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableDescription153: BinaryAssociation = BinaryAssociation(
    name="tableDescription153",
    ends={
        Property(name="TableDescription154", type=table_description_TableCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableCreationDescription", type=TableDescription, multiplicity=Multiplicity(1, 1))
    }
)
tableDescription155: BinaryAssociation = BinaryAssociation(
    name="tableDescription155",
    ends={
        Property(name="TableDescription156", type=table_description_TableNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableNavigationDescription", type=TableDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor147: BinaryAssociation = BinaryAssociation(
    name="backgroundColor147",
    ends={
        Property(name="ColorDescription148", type=table_description_BackgroundStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_BackgroundStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_table_DTable_DRepresentation = Generalization(general=DRepresentation, specific=table_DTable)
gen_table_DTable_LineContainer = Generalization(general=LineContainer, specific=table_DTable)
gen_table_DTable_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DTable)
gen_table_DTableElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=table_DTableElement)
gen_table_LineContainer_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_LineContainer)
gen_table_DCell_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_DCell)
gen_table_DCell_DTableElement = Generalization(general=DTableElement, specific=table_DCell)
gen_table_DCell_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DCell)
gen_table_DCellStyle_DTableElementStyle = Generalization(general=DTableElementStyle, specific=table_DCellStyle)
gen_table_DLine_LineContainer = Generalization(general=LineContainer, specific=table_DLine)
gen_table_DLine_DTableElement = Generalization(general=DTableElement, specific=table_DLine)
gen_table_DLine_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DLine)
gen_table_DTargetColumn_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_DTargetColumn)
gen_table_DTargetColumn_DColumn = Generalization(general=DColumn, specific=table_DTargetColumn)
gen_table_DTargetColumn_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DTargetColumn)
gen_table_DFeatureColumn_DColumn = Generalization(general=DColumn, specific=table_DFeatureColumn)
gen_table_DColumn_DTableElement = Generalization(general=DTableElement, specific=table_DColumn)
gen_table_description_TableDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=table_description_TableDescription)
gen_table_description_TableDescription_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=table_description_TableDescription)
gen_table_description_TableDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=table_description_TableDescription)
gen_table_description_EditionTableDescription_TableDescription = Generalization(general=TableDescription, specific=table_description_EditionTableDescription)
gen_table_description_CrossTableDescription_TableDescription = Generalization(general=TableDescription, specific=table_description_CrossTableDescription)
gen_table_description_TableMapping_RepresentationElementMapping = Generalization(general=RepresentationElementMapping, specific=table_description_TableMapping)
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
gen_table_description_DeleteTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_DeleteTool)
gen_table_description_DeleteTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_DeleteTool)
gen_table_description_DeleteColumnTool_DeleteTool = Generalization(general=DeleteTool, specific=table_description_DeleteColumnTool)
gen_table_description_DeleteLineTool_DeleteTool = Generalization(general=DeleteTool, specific=table_description_DeleteLineTool)
gen_table_description_TableVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=table_description_TableVariable)
gen_table_description_TableVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=table_description_TableVariable)
gen_table_description_TableCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=table_description_TableCreationDescription)
gen_table_description_TableNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=table_description_TableNavigationDescription)

# Domain Model
domain_model = DomainModel(
    name="table",
    types={table_DTable, DRepresentation, LineContainer, DTableElementUpdater, table_DColumn, TableDescription, table_DTableElementUpdater, table_DTableElement, DRepresentationElement, TableMapping, table_LineContainer, DSemanticDecorator, table_DLine, table_DCell, table_DTableElementStyle, table_DCellStyle, CellUpdater, IntersectionMapping, DTableElementStyle, DTableElement, LineMapping, ColumnMapping, table_DTargetColumn, DColumn, table_DFeatureColumn, table_DTableElementSynchronizer, table_RGBValues, description_DocumentedElement, description_EndUserDocumentedElement, tool_RepresentationCreationDescription, tool_RepresentationNavigationDescription, CreateLineTool, table_description_TableDescription, description_RepresentationDescription, table_description_EditionTableDescription, FeatureColumnMapping, table_description_CrossTableDescription, ElementColumnMapping, CreateCrossColumnTool, table_description_TableMapping, RepresentationElementMapping, table_description_LineMapping, description_TableMapping, description_StyleUpdater, description_table_EObject, table_description_ColumnMapping, table_description_ElementColumnMapping, description_ColumnMapping, CreateColumnTool, DeleteColumnTool, table_description_FeatureColumnMapping, description_CellUpdater, table_description_CellUpdater, DeleteLineTool, table_description_StyleUpdater, ForegroundStyleDescription, ForegroundConditionalStyle, BackgroundStyleDescription, BackgroundConditionalStyle, table_description_IntersectionMapping, LabelEditTool, TableTool, tool_EditMaskVariables, table_description_CreateTool, tool_AbstractToolDescription, description_TableTool, table_description_CreateColumnTool, CreateTool, table_description_CreateCrossColumnTool, table_description_CreateLineTool, table_description_CreateCellTool, table_description_DeleteTool, table_description_DeleteColumnTool, DeleteTool, table_description_DeleteLineTool, table_description_ForegroundStyleDescription, ColorDescription, CreateCellTool, table_description_TableTool, TableVariable, tool_ModelOperation, table_description_LabelEditTool, table_description_BackgroundConditionalStyle, table_description_TableVariable, tool_AbstractVariable, tool_VariableContainer, table_description_TableCreationDescription, RepresentationCreationDescription, table_description_TableNavigationDescription, RepresentationNavigationDescription, table_description_BackgroundStyleDescription, table_description_ForegroundConditionalStyle},
    associations={columns0, description1, tableElementMapping2, lines3, cells5, container6, orderedCells7, currentStyle9, line11, column13, currentStyle16, updater18, intersectionMapping20, foregroundStyleOrigin22, originMapping4, originMapping30, table31, orderedCells32, currentStyle35, foregroundColor38, backgroundColor40, backgroundStyleOrigin25, cells28, ownedRepresentationCreationDescriptions43, reusedRepresentationCreationDescriptions44, allRepresentationCreationDescriptions47, ownedRepresentationNavigationDescriptions50, reusedRepresentationNavigationDescriptions52, allRepresentationNavigationDescriptions55, ownedLineMappings58, reusedLineMappings61, allLineMappings64, ownedCreateLine67, reusedCreateLine69, ownedColumnMappings77, reusedColumnMappings78, allColumnMappings81, ownedColumnMappings84, intersection85, createColumn88, ownedSubLines90, reusedSubLines92, allSubLines94, reusedInMappings97, create100, allCreateLine72, importedElements75, create105, delete107, delete103, defaultForeground110, foregroundConditionalStyle111, defaultBackground113, backgroundConditionalStyle115, lineMapping117, columnMapping119, directEdit109, mask127, mapping128, mapping131, mapping133, mask135, mapping137, mapping140, mapping143, foreGroundColor146, create122, variables124, firstModelOperation125, style149, style151, tableDescription153, tableDescription155, backgroundColor147},
    generalizations={gen_table_DTable_DRepresentation, gen_table_DTable_LineContainer, gen_table_DTable_DTableElementUpdater, gen_table_DTableElement_DRepresentationElement, gen_table_LineContainer_DSemanticDecorator, gen_table_DCell_DSemanticDecorator, gen_table_DCell_DTableElement, gen_table_DCell_DTableElementUpdater, gen_table_DCellStyle_DTableElementStyle, gen_table_DLine_LineContainer, gen_table_DLine_DTableElement, gen_table_DLine_DTableElementUpdater, gen_table_DTargetColumn_DSemanticDecorator, gen_table_DTargetColumn_DColumn, gen_table_DTargetColumn_DTableElementUpdater, gen_table_DFeatureColumn_DColumn, gen_table_DColumn_DTableElement, gen_table_description_TableDescription_description_DocumentedElement, gen_table_description_TableDescription_description_EndUserDocumentedElement, gen_table_description_TableDescription_description_RepresentationDescription, gen_table_description_EditionTableDescription_TableDescription, gen_table_description_CrossTableDescription_TableDescription, gen_table_description_TableMapping_RepresentationElementMapping, gen_table_description_LineMapping_description_TableMapping, gen_table_description_LineMapping_description_StyleUpdater, gen_table_description_ColumnMapping_TableMapping, gen_table_description_ElementColumnMapping_description_ColumnMapping, gen_table_description_ElementColumnMapping_description_StyleUpdater, gen_table_description_FeatureColumnMapping_description_ColumnMapping, gen_table_description_FeatureColumnMapping_description_CellUpdater, gen_table_description_FeatureColumnMapping_description_StyleUpdater, gen_table_description_IntersectionMapping_description_TableMapping, gen_table_description_IntersectionMapping_description_CellUpdater, gen_table_description_IntersectionMapping_description_StyleUpdater, gen_table_description_LabelEditTool_TableTool, gen_table_description_CreateTool_tool_AbstractToolDescription, gen_table_description_CreateTool_description_TableTool, gen_table_description_CreateColumnTool_CreateTool, gen_table_description_CreateCrossColumnTool_CreateTool, gen_table_description_CreateLineTool_CreateTool, gen_table_description_CreateCellTool_description_TableTool, gen_table_description_CreateCellTool_tool_AbstractToolDescription, gen_table_description_DeleteTool_tool_AbstractToolDescription, gen_table_description_DeleteTool_description_TableTool, gen_table_description_DeleteColumnTool_DeleteTool, gen_table_description_DeleteLineTool_DeleteTool, gen_table_description_TableVariable_tool_AbstractVariable, gen_table_description_TableVariable_tool_VariableContainer, gen_table_description_TableCreationDescription_RepresentationCreationDescription, gen_table_description_TableNavigationDescription_RepresentationNavigationDescription},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)