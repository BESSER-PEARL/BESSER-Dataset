from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TimingType(Enum):
    DelayUntilStart = "DelayUntilStart"
    Interval = "Interval"


############################################
# Definition of Classes
############################################

class Arc:

    pass
class guigraph_InhibitorArc(Arc):

    pass
class guigraph_StandardArc(Arc):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class ITimeConsumer:

    pass
class guigraph_PreGenerationSequence:

    pass
class Transition:

    pass
class guigraph_TimerTransition(Transition):

    def __init__(self, duration: int, guigraph_TimerTransition: "ITimeConsumer" = None):
        self.duration = duration
        self.guigraph_TimerTransition = guigraph_TimerTransition
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def guigraph_TimerTransition(self):
        return self.__guigraph_TimerTransition

    @guigraph_TimerTransition.setter
    def guigraph_TimerTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_TimerTransition__guigraph_TimerTransition", None)
        self.__guigraph_TimerTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ITimeConsumer"):
                opp_val = getattr(old_value, "ITimeConsumer", None)
                if opp_val == self:
                    setattr(old_value, "ITimeConsumer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ITimeConsumer"):
                opp_val = getattr(value, "ITimeConsumer", None)
                setattr(value, "ITimeConsumer", self)

class guigraph_PageTransition(Transition):

    pass
class guigraph_ConditionActionTransition(Transition):

    def __init__(self, applicationConditionText: str, actionsText: str, guigraph_ConditionActionTransition: "Predicate" = None, guigraph_ConditionActionTransition10: "guigraph_PreGenerationSequence" = None):
        self.applicationConditionText = applicationConditionText
        self.actionsText = actionsText
        self.guigraph_ConditionActionTransition = guigraph_ConditionActionTransition
        self.guigraph_ConditionActionTransition10 = guigraph_ConditionActionTransition10
        
    @property
    def actionsText(self) -> str:
        return self.__actionsText

    @actionsText.setter
    def actionsText(self, actionsText: str):
        self.__actionsText = actionsText

    @property
    def applicationConditionText(self) -> str:
        return self.__applicationConditionText

    @applicationConditionText.setter
    def applicationConditionText(self, applicationConditionText: str):
        self.__applicationConditionText = applicationConditionText

    @property
    def guigraph_ConditionActionTransition(self):
        return self.__guigraph_ConditionActionTransition

    @guigraph_ConditionActionTransition.setter
    def guigraph_ConditionActionTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_ConditionActionTransition__guigraph_ConditionActionTransition", None)
        self.__guigraph_ConditionActionTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Predicate8"):
                opp_val = getattr(old_value, "Predicate8", None)
                if opp_val == self:
                    setattr(old_value, "Predicate8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Predicate8"):
                opp_val = getattr(value, "Predicate8", None)
                setattr(value, "Predicate8", self)

    @property
    def guigraph_ConditionActionTransition10(self):
        return self.__guigraph_ConditionActionTransition10

    @guigraph_ConditionActionTransition10.setter
    def guigraph_ConditionActionTransition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_ConditionActionTransition__guigraph_ConditionActionTransition10", None)
        self.__guigraph_ConditionActionTransition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guigraph_PreGenerationSequence"):
                opp_val = getattr(old_value, "guigraph_PreGenerationSequence", None)
                if opp_val == self:
                    setattr(old_value, "guigraph_PreGenerationSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guigraph_PreGenerationSequence"):
                opp_val = getattr(value, "guigraph_PreGenerationSequence", None)
                setattr(value, "guigraph_PreGenerationSequence", self)

class rules_IRealTimeConsumer:

    pass
class GuiGraphNode:

    pass
class guigraph_Place(GuiGraphNode):

    def __init__(self, initialTokens: int):
        self.initialTokens = initialTokens
        
    @property
    def initialTokens(self) -> int:
        return self.__initialTokens

    @initialTokens.setter
    def initialTokens(self, initialTokens: int):
        self.__initialTokens = initialTokens

class guigraph_Transition(rules_IRealTimeConsumer, GuiGraphNode):

    def __init__(self, rate: int, faultImpact: float, faultProbability: float, terminates: bool, timeMin: str, timeMax: str, timingType: str):
        self.rate = rate
        self.faultImpact = faultImpact
        self.faultProbability = faultProbability
        self.terminates = terminates
        self.timeMin = timeMin
        self.timeMax = timeMax
        self.timingType = timingType
        
    @property
    def timeMax(self) -> str:
        return self.__timeMax

    @timeMax.setter
    def timeMax(self, timeMax: str):
        self.__timeMax = timeMax

    @property
    def timeMin(self) -> str:
        return self.__timeMin

    @timeMin.setter
    def timeMin(self, timeMin: str):
        self.__timeMin = timeMin

    @property
    def faultImpact(self) -> float:
        return self.__faultImpact

    @faultImpact.setter
    def faultImpact(self, faultImpact: float):
        self.__faultImpact = faultImpact

    @property
    def rate(self) -> int:
        return self.__rate

    @rate.setter
    def rate(self, rate: int):
        self.__rate = rate

    @property
    def timingType(self) -> str:
        return self.__timingType

    @timingType.setter
    def timingType(self, timingType: str):
        self.__timingType = timingType

    @property
    def terminates(self) -> bool:
        return self.__terminates

    @terminates.setter
    def terminates(self, terminates: bool):
        self.__terminates = terminates

    @property
    def faultProbability(self) -> float:
        return self.__faultProbability

    @faultProbability.setter
    def faultProbability(self, faultProbability: float):
        self.__faultProbability = faultProbability

class Place:

    pass
class guigraph_NoWidgetNode(Place):

    pass
class Widget:

    pass
class guigraph_Form(Widget, Place):

    pass
class GuiGraph:

    pass
class guigraph_Page(GuiGraph):

    pass
class Predicate:

    pass
class AbstractModelElement:

    pass
class guigraph_Arc(AbstractModelElement):

    pass
class guigraph_GuiGraphNode(AbstractModelElement):

    pass
class guigraph_Widget(AbstractModelElement):

    def __init__(self, image: str, guigraph_Widget: "guigraph_Widget" = None, guigraph_Widget5: set["guigraph_Widget"] = None):
        self.image = image
        self.guigraph_Widget = guigraph_Widget
        self.guigraph_Widget5 = guigraph_Widget5 if guigraph_Widget5 is not None else set()
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def guigraph_Widget(self):
        return self.__guigraph_Widget

    @guigraph_Widget.setter
    def guigraph_Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_Widget__guigraph_Widget", None)
        self.__guigraph_Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guigraph_Widget5"):
                opp_val = getattr(old_value, "guigraph_Widget5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guigraph_Widget5"):
                opp_val = getattr(value, "guigraph_Widget5", None)
                if opp_val is None:
                    setattr(value, "guigraph_Widget5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def guigraph_Widget5(self):
        return self.__guigraph_Widget5

    @guigraph_Widget5.setter
    def guigraph_Widget5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_Widget__guigraph_Widget5", None)
        self.__guigraph_Widget5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "guigraph_Widget"):
                    opp_val = getattr(item, "guigraph_Widget", None)
                    
                    if opp_val == self:
                        setattr(item, "guigraph_Widget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "guigraph_Widget"):
                    opp_val = getattr(item, "guigraph_Widget", None)
                    
                    setattr(item, "guigraph_Widget", self)
                    

class guigraph_GuiGraph(AbstractModelElement):

    def __init__(self, invariantText: str, guigraph_GuiGraph: set["guigraph_Arc"] = None, guigraph_GuiGraph2: set["guigraph_GuiGraphNode"] = None, guigraph_GuiGraph4: "Predicate" = None):
        self.invariantText = invariantText
        self.guigraph_GuiGraph = guigraph_GuiGraph if guigraph_GuiGraph is not None else set()
        self.guigraph_GuiGraph2 = guigraph_GuiGraph2 if guigraph_GuiGraph2 is not None else set()
        self.guigraph_GuiGraph4 = guigraph_GuiGraph4
        
    @property
    def invariantText(self) -> str:
        return self.__invariantText

    @invariantText.setter
    def invariantText(self, invariantText: str):
        self.__invariantText = invariantText

    @property
    def guigraph_GuiGraph4(self):
        return self.__guigraph_GuiGraph4

    @guigraph_GuiGraph4.setter
    def guigraph_GuiGraph4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_GuiGraph__guigraph_GuiGraph4", None)
        self.__guigraph_GuiGraph4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Predicate"):
                opp_val = getattr(old_value, "Predicate", None)
                if opp_val == self:
                    setattr(old_value, "Predicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Predicate"):
                opp_val = getattr(value, "Predicate", None)
                setattr(value, "Predicate", self)

    @property
    def guigraph_GuiGraph2(self):
        return self.__guigraph_GuiGraph2

    @guigraph_GuiGraph2.setter
    def guigraph_GuiGraph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_GuiGraph__guigraph_GuiGraph2", None)
        self.__guigraph_GuiGraph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "guigraph_GuiGraphNode"):
                    opp_val = getattr(item, "guigraph_GuiGraphNode", None)
                    
                    if opp_val == self:
                        setattr(item, "guigraph_GuiGraphNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "guigraph_GuiGraphNode"):
                    opp_val = getattr(item, "guigraph_GuiGraphNode", None)
                    
                    setattr(item, "guigraph_GuiGraphNode", self)
                    

    @property
    def guigraph_GuiGraph(self):
        return self.__guigraph_GuiGraph

    @guigraph_GuiGraph.setter
    def guigraph_GuiGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_guigraph_GuiGraph__guigraph_GuiGraph", None)
        self.__guigraph_GuiGraph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "guigraph_Arc"):
                    opp_val = getattr(item, "guigraph_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "guigraph_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "guigraph_Arc"):
                    opp_val = getattr(item, "guigraph_Arc", None)
                    
                    setattr(item, "guigraph_Arc", self)
                    
