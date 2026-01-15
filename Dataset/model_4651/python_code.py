from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class di_Color:

    pass
class di_Fill:

    pass
class di_Bounds:

    pass
class Shape:

    pass
class di_Diagram(Shape):

    def __init__(self, name: str, documentation: str, resolution: str):
        self.name = name
        self.documentation = documentation
        self.resolution = resolution
        
    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        self.__resolution = resolution

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class di_Point:

    pass
class di_DiagramElement(ABC):

    def __init__(self, id: str, di_DiagramElement: "di_Style" = None, di_DiagramElement7: "di_Style" = None, di_DiagramElement10: set["di_EObject"] = None, di_DiagramElement12: "di_Edge" = None, DiagramElement: "di_DiagramElement" = None, ownedElement: "di_DiagramElement" = None, DiagramElement4: "di_DiagramElement" = None, owningElement: set["di_DiagramElement"] = None, di_DiagramElement15: "di_Edge" = None):
        self.id = id
        self.di_DiagramElement = di_DiagramElement
        self.di_DiagramElement7 = di_DiagramElement7
        self.di_DiagramElement10 = di_DiagramElement10 if di_DiagramElement10 is not None else set()
        self.di_DiagramElement12 = di_DiagramElement12
        self.DiagramElement = DiagramElement
        self.ownedElement = ownedElement
        self.DiagramElement4 = DiagramElement4
        self.owningElement = owningElement if owningElement is not None else set()
        self.di_DiagramElement15 = di_DiagramElement15
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramElement"):
                opp_val = getattr(old_value, "DiagramElement", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElement"):
                opp_val = getattr(value, "DiagramElement", None)
                setattr(value, "DiagramElement", self)

    @property
    def di_DiagramElement7(self):
        return self.__di_DiagramElement7

    @di_DiagramElement7.setter
    def di_DiagramElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement7", None)
        self.__di_DiagramElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Style8"):
                opp_val = getattr(old_value, "di_Style8", None)
                if opp_val == self:
                    setattr(old_value, "di_Style8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Style8"):
                opp_val = getattr(value, "di_Style8", None)
                setattr(value, "di_Style8", self)

    @property
    def DiagramElement(self):
        return self.__DiagramElement

    @DiagramElement.setter
    def DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__DiagramElement", None)
        self.__DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElement"):
                opp_val = getattr(old_value, "ownedElement", None)
                if opp_val == self:
                    setattr(old_value, "ownedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElement"):
                opp_val = getattr(value, "ownedElement", None)
                setattr(value, "ownedElement", self)

    @property
    def di_DiagramElement(self):
        return self.__di_DiagramElement

    @di_DiagramElement.setter
    def di_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement", None)
        self.__di_DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Style"):
                opp_val = getattr(old_value, "di_Style", None)
                if opp_val == self:
                    setattr(old_value, "di_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Style"):
                opp_val = getattr(value, "di_Style", None)
                setattr(value, "di_Style", self)

    @property
    def di_DiagramElement12(self):
        return self.__di_DiagramElement12

    @di_DiagramElement12.setter
    def di_DiagramElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement12", None)
        self.__di_DiagramElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Edge"):
                opp_val = getattr(old_value, "di_Edge", None)
                if opp_val == self:
                    setattr(old_value, "di_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Edge"):
                opp_val = getattr(value, "di_Edge", None)
                setattr(value, "di_Edge", self)

    @property
    def di_DiagramElement15(self):
        return self.__di_DiagramElement15

    @di_DiagramElement15.setter
    def di_DiagramElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement15", None)
        self.__di_DiagramElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Edge14"):
                opp_val = getattr(old_value, "di_Edge14", None)
                if opp_val == self:
                    setattr(old_value, "di_Edge14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Edge14"):
                opp_val = getattr(value, "di_Edge14", None)
                setattr(value, "di_Edge14", self)

    @property
    def owningElement(self):
        return self.__owningElement

    @owningElement.setter
    def owningElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__owningElement", None)
        self.__owningElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElement4"):
                    opp_val = getattr(item, "DiagramElement4", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElement4"):
                    opp_val = getattr(item, "DiagramElement4", None)
                    
                    setattr(item, "DiagramElement4", self)
                    

    @property
    def di_DiagramElement10(self):
        return self.__di_DiagramElement10

    @di_DiagramElement10.setter
    def di_DiagramElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement10", None)
        self.__di_DiagramElement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EObject"):
                    opp_val = getattr(item, "di_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EObject"):
                    opp_val = getattr(item, "di_EObject", None)
                    
                    setattr(item, "di_EObject", self)
                    

    @property
    def DiagramElement4(self):
        return self.__DiagramElement4

    @DiagramElement4.setter
    def DiagramElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__DiagramElement4", None)
        self.__DiagramElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningElement"):
                opp_val = getattr(old_value, "owningElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningElement"):
                opp_val = getattr(value, "owningElement", None)
                if opp_val is None:
                    setattr(value, "owningElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DiagramElement:

    pass
class di_Shape(DiagramElement):

    pass
class di_Edge(DiagramElement):

    pass
class di_EObject:

    pass
class di_Style(ABC):

    def __init__(self, fontItalic: str, fontBold: str, fontUnderline: str, fontStrikeThrough: str, fillOpacity: str, strokeWidth: str, strokeOpacity: str, strokeDashLength: str, fontSize: str, fontName: str, di_Style: "di_DiagramElement" = None, di_Style8: "di_DiagramElement" = None, di_Style20: "di_Fill" = None, di_Style22: "di_Color" = None, di_Style24: "di_Color" = None, di_Style27: "di_Color" = None):
        self.fontItalic = fontItalic
        self.fontBold = fontBold
        self.fontUnderline = fontUnderline
        self.fontStrikeThrough = fontStrikeThrough
        self.fillOpacity = fillOpacity
        self.strokeWidth = strokeWidth
        self.strokeOpacity = strokeOpacity
        self.strokeDashLength = strokeDashLength
        self.fontSize = fontSize
        self.fontName = fontName
        self.di_Style = di_Style
        self.di_Style8 = di_Style8
        self.di_Style20 = di_Style20
        self.di_Style22 = di_Style22
        self.di_Style24 = di_Style24
        self.di_Style27 = di_Style27
        
    @property
    def fontStrikeThrough(self) -> str:
        return self.__fontStrikeThrough

    @fontStrikeThrough.setter
    def fontStrikeThrough(self, fontStrikeThrough: str):
        self.__fontStrikeThrough = fontStrikeThrough

    @property
    def fillOpacity(self) -> str:
        return self.__fillOpacity

    @fillOpacity.setter
    def fillOpacity(self, fillOpacity: str):
        self.__fillOpacity = fillOpacity

    @property
    def strokeWidth(self) -> str:
        return self.__strokeWidth

    @strokeWidth.setter
    def strokeWidth(self, strokeWidth: str):
        self.__strokeWidth = strokeWidth

    @property
    def fontUnderline(self) -> str:
        return self.__fontUnderline

    @fontUnderline.setter
    def fontUnderline(self, fontUnderline: str):
        self.__fontUnderline = fontUnderline

    @property
    def fontSize(self) -> str:
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: str):
        self.__fontSize = fontSize

    @property
    def fontBold(self) -> str:
        return self.__fontBold

    @fontBold.setter
    def fontBold(self, fontBold: str):
        self.__fontBold = fontBold

    @property
    def fontItalic(self) -> str:
        return self.__fontItalic

    @fontItalic.setter
    def fontItalic(self, fontItalic: str):
        self.__fontItalic = fontItalic

    @property
    def strokeOpacity(self) -> str:
        return self.__strokeOpacity

    @strokeOpacity.setter
    def strokeOpacity(self, strokeOpacity: str):
        self.__strokeOpacity = strokeOpacity

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def strokeDashLength(self) -> str:
        return self.__strokeDashLength

    @strokeDashLength.setter
    def strokeDashLength(self, strokeDashLength: str):
        self.__strokeDashLength = strokeDashLength

    @property
    def di_Style27(self):
        return self.__di_Style27

    @di_Style27.setter
    def di_Style27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style27", None)
        self.__di_Style27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Color28"):
                opp_val = getattr(old_value, "di_Color28", None)
                if opp_val == self:
                    setattr(old_value, "di_Color28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Color28"):
                opp_val = getattr(value, "di_Color28", None)
                setattr(value, "di_Color28", self)

    @property
    def di_Style24(self):
        return self.__di_Style24

    @di_Style24.setter
    def di_Style24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style24", None)
        self.__di_Style24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Color25"):
                opp_val = getattr(old_value, "di_Color25", None)
                if opp_val == self:
                    setattr(old_value, "di_Color25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Color25"):
                opp_val = getattr(value, "di_Color25", None)
                setattr(value, "di_Color25", self)

    @property
    def di_Style20(self):
        return self.__di_Style20

    @di_Style20.setter
    def di_Style20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style20", None)
        self.__di_Style20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Fill"):
                opp_val = getattr(old_value, "di_Fill", None)
                if opp_val == self:
                    setattr(old_value, "di_Fill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Fill"):
                opp_val = getattr(value, "di_Fill", None)
                setattr(value, "di_Fill", self)

    @property
    def di_Style8(self):
        return self.__di_Style8

    @di_Style8.setter
    def di_Style8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style8", None)
        self.__di_Style8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DiagramElement7"):
                opp_val = getattr(old_value, "di_DiagramElement7", None)
                if opp_val == self:
                    setattr(old_value, "di_DiagramElement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DiagramElement7"):
                opp_val = getattr(value, "di_DiagramElement7", None)
                setattr(value, "di_DiagramElement7", self)

    @property
    def di_Style(self):
        return self.__di_Style

    @di_Style.setter
    def di_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style", None)
        self.__di_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DiagramElement"):
                opp_val = getattr(old_value, "di_DiagramElement", None)
                if opp_val == self:
                    setattr(old_value, "di_DiagramElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DiagramElement"):
                opp_val = getattr(value, "di_DiagramElement", None)
                setattr(value, "di_DiagramElement", self)

    @property
    def di_Style22(self):
        return self.__di_Style22

    @di_Style22.setter
    def di_Style22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style22", None)
        self.__di_Style22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Color"):
                opp_val = getattr(old_value, "di_Color", None)
                if opp_val == self:
                    setattr(old_value, "di_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Color"):
                opp_val = getattr(value, "di_Color", None)
                setattr(value, "di_Color", self)

    def valid_font_size(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement valid_font_size method
        pass

    def valid_dash_length_size(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement valid_dash_length_size method
        pass

    def valid_fill_opacity(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement valid_fill_opacity method
        pass

    def valid_stroke_width(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement valid_stroke_width method
        pass

    def valid_stroke_opacity(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement valid_stroke_opacity method
        pass
