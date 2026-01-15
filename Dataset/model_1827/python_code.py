from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Animation:

    pass
class book_Fade(Animation):

    def __init__(self, toValue: float, fromValue: float):
        self.toValue = toValue
        self.fromValue = fromValue
        
    @property
    def toValue(self) -> float:
        return self.__toValue

    @toValue.setter
    def toValue(self, toValue: float):
        self.__toValue = toValue

    @property
    def fromValue(self) -> float:
        return self.__fromValue

    @fromValue.setter
    def fromValue(self, fromValue: float):
        self.__fromValue = fromValue

class Action:

    pass
class book_JSAction(Action):

    def __init__(self, javaScript: str):
        self.javaScript = javaScript
        
    @property
    def javaScript(self) -> str:
        return self.__javaScript

    @javaScript.setter
    def javaScript(self, javaScript: str):
        self.__javaScript = javaScript

class book_OpenPage(Action):

    pass
class book_Rotation(Animation):

    def __init__(self, toAngle: float, fromAngle: float):
        self.toAngle = toAngle
        self.fromAngle = fromAngle
        
    @property
    def toAngle(self) -> float:
        return self.__toAngle

    @toAngle.setter
    def toAngle(self, toAngle: float):
        self.__toAngle = toAngle

    @property
    def fromAngle(self) -> float:
        return self.__fromAngle

    @fromAngle.setter
    def fromAngle(self, fromAngle: float):
        self.__fromAngle = fromAngle

class book_Move(Animation):

    def __init__(self, fromLocation: str, toLocation: str):
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        
    @property
    def fromLocation(self) -> str:
        return self.__fromLocation

    @fromLocation.setter
    def fromLocation(self, fromLocation: str):
        self.__fromLocation = fromLocation

    @property
    def toLocation(self) -> str:
        return self.__toLocation

    @toLocation.setter
    def toLocation(self, toLocation: str):
        self.__toLocation = toLocation

class book_Animation(Action):

    def __init__(self, duration: float, delay: float, autoReverse: bool, repeat: int, book_Animation: "book_ImageFlash" = None, book_Animation19: "book_ImageFlash" = None):
        self.duration = duration
        self.delay = delay
        self.autoReverse = autoReverse
        self.repeat = repeat
        self.book_Animation = book_Animation
        self.book_Animation19 = book_Animation19
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    @property
    def autoReverse(self) -> bool:
        return self.__autoReverse

    @autoReverse.setter
    def autoReverse(self, autoReverse: bool):
        self.__autoReverse = autoReverse

    @property
    def delay(self) -> float:
        return self.__delay

    @delay.setter
    def delay(self, delay: float):
        self.__delay = delay

    @property
    def repeat(self) -> int:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: int):
        self.__repeat = repeat

    @property
    def book_Animation19(self):
        return self.__book_Animation19

    @book_Animation19.setter
    def book_Animation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Animation__book_Animation19", None)
        self.__book_Animation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_ImageFlash18"):
                opp_val = getattr(old_value, "book_ImageFlash18", None)
                if opp_val == self:
                    setattr(old_value, "book_ImageFlash18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_ImageFlash18"):
                opp_val = getattr(value, "book_ImageFlash18", None)
                setattr(value, "book_ImageFlash18", self)

    @property
    def book_Animation(self):
        return self.__book_Animation

    @book_Animation.setter
    def book_Animation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Animation__book_Animation", None)
        self.__book_Animation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_ImageFlash"):
                opp_val = getattr(old_value, "book_ImageFlash", None)
                if opp_val == self:
                    setattr(old_value, "book_ImageFlash", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_ImageFlash"):
                opp_val = getattr(value, "book_ImageFlash", None)
                setattr(value, "book_ImageFlash", self)

class Control:

    pass
class book_Media(Control):

    def __init__(self, autoPlay: bool, duration: int, repeat: int, url: str):
        self.autoPlay = autoPlay
        self.duration = duration
        self.repeat = repeat
        self.url = url
        
    @property
    def autoPlay(self) -> bool:
        return self.__autoPlay

    @autoPlay.setter
    def autoPlay(self, autoPlay: bool):
        self.__autoPlay = autoPlay

    @property
    def repeat(self) -> int:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: int):
        self.__repeat = repeat

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class book_ImageFlash(Control):

    def __init__(self, images: str, duration: int, book_ImageFlash: "book_Animation" = None, book_ImageFlash18: "book_Animation" = None):
        self.images = images
        self.duration = duration
        self.book_ImageFlash = book_ImageFlash
        self.book_ImageFlash18 = book_ImageFlash18
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def images(self) -> str:
        return self.__images

    @images.setter
    def images(self, images: str):
        self.__images = images

    @property
    def book_ImageFlash18(self):
        return self.__book_ImageFlash18

    @book_ImageFlash18.setter
    def book_ImageFlash18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_ImageFlash__book_ImageFlash18", None)
        self.__book_ImageFlash18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Animation19"):
                opp_val = getattr(old_value, "book_Animation19", None)
                if opp_val == self:
                    setattr(old_value, "book_Animation19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Animation19"):
                opp_val = getattr(value, "book_Animation19", None)
                setattr(value, "book_Animation19", self)

    @property
    def book_ImageFlash(self):
        return self.__book_ImageFlash

    @book_ImageFlash.setter
    def book_ImageFlash(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_ImageFlash__book_ImageFlash", None)
        self.__book_ImageFlash = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Animation"):
                opp_val = getattr(old_value, "book_Animation", None)
                if opp_val == self:
                    setattr(old_value, "book_Animation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Animation"):
                opp_val = getattr(value, "book_Animation", None)
                setattr(value, "book_Animation", self)

class book_Group(Control):

    pass
class book_Label(Control):

    def __init__(self, text: str, font: str):
        self.text = text
        self.font = font
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

class Node:

    pass
class book_Shape(Node):

    def __init__(self, lineWidth: int, points: str):
        self.lineWidth = lineWidth
        self.points = points
        
    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

class book_Node(ABC):

    def __init__(self, enable: bool, opacity: float, background: str, foreground: str, bounds: str, book_Node: "book_Group" = None):
        self.enable = enable
        self.opacity = opacity
        self.background = background
        self.foreground = foreground
        self.bounds = bounds
        self.book_Node = book_Node
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def enable(self) -> bool:
        return self.__enable

    @enable.setter
    def enable(self, enable: bool):
        self.__enable = enable

    @property
    def opacity(self) -> float:
        return self.__opacity

    @opacity.setter
    def opacity(self, opacity: float):
        self.__opacity = opacity

    @property
    def foreground(self) -> str:
        return self.__foreground

    @foreground.setter
    def foreground(self, foreground: str):
        self.__foreground = foreground

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def book_Node(self):
        return self.__book_Node

    @book_Node.setter
    def book_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Node__book_Node", None)
        self.__book_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Group"):
                opp_val = getattr(old_value, "book_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Group"):
                opp_val = getattr(value, "book_Group", None)
                if opp_val is None:
                    setattr(value, "book_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class book_Control(Node):

    def __init__(self, image: str, sound: str, book_Control11: set["book_Action"] = None, book_Control13: set["book_Action"] = None, book_Control: "book_Layer" = None):
        self.image = image
        self.sound = sound
        self.book_Control11 = book_Control11 if book_Control11 is not None else set()
        self.book_Control13 = book_Control13 if book_Control13 is not None else set()
        self.book_Control = book_Control
        
    @property
    def sound(self) -> str:
        return self.__sound

    @sound.setter
    def sound(self, sound: str):
        self.__sound = sound

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def book_Control(self):
        return self.__book_Control

    @book_Control.setter
    def book_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Control__book_Control", None)
        self.__book_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Layer9"):
                opp_val = getattr(old_value, "book_Layer9", None)
                if opp_val == self:
                    setattr(old_value, "book_Layer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Layer9"):
                opp_val = getattr(value, "book_Layer9", None)
                setattr(value, "book_Layer9", self)

    @property
    def book_Control11(self):
        return self.__book_Control11

    @book_Control11.setter
    def book_Control11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Control__book_Control11", None)
        self.__book_Control11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book_Action"):
                    opp_val = getattr(item, "book_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "book_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book_Action"):
                    opp_val = getattr(item, "book_Action", None)
                    
                    setattr(item, "book_Action", self)
                    

    @property
    def book_Control13(self):
        return self.__book_Control13

    @book_Control13.setter
    def book_Control13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Control__book_Control13", None)
        self.__book_Control13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book_Action14"):
                    opp_val = getattr(item, "book_Action14", None)
                    
                    if opp_val == self:
                        setattr(item, "book_Action14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book_Action14"):
                    opp_val = getattr(item, "book_Action14", None)
                    
                    setattr(item, "book_Action14", self)
                    

class book_Action(ABC):

    pass
class book_Layer:

    def __init__(self, visible: bool, book_Layer: "book_Page" = None, book_Layer9: "book_Control" = None):
        self.visible = visible
        self.book_Layer = book_Layer
        self.book_Layer9 = book_Layer9
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def book_Layer9(self):
        return self.__book_Layer9

    @book_Layer9.setter
    def book_Layer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Layer__book_Layer9", None)
        self.__book_Layer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Control"):
                opp_val = getattr(old_value, "book_Control", None)
                if opp_val == self:
                    setattr(old_value, "book_Control", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Control"):
                opp_val = getattr(value, "book_Control", None)
                setattr(value, "book_Control", self)

    @property
    def book_Layer(self):
        return self.__book_Layer

    @book_Layer.setter
    def book_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Layer__book_Layer", None)
        self.__book_Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Page7"):
                opp_val = getattr(old_value, "book_Page7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Page7"):
                opp_val = getattr(value, "book_Page7", None)
                if opp_val is None:
                    setattr(value, "book_Page7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class book_Page:

    def __init__(self, name: str, book_Page7: set["book_Layer"] = None, book_Page: "book_Book" = None, book_Page5: "book_Book" = None, book_Page21: "book_OpenPage" = None):
        self.name = name
        self.book_Page7 = book_Page7 if book_Page7 is not None else set()
        self.book_Page = book_Page
        self.book_Page5 = book_Page5
        self.book_Page21 = book_Page21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def book_Page21(self):
        return self.__book_Page21

    @book_Page21.setter
    def book_Page21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Page__book_Page21", None)
        self.__book_Page21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_OpenPage"):
                opp_val = getattr(old_value, "book_OpenPage", None)
                if opp_val == self:
                    setattr(old_value, "book_OpenPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_OpenPage"):
                opp_val = getattr(value, "book_OpenPage", None)
                setattr(value, "book_OpenPage", self)

    @property
    def book_Page7(self):
        return self.__book_Page7

    @book_Page7.setter
    def book_Page7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Page__book_Page7", None)
        self.__book_Page7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book_Layer"):
                    opp_val = getattr(item, "book_Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "book_Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book_Layer"):
                    opp_val = getattr(item, "book_Layer", None)
                    
                    setattr(item, "book_Layer", self)
                    

    @property
    def book_Page5(self):
        return self.__book_Page5

    @book_Page5.setter
    def book_Page5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Page__book_Page5", None)
        self.__book_Page5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Book4"):
                opp_val = getattr(old_value, "book_Book4", None)
                if opp_val == self:
                    setattr(old_value, "book_Book4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Book4"):
                opp_val = getattr(value, "book_Book4", None)
                setattr(value, "book_Book4", self)

    @property
    def book_Page(self):
        return self.__book_Page

    @book_Page.setter
    def book_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Page__book_Page", None)
        self.__book_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Book"):
                opp_val = getattr(old_value, "book_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Book"):
                opp_val = getattr(value, "book_Book", None)
                if opp_val is None:
                    setattr(value, "book_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Page:

    pass
class book_Splash(Page):

    def __init__(self, duration: int, book_Splash: "book_Book" = None):
        self.duration = duration
        self.book_Splash = book_Splash
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def book_Splash(self):
        return self.__book_Splash

    @book_Splash.setter
    def book_Splash(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Splash__book_Splash", None)
        self.__book_Splash = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Book2"):
                opp_val = getattr(old_value, "book_Book2", None)
                if opp_val == self:
                    setattr(old_value, "book_Book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Book2"):
                opp_val = getattr(value, "book_Book2", None)
                setattr(value, "book_Book2", self)

class book_Book:

    def __init__(self, title: str, author: str, version: str, description: str, bookId: str, resolution: str, book_Book: set["book_Page"] = None, book_Book2: "book_Splash" = None, book_Book4: "book_Page" = None):
        self.title = title
        self.author = author
        self.version = version
        self.description = description
        self.bookId = bookId
        self.resolution = resolution
        self.book_Book = book_Book if book_Book is not None else set()
        self.book_Book2 = book_Book2
        self.book_Book4 = book_Book4
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        self.__resolution = resolution

    @property
    def bookId(self) -> str:
        return self.__bookId

    @bookId.setter
    def bookId(self, bookId: str):
        self.__bookId = bookId

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def book_Book(self):
        return self.__book_Book

    @book_Book.setter
    def book_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book_Book", None)
        self.__book_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book_Page"):
                    opp_val = getattr(item, "book_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "book_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book_Page"):
                    opp_val = getattr(item, "book_Page", None)
                    
                    setattr(item, "book_Page", self)
                    

    @property
    def book_Book2(self):
        return self.__book_Book2

    @book_Book2.setter
    def book_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book_Book2", None)
        self.__book_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Splash"):
                opp_val = getattr(old_value, "book_Splash", None)
                if opp_val == self:
                    setattr(old_value, "book_Splash", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Splash"):
                opp_val = getattr(value, "book_Splash", None)
                setattr(value, "book_Splash", self)

    @property
    def book_Book4(self):
        return self.__book_Book4

    @book_Book4.setter
    def book_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book_Book4", None)
        self.__book_Book4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_Page5"):
                opp_val = getattr(old_value, "book_Page5", None)
                if opp_val == self:
                    setattr(old_value, "book_Page5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_Page5"):
                opp_val = getattr(value, "book_Page5", None)
                setattr(value, "book_Page5", self)
