from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LabelPosition(Enum):
    Left = "Left"
    Right = "Right"
    Up = "Up"
    Down = "Down"
class FileWidgetInputType(Enum):
    Document = "Document"
    URL = "URL"
    Resource = "Resource"
class FileWidgetDownloadType(Enum):
    Both = "Both"
    URL = "URL"
    Browse = "Browse"
class EventDependencyType(Enum):
    onValueChange = "onValueChange"
    onChange = "onChange"
    onBlur = "onBlur"
    onClick = "onClick"


############################################
# Definition of Classes
############################################

class AbstractTable:

    pass
class form_TableExpression:

    pass
class form_Document:

    pass
class SingleValuatedFormField:

    pass
class form_CheckBoxSingleFormField(SingleValuatedFormField):

    pass
class form_PasswordFormField(SingleValuatedFormField):

    def __init__(self, maxLength: int):
        self.maxLength = maxLength
        
        pass
    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength


class form_DynamicTable(AbstractTable, SingleValuatedFormField):

    def __init__(self, limitMinNumberOfColumn: bool, limitMinNumberOfRow: bool, allowAddRemoveRow: bool, allowAddRemoveColumn: bool, limitMaxNumberOfColumn: bool, limitMaxNumberOfRow: bool, form_DynamicTable: "form_Expression" = None, form_DynamicTable120: "form_Expression" = None, form_DynamicTable123: "form_Expression" = None, form_DynamicTable126: "form_Expression" = None):
        self.limitMinNumberOfColumn = limitMinNumberOfColumn
        self.limitMinNumberOfRow = limitMinNumberOfRow
        self.allowAddRemoveRow = allowAddRemoveRow
        self.allowAddRemoveColumn = allowAddRemoveColumn
        self.limitMaxNumberOfColumn = limitMaxNumberOfColumn
        self.limitMaxNumberOfRow = limitMaxNumberOfRow
        self.form_DynamicTable = form_DynamicTable
        self.form_DynamicTable120 = form_DynamicTable120
        self.form_DynamicTable123 = form_DynamicTable123
        self.form_DynamicTable126 = form_DynamicTable126
        
        pass
    @property
    def allowAddRemoveColumn(self):
        return self.__allowAddRemoveColumn

    @allowAddRemoveColumn.setter
    def allowAddRemoveColumn(self, allowAddRemoveColumn: bool):
        self.__allowAddRemoveColumn = allowAddRemoveColumn


    @property
    def limitMaxNumberOfColumn(self):
        return self.__limitMaxNumberOfColumn

    @limitMaxNumberOfColumn.setter
    def limitMaxNumberOfColumn(self, limitMaxNumberOfColumn: bool):
        self.__limitMaxNumberOfColumn = limitMaxNumberOfColumn


    @property
    def limitMinNumberOfRow(self):
        return self.__limitMinNumberOfRow

    @limitMinNumberOfRow.setter
    def limitMinNumberOfRow(self, limitMinNumberOfRow: bool):
        self.__limitMinNumberOfRow = limitMinNumberOfRow


    @property
    def limitMaxNumberOfRow(self):
        return self.__limitMaxNumberOfRow

    @limitMaxNumberOfRow.setter
    def limitMaxNumberOfRow(self, limitMaxNumberOfRow: bool):
        self.__limitMaxNumberOfRow = limitMaxNumberOfRow


    @property
    def limitMinNumberOfColumn(self):
        return self.__limitMinNumberOfColumn

    @limitMinNumberOfColumn.setter
    def limitMinNumberOfColumn(self, limitMinNumberOfColumn: bool):
        self.__limitMinNumberOfColumn = limitMinNumberOfColumn


    @property
    def allowAddRemoveRow(self):
        return self.__allowAddRemoveRow

    @allowAddRemoveRow.setter
    def allowAddRemoveRow(self, allowAddRemoveRow: bool):
        self.__allowAddRemoveRow = allowAddRemoveRow


    @property
    def form_DynamicTable123(self):
        return self.__form_DynamicTable123

    @form_DynamicTable123.setter
    def form_DynamicTable123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_DynamicTable__form_DynamicTable123", None)
        self.__form_DynamicTable123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression124"):
                opp_val = getattr(old_value, "form_Expression124", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression124"):
                opp_val = getattr(value, "form_Expression124", None)
                setattr(value, "form_Expression124", self)

    @property
    def form_DynamicTable126(self):
        return self.__form_DynamicTable126

    @form_DynamicTable126.setter
    def form_DynamicTable126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_DynamicTable__form_DynamicTable126", None)
        self.__form_DynamicTable126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression127"):
                opp_val = getattr(old_value, "form_Expression127", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression127"):
                opp_val = getattr(value, "form_Expression127", None)
                setattr(value, "form_Expression127", self)

    @property
    def form_DynamicTable(self):
        return self.__form_DynamicTable

    @form_DynamicTable.setter
    def form_DynamicTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_DynamicTable__form_DynamicTable", None)
        self.__form_DynamicTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression118"):
                opp_val = getattr(old_value, "form_Expression118", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression118"):
                opp_val = getattr(value, "form_Expression118", None)
                setattr(value, "form_Expression118", self)

    @property
    def form_DynamicTable120(self):
        return self.__form_DynamicTable120

    @form_DynamicTable120.setter
    def form_DynamicTable120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_DynamicTable__form_DynamicTable120", None)
        self.__form_DynamicTable120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression121"):
                opp_val = getattr(old_value, "form_Expression121", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression121"):
                opp_val = getattr(value, "form_Expression121", None)
                setattr(value, "form_Expression121", self)

class form_DateFormField(SingleValuatedFormField):

    def __init__(self, initialFormat: str, displayFormat: str):
        self.initialFormat = initialFormat
        self.displayFormat = displayFormat
        
        pass
    @property
    def displayFormat(self):
        return self.__displayFormat

    @displayFormat.setter
    def displayFormat(self, displayFormat: str):
        self.__displayFormat = displayFormat


    @property
    def initialFormat(self):
        return self.__initialFormat

    @initialFormat.setter
    def initialFormat(self, initialFormat: str):
        self.__initialFormat = initialFormat


class ItemContainer:

    pass
class form_DurationFormField(ItemContainer, SingleValuatedFormField):

    def __init__(self, day: str, hour: str, min: str, sec: str):
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec
        
        pass
    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def sec(self):
        return self.__sec

    @sec.setter
    def sec(self, sec: str):
        self.__sec = sec


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min


class MultipleValuatedFormField:

    pass
class form_SuggestBox(MultipleValuatedFormField):

    def __init__(self, maxItems: int, useMaxItems: bool, asynchronous: bool, delay: int):
        self.maxItems = maxItems
        self.useMaxItems = useMaxItems
        self.asynchronous = asynchronous
        self.delay = delay
        
        pass
    @property
    def useMaxItems(self):
        return self.__useMaxItems

    @useMaxItems.setter
    def useMaxItems(self, useMaxItems: bool):
        self.__useMaxItems = useMaxItems


    @property
    def asynchronous(self):
        return self.__asynchronous

    @asynchronous.setter
    def asynchronous(self, asynchronous: bool):
        self.__asynchronous = asynchronous


    @property
    def maxItems(self):
        return self.__maxItems

    @maxItems.setter
    def maxItems(self, maxItems: int):
        self.__maxItems = maxItems


    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: int):
        self.__delay = delay


class form_ListFormField(MultipleValuatedFormField):

    def __init__(self, maxHeigth: int):
        self.maxHeigth = maxHeigth
        
        pass
    @property
    def maxHeigth(self):
        return self.__maxHeigth

    @maxHeigth.setter
    def maxHeigth(self, maxHeigth: int):
        self.__maxHeigth = maxHeigth


class form_ComboFormField(MultipleValuatedFormField):

    pass
class form_Table(AbstractTable, MultipleValuatedFormField):

    def __init__(self, usePagination: bool, allowSelection: bool, selectionModeIsMultiple: bool, form_Table115: "form_Expression" = None, form_Table: "form_Expression" = None, form_Table112: "form_Expression" = None):
        self.usePagination = usePagination
        self.allowSelection = allowSelection
        self.selectionModeIsMultiple = selectionModeIsMultiple
        self.form_Table115 = form_Table115
        self.form_Table = form_Table
        self.form_Table112 = form_Table112
        
        pass
    @property
    def allowSelection(self):
        return self.__allowSelection

    @allowSelection.setter
    def allowSelection(self, allowSelection: bool):
        self.__allowSelection = allowSelection


    @property
    def usePagination(self):
        return self.__usePagination

    @usePagination.setter
    def usePagination(self, usePagination: bool):
        self.__usePagination = usePagination


    @property
    def selectionModeIsMultiple(self):
        return self.__selectionModeIsMultiple

    @selectionModeIsMultiple.setter
    def selectionModeIsMultiple(self, selectionModeIsMultiple: bool):
        self.__selectionModeIsMultiple = selectionModeIsMultiple


    @property
    def form_Table112(self):
        return self.__form_Table112

    @form_Table112.setter
    def form_Table112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Table__form_Table112", None)
        self.__form_Table112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression113"):
                opp_val = getattr(old_value, "form_Expression113", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression113"):
                opp_val = getattr(value, "form_Expression113", None)
                setattr(value, "form_Expression113", self)

    @property
    def form_Table115(self):
        return self.__form_Table115

    @form_Table115.setter
    def form_Table115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Table__form_Table115", None)
        self.__form_Table115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression116"):
                opp_val = getattr(old_value, "form_Expression116", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression116"):
                opp_val = getattr(value, "form_Expression116", None)
                setattr(value, "form_Expression116", self)

    @property
    def form_Table(self):
        return self.__form_Table

    @form_Table.setter
    def form_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Table__form_Table", None)
        self.__form_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression110"):
                opp_val = getattr(old_value, "form_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression110"):
                opp_val = getattr(value, "form_Expression110", None)
                setattr(value, "form_Expression110", self)

class form_CheckBoxMultipleFormField(ItemContainer, MultipleValuatedFormField):

    pass
class Info:

    pass
class form_MessageInfo(Info):

    pass
class form_HtmlWidget(Info):

    pass
class form_IFrameWidget(Info):

    pass
class FormButton:

    pass
class form_NextFormButton(FormButton):

    pass
class form_PreviousFormButton(FormButton):

    pass
class form_RichTextAreaFormField(SingleValuatedFormField):

    pass
class form_TextAreaFormField(SingleValuatedFormField):

    def __init__(self, maxLength: int, maxHeigth: int):
        self.maxLength = maxLength
        self.maxHeigth = maxHeigth
        
        pass
    @property
    def maxHeigth(self):
        return self.__maxHeigth

    @maxHeigth.setter
    def maxHeigth(self, maxHeigth: int):
        self.__maxHeigth = maxHeigth


    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength


class form_TextFormField(SingleValuatedFormField):

    def __init__(self, maxLength: int):
        self.maxLength = maxLength
        
        pass
    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength


class form_SelectFormField(MultipleValuatedFormField):

    pass
class form_RadioFormField(ItemContainer, MultipleValuatedFormField):

    pass
class FormField:

    pass
class form_SingleValuatedFormField(FormField):

    pass
class form_MultipleValuatedFormField(FormField):

    pass
class Duplicable:

    pass
class form_FileWidget(Duplicable, SingleValuatedFormField):

    def __init__(self, inputType: str, downloadType: str, downloadOnly: bool, usePreview: bool, initialResourcePath: str, outputDocumentName: str, updateDocument: bool, intialResourceList: str, form_FileWidget: "form_Document" = None, form_FileWidget95: "form_Expression" = None):
        self.inputType = inputType
        self.downloadType = downloadType
        self.downloadOnly = downloadOnly
        self.usePreview = usePreview
        self.initialResourcePath = initialResourcePath
        self.outputDocumentName = outputDocumentName
        self.updateDocument = updateDocument
        self.intialResourceList = intialResourceList
        self.form_FileWidget = form_FileWidget
        self.form_FileWidget95 = form_FileWidget95
        
        pass
    @property
    def downloadType(self):
        return self.__downloadType

    @downloadType.setter
    def downloadType(self, downloadType: str):
        self.__downloadType = downloadType


    @property
    def initialResourcePath(self):
        return self.__initialResourcePath

    @initialResourcePath.setter
    def initialResourcePath(self, initialResourcePath: str):
        self.__initialResourcePath = initialResourcePath


    @property
    def updateDocument(self):
        return self.__updateDocument

    @updateDocument.setter
    def updateDocument(self, updateDocument: bool):
        self.__updateDocument = updateDocument


    @property
    def downloadOnly(self):
        return self.__downloadOnly

    @downloadOnly.setter
    def downloadOnly(self, downloadOnly: bool):
        self.__downloadOnly = downloadOnly


    @property
    def usePreview(self):
        return self.__usePreview

    @usePreview.setter
    def usePreview(self, usePreview: bool):
        self.__usePreview = usePreview


    @property
    def outputDocumentName(self):
        return self.__outputDocumentName

    @outputDocumentName.setter
    def outputDocumentName(self, outputDocumentName: str):
        self.__outputDocumentName = outputDocumentName


    @property
    def inputType(self):
        return self.__inputType

    @inputType.setter
    def inputType(self, inputType: str):
        self.__inputType = inputType


    @property
    def intialResourceList(self):
        return self.__intialResourceList

    @intialResourceList.setter
    def intialResourceList(self, intialResourceList: str):
        self.__intialResourceList = intialResourceList


    @property
    def form_FileWidget(self):
        return self.__form_FileWidget

    @form_FileWidget.setter
    def form_FileWidget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_FileWidget__form_FileWidget", None)
        self.__form_FileWidget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Document"):
                opp_val = getattr(old_value, "form_Document", None)
                if opp_val == self:
                    setattr(old_value, "form_Document", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Document"):
                opp_val = getattr(value, "form_Document", None)
                setattr(value, "form_Document", self)

    @property
    def form_FileWidget95(self):
        return self.__form_FileWidget95

    @form_FileWidget95.setter
    def form_FileWidget95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_FileWidget__form_FileWidget95", None)
        self.__form_FileWidget95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression96"):
                opp_val = getattr(old_value, "form_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression96"):
                opp_val = getattr(value, "form_Expression96", None)
                setattr(value, "form_Expression96", self)

class form_HiddenWidget(Duplicable, SingleValuatedFormField):

    pass
class form_TextInfo(Duplicable, Info):

    pass
class Widget:

    pass
class form_AbstractTable(Duplicable, Widget):

    def __init__(self, leftColumnIsHeader: bool, rightColumnIsHeader: bool, firstRowIsHeader: bool, LastRowIsHeader: bool, initializedUsingCells: bool, useHorizontalHeader: bool, useVerticalHeader: bool, form_AbstractTable: "form_Expression" = None, form_AbstractTable105: "form_Expression" = None, form_AbstractTable108: "form_TableExpression" = None):
        self.leftColumnIsHeader = leftColumnIsHeader
        self.rightColumnIsHeader = rightColumnIsHeader
        self.firstRowIsHeader = firstRowIsHeader
        self.LastRowIsHeader = LastRowIsHeader
        self.initializedUsingCells = initializedUsingCells
        self.useHorizontalHeader = useHorizontalHeader
        self.useVerticalHeader = useVerticalHeader
        self.form_AbstractTable = form_AbstractTable
        self.form_AbstractTable105 = form_AbstractTable105
        self.form_AbstractTable108 = form_AbstractTable108
        
        pass
    @property
    def useVerticalHeader(self):
        return self.__useVerticalHeader

    @useVerticalHeader.setter
    def useVerticalHeader(self, useVerticalHeader: bool):
        self.__useVerticalHeader = useVerticalHeader


    @property
    def LastRowIsHeader(self):
        return self.__LastRowIsHeader

    @LastRowIsHeader.setter
    def LastRowIsHeader(self, LastRowIsHeader: bool):
        self.__LastRowIsHeader = LastRowIsHeader


    @property
    def firstRowIsHeader(self):
        return self.__firstRowIsHeader

    @firstRowIsHeader.setter
    def firstRowIsHeader(self, firstRowIsHeader: bool):
        self.__firstRowIsHeader = firstRowIsHeader


    @property
    def rightColumnIsHeader(self):
        return self.__rightColumnIsHeader

    @rightColumnIsHeader.setter
    def rightColumnIsHeader(self, rightColumnIsHeader: bool):
        self.__rightColumnIsHeader = rightColumnIsHeader


    @property
    def useHorizontalHeader(self):
        return self.__useHorizontalHeader

    @useHorizontalHeader.setter
    def useHorizontalHeader(self, useHorizontalHeader: bool):
        self.__useHorizontalHeader = useHorizontalHeader


    @property
    def initializedUsingCells(self):
        return self.__initializedUsingCells

    @initializedUsingCells.setter
    def initializedUsingCells(self, initializedUsingCells: bool):
        self.__initializedUsingCells = initializedUsingCells


    @property
    def leftColumnIsHeader(self):
        return self.__leftColumnIsHeader

    @leftColumnIsHeader.setter
    def leftColumnIsHeader(self, leftColumnIsHeader: bool):
        self.__leftColumnIsHeader = leftColumnIsHeader


    @property
    def form_AbstractTable105(self):
        return self.__form_AbstractTable105

    @form_AbstractTable105.setter
    def form_AbstractTable105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_AbstractTable__form_AbstractTable105", None)
        self.__form_AbstractTable105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression106"):
                opp_val = getattr(old_value, "form_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression106"):
                opp_val = getattr(value, "form_Expression106", None)
                setattr(value, "form_Expression106", self)

    @property
    def form_AbstractTable(self):
        return self.__form_AbstractTable

    @form_AbstractTable.setter
    def form_AbstractTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_AbstractTable__form_AbstractTable", None)
        self.__form_AbstractTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression103"):
                opp_val = getattr(old_value, "form_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression103"):
                opp_val = getattr(value, "form_Expression103", None)
                setattr(value, "form_Expression103", self)

    @property
    def form_AbstractTable108(self):
        return self.__form_AbstractTable108

    @form_AbstractTable108.setter
    def form_AbstractTable108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_AbstractTable__form_AbstractTable108", None)
        self.__form_AbstractTable108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_TableExpression"):
                opp_val = getattr(old_value, "form_TableExpression", None)
                if opp_val == self:
                    setattr(old_value, "form_TableExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_TableExpression"):
                opp_val = getattr(value, "form_TableExpression", None)
                setattr(value, "form_TableExpression", self)

class form_Info(Widget):

    pass
class form_ImageWidget(Duplicable, Widget):

    def __init__(self, isADocument: bool, form_ImageWidget: "form_Document" = None, form_ImageWidget100: "form_Expression" = None):
        self.isADocument = isADocument
        self.form_ImageWidget = form_ImageWidget
        self.form_ImageWidget100 = form_ImageWidget100
        
        pass
    @property
    def isADocument(self):
        return self.__isADocument

    @isADocument.setter
    def isADocument(self, isADocument: bool):
        self.__isADocument = isADocument


    @property
    def form_ImageWidget100(self):
        return self.__form_ImageWidget100

    @form_ImageWidget100.setter
    def form_ImageWidget100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_ImageWidget__form_ImageWidget100", None)
        self.__form_ImageWidget100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression101"):
                opp_val = getattr(old_value, "form_Expression101", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression101"):
                opp_val = getattr(value, "form_Expression101", None)
                setattr(value, "form_Expression101", self)

    @property
    def form_ImageWidget(self):
        return self.__form_ImageWidget

    @form_ImageWidget.setter
    def form_ImageWidget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_ImageWidget__form_ImageWidget", None)
        self.__form_ImageWidget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Document98"):
                opp_val = getattr(old_value, "form_Document98", None)
                if opp_val == self:
                    setattr(old_value, "form_Document98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Document98"):
                opp_val = getattr(value, "form_Document98", None)
                setattr(value, "form_Document98", self)

class form_FormButton(Widget):

    def __init__(self, labelBehavior: str):
        self.labelBehavior = labelBehavior
        
        pass
    @property
    def labelBehavior(self):
        return self.__labelBehavior

    @labelBehavior.setter
    def labelBehavior(self, labelBehavior: str):
        self.__labelBehavior = labelBehavior


class form_Group(Duplicable, Widget):

    def __init__(self, showBorder: bool, useIterator: bool, form_Group: set["form_Widget"] = None, form_Group77: set["form_Column"] = None, form_Group80: set["form_Line"] = None, form_Group83: "form_GroupIterator" = None):
        self.showBorder = showBorder
        self.useIterator = useIterator
        self.form_Group = form_Group if form_Group is not None else set()
        self.form_Group77 = form_Group77 if form_Group77 is not None else set()
        self.form_Group80 = form_Group80 if form_Group80 is not None else set()
        self.form_Group83 = form_Group83
        
        pass
    @property
    def useIterator(self):
        return self.__useIterator

    @useIterator.setter
    def useIterator(self, useIterator: bool):
        self.__useIterator = useIterator


    @property
    def showBorder(self):
        return self.__showBorder

    @showBorder.setter
    def showBorder(self, showBorder: bool):
        self.__showBorder = showBorder


    @property
    def form_Group80(self):
        return self.__form_Group80

    @form_Group80.setter
    def form_Group80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Group__form_Group80", None)
        self.__form_Group80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Line81"):
                    opp_val = getattr(item, "form_Line81", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Line81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Line81"):
                    opp_val = getattr(item, "form_Line81", None)
                    
                    setattr(item, "form_Line81", self)
                    

    @property
    def form_Group77(self):
        return self.__form_Group77

    @form_Group77.setter
    def form_Group77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Group__form_Group77", None)
        self.__form_Group77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Column78"):
                    opp_val = getattr(item, "form_Column78", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Column78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Column78"):
                    opp_val = getattr(item, "form_Column78", None)
                    
                    setattr(item, "form_Column78", self)
                    

    @property
    def form_Group83(self):
        return self.__form_Group83

    @form_Group83.setter
    def form_Group83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Group__form_Group83", None)
        self.__form_Group83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_GroupIterator"):
                opp_val = getattr(old_value, "form_GroupIterator", None)
                if opp_val == self:
                    setattr(old_value, "form_GroupIterator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_GroupIterator"):
                opp_val = getattr(value, "form_GroupIterator", None)
                setattr(value, "form_GroupIterator", self)

    @property
    def form_Group(self):
        return self.__form_Group

    @form_Group.setter
    def form_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Group__form_Group", None)
        self.__form_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Widget75"):
                    opp_val = getattr(item, "form_Widget75", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Widget75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Widget75"):
                    opp_val = getattr(item, "form_Widget75", None)
                    
                    setattr(item, "form_Widget75", self)
                    

class form_CSSCustomizable(ABC):

    pass
class Form:

    pass
class form_ViewForm(Form):

    pass
class CSSCustomizable:

    pass
class form_MandatoryFieldsCustomization(CSSCustomizable):

    pass
class Element:

    pass
class form_GroupIterator(Element):

    def __init__(self, className: str, form_GroupIterator: "form_Group" = None):
        self.className = className
        self.form_GroupIterator = form_GroupIterator
        
        pass
    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def form_GroupIterator(self):
        return self.__form_GroupIterator

    @form_GroupIterator.setter
    def form_GroupIterator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_GroupIterator__form_GroupIterator", None)
        self.__form_GroupIterator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Group83"):
                opp_val = getattr(old_value, "form_Group83", None)
                if opp_val == self:
                    setattr(old_value, "form_Group83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Group83"):
                opp_val = getattr(value, "form_Group83", None)
                setattr(value, "form_Group83", self)

class form_Duplicable(ABC):

    def __init__(self, duplicate: bool, limitNumberOfDuplication: bool, limitMinNumberOfDuplication: bool, form_Duplicable: "form_Expression" = None, form_Duplicable23: "form_Expression" = None, form_Duplicable26: "form_Expression" = None, form_Duplicable29: "form_Expression" = None, form_Duplicable32: "form_Expression" = None, form_Duplicable35: "form_Expression" = None):
        self.duplicate = duplicate
        self.limitNumberOfDuplication = limitNumberOfDuplication
        self.limitMinNumberOfDuplication = limitMinNumberOfDuplication
        self.form_Duplicable = form_Duplicable
        self.form_Duplicable23 = form_Duplicable23
        self.form_Duplicable26 = form_Duplicable26
        self.form_Duplicable29 = form_Duplicable29
        self.form_Duplicable32 = form_Duplicable32
        self.form_Duplicable35 = form_Duplicable35
        
        pass
    @property
    def limitMinNumberOfDuplication(self):
        return self.__limitMinNumberOfDuplication

    @limitMinNumberOfDuplication.setter
    def limitMinNumberOfDuplication(self, limitMinNumberOfDuplication: bool):
        self.__limitMinNumberOfDuplication = limitMinNumberOfDuplication


    @property
    def duplicate(self):
        return self.__duplicate

    @duplicate.setter
    def duplicate(self, duplicate: bool):
        self.__duplicate = duplicate


    @property
    def limitNumberOfDuplication(self):
        return self.__limitNumberOfDuplication

    @limitNumberOfDuplication.setter
    def limitNumberOfDuplication(self, limitNumberOfDuplication: bool):
        self.__limitNumberOfDuplication = limitNumberOfDuplication


    @property
    def form_Duplicable35(self):
        return self.__form_Duplicable35

    @form_Duplicable35.setter
    def form_Duplicable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Duplicable__form_Duplicable35", None)
        self.__form_Duplicable35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression36"):
                opp_val = getattr(old_value, "form_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression36"):
                opp_val = getattr(value, "form_Expression36", None)
                setattr(value, "form_Expression36", self)

    @property
    def form_Duplicable23(self):
        return self.__form_Duplicable23

    @form_Duplicable23.setter
    def form_Duplicable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Duplicable__form_Duplicable23", None)
        self.__form_Duplicable23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression24"):
                opp_val = getattr(old_value, "form_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression24"):
                opp_val = getattr(value, "form_Expression24", None)
                setattr(value, "form_Expression24", self)

    @property
    def form_Duplicable32(self):
        return self.__form_Duplicable32

    @form_Duplicable32.setter
    def form_Duplicable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Duplicable__form_Duplicable32", None)
        self.__form_Duplicable32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression33"):
                opp_val = getattr(old_value, "form_Expression33", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression33"):
                opp_val = getattr(value, "form_Expression33", None)
                setattr(value, "form_Expression33", self)

    @property
    def form_Duplicable29(self):
        return self.__form_Duplicable29

    @form_Duplicable29.setter
    def form_Duplicable29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Duplicable__form_Duplicable29", None)
        self.__form_Duplicable29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression30"):
                opp_val = getattr(old_value, "form_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression30"):
                opp_val = getattr(value, "form_Expression30", None)
                setattr(value, "form_Expression30", self)

    @property
    def form_Duplicable(self):
        return self.__form_Duplicable

    @form_Duplicable.setter
    def form_Duplicable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Duplicable__form_Duplicable", None)
        self.__form_Duplicable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression21"):
                opp_val = getattr(old_value, "form_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression21"):
                opp_val = getattr(value, "form_Expression21", None)
                setattr(value, "form_Expression21", self)

    @property
    def form_Duplicable26(self):
        return self.__form_Duplicable26

    @form_Duplicable26.setter
    def form_Duplicable26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Duplicable__form_Duplicable26", None)
        self.__form_Duplicable26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression27"):
                opp_val = getattr(old_value, "form_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression27"):
                opp_val = getattr(value, "form_Expression27", None)
                setattr(value, "form_Expression27", self)

class form_ItemContainer(ABC):

    def __init__(self, itemClass: str):
        self.itemClass = itemClass
        
        pass
    @property
    def itemClass(self):
        return self.__itemClass

    @itemClass.setter
    def itemClass(self, itemClass: str):
        self.__itemClass = itemClass


class form_WidgetLayoutInfo:

    def __init__(self, line: int, column: int, verticalSpan: int, horizontalSpan: int, form_WidgetLayoutInfo: "form_Widget" = None):
        self.line = line
        self.column = column
        self.verticalSpan = verticalSpan
        self.horizontalSpan = horizontalSpan
        self.form_WidgetLayoutInfo = form_WidgetLayoutInfo
        
        pass
    @property
    def horizontalSpan(self):
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan


    @property
    def verticalSpan(self):
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan


    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column


    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line


    @property
    def form_WidgetLayoutInfo(self):
        return self.__form_WidgetLayoutInfo

    @form_WidgetLayoutInfo.setter
    def form_WidgetLayoutInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_WidgetLayoutInfo__form_WidgetLayoutInfo", None)
        self.__form_WidgetLayoutInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Widget40"):
                opp_val = getattr(old_value, "form_Widget40", None)
                if opp_val == self:
                    setattr(old_value, "form_Widget40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Widget40"):
                opp_val = getattr(value, "form_Widget40", None)
                setattr(value, "form_Widget40", self)

class form_EStringToStringMapEntry:

    pass
class Validable:

    pass
class form_FormField(Duplicable, Validable, Widget):

    def __init__(self, description: str, exampleMessagePosition: str, form_FormField: "form_Expression" = None):
        self.description = description
        self.exampleMessagePosition = exampleMessagePosition
        self.form_FormField = form_FormField
        
        pass
    @property
    def exampleMessagePosition(self):
        return self.__exampleMessagePosition

    @exampleMessagePosition.setter
    def exampleMessagePosition(self, exampleMessagePosition: str):
        self.__exampleMessagePosition = exampleMessagePosition


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def form_FormField(self):
        return self.__form_FormField

    @form_FormField.setter
    def form_FormField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_FormField__form_FormField", None)
        self.__form_FormField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression85"):
                opp_val = getattr(old_value, "form_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression85"):
                opp_val = getattr(value, "form_Expression85", None)
                setattr(value, "form_Expression85", self)

class ConnectableElement:

    pass
class form_SubmitFormButton(ConnectableElement, FormButton):

    pass
class form_Form(ConnectableElement, Validable):

    def __init__(self, showPageLabel: str, allowHTMLInPageLabel: bool, version: str, nColumn: int, nLine: int, form_Form9: set["form_Column"] = None, form_Form11: set["form_Line"] = None, form_Form13: set["form_Widget"] = None, form_Form16: "form_Expression" = None, form_Form19: set["form_Operation"] = None, form_Form: set["form_EStringToStringMapEntry"] = None):
        self.showPageLabel = showPageLabel
        self.allowHTMLInPageLabel = allowHTMLInPageLabel
        self.version = version
        self.nColumn = nColumn
        self.nLine = nLine
        self.form_Form9 = form_Form9 if form_Form9 is not None else set()
        self.form_Form11 = form_Form11 if form_Form11 is not None else set()
        self.form_Form13 = form_Form13 if form_Form13 is not None else set()
        self.form_Form16 = form_Form16
        self.form_Form19 = form_Form19 if form_Form19 is not None else set()
        self.form_Form = form_Form if form_Form is not None else set()
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def showPageLabel(self):
        return self.__showPageLabel

    @showPageLabel.setter
    def showPageLabel(self, showPageLabel: str):
        self.__showPageLabel = showPageLabel


    @property
    def nColumn(self):
        return self.__nColumn

    @nColumn.setter
    def nColumn(self, nColumn: int):
        self.__nColumn = nColumn


    @property
    def nLine(self):
        return self.__nLine

    @nLine.setter
    def nLine(self, nLine: int):
        self.__nLine = nLine


    @property
    def allowHTMLInPageLabel(self):
        return self.__allowHTMLInPageLabel

    @allowHTMLInPageLabel.setter
    def allowHTMLInPageLabel(self, allowHTMLInPageLabel: bool):
        self.__allowHTMLInPageLabel = allowHTMLInPageLabel


    @property
    def form_Form(self):
        return self.__form_Form

    @form_Form.setter
    def form_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Form__form_Form", None)
        self.__form_Form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_EStringToStringMapEntry"):
                    opp_val = getattr(item, "form_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "form_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_EStringToStringMapEntry"):
                    opp_val = getattr(item, "form_EStringToStringMapEntry", None)
                    
                    setattr(item, "form_EStringToStringMapEntry", self)
                    

    @property
    def form_Form16(self):
        return self.__form_Form16

    @form_Form16.setter
    def form_Form16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Form__form_Form16", None)
        self.__form_Form16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression17"):
                opp_val = getattr(old_value, "form_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression17"):
                opp_val = getattr(value, "form_Expression17", None)
                setattr(value, "form_Expression17", self)

    @property
    def form_Form13(self):
        return self.__form_Form13

    @form_Form13.setter
    def form_Form13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Form__form_Form13", None)
        self.__form_Form13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Widget14"):
                    opp_val = getattr(item, "form_Widget14", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Widget14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Widget14"):
                    opp_val = getattr(item, "form_Widget14", None)
                    
                    setattr(item, "form_Widget14", self)
                    

    @property
    def form_Form9(self):
        return self.__form_Form9

    @form_Form9.setter
    def form_Form9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Form__form_Form9", None)
        self.__form_Form9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Column"):
                    opp_val = getattr(item, "form_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Column"):
                    opp_val = getattr(item, "form_Column", None)
                    
                    setattr(item, "form_Column", self)
                    

    @property
    def form_Form19(self):
        return self.__form_Form19

    @form_Form19.setter
    def form_Form19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Form__form_Form19", None)
        self.__form_Form19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Operation"):
                    opp_val = getattr(item, "form_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Operation"):
                    opp_val = getattr(item, "form_Operation", None)
                    
                    setattr(item, "form_Operation", self)
                    

    @property
    def form_Form11(self):
        return self.__form_Form11

    @form_Form11.setter
    def form_Form11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Form__form_Form11", None)
        self.__form_Form11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Line"):
                    opp_val = getattr(item, "form_Line", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Line", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Line"):
                    opp_val = getattr(item, "form_Line", None)
                    
                    setattr(item, "form_Line", self)
                    

class form_Operation:

    pass
class form_Line:

    def __init__(self, height: str, number: int, form_Line: "form_Form" = None, form_Line81: "form_Group" = None):
        self.height = height
        self.number = number
        self.form_Line = form_Line
        self.form_Line81 = form_Line81
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def form_Line(self):
        return self.__form_Line

    @form_Line.setter
    def form_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Line__form_Line", None)
        self.__form_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Form11"):
                opp_val = getattr(old_value, "form_Form11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Form11"):
                opp_val = getattr(value, "form_Form11", None)
                if opp_val is None:
                    setattr(value, "form_Form11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_Line81(self):
        return self.__form_Line81

    @form_Line81.setter
    def form_Line81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Line__form_Line81", None)
        self.__form_Line81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Group80"):
                opp_val = getattr(old_value, "form_Group80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Group80"):
                opp_val = getattr(value, "form_Group80", None)
                if opp_val is None:
                    setattr(value, "form_Group80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class form_Column:

    def __init__(self, width: str, number: int, form_Column: "form_Form" = None, form_Column78: "form_Group" = None):
        self.width = width
        self.number = number
        self.form_Column = form_Column
        self.form_Column78 = form_Column78
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def form_Column(self):
        return self.__form_Column

    @form_Column.setter
    def form_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Column__form_Column", None)
        self.__form_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Form9"):
                opp_val = getattr(old_value, "form_Form9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Form9"):
                opp_val = getattr(value, "form_Form9", None)
                if opp_val is None:
                    setattr(value, "form_Form9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_Column78(self):
        return self.__form_Column78

    @form_Column78.setter
    def form_Column78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Column__form_Column78", None)
        self.__form_Column78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Group77"):
                opp_val = getattr(old_value, "form_Group77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Group77"):
                opp_val = getattr(value, "form_Group77", None)
                if opp_val is None:
                    setattr(value, "form_Group77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class form_Validable:

    def __init__(self, useDefaultValidator: str, below: bool, form_Validable: set["form_Validator"] = None):
        self.useDefaultValidator = useDefaultValidator
        self.below = below
        self.form_Validable = form_Validable if form_Validable is not None else set()
        
        pass
    @property
    def below(self):
        return self.__below

    @below.setter
    def below(self, below: bool):
        self.__below = below


    @property
    def useDefaultValidator(self):
        return self.__useDefaultValidator

    @useDefaultValidator.setter
    def useDefaultValidator(self, useDefaultValidator: str):
        self.__useDefaultValidator = useDefaultValidator


    @property
    def form_Validable(self):
        return self.__form_Validable

    @form_Validable.setter
    def form_Validable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Validable__form_Validable", None)
        self.__form_Validable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Validator6"):
                    opp_val = getattr(item, "form_Validator6", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Validator6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Validator6"):
                    opp_val = getattr(item, "form_Validator6", None)
                    
                    setattr(item, "form_Validator6", self)
                    

class form_Expression:

    pass
class form_Validator:

    def __init__(self, validatorClass: str, htmlClass: str, name: str, belowField: bool, form_Validator: "form_Expression" = None, form_Validator3: "form_Expression" = None, form_Validator6: "form_Validable" = None):
        self.validatorClass = validatorClass
        self.htmlClass = htmlClass
        self.name = name
        self.belowField = belowField
        self.form_Validator = form_Validator
        self.form_Validator3 = form_Validator3
        self.form_Validator6 = form_Validator6
        
        pass
    @property
    def validatorClass(self):
        return self.__validatorClass

    @validatorClass.setter
    def validatorClass(self, validatorClass: str):
        self.__validatorClass = validatorClass


    @property
    def htmlClass(self):
        return self.__htmlClass

    @htmlClass.setter
    def htmlClass(self, htmlClass: str):
        self.__htmlClass = htmlClass


    @property
    def belowField(self):
        return self.__belowField

    @belowField.setter
    def belowField(self, belowField: bool):
        self.__belowField = belowField


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def form_Validator6(self):
        return self.__form_Validator6

    @form_Validator6.setter
    def form_Validator6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Validator__form_Validator6", None)
        self.__form_Validator6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Validable"):
                opp_val = getattr(old_value, "form_Validable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Validable"):
                opp_val = getattr(value, "form_Validable", None)
                if opp_val is None:
                    setattr(value, "form_Validable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_Validator3(self):
        return self.__form_Validator3

    @form_Validator3.setter
    def form_Validator3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Validator__form_Validator3", None)
        self.__form_Validator3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression4"):
                opp_val = getattr(old_value, "form_Expression4", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression4"):
                opp_val = getattr(value, "form_Expression4", None)
                setattr(value, "form_Expression4", self)

    @property
    def form_Validator(self):
        return self.__form_Validator

    @form_Validator.setter
    def form_Validator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Validator__form_Validator", None)
        self.__form_Validator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression"):
                opp_val = getattr(old_value, "form_Expression", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression"):
                opp_val = getattr(value, "form_Expression", None)
                setattr(value, "form_Expression", self)

class form_Widget(Element, CSSCustomizable):

    def __init__(self, showDisplayLabel: str, allowHTMLForDisplayLabel: bool, displayDependentWidgetOnlyOnEventTriggered: bool, mandatory: bool, readOnly: bool, labelPosition: str, realHtmlAttributes: str, injectWidgetCondition: bool, version: str, returnTypeModifier: str, form_Widget: "form_WidgetDependency" = None, form_Widget14: "form_Form" = None, form_Widget40: "form_WidgetLayoutInfo" = None, form_Widget42: set["form_WidgetDependency"] = None, form_Widget45: set["form_WidgetDependency"] = None, form_Widget48: "form_Expression" = None, form_Widget51: "form_Expression" = None, form_Widget72: "form_Operation" = None, form_Widget75: "form_Group" = None, form_Widget54: "form_Expression" = None, form_Widget57: "form_Expression" = None, form_Widget60: "form_Expression" = None, form_Widget63: "form_Expression" = None, form_Widget66: "form_Expression" = None, form_Widget69: "form_Expression" = None):
        self.showDisplayLabel = showDisplayLabel
        self.allowHTMLForDisplayLabel = allowHTMLForDisplayLabel
        self.displayDependentWidgetOnlyOnEventTriggered = displayDependentWidgetOnlyOnEventTriggered
        self.mandatory = mandatory
        self.readOnly = readOnly
        self.labelPosition = labelPosition
        self.realHtmlAttributes = realHtmlAttributes
        self.injectWidgetCondition = injectWidgetCondition
        self.version = version
        self.returnTypeModifier = returnTypeModifier
        self.form_Widget = form_Widget
        self.form_Widget14 = form_Widget14
        self.form_Widget40 = form_Widget40
        self.form_Widget42 = form_Widget42 if form_Widget42 is not None else set()
        self.form_Widget45 = form_Widget45 if form_Widget45 is not None else set()
        self.form_Widget48 = form_Widget48
        self.form_Widget51 = form_Widget51
        self.form_Widget72 = form_Widget72
        self.form_Widget75 = form_Widget75
        self.form_Widget54 = form_Widget54
        self.form_Widget57 = form_Widget57
        self.form_Widget60 = form_Widget60
        self.form_Widget63 = form_Widget63
        self.form_Widget66 = form_Widget66
        self.form_Widget69 = form_Widget69
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def mandatory(self):
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory


    @property
    def injectWidgetCondition(self):
        return self.__injectWidgetCondition

    @injectWidgetCondition.setter
    def injectWidgetCondition(self, injectWidgetCondition: bool):
        self.__injectWidgetCondition = injectWidgetCondition


    @property
    def displayDependentWidgetOnlyOnEventTriggered(self):
        return self.__displayDependentWidgetOnlyOnEventTriggered

    @displayDependentWidgetOnlyOnEventTriggered.setter
    def displayDependentWidgetOnlyOnEventTriggered(self, displayDependentWidgetOnlyOnEventTriggered: bool):
        self.__displayDependentWidgetOnlyOnEventTriggered = displayDependentWidgetOnlyOnEventTriggered


    @property
    def realHtmlAttributes(self):
        return self.__realHtmlAttributes

    @realHtmlAttributes.setter
    def realHtmlAttributes(self, realHtmlAttributes: str):
        self.__realHtmlAttributes = realHtmlAttributes


    @property
    def labelPosition(self):
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition


    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def showDisplayLabel(self):
        return self.__showDisplayLabel

    @showDisplayLabel.setter
    def showDisplayLabel(self, showDisplayLabel: str):
        self.__showDisplayLabel = showDisplayLabel


    @property
    def allowHTMLForDisplayLabel(self):
        return self.__allowHTMLForDisplayLabel

    @allowHTMLForDisplayLabel.setter
    def allowHTMLForDisplayLabel(self, allowHTMLForDisplayLabel: bool):
        self.__allowHTMLForDisplayLabel = allowHTMLForDisplayLabel


    @property
    def returnTypeModifier(self):
        return self.__returnTypeModifier

    @returnTypeModifier.setter
    def returnTypeModifier(self, returnTypeModifier: str):
        self.__returnTypeModifier = returnTypeModifier


    @property
    def form_Widget63(self):
        return self.__form_Widget63

    @form_Widget63.setter
    def form_Widget63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget63", None)
        self.__form_Widget63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression64"):
                opp_val = getattr(old_value, "form_Expression64", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression64"):
                opp_val = getattr(value, "form_Expression64", None)
                setattr(value, "form_Expression64", self)

    @property
    def form_Widget40(self):
        return self.__form_Widget40

    @form_Widget40.setter
    def form_Widget40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget40", None)
        self.__form_Widget40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_WidgetLayoutInfo"):
                opp_val = getattr(old_value, "form_WidgetLayoutInfo", None)
                if opp_val == self:
                    setattr(old_value, "form_WidgetLayoutInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_WidgetLayoutInfo"):
                opp_val = getattr(value, "form_WidgetLayoutInfo", None)
                setattr(value, "form_WidgetLayoutInfo", self)

    @property
    def form_Widget54(self):
        return self.__form_Widget54

    @form_Widget54.setter
    def form_Widget54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget54", None)
        self.__form_Widget54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression55"):
                opp_val = getattr(old_value, "form_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression55"):
                opp_val = getattr(value, "form_Expression55", None)
                setattr(value, "form_Expression55", self)

    @property
    def form_Widget51(self):
        return self.__form_Widget51

    @form_Widget51.setter
    def form_Widget51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget51", None)
        self.__form_Widget51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression52"):
                opp_val = getattr(old_value, "form_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression52"):
                opp_val = getattr(value, "form_Expression52", None)
                setattr(value, "form_Expression52", self)

    @property
    def form_Widget72(self):
        return self.__form_Widget72

    @form_Widget72.setter
    def form_Widget72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget72", None)
        self.__form_Widget72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Operation73"):
                opp_val = getattr(old_value, "form_Operation73", None)
                if opp_val == self:
                    setattr(old_value, "form_Operation73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Operation73"):
                opp_val = getattr(value, "form_Operation73", None)
                setattr(value, "form_Operation73", self)

    @property
    def form_Widget75(self):
        return self.__form_Widget75

    @form_Widget75.setter
    def form_Widget75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget75", None)
        self.__form_Widget75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Group"):
                opp_val = getattr(old_value, "form_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Group"):
                opp_val = getattr(value, "form_Group", None)
                if opp_val is None:
                    setattr(value, "form_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_Widget42(self):
        return self.__form_Widget42

    @form_Widget42.setter
    def form_Widget42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget42", None)
        self.__form_Widget42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_WidgetDependency43"):
                    opp_val = getattr(item, "form_WidgetDependency43", None)
                    
                    if opp_val == self:
                        setattr(item, "form_WidgetDependency43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_WidgetDependency43"):
                    opp_val = getattr(item, "form_WidgetDependency43", None)
                    
                    setattr(item, "form_WidgetDependency43", self)
                    

    @property
    def form_Widget69(self):
        return self.__form_Widget69

    @form_Widget69.setter
    def form_Widget69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget69", None)
        self.__form_Widget69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression70"):
                opp_val = getattr(old_value, "form_Expression70", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression70"):
                opp_val = getattr(value, "form_Expression70", None)
                setattr(value, "form_Expression70", self)

    @property
    def form_Widget48(self):
        return self.__form_Widget48

    @form_Widget48.setter
    def form_Widget48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget48", None)
        self.__form_Widget48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression49"):
                opp_val = getattr(old_value, "form_Expression49", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression49"):
                opp_val = getattr(value, "form_Expression49", None)
                setattr(value, "form_Expression49", self)

    @property
    def form_Widget66(self):
        return self.__form_Widget66

    @form_Widget66.setter
    def form_Widget66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget66", None)
        self.__form_Widget66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression67"):
                opp_val = getattr(old_value, "form_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression67"):
                opp_val = getattr(value, "form_Expression67", None)
                setattr(value, "form_Expression67", self)

    @property
    def form_Widget(self):
        return self.__form_Widget

    @form_Widget.setter
    def form_Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget", None)
        self.__form_Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_WidgetDependency"):
                opp_val = getattr(old_value, "form_WidgetDependency", None)
                if opp_val == self:
                    setattr(old_value, "form_WidgetDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_WidgetDependency"):
                opp_val = getattr(value, "form_WidgetDependency", None)
                setattr(value, "form_WidgetDependency", self)

    @property
    def form_Widget60(self):
        return self.__form_Widget60

    @form_Widget60.setter
    def form_Widget60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget60", None)
        self.__form_Widget60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression61"):
                opp_val = getattr(old_value, "form_Expression61", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression61"):
                opp_val = getattr(value, "form_Expression61", None)
                setattr(value, "form_Expression61", self)

    @property
    def form_Widget45(self):
        return self.__form_Widget45

    @form_Widget45.setter
    def form_Widget45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget45", None)
        self.__form_Widget45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_WidgetDependency46"):
                    opp_val = getattr(item, "form_WidgetDependency46", None)
                    
                    if opp_val == self:
                        setattr(item, "form_WidgetDependency46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_WidgetDependency46"):
                    opp_val = getattr(item, "form_WidgetDependency46", None)
                    
                    setattr(item, "form_WidgetDependency46", self)
                    

    @property
    def form_Widget14(self):
        return self.__form_Widget14

    @form_Widget14.setter
    def form_Widget14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget14", None)
        self.__form_Widget14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Form13"):
                opp_val = getattr(old_value, "form_Form13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Form13"):
                opp_val = getattr(value, "form_Form13", None)
                if opp_val is None:
                    setattr(value, "form_Form13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_Widget57(self):
        return self.__form_Widget57

    @form_Widget57.setter
    def form_Widget57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Widget__form_Widget57", None)
        self.__form_Widget57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Expression58"):
                opp_val = getattr(old_value, "form_Expression58", None)
                if opp_val == self:
                    setattr(old_value, "form_Expression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Expression58"):
                opp_val = getattr(value, "form_Expression58", None)
                setattr(value, "form_Expression58", self)

class form_WidgetDependency:

    def __init__(self, triggerRefreshOnModification: bool, eventTypes: str, form_WidgetDependency: "form_Widget" = None, form_WidgetDependency43: "form_Widget" = None, form_WidgetDependency46: "form_Widget" = None):
        self.triggerRefreshOnModification = triggerRefreshOnModification
        self.eventTypes = eventTypes
        self.form_WidgetDependency = form_WidgetDependency
        self.form_WidgetDependency43 = form_WidgetDependency43
        self.form_WidgetDependency46 = form_WidgetDependency46
        
        pass
    @property
    def eventTypes(self):
        return self.__eventTypes

    @eventTypes.setter
    def eventTypes(self, eventTypes: str):
        self.__eventTypes = eventTypes


    @property
    def triggerRefreshOnModification(self):
        return self.__triggerRefreshOnModification

    @triggerRefreshOnModification.setter
    def triggerRefreshOnModification(self, triggerRefreshOnModification: bool):
        self.__triggerRefreshOnModification = triggerRefreshOnModification


    @property
    def form_WidgetDependency43(self):
        return self.__form_WidgetDependency43

    @form_WidgetDependency43.setter
    def form_WidgetDependency43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_WidgetDependency__form_WidgetDependency43", None)
        self.__form_WidgetDependency43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Widget42"):
                opp_val = getattr(old_value, "form_Widget42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Widget42"):
                opp_val = getattr(value, "form_Widget42", None)
                if opp_val is None:
                    setattr(value, "form_Widget42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_WidgetDependency(self):
        return self.__form_WidgetDependency

    @form_WidgetDependency.setter
    def form_WidgetDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_WidgetDependency__form_WidgetDependency", None)
        self.__form_WidgetDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Widget"):
                opp_val = getattr(old_value, "form_Widget", None)
                if opp_val == self:
                    setattr(old_value, "form_Widget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Widget"):
                opp_val = getattr(value, "form_Widget", None)
                setattr(value, "form_Widget", self)

    @property
    def form_WidgetDependency46(self):
        return self.__form_WidgetDependency46

    @form_WidgetDependency46.setter
    def form_WidgetDependency46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_WidgetDependency__form_WidgetDependency46", None)
        self.__form_WidgetDependency46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Widget45"):
                opp_val = getattr(old_value, "form_Widget45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Widget45"):
                opp_val = getattr(value, "form_Widget45", None)
                if opp_val is None:
                    setattr(value, "form_Widget45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
