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
table_DTableElement = Class(name="table_DTableElement", is_abstract=True)
DRepresentationElement = Class(name="DRepresentationElement")
TableMapping = Class(name="TableMapping")
table_LineContainer = Class(name="table_LineContainer", is_abstract=True)
DSemanticDecorator = Class(name="DSemanticDecorator")
table_DLine = Class(name="table_DLine")
DTableElement = Class(name="DTableElement")
table_DTable = Class(name="table_DTable")
DRepresentation = Class(name="DRepresentation")
LineContainer = Class(name="LineContainer")
DTableElementUpdater = Class(name="DTableElementUpdater")
table_DColumn = Class(name="table_DColumn", is_abstract=True)
TableDescription = Class(name="TableDescription")
table_DTableElementUpdater = Class(name="table_DTableElementUpdater", is_abstract=True)
LineMapping = Class(name="LineMapping")
table_DCell = Class(name="table_DCell")
table_DTableElementStyle = Class(name="table_DTableElementStyle")
table_DCellStyle = Class(name="table_DCellStyle")
CellUpdater = Class(name="CellUpdater")
IntersectionMapping = Class(name="IntersectionMapping")
DTableElementStyle = Class(name="DTableElementStyle")
ColumnMapping = Class(name="ColumnMapping")
table_DTargetColumn = Class(name="table_DTargetColumn")
DColumn = Class(name="DColumn")
table_DFeatureColumn = Class(name="table_DFeatureColumn")
table_DTableElementSynchronizer = Class(name="table_DTableElementSynchronizer", is_abstract=True)
table_description_TableDescription = Class(name="table_description_TableDescription", is_abstract=True)
description_RepresentationDescription = Class(name="description_RepresentationDescription")
description_DocumentedElement = Class(name="description_DocumentedElement")
table_RGBValues = Class(name="table_RGBValues")
description_EndUserDocumentedElement = Class(name="description_EndUserDocumentedElement")
tool_RepresentationCreationDescription = Class(name="tool_RepresentationCreationDescription")
tool_RepresentationNavigationDescription = Class(name="tool_RepresentationNavigationDescription")
table_description_EditionTableDescription = Class(name="table_description_EditionTableDescription")
FeatureColumnMapping = Class(name="FeatureColumnMapping")
CreateLineTool = Class(name="CreateLineTool")
description_table_EObject = Class(name="description_table_EObject")
table_description_TableMapping = Class(name="table_description_TableMapping")
RepresentationElementMapping = Class(name="RepresentationElementMapping")
table_description_CrossTableDescription = Class(name="table_description_CrossTableDescription")
ElementColumnMapping = Class(name="ElementColumnMapping")
CreateCrossColumnTool = Class(name="CreateCrossColumnTool")
DeleteLineTool = Class(name="DeleteLineTool")
table_description_LineMapping = Class(name="table_description_LineMapping")
description_TableMapping = Class(name="description_TableMapping")
description_StyleUpdater = Class(name="description_StyleUpdater")
table_description_ElementColumnMapping = Class(name="table_description_ElementColumnMapping")
description_ColumnMapping = Class(name="description_ColumnMapping")
table_description_ColumnMapping = Class(name="table_description_ColumnMapping")
table_description_CellUpdater = Class(name="table_description_CellUpdater")
CreateColumnTool = Class(name="CreateColumnTool")
DeleteColumnTool = Class(name="DeleteColumnTool")
table_description_FeatureColumnMapping = Class(name="table_description_FeatureColumnMapping")
description_CellUpdater = Class(name="description_CellUpdater")
BackgroundStyleDescription = Class(name="BackgroundStyleDescription")
BackgroundConditionalStyle = Class(name="BackgroundConditionalStyle")
table_description_IntersectionMapping = Class(name="table_description_IntersectionMapping")
LabelEditTool = Class(name="LabelEditTool")
table_description_StyleUpdater = Class(name="table_description_StyleUpdater", is_abstract=True)
ForegroundStyleDescription = Class(name="ForegroundStyleDescription")
ForegroundConditionalStyle = Class(name="ForegroundConditionalStyle")
table_description_LabelEditTool = Class(name="table_description_LabelEditTool")
TableTool = Class(name="TableTool")
tool_EditMaskVariables = Class(name="tool_EditMaskVariables")
table_description_CreateTool = Class(name="table_description_CreateTool", is_abstract=True)
tool_AbstractToolDescription = Class(name="tool_AbstractToolDescription")
CreateCellTool = Class(name="CreateCellTool")
table_description_TableTool = Class(name="table_description_TableTool")
TableVariable = Class(name="TableVariable")
tool_ModelOperation = Class(name="tool_ModelOperation")
table_description_DeleteTool = Class(name="table_description_DeleteTool", is_abstract=True)
description_TableTool = Class(name="description_TableTool")
table_description_CreateColumnTool = Class(name="table_description_CreateColumnTool")
CreateTool = Class(name="CreateTool")
table_description_CreateCrossColumnTool = Class(name="table_description_CreateCrossColumnTool")
table_description_CreateLineTool = Class(name="table_description_CreateLineTool")
table_description_CreateCellTool = Class(name="table_description_CreateCellTool")
ColorDescription = Class(name="ColorDescription")
table_description_BackgroundStyleDescription = Class(name="table_description_BackgroundStyleDescription")
table_description_ForegroundConditionalStyle = Class(name="table_description_ForegroundConditionalStyle")
table_description_DeleteColumnTool = Class(name="table_description_DeleteColumnTool")
DeleteTool = Class(name="DeleteTool")
table_description_DeleteLineTool = Class(name="table_description_DeleteLineTool")
table_description_ForegroundStyleDescription = Class(name="table_description_ForegroundStyleDescription")
table_description_TableCreationDescription = Class(name="table_description_TableCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
table_description_TableNavigationDescription = Class(name="table_description_TableNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
table_description_BackgroundConditionalStyle = Class(name="table_description_BackgroundConditionalStyle")
table_description_TableVariable = Class(name="table_description_TableVariable")
tool_AbstractVariable = Class(name="tool_AbstractVariable")
tool_VariableContainer = Class(name="tool_VariableContainer")

# table_DTableElement class attributes and methods

# DRepresentationElement class attributes and methods

# TableMapping class attributes and methods

# table_LineContainer class attributes and methods

# DSemanticDecorator class attributes and methods

# table_DLine class attributes and methods
table_DLine_label: Property = Property(name="label", type=StringType)
table_DLine_visible: Property = Property(name="visible", type=BooleanType)
table_DLine_collapsed: Property = Property(name="collapsed", type=BooleanType)
table_DLine.attributes={table_DLine_collapsed, table_DLine_visible, table_DLine_label}

# DTableElement class attributes and methods

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
table_DColumn.attributes={table_DColumn_width, table_DColumn_label, table_DColumn_visible}

# TableDescription class attributes and methods

# table_DTableElementUpdater class attributes and methods
table_DTableElementUpdater_m_activate: Method = Method(name="activate", parameters={Parameter(name='table_sync', type=StringType)})
table_DTableElementUpdater_m_deactivate: Method = Method(name="deactivate", parameters={})
table_DTableElementUpdater.methods={table_DTableElementUpdater_m_deactivate, table_DTableElementUpdater_m_activate}

# LineMapping class attributes and methods

# table_DCell class attributes and methods
table_DCell_label: Property = Property(name="label", type=StringType)
table_DCell.attributes={table_DCell_label}

# table_DTableElementStyle class attributes and methods
table_DTableElementStyle_defaultBackgroundStyle: Property = Property(name="defaultBackgroundStyle", type=BooleanType)
table_DTableElementStyle_labelSize: Property = Property(name="labelSize", type=IntegerType)
table_DTableElementStyle_labelFormat: Property = Property(name="labelFormat", type=StringType)
table_DTableElementStyle_defaultForegroundStyle: Property = Property(name="defaultForegroundStyle", type=BooleanType)
table_DTableElementStyle.attributes={table_DTableElementStyle_defaultBackgroundStyle, table_DTableElementStyle_labelFormat, table_DTableElementStyle_labelSize, table_DTableElementStyle_defaultForegroundStyle}

# table_DCellStyle class attributes and methods

# CellUpdater class attributes and methods

# IntersectionMapping class attributes and methods

# DTableElementStyle class attributes and methods

# ColumnMapping class attributes and methods

# table_DTargetColumn class attributes and methods

# DColumn class attributes and methods

# table_DFeatureColumn class attributes and methods
table_DFeatureColumn_featureName: Property = Property(name="featureName", type=StringType)
table_DFeatureColumn.attributes={table_DFeatureColumn_featureName}

# table_DTableElementSynchronizer class attributes and methods
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='table_cell', type=StringType)})
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='table_column', type=StringType)})
table_DTableElementSynchronizer_m_refresh: Method = Method(name="refresh", parameters={Parameter(name='table_line', type=StringType)})
table_DTableElementSynchronizer.methods={table_DTableElementSynchronizer_m_refresh, table_DTableElementSynchronizer_m_refresh, table_DTableElementSynchronizer_m_refresh}

# table_description_TableDescription class attributes and methods
table_description_TableDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
table_description_TableDescription_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_TableDescription_initialHeaderColumnWidth: Property = Property(name="initialHeaderColumnWidth", type=IntegerType)
table_description_TableDescription.attributes={table_description_TableDescription_domainClass, table_description_TableDescription_preconditionExpression, table_description_TableDescription_initialHeaderColumnWidth}

# description_RepresentationDescription class attributes and methods

# description_DocumentedElement class attributes and methods

# table_RGBValues class attributes and methods

# description_EndUserDocumentedElement class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# table_description_EditionTableDescription class attributes and methods

# FeatureColumnMapping class attributes and methods

# CreateLineTool class attributes and methods

# description_table_EObject class attributes and methods

# table_description_TableMapping class attributes and methods
table_description_TableMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
table_description_TableMapping.attributes={table_description_TableMapping_semanticElements}

# RepresentationElementMapping class attributes and methods

# table_description_CrossTableDescription class attributes and methods

# ElementColumnMapping class attributes and methods

# CreateCrossColumnTool class attributes and methods

# DeleteLineTool class attributes and methods

# table_description_LineMapping class attributes and methods
table_description_LineMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_LineMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_LineMapping_headerLabelExpression: Property = Property(name="headerLabelExpression", type=StringType)
table_description_LineMapping.attributes={table_description_LineMapping_domainClass, table_description_LineMapping_semanticCandidatesExpression, table_description_LineMapping_headerLabelExpression}

# description_TableMapping class attributes and methods

# description_StyleUpdater class attributes and methods

# table_description_ElementColumnMapping class attributes and methods
table_description_ElementColumnMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_ElementColumnMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_ElementColumnMapping.attributes={table_description_ElementColumnMapping_semanticCandidatesExpression, table_description_ElementColumnMapping_domainClass}

# description_ColumnMapping class attributes and methods

# table_description_ColumnMapping class attributes and methods
table_description_ColumnMapping_headerLabelExpression: Property = Property(name="headerLabelExpression", type=StringType)
table_description_ColumnMapping_initialWidth: Property = Property(name="initialWidth", type=IntegerType)
table_description_ColumnMapping.attributes={table_description_ColumnMapping_initialWidth, table_description_ColumnMapping_headerLabelExpression}

# table_description_CellUpdater class attributes and methods
table_description_CellUpdater_canEdit: Property = Property(name="canEdit", type=StringType)
table_description_CellUpdater_m_getLabelComputationExpression: Method = Method(name="getLabelComputationExpression", parameters={}, type=StringType)
table_description_CellUpdater_m_getCreateCell: Method = Method(name="getCreateCell", parameters={}, type=StringType)
table_description_CellUpdater.attributes={table_description_CellUpdater_canEdit}
table_description_CellUpdater.methods={table_description_CellUpdater_m_getCreateCell, table_description_CellUpdater_m_getLabelComputationExpression}

# CreateColumnTool class attributes and methods

# DeleteColumnTool class attributes and methods

# table_description_FeatureColumnMapping class attributes and methods
table_description_FeatureColumnMapping_featureParentExpression: Property = Property(name="featureParentExpression", type=StringType)
table_description_FeatureColumnMapping_featureName: Property = Property(name="featureName", type=StringType)
table_description_FeatureColumnMapping_labelExpression: Property = Property(name="labelExpression", type=StringType)
table_description_FeatureColumnMapping.attributes={table_description_FeatureColumnMapping_featureParentExpression, table_description_FeatureColumnMapping_featureName, table_description_FeatureColumnMapping_labelExpression}

# description_CellUpdater class attributes and methods

# BackgroundStyleDescription class attributes and methods

# BackgroundConditionalStyle class attributes and methods

# table_description_IntersectionMapping class attributes and methods
table_description_IntersectionMapping_lineFinderExpression: Property = Property(name="lineFinderExpression", type=StringType)
table_description_IntersectionMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
table_description_IntersectionMapping_domainClass: Property = Property(name="domainClass", type=StringType)
table_description_IntersectionMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
table_description_IntersectionMapping_labelExpression: Property = Property(name="labelExpression", type=StringType)
table_description_IntersectionMapping_useDomainClass: Property = Property(name="useDomainClass", type=BooleanType)
table_description_IntersectionMapping_columnFinderExpression: Property = Property(name="columnFinderExpression", type=StringType)
table_description_IntersectionMapping.attributes={table_description_IntersectionMapping_preconditionExpression, table_description_IntersectionMapping_domainClass, table_description_IntersectionMapping_lineFinderExpression, table_description_IntersectionMapping_semanticCandidatesExpression, table_description_IntersectionMapping_columnFinderExpression, table_description_IntersectionMapping_labelExpression, table_description_IntersectionMapping_useDomainClass}

# LabelEditTool class attributes and methods

# table_description_StyleUpdater class attributes and methods

# ForegroundStyleDescription class attributes and methods

# ForegroundConditionalStyle class attributes and methods

# table_description_LabelEditTool class attributes and methods

# TableTool class attributes and methods

# tool_EditMaskVariables class attributes and methods

# table_description_CreateTool class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# CreateCellTool class attributes and methods

# table_description_TableTool class attributes and methods

# TableVariable class attributes and methods

# tool_ModelOperation class attributes and methods

# table_description_DeleteTool class attributes and methods

# description_TableTool class attributes and methods

# table_description_CreateColumnTool class attributes and methods

# CreateTool class attributes and methods

# table_description_CreateCrossColumnTool class attributes and methods

# table_description_CreateLineTool class attributes and methods

# table_description_CreateCellTool class attributes and methods

# ColorDescription class attributes and methods

# table_description_BackgroundStyleDescription class attributes and methods

# table_description_ForegroundConditionalStyle class attributes and methods
table_description_ForegroundConditionalStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
table_description_ForegroundConditionalStyle.attributes={table_description_ForegroundConditionalStyle_predicateExpression}

# table_description_DeleteColumnTool class attributes and methods

# DeleteTool class attributes and methods

# table_description_DeleteLineTool class attributes and methods

# table_description_ForegroundStyleDescription class attributes and methods
table_description_ForegroundStyleDescription_labelSize: Property = Property(name="labelSize", type=IntegerType)
table_description_ForegroundStyleDescription_labelFormat: Property = Property(name="labelFormat", type=StringType)
table_description_ForegroundStyleDescription.attributes={table_description_ForegroundStyleDescription_labelFormat, table_description_ForegroundStyleDescription_labelSize}

# table_description_TableCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# table_description_TableNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# table_description_BackgroundConditionalStyle class attributes and methods
table_description_BackgroundConditionalStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
table_description_BackgroundConditionalStyle.attributes={table_description_BackgroundConditionalStyle_predicateExpression}

# table_description_TableVariable class attributes and methods
table_description_TableVariable_documentation: Property = Property(name="documentation", type=StringType)
table_description_TableVariable.attributes={table_description_TableVariable_documentation}

# tool_AbstractVariable class attributes and methods

# tool_VariableContainer class attributes and methods

# Relationships
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
originMapping4: BinaryAssociation = BinaryAssociation(
    name="originMapping4",
    ends={
        Property(name="LineMapping", type=table_DLine, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DLine", type=LineMapping, multiplicity=Multiplicity(1, 1))
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
orderedCells32: BinaryAssociation = BinaryAssociation(
    name="orderedCells32",
    ends={
        Property(name="table_DCell34", type=table_DColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="table_DColumn33", type=table_DCell, multiplicity=Multiplicity(0, 9999))
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
ownedRepresentationCreationDescriptions43: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationCreationDescriptions43",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
importedElements75: BinaryAssociation = BinaryAssociation(
    name="importedElements75",
    ends={
        Property(name="description_table_EObject", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription76", type=description_table_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
allCreateLine72: BinaryAssociation = BinaryAssociation(
    name="allCreateLine72",
    ends={
        Property(name="CreateLineTool74", type=table_description_TableDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableDescription73", type=CreateLineTool, multiplicity=Multiplicity(0, 9999))
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
create99: BinaryAssociation = BinaryAssociation(
    name="create99",
    ends={
        Property(name="CreateLineTool101", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LineMapping100", type=CreateLineTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delete102: BinaryAssociation = BinaryAssociation(
    name="delete102",
    ends={
        Property(name="DeleteLineTool", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mapping", type=DeleteLineTool, multiplicity=Multiplicity(0, 1), is_composite=True)
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
        Property(name="LineMapping93", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="reusedInMappings", type=LineMapping, multiplicity=Multiplicity(0, 9999))
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
        Property(name="LineMapping98", type=table_description_LineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="reusedSubLines", type=LineMapping, multiplicity=Multiplicity(0, 9999))
    }
)
create103: BinaryAssociation = BinaryAssociation(
    name="create103",
    ends={
        Property(name="CreateColumnTool", type=table_description_ElementColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mapping104", type=CreateColumnTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delete105: BinaryAssociation = BinaryAssociation(
    name="delete105",
    ends={
        Property(name="DeleteColumnTool", type=table_description_ElementColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mapping106", type=DeleteColumnTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultBackground111: BinaryAssociation = BinaryAssociation(
    name="defaultBackground111",
    ends={
        Property(name="BackgroundStyleDescription", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater112", type=BackgroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundConditionalStyle113: BinaryAssociation = BinaryAssociation(
    name="backgroundConditionalStyle113",
    ends={
        Property(name="BackgroundConditionalStyle", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater114", type=BackgroundConditionalStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directEdit107: BinaryAssociation = BinaryAssociation(
    name="directEdit107",
    ends={
        Property(name="LabelEditTool", type=table_description_CellUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CellUpdater", type=LabelEditTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultForeground108: BinaryAssociation = BinaryAssociation(
    name="defaultForeground108",
    ends={
        Property(name="ForegroundStyleDescription", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater", type=ForegroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundConditionalStyle109: BinaryAssociation = BinaryAssociation(
    name="foregroundConditionalStyle109",
    ends={
        Property(name="ForegroundConditionalStyle", type=table_description_StyleUpdater, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_StyleUpdater110", type=ForegroundConditionalStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineMapping115: BinaryAssociation = BinaryAssociation(
    name="lineMapping115",
    ends={
        Property(name="LineMapping116", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_IntersectionMapping", type=LineMapping, multiplicity=Multiplicity(1, 9999))
    }
)
columnMapping117: BinaryAssociation = BinaryAssociation(
    name="columnMapping117",
    ends={
        Property(name="ColumnMapping119", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_IntersectionMapping118", type=ColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
firstModelOperation123: BinaryAssociation = BinaryAssociation(
    name="firstModelOperation123",
    ends={
        Property(name="tool_ModelOperation", type=table_description_TableTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableTool124", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mask125: BinaryAssociation = BinaryAssociation(
    name="mask125",
    ends={
        Property(name="tool_EditMaskVariables", type=table_description_LabelEditTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_LabelEditTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
create120: BinaryAssociation = BinaryAssociation(
    name="create120",
    ends={
        Property(name="CreateCellTool", type=table_description_IntersectionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mapping121", type=CreateCellTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables122: BinaryAssociation = BinaryAssociation(
    name="variables122",
    ends={
        Property(name="TableVariable", type=table_description_TableTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableTool", type=TableVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mask132: BinaryAssociation = BinaryAssociation(
    name="mask132",
    ends={
        Property(name="tool_EditMaskVariables133", type=table_description_CreateCellTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateCellTool", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping134: BinaryAssociation = BinaryAssociation(
    name="mapping134",
    ends={
        Property(name="IntersectionMapping136", type=table_description_CreateCellTool, multiplicity=Multiplicity(1, 1)),
        Property(name="create135", type=IntersectionMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping126: BinaryAssociation = BinaryAssociation(
    name="mapping126",
    ends={
        Property(name="ElementColumnMapping127", type=table_description_CreateColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="create", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping128: BinaryAssociation = BinaryAssociation(
    name="mapping128",
    ends={
        Property(name="ElementColumnMapping129", type=table_description_CreateCrossColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateCrossColumnTool", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping130: BinaryAssociation = BinaryAssociation(
    name="mapping130",
    ends={
        Property(name="LineMapping131", type=table_description_CreateLineTool, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_CreateLineTool", type=LineMapping, multiplicity=Multiplicity(0, 1))
    }
)
foreGroundColor142: BinaryAssociation = BinaryAssociation(
    name="foreGroundColor142",
    ends={
        Property(name="ColorDescription", type=table_description_ForegroundStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_ForegroundStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor143: BinaryAssociation = BinaryAssociation(
    name="backgroundColor143",
    ends={
        Property(name="ColorDescription144", type=table_description_BackgroundStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_BackgroundStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
mapping137: BinaryAssociation = BinaryAssociation(
    name="mapping137",
    ends={
        Property(name="ElementColumnMapping138", type=table_description_DeleteColumnTool, multiplicity=Multiplicity(1, 1)),
        Property(name="delete", type=ElementColumnMapping, multiplicity=Multiplicity(1, 1))
    }
)
mapping139: BinaryAssociation = BinaryAssociation(
    name="mapping139",
    ends={
        Property(name="LineMapping141", type=table_description_DeleteLineTool, multiplicity=Multiplicity(1, 1)),
        Property(name="delete140", type=LineMapping, multiplicity=Multiplicity(1, 1))
    }
)
tableDescription149: BinaryAssociation = BinaryAssociation(
    name="tableDescription149",
    ends={
        Property(name="TableDescription150", type=table_description_TableCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableCreationDescription", type=TableDescription, multiplicity=Multiplicity(1, 1))
    }
)
style145: BinaryAssociation = BinaryAssociation(
    name="style145",
    ends={
        Property(name="ForegroundStyleDescription146", type=table_description_ForegroundConditionalStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_ForegroundConditionalStyle", type=ForegroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style147: BinaryAssociation = BinaryAssociation(
    name="style147",
    ends={
        Property(name="BackgroundStyleDescription148", type=table_description_BackgroundConditionalStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_BackgroundConditionalStyle", type=BackgroundStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableDescription151: BinaryAssociation = BinaryAssociation(
    name="tableDescription151",
    ends={
        Property(name="TableDescription152", type=table_description_TableNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="table_description_TableNavigationDescription", type=TableDescription, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_table_DTableElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=table_DTableElement)
gen_table_LineContainer_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_LineContainer)
gen_table_DLine_LineContainer = Generalization(general=LineContainer, specific=table_DLine)
gen_table_DLine_DTableElement = Generalization(general=DTableElement, specific=table_DLine)
gen_table_DLine_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DLine)
gen_table_DTable_DRepresentation = Generalization(general=DRepresentation, specific=table_DTable)
gen_table_DTable_LineContainer = Generalization(general=LineContainer, specific=table_DTable)
gen_table_DTable_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DTable)
gen_table_DCell_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_DCell)
gen_table_DCell_DTableElement = Generalization(general=DTableElement, specific=table_DCell)
gen_table_DCell_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DCell)
gen_table_DCellStyle_DTableElementStyle = Generalization(general=DTableElementStyle, specific=table_DCellStyle)
gen_table_DColumn_DTableElement = Generalization(general=DTableElement, specific=table_DColumn)
gen_table_DTargetColumn_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=table_DTargetColumn)
gen_table_DTargetColumn_DColumn = Generalization(general=DColumn, specific=table_DTargetColumn)
gen_table_DTargetColumn_DTableElementUpdater = Generalization(general=DTableElementUpdater, specific=table_DTargetColumn)
gen_table_DFeatureColumn_DColumn = Generalization(general=DColumn, specific=table_DFeatureColumn)
gen_table_description_TableDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=table_description_TableDescription)
gen_table_description_TableDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=table_description_TableDescription)
gen_table_description_TableDescription_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=table_description_TableDescription)
gen_table_description_EditionTableDescription_TableDescription = Generalization(general=TableDescription, specific=table_description_EditionTableDescription)
gen_table_description_TableMapping_RepresentationElementMapping = Generalization(general=RepresentationElementMapping, specific=table_description_TableMapping)
gen_table_description_CrossTableDescription_TableDescription = Generalization(general=TableDescription, specific=table_description_CrossTableDescription)
gen_table_description_LineMapping_description_TableMapping = Generalization(general=description_TableMapping, specific=table_description_LineMapping)
gen_table_description_LineMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_LineMapping)
gen_table_description_ElementColumnMapping_description_ColumnMapping = Generalization(general=description_ColumnMapping, specific=table_description_ElementColumnMapping)
gen_table_description_ElementColumnMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_ElementColumnMapping)
gen_table_description_ColumnMapping_TableMapping = Generalization(general=TableMapping, specific=table_description_ColumnMapping)
gen_table_description_FeatureColumnMapping_description_ColumnMapping = Generalization(general=description_ColumnMapping, specific=table_description_FeatureColumnMapping)
gen_table_description_FeatureColumnMapping_description_CellUpdater = Generalization(general=description_CellUpdater, specific=table_description_FeatureColumnMapping)
gen_table_description_FeatureColumnMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_FeatureColumnMapping)
gen_table_description_IntersectionMapping_description_TableMapping = Generalization(general=description_TableMapping, specific=table_description_IntersectionMapping)
gen_table_description_IntersectionMapping_description_CellUpdater = Generalization(general=description_CellUpdater, specific=table_description_IntersectionMapping)
gen_table_description_IntersectionMapping_description_StyleUpdater = Generalization(general=description_StyleUpdater, specific=table_description_IntersectionMapping)
gen_table_description_LabelEditTool_TableTool = Generalization(general=TableTool, specific=table_description_LabelEditTool)
gen_table_description_CreateTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_CreateTool)
gen_table_description_CreateCellTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_CreateCellTool)
gen_table_description_CreateTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_CreateTool)
gen_table_description_CreateColumnTool_CreateTool = Generalization(general=CreateTool, specific=table_description_CreateColumnTool)
gen_table_description_CreateCrossColumnTool_CreateTool = Generalization(general=CreateTool, specific=table_description_CreateCrossColumnTool)
gen_table_description_CreateLineTool_CreateTool = Generalization(general=CreateTool, specific=table_description_CreateLineTool)
gen_table_description_CreateCellTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_CreateCellTool)
gen_table_description_DeleteTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=table_description_DeleteTool)
gen_table_description_DeleteTool_description_TableTool = Generalization(general=description_TableTool, specific=table_description_DeleteTool)
gen_table_description_DeleteColumnTool_DeleteTool = Generalization(general=DeleteTool, specific=table_description_DeleteColumnTool)
gen_table_description_DeleteLineTool_DeleteTool = Generalization(general=DeleteTool, specific=table_description_DeleteLineTool)
gen_table_description_TableCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=table_description_TableCreationDescription)
gen_table_description_TableNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=table_description_TableNavigationDescription)
gen_table_description_TableVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=table_description_TableVariable)
gen_table_description_TableVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=table_description_TableVariable)

# Domain Model
domain_model = DomainModel(
    name="table",
    types={table_DTableElement, DRepresentationElement, TableMapping, table_LineContainer, DSemanticDecorator, table_DLine, DTableElement, table_DTable, DRepresentation, LineContainer, DTableElementUpdater, table_DColumn, TableDescription, table_DTableElementUpdater, LineMapping, table_DCell, table_DTableElementStyle, table_DCellStyle, CellUpdater, IntersectionMapping, DTableElementStyle, ColumnMapping, table_DTargetColumn, DColumn, table_DFeatureColumn, table_DTableElementSynchronizer, table_description_TableDescription, description_RepresentationDescription, description_DocumentedElement, table_RGBValues, description_EndUserDocumentedElement, tool_RepresentationCreationDescription, tool_RepresentationNavigationDescription, table_description_EditionTableDescription, FeatureColumnMapping, CreateLineTool, description_table_EObject, table_description_TableMapping, RepresentationElementMapping, table_description_CrossTableDescription, ElementColumnMapping, CreateCrossColumnTool, DeleteLineTool, table_description_LineMapping, description_TableMapping, description_StyleUpdater, table_description_ElementColumnMapping, description_ColumnMapping, table_description_ColumnMapping, table_description_CellUpdater, CreateColumnTool, DeleteColumnTool, table_description_FeatureColumnMapping, description_CellUpdater, BackgroundStyleDescription, BackgroundConditionalStyle, table_description_IntersectionMapping, LabelEditTool, table_description_StyleUpdater, ForegroundStyleDescription, ForegroundConditionalStyle, table_description_LabelEditTool, TableTool, tool_EditMaskVariables, table_description_CreateTool, tool_AbstractToolDescription, CreateCellTool, table_description_TableTool, TableVariable, tool_ModelOperation, table_description_DeleteTool, description_TableTool, table_description_CreateColumnTool, CreateTool, table_description_CreateCrossColumnTool, table_description_CreateLineTool, table_description_CreateCellTool, ColorDescription, table_description_BackgroundStyleDescription, table_description_ForegroundConditionalStyle, table_description_DeleteColumnTool, DeleteTool, table_description_DeleteLineTool, table_description_ForegroundStyleDescription, table_description_TableCreationDescription, RepresentationCreationDescription, table_description_TableNavigationDescription, RepresentationNavigationDescription, table_description_BackgroundConditionalStyle, table_description_TableVariable, tool_AbstractVariable, tool_VariableContainer},
    associations={tableElementMapping2, lines3, columns0, description1, line11, column13, originMapping4, cells5, container6, orderedCells7, currentStyle9, foregroundStyleOrigin22, backgroundStyleOrigin25, currentStyle16, updater18, intersectionMapping20, orderedCells32, cells28, originMapping30, table31, currentStyle35, foregroundColor38, backgroundColor40, reusedRepresentationCreationDescriptions44, allRepresentationCreationDescriptions47, ownedRepresentationCreationDescriptions43, ownedLineMappings58, reusedLineMappings61, allLineMappings64, ownedRepresentationNavigationDescriptions50, reusedRepresentationNavigationDescriptions52, allRepresentationNavigationDescriptions55, importedElements75, ownedColumnMappings77, reusedColumnMappings78, ownedCreateLine67, reusedCreateLine69, allCreateLine72, allColumnMappings81, ownedColumnMappings84, intersection85, createColumn88, create99, delete102, ownedSubLines90, reusedSubLines92, allSubLines94, reusedInMappings97, create103, delete105, defaultBackground111, backgroundConditionalStyle113, directEdit107, defaultForeground108, foregroundConditionalStyle109, lineMapping115, columnMapping117, firstModelOperation123, mask125, create120, variables122, mask132, mapping134, mapping126, mapping128, mapping130, foreGroundColor142, backgroundColor143, mapping137, mapping139, tableDescription149, style145, style147, tableDescription151},
    generalizations={gen_table_DTableElement_DRepresentationElement, gen_table_LineContainer_DSemanticDecorator, gen_table_DLine_LineContainer, gen_table_DLine_DTableElement, gen_table_DLine_DTableElementUpdater, gen_table_DTable_DRepresentation, gen_table_DTable_LineContainer, gen_table_DTable_DTableElementUpdater, gen_table_DCell_DSemanticDecorator, gen_table_DCell_DTableElement, gen_table_DCell_DTableElementUpdater, gen_table_DCellStyle_DTableElementStyle, gen_table_DColumn_DTableElement, gen_table_DTargetColumn_DSemanticDecorator, gen_table_DTargetColumn_DColumn, gen_table_DTargetColumn_DTableElementUpdater, gen_table_DFeatureColumn_DColumn, gen_table_description_TableDescription_description_RepresentationDescription, gen_table_description_TableDescription_description_DocumentedElement, gen_table_description_TableDescription_description_EndUserDocumentedElement, gen_table_description_EditionTableDescription_TableDescription, gen_table_description_TableMapping_RepresentationElementMapping, gen_table_description_CrossTableDescription_TableDescription, gen_table_description_LineMapping_description_TableMapping, gen_table_description_LineMapping_description_StyleUpdater, gen_table_description_ElementColumnMapping_description_ColumnMapping, gen_table_description_ElementColumnMapping_description_StyleUpdater, gen_table_description_ColumnMapping_TableMapping, gen_table_description_FeatureColumnMapping_description_ColumnMapping, gen_table_description_FeatureColumnMapping_description_CellUpdater, gen_table_description_FeatureColumnMapping_description_StyleUpdater, gen_table_description_IntersectionMapping_description_TableMapping, gen_table_description_IntersectionMapping_description_CellUpdater, gen_table_description_IntersectionMapping_description_StyleUpdater, gen_table_description_LabelEditTool_TableTool, gen_table_description_CreateTool_tool_AbstractToolDescription, gen_table_description_CreateCellTool_tool_AbstractToolDescription, gen_table_description_CreateTool_description_TableTool, gen_table_description_CreateColumnTool_CreateTool, gen_table_description_CreateCrossColumnTool_CreateTool, gen_table_description_CreateLineTool_CreateTool, gen_table_description_CreateCellTool_description_TableTool, gen_table_description_DeleteTool_tool_AbstractToolDescription, gen_table_description_DeleteTool_description_TableTool, gen_table_description_DeleteColumnTool_DeleteTool, gen_table_description_DeleteLineTool_DeleteTool, gen_table_description_TableCreationDescription_RepresentationCreationDescription, gen_table_description_TableNavigationDescription_RepresentationNavigationDescription, gen_table_description_TableVariable_tool_AbstractVariable, gen_table_description_TableVariable_tool_VariableContainer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)