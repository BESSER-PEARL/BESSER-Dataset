from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DSemanticDecorator:

    pass
class table_LineContainer(DSemanticDecorator):

    pass
class TableMapping:

    pass
class DRepresentationElement:

    pass
class table_DTableElement(DRepresentationElement):

    pass
class tool_VariableContainer:

    pass
class tool_AbstractVariable:

    pass
class table_description_TableVariable(tool_VariableContainer, tool_AbstractVariable):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


class table_description_BackgroundConditionalStyle:

    def __init__(self, predicateExpression: str, table_description_BackgroundConditionalStyle: "BackgroundStyleDescription" = None):
        self.predicateExpression = predicateExpression
        self.table_description_BackgroundConditionalStyle = table_description_BackgroundConditionalStyle
        
        pass
    @property
    def predicateExpression(self):
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression


    @property
    def table_description_BackgroundConditionalStyle(self):
        return self.__table_description_BackgroundConditionalStyle

    @table_description_BackgroundConditionalStyle.setter
    def table_description_BackgroundConditionalStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_BackgroundConditionalStyle__table_description_BackgroundConditionalStyle", None)
        self.__table_description_BackgroundConditionalStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BackgroundStyleDescription148"):
                opp_val = getattr(old_value, "BackgroundStyleDescription148", None)
                if opp_val == self:
                    setattr(old_value, "BackgroundStyleDescription148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BackgroundStyleDescription148"):
                opp_val = getattr(value, "BackgroundStyleDescription148", None)
                setattr(value, "BackgroundStyleDescription148", self)

class RepresentationNavigationDescription:

    pass
class table_description_TableNavigationDescription(RepresentationNavigationDescription):

    pass
class RepresentationCreationDescription:

    pass
class table_description_TableCreationDescription(RepresentationCreationDescription):

    pass
class table_description_ForegroundStyleDescription:

    def __init__(self, labelSize: int, labelFormat: str, table_description_ForegroundStyleDescription: "ColorDescription" = None):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.table_description_ForegroundStyleDescription = table_description_ForegroundStyleDescription
        
        pass
    @property
    def labelSize(self):
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize


    @property
    def labelFormat(self):
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat


    @property
    def table_description_ForegroundStyleDescription(self):
        return self.__table_description_ForegroundStyleDescription

    @table_description_ForegroundStyleDescription.setter
    def table_description_ForegroundStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_ForegroundStyleDescription__table_description_ForegroundStyleDescription", None)
        self.__table_description_ForegroundStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription"):
                opp_val = getattr(old_value, "ColorDescription", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription"):
                opp_val = getattr(value, "ColorDescription", None)
                setattr(value, "ColorDescription", self)

class DeleteTool:

    pass
class table_description_DeleteLineTool(DeleteTool):

    pass
class table_description_DeleteColumnTool(DeleteTool):

    pass
class table_description_ForegroundConditionalStyle:

    def __init__(self, predicateExpression: str, table_description_ForegroundConditionalStyle: "ForegroundStyleDescription" = None):
        self.predicateExpression = predicateExpression
        self.table_description_ForegroundConditionalStyle = table_description_ForegroundConditionalStyle
        
        pass
    @property
    def predicateExpression(self):
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression


    @property
    def table_description_ForegroundConditionalStyle(self):
        return self.__table_description_ForegroundConditionalStyle

    @table_description_ForegroundConditionalStyle.setter
    def table_description_ForegroundConditionalStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_ForegroundConditionalStyle__table_description_ForegroundConditionalStyle", None)
        self.__table_description_ForegroundConditionalStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ForegroundStyleDescription146"):
                opp_val = getattr(old_value, "ForegroundStyleDescription146", None)
                if opp_val == self:
                    setattr(old_value, "ForegroundStyleDescription146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForegroundStyleDescription146"):
                opp_val = getattr(value, "ForegroundStyleDescription146", None)
                setattr(value, "ForegroundStyleDescription146", self)

class table_description_BackgroundStyleDescription:

    pass
class ColorDescription:

    pass
class CreateTool:

    pass
class table_description_CreateCrossColumnTool(CreateTool):

    pass
class table_description_CreateLineTool(CreateTool):

    pass
class table_description_CreateColumnTool(CreateTool):

    pass
class description_TableTool:

    pass
class tool_ModelOperation:

    pass
class TableVariable:

    pass
class table_description_TableTool:

    pass
class CreateCellTool:

    pass
class tool_AbstractToolDescription:

    pass
class table_description_DeleteTool(description_TableTool, tool_AbstractToolDescription):

    pass
class table_description_CreateCellTool(description_TableTool, tool_AbstractToolDescription):

    pass
class table_description_CreateTool(description_TableTool, tool_AbstractToolDescription):

    pass
class tool_EditMaskVariables:

    pass
class TableTool:

    pass
class table_description_LabelEditTool(TableTool):

    pass
class ForegroundConditionalStyle:

    pass
class ForegroundStyleDescription:

    pass
class table_description_StyleUpdater(ABC):

    pass
class LabelEditTool:

    pass
class BackgroundConditionalStyle:

    pass
class BackgroundStyleDescription:

    pass
class description_CellUpdater:

    pass
class DeleteColumnTool:

    pass
class CreateColumnTool:

    pass
class table_description_CellUpdater:

    def __init__(self, canEdit: str, table_description_CellUpdater: "LabelEditTool" = None):
        self.canEdit = canEdit
        self.table_description_CellUpdater = table_description_CellUpdater
        
        pass
    @property
    def canEdit(self):
        return self.__canEdit

    @canEdit.setter
    def canEdit(self, canEdit: str):
        self.__canEdit = canEdit


    @property
    def table_description_CellUpdater(self):
        return self.__table_description_CellUpdater

    @table_description_CellUpdater.setter
    def table_description_CellUpdater(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_CellUpdater__table_description_CellUpdater", None)
        self.__table_description_CellUpdater = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LabelEditTool"):
                opp_val = getattr(old_value, "LabelEditTool", None)
                if opp_val == self:
                    setattr(old_value, "LabelEditTool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LabelEditTool"):
                opp_val = getattr(value, "LabelEditTool", None)
                setattr(value, "LabelEditTool", self)

    def getCreateCell(self) :
        # TODO: Implement getCreateCell method
        pass

    def getLabelComputationExpression(self) :
        # TODO: Implement getLabelComputationExpression method
        pass

class table_description_ColumnMapping(TableMapping):

    def __init__(self, headerLabelExpression: str, initialWidth: int, TableMapping27: "table_DCellStyle" = None, TableMapping24: "table_DCellStyle" = None, TableMapping: "table_DTableElement" = None):
        self.headerLabelExpression = headerLabelExpression
        self.initialWidth = initialWidth
        
        pass
    @property
    def initialWidth(self):
        return self.__initialWidth

    @initialWidth.setter
    def initialWidth(self, initialWidth: int):
        self.__initialWidth = initialWidth


    @property
    def headerLabelExpression(self):
        return self.__headerLabelExpression

    @headerLabelExpression.setter
    def headerLabelExpression(self, headerLabelExpression: str):
        self.__headerLabelExpression = headerLabelExpression


class description_ColumnMapping:

    pass
class description_StyleUpdater:

    pass
class table_description_FeatureColumnMapping(description_CellUpdater, description_ColumnMapping, description_StyleUpdater):

    def __init__(self, featureParentExpression: str, featureName: str, labelExpression: str):
        self.featureParentExpression = featureParentExpression
        self.featureName = featureName
        self.labelExpression = labelExpression
        
        pass
    @property
    def featureParentExpression(self):
        return self.__featureParentExpression

    @featureParentExpression.setter
    def featureParentExpression(self, featureParentExpression: str):
        self.__featureParentExpression = featureParentExpression


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def labelExpression(self):
        return self.__labelExpression

    @labelExpression.setter
    def labelExpression(self, labelExpression: str):
        self.__labelExpression = labelExpression


class table_description_ElementColumnMapping(description_ColumnMapping, description_StyleUpdater):

    def __init__(self, domainClass: str, semanticCandidatesExpression: str, mapping104: set["CreateColumnTool"] = None, mapping106: "DeleteColumnTool" = None):
        self.domainClass = domainClass
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.mapping104 = mapping104 if mapping104 is not None else set()
        self.mapping106 = mapping106
        
        pass
    @property
    def semanticCandidatesExpression(self):
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression


    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def mapping106(self):
        return self.__mapping106

    @mapping106.setter
    def mapping106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_ElementColumnMapping__mapping106", None)
        self.__mapping106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeleteColumnTool"):
                opp_val = getattr(old_value, "DeleteColumnTool", None)
                if opp_val == self:
                    setattr(old_value, "DeleteColumnTool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeleteColumnTool"):
                opp_val = getattr(value, "DeleteColumnTool", None)
                setattr(value, "DeleteColumnTool", self)

    @property
    def mapping104(self):
        return self.__mapping104

    @mapping104.setter
    def mapping104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_ElementColumnMapping__mapping104", None)
        self.__mapping104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreateColumnTool"):
                    opp_val = getattr(item, "CreateColumnTool", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateColumnTool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateColumnTool"):
                    opp_val = getattr(item, "CreateColumnTool", None)
                    
                    setattr(item, "CreateColumnTool", self)
                    

class description_TableMapping:

    pass
class table_description_IntersectionMapping(description_CellUpdater, description_StyleUpdater, description_TableMapping):

    def __init__(self, lineFinderExpression: str, semanticCandidatesExpression: str, domainClass: str, preconditionExpression: str, labelExpression: str, useDomainClass: bool, columnFinderExpression: str, table_description_IntersectionMapping: set["LineMapping"] = None, table_description_IntersectionMapping118: "ColumnMapping" = None, mapping121: "CreateCellTool" = None):
        self.lineFinderExpression = lineFinderExpression
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.labelExpression = labelExpression
        self.useDomainClass = useDomainClass
        self.columnFinderExpression = columnFinderExpression
        self.table_description_IntersectionMapping = table_description_IntersectionMapping if table_description_IntersectionMapping is not None else set()
        self.table_description_IntersectionMapping118 = table_description_IntersectionMapping118
        self.mapping121 = mapping121
        
        pass
    @property
    def labelExpression(self):
        return self.__labelExpression

    @labelExpression.setter
    def labelExpression(self, labelExpression: str):
        self.__labelExpression = labelExpression


    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def columnFinderExpression(self):
        return self.__columnFinderExpression

    @columnFinderExpression.setter
    def columnFinderExpression(self, columnFinderExpression: str):
        self.__columnFinderExpression = columnFinderExpression


    @property
    def lineFinderExpression(self):
        return self.__lineFinderExpression

    @lineFinderExpression.setter
    def lineFinderExpression(self, lineFinderExpression: str):
        self.__lineFinderExpression = lineFinderExpression


    @property
    def useDomainClass(self):
        return self.__useDomainClass

    @useDomainClass.setter
    def useDomainClass(self, useDomainClass: bool):
        self.__useDomainClass = useDomainClass


    @property
    def semanticCandidatesExpression(self):
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression


    @property
    def preconditionExpression(self):
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression


    @property
    def table_description_IntersectionMapping(self):
        return self.__table_description_IntersectionMapping

    @table_description_IntersectionMapping.setter
    def table_description_IntersectionMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_IntersectionMapping__table_description_IntersectionMapping", None)
        self.__table_description_IntersectionMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping116"):
                    opp_val = getattr(item, "LineMapping116", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping116"):
                    opp_val = getattr(item, "LineMapping116", None)
                    
                    setattr(item, "LineMapping116", self)
                    

    @property
    def table_description_IntersectionMapping118(self):
        return self.__table_description_IntersectionMapping118

    @table_description_IntersectionMapping118.setter
    def table_description_IntersectionMapping118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_IntersectionMapping__table_description_IntersectionMapping118", None)
        self.__table_description_IntersectionMapping118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnMapping119"):
                opp_val = getattr(old_value, "ColumnMapping119", None)
                if opp_val == self:
                    setattr(old_value, "ColumnMapping119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnMapping119"):
                opp_val = getattr(value, "ColumnMapping119", None)
                setattr(value, "ColumnMapping119", self)

    @property
    def mapping121(self):
        return self.__mapping121

    @mapping121.setter
    def mapping121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_IntersectionMapping__mapping121", None)
        self.__mapping121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CreateCellTool"):
                opp_val = getattr(old_value, "CreateCellTool", None)
                if opp_val == self:
                    setattr(old_value, "CreateCellTool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CreateCellTool"):
                opp_val = getattr(value, "CreateCellTool", None)
                setattr(value, "CreateCellTool", self)

class table_description_LineMapping(description_StyleUpdater, description_TableMapping):

    def __init__(self, domainClass: str, semanticCandidatesExpression: str, headerLabelExpression: str, table_description_LineMapping100: set["CreateLineTool"] = None, mapping: "DeleteLineTool" = None, table_description_LineMapping: set["LineMapping"] = None, reusedInMappings: set["LineMapping"] = None, table_description_LineMapping95: set["LineMapping"] = None, reusedSubLines: set["LineMapping"] = None):
        self.domainClass = domainClass
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.headerLabelExpression = headerLabelExpression
        self.table_description_LineMapping100 = table_description_LineMapping100 if table_description_LineMapping100 is not None else set()
        self.mapping = mapping
        self.table_description_LineMapping = table_description_LineMapping if table_description_LineMapping is not None else set()
        self.reusedInMappings = reusedInMappings if reusedInMappings is not None else set()
        self.table_description_LineMapping95 = table_description_LineMapping95 if table_description_LineMapping95 is not None else set()
        self.reusedSubLines = reusedSubLines if reusedSubLines is not None else set()
        
        pass
    @property
    def semanticCandidatesExpression(self):
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression


    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def headerLabelExpression(self):
        return self.__headerLabelExpression

    @headerLabelExpression.setter
    def headerLabelExpression(self, headerLabelExpression: str):
        self.__headerLabelExpression = headerLabelExpression


    @property
    def table_description_LineMapping100(self):
        return self.__table_description_LineMapping100

    @table_description_LineMapping100.setter
    def table_description_LineMapping100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__table_description_LineMapping100", None)
        self.__table_description_LineMapping100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreateLineTool101"):
                    opp_val = getattr(item, "CreateLineTool101", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool101"):
                    opp_val = getattr(item, "CreateLineTool101", None)
                    
                    setattr(item, "CreateLineTool101", self)
                    

    @property
    def mapping(self):
        return self.__mapping

    @mapping.setter
    def mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__mapping", None)
        self.__mapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeleteLineTool"):
                opp_val = getattr(old_value, "DeleteLineTool", None)
                if opp_val == self:
                    setattr(old_value, "DeleteLineTool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeleteLineTool"):
                opp_val = getattr(value, "DeleteLineTool", None)
                setattr(value, "DeleteLineTool", self)

    @property
    def reusedInMappings(self):
        return self.__reusedInMappings

    @reusedInMappings.setter
    def reusedInMappings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__reusedInMappings", None)
        self.__reusedInMappings = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping93"):
                    opp_val = getattr(item, "LineMapping93", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping93"):
                    opp_val = getattr(item, "LineMapping93", None)
                    
                    setattr(item, "LineMapping93", self)
                    

    @property
    def reusedSubLines(self):
        return self.__reusedSubLines

    @reusedSubLines.setter
    def reusedSubLines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__reusedSubLines", None)
        self.__reusedSubLines = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping98"):
                    opp_val = getattr(item, "LineMapping98", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping98"):
                    opp_val = getattr(item, "LineMapping98", None)
                    
                    setattr(item, "LineMapping98", self)
                    

    @property
    def table_description_LineMapping95(self):
        return self.__table_description_LineMapping95

    @table_description_LineMapping95.setter
    def table_description_LineMapping95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__table_description_LineMapping95", None)
        self.__table_description_LineMapping95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping96"):
                    opp_val = getattr(item, "LineMapping96", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping96"):
                    opp_val = getattr(item, "LineMapping96", None)
                    
                    setattr(item, "LineMapping96", self)
                    

    @property
    def table_description_LineMapping(self):
        return self.__table_description_LineMapping

    @table_description_LineMapping.setter
    def table_description_LineMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__table_description_LineMapping", None)
        self.__table_description_LineMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping91"):
                    opp_val = getattr(item, "LineMapping91", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping91"):
                    opp_val = getattr(item, "LineMapping91", None)
                    
                    setattr(item, "LineMapping91", self)
                    

class DeleteLineTool:

    pass
class CreateCrossColumnTool:

    pass
class ElementColumnMapping:

    pass
class RepresentationElementMapping:

    pass
class table_description_TableMapping(RepresentationElementMapping):

    def __init__(self, semanticElements: str):
        self.semanticElements = semanticElements
        
        pass
    @property
    def semanticElements(self):
        return self.__semanticElements

    @semanticElements.setter
    def semanticElements(self, semanticElements: str):
        self.__semanticElements = semanticElements


class description_table_EObject:

    pass
class CreateLineTool:

    pass
class FeatureColumnMapping:

    pass
class tool_RepresentationNavigationDescription:

    pass
class tool_RepresentationCreationDescription:

    pass
class description_EndUserDocumentedElement:

    pass
class table_RGBValues:

    pass
class description_DocumentedElement:

    pass
class description_RepresentationDescription:

    pass
class table_description_TableDescription(description_DocumentedElement, description_EndUserDocumentedElement, description_RepresentationDescription):

    def __init__(self, preconditionExpression: str, domainClass: str, initialHeaderColumnWidth: int, table_description_TableDescription45: set["tool_RepresentationCreationDescription"] = None, table_description_TableDescription48: set["tool_RepresentationCreationDescription"] = None, table_description_TableDescription: set["tool_RepresentationCreationDescription"] = None, table_description_TableDescription59: set["LineMapping"] = None, table_description_TableDescription62: set["LineMapping"] = None, table_description_TableDescription65: set["LineMapping"] = None, table_description_TableDescription51: set["tool_RepresentationNavigationDescription"] = None, table_description_TableDescription53: set["tool_RepresentationNavigationDescription"] = None, table_description_TableDescription56: set["tool_RepresentationNavigationDescription"] = None, table_description_TableDescription76: set["description_table_EObject"] = None, table_description_TableDescription68: set["CreateLineTool"] = None, table_description_TableDescription70: set["CreateLineTool"] = None, table_description_TableDescription73: set["CreateLineTool"] = None):
        self.preconditionExpression = preconditionExpression
        self.domainClass = domainClass
        self.initialHeaderColumnWidth = initialHeaderColumnWidth
        self.table_description_TableDescription45 = table_description_TableDescription45 if table_description_TableDescription45 is not None else set()
        self.table_description_TableDescription48 = table_description_TableDescription48 if table_description_TableDescription48 is not None else set()
        self.table_description_TableDescription = table_description_TableDescription if table_description_TableDescription is not None else set()
        self.table_description_TableDescription59 = table_description_TableDescription59 if table_description_TableDescription59 is not None else set()
        self.table_description_TableDescription62 = table_description_TableDescription62 if table_description_TableDescription62 is not None else set()
        self.table_description_TableDescription65 = table_description_TableDescription65 if table_description_TableDescription65 is not None else set()
        self.table_description_TableDescription51 = table_description_TableDescription51 if table_description_TableDescription51 is not None else set()
        self.table_description_TableDescription53 = table_description_TableDescription53 if table_description_TableDescription53 is not None else set()
        self.table_description_TableDescription56 = table_description_TableDescription56 if table_description_TableDescription56 is not None else set()
        self.table_description_TableDescription76 = table_description_TableDescription76 if table_description_TableDescription76 is not None else set()
        self.table_description_TableDescription68 = table_description_TableDescription68 if table_description_TableDescription68 is not None else set()
        self.table_description_TableDescription70 = table_description_TableDescription70 if table_description_TableDescription70 is not None else set()
        self.table_description_TableDescription73 = table_description_TableDescription73 if table_description_TableDescription73 is not None else set()
        
        pass
    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def initialHeaderColumnWidth(self):
        return self.__initialHeaderColumnWidth

    @initialHeaderColumnWidth.setter
    def initialHeaderColumnWidth(self, initialHeaderColumnWidth: int):
        self.__initialHeaderColumnWidth = initialHeaderColumnWidth


    @property
    def preconditionExpression(self):
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression


    @property
    def table_description_TableDescription51(self):
        return self.__table_description_TableDescription51

    @table_description_TableDescription51.setter
    def table_description_TableDescription51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription51", None)
        self.__table_description_TableDescription51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationNavigationDescription"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationNavigationDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationNavigationDescription"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription", None)
                    
                    setattr(item, "tool_RepresentationNavigationDescription", self)
                    

    @property
    def table_description_TableDescription68(self):
        return self.__table_description_TableDescription68

    @table_description_TableDescription68.setter
    def table_description_TableDescription68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription68", None)
        self.__table_description_TableDescription68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreateLineTool"):
                    opp_val = getattr(item, "CreateLineTool", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool"):
                    opp_val = getattr(item, "CreateLineTool", None)
                    
                    setattr(item, "CreateLineTool", self)
                    

    @property
    def table_description_TableDescription76(self):
        return self.__table_description_TableDescription76

    @table_description_TableDescription76.setter
    def table_description_TableDescription76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription76", None)
        self.__table_description_TableDescription76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_table_EObject"):
                    opp_val = getattr(item, "description_table_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "description_table_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_table_EObject"):
                    opp_val = getattr(item, "description_table_EObject", None)
                    
                    setattr(item, "description_table_EObject", self)
                    

    @property
    def table_description_TableDescription56(self):
        return self.__table_description_TableDescription56

    @table_description_TableDescription56.setter
    def table_description_TableDescription56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription56", None)
        self.__table_description_TableDescription56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationNavigationDescription57"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription57", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationNavigationDescription57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationNavigationDescription57"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription57", None)
                    
                    setattr(item, "tool_RepresentationNavigationDescription57", self)
                    

    @property
    def table_description_TableDescription45(self):
        return self.__table_description_TableDescription45

    @table_description_TableDescription45.setter
    def table_description_TableDescription45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription45", None)
        self.__table_description_TableDescription45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationCreationDescription46"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription46", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationCreationDescription46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationCreationDescription46"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription46", None)
                    
                    setattr(item, "tool_RepresentationCreationDescription46", self)
                    

    @property
    def table_description_TableDescription(self):
        return self.__table_description_TableDescription

    @table_description_TableDescription.setter
    def table_description_TableDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription", None)
        self.__table_description_TableDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationCreationDescription"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationCreationDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationCreationDescription"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription", None)
                    
                    setattr(item, "tool_RepresentationCreationDescription", self)
                    

    @property
    def table_description_TableDescription59(self):
        return self.__table_description_TableDescription59

    @table_description_TableDescription59.setter
    def table_description_TableDescription59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription59", None)
        self.__table_description_TableDescription59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping60"):
                    opp_val = getattr(item, "LineMapping60", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping60"):
                    opp_val = getattr(item, "LineMapping60", None)
                    
                    setattr(item, "LineMapping60", self)
                    

    @property
    def table_description_TableDescription48(self):
        return self.__table_description_TableDescription48

    @table_description_TableDescription48.setter
    def table_description_TableDescription48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription48", None)
        self.__table_description_TableDescription48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationCreationDescription49"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription49", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationCreationDescription49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationCreationDescription49"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription49", None)
                    
                    setattr(item, "tool_RepresentationCreationDescription49", self)
                    

    @property
    def table_description_TableDescription73(self):
        return self.__table_description_TableDescription73

    @table_description_TableDescription73.setter
    def table_description_TableDescription73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription73", None)
        self.__table_description_TableDescription73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreateLineTool74"):
                    opp_val = getattr(item, "CreateLineTool74", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool74"):
                    opp_val = getattr(item, "CreateLineTool74", None)
                    
                    setattr(item, "CreateLineTool74", self)
                    

    @property
    def table_description_TableDescription70(self):
        return self.__table_description_TableDescription70

    @table_description_TableDescription70.setter
    def table_description_TableDescription70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription70", None)
        self.__table_description_TableDescription70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreateLineTool71"):
                    opp_val = getattr(item, "CreateLineTool71", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool71"):
                    opp_val = getattr(item, "CreateLineTool71", None)
                    
                    setattr(item, "CreateLineTool71", self)
                    

    @property
    def table_description_TableDescription65(self):
        return self.__table_description_TableDescription65

    @table_description_TableDescription65.setter
    def table_description_TableDescription65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription65", None)
        self.__table_description_TableDescription65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping66"):
                    opp_val = getattr(item, "LineMapping66", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping66"):
                    opp_val = getattr(item, "LineMapping66", None)
                    
                    setattr(item, "LineMapping66", self)
                    

    @property
    def table_description_TableDescription62(self):
        return self.__table_description_TableDescription62

    @table_description_TableDescription62.setter
    def table_description_TableDescription62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription62", None)
        self.__table_description_TableDescription62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping63"):
                    opp_val = getattr(item, "LineMapping63", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping63"):
                    opp_val = getattr(item, "LineMapping63", None)
                    
                    setattr(item, "LineMapping63", self)
                    

    @property
    def table_description_TableDescription53(self):
        return self.__table_description_TableDescription53

    @table_description_TableDescription53.setter
    def table_description_TableDescription53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription53", None)
        self.__table_description_TableDescription53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationNavigationDescription54"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription54", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationNavigationDescription54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationNavigationDescription54"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription54", None)
                    
                    setattr(item, "tool_RepresentationNavigationDescription54", self)
                    

class table_DTableElementSynchronizer(ABC):

    def __init__(self):
        
        pass
    def refresh(self, table_line):
        # TODO: Implement refresh method
        pass

class DColumn:

    pass
class table_DFeatureColumn(DColumn):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


class ColumnMapping:

    pass
class DTableElementStyle:

    pass
class IntersectionMapping:

    pass
class CellUpdater:

    pass
class table_DCellStyle(DTableElementStyle):

    pass
class table_DTableElementStyle:

    def __init__(self, defaultBackgroundStyle: bool, labelSize: int, labelFormat: str, defaultForegroundStyle: bool, table_DTableElementStyle: "table_DLine" = None, table_DTableElementStyle37: "table_DColumn" = None, table_DTableElementStyle39: "table_RGBValues" = None, table_DTableElementStyle41: "table_RGBValues" = None):
        self.defaultBackgroundStyle = defaultBackgroundStyle
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.defaultForegroundStyle = defaultForegroundStyle
        self.table_DTableElementStyle = table_DTableElementStyle
        self.table_DTableElementStyle37 = table_DTableElementStyle37
        self.table_DTableElementStyle39 = table_DTableElementStyle39
        self.table_DTableElementStyle41 = table_DTableElementStyle41
        
        pass
    @property
    def defaultBackgroundStyle(self):
        return self.__defaultBackgroundStyle

    @defaultBackgroundStyle.setter
    def defaultBackgroundStyle(self, defaultBackgroundStyle: bool):
        self.__defaultBackgroundStyle = defaultBackgroundStyle


    @property
    def labelFormat(self):
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat


    @property
    def defaultForegroundStyle(self):
        return self.__defaultForegroundStyle

    @defaultForegroundStyle.setter
    def defaultForegroundStyle(self, defaultForegroundStyle: bool):
        self.__defaultForegroundStyle = defaultForegroundStyle


    @property
    def labelSize(self):
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize


    @property
    def table_DTableElementStyle37(self):
        return self.__table_DTableElementStyle37

    @table_DTableElementStyle37.setter
    def table_DTableElementStyle37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTableElementStyle__table_DTableElementStyle37", None)
        self.__table_DTableElementStyle37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DColumn36"):
                opp_val = getattr(old_value, "table_DColumn36", None)
                if opp_val == self:
                    setattr(old_value, "table_DColumn36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DColumn36"):
                opp_val = getattr(value, "table_DColumn36", None)
                setattr(value, "table_DColumn36", self)

    @property
    def table_DTableElementStyle39(self):
        return self.__table_DTableElementStyle39

    @table_DTableElementStyle39.setter
    def table_DTableElementStyle39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTableElementStyle__table_DTableElementStyle39", None)
        self.__table_DTableElementStyle39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_RGBValues"):
                opp_val = getattr(old_value, "table_RGBValues", None)
                if opp_val == self:
                    setattr(old_value, "table_RGBValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_RGBValues"):
                opp_val = getattr(value, "table_RGBValues", None)
                setattr(value, "table_RGBValues", self)

    @property
    def table_DTableElementStyle41(self):
        return self.__table_DTableElementStyle41

    @table_DTableElementStyle41.setter
    def table_DTableElementStyle41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTableElementStyle__table_DTableElementStyle41", None)
        self.__table_DTableElementStyle41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_RGBValues42"):
                opp_val = getattr(old_value, "table_RGBValues42", None)
                if opp_val == self:
                    setattr(old_value, "table_RGBValues42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_RGBValues42"):
                opp_val = getattr(value, "table_RGBValues42", None)
                setattr(value, "table_RGBValues42", self)

    @property
    def table_DTableElementStyle(self):
        return self.__table_DTableElementStyle

    @table_DTableElementStyle.setter
    def table_DTableElementStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTableElementStyle__table_DTableElementStyle", None)
        self.__table_DTableElementStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DLine10"):
                opp_val = getattr(old_value, "table_DLine10", None)
                if opp_val == self:
                    setattr(old_value, "table_DLine10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DLine10"):
                opp_val = getattr(value, "table_DLine10", None)
                setattr(value, "table_DLine10", self)

class LineMapping:

    pass
class table_DTableElementUpdater(ABC):

    def __init__(self):
        
        pass
    def deactivate(self):
        # TODO: Implement deactivate method
        pass

    def activate(self, table_sync):
        # TODO: Implement activate method
        pass

class TableDescription:

    pass
class table_description_CrossTableDescription(TableDescription):

    pass
class table_description_EditionTableDescription(TableDescription):

    pass
class DTableElementUpdater:

    pass
class table_DTargetColumn(DColumn, DSemanticDecorator, DTableElementUpdater):

    pass
class LineContainer:

    pass
class DRepresentation:

    pass
class table_DTable(DRepresentation, LineContainer, DTableElementUpdater):

    def __init__(self, headerColumnWidth: int, DTable: "table_DColumn" = None, table: set["table_DColumn"] = None, table_DTable: "TableDescription" = None):
        self.headerColumnWidth = headerColumnWidth
        self.DTable = DTable
        self.table = table if table is not None else set()
        self.table_DTable = table_DTable
        
        pass
    @property
    def headerColumnWidth(self):
        return self.__headerColumnWidth

    @headerColumnWidth.setter
    def headerColumnWidth(self, headerColumnWidth: int):
        self.__headerColumnWidth = headerColumnWidth


    @property
    def DTable(self):
        return self.__DTable

    @DTable.setter
    def DTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTable__DTable", None)
        self.__DTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if opp_val == self:
                    setattr(old_value, "columns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                setattr(value, "columns", self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTable__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DColumn"):
                    opp_val = getattr(item, "DColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "DColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DColumn"):
                    opp_val = getattr(item, "DColumn", None)
                    
                    setattr(item, "DColumn", self)
                    

    @property
    def table_DTable(self):
        return self.__table_DTable

    @table_DTable.setter
    def table_DTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DTable__table_DTable", None)
        self.__table_DTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableDescription"):
                opp_val = getattr(old_value, "TableDescription", None)
                if opp_val == self:
                    setattr(old_value, "TableDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableDescription"):
                opp_val = getattr(value, "TableDescription", None)
                setattr(value, "TableDescription", self)

class DTableElement:

    pass
class table_DCell(DTableElement, DSemanticDecorator, DTableElementUpdater):

    def __init__(self, label: str, table_DCell: "table_DLine" = None, table_DCell17: "table_DCellStyle" = None, table_DCell19: "CellUpdater" = None, table_DCell21: "IntersectionMapping" = None, table_DCell34: "table_DColumn" = None, DCell29: "table_DColumn" = None, cells: "table_DLine" = None, cells14: "table_DColumn" = None, DCell: "table_DLine" = None):
        self.label = label
        self.table_DCell = table_DCell
        self.table_DCell17 = table_DCell17
        self.table_DCell19 = table_DCell19
        self.table_DCell21 = table_DCell21
        self.table_DCell34 = table_DCell34
        self.DCell29 = DCell29
        self.cells = cells
        self.cells14 = cells14
        self.DCell = DCell
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def cells14(self):
        return self.__cells14

    @cells14.setter
    def cells14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__cells14", None)
        self.__cells14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DColumn15"):
                opp_val = getattr(old_value, "DColumn15", None)
                if opp_val == self:
                    setattr(old_value, "DColumn15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DColumn15"):
                opp_val = getattr(value, "DColumn15", None)
                setattr(value, "DColumn15", self)

    @property
    def table_DCell21(self):
        return self.__table_DCell21

    @table_DCell21.setter
    def table_DCell21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__table_DCell21", None)
        self.__table_DCell21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntersectionMapping"):
                opp_val = getattr(old_value, "IntersectionMapping", None)
                if opp_val == self:
                    setattr(old_value, "IntersectionMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntersectionMapping"):
                opp_val = getattr(value, "IntersectionMapping", None)
                setattr(value, "IntersectionMapping", self)

    @property
    def table_DCell(self):
        return self.__table_DCell

    @table_DCell.setter
    def table_DCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__table_DCell", None)
        self.__table_DCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DLine8"):
                opp_val = getattr(old_value, "table_DLine8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DLine8"):
                opp_val = getattr(value, "table_DLine8", None)
                if opp_val is None:
                    setattr(value, "table_DLine8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__cells", None)
        self.__cells = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DLine12"):
                opp_val = getattr(old_value, "DLine12", None)
                if opp_val == self:
                    setattr(old_value, "DLine12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DLine12"):
                opp_val = getattr(value, "DLine12", None)
                setattr(value, "DLine12", self)

    @property
    def DCell29(self):
        return self.__DCell29

    @DCell29.setter
    def DCell29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__DCell29", None)
        self.__DCell29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column"):
                opp_val = getattr(old_value, "column", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column"):
                opp_val = getattr(value, "column", None)
                if opp_val is None:
                    setattr(value, "column", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def table_DCell19(self):
        return self.__table_DCell19

    @table_DCell19.setter
    def table_DCell19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__table_DCell19", None)
        self.__table_DCell19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CellUpdater"):
                opp_val = getattr(old_value, "CellUpdater", None)
                if opp_val == self:
                    setattr(old_value, "CellUpdater", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CellUpdater"):
                opp_val = getattr(value, "CellUpdater", None)
                setattr(value, "CellUpdater", self)

    @property
    def table_DCell17(self):
        return self.__table_DCell17

    @table_DCell17.setter
    def table_DCell17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__table_DCell17", None)
        self.__table_DCell17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DCellStyle"):
                opp_val = getattr(old_value, "table_DCellStyle", None)
                if opp_val == self:
                    setattr(old_value, "table_DCellStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DCellStyle"):
                opp_val = getattr(value, "table_DCellStyle", None)
                setattr(value, "table_DCellStyle", self)

    @property
    def DCell(self):
        return self.__DCell

    @DCell.setter
    def DCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__DCell", None)
        self.__DCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "line"):
                opp_val = getattr(old_value, "line", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "line"):
                opp_val = getattr(value, "line", None)
                if opp_val is None:
                    setattr(value, "line", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def table_DCell34(self):
        return self.__table_DCell34

    @table_DCell34.setter
    def table_DCell34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DCell__table_DCell34", None)
        self.__table_DCell34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DColumn33"):
                opp_val = getattr(old_value, "table_DColumn33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DColumn33"):
                opp_val = getattr(value, "table_DColumn33", None)
                if opp_val is None:
                    setattr(value, "table_DColumn33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class table_DColumn(DTableElement):

    def __init__(self, visible: bool, width: int, label: str, table_DColumn33: set["table_DCell"] = None, column: set["table_DCell"] = None, table_DColumn: "ColumnMapping" = None, columns: "table_DTable" = None, table_DColumn36: "table_DTableElementStyle" = None, DColumn: "table_DTable" = None, DColumn15: "table_DCell" = None):
        self.visible = visible
        self.width = width
        self.label = label
        self.table_DColumn33 = table_DColumn33 if table_DColumn33 is not None else set()
        self.column = column if column is not None else set()
        self.table_DColumn = table_DColumn
        self.columns = columns
        self.table_DColumn36 = table_DColumn36
        self.DColumn = DColumn
        self.DColumn15 = DColumn15
        
        pass
    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def table_DColumn36(self):
        return self.__table_DColumn36

    @table_DColumn36.setter
    def table_DColumn36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__table_DColumn36", None)
        self.__table_DColumn36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DTableElementStyle37"):
                opp_val = getattr(old_value, "table_DTableElementStyle37", None)
                if opp_val == self:
                    setattr(old_value, "table_DTableElementStyle37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DTableElementStyle37"):
                opp_val = getattr(value, "table_DTableElementStyle37", None)
                setattr(value, "table_DTableElementStyle37", self)

    @property
    def table_DColumn33(self):
        return self.__table_DColumn33

    @table_DColumn33.setter
    def table_DColumn33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__table_DColumn33", None)
        self.__table_DColumn33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table_DCell34"):
                    opp_val = getattr(item, "table_DCell34", None)
                    
                    if opp_val == self:
                        setattr(item, "table_DCell34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table_DCell34"):
                    opp_val = getattr(item, "table_DCell34", None)
                    
                    setattr(item, "table_DCell34", self)
                    

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__column", None)
        self.__column = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DCell29"):
                    opp_val = getattr(item, "DCell29", None)
                    
                    if opp_val == self:
                        setattr(item, "DCell29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DCell29"):
                    opp_val = getattr(item, "DCell29", None)
                    
                    setattr(item, "DCell29", self)
                    

    @property
    def table_DColumn(self):
        return self.__table_DColumn

    @table_DColumn.setter
    def table_DColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__table_DColumn", None)
        self.__table_DColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnMapping"):
                opp_val = getattr(old_value, "ColumnMapping", None)
                if opp_val == self:
                    setattr(old_value, "ColumnMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnMapping"):
                opp_val = getattr(value, "ColumnMapping", None)
                setattr(value, "ColumnMapping", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DTable"):
                opp_val = getattr(old_value, "DTable", None)
                if opp_val == self:
                    setattr(old_value, "DTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DTable"):
                opp_val = getattr(value, "DTable", None)
                setattr(value, "DTable", self)

    @property
    def DColumn15(self):
        return self.__DColumn15

    @DColumn15.setter
    def DColumn15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__DColumn15", None)
        self.__DColumn15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cells14"):
                opp_val = getattr(old_value, "cells14", None)
                if opp_val == self:
                    setattr(old_value, "cells14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cells14"):
                opp_val = getattr(value, "cells14", None)
                setattr(value, "cells14", self)

    @property
    def DColumn(self):
        return self.__DColumn

    @DColumn.setter
    def DColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DColumn__DColumn", None)
        self.__DColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class table_DLine(DTableElement, LineContainer, DTableElementUpdater):

    def __init__(self, label: str, visible: bool, collapsed: bool, table_DLine8: set["table_DCell"] = None, table_DLine10: "table_DTableElementStyle" = None, DLine: "table_LineContainer" = None, DLine12: "table_DCell" = None, table_DLine: "LineMapping" = None, line: set["table_DCell"] = None, lines: "table_LineContainer" = None):
        self.label = label
        self.visible = visible
        self.collapsed = collapsed
        self.table_DLine8 = table_DLine8 if table_DLine8 is not None else set()
        self.table_DLine10 = table_DLine10
        self.DLine = DLine
        self.DLine12 = DLine12
        self.table_DLine = table_DLine
        self.line = line if line is not None else set()
        self.lines = lines
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def collapsed(self):
        return self.__collapsed

    @collapsed.setter
    def collapsed(self, collapsed: bool):
        self.__collapsed = collapsed


    @property
    def DLine12(self):
        return self.__DLine12

    @DLine12.setter
    def DLine12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__DLine12", None)
        self.__DLine12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cells"):
                opp_val = getattr(old_value, "cells", None)
                if opp_val == self:
                    setattr(old_value, "cells", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cells"):
                opp_val = getattr(value, "cells", None)
                setattr(value, "cells", self)

    @property
    def table_DLine10(self):
        return self.__table_DLine10

    @table_DLine10.setter
    def table_DLine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__table_DLine10", None)
        self.__table_DLine10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_DTableElementStyle"):
                opp_val = getattr(old_value, "table_DTableElementStyle", None)
                if opp_val == self:
                    setattr(old_value, "table_DTableElementStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_DTableElementStyle"):
                opp_val = getattr(value, "table_DTableElementStyle", None)
                setattr(value, "table_DTableElementStyle", self)

    @property
    def DLine(self):
        return self.__DLine

    @DLine.setter
    def DLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__DLine", None)
        self.__DLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__line", None)
        self.__line = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DCell"):
                    opp_val = getattr(item, "DCell", None)
                    
                    if opp_val == self:
                        setattr(item, "DCell", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DCell"):
                    opp_val = getattr(item, "DCell", None)
                    
                    setattr(item, "DCell", self)
                    

    @property
    def table_DLine(self):
        return self.__table_DLine

    @table_DLine.setter
    def table_DLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__table_DLine", None)
        self.__table_DLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LineMapping"):
                opp_val = getattr(old_value, "LineMapping", None)
                if opp_val == self:
                    setattr(old_value, "LineMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LineMapping"):
                opp_val = getattr(value, "LineMapping", None)
                setattr(value, "LineMapping", self)

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__lines", None)
        self.__lines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LineContainer"):
                opp_val = getattr(old_value, "LineContainer", None)
                if opp_val == self:
                    setattr(old_value, "LineContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LineContainer"):
                opp_val = getattr(value, "LineContainer", None)
                setattr(value, "LineContainer", self)

    @property
    def table_DLine8(self):
        return self.__table_DLine8

    @table_DLine8.setter
    def table_DLine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_DLine__table_DLine8", None)
        self.__table_DLine8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table_DCell"):
                    opp_val = getattr(item, "table_DCell", None)
                    
                    if opp_val == self:
                        setattr(item, "table_DCell", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table_DCell"):
                    opp_val = getattr(item, "table_DCell", None)
                    
                    setattr(item, "table_DCell", self)
                    
