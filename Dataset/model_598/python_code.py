from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class presentation_WindowManager:

    def __init__(self, mixed: str, presentation_WindowManager: "presentation_Window" = None):
        self.mixed = mixed
        self.presentation_WindowManager = presentation_WindowManager
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_WindowManager(self):
        return self.__presentation_WindowManager

    @presentation_WindowManager.setter
    def presentation_WindowManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_WindowManager__presentation_WindowManager", None)
        self.__presentation_WindowManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Window303"):
                opp_val = getattr(old_value, "presentation_Window303", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Window303"):
                opp_val = getattr(value, "presentation_Window303", None)
                if opp_val is None:
                    setattr(value, "presentation_Window303", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ViewerComparator:

    pass
class presentation_ViewerColumn(ABC):

    def __init__(self, mixed: str):
        self.mixed = mixed
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class presentation_Viewer(ABC):

    def __init__(self, mixed: str, group: str, presentation_Viewer: set["presentation_EObject"] = None, presentation_Viewer298: set["presentation_ISelection"] = None, presentation_Viewer300: set["presentation_Control"] = None):
        self.mixed = mixed
        self.group = group
        self.presentation_Viewer = presentation_Viewer if presentation_Viewer is not None else set()
        self.presentation_Viewer298 = presentation_Viewer298 if presentation_Viewer298 is not None else set()
        self.presentation_Viewer300 = presentation_Viewer300 if presentation_Viewer300 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Viewer(self):
        return self.__presentation_Viewer

    @presentation_Viewer.setter
    def presentation_Viewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Viewer__presentation_Viewer", None)
        self.__presentation_Viewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject296"):
                    opp_val = getattr(item, "presentation_EObject296", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject296"):
                    opp_val = getattr(item, "presentation_EObject296", None)
                    
                    setattr(item, "presentation_EObject296", self)
                    

    @property
    def presentation_Viewer298(self):
        return self.__presentation_Viewer298

    @presentation_Viewer298.setter
    def presentation_Viewer298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Viewer__presentation_Viewer298", None)
        self.__presentation_Viewer298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ISelection"):
                    opp_val = getattr(item, "presentation_ISelection", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ISelection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ISelection"):
                    opp_val = getattr(item, "presentation_ISelection", None)
                    
                    setattr(item, "presentation_ISelection", self)
                    

    @property
    def presentation_Viewer300(self):
        return self.__presentation_Viewer300

    @presentation_Viewer300.setter
    def presentation_Viewer300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Viewer__presentation_Viewer300", None)
        self.__presentation_Viewer300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control301"):
                    opp_val = getattr(item, "presentation_Control301", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control301"):
                    opp_val = getattr(item, "presentation_Control301", None)
                    
                    setattr(item, "presentation_Control301", self)
                    

class presentation_URL:

    def __init__(self, mixed: str, presentation_URL: "presentation_XMLDataProvider" = None):
        self.mixed = mixed
        self.presentation_URL = presentation_URL
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_URL(self):
        return self.__presentation_URL

    @presentation_URL.setter
    def presentation_URL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_URL__presentation_URL", None)
        self.__presentation_URL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_XMLDataProvider306"):
                opp_val = getattr(old_value, "presentation_XMLDataProvider306", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_XMLDataProvider306"):
                opp_val = getattr(value, "presentation_XMLDataProvider306", None)
                if opp_val is None:
                    setattr(value, "presentation_XMLDataProvider306", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TrayDialog:

    pass
class presentation_TitleAreaDialog(TrayDialog):

    def __init__(self, errorMessage: str, message: str, title: str, group3: str, titleImage: str, presentation_TitleAreaDialog: set["presentation_RGB"] = None):
        self.errorMessage = errorMessage
        self.message = message
        self.title = title
        self.group3 = group3
        self.titleImage = titleImage
        self.presentation_TitleAreaDialog = presentation_TitleAreaDialog if presentation_TitleAreaDialog is not None else set()
        
    @property
    def errorMessage(self) -> str:
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, errorMessage: str):
        self.__errorMessage = errorMessage

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def titleImage(self) -> str:
        return self.__titleImage

    @titleImage.setter
    def titleImage(self, titleImage: str):
        self.__titleImage = titleImage

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_TitleAreaDialog(self):
        return self.__presentation_TitleAreaDialog

    @presentation_TitleAreaDialog.setter
    def presentation_TitleAreaDialog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TitleAreaDialog__presentation_TitleAreaDialog", None)
        self.__presentation_TitleAreaDialog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_RGB252"):
                    opp_val = getattr(item, "presentation_RGB252", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_RGB252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_RGB252"):
                    opp_val = getattr(item, "presentation_RGB252", None)
                    
                    setattr(item, "presentation_RGB252", self)
                    

class ViewerColumn:

    pass
class presentation_TableViewerColumn(ViewerColumn):

    def __init__(self, group: str, text: str, width: str, presentation_TableViewerColumn: set["presentation_TableColumn"] = None):
        self.group = group
        self.text = text
        self.width = width
        self.presentation_TableViewerColumn = presentation_TableViewerColumn if presentation_TableViewerColumn is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_TableViewerColumn(self):
        return self.__presentation_TableViewerColumn

    @presentation_TableViewerColumn.setter
    def presentation_TableViewerColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableViewerColumn__presentation_TableViewerColumn", None)
        self.__presentation_TableViewerColumn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableColumn250"):
                    opp_val = getattr(item, "presentation_TableColumn250", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableColumn250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableColumn250"):
                    opp_val = getattr(item, "presentation_TableColumn250", None)
                    
                    setattr(item, "presentation_TableColumn250", self)
                    

class AbstractTableViewer:

    pass
class presentation_TableViewer(AbstractTableViewer):

    def __init__(self, group4: str, presentation_TableViewer: set["presentation_Table"] = None):
        self.group4 = group4
        self.presentation_TableViewer = presentation_TableViewer if presentation_TableViewer is not None else set()
        
    @property
    def group4(self) -> str:
        return self.__group4

    @group4.setter
    def group4(self, group4: str):
        self.__group4 = group4

    @property
    def presentation_TableViewer(self):
        return self.__presentation_TableViewer

    @presentation_TableViewer.setter
    def presentation_TableViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableViewer__presentation_TableViewer", None)
        self.__presentation_TableViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Table248"):
                    opp_val = getattr(item, "presentation_Table248", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Table248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Table248"):
                    opp_val = getattr(item, "presentation_Table248", None)
                    
                    setattr(item, "presentation_Table248", self)
                    

class AbstractTreeViewer:

    pass
class presentation_TreeViewer(AbstractTreeViewer):

    def __init__(self, group5: str, presentation_TreeViewer: set["presentation_Tree"] = None):
        self.group5 = group5
        self.presentation_TreeViewer = presentation_TreeViewer if presentation_TreeViewer is not None else set()
        
    @property
    def group5(self) -> str:
        return self.__group5

    @group5.setter
    def group5(self, group5: str):
        self.__group5 = group5

    @property
    def presentation_TreeViewer(self):
        return self.__presentation_TreeViewer

    @presentation_TreeViewer.setter
    def presentation_TreeViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeViewer__presentation_TreeViewer", None)
        self.__presentation_TreeViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Tree294"):
                    opp_val = getattr(item, "presentation_Tree294", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Tree294", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Tree294"):
                    opp_val = getattr(item, "presentation_Tree294", None)
                    
                    setattr(item, "presentation_Tree294", self)
                    

class presentation_TableTreeViewer(AbstractTreeViewer):

    def __init__(self, group5: str, presentation_TableTreeViewer: set["presentation_TableTree"] = None):
        self.group5 = group5
        self.presentation_TableTreeViewer = presentation_TableTreeViewer if presentation_TableTreeViewer is not None else set()
        
    @property
    def group5(self) -> str:
        return self.__group5

    @group5.setter
    def group5(self, group5: str):
        self.__group5 = group5

    @property
    def presentation_TableTreeViewer(self):
        return self.__presentation_TableTreeViewer

    @presentation_TableTreeViewer.setter
    def presentation_TableTreeViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableTreeViewer__presentation_TableTreeViewer", None)
        self.__presentation_TableTreeViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableTree"):
                    opp_val = getattr(item, "presentation_TableTree", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableTree", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableTree"):
                    opp_val = getattr(item, "presentation_TableTree", None)
                    
                    setattr(item, "presentation_TableTree", self)
                    

class ControlEditor:

    pass
class presentation_TableEditor(ControlEditor):

    def __init__(self, group1: str, column: str, dynamic: str, presentation_TableEditor: set["presentation_TableItem"] = None):
        self.group1 = group1
        self.column = column
        self.dynamic = dynamic
        self.presentation_TableEditor = presentation_TableEditor if presentation_TableEditor is not None else set()
        
    @property
    def dynamic(self) -> str:
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, dynamic: str):
        self.__dynamic = dynamic

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def presentation_TableEditor(self):
        return self.__presentation_TableEditor

    @presentation_TableEditor.setter
    def presentation_TableEditor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableEditor__presentation_TableEditor", None)
        self.__presentation_TableEditor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableItem237"):
                    opp_val = getattr(item, "presentation_TableItem237", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableItem237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableItem237"):
                    opp_val = getattr(item, "presentation_TableItem237", None)
                    
                    setattr(item, "presentation_TableItem237", self)
                    

class TextStyle:

    pass
class presentation_StyleRange(TextStyle):

    pass
class presentation_StyledTextContent(ABC):

    def __init__(self, mixed: str, presentation_StyledTextContent: "presentation_StyledText" = None):
        self.mixed = mixed
        self.presentation_StyledTextContent = presentation_StyledTextContent
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_StyledTextContent(self):
        return self.__presentation_StyledTextContent

    @presentation_StyledTextContent.setter
    def presentation_StyledTextContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StyledTextContent__presentation_StyledTextContent", None)
        self.__presentation_StyledTextContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_StyledText210"):
                opp_val = getattr(old_value, "presentation_StyledText210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_StyledText210"):
                opp_val = getattr(value, "presentation_StyledText210", None)
                if opp_val is None:
                    setattr(value, "presentation_StyledText210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ViewerComparator:

    def __init__(self, mixed: str, presentation_ViewerComparator: "presentation_StructuredViewer" = None):
        self.mixed = mixed
        self.presentation_ViewerComparator = presentation_ViewerComparator
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ViewerComparator(self):
        return self.__presentation_ViewerComparator

    @presentation_ViewerComparator.setter
    def presentation_ViewerComparator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ViewerComparator__presentation_ViewerComparator", None)
        self.__presentation_ViewerComparator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_StructuredViewer"):
                opp_val = getattr(old_value, "presentation_StructuredViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_StructuredViewer"):
                opp_val = getattr(value, "presentation_StructuredViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_StructuredViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ViewerSorter(ViewerComparator):

    pass
class presentation_ViewerFilter(ABC):

    def __init__(self, mixed: str, presentation_ViewerFilter: "presentation_StructuredViewer" = None):
        self.mixed = mixed
        self.presentation_ViewerFilter = presentation_ViewerFilter
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ViewerFilter(self):
        return self.__presentation_ViewerFilter

    @presentation_ViewerFilter.setter
    def presentation_ViewerFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ViewerFilter__presentation_ViewerFilter", None)
        self.__presentation_ViewerFilter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_StructuredViewer202"):
                opp_val = getattr(old_value, "presentation_StructuredViewer202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_StructuredViewer202"):
                opp_val = getattr(value, "presentation_StructuredViewer202", None)
                if opp_val is None:
                    setattr(value, "presentation_StructuredViewer202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ContentViewer:

    pass
class presentation_StructuredViewer(ContentViewer):

    def __init__(self, useHashlookup: str, group2: str, presentation_StructuredViewer200: set["presentation_IElementComparer"] = None, presentation_StructuredViewer202: set["presentation_ViewerFilter"] = None, presentation_StructuredViewer204: set["presentation_ViewerSorter"] = None, presentation_StructuredViewer: set["presentation_ViewerComparator"] = None):
        self.useHashlookup = useHashlookup
        self.group2 = group2
        self.presentation_StructuredViewer200 = presentation_StructuredViewer200 if presentation_StructuredViewer200 is not None else set()
        self.presentation_StructuredViewer202 = presentation_StructuredViewer202 if presentation_StructuredViewer202 is not None else set()
        self.presentation_StructuredViewer204 = presentation_StructuredViewer204 if presentation_StructuredViewer204 is not None else set()
        self.presentation_StructuredViewer = presentation_StructuredViewer if presentation_StructuredViewer is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def useHashlookup(self) -> str:
        return self.__useHashlookup

    @useHashlookup.setter
    def useHashlookup(self, useHashlookup: str):
        self.__useHashlookup = useHashlookup

    @property
    def presentation_StructuredViewer204(self):
        return self.__presentation_StructuredViewer204

    @presentation_StructuredViewer204.setter
    def presentation_StructuredViewer204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StructuredViewer__presentation_StructuredViewer204", None)
        self.__presentation_StructuredViewer204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ViewerSorter"):
                    opp_val = getattr(item, "presentation_ViewerSorter", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ViewerSorter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ViewerSorter"):
                    opp_val = getattr(item, "presentation_ViewerSorter", None)
                    
                    setattr(item, "presentation_ViewerSorter", self)
                    

    @property
    def presentation_StructuredViewer(self):
        return self.__presentation_StructuredViewer

    @presentation_StructuredViewer.setter
    def presentation_StructuredViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StructuredViewer__presentation_StructuredViewer", None)
        self.__presentation_StructuredViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ViewerComparator"):
                    opp_val = getattr(item, "presentation_ViewerComparator", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ViewerComparator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ViewerComparator"):
                    opp_val = getattr(item, "presentation_ViewerComparator", None)
                    
                    setattr(item, "presentation_ViewerComparator", self)
                    

    @property
    def presentation_StructuredViewer200(self):
        return self.__presentation_StructuredViewer200

    @presentation_StructuredViewer200.setter
    def presentation_StructuredViewer200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StructuredViewer__presentation_StructuredViewer200", None)
        self.__presentation_StructuredViewer200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IElementComparer"):
                    opp_val = getattr(item, "presentation_IElementComparer", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IElementComparer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IElementComparer"):
                    opp_val = getattr(item, "presentation_IElementComparer", None)
                    
                    setattr(item, "presentation_IElementComparer", self)
                    

    @property
    def presentation_StructuredViewer202(self):
        return self.__presentation_StructuredViewer202

    @presentation_StructuredViewer202.setter
    def presentation_StructuredViewer202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StructuredViewer__presentation_StructuredViewer202", None)
        self.__presentation_StructuredViewer202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ViewerFilter"):
                    opp_val = getattr(item, "presentation_ViewerFilter", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ViewerFilter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ViewerFilter"):
                    opp_val = getattr(item, "presentation_ViewerFilter", None)
                    
                    setattr(item, "presentation_ViewerFilter", self)
                    

class Decorations:

    pass
class presentation_Shell(Decorations):

    def __init__(self, group5: str, minimumSize: str, alpha: str, fullScreen: str, imeInputMode: str, presentation_Shell: "presentation_Shell" = None, presentation_Shell194: set["presentation_Shell"] = None, presentation_Shell261: "presentation_ToolTip" = None):
        self.group5 = group5
        self.minimumSize = minimumSize
        self.alpha = alpha
        self.fullScreen = fullScreen
        self.imeInputMode = imeInputMode
        self.presentation_Shell = presentation_Shell
        self.presentation_Shell194 = presentation_Shell194 if presentation_Shell194 is not None else set()
        self.presentation_Shell261 = presentation_Shell261
        
    @property
    def imeInputMode(self) -> str:
        return self.__imeInputMode

    @imeInputMode.setter
    def imeInputMode(self, imeInputMode: str):
        self.__imeInputMode = imeInputMode

    @property
    def alpha(self) -> str:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha

    @property
    def group5(self) -> str:
        return self.__group5

    @group5.setter
    def group5(self, group5: str):
        self.__group5 = group5

    @property
    def minimumSize(self) -> str:
        return self.__minimumSize

    @minimumSize.setter
    def minimumSize(self, minimumSize: str):
        self.__minimumSize = minimumSize

    @property
    def fullScreen(self) -> str:
        return self.__fullScreen

    @fullScreen.setter
    def fullScreen(self, fullScreen: str):
        self.__fullScreen = fullScreen

    @property
    def presentation_Shell261(self):
        return self.__presentation_Shell261

    @presentation_Shell261.setter
    def presentation_Shell261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Shell__presentation_Shell261", None)
        self.__presentation_Shell261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ToolTip"):
                opp_val = getattr(old_value, "presentation_ToolTip", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ToolTip"):
                opp_val = getattr(value, "presentation_ToolTip", None)
                if opp_val is None:
                    setattr(value, "presentation_ToolTip", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Shell(self):
        return self.__presentation_Shell

    @presentation_Shell.setter
    def presentation_Shell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Shell__presentation_Shell", None)
        self.__presentation_Shell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Shell194"):
                opp_val = getattr(old_value, "presentation_Shell194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Shell194"):
                opp_val = getattr(value, "presentation_Shell194", None)
                if opp_val is None:
                    setattr(value, "presentation_Shell194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Shell194(self):
        return self.__presentation_Shell194

    @presentation_Shell194.setter
    def presentation_Shell194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Shell__presentation_Shell194", None)
        self.__presentation_Shell194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Shell"):
                    opp_val = getattr(item, "presentation_Shell", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Shell", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Shell"):
                    opp_val = getattr(item, "presentation_Shell", None)
                    
                    setattr(item, "presentation_Shell", self)
                    

class presentation_Resource(ABC):

    def __init__(self, mixed: str):
        self.mixed = mixed
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class presentation_RowData:

    def __init__(self, mixed: str, exclude: str, height: str, width: str):
        self.mixed = mixed
        self.exclude = exclude
        self.height = height
        self.width = width
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def exclude(self) -> str:
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: str):
        self.__exclude = exclude

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

class presentation_Observable:

    def __init__(self, mixed: str):
        self.mixed = mixed
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class AbstractDataProvider:

    pass
class presentation_XMLDataProvider(AbstractDataProvider):

    def __init__(self, group1: str, xPath: str, presentation_XMLDataProvider: set["presentation_Document"] = None, presentation_XMLDataProvider306: set["presentation_URL"] = None):
        self.group1 = group1
        self.xPath = xPath
        self.presentation_XMLDataProvider = presentation_XMLDataProvider if presentation_XMLDataProvider is not None else set()
        self.presentation_XMLDataProvider306 = presentation_XMLDataProvider306 if presentation_XMLDataProvider306 is not None else set()
        
    @property
    def xPath(self) -> str:
        return self.__xPath

    @xPath.setter
    def xPath(self, xPath: str):
        self.__xPath = xPath

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def presentation_XMLDataProvider(self):
        return self.__presentation_XMLDataProvider

    @presentation_XMLDataProvider.setter
    def presentation_XMLDataProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_XMLDataProvider__presentation_XMLDataProvider", None)
        self.__presentation_XMLDataProvider = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Document"):
                    opp_val = getattr(item, "presentation_Document", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Document", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Document"):
                    opp_val = getattr(item, "presentation_Document", None)
                    
                    setattr(item, "presentation_Document", self)
                    

    @property
    def presentation_XMLDataProvider306(self):
        return self.__presentation_XMLDataProvider306

    @presentation_XMLDataProvider306.setter
    def presentation_XMLDataProvider306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_XMLDataProvider__presentation_XMLDataProvider306", None)
        self.__presentation_XMLDataProvider306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_URL"):
                    opp_val = getattr(item, "presentation_URL", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_URL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_URL"):
                    opp_val = getattr(item, "presentation_URL", None)
                    
                    setattr(item, "presentation_URL", self)
                    

class presentation_ObjectDataProvider(AbstractDataProvider):

    def __init__(self, group1: str, methodName: str, presentation_ObjectDataProvider180: set["presentation_EObject"] = None, presentation_ObjectDataProvider: set["presentation_Class"] = None, presentation_ObjectDataProvider183: set["presentation_List"] = None):
        self.group1 = group1
        self.methodName = methodName
        self.presentation_ObjectDataProvider180 = presentation_ObjectDataProvider180 if presentation_ObjectDataProvider180 is not None else set()
        self.presentation_ObjectDataProvider = presentation_ObjectDataProvider if presentation_ObjectDataProvider is not None else set()
        self.presentation_ObjectDataProvider183 = presentation_ObjectDataProvider183 if presentation_ObjectDataProvider183 is not None else set()
        
    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def presentation_ObjectDataProvider180(self):
        return self.__presentation_ObjectDataProvider180

    @presentation_ObjectDataProvider180.setter
    def presentation_ObjectDataProvider180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ObjectDataProvider__presentation_ObjectDataProvider180", None)
        self.__presentation_ObjectDataProvider180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject181"):
                    opp_val = getattr(item, "presentation_EObject181", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject181"):
                    opp_val = getattr(item, "presentation_EObject181", None)
                    
                    setattr(item, "presentation_EObject181", self)
                    

    @property
    def presentation_ObjectDataProvider(self):
        return self.__presentation_ObjectDataProvider

    @presentation_ObjectDataProvider.setter
    def presentation_ObjectDataProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ObjectDataProvider__presentation_ObjectDataProvider", None)
        self.__presentation_ObjectDataProvider = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Class"):
                    opp_val = getattr(item, "presentation_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Class"):
                    opp_val = getattr(item, "presentation_Class", None)
                    
                    setattr(item, "presentation_Class", self)
                    

    @property
    def presentation_ObjectDataProvider183(self):
        return self.__presentation_ObjectDataProvider183

    @presentation_ObjectDataProvider183.setter
    def presentation_ObjectDataProvider183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ObjectDataProvider__presentation_ObjectDataProvider183", None)
        self.__presentation_ObjectDataProvider183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_List184"):
                    opp_val = getattr(item, "presentation_List184", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_List184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_List184"):
                    opp_val = getattr(item, "presentation_List184", None)
                    
                    setattr(item, "presentation_List184", self)
                    

class Dialog:

    pass
class presentation_TrayDialog(Dialog):

    def __init__(self, group2: str, helpAvailable: str, presentation_TrayDialog: set["presentation_DialogTray"] = None):
        self.group2 = group2
        self.helpAvailable = helpAvailable
        self.presentation_TrayDialog = presentation_TrayDialog if presentation_TrayDialog is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def helpAvailable(self) -> str:
        return self.__helpAvailable

    @helpAvailable.setter
    def helpAvailable(self, helpAvailable: str):
        self.__helpAvailable = helpAvailable

    @property
    def presentation_TrayDialog(self):
        return self.__presentation_TrayDialog

    @presentation_TrayDialog.setter
    def presentation_TrayDialog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TrayDialog__presentation_TrayDialog", None)
        self.__presentation_TrayDialog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_DialogTray"):
                    opp_val = getattr(item, "presentation_DialogTray", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_DialogTray", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_DialogTray"):
                    opp_val = getattr(item, "presentation_DialogTray", None)
                    
                    setattr(item, "presentation_DialogTray", self)
                    

class presentation_MessageBox(Dialog):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class presentation_Listener(ABC):

    def __init__(self, mixed: str):
        self.mixed = mixed
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class presentation_ISelection(ABC):

    def __init__(self, mixed: str, presentation_ISelection: "presentation_Viewer" = None):
        self.mixed = mixed
        self.presentation_ISelection = presentation_ISelection
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ISelection(self):
        return self.__presentation_ISelection

    @presentation_ISelection.setter
    def presentation_ISelection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ISelection__presentation_ISelection", None)
        self.__presentation_ISelection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Viewer298"):
                opp_val = getattr(old_value, "presentation_Viewer298", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Viewer298"):
                opp_val = getattr(value, "presentation_Viewer298", None)
                if opp_val is None:
                    setattr(value, "presentation_Viewer298", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_TextStyle:

    def __init__(self, mixed: str, presentation_TextStyle: "presentation_IME" = None):
        self.mixed = mixed
        self.presentation_TextStyle = presentation_TextStyle
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_TextStyle(self):
        return self.__presentation_TextStyle

    @presentation_TextStyle.setter
    def presentation_TextStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TextStyle__presentation_TextStyle", None)
        self.__presentation_TextStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_IME153"):
                opp_val = getattr(old_value, "presentation_IME153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_IME153"):
                opp_val = getattr(value, "presentation_IME153", None)
                if opp_val is None:
                    setattr(value, "presentation_IME153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_IElementComparer(ABC):

    def __init__(self, mixed: str, presentation_IElementComparer: "presentation_StructuredViewer" = None):
        self.mixed = mixed
        self.presentation_IElementComparer = presentation_IElementComparer
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_IElementComparer(self):
        return self.__presentation_IElementComparer

    @presentation_IElementComparer.setter
    def presentation_IElementComparer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IElementComparer__presentation_IElementComparer", None)
        self.__presentation_IElementComparer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_StructuredViewer200"):
                opp_val = getattr(old_value, "presentation_StructuredViewer200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_StructuredViewer200"):
                opp_val = getattr(value, "presentation_StructuredViewer200", None)
                if opp_val is None:
                    setattr(value, "presentation_StructuredViewer200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_GridData:

    def __init__(self, exclude: str, grabExcessHorizontalSpace: str, mixed: str, minimumHeight: str, minimumWidth: str, verticalAlignment: str, grabExcessVerticalSpace: str, heightHint: str, horizontalAlignment: str, horizontalIndent: str, horizontalSpan: str, verticalIndent: str, verticalSpan: str, widthHint: str):
        self.exclude = exclude
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.mixed = mixed
        self.minimumHeight = minimumHeight
        self.minimumWidth = minimumWidth
        self.verticalAlignment = verticalAlignment
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.heightHint = heightHint
        self.horizontalAlignment = horizontalAlignment
        self.horizontalIndent = horizontalIndent
        self.horizontalSpan = horizontalSpan
        self.verticalIndent = verticalIndent
        self.verticalSpan = verticalSpan
        self.widthHint = widthHint
        
    @property
    def grabExcessHorizontalSpace(self) -> str:
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: str):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace

    @property
    def minimumHeight(self) -> str:
        return self.__minimumHeight

    @minimumHeight.setter
    def minimumHeight(self, minimumHeight: str):
        self.__minimumHeight = minimumHeight

    @property
    def horizontalSpan(self) -> str:
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: str):
        self.__horizontalSpan = horizontalSpan

    @property
    def verticalIndent(self) -> str:
        return self.__verticalIndent

    @verticalIndent.setter
    def verticalIndent(self, verticalIndent: str):
        self.__verticalIndent = verticalIndent

    @property
    def exclude(self) -> str:
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: str):
        self.__exclude = exclude

    @property
    def horizontalIndent(self) -> str:
        return self.__horizontalIndent

    @horizontalIndent.setter
    def horizontalIndent(self, horizontalIndent: str):
        self.__horizontalIndent = horizontalIndent

    @property
    def heightHint(self) -> str:
        return self.__heightHint

    @heightHint.setter
    def heightHint(self, heightHint: str):
        self.__heightHint = heightHint

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def widthHint(self) -> str:
        return self.__widthHint

    @widthHint.setter
    def widthHint(self, widthHint: str):
        self.__widthHint = widthHint

    @property
    def minimumWidth(self) -> str:
        return self.__minimumWidth

    @minimumWidth.setter
    def minimumWidth(self, minimumWidth: str):
        self.__minimumWidth = minimumWidth

    @property
    def verticalSpan(self) -> str:
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: str):
        self.__verticalSpan = verticalSpan

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def grabExcessVerticalSpace(self) -> str:
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: str):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace

class presentation_FormData:

    def __init__(self, mixed: str, group: str, height: str, width: str, presentation_FormData147: set["presentation_FormAttachment"] = None, presentation_FormData: set["presentation_FormAttachment"] = None, presentation_FormData144: set["presentation_FormAttachment"] = None, presentation_FormData150: set["presentation_FormAttachment"] = None):
        self.mixed = mixed
        self.group = group
        self.height = height
        self.width = width
        self.presentation_FormData147 = presentation_FormData147 if presentation_FormData147 is not None else set()
        self.presentation_FormData = presentation_FormData if presentation_FormData is not None else set()
        self.presentation_FormData144 = presentation_FormData144 if presentation_FormData144 is not None else set()
        self.presentation_FormData150 = presentation_FormData150 if presentation_FormData150 is not None else set()
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def presentation_FormData150(self):
        return self.__presentation_FormData150

    @presentation_FormData150.setter
    def presentation_FormData150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormData__presentation_FormData150", None)
        self.__presentation_FormData150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FormAttachment151"):
                    opp_val = getattr(item, "presentation_FormAttachment151", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FormAttachment151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FormAttachment151"):
                    opp_val = getattr(item, "presentation_FormAttachment151", None)
                    
                    setattr(item, "presentation_FormAttachment151", self)
                    

    @property
    def presentation_FormData144(self):
        return self.__presentation_FormData144

    @presentation_FormData144.setter
    def presentation_FormData144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormData__presentation_FormData144", None)
        self.__presentation_FormData144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FormAttachment145"):
                    opp_val = getattr(item, "presentation_FormAttachment145", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FormAttachment145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FormAttachment145"):
                    opp_val = getattr(item, "presentation_FormAttachment145", None)
                    
                    setattr(item, "presentation_FormAttachment145", self)
                    

    @property
    def presentation_FormData(self):
        return self.__presentation_FormData

    @presentation_FormData.setter
    def presentation_FormData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormData__presentation_FormData", None)
        self.__presentation_FormData = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FormAttachment142"):
                    opp_val = getattr(item, "presentation_FormAttachment142", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FormAttachment142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FormAttachment142"):
                    opp_val = getattr(item, "presentation_FormAttachment142", None)
                    
                    setattr(item, "presentation_FormAttachment142", self)
                    

    @property
    def presentation_FormData147(self):
        return self.__presentation_FormData147

    @presentation_FormData147.setter
    def presentation_FormData147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormData__presentation_FormData147", None)
        self.__presentation_FormData147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FormAttachment148"):
                    opp_val = getattr(item, "presentation_FormAttachment148", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FormAttachment148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FormAttachment148"):
                    opp_val = getattr(item, "presentation_FormAttachment148", None)
                    
                    setattr(item, "presentation_FormAttachment148", self)
                    

class presentation_FormAttachment:

    def __init__(self, group: str, mixed: str, alignment: str, denominator: str, numerator: str, offset: str, presentation_FormAttachment: set["presentation_Control"] = None, presentation_FormAttachment142: "presentation_FormData" = None, presentation_FormAttachment145: "presentation_FormData" = None, presentation_FormAttachment148: "presentation_FormData" = None, presentation_FormAttachment151: "presentation_FormData" = None):
        self.group = group
        self.mixed = mixed
        self.alignment = alignment
        self.denominator = denominator
        self.numerator = numerator
        self.offset = offset
        self.presentation_FormAttachment = presentation_FormAttachment if presentation_FormAttachment is not None else set()
        self.presentation_FormAttachment142 = presentation_FormAttachment142
        self.presentation_FormAttachment145 = presentation_FormAttachment145
        self.presentation_FormAttachment148 = presentation_FormAttachment148
        self.presentation_FormAttachment151 = presentation_FormAttachment151
        
    @property
    def numerator(self) -> str:
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator: str):
        self.__numerator = numerator

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def denominator(self) -> str:
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: str):
        self.__denominator = denominator

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def presentation_FormAttachment142(self):
        return self.__presentation_FormAttachment142

    @presentation_FormAttachment142.setter
    def presentation_FormAttachment142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormAttachment__presentation_FormAttachment142", None)
        self.__presentation_FormAttachment142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_FormData"):
                opp_val = getattr(old_value, "presentation_FormData", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_FormData"):
                opp_val = getattr(value, "presentation_FormData", None)
                if opp_val is None:
                    setattr(value, "presentation_FormData", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_FormAttachment145(self):
        return self.__presentation_FormAttachment145

    @presentation_FormAttachment145.setter
    def presentation_FormAttachment145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormAttachment__presentation_FormAttachment145", None)
        self.__presentation_FormAttachment145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_FormData144"):
                opp_val = getattr(old_value, "presentation_FormData144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_FormData144"):
                opp_val = getattr(value, "presentation_FormData144", None)
                if opp_val is None:
                    setattr(value, "presentation_FormData144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_FormAttachment(self):
        return self.__presentation_FormAttachment

    @presentation_FormAttachment.setter
    def presentation_FormAttachment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormAttachment__presentation_FormAttachment", None)
        self.__presentation_FormAttachment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control140"):
                    opp_val = getattr(item, "presentation_Control140", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control140"):
                    opp_val = getattr(item, "presentation_Control140", None)
                    
                    setattr(item, "presentation_Control140", self)
                    

    @property
    def presentation_FormAttachment148(self):
        return self.__presentation_FormAttachment148

    @presentation_FormAttachment148.setter
    def presentation_FormAttachment148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormAttachment__presentation_FormAttachment148", None)
        self.__presentation_FormAttachment148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_FormData147"):
                opp_val = getattr(old_value, "presentation_FormData147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_FormData147"):
                opp_val = getattr(value, "presentation_FormData147", None)
                if opp_val is None:
                    setattr(value, "presentation_FormData147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_FormAttachment151(self):
        return self.__presentation_FormAttachment151

    @presentation_FormAttachment151.setter
    def presentation_FormAttachment151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FormAttachment__presentation_FormAttachment151", None)
        self.__presentation_FormAttachment151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_FormData150"):
                opp_val = getattr(old_value, "presentation_FormData150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_FormData150"):
                opp_val = getattr(value, "presentation_FormData150", None)
                if opp_val is None:
                    setattr(value, "presentation_FormData150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Layout:

    pass
class presentation_RowLayout(Layout):

    def __init__(self, center: str, fill: str, justify: str, marginWidth: str, pack: str, spacing: str, marginBottom: str, marginHeight: str, marginLeft: str, marginRight: str, marginTop: str, type: str, wrap: str):
        self.center = center
        self.fill = fill
        self.justify = justify
        self.marginWidth = marginWidth
        self.pack = pack
        self.spacing = spacing
        self.marginBottom = marginBottom
        self.marginHeight = marginHeight
        self.marginLeft = marginLeft
        self.marginRight = marginRight
        self.marginTop = marginTop
        self.type = type
        self.wrap = wrap
        
    @property
    def marginWidth(self) -> str:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: str):
        self.__marginWidth = marginWidth

    @property
    def center(self) -> str:
        return self.__center

    @center.setter
    def center(self, center: str):
        self.__center = center

    @property
    def justify(self) -> str:
        return self.__justify

    @justify.setter
    def justify(self, justify: str):
        self.__justify = justify

    @property
    def marginRight(self) -> str:
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: str):
        self.__marginRight = marginRight

    @property
    def pack(self) -> str:
        return self.__pack

    @pack.setter
    def pack(self, pack: str):
        self.__pack = pack

    @property
    def spacing(self) -> str:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: str):
        self.__spacing = spacing

    @property
    def wrap(self) -> str:
        return self.__wrap

    @wrap.setter
    def wrap(self, wrap: str):
        self.__wrap = wrap

    @property
    def fill(self) -> str:
        return self.__fill

    @fill.setter
    def fill(self, fill: str):
        self.__fill = fill

    @property
    def marginTop(self) -> str:
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: str):
        self.__marginTop = marginTop

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def marginLeft(self) -> str:
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: str):
        self.__marginLeft = marginLeft

    @property
    def marginHeight(self) -> str:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: str):
        self.__marginHeight = marginHeight

    @property
    def marginBottom(self) -> str:
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: str):
        self.__marginBottom = marginBottom

class presentation_FormLayout(Layout):

    def __init__(self, marginHeight: str, marginLeft: str, marginBottom: str, marginRight: str, marginTop: str, marginWidth: str, spacing: str):
        self.marginHeight = marginHeight
        self.marginLeft = marginLeft
        self.marginBottom = marginBottom
        self.marginRight = marginRight
        self.marginTop = marginTop
        self.marginWidth = marginWidth
        self.spacing = spacing
        
    @property
    def marginHeight(self) -> str:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: str):
        self.__marginHeight = marginHeight

    @property
    def marginBottom(self) -> str:
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: str):
        self.__marginBottom = marginBottom

    @property
    def marginWidth(self) -> str:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: str):
        self.__marginWidth = marginWidth

    @property
    def marginTop(self) -> str:
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: str):
        self.__marginTop = marginTop

    @property
    def marginRight(self) -> str:
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: str):
        self.__marginRight = marginRight

    @property
    def marginLeft(self) -> str:
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: str):
        self.__marginLeft = marginLeft

    @property
    def spacing(self) -> str:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: str):
        self.__spacing = spacing

class presentation_StackLayout(Layout):

    def __init__(self, marginHeight: str, marginWidth: str, group: str, presentation_StackLayout: set["presentation_Control"] = None):
        self.marginHeight = marginHeight
        self.marginWidth = marginWidth
        self.group = group
        self.presentation_StackLayout = presentation_StackLayout if presentation_StackLayout is not None else set()
        
    @property
    def marginHeight(self) -> str:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: str):
        self.__marginHeight = marginHeight

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def marginWidth(self) -> str:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: str):
        self.__marginWidth = marginWidth

    @property
    def presentation_StackLayout(self):
        return self.__presentation_StackLayout

    @presentation_StackLayout.setter
    def presentation_StackLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StackLayout__presentation_StackLayout", None)
        self.__presentation_StackLayout = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control197"):
                    opp_val = getattr(item, "presentation_Control197", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control197"):
                    opp_val = getattr(item, "presentation_Control197", None)
                    
                    setattr(item, "presentation_Control197", self)
                    

class presentation_GridLayout(Layout):

    def __init__(self, horizontalSpacing: str, makeColumnsEqualWidth: str, marginBottom: str, marginWidth: str, numColumns: str, marginHeight: str, marginLeft: str, marginRight: str, marginTop: str, verticalSpacing: str):
        self.horizontalSpacing = horizontalSpacing
        self.makeColumnsEqualWidth = makeColumnsEqualWidth
        self.marginBottom = marginBottom
        self.marginWidth = marginWidth
        self.numColumns = numColumns
        self.marginHeight = marginHeight
        self.marginLeft = marginLeft
        self.marginRight = marginRight
        self.marginTop = marginTop
        self.verticalSpacing = verticalSpacing
        
    @property
    def verticalSpacing(self) -> str:
        return self.__verticalSpacing

    @verticalSpacing.setter
    def verticalSpacing(self, verticalSpacing: str):
        self.__verticalSpacing = verticalSpacing

    @property
    def marginBottom(self) -> str:
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: str):
        self.__marginBottom = marginBottom

    @property
    def horizontalSpacing(self) -> str:
        return self.__horizontalSpacing

    @horizontalSpacing.setter
    def horizontalSpacing(self, horizontalSpacing: str):
        self.__horizontalSpacing = horizontalSpacing

    @property
    def marginTop(self) -> str:
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: str):
        self.__marginTop = marginTop

    @property
    def marginRight(self) -> str:
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: str):
        self.__marginRight = marginRight

    @property
    def marginHeight(self) -> str:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: str):
        self.__marginHeight = marginHeight

    @property
    def marginLeft(self) -> str:
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: str):
        self.__marginLeft = marginLeft

    @property
    def numColumns(self) -> str:
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: str):
        self.__numColumns = numColumns

    @property
    def makeColumnsEqualWidth(self) -> str:
        return self.__makeColumnsEqualWidth

    @makeColumnsEqualWidth.setter
    def makeColumnsEqualWidth(self, makeColumnsEqualWidth: str):
        self.__makeColumnsEqualWidth = makeColumnsEqualWidth

    @property
    def marginWidth(self) -> str:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: str):
        self.__marginWidth = marginWidth

class presentation_FillLayout(Layout):

    def __init__(self, marginWidth: str, marginHeight: str, spacing: str, type: str):
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.spacing = spacing
        self.type = type
        
    @property
    def marginHeight(self) -> str:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: str):
        self.__marginHeight = marginHeight

    @property
    def spacing(self) -> str:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: str):
        self.__spacing = spacing

    @property
    def marginWidth(self) -> str:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: str):
        self.__marginWidth = marginWidth

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class DocumentObject:

    pass
class presentation_Element(DocumentObject):

    pass
class presentation_EStringToStringMapEntry:

    pass
class presentation_Window(ABC):

    def __init__(self, mixed: str, group: str, blockOnOpen: str, presentation_Window: "presentation_DocumentRoot" = None, presentation_Window303: set["presentation_WindowManager"] = None):
        self.mixed = mixed
        self.group = group
        self.blockOnOpen = blockOnOpen
        self.presentation_Window = presentation_Window
        self.presentation_Window303 = presentation_Window303 if presentation_Window303 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def blockOnOpen(self) -> str:
        return self.__blockOnOpen

    @blockOnOpen.setter
    def blockOnOpen(self, blockOnOpen: str):
        self.__blockOnOpen = blockOnOpen

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Window303(self):
        return self.__presentation_Window303

    @presentation_Window303.setter
    def presentation_Window303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Window__presentation_Window303", None)
        self.__presentation_Window303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_WindowManager"):
                    opp_val = getattr(item, "presentation_WindowManager", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_WindowManager", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_WindowManager"):
                    opp_val = getattr(item, "presentation_WindowManager", None)
                    
                    setattr(item, "presentation_WindowManager", self)
                    

    @property
    def presentation_Window(self):
        return self.__presentation_Window

    @presentation_Window.setter
    def presentation_Window(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Window__presentation_Window", None)
        self.__presentation_Window = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot131"):
                opp_val = getattr(old_value, "presentation_DocumentRoot131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot131"):
                opp_val = getattr(value, "presentation_DocumentRoot131", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Observable:

    pass
class presentation_DocumentObject(Observable):

    pass
class presentation_Document(ABC):

    def __init__(self, mixed: str, presentation_Document: "presentation_XMLDataProvider" = None):
        self.mixed = mixed
        self.presentation_Document = presentation_Document
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Document(self):
        return self.__presentation_Document

    @presentation_Document.setter
    def presentation_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Document__presentation_Document", None)
        self.__presentation_Document = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_XMLDataProvider"):
                opp_val = getattr(old_value, "presentation_XMLDataProvider", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_XMLDataProvider"):
                opp_val = getattr(value, "presentation_XMLDataProvider", None)
                if opp_val is None:
                    setattr(value, "presentation_XMLDataProvider", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_DialogTray(ABC):

    def __init__(self, mixed: str, presentation_DialogTray: "presentation_TrayDialog" = None):
        self.mixed = mixed
        self.presentation_DialogTray = presentation_DialogTray
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_DialogTray(self):
        return self.__presentation_DialogTray

    @presentation_DialogTray.setter
    def presentation_DialogTray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DialogTray__presentation_DialogTray", None)
        self.__presentation_DialogTray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TrayDialog"):
                opp_val = getattr(old_value, "presentation_TrayDialog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TrayDialog"):
                opp_val = getattr(value, "presentation_TrayDialog", None)
                if opp_val is None:
                    setattr(value, "presentation_TrayDialog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_DocumentRoot:

    def __init__(self, mixed: str, presentation_DocumentRoot131: set["presentation_Window"] = None, presentation_DocumentRoot: set["presentation_EStringToStringMapEntry"] = None, presentation_DocumentRoot125: set["presentation_EStringToStringMapEntry"] = None, presentation_DocumentRoot128: set["presentation_Composite"] = None):
        self.mixed = mixed
        self.presentation_DocumentRoot131 = presentation_DocumentRoot131 if presentation_DocumentRoot131 is not None else set()
        self.presentation_DocumentRoot = presentation_DocumentRoot if presentation_DocumentRoot is not None else set()
        self.presentation_DocumentRoot125 = presentation_DocumentRoot125 if presentation_DocumentRoot125 is not None else set()
        self.presentation_DocumentRoot128 = presentation_DocumentRoot128 if presentation_DocumentRoot128 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_DocumentRoot(self):
        return self.__presentation_DocumentRoot

    @presentation_DocumentRoot.setter
    def presentation_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot", None)
        self.__presentation_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EStringToStringMapEntry"):
                    opp_val = getattr(item, "presentation_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EStringToStringMapEntry"):
                    opp_val = getattr(item, "presentation_EStringToStringMapEntry", None)
                    
                    setattr(item, "presentation_EStringToStringMapEntry", self)
                    

    @property
    def presentation_DocumentRoot128(self):
        return self.__presentation_DocumentRoot128

    @presentation_DocumentRoot128.setter
    def presentation_DocumentRoot128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot128", None)
        self.__presentation_DocumentRoot128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Composite129"):
                    opp_val = getattr(item, "presentation_Composite129", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Composite129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Composite129"):
                    opp_val = getattr(item, "presentation_Composite129", None)
                    
                    setattr(item, "presentation_Composite129", self)
                    

    @property
    def presentation_DocumentRoot131(self):
        return self.__presentation_DocumentRoot131

    @presentation_DocumentRoot131.setter
    def presentation_DocumentRoot131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot131", None)
        self.__presentation_DocumentRoot131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Window"):
                    opp_val = getattr(item, "presentation_Window", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Window", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Window"):
                    opp_val = getattr(item, "presentation_Window", None)
                    
                    setattr(item, "presentation_Window", self)
                    

    @property
    def presentation_DocumentRoot125(self):
        return self.__presentation_DocumentRoot125

    @presentation_DocumentRoot125.setter
    def presentation_DocumentRoot125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot125", None)
        self.__presentation_DocumentRoot125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EStringToStringMapEntry126"):
                    opp_val = getattr(item, "presentation_EStringToStringMapEntry126", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EStringToStringMapEntry126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EStringToStringMapEntry126"):
                    opp_val = getattr(item, "presentation_EStringToStringMapEntry126", None)
                    
                    setattr(item, "presentation_EStringToStringMapEntry126", self)
                    

class presentation_IDialogBlockedHandler(ABC):

    def __init__(self, mixed: str, presentation_IDialogBlockedHandler: "presentation_Dialog" = None):
        self.mixed = mixed
        self.presentation_IDialogBlockedHandler = presentation_IDialogBlockedHandler
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_IDialogBlockedHandler(self):
        return self.__presentation_IDialogBlockedHandler

    @presentation_IDialogBlockedHandler.setter
    def presentation_IDialogBlockedHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IDialogBlockedHandler__presentation_IDialogBlockedHandler", None)
        self.__presentation_IDialogBlockedHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Dialog122"):
                opp_val = getattr(old_value, "presentation_Dialog122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Dialog122"):
                opp_val = getattr(value, "presentation_Dialog122", None)
                if opp_val is None:
                    setattr(value, "presentation_Dialog122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Window:

    pass
class presentation_Dialog(Window):

    def __init__(self, group1: str, presentation_Dialog: set["presentation_Control"] = None, presentation_Dialog122: set["presentation_IDialogBlockedHandler"] = None):
        self.group1 = group1
        self.presentation_Dialog = presentation_Dialog if presentation_Dialog is not None else set()
        self.presentation_Dialog122 = presentation_Dialog122 if presentation_Dialog122 is not None else set()
        
    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def presentation_Dialog122(self):
        return self.__presentation_Dialog122

    @presentation_Dialog122.setter
    def presentation_Dialog122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Dialog__presentation_Dialog122", None)
        self.__presentation_Dialog122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IDialogBlockedHandler"):
                    opp_val = getattr(item, "presentation_IDialogBlockedHandler", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IDialogBlockedHandler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IDialogBlockedHandler"):
                    opp_val = getattr(item, "presentation_IDialogBlockedHandler", None)
                    
                    setattr(item, "presentation_IDialogBlockedHandler", self)
                    

    @property
    def presentation_Dialog(self):
        return self.__presentation_Dialog

    @presentation_Dialog.setter
    def presentation_Dialog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Dialog__presentation_Dialog", None)
        self.__presentation_Dialog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control120"):
                    opp_val = getattr(item, "presentation_Control120", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control120"):
                    opp_val = getattr(item, "presentation_Control120", None)
                    
                    setattr(item, "presentation_Control120", self)
                    

class presentation_DefaultLabelProvider:

    def __init__(self, mixed: str):
        self.mixed = mixed
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class presentation_DefaultCellModifier:

    def __init__(self, mixed: str):
        self.mixed = mixed
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class Resource:

    pass
class presentation_RGB:

    def __init__(self, mixed: str, presentation_RGB: "presentation_CTabFolder" = None, presentation_RGB101: "presentation_CTabFolder" = None, presentation_RGB107: "presentation_CTabFolder" = None, presentation_RGB252: "presentation_TitleAreaDialog" = None):
        self.mixed = mixed
        self.presentation_RGB = presentation_RGB
        self.presentation_RGB101 = presentation_RGB101
        self.presentation_RGB107 = presentation_RGB107
        self.presentation_RGB252 = presentation_RGB252
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_RGB101(self):
        return self.__presentation_RGB101

    @presentation_RGB101.setter
    def presentation_RGB101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_RGB__presentation_RGB101", None)
        self.__presentation_RGB101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabFolder100"):
                opp_val = getattr(old_value, "presentation_CTabFolder100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabFolder100"):
                opp_val = getattr(value, "presentation_CTabFolder100", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabFolder100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_RGB(self):
        return self.__presentation_RGB

    @presentation_RGB.setter
    def presentation_RGB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_RGB__presentation_RGB", None)
        self.__presentation_RGB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabFolder"):
                opp_val = getattr(old_value, "presentation_CTabFolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabFolder"):
                opp_val = getattr(value, "presentation_CTabFolder", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabFolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_RGB252(self):
        return self.__presentation_RGB252

    @presentation_RGB252.setter
    def presentation_RGB252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_RGB__presentation_RGB252", None)
        self.__presentation_RGB252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TitleAreaDialog"):
                opp_val = getattr(old_value, "presentation_TitleAreaDialog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TitleAreaDialog"):
                opp_val = getattr(value, "presentation_TitleAreaDialog", None)
                if opp_val is None:
                    setattr(value, "presentation_TitleAreaDialog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_RGB107(self):
        return self.__presentation_RGB107

    @presentation_RGB107.setter
    def presentation_RGB107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_RGB__presentation_RGB107", None)
        self.__presentation_RGB107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabFolder106"):
                opp_val = getattr(old_value, "presentation_CTabFolder106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabFolder106"):
                opp_val = getattr(value, "presentation_CTabFolder106", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabFolder106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Item:

    pass
class presentation_TrayItem(Item):

    pass
class presentation_CTabItem(Item):

    def __init__(self, group: str, bounds: str, disabledImage: str, font: str, showClose: str, toolTipText: str, presentation_CTabItem104: "presentation_CTabFolder" = None, presentation_CTabItem: "presentation_CTabFolder" = None, presentation_CTabItem109: set["presentation_CTabFolder"] = None, presentation_CTabItem112: set["presentation_Control"] = None):
        self.group = group
        self.bounds = bounds
        self.disabledImage = disabledImage
        self.font = font
        self.showClose = showClose
        self.toolTipText = toolTipText
        self.presentation_CTabItem104 = presentation_CTabItem104
        self.presentation_CTabItem = presentation_CTabItem
        self.presentation_CTabItem109 = presentation_CTabItem109 if presentation_CTabItem109 is not None else set()
        self.presentation_CTabItem112 = presentation_CTabItem112 if presentation_CTabItem112 is not None else set()
        
    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def showClose(self) -> str:
        return self.__showClose

    @showClose.setter
    def showClose(self, showClose: str):
        self.__showClose = showClose

    @property
    def disabledImage(self) -> str:
        return self.__disabledImage

    @disabledImage.setter
    def disabledImage(self, disabledImage: str):
        self.__disabledImage = disabledImage

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def presentation_CTabItem112(self):
        return self.__presentation_CTabItem112

    @presentation_CTabItem112.setter
    def presentation_CTabItem112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabItem__presentation_CTabItem112", None)
        self.__presentation_CTabItem112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control113"):
                    opp_val = getattr(item, "presentation_Control113", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control113"):
                    opp_val = getattr(item, "presentation_Control113", None)
                    
                    setattr(item, "presentation_Control113", self)
                    

    @property
    def presentation_CTabItem109(self):
        return self.__presentation_CTabItem109

    @presentation_CTabItem109.setter
    def presentation_CTabItem109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabItem__presentation_CTabItem109", None)
        self.__presentation_CTabItem109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CTabFolder110"):
                    opp_val = getattr(item, "presentation_CTabFolder110", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CTabFolder110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CTabFolder110"):
                    opp_val = getattr(item, "presentation_CTabFolder110", None)
                    
                    setattr(item, "presentation_CTabFolder110", self)
                    

    @property
    def presentation_CTabItem(self):
        return self.__presentation_CTabItem

    @presentation_CTabItem.setter
    def presentation_CTabItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabItem__presentation_CTabItem", None)
        self.__presentation_CTabItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabFolder95"):
                opp_val = getattr(old_value, "presentation_CTabFolder95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabFolder95"):
                opp_val = getattr(value, "presentation_CTabFolder95", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabFolder95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_CTabItem104(self):
        return self.__presentation_CTabItem104

    @presentation_CTabItem104.setter
    def presentation_CTabItem104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabItem__presentation_CTabItem104", None)
        self.__presentation_CTabItem104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabFolder103"):
                opp_val = getattr(old_value, "presentation_CTabFolder103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabFolder103"):
                opp_val = getattr(value, "presentation_CTabFolder103", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabFolder103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_TreeColumn(Item):

    def __init__(self, group: str, alignment: str, moveable: str, resizable: str, toolTipText: str, width: str, presentation_TreeColumn: "presentation_Tree" = None, presentation_TreeColumn271: "presentation_Tree" = None, presentation_TreeColumn282: set["presentation_Tree"] = None):
        self.group = group
        self.alignment = alignment
        self.moveable = moveable
        self.resizable = resizable
        self.toolTipText = toolTipText
        self.width = width
        self.presentation_TreeColumn = presentation_TreeColumn
        self.presentation_TreeColumn271 = presentation_TreeColumn271
        self.presentation_TreeColumn282 = presentation_TreeColumn282 if presentation_TreeColumn282 is not None else set()
        
    @property
    def resizable(self) -> str:
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: str):
        self.__resizable = resizable

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def moveable(self) -> str:
        return self.__moveable

    @moveable.setter
    def moveable(self, moveable: str):
        self.__moveable = moveable

    @property
    def presentation_TreeColumn282(self):
        return self.__presentation_TreeColumn282

    @presentation_TreeColumn282.setter
    def presentation_TreeColumn282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeColumn__presentation_TreeColumn282", None)
        self.__presentation_TreeColumn282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Tree283"):
                    opp_val = getattr(item, "presentation_Tree283", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Tree283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Tree283"):
                    opp_val = getattr(item, "presentation_Tree283", None)
                    
                    setattr(item, "presentation_Tree283", self)
                    

    @property
    def presentation_TreeColumn(self):
        return self.__presentation_TreeColumn

    @presentation_TreeColumn.setter
    def presentation_TreeColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeColumn__presentation_TreeColumn", None)
        self.__presentation_TreeColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Tree"):
                opp_val = getattr(old_value, "presentation_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Tree"):
                opp_val = getattr(value, "presentation_Tree", None)
                if opp_val is None:
                    setattr(value, "presentation_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeColumn271(self):
        return self.__presentation_TreeColumn271

    @presentation_TreeColumn271.setter
    def presentation_TreeColumn271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeColumn__presentation_TreeColumn271", None)
        self.__presentation_TreeColumn271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Tree270"):
                opp_val = getattr(old_value, "presentation_Tree270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Tree270"):
                opp_val = getattr(value, "presentation_Tree270", None)
                if opp_val is None:
                    setattr(value, "presentation_Tree270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ExpandItem(Item):

    def __init__(self, group: str, expanded: str, height: str, presentation_ExpandItem: "presentation_ExpandBar" = None, presentation_ExpandItem134: set["presentation_ExpandBar"] = None, presentation_ExpandItem137: set["presentation_Control"] = None):
        self.group = group
        self.expanded = expanded
        self.height = height
        self.presentation_ExpandItem = presentation_ExpandItem
        self.presentation_ExpandItem134 = presentation_ExpandItem134 if presentation_ExpandItem134 is not None else set()
        self.presentation_ExpandItem137 = presentation_ExpandItem137 if presentation_ExpandItem137 is not None else set()
        
    @property
    def expanded(self) -> str:
        return self.__expanded

    @expanded.setter
    def expanded(self, expanded: str):
        self.__expanded = expanded

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_ExpandItem(self):
        return self.__presentation_ExpandItem

    @presentation_ExpandItem.setter
    def presentation_ExpandItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ExpandItem__presentation_ExpandItem", None)
        self.__presentation_ExpandItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ExpandBar"):
                opp_val = getattr(old_value, "presentation_ExpandBar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ExpandBar"):
                opp_val = getattr(value, "presentation_ExpandBar", None)
                if opp_val is None:
                    setattr(value, "presentation_ExpandBar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_ExpandItem134(self):
        return self.__presentation_ExpandItem134

    @presentation_ExpandItem134.setter
    def presentation_ExpandItem134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ExpandItem__presentation_ExpandItem134", None)
        self.__presentation_ExpandItem134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ExpandBar135"):
                    opp_val = getattr(item, "presentation_ExpandBar135", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ExpandBar135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ExpandBar135"):
                    opp_val = getattr(item, "presentation_ExpandBar135", None)
                    
                    setattr(item, "presentation_ExpandBar135", self)
                    

    @property
    def presentation_ExpandItem137(self):
        return self.__presentation_ExpandItem137

    @presentation_ExpandItem137.setter
    def presentation_ExpandItem137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ExpandItem__presentation_ExpandItem137", None)
        self.__presentation_ExpandItem137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control138"):
                    opp_val = getattr(item, "presentation_Control138", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control138"):
                    opp_val = getattr(item, "presentation_Control138", None)
                    
                    setattr(item, "presentation_Control138", self)
                    

class presentation_TreeItem(Item):

    def __init__(self, group: str, texts: str, checked: str, expanded: str, grayed: str, itemCount: str, handle: str, presentation_TreeItem: "presentation_Tree" = None, presentation_TreeItem274: "presentation_Tree" = None, presentation_TreeItem277: "presentation_Tree" = None, presentation_TreeItem280: "presentation_Tree" = None, presentation_TreeItem286: "presentation_TreeItem" = None, presentation_TreeItem284: set["presentation_TreeItem"] = None, presentation_TreeItem289: "presentation_TreeItem" = None, presentation_TreeItem287: set["presentation_TreeItem"] = None, presentation_TreeItem291: set["presentation_Tree"] = None):
        self.group = group
        self.texts = texts
        self.checked = checked
        self.expanded = expanded
        self.grayed = grayed
        self.itemCount = itemCount
        self.handle = handle
        self.presentation_TreeItem = presentation_TreeItem
        self.presentation_TreeItem274 = presentation_TreeItem274
        self.presentation_TreeItem277 = presentation_TreeItem277
        self.presentation_TreeItem280 = presentation_TreeItem280
        self.presentation_TreeItem286 = presentation_TreeItem286
        self.presentation_TreeItem284 = presentation_TreeItem284 if presentation_TreeItem284 is not None else set()
        self.presentation_TreeItem289 = presentation_TreeItem289
        self.presentation_TreeItem287 = presentation_TreeItem287 if presentation_TreeItem287 is not None else set()
        self.presentation_TreeItem291 = presentation_TreeItem291 if presentation_TreeItem291 is not None else set()
        
    @property
    def itemCount(self) -> str:
        return self.__itemCount

    @itemCount.setter
    def itemCount(self, itemCount: str):
        self.__itemCount = itemCount

    @property
    def grayed(self) -> str:
        return self.__grayed

    @grayed.setter
    def grayed(self, grayed: str):
        self.__grayed = grayed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def texts(self) -> str:
        return self.__texts

    @texts.setter
    def texts(self, texts: str):
        self.__texts = texts

    @property
    def expanded(self) -> str:
        return self.__expanded

    @expanded.setter
    def expanded(self, expanded: str):
        self.__expanded = expanded

    @property
    def handle(self) -> str:
        return self.__handle

    @handle.setter
    def handle(self, handle: str):
        self.__handle = handle

    @property
    def checked(self) -> str:
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked

    @property
    def presentation_TreeItem277(self):
        return self.__presentation_TreeItem277

    @presentation_TreeItem277.setter
    def presentation_TreeItem277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem277", None)
        self.__presentation_TreeItem277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Tree276"):
                opp_val = getattr(old_value, "presentation_Tree276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Tree276"):
                opp_val = getattr(value, "presentation_Tree276", None)
                if opp_val is None:
                    setattr(value, "presentation_Tree276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeItem280(self):
        return self.__presentation_TreeItem280

    @presentation_TreeItem280.setter
    def presentation_TreeItem280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem280", None)
        self.__presentation_TreeItem280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Tree279"):
                opp_val = getattr(old_value, "presentation_Tree279", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Tree279"):
                opp_val = getattr(value, "presentation_Tree279", None)
                if opp_val is None:
                    setattr(value, "presentation_Tree279", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeItem287(self):
        return self.__presentation_TreeItem287

    @presentation_TreeItem287.setter
    def presentation_TreeItem287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem287", None)
        self.__presentation_TreeItem287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeItem289"):
                    opp_val = getattr(item, "presentation_TreeItem289", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeItem289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeItem289"):
                    opp_val = getattr(item, "presentation_TreeItem289", None)
                    
                    setattr(item, "presentation_TreeItem289", self)
                    

    @property
    def presentation_TreeItem(self):
        return self.__presentation_TreeItem

    @presentation_TreeItem.setter
    def presentation_TreeItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem", None)
        self.__presentation_TreeItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Tree268"):
                opp_val = getattr(old_value, "presentation_Tree268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Tree268"):
                opp_val = getattr(value, "presentation_Tree268", None)
                if opp_val is None:
                    setattr(value, "presentation_Tree268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeItem289(self):
        return self.__presentation_TreeItem289

    @presentation_TreeItem289.setter
    def presentation_TreeItem289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem289", None)
        self.__presentation_TreeItem289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TreeItem287"):
                opp_val = getattr(old_value, "presentation_TreeItem287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TreeItem287"):
                opp_val = getattr(value, "presentation_TreeItem287", None)
                if opp_val is None:
                    setattr(value, "presentation_TreeItem287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeItem274(self):
        return self.__presentation_TreeItem274

    @presentation_TreeItem274.setter
    def presentation_TreeItem274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem274", None)
        self.__presentation_TreeItem274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Tree273"):
                opp_val = getattr(old_value, "presentation_Tree273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Tree273"):
                opp_val = getattr(value, "presentation_Tree273", None)
                if opp_val is None:
                    setattr(value, "presentation_Tree273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeItem284(self):
        return self.__presentation_TreeItem284

    @presentation_TreeItem284.setter
    def presentation_TreeItem284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem284", None)
        self.__presentation_TreeItem284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeItem286"):
                    opp_val = getattr(item, "presentation_TreeItem286", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeItem286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeItem286"):
                    opp_val = getattr(item, "presentation_TreeItem286", None)
                    
                    setattr(item, "presentation_TreeItem286", self)
                    

    @property
    def presentation_TreeItem286(self):
        return self.__presentation_TreeItem286

    @presentation_TreeItem286.setter
    def presentation_TreeItem286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem286", None)
        self.__presentation_TreeItem286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TreeItem284"):
                opp_val = getattr(old_value, "presentation_TreeItem284", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TreeItem284"):
                opp_val = getattr(value, "presentation_TreeItem284", None)
                if opp_val is None:
                    setattr(value, "presentation_TreeItem284", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TreeItem291(self):
        return self.__presentation_TreeItem291

    @presentation_TreeItem291.setter
    def presentation_TreeItem291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreeItem__presentation_TreeItem291", None)
        self.__presentation_TreeItem291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Tree292"):
                    opp_val = getattr(item, "presentation_Tree292", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Tree292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Tree292"):
                    opp_val = getattr(item, "presentation_Tree292", None)
                    
                    setattr(item, "presentation_Tree292", self)
                    

class presentation_ToolItem(Item):

    def __init__(self, group: str, enabled: str, hotImage: str, selection: str, toolTipText: str, width: str, bounds: str, disabledImage: str, presentation_ToolItem: "presentation_ToolBar" = None, presentation_ToolItem255: set["presentation_Control"] = None, presentation_ToolItem258: set["presentation_ToolBar"] = None):
        self.group = group
        self.enabled = enabled
        self.hotImage = hotImage
        self.selection = selection
        self.toolTipText = toolTipText
        self.width = width
        self.bounds = bounds
        self.disabledImage = disabledImage
        self.presentation_ToolItem = presentation_ToolItem
        self.presentation_ToolItem255 = presentation_ToolItem255 if presentation_ToolItem255 is not None else set()
        self.presentation_ToolItem258 = presentation_ToolItem258 if presentation_ToolItem258 is not None else set()
        
    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def hotImage(self) -> str:
        return self.__hotImage

    @hotImage.setter
    def hotImage(self, hotImage: str):
        self.__hotImage = hotImage

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def disabledImage(self) -> str:
        return self.__disabledImage

    @disabledImage.setter
    def disabledImage(self, disabledImage: str):
        self.__disabledImage = disabledImage

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def presentation_ToolItem255(self):
        return self.__presentation_ToolItem255

    @presentation_ToolItem255.setter
    def presentation_ToolItem255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ToolItem__presentation_ToolItem255", None)
        self.__presentation_ToolItem255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control256"):
                    opp_val = getattr(item, "presentation_Control256", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control256"):
                    opp_val = getattr(item, "presentation_Control256", None)
                    
                    setattr(item, "presentation_Control256", self)
                    

    @property
    def presentation_ToolItem258(self):
        return self.__presentation_ToolItem258

    @presentation_ToolItem258.setter
    def presentation_ToolItem258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ToolItem__presentation_ToolItem258", None)
        self.__presentation_ToolItem258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ToolBar259"):
                    opp_val = getattr(item, "presentation_ToolBar259", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ToolBar259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ToolBar259"):
                    opp_val = getattr(item, "presentation_ToolBar259", None)
                    
                    setattr(item, "presentation_ToolBar259", self)
                    

    @property
    def presentation_ToolItem(self):
        return self.__presentation_ToolItem

    @presentation_ToolItem.setter
    def presentation_ToolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ToolItem__presentation_ToolItem", None)
        self.__presentation_ToolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ToolBar"):
                opp_val = getattr(old_value, "presentation_ToolBar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ToolBar"):
                opp_val = getattr(value, "presentation_ToolBar", None)
                if opp_val is None:
                    setattr(value, "presentation_ToolBar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_TabItem(Item):

    def __init__(self, group: str, bounds: str, toolTipText: str, presentation_TabItem: "presentation_TabFolder" = None, presentation_TabItem214: "presentation_TabFolder" = None, presentation_TabItem216: set["presentation_TabFolder"] = None, presentation_TabItem219: set["presentation_Control"] = None):
        self.group = group
        self.bounds = bounds
        self.toolTipText = toolTipText
        self.presentation_TabItem = presentation_TabItem
        self.presentation_TabItem214 = presentation_TabItem214
        self.presentation_TabItem216 = presentation_TabItem216 if presentation_TabItem216 is not None else set()
        self.presentation_TabItem219 = presentation_TabItem219 if presentation_TabItem219 is not None else set()
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_TabItem214(self):
        return self.__presentation_TabItem214

    @presentation_TabItem214.setter
    def presentation_TabItem214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabItem__presentation_TabItem214", None)
        self.__presentation_TabItem214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TabFolder213"):
                opp_val = getattr(old_value, "presentation_TabFolder213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TabFolder213"):
                opp_val = getattr(value, "presentation_TabFolder213", None)
                if opp_val is None:
                    setattr(value, "presentation_TabFolder213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TabItem219(self):
        return self.__presentation_TabItem219

    @presentation_TabItem219.setter
    def presentation_TabItem219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabItem__presentation_TabItem219", None)
        self.__presentation_TabItem219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control220"):
                    opp_val = getattr(item, "presentation_Control220", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control220"):
                    opp_val = getattr(item, "presentation_Control220", None)
                    
                    setattr(item, "presentation_Control220", self)
                    

    @property
    def presentation_TabItem(self):
        return self.__presentation_TabItem

    @presentation_TabItem.setter
    def presentation_TabItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabItem__presentation_TabItem", None)
        self.__presentation_TabItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TabFolder"):
                opp_val = getattr(old_value, "presentation_TabFolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TabFolder"):
                opp_val = getattr(value, "presentation_TabFolder", None)
                if opp_val is None:
                    setattr(value, "presentation_TabFolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TabItem216(self):
        return self.__presentation_TabItem216

    @presentation_TabItem216.setter
    def presentation_TabItem216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabItem__presentation_TabItem216", None)
        self.__presentation_TabItem216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TabFolder217"):
                    opp_val = getattr(item, "presentation_TabFolder217", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TabFolder217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TabFolder217"):
                    opp_val = getattr(item, "presentation_TabFolder217", None)
                    
                    setattr(item, "presentation_TabFolder217", self)
                    

class presentation_TableColumn(Item):

    def __init__(self, group: str, alignment: str, resizable: str, toolTipText: str, width: str, moveable: str, presentation_TableColumn: "presentation_Table" = None, presentation_TableColumn224: "presentation_Table" = None, presentation_TableColumn232: set["presentation_Element"] = None, presentation_TableColumn234: set["presentation_Table"] = None, presentation_TableColumn250: "presentation_TableViewerColumn" = None):
        self.group = group
        self.alignment = alignment
        self.resizable = resizable
        self.toolTipText = toolTipText
        self.width = width
        self.moveable = moveable
        self.presentation_TableColumn = presentation_TableColumn
        self.presentation_TableColumn224 = presentation_TableColumn224
        self.presentation_TableColumn232 = presentation_TableColumn232 if presentation_TableColumn232 is not None else set()
        self.presentation_TableColumn234 = presentation_TableColumn234 if presentation_TableColumn234 is not None else set()
        self.presentation_TableColumn250 = presentation_TableColumn250
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def resizable(self) -> str:
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: str):
        self.__resizable = resizable

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def moveable(self) -> str:
        return self.__moveable

    @moveable.setter
    def moveable(self, moveable: str):
        self.__moveable = moveable

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def presentation_TableColumn234(self):
        return self.__presentation_TableColumn234

    @presentation_TableColumn234.setter
    def presentation_TableColumn234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableColumn__presentation_TableColumn234", None)
        self.__presentation_TableColumn234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Table235"):
                    opp_val = getattr(item, "presentation_Table235", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Table235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Table235"):
                    opp_val = getattr(item, "presentation_Table235", None)
                    
                    setattr(item, "presentation_Table235", self)
                    

    @property
    def presentation_TableColumn250(self):
        return self.__presentation_TableColumn250

    @presentation_TableColumn250.setter
    def presentation_TableColumn250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableColumn__presentation_TableColumn250", None)
        self.__presentation_TableColumn250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableViewerColumn"):
                opp_val = getattr(old_value, "presentation_TableViewerColumn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableViewerColumn"):
                opp_val = getattr(value, "presentation_TableViewerColumn", None)
                if opp_val is None:
                    setattr(value, "presentation_TableViewerColumn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TableColumn(self):
        return self.__presentation_TableColumn

    @presentation_TableColumn.setter
    def presentation_TableColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableColumn__presentation_TableColumn", None)
        self.__presentation_TableColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Table"):
                opp_val = getattr(old_value, "presentation_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Table"):
                opp_val = getattr(value, "presentation_Table", None)
                if opp_val is None:
                    setattr(value, "presentation_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TableColumn232(self):
        return self.__presentation_TableColumn232

    @presentation_TableColumn232.setter
    def presentation_TableColumn232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableColumn__presentation_TableColumn232", None)
        self.__presentation_TableColumn232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Element"):
                    opp_val = getattr(item, "presentation_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Element"):
                    opp_val = getattr(item, "presentation_Element", None)
                    
                    setattr(item, "presentation_Element", self)
                    

    @property
    def presentation_TableColumn224(self):
        return self.__presentation_TableColumn224

    @presentation_TableColumn224.setter
    def presentation_TableColumn224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableColumn__presentation_TableColumn224", None)
        self.__presentation_TableColumn224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Table223"):
                opp_val = getattr(old_value, "presentation_Table223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Table223"):
                opp_val = getattr(value, "presentation_Table223", None)
                if opp_val is None:
                    setattr(value, "presentation_Table223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_MenuItem(Item):

    def __init__(self, group: str, selection: str, accelerator: str, enabled: str, presentation_MenuItem159: "presentation_Menu" = None, presentation_MenuItem: "presentation_Menu" = None, presentation_MenuItem162: "presentation_Menu" = None, presentation_MenuItem173: set["presentation_ICommand"] = None, presentation_MenuItem170: set["presentation_Menu"] = None, presentation_MenuItem176: set["presentation_Menu"] = None):
        self.group = group
        self.selection = selection
        self.accelerator = accelerator
        self.enabled = enabled
        self.presentation_MenuItem159 = presentation_MenuItem159
        self.presentation_MenuItem = presentation_MenuItem
        self.presentation_MenuItem162 = presentation_MenuItem162
        self.presentation_MenuItem173 = presentation_MenuItem173 if presentation_MenuItem173 is not None else set()
        self.presentation_MenuItem170 = presentation_MenuItem170 if presentation_MenuItem170 is not None else set()
        self.presentation_MenuItem176 = presentation_MenuItem176 if presentation_MenuItem176 is not None else set()
        
    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def accelerator(self) -> str:
        return self.__accelerator

    @accelerator.setter
    def accelerator(self, accelerator: str):
        self.__accelerator = accelerator

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_MenuItem162(self):
        return self.__presentation_MenuItem162

    @presentation_MenuItem162.setter
    def presentation_MenuItem162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_MenuItem__presentation_MenuItem162", None)
        self.__presentation_MenuItem162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Menu161"):
                opp_val = getattr(old_value, "presentation_Menu161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Menu161"):
                opp_val = getattr(value, "presentation_Menu161", None)
                if opp_val is None:
                    setattr(value, "presentation_Menu161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_MenuItem159(self):
        return self.__presentation_MenuItem159

    @presentation_MenuItem159.setter
    def presentation_MenuItem159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_MenuItem__presentation_MenuItem159", None)
        self.__presentation_MenuItem159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Menu158"):
                opp_val = getattr(old_value, "presentation_Menu158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Menu158"):
                opp_val = getattr(value, "presentation_Menu158", None)
                if opp_val is None:
                    setattr(value, "presentation_Menu158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_MenuItem176(self):
        return self.__presentation_MenuItem176

    @presentation_MenuItem176.setter
    def presentation_MenuItem176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_MenuItem__presentation_MenuItem176", None)
        self.__presentation_MenuItem176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Menu177"):
                    opp_val = getattr(item, "presentation_Menu177", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Menu177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Menu177"):
                    opp_val = getattr(item, "presentation_Menu177", None)
                    
                    setattr(item, "presentation_Menu177", self)
                    

    @property
    def presentation_MenuItem(self):
        return self.__presentation_MenuItem

    @presentation_MenuItem.setter
    def presentation_MenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_MenuItem__presentation_MenuItem", None)
        self.__presentation_MenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Menu156"):
                opp_val = getattr(old_value, "presentation_Menu156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Menu156"):
                opp_val = getattr(value, "presentation_Menu156", None)
                if opp_val is None:
                    setattr(value, "presentation_Menu156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_MenuItem170(self):
        return self.__presentation_MenuItem170

    @presentation_MenuItem170.setter
    def presentation_MenuItem170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_MenuItem__presentation_MenuItem170", None)
        self.__presentation_MenuItem170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Menu171"):
                    opp_val = getattr(item, "presentation_Menu171", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Menu171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Menu171"):
                    opp_val = getattr(item, "presentation_Menu171", None)
                    
                    setattr(item, "presentation_Menu171", self)
                    

    @property
    def presentation_MenuItem173(self):
        return self.__presentation_MenuItem173

    @presentation_MenuItem173.setter
    def presentation_MenuItem173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_MenuItem__presentation_MenuItem173", None)
        self.__presentation_MenuItem173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ICommand174"):
                    opp_val = getattr(item, "presentation_ICommand174", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ICommand174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ICommand174"):
                    opp_val = getattr(item, "presentation_ICommand174", None)
                    
                    setattr(item, "presentation_ICommand174", self)
                    

class presentation_CoolItem(Item):

    def __init__(self, bounds: str, minimumSize: str, group: str, preferredSize: str, size: str, presentation_CoolItem: "presentation_CoolBar" = None, presentation_CoolItem91: set["presentation_Control"] = None, presentation_CoolItem88: set["presentation_CoolBar"] = None):
        self.bounds = bounds
        self.minimumSize = minimumSize
        self.group = group
        self.preferredSize = preferredSize
        self.size = size
        self.presentation_CoolItem = presentation_CoolItem
        self.presentation_CoolItem91 = presentation_CoolItem91 if presentation_CoolItem91 is not None else set()
        self.presentation_CoolItem88 = presentation_CoolItem88 if presentation_CoolItem88 is not None else set()
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def preferredSize(self) -> str:
        return self.__preferredSize

    @preferredSize.setter
    def preferredSize(self, preferredSize: str):
        self.__preferredSize = preferredSize

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def minimumSize(self) -> str:
        return self.__minimumSize

    @minimumSize.setter
    def minimumSize(self, minimumSize: str):
        self.__minimumSize = minimumSize

    @property
    def presentation_CoolItem91(self):
        return self.__presentation_CoolItem91

    @presentation_CoolItem91.setter
    def presentation_CoolItem91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CoolItem__presentation_CoolItem91", None)
        self.__presentation_CoolItem91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control92"):
                    opp_val = getattr(item, "presentation_Control92", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control92"):
                    opp_val = getattr(item, "presentation_Control92", None)
                    
                    setattr(item, "presentation_Control92", self)
                    

    @property
    def presentation_CoolItem88(self):
        return self.__presentation_CoolItem88

    @presentation_CoolItem88.setter
    def presentation_CoolItem88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CoolItem__presentation_CoolItem88", None)
        self.__presentation_CoolItem88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CoolBar89"):
                    opp_val = getattr(item, "presentation_CoolBar89", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CoolBar89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CoolBar89"):
                    opp_val = getattr(item, "presentation_CoolBar89", None)
                    
                    setattr(item, "presentation_CoolBar89", self)
                    

    @property
    def presentation_CoolItem(self):
        return self.__presentation_CoolItem

    @presentation_CoolItem.setter
    def presentation_CoolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CoolItem__presentation_CoolItem", None)
        self.__presentation_CoolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CoolBar"):
                opp_val = getattr(old_value, "presentation_CoolBar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CoolBar"):
                opp_val = getattr(value, "presentation_CoolBar", None)
                if opp_val is None:
                    setattr(value, "presentation_CoolBar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ControlEditor:

    def __init__(self, grabHorizontal: str, grabVertical: str, horizontalAlignment: str, mixed: str, group: str, verticalAlignment: str, minimumHeight: str, minimumWidth: str, presentation_ControlEditor: set["presentation_Control"] = None):
        self.grabHorizontal = grabHorizontal
        self.grabVertical = grabVertical
        self.horizontalAlignment = horizontalAlignment
        self.mixed = mixed
        self.group = group
        self.verticalAlignment = verticalAlignment
        self.minimumHeight = minimumHeight
        self.minimumWidth = minimumWidth
        self.presentation_ControlEditor = presentation_ControlEditor if presentation_ControlEditor is not None else set()
        
    @property
    def minimumHeight(self) -> str:
        return self.__minimumHeight

    @minimumHeight.setter
    def minimumHeight(self, minimumHeight: str):
        self.__minimumHeight = minimumHeight

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def grabHorizontal(self) -> str:
        return self.__grabHorizontal

    @grabHorizontal.setter
    def grabHorizontal(self, grabHorizontal: str):
        self.__grabHorizontal = grabHorizontal

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def minimumWidth(self) -> str:
        return self.__minimumWidth

    @minimumWidth.setter
    def minimumWidth(self, minimumWidth: str):
        self.__minimumWidth = minimumWidth

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def grabVertical(self) -> str:
        return self.__grabVertical

    @grabVertical.setter
    def grabVertical(self, grabVertical: str):
        self.__grabVertical = grabVertical

    @property
    def presentation_ControlEditor(self):
        return self.__presentation_ControlEditor

    @presentation_ControlEditor.setter
    def presentation_ControlEditor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ControlEditor__presentation_ControlEditor", None)
        self.__presentation_ControlEditor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control85"):
                    opp_val = getattr(item, "presentation_Control85", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control85"):
                    opp_val = getattr(item, "presentation_Control85", None)
                    
                    setattr(item, "presentation_Control85", self)
                    

class presentation_Cursor(Resource):

    pass
class presentation_IContentProvider(ABC):

    def __init__(self, mixed: str, presentation_IContentProvider: "presentation_ContentViewer" = None):
        self.mixed = mixed
        self.presentation_IContentProvider = presentation_IContentProvider
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_IContentProvider(self):
        return self.__presentation_IContentProvider

    @presentation_IContentProvider.setter
    def presentation_IContentProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IContentProvider__presentation_IContentProvider", None)
        self.__presentation_IContentProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ContentViewer"):
                opp_val = getattr(old_value, "presentation_ContentViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ContentViewer"):
                opp_val = getattr(value, "presentation_ContentViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_ContentViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Viewer:

    pass
class presentation_ContentViewer(Viewer):

    def __init__(self, group1: str, presentation_ContentViewer: set["presentation_IContentProvider"] = None, presentation_ContentViewer73: set["presentation_IBaseLabelProvider"] = None):
        self.group1 = group1
        self.presentation_ContentViewer = presentation_ContentViewer if presentation_ContentViewer is not None else set()
        self.presentation_ContentViewer73 = presentation_ContentViewer73 if presentation_ContentViewer73 is not None else set()
        
    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def presentation_ContentViewer(self):
        return self.__presentation_ContentViewer

    @presentation_ContentViewer.setter
    def presentation_ContentViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ContentViewer__presentation_ContentViewer", None)
        self.__presentation_ContentViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IContentProvider"):
                    opp_val = getattr(item, "presentation_IContentProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IContentProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IContentProvider"):
                    opp_val = getattr(item, "presentation_IContentProvider", None)
                    
                    setattr(item, "presentation_IContentProvider", self)
                    

    @property
    def presentation_ContentViewer73(self):
        return self.__presentation_ContentViewer73

    @presentation_ContentViewer73.setter
    def presentation_ContentViewer73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ContentViewer__presentation_ContentViewer73", None)
        self.__presentation_ContentViewer73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IBaseLabelProvider74"):
                    opp_val = getattr(item, "presentation_IBaseLabelProvider74", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IBaseLabelProvider74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IBaseLabelProvider74"):
                    opp_val = getattr(item, "presentation_IBaseLabelProvider74", None)
                    
                    setattr(item, "presentation_IBaseLabelProvider74", self)
                    

class presentation_Layout(ABC):

    def __init__(self, mixed: str, presentation_Layout: "presentation_Composite" = None):
        self.mixed = mixed
        self.presentation_Layout = presentation_Layout
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Layout(self):
        return self.__presentation_Layout

    @presentation_Layout.setter
    def presentation_Layout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Layout__presentation_Layout", None)
        self.__presentation_Layout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Composite70"):
                opp_val = getattr(old_value, "presentation_Composite70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Composite70"):
                opp_val = getattr(value, "presentation_Composite70", None)
                if opp_val is None:
                    setattr(value, "presentation_Composite70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Scrollable:

    pass
class presentation_Text(Scrollable):

    def __init__(self, caretLocation: str, doubleClickEnabled: str, echoChar: str, editable: str, lineDelimiter: str, message: str, selection: str, selectionText: str, tabs: str, text: str, textLimit: str, orientation: str, topIndex: str):
        self.caretLocation = caretLocation
        self.doubleClickEnabled = doubleClickEnabled
        self.echoChar = echoChar
        self.editable = editable
        self.lineDelimiter = lineDelimiter
        self.message = message
        self.selection = selection
        self.selectionText = selectionText
        self.tabs = tabs
        self.text = text
        self.textLimit = textLimit
        self.orientation = orientation
        self.topIndex = topIndex
        
    @property
    def topIndex(self) -> str:
        return self.__topIndex

    @topIndex.setter
    def topIndex(self, topIndex: str):
        self.__topIndex = topIndex

    @property
    def textLimit(self) -> str:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: str):
        self.__textLimit = textLimit

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def editable(self) -> str:
        return self.__editable

    @editable.setter
    def editable(self, editable: str):
        self.__editable = editable

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def lineDelimiter(self) -> str:
        return self.__lineDelimiter

    @lineDelimiter.setter
    def lineDelimiter(self, lineDelimiter: str):
        self.__lineDelimiter = lineDelimiter

    @property
    def selectionText(self) -> str:
        return self.__selectionText

    @selectionText.setter
    def selectionText(self, selectionText: str):
        self.__selectionText = selectionText

    @property
    def tabs(self) -> str:
        return self.__tabs

    @tabs.setter
    def tabs(self, tabs: str):
        self.__tabs = tabs

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def echoChar(self) -> str:
        return self.__echoChar

    @echoChar.setter
    def echoChar(self, echoChar: str):
        self.__echoChar = echoChar

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def doubleClickEnabled(self) -> str:
        return self.__doubleClickEnabled

    @doubleClickEnabled.setter
    def doubleClickEnabled(self, doubleClickEnabled: str):
        self.__doubleClickEnabled = doubleClickEnabled

    @property
    def caretLocation(self) -> str:
        return self.__caretLocation

    @caretLocation.setter
    def caretLocation(self, caretLocation: str):
        self.__caretLocation = caretLocation

class presentation_List(Scrollable):

    def __init__(self, selection: str, selectionIndices: str, group2: str, items: str, topIndex: str, presentation_List: "presentation_ListViewer" = None, presentation_List184: "presentation_ObjectDataProvider" = None):
        self.selection = selection
        self.selectionIndices = selectionIndices
        self.group2 = group2
        self.items = items
        self.topIndex = topIndex
        self.presentation_List = presentation_List
        self.presentation_List184 = presentation_List184
        
    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def selectionIndices(self) -> str:
        return self.__selectionIndices

    @selectionIndices.setter
    def selectionIndices(self, selectionIndices: str):
        self.__selectionIndices = selectionIndices

    @property
    def topIndex(self) -> str:
        return self.__topIndex

    @topIndex.setter
    def topIndex(self, topIndex: str):
        self.__topIndex = topIndex

    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def presentation_List(self):
        return self.__presentation_List

    @presentation_List.setter
    def presentation_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_List__presentation_List", None)
        self.__presentation_List = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ListViewer"):
                opp_val = getattr(old_value, "presentation_ListViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ListViewer"):
                opp_val = getattr(value, "presentation_ListViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_ListViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_List184(self):
        return self.__presentation_List184

    @presentation_List184.setter
    def presentation_List184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_List__presentation_List184", None)
        self.__presentation_List184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ObjectDataProvider183"):
                opp_val = getattr(old_value, "presentation_ObjectDataProvider183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ObjectDataProvider183"):
                opp_val = getattr(value, "presentation_ObjectDataProvider183", None)
                if opp_val is None:
                    setattr(value, "presentation_ObjectDataProvider183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_Composite(Scrollable):

    def __init__(self, group2: str, backgroundMode: str, layoutDeferred: str, presentation_Composite: set["presentation_Control"] = None, presentation_Composite67: set["presentation_Control"] = None, presentation_Composite70: set["presentation_Layout"] = None, presentation_Composite129: "presentation_DocumentRoot" = None):
        self.group2 = group2
        self.backgroundMode = backgroundMode
        self.layoutDeferred = layoutDeferred
        self.presentation_Composite = presentation_Composite if presentation_Composite is not None else set()
        self.presentation_Composite67 = presentation_Composite67 if presentation_Composite67 is not None else set()
        self.presentation_Composite70 = presentation_Composite70 if presentation_Composite70 is not None else set()
        self.presentation_Composite129 = presentation_Composite129
        
    @property
    def layoutDeferred(self) -> str:
        return self.__layoutDeferred

    @layoutDeferred.setter
    def layoutDeferred(self, layoutDeferred: str):
        self.__layoutDeferred = layoutDeferred

    @property
    def backgroundMode(self) -> str:
        return self.__backgroundMode

    @backgroundMode.setter
    def backgroundMode(self, backgroundMode: str):
        self.__backgroundMode = backgroundMode

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def presentation_Composite(self):
        return self.__presentation_Composite

    @presentation_Composite.setter
    def presentation_Composite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Composite__presentation_Composite", None)
        self.__presentation_Composite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control65"):
                    opp_val = getattr(item, "presentation_Control65", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control65"):
                    opp_val = getattr(item, "presentation_Control65", None)
                    
                    setattr(item, "presentation_Control65", self)
                    

    @property
    def presentation_Composite67(self):
        return self.__presentation_Composite67

    @presentation_Composite67.setter
    def presentation_Composite67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Composite__presentation_Composite67", None)
        self.__presentation_Composite67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control68"):
                    opp_val = getattr(item, "presentation_Control68", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control68"):
                    opp_val = getattr(item, "presentation_Control68", None)
                    
                    setattr(item, "presentation_Control68", self)
                    

    @property
    def presentation_Composite70(self):
        return self.__presentation_Composite70

    @presentation_Composite70.setter
    def presentation_Composite70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Composite__presentation_Composite70", None)
        self.__presentation_Composite70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Layout"):
                    opp_val = getattr(item, "presentation_Layout", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Layout", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Layout"):
                    opp_val = getattr(item, "presentation_Layout", None)
                    
                    setattr(item, "presentation_Layout", self)
                    

    @property
    def presentation_Composite129(self):
        return self.__presentation_Composite129

    @presentation_Composite129.setter
    def presentation_Composite129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Composite__presentation_Composite129", None)
        self.__presentation_Composite129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot128"):
                opp_val = getattr(old_value, "presentation_DocumentRoot128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot128"):
                opp_val = getattr(value, "presentation_DocumentRoot128", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractListViewer:

    pass
class presentation_ListViewer(AbstractListViewer):

    def __init__(self, group3: str, presentation_ListViewer: set["presentation_List"] = None):
        self.group3 = group3
        self.presentation_ListViewer = presentation_ListViewer if presentation_ListViewer is not None else set()
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_ListViewer(self):
        return self.__presentation_ListViewer

    @presentation_ListViewer.setter
    def presentation_ListViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ListViewer__presentation_ListViewer", None)
        self.__presentation_ListViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_List"):
                    opp_val = getattr(item, "presentation_List", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_List", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_List"):
                    opp_val = getattr(item, "presentation_List", None)
                    
                    setattr(item, "presentation_List", self)
                    

class presentation_ComboViewer(AbstractListViewer):

    pass
class presentation_IBaseLabelProvider(ABC):

    def __init__(self, mixed: str, presentation_IBaseLabelProvider: "presentation_ComboBoxViewerCellEditor" = None, presentation_IBaseLabelProvider74: "presentation_ContentViewer" = None):
        self.mixed = mixed
        self.presentation_IBaseLabelProvider = presentation_IBaseLabelProvider
        self.presentation_IBaseLabelProvider74 = presentation_IBaseLabelProvider74
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_IBaseLabelProvider(self):
        return self.__presentation_IBaseLabelProvider

    @presentation_IBaseLabelProvider.setter
    def presentation_IBaseLabelProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IBaseLabelProvider__presentation_IBaseLabelProvider", None)
        self.__presentation_IBaseLabelProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ComboBoxViewerCellEditor61"):
                opp_val = getattr(old_value, "presentation_ComboBoxViewerCellEditor61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ComboBoxViewerCellEditor61"):
                opp_val = getattr(value, "presentation_ComboBoxViewerCellEditor61", None)
                if opp_val is None:
                    setattr(value, "presentation_ComboBoxViewerCellEditor61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_IBaseLabelProvider74(self):
        return self.__presentation_IBaseLabelProvider74

    @presentation_IBaseLabelProvider74.setter
    def presentation_IBaseLabelProvider74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IBaseLabelProvider__presentation_IBaseLabelProvider74", None)
        self.__presentation_IBaseLabelProvider74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ContentViewer73"):
                opp_val = getattr(old_value, "presentation_ContentViewer73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ContentViewer73"):
                opp_val = getattr(value, "presentation_ContentViewer73", None)
                if opp_val is None:
                    setattr(value, "presentation_ContentViewer73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_IStructuredContentProvider(ABC):

    def __init__(self, mixed: str, presentation_IStructuredContentProvider: "presentation_ComboBoxViewerCellEditor" = None):
        self.mixed = mixed
        self.presentation_IStructuredContentProvider = presentation_IStructuredContentProvider
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_IStructuredContentProvider(self):
        return self.__presentation_IStructuredContentProvider

    @presentation_IStructuredContentProvider.setter
    def presentation_IStructuredContentProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IStructuredContentProvider__presentation_IStructuredContentProvider", None)
        self.__presentation_IStructuredContentProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ComboBoxViewerCellEditor59"):
                opp_val = getattr(old_value, "presentation_ComboBoxViewerCellEditor59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ComboBoxViewerCellEditor59"):
                opp_val = getattr(value, "presentation_ComboBoxViewerCellEditor59", None)
                if opp_val is None:
                    setattr(value, "presentation_ComboBoxViewerCellEditor59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractComboBoxCellEditor:

    pass
class presentation_ComboBoxCellEditor(AbstractComboBoxCellEditor):

    pass
class presentation_ComboBoxViewerCellEditor(AbstractComboBoxCellEditor):

    def __init__(self, group1: str, presentation_ComboBoxViewerCellEditor: set["presentation_EObject"] = None, presentation_ComboBoxViewerCellEditor59: set["presentation_IStructuredContentProvider"] = None, presentation_ComboBoxViewerCellEditor61: set["presentation_IBaseLabelProvider"] = None, presentation_ComboBoxViewerCellEditor63: set["presentation_ComboViewer"] = None):
        self.group1 = group1
        self.presentation_ComboBoxViewerCellEditor = presentation_ComboBoxViewerCellEditor if presentation_ComboBoxViewerCellEditor is not None else set()
        self.presentation_ComboBoxViewerCellEditor59 = presentation_ComboBoxViewerCellEditor59 if presentation_ComboBoxViewerCellEditor59 is not None else set()
        self.presentation_ComboBoxViewerCellEditor61 = presentation_ComboBoxViewerCellEditor61 if presentation_ComboBoxViewerCellEditor61 is not None else set()
        self.presentation_ComboBoxViewerCellEditor63 = presentation_ComboBoxViewerCellEditor63 if presentation_ComboBoxViewerCellEditor63 is not None else set()
        
    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def presentation_ComboBoxViewerCellEditor61(self):
        return self.__presentation_ComboBoxViewerCellEditor61

    @presentation_ComboBoxViewerCellEditor61.setter
    def presentation_ComboBoxViewerCellEditor61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ComboBoxViewerCellEditor__presentation_ComboBoxViewerCellEditor61", None)
        self.__presentation_ComboBoxViewerCellEditor61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IBaseLabelProvider"):
                    opp_val = getattr(item, "presentation_IBaseLabelProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IBaseLabelProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IBaseLabelProvider"):
                    opp_val = getattr(item, "presentation_IBaseLabelProvider", None)
                    
                    setattr(item, "presentation_IBaseLabelProvider", self)
                    

    @property
    def presentation_ComboBoxViewerCellEditor59(self):
        return self.__presentation_ComboBoxViewerCellEditor59

    @presentation_ComboBoxViewerCellEditor59.setter
    def presentation_ComboBoxViewerCellEditor59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ComboBoxViewerCellEditor__presentation_ComboBoxViewerCellEditor59", None)
        self.__presentation_ComboBoxViewerCellEditor59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IStructuredContentProvider"):
                    opp_val = getattr(item, "presentation_IStructuredContentProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IStructuredContentProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IStructuredContentProvider"):
                    opp_val = getattr(item, "presentation_IStructuredContentProvider", None)
                    
                    setattr(item, "presentation_IStructuredContentProvider", self)
                    

    @property
    def presentation_ComboBoxViewerCellEditor63(self):
        return self.__presentation_ComboBoxViewerCellEditor63

    @presentation_ComboBoxViewerCellEditor63.setter
    def presentation_ComboBoxViewerCellEditor63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ComboBoxViewerCellEditor__presentation_ComboBoxViewerCellEditor63", None)
        self.__presentation_ComboBoxViewerCellEditor63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ComboViewer"):
                    opp_val = getattr(item, "presentation_ComboViewer", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ComboViewer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ComboViewer"):
                    opp_val = getattr(item, "presentation_ComboViewer", None)
                    
                    setattr(item, "presentation_ComboViewer", self)
                    

    @property
    def presentation_ComboBoxViewerCellEditor(self):
        return self.__presentation_ComboBoxViewerCellEditor

    @presentation_ComboBoxViewerCellEditor.setter
    def presentation_ComboBoxViewerCellEditor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ComboBoxViewerCellEditor__presentation_ComboBoxViewerCellEditor", None)
        self.__presentation_ComboBoxViewerCellEditor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject57"):
                    opp_val = getattr(item, "presentation_EObject57", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject57"):
                    opp_val = getattr(item, "presentation_EObject57", None)
                    
                    setattr(item, "presentation_EObject57", self)
                    

class presentation_ICellModifier(ABC):

    def __init__(self, mixed: str, presentation_ICellModifier: "presentation_ColumnViewer" = None):
        self.mixed = mixed
        self.presentation_ICellModifier = presentation_ICellModifier
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ICellModifier(self):
        return self.__presentation_ICellModifier

    @presentation_ICellModifier.setter
    def presentation_ICellModifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ICellModifier__presentation_ICellModifier", None)
        self.__presentation_ICellModifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ColumnViewer49"):
                opp_val = getattr(old_value, "presentation_ColumnViewer49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ColumnViewer49"):
                opp_val = getattr(value, "presentation_ColumnViewer49", None)
                if opp_val is None:
                    setattr(value, "presentation_ColumnViewer49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ColumnViewerEditor(ABC):

    def __init__(self, mixed: str, presentation_ColumnViewerEditor: "presentation_ColumnViewer" = None):
        self.mixed = mixed
        self.presentation_ColumnViewerEditor = presentation_ColumnViewerEditor
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ColumnViewerEditor(self):
        return self.__presentation_ColumnViewerEditor

    @presentation_ColumnViewerEditor.setter
    def presentation_ColumnViewerEditor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ColumnViewerEditor__presentation_ColumnViewerEditor", None)
        self.__presentation_ColumnViewerEditor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ColumnViewer"):
                opp_val = getattr(old_value, "presentation_ColumnViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ColumnViewer"):
                opp_val = getattr(value, "presentation_ColumnViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_ColumnViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DialogCellEditor:

    pass
class presentation_ColorCellEditor(DialogCellEditor):

    pass
class presentation_Collection(ABC):

    def __init__(self, mixed: str, presentation_Collection245: "presentation_TableItem" = None, presentation_Collection: "presentation_TableItem" = None):
        self.mixed = mixed
        self.presentation_Collection245 = presentation_Collection245
        self.presentation_Collection = presentation_Collection
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Collection(self):
        return self.__presentation_Collection

    @presentation_Collection.setter
    def presentation_Collection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Collection__presentation_Collection", None)
        self.__presentation_Collection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableItem239"):
                opp_val = getattr(old_value, "presentation_TableItem239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableItem239"):
                opp_val = getattr(value, "presentation_TableItem239", None)
                if opp_val is None:
                    setattr(value, "presentation_TableItem239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Collection245(self):
        return self.__presentation_Collection245

    @presentation_Collection245.setter
    def presentation_Collection245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Collection__presentation_Collection245", None)
        self.__presentation_Collection245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableItem244"):
                opp_val = getattr(old_value, "presentation_TableItem244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableItem244"):
                opp_val = getattr(value, "presentation_TableItem244", None)
                if opp_val is None:
                    setattr(value, "presentation_TableItem244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_Class:

    def __init__(self, mixed: str, presentation_Class: "presentation_ObjectDataProvider" = None):
        self.mixed = mixed
        self.presentation_Class = presentation_Class
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Class(self):
        return self.__presentation_Class

    @presentation_Class.setter
    def presentation_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Class__presentation_Class", None)
        self.__presentation_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ObjectDataProvider"):
                opp_val = getattr(old_value, "presentation_ObjectDataProvider", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ObjectDataProvider"):
                opp_val = getattr(value, "presentation_ObjectDataProvider", None)
                if opp_val is None:
                    setattr(value, "presentation_ObjectDataProvider", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Canvas:

    pass
class presentation_Decorations(Canvas):

    def __init__(self, group4: str, images: str, image: str, maximized: str, minimized: str, text: str, presentation_Decorations: set["presentation_Button"] = None, presentation_Decorations117: set["presentation_Menu"] = None, presentation_Decorations168: "presentation_Menu" = None):
        self.group4 = group4
        self.images = images
        self.image = image
        self.maximized = maximized
        self.minimized = minimized
        self.text = text
        self.presentation_Decorations = presentation_Decorations if presentation_Decorations is not None else set()
        self.presentation_Decorations117 = presentation_Decorations117 if presentation_Decorations117 is not None else set()
        self.presentation_Decorations168 = presentation_Decorations168
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def minimized(self) -> str:
        return self.__minimized

    @minimized.setter
    def minimized(self, minimized: str):
        self.__minimized = minimized

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def images(self) -> str:
        return self.__images

    @images.setter
    def images(self, images: str):
        self.__images = images

    @property
    def group4(self) -> str:
        return self.__group4

    @group4.setter
    def group4(self, group4: str):
        self.__group4 = group4

    @property
    def maximized(self) -> str:
        return self.__maximized

    @maximized.setter
    def maximized(self, maximized: str):
        self.__maximized = maximized

    @property
    def presentation_Decorations117(self):
        return self.__presentation_Decorations117

    @presentation_Decorations117.setter
    def presentation_Decorations117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Decorations__presentation_Decorations117", None)
        self.__presentation_Decorations117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Menu118"):
                    opp_val = getattr(item, "presentation_Menu118", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Menu118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Menu118"):
                    opp_val = getattr(item, "presentation_Menu118", None)
                    
                    setattr(item, "presentation_Menu118", self)
                    

    @property
    def presentation_Decorations(self):
        return self.__presentation_Decorations

    @presentation_Decorations.setter
    def presentation_Decorations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Decorations__presentation_Decorations", None)
        self.__presentation_Decorations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Button115"):
                    opp_val = getattr(item, "presentation_Button115", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Button115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Button115"):
                    opp_val = getattr(item, "presentation_Button115", None)
                    
                    setattr(item, "presentation_Button115", self)
                    

    @property
    def presentation_Decorations168(self):
        return self.__presentation_Decorations168

    @presentation_Decorations168.setter
    def presentation_Decorations168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Decorations__presentation_Decorations168", None)
        self.__presentation_Decorations168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Menu167"):
                opp_val = getattr(old_value, "presentation_Menu167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Menu167"):
                opp_val = getattr(value, "presentation_Menu167", None)
                if opp_val is None:
                    setattr(value, "presentation_Menu167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_StyledText(Canvas):

    def __init__(self, selectionRanges: str, alignment: str, bidiColoring: str, blockSelection: str, caretOffset: str, group4: str, ranges: str, horizontalIndex: str, horizontalPixel: str, indent: str, justify: str, doubleClickEnabled: str, editable: str, orientation: str, selection: str, selectionBackground: str, selectionForeground: str, lineDelimiter: str, lineSpacing: str, textLimit: str, topIndex: str, topPixel: str, wordWrap: str, selectionText: str, tabs: str, text: str, presentation_StyledText207: set["presentation_StyleRange"] = None, presentation_StyledText210: set["presentation_StyledTextContent"] = None, presentation_StyledText: set["presentation_StyleRange"] = None):
        self.selectionRanges = selectionRanges
        self.alignment = alignment
        self.bidiColoring = bidiColoring
        self.blockSelection = blockSelection
        self.caretOffset = caretOffset
        self.group4 = group4
        self.ranges = ranges
        self.horizontalIndex = horizontalIndex
        self.horizontalPixel = horizontalPixel
        self.indent = indent
        self.justify = justify
        self.doubleClickEnabled = doubleClickEnabled
        self.editable = editable
        self.orientation = orientation
        self.selection = selection
        self.selectionBackground = selectionBackground
        self.selectionForeground = selectionForeground
        self.lineDelimiter = lineDelimiter
        self.lineSpacing = lineSpacing
        self.textLimit = textLimit
        self.topIndex = topIndex
        self.topPixel = topPixel
        self.wordWrap = wordWrap
        self.selectionText = selectionText
        self.tabs = tabs
        self.text = text
        self.presentation_StyledText207 = presentation_StyledText207 if presentation_StyledText207 is not None else set()
        self.presentation_StyledText210 = presentation_StyledText210 if presentation_StyledText210 is not None else set()
        self.presentation_StyledText = presentation_StyledText if presentation_StyledText is not None else set()
        
    @property
    def horizontalPixel(self) -> str:
        return self.__horizontalPixel

    @horizontalPixel.setter
    def horizontalPixel(self, horizontalPixel: str):
        self.__horizontalPixel = horizontalPixel

    @property
    def indent(self) -> str:
        return self.__indent

    @indent.setter
    def indent(self, indent: str):
        self.__indent = indent

    @property
    def caretOffset(self) -> str:
        return self.__caretOffset

    @caretOffset.setter
    def caretOffset(self, caretOffset: str):
        self.__caretOffset = caretOffset

    @property
    def editable(self) -> str:
        return self.__editable

    @editable.setter
    def editable(self, editable: str):
        self.__editable = editable

    @property
    def selectionBackground(self) -> str:
        return self.__selectionBackground

    @selectionBackground.setter
    def selectionBackground(self, selectionBackground: str):
        self.__selectionBackground = selectionBackground

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def tabs(self) -> str:
        return self.__tabs

    @tabs.setter
    def tabs(self, tabs: str):
        self.__tabs = tabs

    @property
    def wordWrap(self) -> str:
        return self.__wordWrap

    @wordWrap.setter
    def wordWrap(self, wordWrap: str):
        self.__wordWrap = wordWrap

    @property
    def selectionRanges(self) -> str:
        return self.__selectionRanges

    @selectionRanges.setter
    def selectionRanges(self, selectionRanges: str):
        self.__selectionRanges = selectionRanges

    @property
    def selectionForeground(self) -> str:
        return self.__selectionForeground

    @selectionForeground.setter
    def selectionForeground(self, selectionForeground: str):
        self.__selectionForeground = selectionForeground

    @property
    def group4(self) -> str:
        return self.__group4

    @group4.setter
    def group4(self, group4: str):
        self.__group4 = group4

    @property
    def textLimit(self) -> str:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: str):
        self.__textLimit = textLimit

    @property
    def blockSelection(self) -> str:
        return self.__blockSelection

    @blockSelection.setter
    def blockSelection(self, blockSelection: str):
        self.__blockSelection = blockSelection

    @property
    def topIndex(self) -> str:
        return self.__topIndex

    @topIndex.setter
    def topIndex(self, topIndex: str):
        self.__topIndex = topIndex

    @property
    def doubleClickEnabled(self) -> str:
        return self.__doubleClickEnabled

    @doubleClickEnabled.setter
    def doubleClickEnabled(self, doubleClickEnabled: str):
        self.__doubleClickEnabled = doubleClickEnabled

    @property
    def selectionText(self) -> str:
        return self.__selectionText

    @selectionText.setter
    def selectionText(self, selectionText: str):
        self.__selectionText = selectionText

    @property
    def horizontalIndex(self) -> str:
        return self.__horizontalIndex

    @horizontalIndex.setter
    def horizontalIndex(self, horizontalIndex: str):
        self.__horizontalIndex = horizontalIndex

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def justify(self) -> str:
        return self.__justify

    @justify.setter
    def justify(self, justify: str):
        self.__justify = justify

    @property
    def lineSpacing(self) -> str:
        return self.__lineSpacing

    @lineSpacing.setter
    def lineSpacing(self, lineSpacing: str):
        self.__lineSpacing = lineSpacing

    @property
    def bidiColoring(self) -> str:
        return self.__bidiColoring

    @bidiColoring.setter
    def bidiColoring(self, bidiColoring: str):
        self.__bidiColoring = bidiColoring

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def lineDelimiter(self) -> str:
        return self.__lineDelimiter

    @lineDelimiter.setter
    def lineDelimiter(self, lineDelimiter: str):
        self.__lineDelimiter = lineDelimiter

    @property
    def topPixel(self) -> str:
        return self.__topPixel

    @topPixel.setter
    def topPixel(self, topPixel: str):
        self.__topPixel = topPixel

    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def presentation_StyledText(self):
        return self.__presentation_StyledText

    @presentation_StyledText.setter
    def presentation_StyledText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StyledText__presentation_StyledText", None)
        self.__presentation_StyledText = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_StyleRange"):
                    opp_val = getattr(item, "presentation_StyleRange", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_StyleRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_StyleRange"):
                    opp_val = getattr(item, "presentation_StyleRange", None)
                    
                    setattr(item, "presentation_StyleRange", self)
                    

    @property
    def presentation_StyledText210(self):
        return self.__presentation_StyledText210

    @presentation_StyledText210.setter
    def presentation_StyledText210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StyledText__presentation_StyledText210", None)
        self.__presentation_StyledText210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_StyledTextContent"):
                    opp_val = getattr(item, "presentation_StyledTextContent", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_StyledTextContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_StyledTextContent"):
                    opp_val = getattr(item, "presentation_StyledTextContent", None)
                    
                    setattr(item, "presentation_StyledTextContent", self)
                    

    @property
    def presentation_StyledText207(self):
        return self.__presentation_StyledText207

    @presentation_StyledText207.setter
    def presentation_StyledText207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_StyledText__presentation_StyledText207", None)
        self.__presentation_StyledText207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_StyleRange208"):
                    opp_val = getattr(item, "presentation_StyleRange208", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_StyleRange208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_StyleRange208"):
                    opp_val = getattr(item, "presentation_StyleRange208", None)
                    
                    setattr(item, "presentation_StyleRange208", self)
                    

class presentation_CLabel(Canvas):

    def __init__(self, alignment: str, image: str, text: str):
        self.alignment = alignment
        self.image = image
        self.text = text
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

class TreeViewer:

    pass
class presentation_CheckboxTreeViewer(TreeViewer):

    def __init__(self, group6: str, allChecked: str, presentation_CheckboxTreeViewer: set["presentation_EObject"] = None, presentation_CheckboxTreeViewer42: set["presentation_ICheckStateProvider"] = None, presentation_CheckboxTreeViewer45: set["presentation_EObject"] = None):
        self.group6 = group6
        self.allChecked = allChecked
        self.presentation_CheckboxTreeViewer = presentation_CheckboxTreeViewer if presentation_CheckboxTreeViewer is not None else set()
        self.presentation_CheckboxTreeViewer42 = presentation_CheckboxTreeViewer42 if presentation_CheckboxTreeViewer42 is not None else set()
        self.presentation_CheckboxTreeViewer45 = presentation_CheckboxTreeViewer45 if presentation_CheckboxTreeViewer45 is not None else set()
        
    @property
    def group6(self) -> str:
        return self.__group6

    @group6.setter
    def group6(self, group6: str):
        self.__group6 = group6

    @property
    def allChecked(self) -> str:
        return self.__allChecked

    @allChecked.setter
    def allChecked(self, allChecked: str):
        self.__allChecked = allChecked

    @property
    def presentation_CheckboxTreeViewer42(self):
        return self.__presentation_CheckboxTreeViewer42

    @presentation_CheckboxTreeViewer42.setter
    def presentation_CheckboxTreeViewer42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CheckboxTreeViewer__presentation_CheckboxTreeViewer42", None)
        self.__presentation_CheckboxTreeViewer42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ICheckStateProvider43"):
                    opp_val = getattr(item, "presentation_ICheckStateProvider43", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ICheckStateProvider43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ICheckStateProvider43"):
                    opp_val = getattr(item, "presentation_ICheckStateProvider43", None)
                    
                    setattr(item, "presentation_ICheckStateProvider43", self)
                    

    @property
    def presentation_CheckboxTreeViewer(self):
        return self.__presentation_CheckboxTreeViewer

    @presentation_CheckboxTreeViewer.setter
    def presentation_CheckboxTreeViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CheckboxTreeViewer__presentation_CheckboxTreeViewer", None)
        self.__presentation_CheckboxTreeViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject40"):
                    opp_val = getattr(item, "presentation_EObject40", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject40"):
                    opp_val = getattr(item, "presentation_EObject40", None)
                    
                    setattr(item, "presentation_EObject40", self)
                    

    @property
    def presentation_CheckboxTreeViewer45(self):
        return self.__presentation_CheckboxTreeViewer45

    @presentation_CheckboxTreeViewer45.setter
    def presentation_CheckboxTreeViewer45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CheckboxTreeViewer__presentation_CheckboxTreeViewer45", None)
        self.__presentation_CheckboxTreeViewer45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject46"):
                    opp_val = getattr(item, "presentation_EObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject46"):
                    opp_val = getattr(item, "presentation_EObject46", None)
                    
                    setattr(item, "presentation_EObject46", self)
                    

class presentation_ICheckStateProvider(ABC):

    def __init__(self, mixed: str, presentation_ICheckStateProvider: "presentation_CheckboxTableViewer" = None, presentation_ICheckStateProvider43: "presentation_CheckboxTreeViewer" = None):
        self.mixed = mixed
        self.presentation_ICheckStateProvider = presentation_ICheckStateProvider
        self.presentation_ICheckStateProvider43 = presentation_ICheckStateProvider43
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ICheckStateProvider(self):
        return self.__presentation_ICheckStateProvider

    @presentation_ICheckStateProvider.setter
    def presentation_ICheckStateProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ICheckStateProvider__presentation_ICheckStateProvider", None)
        self.__presentation_ICheckStateProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CheckboxTableViewer35"):
                opp_val = getattr(old_value, "presentation_CheckboxTableViewer35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CheckboxTableViewer35"):
                opp_val = getattr(value, "presentation_CheckboxTableViewer35", None)
                if opp_val is None:
                    setattr(value, "presentation_CheckboxTableViewer35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_ICheckStateProvider43(self):
        return self.__presentation_ICheckStateProvider43

    @presentation_ICheckStateProvider43.setter
    def presentation_ICheckStateProvider43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ICheckStateProvider__presentation_ICheckStateProvider43", None)
        self.__presentation_ICheckStateProvider43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CheckboxTreeViewer42"):
                opp_val = getattr(old_value, "presentation_CheckboxTreeViewer42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CheckboxTreeViewer42"):
                opp_val = getattr(value, "presentation_CheckboxTreeViewer42", None)
                if opp_val is None:
                    setattr(value, "presentation_CheckboxTreeViewer42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TableViewer:

    pass
class presentation_CheckboxTableViewer(TableViewer):

    def __init__(self, allChecked: str, group5: str, allGrayed: str, presentation_CheckboxTableViewer35: set["presentation_ICheckStateProvider"] = None, presentation_CheckboxTableViewer37: set["presentation_EObject"] = None, presentation_CheckboxTableViewer: set["presentation_EObject"] = None):
        self.allChecked = allChecked
        self.group5 = group5
        self.allGrayed = allGrayed
        self.presentation_CheckboxTableViewer35 = presentation_CheckboxTableViewer35 if presentation_CheckboxTableViewer35 is not None else set()
        self.presentation_CheckboxTableViewer37 = presentation_CheckboxTableViewer37 if presentation_CheckboxTableViewer37 is not None else set()
        self.presentation_CheckboxTableViewer = presentation_CheckboxTableViewer if presentation_CheckboxTableViewer is not None else set()
        
    @property
    def allGrayed(self) -> str:
        return self.__allGrayed

    @allGrayed.setter
    def allGrayed(self, allGrayed: str):
        self.__allGrayed = allGrayed

    @property
    def allChecked(self) -> str:
        return self.__allChecked

    @allChecked.setter
    def allChecked(self, allChecked: str):
        self.__allChecked = allChecked

    @property
    def group5(self) -> str:
        return self.__group5

    @group5.setter
    def group5(self, group5: str):
        self.__group5 = group5

    @property
    def presentation_CheckboxTableViewer(self):
        return self.__presentation_CheckboxTableViewer

    @presentation_CheckboxTableViewer.setter
    def presentation_CheckboxTableViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CheckboxTableViewer__presentation_CheckboxTableViewer", None)
        self.__presentation_CheckboxTableViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject33"):
                    opp_val = getattr(item, "presentation_EObject33", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject33"):
                    opp_val = getattr(item, "presentation_EObject33", None)
                    
                    setattr(item, "presentation_EObject33", self)
                    

    @property
    def presentation_CheckboxTableViewer35(self):
        return self.__presentation_CheckboxTableViewer35

    @presentation_CheckboxTableViewer35.setter
    def presentation_CheckboxTableViewer35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CheckboxTableViewer__presentation_CheckboxTableViewer35", None)
        self.__presentation_CheckboxTableViewer35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ICheckStateProvider"):
                    opp_val = getattr(item, "presentation_ICheckStateProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ICheckStateProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ICheckStateProvider"):
                    opp_val = getattr(item, "presentation_ICheckStateProvider", None)
                    
                    setattr(item, "presentation_ICheckStateProvider", self)
                    

    @property
    def presentation_CheckboxTableViewer37(self):
        return self.__presentation_CheckboxTableViewer37

    @presentation_CheckboxTableViewer37.setter
    def presentation_CheckboxTableViewer37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CheckboxTableViewer__presentation_CheckboxTableViewer37", None)
        self.__presentation_CheckboxTableViewer37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject38"):
                    opp_val = getattr(item, "presentation_EObject38", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject38"):
                    opp_val = getattr(item, "presentation_EObject38", None)
                    
                    setattr(item, "presentation_EObject38", self)
                    

class presentation_LayoutData:

    def __init__(self, mixed: str, presentation_LayoutData: "presentation_CellEditor" = None):
        self.mixed = mixed
        self.presentation_LayoutData = presentation_LayoutData
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_LayoutData(self):
        return self.__presentation_LayoutData

    @presentation_LayoutData.setter
    def presentation_LayoutData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_LayoutData__presentation_LayoutData", None)
        self.__presentation_LayoutData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CellEditor26"):
                opp_val = getattr(old_value, "presentation_CellEditor26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CellEditor26"):
                opp_val = getattr(value, "presentation_CellEditor26", None)
                if opp_val is None:
                    setattr(value, "presentation_CellEditor26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ICellEditorValidator(ABC):

    def __init__(self, mixed: str, presentation_ICellEditorValidator: "presentation_CellEditor" = None):
        self.mixed = mixed
        self.presentation_ICellEditorValidator = presentation_ICellEditorValidator
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ICellEditorValidator(self):
        return self.__presentation_ICellEditorValidator

    @presentation_ICellEditorValidator.setter
    def presentation_ICellEditorValidator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ICellEditorValidator__presentation_ICellEditorValidator", None)
        self.__presentation_ICellEditorValidator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CellEditor"):
                opp_val = getattr(old_value, "presentation_CellEditor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CellEditor"):
                opp_val = getattr(value, "presentation_CellEditor", None)
                if opp_val is None:
                    setattr(value, "presentation_CellEditor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_CellEditor(ABC):

    def __init__(self, mixed: str, group: str, errorMessage: str, style: str, presentation_CellEditor: set["presentation_ICellEditorValidator"] = None, presentation_CellEditor26: set["presentation_LayoutData"] = None, presentation_CellEditor28: set["presentation_EObject"] = None, presentation_CellEditor31: set["presentation_Control"] = None, presentation_CellEditor52: "presentation_ColumnViewer" = None):
        self.mixed = mixed
        self.group = group
        self.errorMessage = errorMessage
        self.style = style
        self.presentation_CellEditor = presentation_CellEditor if presentation_CellEditor is not None else set()
        self.presentation_CellEditor26 = presentation_CellEditor26 if presentation_CellEditor26 is not None else set()
        self.presentation_CellEditor28 = presentation_CellEditor28 if presentation_CellEditor28 is not None else set()
        self.presentation_CellEditor31 = presentation_CellEditor31 if presentation_CellEditor31 is not None else set()
        self.presentation_CellEditor52 = presentation_CellEditor52
        
    @property
    def errorMessage(self) -> str:
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, errorMessage: str):
        self.__errorMessage = errorMessage

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def presentation_CellEditor52(self):
        return self.__presentation_CellEditor52

    @presentation_CellEditor52.setter
    def presentation_CellEditor52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CellEditor__presentation_CellEditor52", None)
        self.__presentation_CellEditor52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ColumnViewer51"):
                opp_val = getattr(old_value, "presentation_ColumnViewer51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ColumnViewer51"):
                opp_val = getattr(value, "presentation_ColumnViewer51", None)
                if opp_val is None:
                    setattr(value, "presentation_ColumnViewer51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_CellEditor28(self):
        return self.__presentation_CellEditor28

    @presentation_CellEditor28.setter
    def presentation_CellEditor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CellEditor__presentation_CellEditor28", None)
        self.__presentation_CellEditor28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject29"):
                    opp_val = getattr(item, "presentation_EObject29", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject29"):
                    opp_val = getattr(item, "presentation_EObject29", None)
                    
                    setattr(item, "presentation_EObject29", self)
                    

    @property
    def presentation_CellEditor(self):
        return self.__presentation_CellEditor

    @presentation_CellEditor.setter
    def presentation_CellEditor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CellEditor__presentation_CellEditor", None)
        self.__presentation_CellEditor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ICellEditorValidator"):
                    opp_val = getattr(item, "presentation_ICellEditorValidator", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ICellEditorValidator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ICellEditorValidator"):
                    opp_val = getattr(item, "presentation_ICellEditorValidator", None)
                    
                    setattr(item, "presentation_ICellEditorValidator", self)
                    

    @property
    def presentation_CellEditor31(self):
        return self.__presentation_CellEditor31

    @presentation_CellEditor31.setter
    def presentation_CellEditor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CellEditor__presentation_CellEditor31", None)
        self.__presentation_CellEditor31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control"):
                    opp_val = getattr(item, "presentation_Control", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control"):
                    opp_val = getattr(item, "presentation_Control", None)
                    
                    setattr(item, "presentation_Control", self)
                    

    @property
    def presentation_CellEditor26(self):
        return self.__presentation_CellEditor26

    @presentation_CellEditor26.setter
    def presentation_CellEditor26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CellEditor__presentation_CellEditor26", None)
        self.__presentation_CellEditor26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_LayoutData"):
                    opp_val = getattr(item, "presentation_LayoutData", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_LayoutData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_LayoutData"):
                    opp_val = getattr(item, "presentation_LayoutData", None)
                    
                    setattr(item, "presentation_LayoutData", self)
                    

class presentation_TableItem(Item):

    def __init__(self, group: str, checked: str, grayed: str, imageIndent: str, texts: str, presentation_TableItem: "presentation_Cell" = None, presentation_TableItem227: "presentation_Table" = None, presentation_TableItem230: "presentation_Table" = None, presentation_TableItem237: "presentation_TableEditor" = None, presentation_TableItem241: set["presentation_Table"] = None, presentation_TableItem244: set["presentation_Collection"] = None, presentation_TableItem239: set["presentation_Collection"] = None):
        self.group = group
        self.checked = checked
        self.grayed = grayed
        self.imageIndent = imageIndent
        self.texts = texts
        self.presentation_TableItem = presentation_TableItem
        self.presentation_TableItem227 = presentation_TableItem227
        self.presentation_TableItem230 = presentation_TableItem230
        self.presentation_TableItem237 = presentation_TableItem237
        self.presentation_TableItem241 = presentation_TableItem241 if presentation_TableItem241 is not None else set()
        self.presentation_TableItem244 = presentation_TableItem244 if presentation_TableItem244 is not None else set()
        self.presentation_TableItem239 = presentation_TableItem239 if presentation_TableItem239 is not None else set()
        
    @property
    def checked(self) -> str:
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked

    @property
    def texts(self) -> str:
        return self.__texts

    @texts.setter
    def texts(self, texts: str):
        self.__texts = texts

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def grayed(self) -> str:
        return self.__grayed

    @grayed.setter
    def grayed(self, grayed: str):
        self.__grayed = grayed

    @property
    def imageIndent(self) -> str:
        return self.__imageIndent

    @imageIndent.setter
    def imageIndent(self, imageIndent: str):
        self.__imageIndent = imageIndent

    @property
    def presentation_TableItem230(self):
        return self.__presentation_TableItem230

    @presentation_TableItem230.setter
    def presentation_TableItem230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem230", None)
        self.__presentation_TableItem230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Table229"):
                opp_val = getattr(old_value, "presentation_Table229", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Table229"):
                opp_val = getattr(value, "presentation_Table229", None)
                if opp_val is None:
                    setattr(value, "presentation_Table229", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TableItem237(self):
        return self.__presentation_TableItem237

    @presentation_TableItem237.setter
    def presentation_TableItem237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem237", None)
        self.__presentation_TableItem237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableEditor"):
                opp_val = getattr(old_value, "presentation_TableEditor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableEditor"):
                opp_val = getattr(value, "presentation_TableEditor", None)
                if opp_val is None:
                    setattr(value, "presentation_TableEditor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TableItem227(self):
        return self.__presentation_TableItem227

    @presentation_TableItem227.setter
    def presentation_TableItem227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem227", None)
        self.__presentation_TableItem227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Table226"):
                opp_val = getattr(old_value, "presentation_Table226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Table226"):
                opp_val = getattr(value, "presentation_Table226", None)
                if opp_val is None:
                    setattr(value, "presentation_Table226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TableItem(self):
        return self.__presentation_TableItem

    @presentation_TableItem.setter
    def presentation_TableItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem", None)
        self.__presentation_TableItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Cell"):
                opp_val = getattr(old_value, "presentation_Cell", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Cell"):
                opp_val = getattr(value, "presentation_Cell", None)
                if opp_val is None:
                    setattr(value, "presentation_Cell", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TableItem239(self):
        return self.__presentation_TableItem239

    @presentation_TableItem239.setter
    def presentation_TableItem239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem239", None)
        self.__presentation_TableItem239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Collection"):
                    opp_val = getattr(item, "presentation_Collection", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Collection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Collection"):
                    opp_val = getattr(item, "presentation_Collection", None)
                    
                    setattr(item, "presentation_Collection", self)
                    

    @property
    def presentation_TableItem241(self):
        return self.__presentation_TableItem241

    @presentation_TableItem241.setter
    def presentation_TableItem241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem241", None)
        self.__presentation_TableItem241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Table242"):
                    opp_val = getattr(item, "presentation_Table242", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Table242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Table242"):
                    opp_val = getattr(item, "presentation_Table242", None)
                    
                    setattr(item, "presentation_Table242", self)
                    

    @property
    def presentation_TableItem244(self):
        return self.__presentation_TableItem244

    @presentation_TableItem244.setter
    def presentation_TableItem244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TableItem__presentation_TableItem244", None)
        self.__presentation_TableItem244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Collection245"):
                    opp_val = getattr(item, "presentation_Collection245", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Collection245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Collection245"):
                    opp_val = getattr(item, "presentation_Collection245", None)
                    
                    setattr(item, "presentation_Collection245", self)
                    

class presentation_Cell:

    def __init__(self, mixed: str, group: str, image: str, text: str, presentation_Cell: set["presentation_TableItem"] = None):
        self.mixed = mixed
        self.group = group
        self.image = image
        self.text = text
        self.presentation_Cell = presentation_Cell if presentation_Cell is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def presentation_Cell(self):
        return self.__presentation_Cell

    @presentation_Cell.setter
    def presentation_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Cell__presentation_Cell", None)
        self.__presentation_Cell = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableItem"):
                    opp_val = getattr(item, "presentation_TableItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableItem"):
                    opp_val = getattr(item, "presentation_TableItem", None)
                    
                    setattr(item, "presentation_TableItem", self)
                    

class Widget:

    pass
class presentation_Menu(Widget):

    def __init__(self, group: str, enabled: str, handle: str, visible: str, presentation_Menu: "presentation_Control" = None, presentation_Menu118: "presentation_Decorations" = None, presentation_Menu158: set["presentation_MenuItem"] = None, presentation_Menu156: set["presentation_MenuItem"] = None, presentation_Menu167: set["presentation_Decorations"] = None, presentation_Menu161: set["presentation_MenuItem"] = None, presentation_Menu165: "presentation_Menu" = None, presentation_Menu163: set["presentation_Menu"] = None, presentation_Menu171: "presentation_MenuItem" = None, presentation_Menu177: "presentation_MenuItem" = None):
        self.group = group
        self.enabled = enabled
        self.handle = handle
        self.visible = visible
        self.presentation_Menu = presentation_Menu
        self.presentation_Menu118 = presentation_Menu118
        self.presentation_Menu158 = presentation_Menu158 if presentation_Menu158 is not None else set()
        self.presentation_Menu156 = presentation_Menu156 if presentation_Menu156 is not None else set()
        self.presentation_Menu167 = presentation_Menu167 if presentation_Menu167 is not None else set()
        self.presentation_Menu161 = presentation_Menu161 if presentation_Menu161 is not None else set()
        self.presentation_Menu165 = presentation_Menu165
        self.presentation_Menu163 = presentation_Menu163 if presentation_Menu163 is not None else set()
        self.presentation_Menu171 = presentation_Menu171
        self.presentation_Menu177 = presentation_Menu177
        
    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def handle(self) -> str:
        return self.__handle

    @handle.setter
    def handle(self, handle: str):
        self.__handle = handle

    @property
    def presentation_Menu177(self):
        return self.__presentation_Menu177

    @presentation_Menu177.setter
    def presentation_Menu177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu177", None)
        self.__presentation_Menu177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_MenuItem176"):
                opp_val = getattr(old_value, "presentation_MenuItem176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_MenuItem176"):
                opp_val = getattr(value, "presentation_MenuItem176", None)
                if opp_val is None:
                    setattr(value, "presentation_MenuItem176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Menu167(self):
        return self.__presentation_Menu167

    @presentation_Menu167.setter
    def presentation_Menu167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu167", None)
        self.__presentation_Menu167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Decorations168"):
                    opp_val = getattr(item, "presentation_Decorations168", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Decorations168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Decorations168"):
                    opp_val = getattr(item, "presentation_Decorations168", None)
                    
                    setattr(item, "presentation_Decorations168", self)
                    

    @property
    def presentation_Menu165(self):
        return self.__presentation_Menu165

    @presentation_Menu165.setter
    def presentation_Menu165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu165", None)
        self.__presentation_Menu165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Menu163"):
                opp_val = getattr(old_value, "presentation_Menu163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Menu163"):
                opp_val = getattr(value, "presentation_Menu163", None)
                if opp_val is None:
                    setattr(value, "presentation_Menu163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Menu161(self):
        return self.__presentation_Menu161

    @presentation_Menu161.setter
    def presentation_Menu161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu161", None)
        self.__presentation_Menu161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_MenuItem162"):
                    opp_val = getattr(item, "presentation_MenuItem162", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_MenuItem162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_MenuItem162"):
                    opp_val = getattr(item, "presentation_MenuItem162", None)
                    
                    setattr(item, "presentation_MenuItem162", self)
                    

    @property
    def presentation_Menu163(self):
        return self.__presentation_Menu163

    @presentation_Menu163.setter
    def presentation_Menu163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu163", None)
        self.__presentation_Menu163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Menu165"):
                    opp_val = getattr(item, "presentation_Menu165", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Menu165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Menu165"):
                    opp_val = getattr(item, "presentation_Menu165", None)
                    
                    setattr(item, "presentation_Menu165", self)
                    

    @property
    def presentation_Menu118(self):
        return self.__presentation_Menu118

    @presentation_Menu118.setter
    def presentation_Menu118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu118", None)
        self.__presentation_Menu118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Decorations117"):
                opp_val = getattr(old_value, "presentation_Decorations117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Decorations117"):
                opp_val = getattr(value, "presentation_Decorations117", None)
                if opp_val is None:
                    setattr(value, "presentation_Decorations117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Menu(self):
        return self.__presentation_Menu

    @presentation_Menu.setter
    def presentation_Menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu", None)
        self.__presentation_Menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Control76"):
                opp_val = getattr(old_value, "presentation_Control76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Control76"):
                opp_val = getattr(value, "presentation_Control76", None)
                if opp_val is None:
                    setattr(value, "presentation_Control76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Menu171(self):
        return self.__presentation_Menu171

    @presentation_Menu171.setter
    def presentation_Menu171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu171", None)
        self.__presentation_Menu171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_MenuItem170"):
                opp_val = getattr(old_value, "presentation_MenuItem170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_MenuItem170"):
                opp_val = getattr(value, "presentation_MenuItem170", None)
                if opp_val is None:
                    setattr(value, "presentation_MenuItem170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Menu156(self):
        return self.__presentation_Menu156

    @presentation_Menu156.setter
    def presentation_Menu156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu156", None)
        self.__presentation_Menu156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_MenuItem"):
                    opp_val = getattr(item, "presentation_MenuItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_MenuItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_MenuItem"):
                    opp_val = getattr(item, "presentation_MenuItem", None)
                    
                    setattr(item, "presentation_MenuItem", self)
                    

    @property
    def presentation_Menu158(self):
        return self.__presentation_Menu158

    @presentation_Menu158.setter
    def presentation_Menu158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Menu__presentation_Menu158", None)
        self.__presentation_Menu158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_MenuItem159"):
                    opp_val = getattr(item, "presentation_MenuItem159", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_MenuItem159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_MenuItem159"):
                    opp_val = getattr(item, "presentation_MenuItem159", None)
                    
                    setattr(item, "presentation_MenuItem159", self)
                    

class presentation_Control(Widget):

    def __init__(self, group: str, background: str, bounds: str, capture: str, dragDetect: str, enabled: str, font: str, backgroundImage: str, redraw: str, size: str, toolTipText: str, visible: str, foreground: str, handle: str, location: str, presentation_Control: "presentation_CellEditor" = None, presentation_Control65: "presentation_Composite" = None, presentation_Control68: "presentation_Composite" = None, presentation_Control76: set["presentation_Menu"] = None, presentation_Control78: set["presentation_Cursor"] = None, presentation_Control80: set["presentation_EObject"] = None, presentation_Control83: set["presentation_Accessible"] = None, presentation_Control85: "presentation_ControlEditor" = None, presentation_Control92: "presentation_CoolItem" = None, presentation_Control98: "presentation_CTabFolder" = None, presentation_Control113: "presentation_CTabItem" = None, presentation_Control120: "presentation_Dialog" = None, presentation_Control138: "presentation_ExpandItem" = None, presentation_Control140: "presentation_FormAttachment" = None, presentation_Control186: "presentation_SashForm" = None, presentation_Control197: "presentation_StackLayout" = None, presentation_Control220: "presentation_TabItem" = None, presentation_Control256: "presentation_ToolItem" = None, presentation_Control301: "presentation_Viewer" = None):
        self.group = group
        self.background = background
        self.bounds = bounds
        self.capture = capture
        self.dragDetect = dragDetect
        self.enabled = enabled
        self.font = font
        self.backgroundImage = backgroundImage
        self.redraw = redraw
        self.size = size
        self.toolTipText = toolTipText
        self.visible = visible
        self.foreground = foreground
        self.handle = handle
        self.location = location
        self.presentation_Control = presentation_Control
        self.presentation_Control65 = presentation_Control65
        self.presentation_Control68 = presentation_Control68
        self.presentation_Control76 = presentation_Control76 if presentation_Control76 is not None else set()
        self.presentation_Control78 = presentation_Control78 if presentation_Control78 is not None else set()
        self.presentation_Control80 = presentation_Control80 if presentation_Control80 is not None else set()
        self.presentation_Control83 = presentation_Control83 if presentation_Control83 is not None else set()
        self.presentation_Control85 = presentation_Control85
        self.presentation_Control92 = presentation_Control92
        self.presentation_Control98 = presentation_Control98
        self.presentation_Control113 = presentation_Control113
        self.presentation_Control120 = presentation_Control120
        self.presentation_Control138 = presentation_Control138
        self.presentation_Control140 = presentation_Control140
        self.presentation_Control186 = presentation_Control186
        self.presentation_Control197 = presentation_Control197
        self.presentation_Control220 = presentation_Control220
        self.presentation_Control256 = presentation_Control256
        self.presentation_Control301 = presentation_Control301
        
    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def capture(self) -> str:
        return self.__capture

    @capture.setter
    def capture(self, capture: str):
        self.__capture = capture

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def redraw(self) -> str:
        return self.__redraw

    @redraw.setter
    def redraw(self, redraw: str):
        self.__redraw = redraw

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def backgroundImage(self) -> str:
        return self.__backgroundImage

    @backgroundImage.setter
    def backgroundImage(self, backgroundImage: str):
        self.__backgroundImage = backgroundImage

    @property
    def handle(self) -> str:
        return self.__handle

    @handle.setter
    def handle(self, handle: str):
        self.__handle = handle

    @property
    def foreground(self) -> str:
        return self.__foreground

    @foreground.setter
    def foreground(self, foreground: str):
        self.__foreground = foreground

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def dragDetect(self) -> str:
        return self.__dragDetect

    @dragDetect.setter
    def dragDetect(self, dragDetect: str):
        self.__dragDetect = dragDetect

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def presentation_Control(self):
        return self.__presentation_Control

    @presentation_Control.setter
    def presentation_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control", None)
        self.__presentation_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CellEditor31"):
                opp_val = getattr(old_value, "presentation_CellEditor31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CellEditor31"):
                opp_val = getattr(value, "presentation_CellEditor31", None)
                if opp_val is None:
                    setattr(value, "presentation_CellEditor31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control197(self):
        return self.__presentation_Control197

    @presentation_Control197.setter
    def presentation_Control197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control197", None)
        self.__presentation_Control197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_StackLayout"):
                opp_val = getattr(old_value, "presentation_StackLayout", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_StackLayout"):
                opp_val = getattr(value, "presentation_StackLayout", None)
                if opp_val is None:
                    setattr(value, "presentation_StackLayout", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control85(self):
        return self.__presentation_Control85

    @presentation_Control85.setter
    def presentation_Control85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control85", None)
        self.__presentation_Control85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ControlEditor"):
                opp_val = getattr(old_value, "presentation_ControlEditor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ControlEditor"):
                opp_val = getattr(value, "presentation_ControlEditor", None)
                if opp_val is None:
                    setattr(value, "presentation_ControlEditor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control140(self):
        return self.__presentation_Control140

    @presentation_Control140.setter
    def presentation_Control140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control140", None)
        self.__presentation_Control140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_FormAttachment"):
                opp_val = getattr(old_value, "presentation_FormAttachment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_FormAttachment"):
                opp_val = getattr(value, "presentation_FormAttachment", None)
                if opp_val is None:
                    setattr(value, "presentation_FormAttachment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control138(self):
        return self.__presentation_Control138

    @presentation_Control138.setter
    def presentation_Control138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control138", None)
        self.__presentation_Control138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ExpandItem137"):
                opp_val = getattr(old_value, "presentation_ExpandItem137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ExpandItem137"):
                opp_val = getattr(value, "presentation_ExpandItem137", None)
                if opp_val is None:
                    setattr(value, "presentation_ExpandItem137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control186(self):
        return self.__presentation_Control186

    @presentation_Control186.setter
    def presentation_Control186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control186", None)
        self.__presentation_Control186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SashForm"):
                opp_val = getattr(old_value, "presentation_SashForm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SashForm"):
                opp_val = getattr(value, "presentation_SashForm", None)
                if opp_val is None:
                    setattr(value, "presentation_SashForm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control68(self):
        return self.__presentation_Control68

    @presentation_Control68.setter
    def presentation_Control68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control68", None)
        self.__presentation_Control68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Composite67"):
                opp_val = getattr(old_value, "presentation_Composite67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Composite67"):
                opp_val = getattr(value, "presentation_Composite67", None)
                if opp_val is None:
                    setattr(value, "presentation_Composite67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control220(self):
        return self.__presentation_Control220

    @presentation_Control220.setter
    def presentation_Control220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control220", None)
        self.__presentation_Control220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TabItem219"):
                opp_val = getattr(old_value, "presentation_TabItem219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TabItem219"):
                opp_val = getattr(value, "presentation_TabItem219", None)
                if opp_val is None:
                    setattr(value, "presentation_TabItem219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control98(self):
        return self.__presentation_Control98

    @presentation_Control98.setter
    def presentation_Control98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control98", None)
        self.__presentation_Control98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabFolder97"):
                opp_val = getattr(old_value, "presentation_CTabFolder97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabFolder97"):
                opp_val = getattr(value, "presentation_CTabFolder97", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabFolder97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control65(self):
        return self.__presentation_Control65

    @presentation_Control65.setter
    def presentation_Control65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control65", None)
        self.__presentation_Control65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Composite"):
                opp_val = getattr(old_value, "presentation_Composite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Composite"):
                opp_val = getattr(value, "presentation_Composite", None)
                if opp_val is None:
                    setattr(value, "presentation_Composite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control92(self):
        return self.__presentation_Control92

    @presentation_Control92.setter
    def presentation_Control92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control92", None)
        self.__presentation_Control92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CoolItem91"):
                opp_val = getattr(old_value, "presentation_CoolItem91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CoolItem91"):
                opp_val = getattr(value, "presentation_CoolItem91", None)
                if opp_val is None:
                    setattr(value, "presentation_CoolItem91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control256(self):
        return self.__presentation_Control256

    @presentation_Control256.setter
    def presentation_Control256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control256", None)
        self.__presentation_Control256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ToolItem255"):
                opp_val = getattr(old_value, "presentation_ToolItem255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ToolItem255"):
                opp_val = getattr(value, "presentation_ToolItem255", None)
                if opp_val is None:
                    setattr(value, "presentation_ToolItem255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control301(self):
        return self.__presentation_Control301

    @presentation_Control301.setter
    def presentation_Control301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control301", None)
        self.__presentation_Control301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Viewer300"):
                opp_val = getattr(old_value, "presentation_Viewer300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Viewer300"):
                opp_val = getattr(value, "presentation_Viewer300", None)
                if opp_val is None:
                    setattr(value, "presentation_Viewer300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control120(self):
        return self.__presentation_Control120

    @presentation_Control120.setter
    def presentation_Control120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control120", None)
        self.__presentation_Control120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Dialog"):
                opp_val = getattr(old_value, "presentation_Dialog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Dialog"):
                opp_val = getattr(value, "presentation_Dialog", None)
                if opp_val is None:
                    setattr(value, "presentation_Dialog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control76(self):
        return self.__presentation_Control76

    @presentation_Control76.setter
    def presentation_Control76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control76", None)
        self.__presentation_Control76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Menu"):
                    opp_val = getattr(item, "presentation_Menu", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Menu", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Menu"):
                    opp_val = getattr(item, "presentation_Menu", None)
                    
                    setattr(item, "presentation_Menu", self)
                    

    @property
    def presentation_Control113(self):
        return self.__presentation_Control113

    @presentation_Control113.setter
    def presentation_Control113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control113", None)
        self.__presentation_Control113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabItem112"):
                opp_val = getattr(old_value, "presentation_CTabItem112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabItem112"):
                opp_val = getattr(value, "presentation_CTabItem112", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabItem112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Control80(self):
        return self.__presentation_Control80

    @presentation_Control80.setter
    def presentation_Control80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control80", None)
        self.__presentation_Control80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject81"):
                    opp_val = getattr(item, "presentation_EObject81", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject81"):
                    opp_val = getattr(item, "presentation_EObject81", None)
                    
                    setattr(item, "presentation_EObject81", self)
                    

    @property
    def presentation_Control78(self):
        return self.__presentation_Control78

    @presentation_Control78.setter
    def presentation_Control78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control78", None)
        self.__presentation_Control78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Cursor"):
                    opp_val = getattr(item, "presentation_Cursor", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Cursor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Cursor"):
                    opp_val = getattr(item, "presentation_Cursor", None)
                    
                    setattr(item, "presentation_Cursor", self)
                    

    @property
    def presentation_Control83(self):
        return self.__presentation_Control83

    @presentation_Control83.setter
    def presentation_Control83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Control__presentation_Control83", None)
        self.__presentation_Control83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Accessible"):
                    opp_val = getattr(item, "presentation_Accessible", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Accessible", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Accessible"):
                    opp_val = getattr(item, "presentation_Accessible", None)
                    
                    setattr(item, "presentation_Accessible", self)
                    

class presentation_ToolTip(Widget):

    def __init__(self, group: str, autoHide: str, message: str, visible: str, text: str, presentation_ToolTip: set["presentation_Shell"] = None):
        self.group = group
        self.autoHide = autoHide
        self.message = message
        self.visible = visible
        self.text = text
        self.presentation_ToolTip = presentation_ToolTip if presentation_ToolTip is not None else set()
        
    @property
    def autoHide(self) -> str:
        return self.__autoHide

    @autoHide.setter
    def autoHide(self, autoHide: str):
        self.__autoHide = autoHide

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def presentation_ToolTip(self):
        return self.__presentation_ToolTip

    @presentation_ToolTip.setter
    def presentation_ToolTip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ToolTip__presentation_ToolTip", None)
        self.__presentation_ToolTip = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Shell261"):
                    opp_val = getattr(item, "presentation_Shell261", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Shell261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Shell261"):
                    opp_val = getattr(item, "presentation_Shell261", None)
                    
                    setattr(item, "presentation_Shell261", self)
                    

class presentation_Tray(Widget):

    def __init__(self, group: str, presentation_Tray: set["presentation_TrayItem"] = None):
        self.group = group
        self.presentation_Tray = presentation_Tray if presentation_Tray is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_Tray(self):
        return self.__presentation_Tray

    @presentation_Tray.setter
    def presentation_Tray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tray__presentation_Tray", None)
        self.__presentation_Tray = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TrayItem"):
                    opp_val = getattr(item, "presentation_TrayItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TrayItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TrayItem"):
                    opp_val = getattr(item, "presentation_TrayItem", None)
                    
                    setattr(item, "presentation_TrayItem", self)
                    

class presentation_ScrollBar(Widget):

    def __init__(self, group: str, maximum: str, minimum: str, pageIncrement: str, enabled: str, increment: str, selection: str, size: str, thumb: str, visible: str, presentation_ScrollBar: "presentation_Scrollable" = None, presentation_ScrollBar190: "presentation_Scrollable" = None, presentation_ScrollBar192: set["presentation_Scrollable"] = None):
        self.group = group
        self.maximum = maximum
        self.minimum = minimum
        self.pageIncrement = pageIncrement
        self.enabled = enabled
        self.increment = increment
        self.selection = selection
        self.size = size
        self.thumb = thumb
        self.visible = visible
        self.presentation_ScrollBar = presentation_ScrollBar
        self.presentation_ScrollBar190 = presentation_ScrollBar190
        self.presentation_ScrollBar192 = presentation_ScrollBar192 if presentation_ScrollBar192 is not None else set()
        
    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def increment(self) -> str:
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def thumb(self) -> str:
        return self.__thumb

    @thumb.setter
    def thumb(self, thumb: str):
        self.__thumb = thumb

    @property
    def pageIncrement(self) -> str:
        return self.__pageIncrement

    @pageIncrement.setter
    def pageIncrement(self, pageIncrement: str):
        self.__pageIncrement = pageIncrement

    @property
    def presentation_ScrollBar(self):
        return self.__presentation_ScrollBar

    @presentation_ScrollBar.setter
    def presentation_ScrollBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ScrollBar__presentation_ScrollBar", None)
        self.__presentation_ScrollBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Scrollable"):
                opp_val = getattr(old_value, "presentation_Scrollable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Scrollable"):
                opp_val = getattr(value, "presentation_Scrollable", None)
                if opp_val is None:
                    setattr(value, "presentation_Scrollable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_ScrollBar192(self):
        return self.__presentation_ScrollBar192

    @presentation_ScrollBar192.setter
    def presentation_ScrollBar192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ScrollBar__presentation_ScrollBar192", None)
        self.__presentation_ScrollBar192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Scrollable193"):
                    opp_val = getattr(item, "presentation_Scrollable193", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Scrollable193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Scrollable193"):
                    opp_val = getattr(item, "presentation_Scrollable193", None)
                    
                    setattr(item, "presentation_Scrollable193", self)
                    

    @property
    def presentation_ScrollBar190(self):
        return self.__presentation_ScrollBar190

    @presentation_ScrollBar190.setter
    def presentation_ScrollBar190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ScrollBar__presentation_ScrollBar190", None)
        self.__presentation_ScrollBar190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Scrollable189"):
                opp_val = getattr(old_value, "presentation_Scrollable189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Scrollable189"):
                opp_val = getattr(value, "presentation_Scrollable189", None)
                if opp_val is None:
                    setattr(value, "presentation_Scrollable189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_Item(Widget):

    def __init__(self, image: str, text: str):
        self.image = image
        self.text = text
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class presentation_Tracker(Widget):

    def __init__(self, group: str, rectangles: str, stippled: str, presentation_Tracker: set["presentation_Cursor"] = None):
        self.group = group
        self.rectangles = rectangles
        self.stippled = stippled
        self.presentation_Tracker = presentation_Tracker if presentation_Tracker is not None else set()
        
    @property
    def stippled(self) -> str:
        return self.__stippled

    @stippled.setter
    def stippled(self, stippled: str):
        self.__stippled = stippled

    @property
    def rectangles(self) -> str:
        return self.__rectangles

    @rectangles.setter
    def rectangles(self, rectangles: str):
        self.__rectangles = rectangles

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_Tracker(self):
        return self.__presentation_Tracker

    @presentation_Tracker.setter
    def presentation_Tracker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tracker__presentation_Tracker", None)
        self.__presentation_Tracker = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Cursor263"):
                    opp_val = getattr(item, "presentation_Cursor263", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Cursor263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Cursor263"):
                    opp_val = getattr(item, "presentation_Cursor263", None)
                    
                    setattr(item, "presentation_Cursor263", self)
                    

class presentation_Caret(Widget):

    def __init__(self, group: str, bounds: str, font: str, image: str, location: str, size: str, visible: str, presentation_Caret: "presentation_Canvas" = None, presentation_Caret21: set["presentation_Canvas"] = None):
        self.group = group
        self.bounds = bounds
        self.font = font
        self.image = image
        self.location = location
        self.size = size
        self.visible = visible
        self.presentation_Caret = presentation_Caret
        self.presentation_Caret21 = presentation_Caret21 if presentation_Caret21 is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def presentation_Caret21(self):
        return self.__presentation_Caret21

    @presentation_Caret21.setter
    def presentation_Caret21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Caret__presentation_Caret21", None)
        self.__presentation_Caret21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Canvas22"):
                    opp_val = getattr(item, "presentation_Canvas22", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Canvas22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Canvas22"):
                    opp_val = getattr(item, "presentation_Canvas22", None)
                    
                    setattr(item, "presentation_Canvas22", self)
                    

    @property
    def presentation_Caret(self):
        return self.__presentation_Caret

    @presentation_Caret.setter
    def presentation_Caret(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Caret__presentation_Caret", None)
        self.__presentation_Caret = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Canvas19"):
                opp_val = getattr(old_value, "presentation_Canvas19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Canvas19"):
                opp_val = getattr(value, "presentation_Canvas19", None)
                if opp_val is None:
                    setattr(value, "presentation_Canvas19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_IME(Widget):

    def __init__(self, compositionOffset: str, text: str, group: str, ranges: str, presentation_IME: "presentation_Canvas" = None, presentation_IME153: set["presentation_TextStyle"] = None):
        self.compositionOffset = compositionOffset
        self.text = text
        self.group = group
        self.ranges = ranges
        self.presentation_IME = presentation_IME
        self.presentation_IME153 = presentation_IME153 if presentation_IME153 is not None else set()
        
    @property
    def compositionOffset(self) -> str:
        return self.__compositionOffset

    @compositionOffset.setter
    def compositionOffset(self, compositionOffset: str):
        self.__compositionOffset = compositionOffset

    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def presentation_IME153(self):
        return self.__presentation_IME153

    @presentation_IME153.setter
    def presentation_IME153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IME__presentation_IME153", None)
        self.__presentation_IME153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TextStyle"):
                    opp_val = getattr(item, "presentation_TextStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TextStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TextStyle"):
                    opp_val = getattr(item, "presentation_TextStyle", None)
                    
                    setattr(item, "presentation_TextStyle", self)
                    

    @property
    def presentation_IME(self):
        return self.__presentation_IME

    @presentation_IME.setter
    def presentation_IME(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IME__presentation_IME", None)
        self.__presentation_IME = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Canvas"):
                opp_val = getattr(old_value, "presentation_Canvas", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Canvas"):
                opp_val = getattr(value, "presentation_Canvas", None)
                if opp_val is None:
                    setattr(value, "presentation_Canvas", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ICommand(ABC):

    def __init__(self, mixed: str, presentation_ICommand: "presentation_Button" = None, presentation_ICommand174: "presentation_MenuItem" = None):
        self.mixed = mixed
        self.presentation_ICommand = presentation_ICommand
        self.presentation_ICommand174 = presentation_ICommand174
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_ICommand(self):
        return self.__presentation_ICommand

    @presentation_ICommand.setter
    def presentation_ICommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ICommand__presentation_ICommand", None)
        self.__presentation_ICommand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Button"):
                opp_val = getattr(old_value, "presentation_Button", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Button"):
                opp_val = getattr(value, "presentation_Button", None)
                if opp_val is None:
                    setattr(value, "presentation_Button", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_ICommand174(self):
        return self.__presentation_ICommand174

    @presentation_ICommand174.setter
    def presentation_ICommand174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ICommand__presentation_ICommand174", None)
        self.__presentation_ICommand174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_MenuItem173"):
                opp_val = getattr(old_value, "presentation_MenuItem173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_MenuItem173"):
                opp_val = getattr(value, "presentation_MenuItem173", None)
                if opp_val is None:
                    setattr(value, "presentation_MenuItem173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Control:

    pass
class presentation_ProgressBar(Control):

    def __init__(self, maximum: str, minimum: str, selection: str, state: str):
        self.maximum = maximum
        self.minimum = minimum
        self.selection = selection
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

class presentation_Scrollable(Control):

    def __init__(self, group1: str, clientArea: str, presentation_Scrollable: set["presentation_ScrollBar"] = None, presentation_Scrollable189: set["presentation_ScrollBar"] = None, presentation_Scrollable193: "presentation_ScrollBar" = None):
        self.group1 = group1
        self.clientArea = clientArea
        self.presentation_Scrollable = presentation_Scrollable if presentation_Scrollable is not None else set()
        self.presentation_Scrollable189 = presentation_Scrollable189 if presentation_Scrollable189 is not None else set()
        self.presentation_Scrollable193 = presentation_Scrollable193
        
    @property
    def clientArea(self) -> str:
        return self.__clientArea

    @clientArea.setter
    def clientArea(self, clientArea: str):
        self.__clientArea = clientArea

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def presentation_Scrollable193(self):
        return self.__presentation_Scrollable193

    @presentation_Scrollable193.setter
    def presentation_Scrollable193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Scrollable__presentation_Scrollable193", None)
        self.__presentation_Scrollable193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ScrollBar192"):
                opp_val = getattr(old_value, "presentation_ScrollBar192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ScrollBar192"):
                opp_val = getattr(value, "presentation_ScrollBar192", None)
                if opp_val is None:
                    setattr(value, "presentation_ScrollBar192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Scrollable(self):
        return self.__presentation_Scrollable

    @presentation_Scrollable.setter
    def presentation_Scrollable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Scrollable__presentation_Scrollable", None)
        self.__presentation_Scrollable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ScrollBar"):
                    opp_val = getattr(item, "presentation_ScrollBar", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ScrollBar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ScrollBar"):
                    opp_val = getattr(item, "presentation_ScrollBar", None)
                    
                    setattr(item, "presentation_ScrollBar", self)
                    

    @property
    def presentation_Scrollable189(self):
        return self.__presentation_Scrollable189

    @presentation_Scrollable189.setter
    def presentation_Scrollable189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Scrollable__presentation_Scrollable189", None)
        self.__presentation_Scrollable189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ScrollBar190"):
                    opp_val = getattr(item, "presentation_ScrollBar190", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ScrollBar190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ScrollBar190"):
                    opp_val = getattr(item, "presentation_ScrollBar190", None)
                    
                    setattr(item, "presentation_ScrollBar190", self)
                    

class presentation_Sash(Control):

    pass
class presentation_Scale(Control):

    def __init__(self, increment: str, maximum: str, minimum: str, pageIncrement: str, selection: str):
        self.increment = increment
        self.maximum = maximum
        self.minimum = minimum
        self.pageIncrement = pageIncrement
        self.selection = selection
        
    @property
    def increment(self) -> str:
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def pageIncrement(self) -> str:
        return self.__pageIncrement

    @pageIncrement.setter
    def pageIncrement(self, pageIncrement: str):
        self.__pageIncrement = pageIncrement

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

class presentation_Link(Control):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class presentation_Slider(Control):

    def __init__(self, selection: str, thumb: str, increment: str, maximum: str, minimum: str, pageIncrement: str):
        self.selection = selection
        self.thumb = thumb
        self.increment = increment
        self.maximum = maximum
        self.minimum = minimum
        self.pageIncrement = pageIncrement
        
    @property
    def increment(self) -> str:
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def pageIncrement(self) -> str:
        return self.__pageIncrement

    @pageIncrement.setter
    def pageIncrement(self, pageIncrement: str):
        self.__pageIncrement = pageIncrement

    @property
    def thumb(self) -> str:
        return self.__thumb

    @thumb.setter
    def thumb(self, thumb: str):
        self.__thumb = thumb

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

class presentation_Label(Control):

    def __init__(self, image: str, alignment: str, text: str):
        self.image = image
        self.alignment = alignment
        self.text = text
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

class presentation_Button(Control):

    def __init__(self, group1: str, alignment: str, grayed: str, image: str, selection: str, text: str, presentation_Button: set["presentation_ICommand"] = None, presentation_Button115: "presentation_Decorations" = None):
        self.group1 = group1
        self.alignment = alignment
        self.grayed = grayed
        self.image = image
        self.selection = selection
        self.text = text
        self.presentation_Button = presentation_Button if presentation_Button is not None else set()
        self.presentation_Button115 = presentation_Button115
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def grayed(self) -> str:
        return self.__grayed

    @grayed.setter
    def grayed(self, grayed: str):
        self.__grayed = grayed

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def presentation_Button(self):
        return self.__presentation_Button

    @presentation_Button.setter
    def presentation_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Button__presentation_Button", None)
        self.__presentation_Button = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ICommand"):
                    opp_val = getattr(item, "presentation_ICommand", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ICommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ICommand"):
                    opp_val = getattr(item, "presentation_ICommand", None)
                    
                    setattr(item, "presentation_ICommand", self)
                    

    @property
    def presentation_Button115(self):
        return self.__presentation_Button115

    @presentation_Button115.setter
    def presentation_Button115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Button__presentation_Button115", None)
        self.__presentation_Button115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Decorations"):
                opp_val = getattr(old_value, "presentation_Decorations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Decorations"):
                opp_val = getattr(value, "presentation_Decorations", None)
                if opp_val is None:
                    setattr(value, "presentation_Decorations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_Widget(ABC):

    def __init__(self, collapseEvent: str, dataContext: str, mixed: str, activateEvent: str, armEvent: str, closeEvent: str, deactivateEvent: str, defaultSelectionEvent: str, deiconifyEvent: str, eraseItemEvent: str, disposeEvent: str, dragDetectEvent: str, expandEvent: str, focusInEvent: str, focusOutEvent: str, hardKeyDownEvent: str, hideEvent: str, iconifyEvent: str, imeCompositionEvent: str, keyDownEvent: str, keyUpEvent: str, hardKeyUpEvent: str, helpEvent: str, menuDetectEvent: str, modifyEvent: str, mouseDoubleClickEvent: str, mouseDownEvent: str, mouseEnterEvent: str, measureItemEvent: str, mouseHoverEvent: str, mouseMoveEvent: str, mouseUpEvent: str, mouseWheelEvent: str, mouseExitEvent: str, paintEvent: str, paintItemEvent: str, resizeEvent: str, selectionEvent: str, setDataEvent: str, showEvent: str, moveEvent: str, traverseEvent: str, verifyEvent: str, style: str, presentation_Widget: "presentation_Binding" = None):
        self.collapseEvent = collapseEvent
        self.dataContext = dataContext
        self.mixed = mixed
        self.activateEvent = activateEvent
        self.armEvent = armEvent
        self.closeEvent = closeEvent
        self.deactivateEvent = deactivateEvent
        self.defaultSelectionEvent = defaultSelectionEvent
        self.deiconifyEvent = deiconifyEvent
        self.eraseItemEvent = eraseItemEvent
        self.disposeEvent = disposeEvent
        self.dragDetectEvent = dragDetectEvent
        self.expandEvent = expandEvent
        self.focusInEvent = focusInEvent
        self.focusOutEvent = focusOutEvent
        self.hardKeyDownEvent = hardKeyDownEvent
        self.hideEvent = hideEvent
        self.iconifyEvent = iconifyEvent
        self.imeCompositionEvent = imeCompositionEvent
        self.keyDownEvent = keyDownEvent
        self.keyUpEvent = keyUpEvent
        self.hardKeyUpEvent = hardKeyUpEvent
        self.helpEvent = helpEvent
        self.menuDetectEvent = menuDetectEvent
        self.modifyEvent = modifyEvent
        self.mouseDoubleClickEvent = mouseDoubleClickEvent
        self.mouseDownEvent = mouseDownEvent
        self.mouseEnterEvent = mouseEnterEvent
        self.measureItemEvent = measureItemEvent
        self.mouseHoverEvent = mouseHoverEvent
        self.mouseMoveEvent = mouseMoveEvent
        self.mouseUpEvent = mouseUpEvent
        self.mouseWheelEvent = mouseWheelEvent
        self.mouseExitEvent = mouseExitEvent
        self.paintEvent = paintEvent
        self.paintItemEvent = paintItemEvent
        self.resizeEvent = resizeEvent
        self.selectionEvent = selectionEvent
        self.setDataEvent = setDataEvent
        self.showEvent = showEvent
        self.moveEvent = moveEvent
        self.traverseEvent = traverseEvent
        self.verifyEvent = verifyEvent
        self.style = style
        self.presentation_Widget = presentation_Widget
        
    @property
    def collapseEvent(self) -> str:
        return self.__collapseEvent

    @collapseEvent.setter
    def collapseEvent(self, collapseEvent: str):
        self.__collapseEvent = collapseEvent

    @property
    def dragDetectEvent(self) -> str:
        return self.__dragDetectEvent

    @dragDetectEvent.setter
    def dragDetectEvent(self, dragDetectEvent: str):
        self.__dragDetectEvent = dragDetectEvent

    @property
    def hideEvent(self) -> str:
        return self.__hideEvent

    @hideEvent.setter
    def hideEvent(self, hideEvent: str):
        self.__hideEvent = hideEvent

    @property
    def focusInEvent(self) -> str:
        return self.__focusInEvent

    @focusInEvent.setter
    def focusInEvent(self, focusInEvent: str):
        self.__focusInEvent = focusInEvent

    @property
    def traverseEvent(self) -> str:
        return self.__traverseEvent

    @traverseEvent.setter
    def traverseEvent(self, traverseEvent: str):
        self.__traverseEvent = traverseEvent

    @property
    def selectionEvent(self) -> str:
        return self.__selectionEvent

    @selectionEvent.setter
    def selectionEvent(self, selectionEvent: str):
        self.__selectionEvent = selectionEvent

    @property
    def mouseMoveEvent(self) -> str:
        return self.__mouseMoveEvent

    @mouseMoveEvent.setter
    def mouseMoveEvent(self, mouseMoveEvent: str):
        self.__mouseMoveEvent = mouseMoveEvent

    @property
    def mouseEnterEvent(self) -> str:
        return self.__mouseEnterEvent

    @mouseEnterEvent.setter
    def mouseEnterEvent(self, mouseEnterEvent: str):
        self.__mouseEnterEvent = mouseEnterEvent

    @property
    def paintEvent(self) -> str:
        return self.__paintEvent

    @paintEvent.setter
    def paintEvent(self, paintEvent: str):
        self.__paintEvent = paintEvent

    @property
    def verifyEvent(self) -> str:
        return self.__verifyEvent

    @verifyEvent.setter
    def verifyEvent(self, verifyEvent: str):
        self.__verifyEvent = verifyEvent

    @property
    def mouseDoubleClickEvent(self) -> str:
        return self.__mouseDoubleClickEvent

    @mouseDoubleClickEvent.setter
    def mouseDoubleClickEvent(self, mouseDoubleClickEvent: str):
        self.__mouseDoubleClickEvent = mouseDoubleClickEvent

    @property
    def eraseItemEvent(self) -> str:
        return self.__eraseItemEvent

    @eraseItemEvent.setter
    def eraseItemEvent(self, eraseItemEvent: str):
        self.__eraseItemEvent = eraseItemEvent

    @property
    def helpEvent(self) -> str:
        return self.__helpEvent

    @helpEvent.setter
    def helpEvent(self, helpEvent: str):
        self.__helpEvent = helpEvent

    @property
    def armEvent(self) -> str:
        return self.__armEvent

    @armEvent.setter
    def armEvent(self, armEvent: str):
        self.__armEvent = armEvent

    @property
    def iconifyEvent(self) -> str:
        return self.__iconifyEvent

    @iconifyEvent.setter
    def iconifyEvent(self, iconifyEvent: str):
        self.__iconifyEvent = iconifyEvent

    @property
    def keyUpEvent(self) -> str:
        return self.__keyUpEvent

    @keyUpEvent.setter
    def keyUpEvent(self, keyUpEvent: str):
        self.__keyUpEvent = keyUpEvent

    @property
    def mouseExitEvent(self) -> str:
        return self.__mouseExitEvent

    @mouseExitEvent.setter
    def mouseExitEvent(self, mouseExitEvent: str):
        self.__mouseExitEvent = mouseExitEvent

    @property
    def showEvent(self) -> str:
        return self.__showEvent

    @showEvent.setter
    def showEvent(self, showEvent: str):
        self.__showEvent = showEvent

    @property
    def hardKeyUpEvent(self) -> str:
        return self.__hardKeyUpEvent

    @hardKeyUpEvent.setter
    def hardKeyUpEvent(self, hardKeyUpEvent: str):
        self.__hardKeyUpEvent = hardKeyUpEvent

    @property
    def setDataEvent(self) -> str:
        return self.__setDataEvent

    @setDataEvent.setter
    def setDataEvent(self, setDataEvent: str):
        self.__setDataEvent = setDataEvent

    @property
    def imeCompositionEvent(self) -> str:
        return self.__imeCompositionEvent

    @imeCompositionEvent.setter
    def imeCompositionEvent(self, imeCompositionEvent: str):
        self.__imeCompositionEvent = imeCompositionEvent

    @property
    def resizeEvent(self) -> str:
        return self.__resizeEvent

    @resizeEvent.setter
    def resizeEvent(self, resizeEvent: str):
        self.__resizeEvent = resizeEvent

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def measureItemEvent(self) -> str:
        return self.__measureItemEvent

    @measureItemEvent.setter
    def measureItemEvent(self, measureItemEvent: str):
        self.__measureItemEvent = measureItemEvent

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def closeEvent(self) -> str:
        return self.__closeEvent

    @closeEvent.setter
    def closeEvent(self, closeEvent: str):
        self.__closeEvent = closeEvent

    @property
    def keyDownEvent(self) -> str:
        return self.__keyDownEvent

    @keyDownEvent.setter
    def keyDownEvent(self, keyDownEvent: str):
        self.__keyDownEvent = keyDownEvent

    @property
    def activateEvent(self) -> str:
        return self.__activateEvent

    @activateEvent.setter
    def activateEvent(self, activateEvent: str):
        self.__activateEvent = activateEvent

    @property
    def focusOutEvent(self) -> str:
        return self.__focusOutEvent

    @focusOutEvent.setter
    def focusOutEvent(self, focusOutEvent: str):
        self.__focusOutEvent = focusOutEvent

    @property
    def mouseWheelEvent(self) -> str:
        return self.__mouseWheelEvent

    @mouseWheelEvent.setter
    def mouseWheelEvent(self, mouseWheelEvent: str):
        self.__mouseWheelEvent = mouseWheelEvent

    @property
    def defaultSelectionEvent(self) -> str:
        return self.__defaultSelectionEvent

    @defaultSelectionEvent.setter
    def defaultSelectionEvent(self, defaultSelectionEvent: str):
        self.__defaultSelectionEvent = defaultSelectionEvent

    @property
    def hardKeyDownEvent(self) -> str:
        return self.__hardKeyDownEvent

    @hardKeyDownEvent.setter
    def hardKeyDownEvent(self, hardKeyDownEvent: str):
        self.__hardKeyDownEvent = hardKeyDownEvent

    @property
    def deactivateEvent(self) -> str:
        return self.__deactivateEvent

    @deactivateEvent.setter
    def deactivateEvent(self, deactivateEvent: str):
        self.__deactivateEvent = deactivateEvent

    @property
    def paintItemEvent(self) -> str:
        return self.__paintItemEvent

    @paintItemEvent.setter
    def paintItemEvent(self, paintItemEvent: str):
        self.__paintItemEvent = paintItemEvent

    @property
    def menuDetectEvent(self) -> str:
        return self.__menuDetectEvent

    @menuDetectEvent.setter
    def menuDetectEvent(self, menuDetectEvent: str):
        self.__menuDetectEvent = menuDetectEvent

    @property
    def mouseDownEvent(self) -> str:
        return self.__mouseDownEvent

    @mouseDownEvent.setter
    def mouseDownEvent(self, mouseDownEvent: str):
        self.__mouseDownEvent = mouseDownEvent

    @property
    def deiconifyEvent(self) -> str:
        return self.__deiconifyEvent

    @deiconifyEvent.setter
    def deiconifyEvent(self, deiconifyEvent: str):
        self.__deiconifyEvent = deiconifyEvent

    @property
    def moveEvent(self) -> str:
        return self.__moveEvent

    @moveEvent.setter
    def moveEvent(self, moveEvent: str):
        self.__moveEvent = moveEvent

    @property
    def mouseHoverEvent(self) -> str:
        return self.__mouseHoverEvent

    @mouseHoverEvent.setter
    def mouseHoverEvent(self, mouseHoverEvent: str):
        self.__mouseHoverEvent = mouseHoverEvent

    @property
    def modifyEvent(self) -> str:
        return self.__modifyEvent

    @modifyEvent.setter
    def modifyEvent(self, modifyEvent: str):
        self.__modifyEvent = modifyEvent

    @property
    def dataContext(self) -> str:
        return self.__dataContext

    @dataContext.setter
    def dataContext(self, dataContext: str):
        self.__dataContext = dataContext

    @property
    def expandEvent(self) -> str:
        return self.__expandEvent

    @expandEvent.setter
    def expandEvent(self, expandEvent: str):
        self.__expandEvent = expandEvent

    @property
    def mouseUpEvent(self) -> str:
        return self.__mouseUpEvent

    @mouseUpEvent.setter
    def mouseUpEvent(self, mouseUpEvent: str):
        self.__mouseUpEvent = mouseUpEvent

    @property
    def disposeEvent(self) -> str:
        return self.__disposeEvent

    @disposeEvent.setter
    def disposeEvent(self, disposeEvent: str):
        self.__disposeEvent = disposeEvent

    @property
    def presentation_Widget(self):
        return self.__presentation_Widget

    @presentation_Widget.setter
    def presentation_Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Widget__presentation_Widget", None)
        self.__presentation_Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Binding13"):
                opp_val = getattr(old_value, "presentation_Binding13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Binding13"):
                opp_val = getattr(value, "presentation_Binding13", None)
                if opp_val is None:
                    setattr(value, "presentation_Binding13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Composite:

    pass
class presentation_CTabFolder(Composite):

    def __init__(self, group3: str, borderVisible: str, marginHeight: str, marginWidth: str, maximized: str, maximizeVisible: str, mINTABWIDTH: str, minimized: str, minimizeVisible: str, minimumCharacters: str, mRUVisible: str, selectionBackground: str, selectionForeground: str, simple: str, single: str, tabHeight: str, tabPosition: str, unselectedCloseVisible: str, unselectedImageVisible: str, presentation_CTabFolder: set["presentation_RGB"] = None, presentation_CTabFolder100: set["presentation_RGB"] = None, presentation_CTabFolder103: set["presentation_CTabItem"] = None, presentation_CTabFolder95: set["presentation_CTabItem"] = None, presentation_CTabFolder106: set["presentation_RGB"] = None, presentation_CTabFolder97: set["presentation_Control"] = None, presentation_CTabFolder110: "presentation_CTabItem" = None):
        self.group3 = group3
        self.borderVisible = borderVisible
        self.marginHeight = marginHeight
        self.marginWidth = marginWidth
        self.maximized = maximized
        self.maximizeVisible = maximizeVisible
        self.mINTABWIDTH = mINTABWIDTH
        self.minimized = minimized
        self.minimizeVisible = minimizeVisible
        self.minimumCharacters = minimumCharacters
        self.mRUVisible = mRUVisible
        self.selectionBackground = selectionBackground
        self.selectionForeground = selectionForeground
        self.simple = simple
        self.single = single
        self.tabHeight = tabHeight
        self.tabPosition = tabPosition
        self.unselectedCloseVisible = unselectedCloseVisible
        self.unselectedImageVisible = unselectedImageVisible
        self.presentation_CTabFolder = presentation_CTabFolder if presentation_CTabFolder is not None else set()
        self.presentation_CTabFolder100 = presentation_CTabFolder100 if presentation_CTabFolder100 is not None else set()
        self.presentation_CTabFolder103 = presentation_CTabFolder103 if presentation_CTabFolder103 is not None else set()
        self.presentation_CTabFolder95 = presentation_CTabFolder95 if presentation_CTabFolder95 is not None else set()
        self.presentation_CTabFolder106 = presentation_CTabFolder106 if presentation_CTabFolder106 is not None else set()
        self.presentation_CTabFolder97 = presentation_CTabFolder97 if presentation_CTabFolder97 is not None else set()
        self.presentation_CTabFolder110 = presentation_CTabFolder110
        
    @property
    def simple(self) -> str:
        return self.__simple

    @simple.setter
    def simple(self, simple: str):
        self.__simple = simple

    @property
    def mRUVisible(self) -> str:
        return self.__mRUVisible

    @mRUVisible.setter
    def mRUVisible(self, mRUVisible: str):
        self.__mRUVisible = mRUVisible

    @property
    def maximizeVisible(self) -> str:
        return self.__maximizeVisible

    @maximizeVisible.setter
    def maximizeVisible(self, maximizeVisible: str):
        self.__maximizeVisible = maximizeVisible

    @property
    def minimumCharacters(self) -> str:
        return self.__minimumCharacters

    @minimumCharacters.setter
    def minimumCharacters(self, minimumCharacters: str):
        self.__minimumCharacters = minimumCharacters

    @property
    def minimized(self) -> str:
        return self.__minimized

    @minimized.setter
    def minimized(self, minimized: str):
        self.__minimized = minimized

    @property
    def maximized(self) -> str:
        return self.__maximized

    @maximized.setter
    def maximized(self, maximized: str):
        self.__maximized = maximized

    @property
    def borderVisible(self) -> str:
        return self.__borderVisible

    @borderVisible.setter
    def borderVisible(self, borderVisible: str):
        self.__borderVisible = borderVisible

    @property
    def tabPosition(self) -> str:
        return self.__tabPosition

    @tabPosition.setter
    def tabPosition(self, tabPosition: str):
        self.__tabPosition = tabPosition

    @property
    def marginHeight(self) -> str:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: str):
        self.__marginHeight = marginHeight

    @property
    def single(self) -> str:
        return self.__single

    @single.setter
    def single(self, single: str):
        self.__single = single

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def tabHeight(self) -> str:
        return self.__tabHeight

    @tabHeight.setter
    def tabHeight(self, tabHeight: str):
        self.__tabHeight = tabHeight

    @property
    def selectionForeground(self) -> str:
        return self.__selectionForeground

    @selectionForeground.setter
    def selectionForeground(self, selectionForeground: str):
        self.__selectionForeground = selectionForeground

    @property
    def mINTABWIDTH(self) -> str:
        return self.__mINTABWIDTH

    @mINTABWIDTH.setter
    def mINTABWIDTH(self, mINTABWIDTH: str):
        self.__mINTABWIDTH = mINTABWIDTH

    @property
    def marginWidth(self) -> str:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: str):
        self.__marginWidth = marginWidth

    @property
    def selectionBackground(self) -> str:
        return self.__selectionBackground

    @selectionBackground.setter
    def selectionBackground(self, selectionBackground: str):
        self.__selectionBackground = selectionBackground

    @property
    def unselectedCloseVisible(self) -> str:
        return self.__unselectedCloseVisible

    @unselectedCloseVisible.setter
    def unselectedCloseVisible(self, unselectedCloseVisible: str):
        self.__unselectedCloseVisible = unselectedCloseVisible

    @property
    def unselectedImageVisible(self) -> str:
        return self.__unselectedImageVisible

    @unselectedImageVisible.setter
    def unselectedImageVisible(self, unselectedImageVisible: str):
        self.__unselectedImageVisible = unselectedImageVisible

    @property
    def minimizeVisible(self) -> str:
        return self.__minimizeVisible

    @minimizeVisible.setter
    def minimizeVisible(self, minimizeVisible: str):
        self.__minimizeVisible = minimizeVisible

    @property
    def presentation_CTabFolder103(self):
        return self.__presentation_CTabFolder103

    @presentation_CTabFolder103.setter
    def presentation_CTabFolder103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder103", None)
        self.__presentation_CTabFolder103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CTabItem104"):
                    opp_val = getattr(item, "presentation_CTabItem104", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CTabItem104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CTabItem104"):
                    opp_val = getattr(item, "presentation_CTabItem104", None)
                    
                    setattr(item, "presentation_CTabItem104", self)
                    

    @property
    def presentation_CTabFolder100(self):
        return self.__presentation_CTabFolder100

    @presentation_CTabFolder100.setter
    def presentation_CTabFolder100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder100", None)
        self.__presentation_CTabFolder100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_RGB101"):
                    opp_val = getattr(item, "presentation_RGB101", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_RGB101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_RGB101"):
                    opp_val = getattr(item, "presentation_RGB101", None)
                    
                    setattr(item, "presentation_RGB101", self)
                    

    @property
    def presentation_CTabFolder(self):
        return self.__presentation_CTabFolder

    @presentation_CTabFolder.setter
    def presentation_CTabFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder", None)
        self.__presentation_CTabFolder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_RGB"):
                    opp_val = getattr(item, "presentation_RGB", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_RGB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_RGB"):
                    opp_val = getattr(item, "presentation_RGB", None)
                    
                    setattr(item, "presentation_RGB", self)
                    

    @property
    def presentation_CTabFolder110(self):
        return self.__presentation_CTabFolder110

    @presentation_CTabFolder110.setter
    def presentation_CTabFolder110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder110", None)
        self.__presentation_CTabFolder110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CTabItem109"):
                opp_val = getattr(old_value, "presentation_CTabItem109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CTabItem109"):
                opp_val = getattr(value, "presentation_CTabItem109", None)
                if opp_val is None:
                    setattr(value, "presentation_CTabItem109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_CTabFolder106(self):
        return self.__presentation_CTabFolder106

    @presentation_CTabFolder106.setter
    def presentation_CTabFolder106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder106", None)
        self.__presentation_CTabFolder106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_RGB107"):
                    opp_val = getattr(item, "presentation_RGB107", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_RGB107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_RGB107"):
                    opp_val = getattr(item, "presentation_RGB107", None)
                    
                    setattr(item, "presentation_RGB107", self)
                    

    @property
    def presentation_CTabFolder97(self):
        return self.__presentation_CTabFolder97

    @presentation_CTabFolder97.setter
    def presentation_CTabFolder97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder97", None)
        self.__presentation_CTabFolder97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control98"):
                    opp_val = getattr(item, "presentation_Control98", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control98"):
                    opp_val = getattr(item, "presentation_Control98", None)
                    
                    setattr(item, "presentation_Control98", self)
                    

    @property
    def presentation_CTabFolder95(self):
        return self.__presentation_CTabFolder95

    @presentation_CTabFolder95.setter
    def presentation_CTabFolder95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CTabFolder__presentation_CTabFolder95", None)
        self.__presentation_CTabFolder95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CTabItem"):
                    opp_val = getattr(item, "presentation_CTabItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CTabItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CTabItem"):
                    opp_val = getattr(item, "presentation_CTabItem", None)
                    
                    setattr(item, "presentation_CTabItem", self)
                    

class presentation_ToolBar(Composite):

    def __init__(self, group3: str, presentation_ToolBar: set["presentation_ToolItem"] = None, presentation_ToolBar259: "presentation_ToolItem" = None):
        self.group3 = group3
        self.presentation_ToolBar = presentation_ToolBar if presentation_ToolBar is not None else set()
        self.presentation_ToolBar259 = presentation_ToolBar259
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_ToolBar(self):
        return self.__presentation_ToolBar

    @presentation_ToolBar.setter
    def presentation_ToolBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ToolBar__presentation_ToolBar", None)
        self.__presentation_ToolBar = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ToolItem"):
                    opp_val = getattr(item, "presentation_ToolItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ToolItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ToolItem"):
                    opp_val = getattr(item, "presentation_ToolItem", None)
                    
                    setattr(item, "presentation_ToolItem", self)
                    

    @property
    def presentation_ToolBar259(self):
        return self.__presentation_ToolBar259

    @presentation_ToolBar259.setter
    def presentation_ToolBar259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ToolBar__presentation_ToolBar259", None)
        self.__presentation_ToolBar259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ToolItem258"):
                opp_val = getattr(old_value, "presentation_ToolItem258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ToolItem258"):
                opp_val = getattr(value, "presentation_ToolItem258", None)
                if opp_val is None:
                    setattr(value, "presentation_ToolItem258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_TableTree(Composite):

    pass
class presentation_TabFolder(Composite):

    def __init__(self, group3: str, presentation_TabFolder: set["presentation_TabItem"] = None, presentation_TabFolder213: set["presentation_TabItem"] = None, presentation_TabFolder217: "presentation_TabItem" = None):
        self.group3 = group3
        self.presentation_TabFolder = presentation_TabFolder if presentation_TabFolder is not None else set()
        self.presentation_TabFolder213 = presentation_TabFolder213 if presentation_TabFolder213 is not None else set()
        self.presentation_TabFolder217 = presentation_TabFolder217
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_TabFolder217(self):
        return self.__presentation_TabFolder217

    @presentation_TabFolder217.setter
    def presentation_TabFolder217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabFolder__presentation_TabFolder217", None)
        self.__presentation_TabFolder217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TabItem216"):
                opp_val = getattr(old_value, "presentation_TabItem216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TabItem216"):
                opp_val = getattr(value, "presentation_TabItem216", None)
                if opp_val is None:
                    setattr(value, "presentation_TabItem216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_TabFolder213(self):
        return self.__presentation_TabFolder213

    @presentation_TabFolder213.setter
    def presentation_TabFolder213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabFolder__presentation_TabFolder213", None)
        self.__presentation_TabFolder213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TabItem214"):
                    opp_val = getattr(item, "presentation_TabItem214", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TabItem214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TabItem214"):
                    opp_val = getattr(item, "presentation_TabItem214", None)
                    
                    setattr(item, "presentation_TabItem214", self)
                    

    @property
    def presentation_TabFolder(self):
        return self.__presentation_TabFolder

    @presentation_TabFolder.setter
    def presentation_TabFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TabFolder__presentation_TabFolder", None)
        self.__presentation_TabFolder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TabItem"):
                    opp_val = getattr(item, "presentation_TabItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TabItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TabItem"):
                    opp_val = getattr(item, "presentation_TabItem", None)
                    
                    setattr(item, "presentation_TabItem", self)
                    

class presentation_SashForm(Composite):

    def __init__(self, group3: str, sashWidth1: str, weights: str, orientation: str, sASHWIDTH: str, presentation_SashForm: set["presentation_Control"] = None):
        self.group3 = group3
        self.sashWidth1 = sashWidth1
        self.weights = weights
        self.orientation = orientation
        self.sASHWIDTH = sASHWIDTH
        self.presentation_SashForm = presentation_SashForm if presentation_SashForm is not None else set()
        
    @property
    def sashWidth1(self) -> str:
        return self.__sashWidth1

    @sashWidth1.setter
    def sashWidth1(self, sashWidth1: str):
        self.__sashWidth1 = sashWidth1

    @property
    def sASHWIDTH(self) -> str:
        return self.__sASHWIDTH

    @sASHWIDTH.setter
    def sASHWIDTH(self, sASHWIDTH: str):
        self.__sASHWIDTH = sASHWIDTH

    @property
    def weights(self) -> str:
        return self.__weights

    @weights.setter
    def weights(self, weights: str):
        self.__weights = weights

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_SashForm(self):
        return self.__presentation_SashForm

    @presentation_SashForm.setter
    def presentation_SashForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SashForm__presentation_SashForm", None)
        self.__presentation_SashForm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Control186"):
                    opp_val = getattr(item, "presentation_Control186", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Control186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Control186"):
                    opp_val = getattr(item, "presentation_Control186", None)
                    
                    setattr(item, "presentation_Control186", self)
                    

class presentation_Group(Composite):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class presentation_CCombo(Composite):

    def __init__(self, group3: str, items: str, editable: str, listVisible: str, selection: str, text: str, textLimit: str, visibleItemCount: str):
        self.group3 = group3
        self.items = items
        self.editable = editable
        self.listVisible = listVisible
        self.selection = selection
        self.text = text
        self.textLimit = textLimit
        self.visibleItemCount = visibleItemCount
        
    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def textLimit(self) -> str:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: str):
        self.__textLimit = textLimit

    @property
    def visibleItemCount(self) -> str:
        return self.__visibleItemCount

    @visibleItemCount.setter
    def visibleItemCount(self, visibleItemCount: str):
        self.__visibleItemCount = visibleItemCount

    @property
    def listVisible(self) -> str:
        return self.__listVisible

    @listVisible.setter
    def listVisible(self, listVisible: str):
        self.__listVisible = listVisible

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def editable(self) -> str:
        return self.__editable

    @editable.setter
    def editable(self, editable: str):
        self.__editable = editable

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

class presentation_DateTime(Composite):

    def __init__(self, day: str, hours: str, minutes: str, month: str, seconds: str, year: str):
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.month = month
        self.seconds = seconds
        self.year = year
        
    @property
    def hours(self) -> str:
        return self.__hours

    @hours.setter
    def hours(self, hours: str):
        self.__hours = hours

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def seconds(self) -> str:
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: str):
        self.__seconds = seconds

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def minutes(self) -> str:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: str):
        self.__minutes = minutes

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

class presentation_Combo(Composite):

    def __init__(self, listVisible: str, group3: str, items: str, orientation: str, selection: str, text: str, textLimit: str, visibleItemCount: str):
        self.listVisible = listVisible
        self.group3 = group3
        self.items = items
        self.orientation = orientation
        self.selection = selection
        self.text = text
        self.textLimit = textLimit
        self.visibleItemCount = visibleItemCount
        
    @property
    def listVisible(self) -> str:
        return self.__listVisible

    @listVisible.setter
    def listVisible(self, listVisible: str):
        self.__listVisible = listVisible

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def textLimit(self) -> str:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: str):
        self.__textLimit = textLimit

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def visibleItemCount(self) -> str:
        return self.__visibleItemCount

    @visibleItemCount.setter
    def visibleItemCount(self, visibleItemCount: str):
        self.__visibleItemCount = visibleItemCount

    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

class presentation_CoolBar(Composite):

    def __init__(self, group3: str, itemOrder: str, itemSizes: str, locked: str, wrapIndices: str, presentation_CoolBar: set["presentation_CoolItem"] = None, presentation_CoolBar89: "presentation_CoolItem" = None):
        self.group3 = group3
        self.itemOrder = itemOrder
        self.itemSizes = itemSizes
        self.locked = locked
        self.wrapIndices = wrapIndices
        self.presentation_CoolBar = presentation_CoolBar if presentation_CoolBar is not None else set()
        self.presentation_CoolBar89 = presentation_CoolBar89
        
    @property
    def wrapIndices(self) -> str:
        return self.__wrapIndices

    @wrapIndices.setter
    def wrapIndices(self, wrapIndices: str):
        self.__wrapIndices = wrapIndices

    @property
    def itemOrder(self) -> str:
        return self.__itemOrder

    @itemOrder.setter
    def itemOrder(self, itemOrder: str):
        self.__itemOrder = itemOrder

    @property
    def itemSizes(self) -> str:
        return self.__itemSizes

    @itemSizes.setter
    def itemSizes(self, itemSizes: str):
        self.__itemSizes = itemSizes

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def locked(self) -> str:
        return self.__locked

    @locked.setter
    def locked(self, locked: str):
        self.__locked = locked

    @property
    def presentation_CoolBar(self):
        return self.__presentation_CoolBar

    @presentation_CoolBar.setter
    def presentation_CoolBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CoolBar__presentation_CoolBar", None)
        self.__presentation_CoolBar = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CoolItem"):
                    opp_val = getattr(item, "presentation_CoolItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CoolItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CoolItem"):
                    opp_val = getattr(item, "presentation_CoolItem", None)
                    
                    setattr(item, "presentation_CoolItem", self)
                    

    @property
    def presentation_CoolBar89(self):
        return self.__presentation_CoolBar89

    @presentation_CoolBar89.setter
    def presentation_CoolBar89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_CoolBar__presentation_CoolBar89", None)
        self.__presentation_CoolBar89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_CoolItem88"):
                opp_val = getattr(old_value, "presentation_CoolItem88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_CoolItem88"):
                opp_val = getattr(value, "presentation_CoolItem88", None)
                if opp_val is None:
                    setattr(value, "presentation_CoolItem88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_Tree(Composite):

    def __init__(self, group3: str, columnOrder: str, headerVisible: str, itemCount: str, linesVisible: str, sortDirection: str, presentation_Tree: set["presentation_TreeColumn"] = None, presentation_Tree268: set["presentation_TreeItem"] = None, presentation_Tree270: set["presentation_TreeColumn"] = None, presentation_Tree273: set["presentation_TreeItem"] = None, presentation_Tree276: set["presentation_TreeItem"] = None, presentation_Tree279: set["presentation_TreeItem"] = None, presentation_Tree283: "presentation_TreeColumn" = None, presentation_Tree292: "presentation_TreeItem" = None, presentation_Tree294: "presentation_TreeViewer" = None):
        self.group3 = group3
        self.columnOrder = columnOrder
        self.headerVisible = headerVisible
        self.itemCount = itemCount
        self.linesVisible = linesVisible
        self.sortDirection = sortDirection
        self.presentation_Tree = presentation_Tree if presentation_Tree is not None else set()
        self.presentation_Tree268 = presentation_Tree268 if presentation_Tree268 is not None else set()
        self.presentation_Tree270 = presentation_Tree270 if presentation_Tree270 is not None else set()
        self.presentation_Tree273 = presentation_Tree273 if presentation_Tree273 is not None else set()
        self.presentation_Tree276 = presentation_Tree276 if presentation_Tree276 is not None else set()
        self.presentation_Tree279 = presentation_Tree279 if presentation_Tree279 is not None else set()
        self.presentation_Tree283 = presentation_Tree283
        self.presentation_Tree292 = presentation_Tree292
        self.presentation_Tree294 = presentation_Tree294
        
    @property
    def linesVisible(self) -> str:
        return self.__linesVisible

    @linesVisible.setter
    def linesVisible(self, linesVisible: str):
        self.__linesVisible = linesVisible

    @property
    def sortDirection(self) -> str:
        return self.__sortDirection

    @sortDirection.setter
    def sortDirection(self, sortDirection: str):
        self.__sortDirection = sortDirection

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def columnOrder(self) -> str:
        return self.__columnOrder

    @columnOrder.setter
    def columnOrder(self, columnOrder: str):
        self.__columnOrder = columnOrder

    @property
    def itemCount(self) -> str:
        return self.__itemCount

    @itemCount.setter
    def itemCount(self, itemCount: str):
        self.__itemCount = itemCount

    @property
    def headerVisible(self) -> str:
        return self.__headerVisible

    @headerVisible.setter
    def headerVisible(self, headerVisible: str):
        self.__headerVisible = headerVisible

    @property
    def presentation_Tree294(self):
        return self.__presentation_Tree294

    @presentation_Tree294.setter
    def presentation_Tree294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree294", None)
        self.__presentation_Tree294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TreeViewer"):
                opp_val = getattr(old_value, "presentation_TreeViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TreeViewer"):
                opp_val = getattr(value, "presentation_TreeViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_TreeViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Tree292(self):
        return self.__presentation_Tree292

    @presentation_Tree292.setter
    def presentation_Tree292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree292", None)
        self.__presentation_Tree292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TreeItem291"):
                opp_val = getattr(old_value, "presentation_TreeItem291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TreeItem291"):
                opp_val = getattr(value, "presentation_TreeItem291", None)
                if opp_val is None:
                    setattr(value, "presentation_TreeItem291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Tree(self):
        return self.__presentation_Tree

    @presentation_Tree.setter
    def presentation_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree", None)
        self.__presentation_Tree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeColumn"):
                    opp_val = getattr(item, "presentation_TreeColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeColumn"):
                    opp_val = getattr(item, "presentation_TreeColumn", None)
                    
                    setattr(item, "presentation_TreeColumn", self)
                    

    @property
    def presentation_Tree273(self):
        return self.__presentation_Tree273

    @presentation_Tree273.setter
    def presentation_Tree273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree273", None)
        self.__presentation_Tree273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeItem274"):
                    opp_val = getattr(item, "presentation_TreeItem274", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeItem274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeItem274"):
                    opp_val = getattr(item, "presentation_TreeItem274", None)
                    
                    setattr(item, "presentation_TreeItem274", self)
                    

    @property
    def presentation_Tree268(self):
        return self.__presentation_Tree268

    @presentation_Tree268.setter
    def presentation_Tree268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree268", None)
        self.__presentation_Tree268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeItem"):
                    opp_val = getattr(item, "presentation_TreeItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeItem"):
                    opp_val = getattr(item, "presentation_TreeItem", None)
                    
                    setattr(item, "presentation_TreeItem", self)
                    

    @property
    def presentation_Tree279(self):
        return self.__presentation_Tree279

    @presentation_Tree279.setter
    def presentation_Tree279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree279", None)
        self.__presentation_Tree279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeItem280"):
                    opp_val = getattr(item, "presentation_TreeItem280", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeItem280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeItem280"):
                    opp_val = getattr(item, "presentation_TreeItem280", None)
                    
                    setattr(item, "presentation_TreeItem280", self)
                    

    @property
    def presentation_Tree276(self):
        return self.__presentation_Tree276

    @presentation_Tree276.setter
    def presentation_Tree276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree276", None)
        self.__presentation_Tree276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeItem277"):
                    opp_val = getattr(item, "presentation_TreeItem277", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeItem277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeItem277"):
                    opp_val = getattr(item, "presentation_TreeItem277", None)
                    
                    setattr(item, "presentation_TreeItem277", self)
                    

    @property
    def presentation_Tree283(self):
        return self.__presentation_Tree283

    @presentation_Tree283.setter
    def presentation_Tree283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree283", None)
        self.__presentation_Tree283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TreeColumn282"):
                opp_val = getattr(old_value, "presentation_TreeColumn282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TreeColumn282"):
                opp_val = getattr(value, "presentation_TreeColumn282", None)
                if opp_val is None:
                    setattr(value, "presentation_TreeColumn282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Tree270(self):
        return self.__presentation_Tree270

    @presentation_Tree270.setter
    def presentation_Tree270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Tree__presentation_Tree270", None)
        self.__presentation_Tree270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreeColumn271"):
                    opp_val = getattr(item, "presentation_TreeColumn271", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreeColumn271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreeColumn271"):
                    opp_val = getattr(item, "presentation_TreeColumn271", None)
                    
                    setattr(item, "presentation_TreeColumn271", self)
                    

class presentation_Canvas(Composite):

    def __init__(self, mixed1: str, group3: str, presentation_Canvas: set["presentation_IME"] = None, presentation_Canvas19: set["presentation_Caret"] = None, presentation_Canvas22: "presentation_Caret" = None):
        self.mixed1 = mixed1
        self.group3 = group3
        self.presentation_Canvas = presentation_Canvas if presentation_Canvas is not None else set()
        self.presentation_Canvas19 = presentation_Canvas19 if presentation_Canvas19 is not None else set()
        self.presentation_Canvas22 = presentation_Canvas22
        
    @property
    def mixed1(self) -> str:
        return self.__mixed1

    @mixed1.setter
    def mixed1(self, mixed1: str):
        self.__mixed1 = mixed1

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_Canvas19(self):
        return self.__presentation_Canvas19

    @presentation_Canvas19.setter
    def presentation_Canvas19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Canvas__presentation_Canvas19", None)
        self.__presentation_Canvas19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Caret"):
                    opp_val = getattr(item, "presentation_Caret", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Caret", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Caret"):
                    opp_val = getattr(item, "presentation_Caret", None)
                    
                    setattr(item, "presentation_Caret", self)
                    

    @property
    def presentation_Canvas22(self):
        return self.__presentation_Canvas22

    @presentation_Canvas22.setter
    def presentation_Canvas22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Canvas__presentation_Canvas22", None)
        self.__presentation_Canvas22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Caret21"):
                opp_val = getattr(old_value, "presentation_Caret21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Caret21"):
                opp_val = getattr(value, "presentation_Caret21", None)
                if opp_val is None:
                    setattr(value, "presentation_Caret21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Canvas(self):
        return self.__presentation_Canvas

    @presentation_Canvas.setter
    def presentation_Canvas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Canvas__presentation_Canvas", None)
        self.__presentation_Canvas = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IME"):
                    opp_val = getattr(item, "presentation_IME", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IME", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IME"):
                    opp_val = getattr(item, "presentation_IME", None)
                    
                    setattr(item, "presentation_IME", self)
                    

class presentation_Spinner(Composite):

    def __init__(self, digits: str, pageIncrement: str, selection: str, text: str, textLimit: str, increment: str, maximum: str, minimum: str):
        self.digits = digits
        self.pageIncrement = pageIncrement
        self.selection = selection
        self.text = text
        self.textLimit = textLimit
        self.increment = increment
        self.maximum = maximum
        self.minimum = minimum
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def pageIncrement(self) -> str:
        return self.__pageIncrement

    @pageIncrement.setter
    def pageIncrement(self, pageIncrement: str):
        self.__pageIncrement = pageIncrement

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def increment(self) -> str:
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment

    @property
    def textLimit(self) -> str:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: str):
        self.__textLimit = textLimit

    @property
    def digits(self) -> str:
        return self.__digits

    @digits.setter
    def digits(self, digits: str):
        self.__digits = digits

class presentation_ExpandBar(Composite):

    def __init__(self, group3: str, spacing: str, presentation_ExpandBar: set["presentation_ExpandItem"] = None, presentation_ExpandBar135: "presentation_ExpandItem" = None):
        self.group3 = group3
        self.spacing = spacing
        self.presentation_ExpandBar = presentation_ExpandBar if presentation_ExpandBar is not None else set()
        self.presentation_ExpandBar135 = presentation_ExpandBar135
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def spacing(self) -> str:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: str):
        self.__spacing = spacing

    @property
    def presentation_ExpandBar135(self):
        return self.__presentation_ExpandBar135

    @presentation_ExpandBar135.setter
    def presentation_ExpandBar135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ExpandBar__presentation_ExpandBar135", None)
        self.__presentation_ExpandBar135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ExpandItem134"):
                opp_val = getattr(old_value, "presentation_ExpandItem134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ExpandItem134"):
                opp_val = getattr(value, "presentation_ExpandItem134", None)
                if opp_val is None:
                    setattr(value, "presentation_ExpandItem134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_ExpandBar(self):
        return self.__presentation_ExpandBar

    @presentation_ExpandBar.setter
    def presentation_ExpandBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ExpandBar__presentation_ExpandBar", None)
        self.__presentation_ExpandBar = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ExpandItem"):
                    opp_val = getattr(item, "presentation_ExpandItem", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ExpandItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ExpandItem"):
                    opp_val = getattr(item, "presentation_ExpandItem", None)
                    
                    setattr(item, "presentation_ExpandItem", self)
                    

class presentation_Table(Composite):

    def __init__(self, group3: str, columnOrder: str, selectionIndices: str, headerVisible: str, itemCount: str, linesVisible: str, sortDirection: str, topIndex: str, presentation_Table: set["presentation_TableColumn"] = None, presentation_Table223: set["presentation_TableColumn"] = None, presentation_Table226: set["presentation_TableItem"] = None, presentation_Table229: set["presentation_TableItem"] = None, presentation_Table235: "presentation_TableColumn" = None, presentation_Table242: "presentation_TableItem" = None, presentation_Table248: "presentation_TableViewer" = None):
        self.group3 = group3
        self.columnOrder = columnOrder
        self.selectionIndices = selectionIndices
        self.headerVisible = headerVisible
        self.itemCount = itemCount
        self.linesVisible = linesVisible
        self.sortDirection = sortDirection
        self.topIndex = topIndex
        self.presentation_Table = presentation_Table if presentation_Table is not None else set()
        self.presentation_Table223 = presentation_Table223 if presentation_Table223 is not None else set()
        self.presentation_Table226 = presentation_Table226 if presentation_Table226 is not None else set()
        self.presentation_Table229 = presentation_Table229 if presentation_Table229 is not None else set()
        self.presentation_Table235 = presentation_Table235
        self.presentation_Table242 = presentation_Table242
        self.presentation_Table248 = presentation_Table248
        
    @property
    def sortDirection(self) -> str:
        return self.__sortDirection

    @sortDirection.setter
    def sortDirection(self, sortDirection: str):
        self.__sortDirection = sortDirection

    @property
    def topIndex(self) -> str:
        return self.__topIndex

    @topIndex.setter
    def topIndex(self, topIndex: str):
        self.__topIndex = topIndex

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def columnOrder(self) -> str:
        return self.__columnOrder

    @columnOrder.setter
    def columnOrder(self, columnOrder: str):
        self.__columnOrder = columnOrder

    @property
    def linesVisible(self) -> str:
        return self.__linesVisible

    @linesVisible.setter
    def linesVisible(self, linesVisible: str):
        self.__linesVisible = linesVisible

    @property
    def headerVisible(self) -> str:
        return self.__headerVisible

    @headerVisible.setter
    def headerVisible(self, headerVisible: str):
        self.__headerVisible = headerVisible

    @property
    def itemCount(self) -> str:
        return self.__itemCount

    @itemCount.setter
    def itemCount(self, itemCount: str):
        self.__itemCount = itemCount

    @property
    def selectionIndices(self) -> str:
        return self.__selectionIndices

    @selectionIndices.setter
    def selectionIndices(self, selectionIndices: str):
        self.__selectionIndices = selectionIndices

    @property
    def presentation_Table248(self):
        return self.__presentation_Table248

    @presentation_Table248.setter
    def presentation_Table248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table248", None)
        self.__presentation_Table248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableViewer"):
                opp_val = getattr(old_value, "presentation_TableViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableViewer"):
                opp_val = getattr(value, "presentation_TableViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_TableViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Table(self):
        return self.__presentation_Table

    @presentation_Table.setter
    def presentation_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table", None)
        self.__presentation_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableColumn"):
                    opp_val = getattr(item, "presentation_TableColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableColumn"):
                    opp_val = getattr(item, "presentation_TableColumn", None)
                    
                    setattr(item, "presentation_TableColumn", self)
                    

    @property
    def presentation_Table226(self):
        return self.__presentation_Table226

    @presentation_Table226.setter
    def presentation_Table226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table226", None)
        self.__presentation_Table226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableItem227"):
                    opp_val = getattr(item, "presentation_TableItem227", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableItem227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableItem227"):
                    opp_val = getattr(item, "presentation_TableItem227", None)
                    
                    setattr(item, "presentation_TableItem227", self)
                    

    @property
    def presentation_Table235(self):
        return self.__presentation_Table235

    @presentation_Table235.setter
    def presentation_Table235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table235", None)
        self.__presentation_Table235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableColumn234"):
                opp_val = getattr(old_value, "presentation_TableColumn234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableColumn234"):
                opp_val = getattr(value, "presentation_TableColumn234", None)
                if opp_val is None:
                    setattr(value, "presentation_TableColumn234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_Table223(self):
        return self.__presentation_Table223

    @presentation_Table223.setter
    def presentation_Table223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table223", None)
        self.__presentation_Table223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableColumn224"):
                    opp_val = getattr(item, "presentation_TableColumn224", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableColumn224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableColumn224"):
                    opp_val = getattr(item, "presentation_TableColumn224", None)
                    
                    setattr(item, "presentation_TableColumn224", self)
                    

    @property
    def presentation_Table229(self):
        return self.__presentation_Table229

    @presentation_Table229.setter
    def presentation_Table229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table229", None)
        self.__presentation_Table229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TableItem230"):
                    opp_val = getattr(item, "presentation_TableItem230", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TableItem230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TableItem230"):
                    opp_val = getattr(item, "presentation_TableItem230", None)
                    
                    setattr(item, "presentation_TableItem230", self)
                    

    @property
    def presentation_Table242(self):
        return self.__presentation_Table242

    @presentation_Table242.setter
    def presentation_Table242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Table__presentation_Table242", None)
        self.__presentation_Table242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_TableItem241"):
                opp_val = getattr(old_value, "presentation_TableItem241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_TableItem241"):
                opp_val = getattr(value, "presentation_TableItem241", None)
                if opp_val is None:
                    setattr(value, "presentation_TableItem241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_Browser(Composite):

    def __init__(self, group3: str, browserType: str, text: str, url: str, presentation_Browser: set["presentation_EObject"] = None):
        self.group3 = group3
        self.browserType = browserType
        self.text = text
        self.url = url
        self.presentation_Browser = presentation_Browser if presentation_Browser is not None else set()
        
    @property
    def browserType(self) -> str:
        return self.__browserType

    @browserType.setter
    def browserType(self, browserType: str):
        self.__browserType = browserType

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_Browser(self):
        return self.__presentation_Browser

    @presentation_Browser.setter
    def presentation_Browser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Browser__presentation_Browser", None)
        self.__presentation_Browser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject15"):
                    opp_val = getattr(item, "presentation_EObject15", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject15"):
                    opp_val = getattr(item, "presentation_EObject15", None)
                    
                    setattr(item, "presentation_EObject15", self)
                    

class presentation_Binding:

    def __init__(self, mixed: str, group: str, elementName: str, path: str, xPath: str, presentation_Binding10: set["presentation_EObject"] = None, presentation_Binding: set["presentation_EObject"] = None, presentation_Binding13: set["presentation_Widget"] = None):
        self.mixed = mixed
        self.group = group
        self.elementName = elementName
        self.path = path
        self.xPath = xPath
        self.presentation_Binding10 = presentation_Binding10 if presentation_Binding10 is not None else set()
        self.presentation_Binding = presentation_Binding if presentation_Binding is not None else set()
        self.presentation_Binding13 = presentation_Binding13 if presentation_Binding13 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xPath(self) -> str:
        return self.__xPath

    @xPath.setter
    def xPath(self, xPath: str):
        self.__xPath = xPath

    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def presentation_Binding13(self):
        return self.__presentation_Binding13

    @presentation_Binding13.setter
    def presentation_Binding13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Binding__presentation_Binding13", None)
        self.__presentation_Binding13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_Widget"):
                    opp_val = getattr(item, "presentation_Widget", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_Widget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_Widget"):
                    opp_val = getattr(item, "presentation_Widget", None)
                    
                    setattr(item, "presentation_Widget", self)
                    

    @property
    def presentation_Binding10(self):
        return self.__presentation_Binding10

    @presentation_Binding10.setter
    def presentation_Binding10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Binding__presentation_Binding10", None)
        self.__presentation_Binding10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject11"):
                    opp_val = getattr(item, "presentation_EObject11", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject11"):
                    opp_val = getattr(item, "presentation_EObject11", None)
                    
                    setattr(item, "presentation_EObject11", self)
                    

    @property
    def presentation_Binding(self):
        return self.__presentation_Binding

    @presentation_Binding.setter
    def presentation_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Binding__presentation_Binding", None)
        self.__presentation_Binding = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject8"):
                    opp_val = getattr(item, "presentation_EObject8", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject8"):
                    opp_val = getattr(item, "presentation_EObject8", None)
                    
                    setattr(item, "presentation_EObject8", self)
                    

class presentation_EObject:

    pass
class presentation_Accessible:

    def __init__(self, mixed: str, presentation_Accessible: "presentation_Control" = None):
        self.mixed = mixed
        self.presentation_Accessible = presentation_Accessible
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_Accessible(self):
        return self.__presentation_Accessible

    @presentation_Accessible.setter
    def presentation_Accessible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_Accessible__presentation_Accessible", None)
        self.__presentation_Accessible = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_Control83"):
                opp_val = getattr(old_value, "presentation_Control83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_Control83"):
                opp_val = getattr(value, "presentation_Control83", None)
                if opp_val is None:
                    setattr(value, "presentation_Control83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ColumnViewer:

    pass
class presentation_AbstractTableViewer(ColumnViewer):

    def __init__(self, itemCount: str):
        self.itemCount = itemCount
        
    @property
    def itemCount(self) -> str:
        return self.__itemCount

    @itemCount.setter
    def itemCount(self, itemCount: str):
        self.__itemCount = itemCount

class presentation_TreePath:

    def __init__(self, mixed: str, presentation_TreePath: "presentation_AbstractTreeViewer" = None):
        self.mixed = mixed
        self.presentation_TreePath = presentation_TreePath
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_TreePath(self):
        return self.__presentation_TreePath

    @presentation_TreePath.setter
    def presentation_TreePath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_TreePath__presentation_TreePath", None)
        self.__presentation_TreePath = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_AbstractTreeViewer"):
                opp_val = getattr(old_value, "presentation_AbstractTreeViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_AbstractTreeViewer"):
                opp_val = getattr(value, "presentation_AbstractTreeViewer", None)
                if opp_val is None:
                    setattr(value, "presentation_AbstractTreeViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_AbstractTreeViewer(ColumnViewer):

    def __init__(self, group4: str, autoExpandLevel: str, presentation_AbstractTreeViewer: set["presentation_TreePath"] = None, presentation_AbstractTreeViewer3: set["presentation_EObject"] = None, presentation_AbstractTreeViewer5: set["presentation_EObject"] = None):
        self.group4 = group4
        self.autoExpandLevel = autoExpandLevel
        self.presentation_AbstractTreeViewer = presentation_AbstractTreeViewer if presentation_AbstractTreeViewer is not None else set()
        self.presentation_AbstractTreeViewer3 = presentation_AbstractTreeViewer3 if presentation_AbstractTreeViewer3 is not None else set()
        self.presentation_AbstractTreeViewer5 = presentation_AbstractTreeViewer5 if presentation_AbstractTreeViewer5 is not None else set()
        
    @property
    def autoExpandLevel(self) -> str:
        return self.__autoExpandLevel

    @autoExpandLevel.setter
    def autoExpandLevel(self, autoExpandLevel: str):
        self.__autoExpandLevel = autoExpandLevel

    @property
    def group4(self) -> str:
        return self.__group4

    @group4.setter
    def group4(self, group4: str):
        self.__group4 = group4

    @property
    def presentation_AbstractTreeViewer3(self):
        return self.__presentation_AbstractTreeViewer3

    @presentation_AbstractTreeViewer3.setter
    def presentation_AbstractTreeViewer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AbstractTreeViewer__presentation_AbstractTreeViewer3", None)
        self.__presentation_AbstractTreeViewer3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject"):
                    opp_val = getattr(item, "presentation_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject"):
                    opp_val = getattr(item, "presentation_EObject", None)
                    
                    setattr(item, "presentation_EObject", self)
                    

    @property
    def presentation_AbstractTreeViewer(self):
        return self.__presentation_AbstractTreeViewer

    @presentation_AbstractTreeViewer.setter
    def presentation_AbstractTreeViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AbstractTreeViewer__presentation_AbstractTreeViewer", None)
        self.__presentation_AbstractTreeViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_TreePath"):
                    opp_val = getattr(item, "presentation_TreePath", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_TreePath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_TreePath"):
                    opp_val = getattr(item, "presentation_TreePath", None)
                    
                    setattr(item, "presentation_TreePath", self)
                    

    @property
    def presentation_AbstractTreeViewer5(self):
        return self.__presentation_AbstractTreeViewer5

    @presentation_AbstractTreeViewer5.setter
    def presentation_AbstractTreeViewer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AbstractTreeViewer__presentation_AbstractTreeViewer5", None)
        self.__presentation_AbstractTreeViewer5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject6"):
                    opp_val = getattr(item, "presentation_EObject6", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject6"):
                    opp_val = getattr(item, "presentation_EObject6", None)
                    
                    setattr(item, "presentation_EObject6", self)
                    

class StructuredViewer:

    pass
class presentation_ColumnViewer(StructuredViewer):

    def __init__(self, group3: str, presentation_ColumnViewer: set["presentation_ColumnViewerEditor"] = None, presentation_ColumnViewer49: set["presentation_ICellModifier"] = None, presentation_ColumnViewer51: set["presentation_CellEditor"] = None, presentation_ColumnViewer54: set["presentation_EObject"] = None):
        self.group3 = group3
        self.presentation_ColumnViewer = presentation_ColumnViewer if presentation_ColumnViewer is not None else set()
        self.presentation_ColumnViewer49 = presentation_ColumnViewer49 if presentation_ColumnViewer49 is not None else set()
        self.presentation_ColumnViewer51 = presentation_ColumnViewer51 if presentation_ColumnViewer51 is not None else set()
        self.presentation_ColumnViewer54 = presentation_ColumnViewer54 if presentation_ColumnViewer54 is not None else set()
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def presentation_ColumnViewer49(self):
        return self.__presentation_ColumnViewer49

    @presentation_ColumnViewer49.setter
    def presentation_ColumnViewer49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ColumnViewer__presentation_ColumnViewer49", None)
        self.__presentation_ColumnViewer49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ICellModifier"):
                    opp_val = getattr(item, "presentation_ICellModifier", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ICellModifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ICellModifier"):
                    opp_val = getattr(item, "presentation_ICellModifier", None)
                    
                    setattr(item, "presentation_ICellModifier", self)
                    

    @property
    def presentation_ColumnViewer(self):
        return self.__presentation_ColumnViewer

    @presentation_ColumnViewer.setter
    def presentation_ColumnViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ColumnViewer__presentation_ColumnViewer", None)
        self.__presentation_ColumnViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ColumnViewerEditor"):
                    opp_val = getattr(item, "presentation_ColumnViewerEditor", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ColumnViewerEditor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ColumnViewerEditor"):
                    opp_val = getattr(item, "presentation_ColumnViewerEditor", None)
                    
                    setattr(item, "presentation_ColumnViewerEditor", self)
                    

    @property
    def presentation_ColumnViewer54(self):
        return self.__presentation_ColumnViewer54

    @presentation_ColumnViewer54.setter
    def presentation_ColumnViewer54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ColumnViewer__presentation_ColumnViewer54", None)
        self.__presentation_ColumnViewer54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject55"):
                    opp_val = getattr(item, "presentation_EObject55", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject55"):
                    opp_val = getattr(item, "presentation_EObject55", None)
                    
                    setattr(item, "presentation_EObject55", self)
                    

    @property
    def presentation_ColumnViewer51(self):
        return self.__presentation_ColumnViewer51

    @presentation_ColumnViewer51.setter
    def presentation_ColumnViewer51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ColumnViewer__presentation_ColumnViewer51", None)
        self.__presentation_ColumnViewer51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CellEditor52"):
                    opp_val = getattr(item, "presentation_CellEditor52", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CellEditor52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CellEditor52"):
                    opp_val = getattr(item, "presentation_CellEditor52", None)
                    
                    setattr(item, "presentation_CellEditor52", self)
                    

class presentation_AbstractListViewer(StructuredViewer):

    pass
class presentation_IBindingContext(ABC):

    def __init__(self, mixed: str, presentation_IBindingContext: "presentation_AbstractDataProvider" = None):
        self.mixed = mixed
        self.presentation_IBindingContext = presentation_IBindingContext
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def presentation_IBindingContext(self):
        return self.__presentation_IBindingContext

    @presentation_IBindingContext.setter
    def presentation_IBindingContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_IBindingContext__presentation_IBindingContext", None)
        self.__presentation_IBindingContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_AbstractDataProvider"):
                opp_val = getattr(old_value, "presentation_AbstractDataProvider", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_AbstractDataProvider"):
                opp_val = getattr(value, "presentation_AbstractDataProvider", None)
                if opp_val is None:
                    setattr(value, "presentation_AbstractDataProvider", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_AbstractDataProvider(ABC):

    def __init__(self, group: str, key: str, mixed: str, presentation_AbstractDataProvider: set["presentation_IBindingContext"] = None):
        self.group = group
        self.key = key
        self.mixed = mixed
        self.presentation_AbstractDataProvider = presentation_AbstractDataProvider if presentation_AbstractDataProvider is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def presentation_AbstractDataProvider(self):
        return self.__presentation_AbstractDataProvider

    @presentation_AbstractDataProvider.setter
    def presentation_AbstractDataProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AbstractDataProvider__presentation_AbstractDataProvider", None)
        self.__presentation_AbstractDataProvider = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_IBindingContext"):
                    opp_val = getattr(item, "presentation_IBindingContext", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_IBindingContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_IBindingContext"):
                    opp_val = getattr(item, "presentation_IBindingContext", None)
                    
                    setattr(item, "presentation_IBindingContext", self)
                    

class CellEditor:

    pass
class presentation_DialogCellEditor(CellEditor):

    pass
class presentation_TextCellEditor(CellEditor):

    pass
class presentation_CheckboxCellEditor(CellEditor):

    pass
class presentation_AbstractComboBoxCellEditor(CellEditor):

    def __init__(self, activationStyle: str):
        self.activationStyle = activationStyle
        
    @property
    def activationStyle(self) -> str:
        return self.__activationStyle

    @activationStyle.setter
    def activationStyle(self, activationStyle: str):
        self.__activationStyle = activationStyle
