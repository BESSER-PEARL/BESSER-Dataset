from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tool_VariableContainer:

    pass
class description_AbstractVariable:

    pass
class table_description_TableVariable(description_AbstractVariable, tool_VariableContainer):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

class table_description_BackgroundConditionalStyle:

    def __init__(self, predicateExpression: str, table_description_BackgroundConditionalStyle: "BackgroundStyleDescription" = None):
        self.predicateExpression = predicateExpression
        self.table_description_BackgroundConditionalStyle = table_description_BackgroundConditionalStyle
        
    @property
    def predicateExpression(self) -> str:
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
            if hasattr(old_value, "BackgroundStyleDescription147"):
                opp_val = getattr(old_value, "BackgroundStyleDescription147", None)
                if opp_val == self:
                    setattr(old_value, "BackgroundStyleDescription147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BackgroundStyleDescription147"):
                opp_val = getattr(value, "BackgroundStyleDescription147", None)
                setattr(value, "BackgroundStyleDescription147", self)

class table_description_ForegroundConditionalStyle:

    def __init__(self, predicateExpression: str, table_description_ForegroundConditionalStyle: "ForegroundStyleDescription" = None):
        self.predicateExpression = predicateExpression
        self.table_description_ForegroundConditionalStyle = table_description_ForegroundConditionalStyle
        
    @property
    def predicateExpression(self) -> str:
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
            if hasattr(old_value, "ForegroundStyleDescription145"):
                opp_val = getattr(old_value, "ForegroundStyleDescription145", None)
                if opp_val == self:
                    setattr(old_value, "ForegroundStyleDescription145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForegroundStyleDescription145"):
                opp_val = getattr(value, "ForegroundStyleDescription145", None)
                setattr(value, "ForegroundStyleDescription145", self)

class RepresentationNavigationDescription:

    pass
class table_description_TableNavigationDescription(RepresentationNavigationDescription):

    pass
class RepresentationCreationDescription:

    pass
class table_description_TableCreationDescription(RepresentationCreationDescription):

    pass
class CreateTool:

    pass
class table_description_CreateLineTool(CreateTool):

    pass
class table_description_CreateCrossColumnTool(CreateTool):

    pass
class table_description_CreateColumnTool(CreateTool):

    pass
class description_TableTool:

    pass
class tool_AbstractToolDescription:

    pass
class table_description_CreateTool(description_TableTool, tool_AbstractToolDescription):

    pass
class tool_EditMaskVariables:

    pass
class TableTool:

    pass
class table_description_LabelEditTool(TableTool):

    pass
class table_description_BackgroundStyleDescription:

    pass
class ColorDescription:

    pass
class table_description_ForegroundStyleDescription:

    def __init__(self, labelSize: int, labelFormat: str, table_description_ForegroundStyleDescription: "ColorDescription" = None):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.table_description_ForegroundStyleDescription = table_description_ForegroundStyleDescription
        
    @property
    def labelFormat(self) -> str:
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat

    @property
    def labelSize(self) -> int:
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize

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
class table_description_DeleteTool(description_TableTool, tool_AbstractToolDescription):

    pass
class table_description_CreateCellTool(description_TableTool, tool_AbstractToolDescription):

    pass
class BackgroundConditionalStyle:

    pass
class BackgroundStyleDescription:

    pass
class tool_ModelOperation:

    pass
class ForegroundConditionalStyle:

    pass
class TableVariable:

    pass
class ForegroundStyleDescription:

    pass
class table_description_TableTool:

    pass
class table_description_StyleUpdater(ABC):

    pass
class CreateCellTool:

    pass
class description_CellUpdater:

    pass
class DeleteColumnTool:

    pass
class CreateColumnTool:

    pass
class description_ColumnMapping:

    pass
class LabelEditTool:

    pass
class table_description_CellUpdater:

    def __init__(self, canEdit: str, table_description_CellUpdater: "LabelEditTool" = None):
        self.canEdit = canEdit
        self.table_description_CellUpdater = table_description_CellUpdater
        
    @property
    def canEdit(self) -> str:
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

    def getLabelComputationExpression(self) -> str:
        # TODO: Implement getLabelComputationExpression method
        pass

    def getCreateCell(self) -> str:
        # TODO: Implement getCreateCell method
        pass

class description_StyleUpdater:

    pass
class table_description_ElementColumnMapping(description_ColumnMapping, description_StyleUpdater):

    def __init__(self, domainClass: str, semanticCandidatesExpression: str, CreateColumnTool: set["CreateColumnTool"] = None, DeleteColumnTool: "DeleteColumnTool" = None):
        self.domainClass = domainClass
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.CreateColumnTool = CreateColumnTool if CreateColumnTool is not None else set()
        self.DeleteColumnTool = DeleteColumnTool
        
    @property
    def semanticCandidatesExpression(self) -> str:
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression

    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def CreateColumnTool(self):
        return self.__CreateColumnTool

    @CreateColumnTool.setter
    def CreateColumnTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_ElementColumnMapping__CreateColumnTool", None)
        self.__CreateColumnTool = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description101"):
                    opp_val = getattr(item, "description101", None)
                    
                    if opp_val == self:
                        setattr(item, "description101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description101"):
                    opp_val = getattr(item, "description101", None)
                    
                    setattr(item, "description101", self)
                    

    @property
    def DeleteColumnTool(self):
        return self.__DeleteColumnTool

    @DeleteColumnTool.setter
    def DeleteColumnTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_ElementColumnMapping__DeleteColumnTool", None)
        self.__DeleteColumnTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description103"):
                opp_val = getattr(old_value, "description103", None)
                if opp_val == self:
                    setattr(old_value, "description103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description103"):
                opp_val = getattr(value, "description103", None)
                setattr(value, "description103", self)

class table_description_FeatureColumnMapping(description_ColumnMapping, description_CellUpdater, description_StyleUpdater):

    def __init__(self, featureName: str, labelExpression: str, featureParentExpression: str):
        self.featureName = featureName
        self.labelExpression = labelExpression
        self.featureParentExpression = featureParentExpression
        
    @property
    def featureParentExpression(self) -> str:
        return self.__featureParentExpression

    @featureParentExpression.setter
    def featureParentExpression(self, featureParentExpression: str):
        self.__featureParentExpression = featureParentExpression

    @property
    def labelExpression(self) -> str:
        return self.__labelExpression

    @labelExpression.setter
    def labelExpression(self, labelExpression: str):
        self.__labelExpression = labelExpression

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class description_TableMapping:

    pass
class table_description_IntersectionMapping(description_TableMapping, description_CellUpdater, description_StyleUpdater):

    def __init__(self, useDomainClass: bool, columnFinderExpression: str, lineFinderExpression: str, semanticCandidatesExpression: str, domainClass: str, preconditionExpression: str, labelExpression: str, CreateCellTool: "CreateCellTool" = None, table_description_IntersectionMapping: set["LineMapping"] = None, table_description_IntersectionMapping115: "ColumnMapping" = None):
        self.useDomainClass = useDomainClass
        self.columnFinderExpression = columnFinderExpression
        self.lineFinderExpression = lineFinderExpression
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.labelExpression = labelExpression
        self.CreateCellTool = CreateCellTool
        self.table_description_IntersectionMapping = table_description_IntersectionMapping if table_description_IntersectionMapping is not None else set()
        self.table_description_IntersectionMapping115 = table_description_IntersectionMapping115
        
    @property
    def lineFinderExpression(self) -> str:
        return self.__lineFinderExpression

    @lineFinderExpression.setter
    def lineFinderExpression(self, lineFinderExpression: str):
        self.__lineFinderExpression = lineFinderExpression

    @property
    def semanticCandidatesExpression(self) -> str:
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression

    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def columnFinderExpression(self) -> str:
        return self.__columnFinderExpression

    @columnFinderExpression.setter
    def columnFinderExpression(self, columnFinderExpression: str):
        self.__columnFinderExpression = columnFinderExpression

    @property
    def useDomainClass(self) -> bool:
        return self.__useDomainClass

    @useDomainClass.setter
    def useDomainClass(self, useDomainClass: bool):
        self.__useDomainClass = useDomainClass

    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

    @property
    def labelExpression(self) -> str:
        return self.__labelExpression

    @labelExpression.setter
    def labelExpression(self, labelExpression: str):
        self.__labelExpression = labelExpression

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
                if hasattr(item, "LineMapping113"):
                    opp_val = getattr(item, "LineMapping113", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping113"):
                    opp_val = getattr(item, "LineMapping113", None)
                    
                    setattr(item, "LineMapping113", self)
                    

    @property
    def CreateCellTool(self):
        return self.__CreateCellTool

    @CreateCellTool.setter
    def CreateCellTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_IntersectionMapping__CreateCellTool", None)
        self.__CreateCellTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description118"):
                opp_val = getattr(old_value, "description118", None)
                if opp_val == self:
                    setattr(old_value, "description118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description118"):
                opp_val = getattr(value, "description118", None)
                setattr(value, "description118", self)

    @property
    def table_description_IntersectionMapping115(self):
        return self.__table_description_IntersectionMapping115

    @table_description_IntersectionMapping115.setter
    def table_description_IntersectionMapping115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_IntersectionMapping__table_description_IntersectionMapping115", None)
        self.__table_description_IntersectionMapping115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnMapping116"):
                opp_val = getattr(old_value, "ColumnMapping116", None)
                if opp_val == self:
                    setattr(old_value, "ColumnMapping116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnMapping116"):
                opp_val = getattr(value, "ColumnMapping116", None)
                setattr(value, "ColumnMapping116", self)

class table_description_LineMapping(description_TableMapping, description_StyleUpdater):

    def __init__(self, domainClass: str, semanticCandidatesExpression: str, headerLabelExpression: str, table_description_LineMapping: set["LineMapping"] = None, LineMapping88: set["LineMapping"] = None, table_description_LineMapping90: set["LineMapping"] = None, LineMapping93: set["LineMapping"] = None, table_description_LineMapping96: set["CreateLineTool"] = None, DeleteLineTool: "DeleteLineTool" = None):
        self.domainClass = domainClass
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.headerLabelExpression = headerLabelExpression
        self.table_description_LineMapping = table_description_LineMapping if table_description_LineMapping is not None else set()
        self.LineMapping88 = LineMapping88 if LineMapping88 is not None else set()
        self.table_description_LineMapping90 = table_description_LineMapping90 if table_description_LineMapping90 is not None else set()
        self.LineMapping93 = LineMapping93 if LineMapping93 is not None else set()
        self.table_description_LineMapping96 = table_description_LineMapping96 if table_description_LineMapping96 is not None else set()
        self.DeleteLineTool = DeleteLineTool
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def semanticCandidatesExpression(self) -> str:
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression

    @property
    def headerLabelExpression(self) -> str:
        return self.__headerLabelExpression

    @headerLabelExpression.setter
    def headerLabelExpression(self, headerLabelExpression: str):
        self.__headerLabelExpression = headerLabelExpression

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
                if hasattr(item, "LineMapping86"):
                    opp_val = getattr(item, "LineMapping86", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping86"):
                    opp_val = getattr(item, "LineMapping86", None)
                    
                    setattr(item, "LineMapping86", self)
                    

    @property
    def LineMapping93(self):
        return self.__LineMapping93

    @LineMapping93.setter
    def LineMapping93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__LineMapping93", None)
        self.__LineMapping93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description94"):
                    opp_val = getattr(item, "description94", None)
                    
                    if opp_val == self:
                        setattr(item, "description94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description94"):
                    opp_val = getattr(item, "description94", None)
                    
                    setattr(item, "description94", self)
                    

    @property
    def LineMapping88(self):
        return self.__LineMapping88

    @LineMapping88.setter
    def LineMapping88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__LineMapping88", None)
        self.__LineMapping88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description"):
                    opp_val = getattr(item, "description", None)
                    
                    if opp_val == self:
                        setattr(item, "description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description"):
                    opp_val = getattr(item, "description", None)
                    
                    setattr(item, "description", self)
                    

    @property
    def table_description_LineMapping90(self):
        return self.__table_description_LineMapping90

    @table_description_LineMapping90.setter
    def table_description_LineMapping90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__table_description_LineMapping90", None)
        self.__table_description_LineMapping90 = value if value is not None else set()
        
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
                    

    @property
    def table_description_LineMapping96(self):
        return self.__table_description_LineMapping96

    @table_description_LineMapping96.setter
    def table_description_LineMapping96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__table_description_LineMapping96", None)
        self.__table_description_LineMapping96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CreateLineTool97"):
                    opp_val = getattr(item, "CreateLineTool97", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool97"):
                    opp_val = getattr(item, "CreateLineTool97", None)
                    
                    setattr(item, "CreateLineTool97", self)
                    

    @property
    def DeleteLineTool(self):
        return self.__DeleteLineTool

    @DeleteLineTool.setter
    def DeleteLineTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_LineMapping__DeleteLineTool", None)
        self.__DeleteLineTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description99"):
                opp_val = getattr(old_value, "description99", None)
                if opp_val == self:
                    setattr(old_value, "description99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description99"):
                opp_val = getattr(value, "description99", None)
                setattr(value, "description99", self)

class RepresentationElementMapping:

    pass
class table_description_TableMapping(RepresentationElementMapping):

    def __init__(self, semanticElements: str):
        self.semanticElements = semanticElements
        
    @property
    def semanticElements(self) -> str:
        return self.__semanticElements

    @semanticElements.setter
    def semanticElements(self, semanticElements: str):
        self.__semanticElements = semanticElements

class CreateCrossColumnTool:

    pass
class ElementColumnMapping:

    pass
class DeleteLineTool:

    pass
class CreateLineTool:

    pass
class FeatureColumnMapping:

    pass
class description_table_EObject:

    pass
class tool_RepresentationCreationDescription:

    pass
class description_EndUserDocumentedElement:

    pass
class description_DocumentedElement:

    pass
class description_RepresentationDescription:

    pass
class table_description_TableDescription(description_RepresentationDescription, description_DocumentedElement, description_EndUserDocumentedElement):

    def __init__(self, preconditionExpression: str, domainClass: str, initialHeaderColumnWidth: int, table_description_TableDescription40: set["tool_RepresentationCreationDescription"] = None, table_description_TableDescription43: set["tool_RepresentationCreationDescription"] = None, table_description_TableDescription46: set["tool_RepresentationNavigationDescription"] = None, table_description_TableDescription: set["tool_RepresentationCreationDescription"] = None, table_description_TableDescription63: set["CreateLineTool"] = None, table_description_TableDescription65: set["CreateLineTool"] = None, table_description_TableDescription68: set["CreateLineTool"] = None, table_description_TableDescription71: set["description_table_EObject"] = None, table_description_TableDescription48: set["tool_RepresentationNavigationDescription"] = None, table_description_TableDescription51: set["tool_RepresentationNavigationDescription"] = None, table_description_TableDescription54: set["LineMapping"] = None, table_description_TableDescription57: set["LineMapping"] = None, table_description_TableDescription60: set["LineMapping"] = None):
        self.preconditionExpression = preconditionExpression
        self.domainClass = domainClass
        self.initialHeaderColumnWidth = initialHeaderColumnWidth
        self.table_description_TableDescription40 = table_description_TableDescription40 if table_description_TableDescription40 is not None else set()
        self.table_description_TableDescription43 = table_description_TableDescription43 if table_description_TableDescription43 is not None else set()
        self.table_description_TableDescription46 = table_description_TableDescription46 if table_description_TableDescription46 is not None else set()
        self.table_description_TableDescription = table_description_TableDescription if table_description_TableDescription is not None else set()
        self.table_description_TableDescription63 = table_description_TableDescription63 if table_description_TableDescription63 is not None else set()
        self.table_description_TableDescription65 = table_description_TableDescription65 if table_description_TableDescription65 is not None else set()
        self.table_description_TableDescription68 = table_description_TableDescription68 if table_description_TableDescription68 is not None else set()
        self.table_description_TableDescription71 = table_description_TableDescription71 if table_description_TableDescription71 is not None else set()
        self.table_description_TableDescription48 = table_description_TableDescription48 if table_description_TableDescription48 is not None else set()
        self.table_description_TableDescription51 = table_description_TableDescription51 if table_description_TableDescription51 is not None else set()
        self.table_description_TableDescription54 = table_description_TableDescription54 if table_description_TableDescription54 is not None else set()
        self.table_description_TableDescription57 = table_description_TableDescription57 if table_description_TableDescription57 is not None else set()
        self.table_description_TableDescription60 = table_description_TableDescription60 if table_description_TableDescription60 is not None else set()
        
    @property
    def initialHeaderColumnWidth(self) -> int:
        return self.__initialHeaderColumnWidth

    @initialHeaderColumnWidth.setter
    def initialHeaderColumnWidth(self, initialHeaderColumnWidth: int):
        self.__initialHeaderColumnWidth = initialHeaderColumnWidth

    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def table_description_TableDescription54(self):
        return self.__table_description_TableDescription54

    @table_description_TableDescription54.setter
    def table_description_TableDescription54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription54", None)
        self.__table_description_TableDescription54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping55"):
                    opp_val = getattr(item, "LineMapping55", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping55"):
                    opp_val = getattr(item, "LineMapping55", None)
                    
                    setattr(item, "LineMapping55", self)
                    

    @property
    def table_description_TableDescription63(self):
        return self.__table_description_TableDescription63

    @table_description_TableDescription63.setter
    def table_description_TableDescription63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription63", None)
        self.__table_description_TableDescription63 = value if value is not None else set()
        
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
    def table_description_TableDescription46(self):
        return self.__table_description_TableDescription46

    @table_description_TableDescription46.setter
    def table_description_TableDescription46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription46", None)
        self.__table_description_TableDescription46 = value if value is not None else set()
        
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
    def table_description_TableDescription60(self):
        return self.__table_description_TableDescription60

    @table_description_TableDescription60.setter
    def table_description_TableDescription60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription60", None)
        self.__table_description_TableDescription60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping61"):
                    opp_val = getattr(item, "LineMapping61", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping61"):
                    opp_val = getattr(item, "LineMapping61", None)
                    
                    setattr(item, "LineMapping61", self)
                    

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
                if hasattr(item, "CreateLineTool69"):
                    opp_val = getattr(item, "CreateLineTool69", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool69"):
                    opp_val = getattr(item, "CreateLineTool69", None)
                    
                    setattr(item, "CreateLineTool69", self)
                    

    @property
    def table_description_TableDescription57(self):
        return self.__table_description_TableDescription57

    @table_description_TableDescription57.setter
    def table_description_TableDescription57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription57", None)
        self.__table_description_TableDescription57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineMapping58"):
                    opp_val = getattr(item, "LineMapping58", None)
                    
                    if opp_val == self:
                        setattr(item, "LineMapping58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineMapping58"):
                    opp_val = getattr(item, "LineMapping58", None)
                    
                    setattr(item, "LineMapping58", self)
                    

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
                if hasattr(item, "CreateLineTool66"):
                    opp_val = getattr(item, "CreateLineTool66", None)
                    
                    if opp_val == self:
                        setattr(item, "CreateLineTool66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CreateLineTool66"):
                    opp_val = getattr(item, "CreateLineTool66", None)
                    
                    setattr(item, "CreateLineTool66", self)
                    

    @property
    def table_description_TableDescription40(self):
        return self.__table_description_TableDescription40

    @table_description_TableDescription40.setter
    def table_description_TableDescription40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription40", None)
        self.__table_description_TableDescription40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationCreationDescription41"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription41", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationCreationDescription41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationCreationDescription41"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription41", None)
                    
                    setattr(item, "tool_RepresentationCreationDescription41", self)
                    

    @property
    def table_description_TableDescription71(self):
        return self.__table_description_TableDescription71

    @table_description_TableDescription71.setter
    def table_description_TableDescription71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription71", None)
        self.__table_description_TableDescription71 = value if value is not None else set()
        
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
    def table_description_TableDescription43(self):
        return self.__table_description_TableDescription43

    @table_description_TableDescription43.setter
    def table_description_TableDescription43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_description_TableDescription__table_description_TableDescription43", None)
        self.__table_description_TableDescription43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationCreationDescription44"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription44", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationCreationDescription44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationCreationDescription44"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription44", None)
                    
                    setattr(item, "tool_RepresentationCreationDescription44", self)
                    

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
                if hasattr(item, "tool_RepresentationNavigationDescription52"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription52", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationNavigationDescription52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationNavigationDescription52"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription52", None)
                    
                    setattr(item, "tool_RepresentationNavigationDescription52", self)
                    

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
                if hasattr(item, "tool_RepresentationNavigationDescription49"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription49", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationNavigationDescription49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationNavigationDescription49"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription49", None)
                    
                    setattr(item, "tool_RepresentationNavigationDescription49", self)
                    

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
                    

class tool_RepresentationNavigationDescription:

    pass
class DColumn:

    pass
class table_DFeatureColumn(DColumn):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
    @property
    def featureName(self) -> str:
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

    def __init__(self, labelSize: int, labelFormat: str, defaultForegroundStyle: bool, defaultBackgroundStyle: bool, foregroundColor: str, backgroundColor: str, table_DTableElementStyle: "table_DLine" = None, table_DTableElementStyle37: "table_DColumn" = None):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.defaultForegroundStyle = defaultForegroundStyle
        self.defaultBackgroundStyle = defaultBackgroundStyle
        self.foregroundColor = foregroundColor
        self.backgroundColor = backgroundColor
        self.table_DTableElementStyle = table_DTableElementStyle
        self.table_DTableElementStyle37 = table_DTableElementStyle37
        
    @property
    def foregroundColor(self) -> str:
        return self.__foregroundColor

    @foregroundColor.setter
    def foregroundColor(self, foregroundColor: str):
        self.__foregroundColor = foregroundColor

    @property
    def labelSize(self) -> int:
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def defaultForegroundStyle(self) -> bool:
        return self.__defaultForegroundStyle

    @defaultForegroundStyle.setter
    def defaultForegroundStyle(self, defaultForegroundStyle: bool):
        self.__defaultForegroundStyle = defaultForegroundStyle

    @property
    def defaultBackgroundStyle(self) -> bool:
        return self.__defaultBackgroundStyle

    @defaultBackgroundStyle.setter
    def defaultBackgroundStyle(self, defaultBackgroundStyle: bool):
        self.__defaultBackgroundStyle = defaultBackgroundStyle

    @property
    def labelFormat(self) -> str:
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat

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

class LineMapping:

    pass
class DTableElement:

    pass
class DSemanticDecorator:

    pass
class table_DTargetColumn(DSemanticDecorator, DColumn):

    pass
class table_DCell(DSemanticDecorator, DTableElement):

    def __init__(self, label: str, table_DCell17: "table_DCellStyle" = None, DCell: "table_DLine" = None, table_DCell: "table_DLine" = None, cells: "table_DLine" = None, cells14: "table_DColumn" = None, table_DCell19: "CellUpdater" = None, table_DCell21: "IntersectionMapping" = None, DCell29: "table_DColumn" = None, table_DCell34: "table_DColumn" = None):
        self.label = label
        self.table_DCell17 = table_DCell17
        self.DCell = DCell
        self.table_DCell = table_DCell
        self.cells = cells
        self.cells14 = cells14
        self.table_DCell19 = table_DCell19
        self.table_DCell21 = table_DCell21
        self.DCell29 = DCell29
        self.table_DCell34 = table_DCell34
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

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

class table_LineContainer(DSemanticDecorator):

    pass
class TableMapping:

    pass
class table_description_ColumnMapping(TableMapping):

    def __init__(self, headerLabelExpression: str, initialWidth: int, TableMapping: "table_DTableElement", TableMapping27: "table_DCellStyle", TableMapping24: "table_DCellStyle"):
        self.headerLabelExpression = headerLabelExpression
        self.initialWidth = initialWidth
        
    @property
    def initialWidth(self) -> int:
        return self.__initialWidth

    @initialWidth.setter
    def initialWidth(self, initialWidth: int):
        self.__initialWidth = initialWidth

    @property
    def headerLabelExpression(self) -> str:
        return self.__headerLabelExpression

    @headerLabelExpression.setter
    def headerLabelExpression(self, headerLabelExpression: str):
        self.__headerLabelExpression = headerLabelExpression

class DRepresentationElement:

    pass
class table_DTableElement(DRepresentationElement):

    pass
class table_DColumn(DTableElement):

    def __init__(self, label: str, visible: bool, width: int, DColumn: "table_DTable" = None, DColumn15: "table_DCell" = None, column: set["table_DCell"] = None, table_DColumn: "ColumnMapping" = None, columns: "table_DTable" = None, table_DColumn33: set["table_DCell"] = None, table_DColumn36: "table_DTableElementStyle" = None):
        self.label = label
        self.visible = visible
        self.width = width
        self.DColumn = DColumn
        self.DColumn15 = DColumn15
        self.column = column if column is not None else set()
        self.table_DColumn = table_DColumn
        self.columns = columns
        self.table_DColumn33 = table_DColumn33 if table_DColumn33 is not None else set()
        self.table_DColumn36 = table_DColumn36
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

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

class LineContainer:

    pass
class table_DLine(LineContainer, DTableElement):

    def __init__(self, label: str, visible: bool, collapsed: bool, DLine: "table_LineContainer" = None, table_DLine: "LineMapping" = None, line: set["table_DCell"] = None, lines: "table_LineContainer" = None, table_DLine8: set["table_DCell"] = None, table_DLine10: "table_DTableElementStyle" = None, DLine12: "table_DCell" = None):
        self.label = label
        self.visible = visible
        self.collapsed = collapsed
        self.DLine = DLine
        self.table_DLine = table_DLine
        self.line = line if line is not None else set()
        self.lines = lines
        self.table_DLine8 = table_DLine8 if table_DLine8 is not None else set()
        self.table_DLine10 = table_DLine10
        self.DLine12 = DLine12
        
    @property
    def collapsed(self) -> bool:
        return self.__collapsed

    @collapsed.setter
    def collapsed(self, collapsed: bool):
        self.__collapsed = collapsed

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

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
                    

class DRepresentation:

    pass
class table_DTable(LineContainer, DRepresentation):

    def __init__(self, headerColumnWidth: int, table: set["table_DColumn"] = None, table_DTable: "TableDescription" = None, DTable: "table_DColumn" = None):
        self.headerColumnWidth = headerColumnWidth
        self.table = table if table is not None else set()
        self.table_DTable = table_DTable
        self.DTable = DTable
        
    @property
    def headerColumnWidth(self) -> int:
        return self.__headerColumnWidth

    @headerColumnWidth.setter
    def headerColumnWidth(self, headerColumnWidth: int):
        self.__headerColumnWidth = headerColumnWidth

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

class TableDescription:

    pass
class table_description_CrossTableDescription(TableDescription):

    pass
class table_description_EditionTableDescription(TableDescription):

    pass