from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PresetClassType(Enum):
    custom = "custom"
    entrance = "entrance"
    exit = "exit"
    emphasis = "emphasis"
    motionPath = "motionPath"
    oleAction = "oleAction"
    mediaCall = "mediaCall"
class VisibilityType(Enum):
    visible = "visible"
    hidden = "hidden"
class NodeTypeType(Enum):
    timingRoot = "timingRoot"
    mainSequence = "mainSequence"
    interactiveSequence = "interactiveSequence"
    default = "default"
    onClick = "onClick"
    withPrevious = "withPrevious"
    afterPrevious = "afterPrevious"
class ActionType(Enum):
    previousPage = "previousPage"
    nextPage = "nextPage"
    firstPage = "firstPage"
    lastPage = "lastPage"
    hide = "hide"
    stop = "stop"
    execute = "execute"
    show = "show"
    verb = "verb"
    fadeOut = "fadeOut"
    sound = "sound"
    none = "none"
class TransitionTypeType(Enum):
    semiAutomatic = "semiAutomatic"
    manual = "manual"
    automatic = "automatic"
class SourceType(Enum):
    fixed = "fixed"
    currentDate = "currentDate"
class AnimationsType(Enum):
    enabled = "enabled"
    disabled = "disabled"
class TransitionStyleType(Enum):
    none = "none"
    fadeFromLeft = "fadeFromLeft"
    fadeFromTop = "fadeFromTop"
    fadeFromRight = "fadeFromRight"
    fadeFromBottom = "fadeFromBottom"
    fadeFromUpperleft = "fadeFromUpperleft"
    fadeFromCenter = "fadeFromCenter"
    verticalStripes = "verticalStripes"
    horizontalStripes = "horizontalStripes"
    clockwise = "clockwise"
    counterclockwise = "counterclockwise"
    openVertical = "openVertical"
    openHorizontal = "openHorizontal"
    closeVertical = "closeVertical"
    closeHorizontal = "closeHorizontal"
    wavylineFromLeft = "wavylineFromLeft"
    wavylineFromTop = "wavylineFromTop"
    wavylineFromRight = "wavylineFromRight"
    wavylineFromBottom = "wavylineFromBottom"
    spiralinLeft = "spiralinLeft"
    spiralinRight = "spiralinRight"
    spiraloutLeft = "spiraloutLeft"
    spiraloutRight = "spiraloutRight"
    rollFromTop = "rollFromTop"
    rollFromLeft = "rollFromLeft"
    rollFromRight = "rollFromRight"
    rollFromBottom = "rollFromBottom"
    stretchFromLeft = "stretchFromLeft"
    stretchFromTop = "stretchFromTop"
    stretchFromRight = "stretchFromRight"
    stretchFromBottom = "stretchFromBottom"
    verticalLines = "verticalLines"
    horizontalLines = "horizontalLines"
    dissolve = "dissolve"
    random = "random"
    verticalCheckerboard = "verticalCheckerboard"
    fadeFromUpperright = "fadeFromUpperright"
    fadeFromLowerleft = "fadeFromLowerleft"
    fadeFromLowerright = "fadeFromLowerright"
    moveFromLeft = "moveFromLeft"
    moveFromTop = "moveFromTop"
    moveFromRight = "moveFromRight"
    moveFromBottom = "moveFromBottom"
    moveFromUpperleft = "moveFromUpperleft"
    moveFromUpperright = "moveFromUpperright"
    moveFromLowerleft = "moveFromLowerleft"
    moveFromLowerright = "moveFromLowerright"
    uncoverToLeft = "uncoverToLeft"
    uncoverToTop = "uncoverToTop"
    uncoverToRight = "uncoverToRight"
    uncoverToBottom = "uncoverToBottom"
    uncoverToUpperleft = "uncoverToUpperleft"
    uncoverToUpperright = "uncoverToUpperright"
    uncoverToLowerleft = "uncoverToLowerleft"
    uncoverToLowerright = "uncoverToLowerright"
    fadeToCenter = "fadeToCenter"
    horizontalCheckerboard = "horizontalCheckerboard"
    interlockingHorizontalLeft = "interlockingHorizontalLeft"
    interlockingHorizontalRight = "interlockingHorizontalRight"
    interlockingVerticalTop = "interlockingVerticalTop"
    interlockingVerticalBottom = "interlockingVerticalBottom"
    flyAway = "flyAway"
    open = "open"
    close = "close"
    melt = "melt"
class TransitionOnClickType(Enum):
    enabled = "enabled"
    disabled = "disabled"


############################################
# Definition of Classes
############################################

class presentation_EStringToStringMapEntry:

    pass
class presentation_DocumentRoot:

    def __init__(self, mixed: str, action: str, animations1: str, backgroundVisible: str, class_: str, classNames: str, delay: str, direction: str, displayDateTime: str, displayFooter: str, displayHeader: str, displayPageNumber: str, duration: str, effect: str, backgroundObjectsVisible: str, pathId: str, endless: str, pause: str, forceManual: str, placeholder1: str, fullScreen: str, groupId: str, masterElement: str, mouseAsPen: str, mouseVisible: str, name: str, nodeType: str, pages: str, source: str, speed: str, playFull: str, startPage: str, presentationPageLayoutName: str, presetClass: str, startScale: str, presetId: str, presetSubType: str, show1: str, showEndOfPresentationSlide: str, showLogo: str, styleName: str, transitionOnClick: str, transitionSpeed: str, transitionStyle: str, transitionType: str, useDateTimeName: str, startWithNavigator: str, stayOnTop: str, useFooterName: str, userTransformed: str, verb: str, visibility: str, useHeaderName: str, presentation_DocumentRoot: set["presentation_EStringToStringMapEntry"] = None, presentation_DocumentRoot55: set["presentation_EStringToStringMapEntry"] = None, presentation_DocumentRoot58: set["presentation_AnimationGroupType"] = None, presentation_DocumentRoot61: set["presentation_AnimationsType1"] = None, presentation_DocumentRoot64: set["presentation_DateTimeType"] = None, presentation_DocumentRoot66: set["presentation_DateTimeDeclType"] = None, presentation_DocumentRoot68: set["presentation_DimType"] = None, presentation_DocumentRoot71: set["presentation_EventListenerType"] = None, presentation_DocumentRoot74: set["presentation_FooterType"] = None, presentation_DocumentRoot78: set["presentation_HeaderType"] = None, presentation_DocumentRoot80: set["presentation_HeaderDeclType"] = None, presentation_DocumentRoot82: set["presentation_HideShapeType"] = None, presentation_DocumentRoot85: set["presentation_HideTextType"] = None, presentation_DocumentRoot88: set["presentation_NotesType"] = None, presentation_DocumentRoot91: set["presentation_PlaceholderType"] = None, presentation_DocumentRoot76: set["presentation_FooterDeclType"] = None, presentation_DocumentRoot95: set["presentation_SettingsType"] = None, presentation_DocumentRoot98: set["presentation_ShowType"] = None, presentation_DocumentRoot101: set["presentation_ShowShapeType"] = None, presentation_DocumentRoot104: set["presentation_ShowTextType"] = None, presentation_DocumentRoot107: set["presentation_SoundType"] = None, presentation_DocumentRoot93: set["presentation_PlayType"] = None):
        self.mixed = mixed
        self.action = action
        self.animations1 = animations1
        self.backgroundVisible = backgroundVisible
        self.class_ = class_
        self.classNames = classNames
        self.delay = delay
        self.direction = direction
        self.displayDateTime = displayDateTime
        self.displayFooter = displayFooter
        self.displayHeader = displayHeader
        self.displayPageNumber = displayPageNumber
        self.duration = duration
        self.effect = effect
        self.backgroundObjectsVisible = backgroundObjectsVisible
        self.pathId = pathId
        self.endless = endless
        self.pause = pause
        self.forceManual = forceManual
        self.placeholder1 = placeholder1
        self.fullScreen = fullScreen
        self.groupId = groupId
        self.masterElement = masterElement
        self.mouseAsPen = mouseAsPen
        self.mouseVisible = mouseVisible
        self.name = name
        self.nodeType = nodeType
        self.pages = pages
        self.source = source
        self.speed = speed
        self.playFull = playFull
        self.startPage = startPage
        self.presentationPageLayoutName = presentationPageLayoutName
        self.presetClass = presetClass
        self.startScale = startScale
        self.presetId = presetId
        self.presetSubType = presetSubType
        self.show1 = show1
        self.showEndOfPresentationSlide = showEndOfPresentationSlide
        self.showLogo = showLogo
        self.styleName = styleName
        self.transitionOnClick = transitionOnClick
        self.transitionSpeed = transitionSpeed
        self.transitionStyle = transitionStyle
        self.transitionType = transitionType
        self.useDateTimeName = useDateTimeName
        self.startWithNavigator = startWithNavigator
        self.stayOnTop = stayOnTop
        self.useFooterName = useFooterName
        self.userTransformed = userTransformed
        self.verb = verb
        self.visibility = visibility
        self.useHeaderName = useHeaderName
        self.presentation_DocumentRoot = presentation_DocumentRoot if presentation_DocumentRoot is not None else set()
        self.presentation_DocumentRoot55 = presentation_DocumentRoot55 if presentation_DocumentRoot55 is not None else set()
        self.presentation_DocumentRoot58 = presentation_DocumentRoot58 if presentation_DocumentRoot58 is not None else set()
        self.presentation_DocumentRoot61 = presentation_DocumentRoot61 if presentation_DocumentRoot61 is not None else set()
        self.presentation_DocumentRoot64 = presentation_DocumentRoot64 if presentation_DocumentRoot64 is not None else set()
        self.presentation_DocumentRoot66 = presentation_DocumentRoot66 if presentation_DocumentRoot66 is not None else set()
        self.presentation_DocumentRoot68 = presentation_DocumentRoot68 if presentation_DocumentRoot68 is not None else set()
        self.presentation_DocumentRoot71 = presentation_DocumentRoot71 if presentation_DocumentRoot71 is not None else set()
        self.presentation_DocumentRoot74 = presentation_DocumentRoot74 if presentation_DocumentRoot74 is not None else set()
        self.presentation_DocumentRoot78 = presentation_DocumentRoot78 if presentation_DocumentRoot78 is not None else set()
        self.presentation_DocumentRoot80 = presentation_DocumentRoot80 if presentation_DocumentRoot80 is not None else set()
        self.presentation_DocumentRoot82 = presentation_DocumentRoot82 if presentation_DocumentRoot82 is not None else set()
        self.presentation_DocumentRoot85 = presentation_DocumentRoot85 if presentation_DocumentRoot85 is not None else set()
        self.presentation_DocumentRoot88 = presentation_DocumentRoot88 if presentation_DocumentRoot88 is not None else set()
        self.presentation_DocumentRoot91 = presentation_DocumentRoot91 if presentation_DocumentRoot91 is not None else set()
        self.presentation_DocumentRoot76 = presentation_DocumentRoot76 if presentation_DocumentRoot76 is not None else set()
        self.presentation_DocumentRoot95 = presentation_DocumentRoot95 if presentation_DocumentRoot95 is not None else set()
        self.presentation_DocumentRoot98 = presentation_DocumentRoot98 if presentation_DocumentRoot98 is not None else set()
        self.presentation_DocumentRoot101 = presentation_DocumentRoot101 if presentation_DocumentRoot101 is not None else set()
        self.presentation_DocumentRoot104 = presentation_DocumentRoot104 if presentation_DocumentRoot104 is not None else set()
        self.presentation_DocumentRoot107 = presentation_DocumentRoot107 if presentation_DocumentRoot107 is not None else set()
        self.presentation_DocumentRoot93 = presentation_DocumentRoot93 if presentation_DocumentRoot93 is not None else set()
        
        pass
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def startScale(self):
        return self.__startScale

    @startScale.setter
    def startScale(self, startScale: str):
        self.__startScale = startScale


    @property
    def placeholder1(self):
        return self.__placeholder1

    @placeholder1.setter
    def placeholder1(self, placeholder1: str):
        self.__placeholder1 = placeholder1


    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, pause: str):
        self.__pause = pause


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def endless(self):
        return self.__endless

    @endless.setter
    def endless(self, endless: str):
        self.__endless = endless


    @property
    def presetSubType(self):
        return self.__presetSubType

    @presetSubType.setter
    def presetSubType(self, presetSubType: str):
        self.__presetSubType = presetSubType


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def userTransformed(self):
        return self.__userTransformed

    @userTransformed.setter
    def userTransformed(self, userTransformed: str):
        self.__userTransformed = userTransformed


    @property
    def nodeType(self):
        return self.__nodeType

    @nodeType.setter
    def nodeType(self, nodeType: str):
        self.__nodeType = nodeType


    @property
    def startPage(self):
        return self.__startPage

    @startPage.setter
    def startPage(self, startPage: str):
        self.__startPage = startPage


    @property
    def displayDateTime(self):
        return self.__displayDateTime

    @displayDateTime.setter
    def displayDateTime(self, displayDateTime: str):
        self.__displayDateTime = displayDateTime


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def forceManual(self):
        return self.__forceManual

    @forceManual.setter
    def forceManual(self, forceManual: str):
        self.__forceManual = forceManual


    @property
    def styleName(self):
        return self.__styleName

    @styleName.setter
    def styleName(self, styleName: str):
        self.__styleName = styleName


    @property
    def stayOnTop(self):
        return self.__stayOnTop

    @stayOnTop.setter
    def stayOnTop(self, stayOnTop: str):
        self.__stayOnTop = stayOnTop


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def presetClass(self):
        return self.__presetClass

    @presetClass.setter
    def presetClass(self, presetClass: str):
        self.__presetClass = presetClass


    @property
    def backgroundVisible(self):
        return self.__backgroundVisible

    @backgroundVisible.setter
    def backgroundVisible(self, backgroundVisible: str):
        self.__backgroundVisible = backgroundVisible


    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay


    @property
    def fullScreen(self):
        return self.__fullScreen

    @fullScreen.setter
    def fullScreen(self, fullScreen: str):
        self.__fullScreen = fullScreen


    @property
    def mouseVisible(self):
        return self.__mouseVisible

    @mouseVisible.setter
    def mouseVisible(self, mouseVisible: str):
        self.__mouseVisible = mouseVisible


    @property
    def animations1(self):
        return self.__animations1

    @animations1.setter
    def animations1(self, animations1: str):
        self.__animations1 = animations1


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def useHeaderName(self):
        return self.__useHeaderName

    @useHeaderName.setter
    def useHeaderName(self, useHeaderName: str):
        self.__useHeaderName = useHeaderName


    @property
    def masterElement(self):
        return self.__masterElement

    @masterElement.setter
    def masterElement(self, masterElement: str):
        self.__masterElement = masterElement


    @property
    def showLogo(self):
        return self.__showLogo

    @showLogo.setter
    def showLogo(self, showLogo: str):
        self.__showLogo = showLogo


    @property
    def transitionOnClick(self):
        return self.__transitionOnClick

    @transitionOnClick.setter
    def transitionOnClick(self, transitionOnClick: str):
        self.__transitionOnClick = transitionOnClick


    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def displayPageNumber(self):
        return self.__displayPageNumber

    @displayPageNumber.setter
    def displayPageNumber(self, displayPageNumber: str):
        self.__displayPageNumber = displayPageNumber


    @property
    def useFooterName(self):
        return self.__useFooterName

    @useFooterName.setter
    def useFooterName(self, useFooterName: str):
        self.__useFooterName = useFooterName


    @property
    def displayHeader(self):
        return self.__displayHeader

    @displayHeader.setter
    def displayHeader(self, displayHeader: str):
        self.__displayHeader = displayHeader


    @property
    def show1(self):
        return self.__show1

    @show1.setter
    def show1(self, show1: str):
        self.__show1 = show1


    @property
    def verb(self):
        return self.__verb

    @verb.setter
    def verb(self, verb: str):
        self.__verb = verb


    @property
    def groupId(self):
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId


    @property
    def presetId(self):
        return self.__presetId

    @presetId.setter
    def presetId(self, presetId: str):
        self.__presetId = presetId


    @property
    def useDateTimeName(self):
        return self.__useDateTimeName

    @useDateTimeName.setter
    def useDateTimeName(self, useDateTimeName: str):
        self.__useDateTimeName = useDateTimeName


    @property
    def pathId(self):
        return self.__pathId

    @pathId.setter
    def pathId(self, pathId: str):
        self.__pathId = pathId


    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration


    @property
    def mouseAsPen(self):
        return self.__mouseAsPen

    @mouseAsPen.setter
    def mouseAsPen(self, mouseAsPen: str):
        self.__mouseAsPen = mouseAsPen


    @property
    def transitionStyle(self):
        return self.__transitionStyle

    @transitionStyle.setter
    def transitionStyle(self, transitionStyle: str):
        self.__transitionStyle = transitionStyle


    @property
    def transitionType(self):
        return self.__transitionType

    @transitionType.setter
    def transitionType(self, transitionType: str):
        self.__transitionType = transitionType


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def showEndOfPresentationSlide(self):
        return self.__showEndOfPresentationSlide

    @showEndOfPresentationSlide.setter
    def showEndOfPresentationSlide(self, showEndOfPresentationSlide: str):
        self.__showEndOfPresentationSlide = showEndOfPresentationSlide


    @property
    def transitionSpeed(self):
        return self.__transitionSpeed

    @transitionSpeed.setter
    def transitionSpeed(self, transitionSpeed: str):
        self.__transitionSpeed = transitionSpeed


    @property
    def playFull(self):
        return self.__playFull

    @playFull.setter
    def playFull(self, playFull: str):
        self.__playFull = playFull


    @property
    def backgroundObjectsVisible(self):
        return self.__backgroundObjectsVisible

    @backgroundObjectsVisible.setter
    def backgroundObjectsVisible(self, backgroundObjectsVisible: str):
        self.__backgroundObjectsVisible = backgroundObjectsVisible


    @property
    def displayFooter(self):
        return self.__displayFooter

    @displayFooter.setter
    def displayFooter(self, displayFooter: str):
        self.__displayFooter = displayFooter


    @property
    def classNames(self):
        return self.__classNames

    @classNames.setter
    def classNames(self, classNames: str):
        self.__classNames = classNames


    @property
    def startWithNavigator(self):
        return self.__startWithNavigator

    @startWithNavigator.setter
    def startWithNavigator(self, startWithNavigator: str):
        self.__startWithNavigator = startWithNavigator


    @property
    def presentationPageLayoutName(self):
        return self.__presentationPageLayoutName

    @presentationPageLayoutName.setter
    def presentationPageLayoutName(self, presentationPageLayoutName: str):
        self.__presentationPageLayoutName = presentationPageLayoutName


    @property
    def presentation_DocumentRoot61(self):
        return self.__presentation_DocumentRoot61

    @presentation_DocumentRoot61.setter
    def presentation_DocumentRoot61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot61", None)
        self.__presentation_DocumentRoot61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_AnimationsType162"):
                    opp_val = getattr(item, "presentation_AnimationsType162", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_AnimationsType162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_AnimationsType162"):
                    opp_val = getattr(item, "presentation_AnimationsType162", None)
                    
                    setattr(item, "presentation_AnimationsType162", self)
                    

    @property
    def presentation_DocumentRoot82(self):
        return self.__presentation_DocumentRoot82

    @presentation_DocumentRoot82.setter
    def presentation_DocumentRoot82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot82", None)
        self.__presentation_DocumentRoot82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_HideShapeType83"):
                    opp_val = getattr(item, "presentation_HideShapeType83", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_HideShapeType83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_HideShapeType83"):
                    opp_val = getattr(item, "presentation_HideShapeType83", None)
                    
                    setattr(item, "presentation_HideShapeType83", self)
                    

    @property
    def presentation_DocumentRoot74(self):
        return self.__presentation_DocumentRoot74

    @presentation_DocumentRoot74.setter
    def presentation_DocumentRoot74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot74", None)
        self.__presentation_DocumentRoot74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FooterType"):
                    opp_val = getattr(item, "presentation_FooterType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FooterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FooterType"):
                    opp_val = getattr(item, "presentation_FooterType", None)
                    
                    setattr(item, "presentation_FooterType", self)
                    

    @property
    def presentation_DocumentRoot95(self):
        return self.__presentation_DocumentRoot95

    @presentation_DocumentRoot95.setter
    def presentation_DocumentRoot95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot95", None)
        self.__presentation_DocumentRoot95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_SettingsType96"):
                    opp_val = getattr(item, "presentation_SettingsType96", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_SettingsType96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_SettingsType96"):
                    opp_val = getattr(item, "presentation_SettingsType96", None)
                    
                    setattr(item, "presentation_SettingsType96", self)
                    

    @property
    def presentation_DocumentRoot78(self):
        return self.__presentation_DocumentRoot78

    @presentation_DocumentRoot78.setter
    def presentation_DocumentRoot78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot78", None)
        self.__presentation_DocumentRoot78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_HeaderType"):
                    opp_val = getattr(item, "presentation_HeaderType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_HeaderType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_HeaderType"):
                    opp_val = getattr(item, "presentation_HeaderType", None)
                    
                    setattr(item, "presentation_HeaderType", self)
                    

    @property
    def presentation_DocumentRoot98(self):
        return self.__presentation_DocumentRoot98

    @presentation_DocumentRoot98.setter
    def presentation_DocumentRoot98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot98", None)
        self.__presentation_DocumentRoot98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ShowType99"):
                    opp_val = getattr(item, "presentation_ShowType99", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ShowType99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ShowType99"):
                    opp_val = getattr(item, "presentation_ShowType99", None)
                    
                    setattr(item, "presentation_ShowType99", self)
                    

    @property
    def presentation_DocumentRoot91(self):
        return self.__presentation_DocumentRoot91

    @presentation_DocumentRoot91.setter
    def presentation_DocumentRoot91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot91", None)
        self.__presentation_DocumentRoot91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_PlaceholderType"):
                    opp_val = getattr(item, "presentation_PlaceholderType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_PlaceholderType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_PlaceholderType"):
                    opp_val = getattr(item, "presentation_PlaceholderType", None)
                    
                    setattr(item, "presentation_PlaceholderType", self)
                    

    @property
    def presentation_DocumentRoot55(self):
        return self.__presentation_DocumentRoot55

    @presentation_DocumentRoot55.setter
    def presentation_DocumentRoot55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot55", None)
        self.__presentation_DocumentRoot55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EStringToStringMapEntry56"):
                    opp_val = getattr(item, "presentation_EStringToStringMapEntry56", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EStringToStringMapEntry56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EStringToStringMapEntry56"):
                    opp_val = getattr(item, "presentation_EStringToStringMapEntry56", None)
                    
                    setattr(item, "presentation_EStringToStringMapEntry56", self)
                    

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
    def presentation_DocumentRoot66(self):
        return self.__presentation_DocumentRoot66

    @presentation_DocumentRoot66.setter
    def presentation_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot66", None)
        self.__presentation_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_DateTimeDeclType"):
                    opp_val = getattr(item, "presentation_DateTimeDeclType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_DateTimeDeclType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_DateTimeDeclType"):
                    opp_val = getattr(item, "presentation_DateTimeDeclType", None)
                    
                    setattr(item, "presentation_DateTimeDeclType", self)
                    

    @property
    def presentation_DocumentRoot107(self):
        return self.__presentation_DocumentRoot107

    @presentation_DocumentRoot107.setter
    def presentation_DocumentRoot107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot107", None)
        self.__presentation_DocumentRoot107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_SoundType108"):
                    opp_val = getattr(item, "presentation_SoundType108", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_SoundType108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_SoundType108"):
                    opp_val = getattr(item, "presentation_SoundType108", None)
                    
                    setattr(item, "presentation_SoundType108", self)
                    

    @property
    def presentation_DocumentRoot93(self):
        return self.__presentation_DocumentRoot93

    @presentation_DocumentRoot93.setter
    def presentation_DocumentRoot93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot93", None)
        self.__presentation_DocumentRoot93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_PlayType"):
                    opp_val = getattr(item, "presentation_PlayType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_PlayType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_PlayType"):
                    opp_val = getattr(item, "presentation_PlayType", None)
                    
                    setattr(item, "presentation_PlayType", self)
                    

    @property
    def presentation_DocumentRoot104(self):
        return self.__presentation_DocumentRoot104

    @presentation_DocumentRoot104.setter
    def presentation_DocumentRoot104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot104", None)
        self.__presentation_DocumentRoot104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ShowTextType105"):
                    opp_val = getattr(item, "presentation_ShowTextType105", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ShowTextType105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ShowTextType105"):
                    opp_val = getattr(item, "presentation_ShowTextType105", None)
                    
                    setattr(item, "presentation_ShowTextType105", self)
                    

    @property
    def presentation_DocumentRoot85(self):
        return self.__presentation_DocumentRoot85

    @presentation_DocumentRoot85.setter
    def presentation_DocumentRoot85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot85", None)
        self.__presentation_DocumentRoot85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_HideTextType86"):
                    opp_val = getattr(item, "presentation_HideTextType86", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_HideTextType86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_HideTextType86"):
                    opp_val = getattr(item, "presentation_HideTextType86", None)
                    
                    setattr(item, "presentation_HideTextType86", self)
                    

    @property
    def presentation_DocumentRoot101(self):
        return self.__presentation_DocumentRoot101

    @presentation_DocumentRoot101.setter
    def presentation_DocumentRoot101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot101", None)
        self.__presentation_DocumentRoot101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ShowShapeType102"):
                    opp_val = getattr(item, "presentation_ShowShapeType102", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ShowShapeType102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ShowShapeType102"):
                    opp_val = getattr(item, "presentation_ShowShapeType102", None)
                    
                    setattr(item, "presentation_ShowShapeType102", self)
                    

    @property
    def presentation_DocumentRoot76(self):
        return self.__presentation_DocumentRoot76

    @presentation_DocumentRoot76.setter
    def presentation_DocumentRoot76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot76", None)
        self.__presentation_DocumentRoot76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FooterDeclType"):
                    opp_val = getattr(item, "presentation_FooterDeclType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FooterDeclType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FooterDeclType"):
                    opp_val = getattr(item, "presentation_FooterDeclType", None)
                    
                    setattr(item, "presentation_FooterDeclType", self)
                    

    @property
    def presentation_DocumentRoot71(self):
        return self.__presentation_DocumentRoot71

    @presentation_DocumentRoot71.setter
    def presentation_DocumentRoot71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot71", None)
        self.__presentation_DocumentRoot71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EventListenerType72"):
                    opp_val = getattr(item, "presentation_EventListenerType72", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EventListenerType72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EventListenerType72"):
                    opp_val = getattr(item, "presentation_EventListenerType72", None)
                    
                    setattr(item, "presentation_EventListenerType72", self)
                    

    @property
    def presentation_DocumentRoot68(self):
        return self.__presentation_DocumentRoot68

    @presentation_DocumentRoot68.setter
    def presentation_DocumentRoot68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot68", None)
        self.__presentation_DocumentRoot68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_DimType69"):
                    opp_val = getattr(item, "presentation_DimType69", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_DimType69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_DimType69"):
                    opp_val = getattr(item, "presentation_DimType69", None)
                    
                    setattr(item, "presentation_DimType69", self)
                    

    @property
    def presentation_DocumentRoot58(self):
        return self.__presentation_DocumentRoot58

    @presentation_DocumentRoot58.setter
    def presentation_DocumentRoot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot58", None)
        self.__presentation_DocumentRoot58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_AnimationGroupType59"):
                    opp_val = getattr(item, "presentation_AnimationGroupType59", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_AnimationGroupType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_AnimationGroupType59"):
                    opp_val = getattr(item, "presentation_AnimationGroupType59", None)
                    
                    setattr(item, "presentation_AnimationGroupType59", self)
                    

    @property
    def presentation_DocumentRoot64(self):
        return self.__presentation_DocumentRoot64

    @presentation_DocumentRoot64.setter
    def presentation_DocumentRoot64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot64", None)
        self.__presentation_DocumentRoot64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_DateTimeType"):
                    opp_val = getattr(item, "presentation_DateTimeType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_DateTimeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_DateTimeType"):
                    opp_val = getattr(item, "presentation_DateTimeType", None)
                    
                    setattr(item, "presentation_DateTimeType", self)
                    

    @property
    def presentation_DocumentRoot80(self):
        return self.__presentation_DocumentRoot80

    @presentation_DocumentRoot80.setter
    def presentation_DocumentRoot80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot80", None)
        self.__presentation_DocumentRoot80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_HeaderDeclType"):
                    opp_val = getattr(item, "presentation_HeaderDeclType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_HeaderDeclType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_HeaderDeclType"):
                    opp_val = getattr(item, "presentation_HeaderDeclType", None)
                    
                    setattr(item, "presentation_HeaderDeclType", self)
                    

    @property
    def presentation_DocumentRoot88(self):
        return self.__presentation_DocumentRoot88

    @presentation_DocumentRoot88.setter
    def presentation_DocumentRoot88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DocumentRoot__presentation_DocumentRoot88", None)
        self.__presentation_DocumentRoot88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_NotesType89"):
                    opp_val = getattr(item, "presentation_NotesType89", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_NotesType89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_NotesType89"):
                    opp_val = getattr(item, "presentation_NotesType89", None)
                    
                    setattr(item, "presentation_NotesType89", self)
                    

class presentation_ShowTextType:

    def __init__(self, delay: str, direction: str, effect: str, pathId: str, shapeId: str, speed: str, startScale: str, presentation_ShowTextType: "presentation_SoundType" = None, presentation_ShowTextType105: "presentation_DocumentRoot" = None):
        self.delay = delay
        self.direction = direction
        self.effect = effect
        self.pathId = pathId
        self.shapeId = shapeId
        self.speed = speed
        self.startScale = startScale
        self.presentation_ShowTextType = presentation_ShowTextType
        self.presentation_ShowTextType105 = presentation_ShowTextType105
        
        pass
    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def startScale(self):
        return self.__startScale

    @startScale.setter
    def startScale(self, startScale: str):
        self.__startScale = startScale


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay


    @property
    def pathId(self):
        return self.__pathId

    @pathId.setter
    def pathId(self, pathId: str):
        self.__pathId = pathId


    @property
    def shapeId(self):
        return self.__shapeId

    @shapeId.setter
    def shapeId(self, shapeId: str):
        self.__shapeId = shapeId


    @property
    def presentation_ShowTextType(self):
        return self.__presentation_ShowTextType

    @presentation_ShowTextType.setter
    def presentation_ShowTextType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ShowTextType__presentation_ShowTextType", None)
        self.__presentation_ShowTextType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SoundType52"):
                opp_val = getattr(old_value, "presentation_SoundType52", None)
                if opp_val == self:
                    setattr(old_value, "presentation_SoundType52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SoundType52"):
                opp_val = getattr(value, "presentation_SoundType52", None)
                setattr(value, "presentation_SoundType52", self)

    @property
    def presentation_ShowTextType105(self):
        return self.__presentation_ShowTextType105

    @presentation_ShowTextType105.setter
    def presentation_ShowTextType105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ShowTextType__presentation_ShowTextType105", None)
        self.__presentation_ShowTextType105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot104"):
                opp_val = getattr(old_value, "presentation_DocumentRoot104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot104"):
                opp_val = getattr(value, "presentation_DocumentRoot104", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ShowShapeType:

    def __init__(self, delay: str, direction: str, effect: str, pathId: str, shapeId: str, speed: str, startScale: str, presentation_ShowShapeType: "presentation_SoundType" = None, presentation_ShowShapeType102: "presentation_DocumentRoot" = None):
        self.delay = delay
        self.direction = direction
        self.effect = effect
        self.pathId = pathId
        self.shapeId = shapeId
        self.speed = speed
        self.startScale = startScale
        self.presentation_ShowShapeType = presentation_ShowShapeType
        self.presentation_ShowShapeType102 = presentation_ShowShapeType102
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def pathId(self):
        return self.__pathId

    @pathId.setter
    def pathId(self, pathId: str):
        self.__pathId = pathId


    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def startScale(self):
        return self.__startScale

    @startScale.setter
    def startScale(self, startScale: str):
        self.__startScale = startScale


    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def shapeId(self):
        return self.__shapeId

    @shapeId.setter
    def shapeId(self, shapeId: str):
        self.__shapeId = shapeId


    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay


    @property
    def presentation_ShowShapeType(self):
        return self.__presentation_ShowShapeType

    @presentation_ShowShapeType.setter
    def presentation_ShowShapeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ShowShapeType__presentation_ShowShapeType", None)
        self.__presentation_ShowShapeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SoundType50"):
                opp_val = getattr(old_value, "presentation_SoundType50", None)
                if opp_val == self:
                    setattr(old_value, "presentation_SoundType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SoundType50"):
                opp_val = getattr(value, "presentation_SoundType50", None)
                setattr(value, "presentation_SoundType50", self)

    @property
    def presentation_ShowShapeType102(self):
        return self.__presentation_ShowShapeType102

    @presentation_ShowShapeType102.setter
    def presentation_ShowShapeType102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ShowShapeType__presentation_ShowShapeType102", None)
        self.__presentation_ShowShapeType102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot101"):
                opp_val = getattr(old_value, "presentation_DocumentRoot101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot101"):
                opp_val = getattr(value, "presentation_DocumentRoot101", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_PlayType:

    def __init__(self, shapeId: str, speed: str, presentation_PlayType: "presentation_DocumentRoot" = None):
        self.shapeId = shapeId
        self.speed = speed
        self.presentation_PlayType = presentation_PlayType
        
        pass
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def shapeId(self):
        return self.__shapeId

    @shapeId.setter
    def shapeId(self, shapeId: str):
        self.__shapeId = shapeId


    @property
    def presentation_PlayType(self):
        return self.__presentation_PlayType

    @presentation_PlayType.setter
    def presentation_PlayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_PlayType__presentation_PlayType", None)
        self.__presentation_PlayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot93"):
                opp_val = getattr(old_value, "presentation_DocumentRoot93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot93"):
                opp_val = getattr(value, "presentation_DocumentRoot93", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_ShowType:

    def __init__(self, name: str, pages: str, presentation_ShowType: "presentation_SettingsType" = None, presentation_ShowType99: "presentation_DocumentRoot" = None):
        self.name = name
        self.pages = pages
        self.presentation_ShowType = presentation_ShowType
        self.presentation_ShowType99 = presentation_ShowType99
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def presentation_ShowType(self):
        return self.__presentation_ShowType

    @presentation_ShowType.setter
    def presentation_ShowType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ShowType__presentation_ShowType", None)
        self.__presentation_ShowType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SettingsType"):
                opp_val = getattr(old_value, "presentation_SettingsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SettingsType"):
                opp_val = getattr(value, "presentation_SettingsType", None)
                if opp_val is None:
                    setattr(value, "presentation_SettingsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_ShowType99(self):
        return self.__presentation_ShowType99

    @presentation_ShowType99.setter
    def presentation_ShowType99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_ShowType__presentation_ShowType99", None)
        self.__presentation_ShowType99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot98"):
                opp_val = getattr(old_value, "presentation_DocumentRoot98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot98"):
                opp_val = getattr(value, "presentation_DocumentRoot98", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_SettingsType:

    def __init__(self, animations: str, endless: str, fullScreen: str, mouseAsPen: str, mouseVisible: str, pause: str, show1: str, showEndOfPresentationSlide: str, showLogo: str, startPage: str, startWithNavigator: str, stayOnTop: str, transitionOnClick: str, forceManual: str, presentation_SettingsType: set["presentation_ShowType"] = None, presentation_SettingsType96: "presentation_DocumentRoot" = None):
        self.animations = animations
        self.endless = endless
        self.fullScreen = fullScreen
        self.mouseAsPen = mouseAsPen
        self.mouseVisible = mouseVisible
        self.pause = pause
        self.show1 = show1
        self.showEndOfPresentationSlide = showEndOfPresentationSlide
        self.showLogo = showLogo
        self.startPage = startPage
        self.startWithNavigator = startWithNavigator
        self.stayOnTop = stayOnTop
        self.transitionOnClick = transitionOnClick
        self.forceManual = forceManual
        self.presentation_SettingsType = presentation_SettingsType if presentation_SettingsType is not None else set()
        self.presentation_SettingsType96 = presentation_SettingsType96
        
        pass
    @property
    def transitionOnClick(self):
        return self.__transitionOnClick

    @transitionOnClick.setter
    def transitionOnClick(self, transitionOnClick: str):
        self.__transitionOnClick = transitionOnClick


    @property
    def fullScreen(self):
        return self.__fullScreen

    @fullScreen.setter
    def fullScreen(self, fullScreen: str):
        self.__fullScreen = fullScreen


    @property
    def endless(self):
        return self.__endless

    @endless.setter
    def endless(self, endless: str):
        self.__endless = endless


    @property
    def showLogo(self):
        return self.__showLogo

    @showLogo.setter
    def showLogo(self, showLogo: str):
        self.__showLogo = showLogo


    @property
    def stayOnTop(self):
        return self.__stayOnTop

    @stayOnTop.setter
    def stayOnTop(self, stayOnTop: str):
        self.__stayOnTop = stayOnTop


    @property
    def startWithNavigator(self):
        return self.__startWithNavigator

    @startWithNavigator.setter
    def startWithNavigator(self, startWithNavigator: str):
        self.__startWithNavigator = startWithNavigator


    @property
    def forceManual(self):
        return self.__forceManual

    @forceManual.setter
    def forceManual(self, forceManual: str):
        self.__forceManual = forceManual


    @property
    def mouseAsPen(self):
        return self.__mouseAsPen

    @mouseAsPen.setter
    def mouseAsPen(self, mouseAsPen: str):
        self.__mouseAsPen = mouseAsPen


    @property
    def mouseVisible(self):
        return self.__mouseVisible

    @mouseVisible.setter
    def mouseVisible(self, mouseVisible: str):
        self.__mouseVisible = mouseVisible


    @property
    def showEndOfPresentationSlide(self):
        return self.__showEndOfPresentationSlide

    @showEndOfPresentationSlide.setter
    def showEndOfPresentationSlide(self, showEndOfPresentationSlide: str):
        self.__showEndOfPresentationSlide = showEndOfPresentationSlide


    @property
    def animations(self):
        return self.__animations

    @animations.setter
    def animations(self, animations: str):
        self.__animations = animations


    @property
    def show1(self):
        return self.__show1

    @show1.setter
    def show1(self, show1: str):
        self.__show1 = show1


    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, pause: str):
        self.__pause = pause


    @property
    def startPage(self):
        return self.__startPage

    @startPage.setter
    def startPage(self, startPage: str):
        self.__startPage = startPage


    @property
    def presentation_SettingsType96(self):
        return self.__presentation_SettingsType96

    @presentation_SettingsType96.setter
    def presentation_SettingsType96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SettingsType__presentation_SettingsType96", None)
        self.__presentation_SettingsType96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot95"):
                opp_val = getattr(old_value, "presentation_DocumentRoot95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot95"):
                opp_val = getattr(value, "presentation_DocumentRoot95", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_SettingsType(self):
        return self.__presentation_SettingsType

    @presentation_SettingsType.setter
    def presentation_SettingsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SettingsType__presentation_SettingsType", None)
        self.__presentation_SettingsType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ShowType"):
                    opp_val = getattr(item, "presentation_ShowType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ShowType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ShowType"):
                    opp_val = getattr(item, "presentation_ShowType", None)
                    
                    setattr(item, "presentation_ShowType", self)
                    

class presentation_PlaceholderType:

    def __init__(self, height: str, object: str, width: str, x: str, y: str, presentation_PlaceholderType: "presentation_DocumentRoot" = None):
        self.height = height
        self.object = object
        self.width = width
        self.x = x
        self.y = y
        self.presentation_PlaceholderType = presentation_PlaceholderType
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def presentation_PlaceholderType(self):
        return self.__presentation_PlaceholderType

    @presentation_PlaceholderType.setter
    def presentation_PlaceholderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_PlaceholderType__presentation_PlaceholderType", None)
        self.__presentation_PlaceholderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot91"):
                opp_val = getattr(old_value, "presentation_DocumentRoot91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot91"):
                opp_val = getattr(value, "presentation_DocumentRoot91", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_CustomShapeType:

    pass
class presentation_SceneType:

    pass
class presentation_ControlType:

    pass
class presentation_ConnectorType:

    pass
class presentation_CaptionType:

    pass
class presentation_MeasureType:

    pass
class presentation_FrameType:

    pass
class presentation_PageThumbnailType:

    pass
class presentation_PathType:

    pass
class presentation_GType:

    pass
class presentation_EllipseType:

    pass
class presentation_CircleType:

    pass
class presentation_PolylineType:

    pass
class presentation_LineType:

    pass
class presentation_RegularPolygonType:

    pass
class presentation_PolygonType:

    pass
class presentation_NotesType:

    def __init__(self, shape: str, pageLayoutName: str, styleName: str, useDateTimeName: str, useFooterName: str, useHeaderName: str, presentation_NotesType43: set["presentation_ControlType"] = None, presentation_NotesType45: set["presentation_SceneType"] = None, presentation_NotesType47: set["presentation_CustomShapeType"] = None, presentation_NotesType89: "presentation_DocumentRoot" = None, presentation_NotesType: "presentation_FormsType" = None, presentation_NotesType15: set["presentation_RectType"] = None, presentation_NotesType21: set["presentation_PolygonType"] = None, presentation_NotesType23: set["presentation_RegularPolygonType"] = None, presentation_NotesType17: set["presentation_LineType"] = None, presentation_NotesType19: set["presentation_PolylineType"] = None, presentation_NotesType27: set["presentation_CircleType"] = None, presentation_NotesType29: set["presentation_EllipseType"] = None, presentation_NotesType31: set["presentation_GType"] = None, presentation_NotesType33: set["presentation_PageThumbnailType"] = None, presentation_NotesType25: set["presentation_PathType"] = None, presentation_NotesType35: set["presentation_FrameType"] = None, presentation_NotesType37: set["presentation_MeasureType"] = None, presentation_NotesType39: set["presentation_CaptionType"] = None, presentation_NotesType41: set["presentation_ConnectorType"] = None):
        self.shape = shape
        self.pageLayoutName = pageLayoutName
        self.styleName = styleName
        self.useDateTimeName = useDateTimeName
        self.useFooterName = useFooterName
        self.useHeaderName = useHeaderName
        self.presentation_NotesType43 = presentation_NotesType43 if presentation_NotesType43 is not None else set()
        self.presentation_NotesType45 = presentation_NotesType45 if presentation_NotesType45 is not None else set()
        self.presentation_NotesType47 = presentation_NotesType47 if presentation_NotesType47 is not None else set()
        self.presentation_NotesType89 = presentation_NotesType89
        self.presentation_NotesType = presentation_NotesType
        self.presentation_NotesType15 = presentation_NotesType15 if presentation_NotesType15 is not None else set()
        self.presentation_NotesType21 = presentation_NotesType21 if presentation_NotesType21 is not None else set()
        self.presentation_NotesType23 = presentation_NotesType23 if presentation_NotesType23 is not None else set()
        self.presentation_NotesType17 = presentation_NotesType17 if presentation_NotesType17 is not None else set()
        self.presentation_NotesType19 = presentation_NotesType19 if presentation_NotesType19 is not None else set()
        self.presentation_NotesType27 = presentation_NotesType27 if presentation_NotesType27 is not None else set()
        self.presentation_NotesType29 = presentation_NotesType29 if presentation_NotesType29 is not None else set()
        self.presentation_NotesType31 = presentation_NotesType31 if presentation_NotesType31 is not None else set()
        self.presentation_NotesType33 = presentation_NotesType33 if presentation_NotesType33 is not None else set()
        self.presentation_NotesType25 = presentation_NotesType25 if presentation_NotesType25 is not None else set()
        self.presentation_NotesType35 = presentation_NotesType35 if presentation_NotesType35 is not None else set()
        self.presentation_NotesType37 = presentation_NotesType37 if presentation_NotesType37 is not None else set()
        self.presentation_NotesType39 = presentation_NotesType39 if presentation_NotesType39 is not None else set()
        self.presentation_NotesType41 = presentation_NotesType41 if presentation_NotesType41 is not None else set()
        
        pass
    @property
    def pageLayoutName(self):
        return self.__pageLayoutName

    @pageLayoutName.setter
    def pageLayoutName(self, pageLayoutName: str):
        self.__pageLayoutName = pageLayoutName


    @property
    def useFooterName(self):
        return self.__useFooterName

    @useFooterName.setter
    def useFooterName(self, useFooterName: str):
        self.__useFooterName = useFooterName


    @property
    def styleName(self):
        return self.__styleName

    @styleName.setter
    def styleName(self, styleName: str):
        self.__styleName = styleName


    @property
    def useDateTimeName(self):
        return self.__useDateTimeName

    @useDateTimeName.setter
    def useDateTimeName(self, useDateTimeName: str):
        self.__useDateTimeName = useDateTimeName


    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def useHeaderName(self):
        return self.__useHeaderName

    @useHeaderName.setter
    def useHeaderName(self, useHeaderName: str):
        self.__useHeaderName = useHeaderName


    @property
    def presentation_NotesType45(self):
        return self.__presentation_NotesType45

    @presentation_NotesType45.setter
    def presentation_NotesType45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType45", None)
        self.__presentation_NotesType45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_SceneType"):
                    opp_val = getattr(item, "presentation_SceneType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_SceneType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_SceneType"):
                    opp_val = getattr(item, "presentation_SceneType", None)
                    
                    setattr(item, "presentation_SceneType", self)
                    

    @property
    def presentation_NotesType23(self):
        return self.__presentation_NotesType23

    @presentation_NotesType23.setter
    def presentation_NotesType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType23", None)
        self.__presentation_NotesType23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_RegularPolygonType"):
                    opp_val = getattr(item, "presentation_RegularPolygonType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_RegularPolygonType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_RegularPolygonType"):
                    opp_val = getattr(item, "presentation_RegularPolygonType", None)
                    
                    setattr(item, "presentation_RegularPolygonType", self)
                    

    @property
    def presentation_NotesType31(self):
        return self.__presentation_NotesType31

    @presentation_NotesType31.setter
    def presentation_NotesType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType31", None)
        self.__presentation_NotesType31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_GType"):
                    opp_val = getattr(item, "presentation_GType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_GType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_GType"):
                    opp_val = getattr(item, "presentation_GType", None)
                    
                    setattr(item, "presentation_GType", self)
                    

    @property
    def presentation_NotesType(self):
        return self.__presentation_NotesType

    @presentation_NotesType.setter
    def presentation_NotesType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType", None)
        self.__presentation_NotesType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_FormsType"):
                opp_val = getattr(old_value, "presentation_FormsType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_FormsType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_FormsType"):
                opp_val = getattr(value, "presentation_FormsType", None)
                setattr(value, "presentation_FormsType", self)

    @property
    def presentation_NotesType39(self):
        return self.__presentation_NotesType39

    @presentation_NotesType39.setter
    def presentation_NotesType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType39", None)
        self.__presentation_NotesType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CaptionType"):
                    opp_val = getattr(item, "presentation_CaptionType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CaptionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CaptionType"):
                    opp_val = getattr(item, "presentation_CaptionType", None)
                    
                    setattr(item, "presentation_CaptionType", self)
                    

    @property
    def presentation_NotesType41(self):
        return self.__presentation_NotesType41

    @presentation_NotesType41.setter
    def presentation_NotesType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType41", None)
        self.__presentation_NotesType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ConnectorType"):
                    opp_val = getattr(item, "presentation_ConnectorType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ConnectorType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ConnectorType"):
                    opp_val = getattr(item, "presentation_ConnectorType", None)
                    
                    setattr(item, "presentation_ConnectorType", self)
                    

    @property
    def presentation_NotesType89(self):
        return self.__presentation_NotesType89

    @presentation_NotesType89.setter
    def presentation_NotesType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType89", None)
        self.__presentation_NotesType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot88"):
                opp_val = getattr(old_value, "presentation_DocumentRoot88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot88"):
                opp_val = getattr(value, "presentation_DocumentRoot88", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_NotesType43(self):
        return self.__presentation_NotesType43

    @presentation_NotesType43.setter
    def presentation_NotesType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType43", None)
        self.__presentation_NotesType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_ControlType"):
                    opp_val = getattr(item, "presentation_ControlType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_ControlType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_ControlType"):
                    opp_val = getattr(item, "presentation_ControlType", None)
                    
                    setattr(item, "presentation_ControlType", self)
                    

    @property
    def presentation_NotesType17(self):
        return self.__presentation_NotesType17

    @presentation_NotesType17.setter
    def presentation_NotesType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType17", None)
        self.__presentation_NotesType17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_LineType"):
                    opp_val = getattr(item, "presentation_LineType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_LineType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_LineType"):
                    opp_val = getattr(item, "presentation_LineType", None)
                    
                    setattr(item, "presentation_LineType", self)
                    

    @property
    def presentation_NotesType25(self):
        return self.__presentation_NotesType25

    @presentation_NotesType25.setter
    def presentation_NotesType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType25", None)
        self.__presentation_NotesType25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_PathType"):
                    opp_val = getattr(item, "presentation_PathType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_PathType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_PathType"):
                    opp_val = getattr(item, "presentation_PathType", None)
                    
                    setattr(item, "presentation_PathType", self)
                    

    @property
    def presentation_NotesType21(self):
        return self.__presentation_NotesType21

    @presentation_NotesType21.setter
    def presentation_NotesType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType21", None)
        self.__presentation_NotesType21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_PolygonType"):
                    opp_val = getattr(item, "presentation_PolygonType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_PolygonType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_PolygonType"):
                    opp_val = getattr(item, "presentation_PolygonType", None)
                    
                    setattr(item, "presentation_PolygonType", self)
                    

    @property
    def presentation_NotesType37(self):
        return self.__presentation_NotesType37

    @presentation_NotesType37.setter
    def presentation_NotesType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType37", None)
        self.__presentation_NotesType37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_MeasureType"):
                    opp_val = getattr(item, "presentation_MeasureType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_MeasureType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_MeasureType"):
                    opp_val = getattr(item, "presentation_MeasureType", None)
                    
                    setattr(item, "presentation_MeasureType", self)
                    

    @property
    def presentation_NotesType47(self):
        return self.__presentation_NotesType47

    @presentation_NotesType47.setter
    def presentation_NotesType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType47", None)
        self.__presentation_NotesType47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CustomShapeType"):
                    opp_val = getattr(item, "presentation_CustomShapeType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CustomShapeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CustomShapeType"):
                    opp_val = getattr(item, "presentation_CustomShapeType", None)
                    
                    setattr(item, "presentation_CustomShapeType", self)
                    

    @property
    def presentation_NotesType27(self):
        return self.__presentation_NotesType27

    @presentation_NotesType27.setter
    def presentation_NotesType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType27", None)
        self.__presentation_NotesType27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_CircleType"):
                    opp_val = getattr(item, "presentation_CircleType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_CircleType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_CircleType"):
                    opp_val = getattr(item, "presentation_CircleType", None)
                    
                    setattr(item, "presentation_CircleType", self)
                    

    @property
    def presentation_NotesType15(self):
        return self.__presentation_NotesType15

    @presentation_NotesType15.setter
    def presentation_NotesType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType15", None)
        self.__presentation_NotesType15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_RectType"):
                    opp_val = getattr(item, "presentation_RectType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_RectType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_RectType"):
                    opp_val = getattr(item, "presentation_RectType", None)
                    
                    setattr(item, "presentation_RectType", self)
                    

    @property
    def presentation_NotesType19(self):
        return self.__presentation_NotesType19

    @presentation_NotesType19.setter
    def presentation_NotesType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType19", None)
        self.__presentation_NotesType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_PolylineType"):
                    opp_val = getattr(item, "presentation_PolylineType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_PolylineType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_PolylineType"):
                    opp_val = getattr(item, "presentation_PolylineType", None)
                    
                    setattr(item, "presentation_PolylineType", self)
                    

    @property
    def presentation_NotesType33(self):
        return self.__presentation_NotesType33

    @presentation_NotesType33.setter
    def presentation_NotesType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType33", None)
        self.__presentation_NotesType33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_PageThumbnailType"):
                    opp_val = getattr(item, "presentation_PageThumbnailType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_PageThumbnailType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_PageThumbnailType"):
                    opp_val = getattr(item, "presentation_PageThumbnailType", None)
                    
                    setattr(item, "presentation_PageThumbnailType", self)
                    

    @property
    def presentation_NotesType35(self):
        return self.__presentation_NotesType35

    @presentation_NotesType35.setter
    def presentation_NotesType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType35", None)
        self.__presentation_NotesType35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_FrameType"):
                    opp_val = getattr(item, "presentation_FrameType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_FrameType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_FrameType"):
                    opp_val = getattr(item, "presentation_FrameType", None)
                    
                    setattr(item, "presentation_FrameType", self)
                    

    @property
    def presentation_NotesType29(self):
        return self.__presentation_NotesType29

    @presentation_NotesType29.setter
    def presentation_NotesType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_NotesType__presentation_NotesType29", None)
        self.__presentation_NotesType29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EllipseType"):
                    opp_val = getattr(item, "presentation_EllipseType", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EllipseType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EllipseType"):
                    opp_val = getattr(item, "presentation_EllipseType", None)
                    
                    setattr(item, "presentation_EllipseType", self)
                    

class presentation_RectType:

    pass
class presentation_FormsType:

    pass
class presentation_HideTextType:

    def __init__(self, pathId: str, shapeId: str, delay: str, direction: str, effect: str, speed: str, startScale: str, presentation_HideTextType86: "presentation_DocumentRoot" = None, presentation_HideTextType: "presentation_SoundType" = None):
        self.pathId = pathId
        self.shapeId = shapeId
        self.delay = delay
        self.direction = direction
        self.effect = effect
        self.speed = speed
        self.startScale = startScale
        self.presentation_HideTextType86 = presentation_HideTextType86
        self.presentation_HideTextType = presentation_HideTextType
        
        pass
    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay


    @property
    def pathId(self):
        return self.__pathId

    @pathId.setter
    def pathId(self, pathId: str):
        self.__pathId = pathId


    @property
    def startScale(self):
        return self.__startScale

    @startScale.setter
    def startScale(self, startScale: str):
        self.__startScale = startScale


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def shapeId(self):
        return self.__shapeId

    @shapeId.setter
    def shapeId(self, shapeId: str):
        self.__shapeId = shapeId


    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def presentation_HideTextType86(self):
        return self.__presentation_HideTextType86

    @presentation_HideTextType86.setter
    def presentation_HideTextType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_HideTextType__presentation_HideTextType86", None)
        self.__presentation_HideTextType86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot85"):
                opp_val = getattr(old_value, "presentation_DocumentRoot85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot85"):
                opp_val = getattr(value, "presentation_DocumentRoot85", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_HideTextType(self):
        return self.__presentation_HideTextType

    @presentation_HideTextType.setter
    def presentation_HideTextType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_HideTextType__presentation_HideTextType", None)
        self.__presentation_HideTextType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SoundType12"):
                opp_val = getattr(old_value, "presentation_SoundType12", None)
                if opp_val == self:
                    setattr(old_value, "presentation_SoundType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SoundType12"):
                opp_val = getattr(value, "presentation_SoundType12", None)
                setattr(value, "presentation_SoundType12", self)

class presentation_FooterDeclType:

    def __init__(self, mixed: str, name: str, presentation_FooterDeclType: "presentation_DocumentRoot" = None):
        self.mixed = mixed
        self.name = name
        self.presentation_FooterDeclType = presentation_FooterDeclType
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def presentation_FooterDeclType(self):
        return self.__presentation_FooterDeclType

    @presentation_FooterDeclType.setter
    def presentation_FooterDeclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_FooterDeclType__presentation_FooterDeclType", None)
        self.__presentation_FooterDeclType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot76"):
                opp_val = getattr(old_value, "presentation_DocumentRoot76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot76"):
                opp_val = getattr(value, "presentation_DocumentRoot76", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_HideShapeType:

    def __init__(self, speed: str, startScale: str, delay: str, direction: str, effect: str, pathId: str, shapeId: str, presentation_HideShapeType83: "presentation_DocumentRoot" = None, presentation_HideShapeType: "presentation_SoundType" = None):
        self.speed = speed
        self.startScale = startScale
        self.delay = delay
        self.direction = direction
        self.effect = effect
        self.pathId = pathId
        self.shapeId = shapeId
        self.presentation_HideShapeType83 = presentation_HideShapeType83
        self.presentation_HideShapeType = presentation_HideShapeType
        
        pass
    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay


    @property
    def shapeId(self):
        return self.__shapeId

    @shapeId.setter
    def shapeId(self, shapeId: str):
        self.__shapeId = shapeId


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def startScale(self):
        return self.__startScale

    @startScale.setter
    def startScale(self, startScale: str):
        self.__startScale = startScale


    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def pathId(self):
        return self.__pathId

    @pathId.setter
    def pathId(self, pathId: str):
        self.__pathId = pathId


    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def presentation_HideShapeType83(self):
        return self.__presentation_HideShapeType83

    @presentation_HideShapeType83.setter
    def presentation_HideShapeType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_HideShapeType__presentation_HideShapeType83", None)
        self.__presentation_HideShapeType83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot82"):
                opp_val = getattr(old_value, "presentation_DocumentRoot82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot82"):
                opp_val = getattr(value, "presentation_DocumentRoot82", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_HideShapeType(self):
        return self.__presentation_HideShapeType

    @presentation_HideShapeType.setter
    def presentation_HideShapeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_HideShapeType__presentation_HideShapeType", None)
        self.__presentation_HideShapeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SoundType10"):
                opp_val = getattr(old_value, "presentation_SoundType10", None)
                if opp_val == self:
                    setattr(old_value, "presentation_SoundType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SoundType10"):
                opp_val = getattr(value, "presentation_SoundType10", None)
                setattr(value, "presentation_SoundType10", self)

class presentation_HeaderType:

    pass
class presentation_HeaderDeclType:

    def __init__(self, mixed: str, name: str, presentation_HeaderDeclType: "presentation_DocumentRoot" = None):
        self.mixed = mixed
        self.name = name
        self.presentation_HeaderDeclType = presentation_HeaderDeclType
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def presentation_HeaderDeclType(self):
        return self.__presentation_HeaderDeclType

    @presentation_HeaderDeclType.setter
    def presentation_HeaderDeclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_HeaderDeclType__presentation_HeaderDeclType", None)
        self.__presentation_HeaderDeclType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot80"):
                opp_val = getattr(old_value, "presentation_DocumentRoot80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot80"):
                opp_val = getattr(value, "presentation_DocumentRoot80", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_FooterType:

    pass
class presentation_DimType:

    def __init__(self, color: str, shapeId: str, presentation_DimType69: "presentation_DocumentRoot" = None, presentation_DimType: "presentation_SoundType" = None):
        self.color = color
        self.shapeId = shapeId
        self.presentation_DimType69 = presentation_DimType69
        self.presentation_DimType = presentation_DimType
        
        pass
    @property
    def shapeId(self):
        return self.__shapeId

    @shapeId.setter
    def shapeId(self, shapeId: str):
        self.__shapeId = shapeId


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def presentation_DimType(self):
        return self.__presentation_DimType

    @presentation_DimType.setter
    def presentation_DimType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DimType__presentation_DimType", None)
        self.__presentation_DimType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SoundType"):
                opp_val = getattr(old_value, "presentation_SoundType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_SoundType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SoundType"):
                opp_val = getattr(value, "presentation_SoundType", None)
                setattr(value, "presentation_SoundType", self)

    @property
    def presentation_DimType69(self):
        return self.__presentation_DimType69

    @presentation_DimType69.setter
    def presentation_DimType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DimType__presentation_DimType69", None)
        self.__presentation_DimType69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot68"):
                opp_val = getattr(old_value, "presentation_DocumentRoot68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot68"):
                opp_val = getattr(value, "presentation_DocumentRoot68", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_DateTimeType:

    pass
class presentation_EventListenerType:

    def __init__(self, show: str, speed: str, startScale: str, type: str, action: str, actuate: str, direction: str, effect: str, eventName: str, href: str, verb: str, presentation_EventListenerType72: "presentation_DocumentRoot" = None, presentation_EventListenerType: "presentation_SoundType" = None):
        self.show = show
        self.speed = speed
        self.startScale = startScale
        self.type = type
        self.action = action
        self.actuate = actuate
        self.direction = direction
        self.effect = effect
        self.eventName = eventName
        self.href = href
        self.verb = verb
        self.presentation_EventListenerType72 = presentation_EventListenerType72
        self.presentation_EventListenerType = presentation_EventListenerType
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def actuate(self):
        return self.__actuate

    @actuate.setter
    def actuate(self, actuate: str):
        self.__actuate = actuate


    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def verb(self):
        return self.__verb

    @verb.setter
    def verb(self, verb: str):
        self.__verb = verb


    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed


    @property
    def show(self):
        return self.__show

    @show.setter
    def show(self, show: str):
        self.__show = show


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def eventName(self):
        return self.__eventName

    @eventName.setter
    def eventName(self, eventName: str):
        self.__eventName = eventName


    @property
    def href(self):
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href


    @property
    def startScale(self):
        return self.__startScale

    @startScale.setter
    def startScale(self, startScale: str):
        self.__startScale = startScale


    @property
    def presentation_EventListenerType(self):
        return self.__presentation_EventListenerType

    @presentation_EventListenerType.setter
    def presentation_EventListenerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_EventListenerType__presentation_EventListenerType", None)
        self.__presentation_EventListenerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_SoundType8"):
                opp_val = getattr(old_value, "presentation_SoundType8", None)
                if opp_val == self:
                    setattr(old_value, "presentation_SoundType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_SoundType8"):
                opp_val = getattr(value, "presentation_SoundType8", None)
                setattr(value, "presentation_SoundType8", self)

    @property
    def presentation_EventListenerType72(self):
        return self.__presentation_EventListenerType72

    @presentation_EventListenerType72.setter
    def presentation_EventListenerType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_EventListenerType__presentation_EventListenerType72", None)
        self.__presentation_EventListenerType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot71"):
                opp_val = getattr(old_value, "presentation_DocumentRoot71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot71"):
                opp_val = getattr(value, "presentation_DocumentRoot71", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_SoundType:

    def __init__(self, actuate: str, href: str, playFull: str, show: str, type: str, presentation_SoundType50: "presentation_ShowShapeType" = None, presentation_SoundType52: "presentation_ShowTextType" = None, presentation_SoundType: "presentation_DimType" = None, presentation_SoundType8: "presentation_EventListenerType" = None, presentation_SoundType10: "presentation_HideShapeType" = None, presentation_SoundType12: "presentation_HideTextType" = None, presentation_SoundType108: "presentation_DocumentRoot" = None):
        self.actuate = actuate
        self.href = href
        self.playFull = playFull
        self.show = show
        self.type = type
        self.presentation_SoundType50 = presentation_SoundType50
        self.presentation_SoundType52 = presentation_SoundType52
        self.presentation_SoundType = presentation_SoundType
        self.presentation_SoundType8 = presentation_SoundType8
        self.presentation_SoundType10 = presentation_SoundType10
        self.presentation_SoundType12 = presentation_SoundType12
        self.presentation_SoundType108 = presentation_SoundType108
        
        pass
    @property
    def actuate(self):
        return self.__actuate

    @actuate.setter
    def actuate(self, actuate: str):
        self.__actuate = actuate


    @property
    def playFull(self):
        return self.__playFull

    @playFull.setter
    def playFull(self, playFull: str):
        self.__playFull = playFull


    @property
    def href(self):
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href


    @property
    def show(self):
        return self.__show

    @show.setter
    def show(self, show: str):
        self.__show = show


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def presentation_SoundType108(self):
        return self.__presentation_SoundType108

    @presentation_SoundType108.setter
    def presentation_SoundType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType108", None)
        self.__presentation_SoundType108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot107"):
                opp_val = getattr(old_value, "presentation_DocumentRoot107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot107"):
                opp_val = getattr(value, "presentation_DocumentRoot107", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_SoundType(self):
        return self.__presentation_SoundType

    @presentation_SoundType.setter
    def presentation_SoundType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType", None)
        self.__presentation_SoundType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DimType"):
                opp_val = getattr(old_value, "presentation_DimType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_DimType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DimType"):
                opp_val = getattr(value, "presentation_DimType", None)
                setattr(value, "presentation_DimType", self)

    @property
    def presentation_SoundType10(self):
        return self.__presentation_SoundType10

    @presentation_SoundType10.setter
    def presentation_SoundType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType10", None)
        self.__presentation_SoundType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_HideShapeType"):
                opp_val = getattr(old_value, "presentation_HideShapeType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_HideShapeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_HideShapeType"):
                opp_val = getattr(value, "presentation_HideShapeType", None)
                setattr(value, "presentation_HideShapeType", self)

    @property
    def presentation_SoundType52(self):
        return self.__presentation_SoundType52

    @presentation_SoundType52.setter
    def presentation_SoundType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType52", None)
        self.__presentation_SoundType52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ShowTextType"):
                opp_val = getattr(old_value, "presentation_ShowTextType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_ShowTextType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ShowTextType"):
                opp_val = getattr(value, "presentation_ShowTextType", None)
                setattr(value, "presentation_ShowTextType", self)

    @property
    def presentation_SoundType8(self):
        return self.__presentation_SoundType8

    @presentation_SoundType8.setter
    def presentation_SoundType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType8", None)
        self.__presentation_SoundType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_EventListenerType"):
                opp_val = getattr(old_value, "presentation_EventListenerType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_EventListenerType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_EventListenerType"):
                opp_val = getattr(value, "presentation_EventListenerType", None)
                setattr(value, "presentation_EventListenerType", self)

    @property
    def presentation_SoundType12(self):
        return self.__presentation_SoundType12

    @presentation_SoundType12.setter
    def presentation_SoundType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType12", None)
        self.__presentation_SoundType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_HideTextType"):
                opp_val = getattr(old_value, "presentation_HideTextType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_HideTextType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_HideTextType"):
                opp_val = getattr(value, "presentation_HideTextType", None)
                setattr(value, "presentation_HideTextType", self)

    @property
    def presentation_SoundType50(self):
        return self.__presentation_SoundType50

    @presentation_SoundType50.setter
    def presentation_SoundType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_SoundType__presentation_SoundType50", None)
        self.__presentation_SoundType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_ShowShapeType"):
                opp_val = getattr(old_value, "presentation_ShowShapeType", None)
                if opp_val == self:
                    setattr(old_value, "presentation_ShowShapeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_ShowShapeType"):
                opp_val = getattr(value, "presentation_ShowShapeType", None)
                setattr(value, "presentation_ShowShapeType", self)

class presentation_AnimationsType1:

    def __init__(self, group: str, presentationAnimationElementsGroup: str, presentation_AnimationsType162: "presentation_DocumentRoot" = None, presentation_AnimationsType1: set["presentation_EObject"] = None, presentation_AnimationsType14: set["presentation_AnimationGroupType"] = None):
        self.group = group
        self.presentationAnimationElementsGroup = presentationAnimationElementsGroup
        self.presentation_AnimationsType162 = presentation_AnimationsType162
        self.presentation_AnimationsType1 = presentation_AnimationsType1 if presentation_AnimationsType1 is not None else set()
        self.presentation_AnimationsType14 = presentation_AnimationsType14 if presentation_AnimationsType14 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def presentationAnimationElementsGroup(self):
        return self.__presentationAnimationElementsGroup

    @presentationAnimationElementsGroup.setter
    def presentationAnimationElementsGroup(self, presentationAnimationElementsGroup: str):
        self.__presentationAnimationElementsGroup = presentationAnimationElementsGroup


    @property
    def presentation_AnimationsType14(self):
        return self.__presentation_AnimationsType14

    @presentation_AnimationsType14.setter
    def presentation_AnimationsType14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AnimationsType1__presentation_AnimationsType14", None)
        self.__presentation_AnimationsType14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_AnimationGroupType5"):
                    opp_val = getattr(item, "presentation_AnimationGroupType5", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_AnimationGroupType5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_AnimationGroupType5"):
                    opp_val = getattr(item, "presentation_AnimationGroupType5", None)
                    
                    setattr(item, "presentation_AnimationGroupType5", self)
                    

    @property
    def presentation_AnimationsType162(self):
        return self.__presentation_AnimationsType162

    @presentation_AnimationsType162.setter
    def presentation_AnimationsType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AnimationsType1__presentation_AnimationsType162", None)
        self.__presentation_AnimationsType162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot61"):
                opp_val = getattr(old_value, "presentation_DocumentRoot61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot61"):
                opp_val = getattr(value, "presentation_DocumentRoot61", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_AnimationsType1(self):
        return self.__presentation_AnimationsType1

    @presentation_AnimationsType1.setter
    def presentation_AnimationsType1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AnimationsType1__presentation_AnimationsType1", None)
        self.__presentation_AnimationsType1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "presentation_EObject2"):
                    opp_val = getattr(item, "presentation_EObject2", None)
                    
                    if opp_val == self:
                        setattr(item, "presentation_EObject2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "presentation_EObject2"):
                    opp_val = getattr(item, "presentation_EObject2", None)
                    
                    setattr(item, "presentation_EObject2", self)
                    

class presentation_EObject:

    pass
class presentation_DateTimeDeclType:

    def __init__(self, mixed: str, dataStyleName: str, name: str, source: str, presentation_DateTimeDeclType: "presentation_DocumentRoot" = None):
        self.mixed = mixed
        self.dataStyleName = dataStyleName
        self.name = name
        self.source = source
        self.presentation_DateTimeDeclType = presentation_DateTimeDeclType
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def dataStyleName(self):
        return self.__dataStyleName

    @dataStyleName.setter
    def dataStyleName(self, dataStyleName: str):
        self.__dataStyleName = dataStyleName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def presentation_DateTimeDeclType(self):
        return self.__presentation_DateTimeDeclType

    @presentation_DateTimeDeclType.setter
    def presentation_DateTimeDeclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_DateTimeDeclType__presentation_DateTimeDeclType", None)
        self.__presentation_DateTimeDeclType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot66"):
                opp_val = getattr(old_value, "presentation_DocumentRoot66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot66"):
                opp_val = getattr(value, "presentation_DocumentRoot66", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class presentation_AnimationGroupType:

    def __init__(self, presentationAnimationElementsGroup: str, presentation_AnimationGroupType59: "presentation_DocumentRoot" = None, presentation_AnimationGroupType5: "presentation_AnimationsType1" = None, presentation_AnimationGroupType: set["presentation_EObject"] = None):
        self.presentationAnimationElementsGroup = presentationAnimationElementsGroup
        self.presentation_AnimationGroupType59 = presentation_AnimationGroupType59
        self.presentation_AnimationGroupType5 = presentation_AnimationGroupType5
        self.presentation_AnimationGroupType = presentation_AnimationGroupType if presentation_AnimationGroupType is not None else set()
        
        pass
    @property
    def presentationAnimationElementsGroup(self):
        return self.__presentationAnimationElementsGroup

    @presentationAnimationElementsGroup.setter
    def presentationAnimationElementsGroup(self, presentationAnimationElementsGroup: str):
        self.__presentationAnimationElementsGroup = presentationAnimationElementsGroup


    @property
    def presentation_AnimationGroupType59(self):
        return self.__presentation_AnimationGroupType59

    @presentation_AnimationGroupType59.setter
    def presentation_AnimationGroupType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AnimationGroupType__presentation_AnimationGroupType59", None)
        self.__presentation_AnimationGroupType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_DocumentRoot58"):
                opp_val = getattr(old_value, "presentation_DocumentRoot58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_DocumentRoot58"):
                opp_val = getattr(value, "presentation_DocumentRoot58", None)
                if opp_val is None:
                    setattr(value, "presentation_DocumentRoot58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_AnimationGroupType5(self):
        return self.__presentation_AnimationGroupType5

    @presentation_AnimationGroupType5.setter
    def presentation_AnimationGroupType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AnimationGroupType__presentation_AnimationGroupType5", None)
        self.__presentation_AnimationGroupType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentation_AnimationsType14"):
                opp_val = getattr(old_value, "presentation_AnimationsType14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentation_AnimationsType14"):
                opp_val = getattr(value, "presentation_AnimationsType14", None)
                if opp_val is None:
                    setattr(value, "presentation_AnimationsType14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def presentation_AnimationGroupType(self):
        return self.__presentation_AnimationGroupType

    @presentation_AnimationGroupType.setter
    def presentation_AnimationGroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_presentation_AnimationGroupType__presentation_AnimationGroupType", None)
        self.__presentation_AnimationGroupType = value if value is not None else set()
        
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
                    
