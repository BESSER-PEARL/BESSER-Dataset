from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TMessageExtremity:

    pass
class TSourceTargetMessageMapping:

    pass
class sequence_template_TDestructionMessageMapping(TSourceTargetMessageMapping):

    pass
class sequence_template_TBasicMessageMapping(TSourceTargetMessageMapping):

    pass
class sequence_template_TCreationMessageMapping(TSourceTargetMessageMapping):

    pass
class TBasicMessageMapping:

    pass
class TMessageStyle:

    pass
class TAbstractMapping:

    pass
class sequence_template_TMessageMapping(TAbstractMapping):

    def __init__(self, sendingEndFinderExpression: str, receivingEndFinderExpression: str, sequence_template_TMessageMapping: "TMessageStyle" = None, sequence_template_TMessageMapping78: set["TConditionalMessageStyle"] = None):
        self.sendingEndFinderExpression = sendingEndFinderExpression
        self.receivingEndFinderExpression = receivingEndFinderExpression
        self.sequence_template_TMessageMapping = sequence_template_TMessageMapping
        self.sequence_template_TMessageMapping78 = sequence_template_TMessageMapping78 if sequence_template_TMessageMapping78 is not None else set()
        
    @property
    def sendingEndFinderExpression(self) -> str:
        return self.__sendingEndFinderExpression

    @sendingEndFinderExpression.setter
    def sendingEndFinderExpression(self, sendingEndFinderExpression: str):
        self.__sendingEndFinderExpression = sendingEndFinderExpression

    @property
    def receivingEndFinderExpression(self) -> str:
        return self.__receivingEndFinderExpression

    @receivingEndFinderExpression.setter
    def receivingEndFinderExpression(self, receivingEndFinderExpression: str):
        self.__receivingEndFinderExpression = receivingEndFinderExpression

    @property
    def sequence_template_TMessageMapping78(self):
        return self.__sequence_template_TMessageMapping78

    @sequence_template_TMessageMapping78.setter
    def sequence_template_TMessageMapping78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TMessageMapping__sequence_template_TMessageMapping78", None)
        self.__sequence_template_TMessageMapping78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TConditionalMessageStyle"):
                    opp_val = getattr(item, "TConditionalMessageStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "TConditionalMessageStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TConditionalMessageStyle"):
                    opp_val = getattr(item, "TConditionalMessageStyle", None)
                    
                    setattr(item, "TConditionalMessageStyle", self)
                    

    @property
    def sequence_template_TMessageMapping(self):
        return self.__sequence_template_TMessageMapping

    @sequence_template_TMessageMapping.setter
    def sequence_template_TMessageMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TMessageMapping__sequence_template_TMessageMapping", None)
        self.__sequence_template_TMessageMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TMessageStyle"):
                opp_val = getattr(old_value, "TMessageStyle", None)
                if opp_val == self:
                    setattr(old_value, "TMessageStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TMessageStyle"):
                opp_val = getattr(value, "TMessageStyle", None)
                setattr(value, "TMessageStyle", self)

class TConditionalExecutionStyle:

    pass
class TExecutionStyle:

    pass
class TConditionalMessageStyle:

    pass
class ColorDescription:

    pass
class TConditionalLifelineStyle:

    pass
class TLifelineStyle:

    pass
class style_NodeStyleDescription:

    pass
class TExecutionMapping:

    pass
class template_TMessageExtremity:

    pass
class template_TAbstractMapping:

    pass
class sequence_template_TLifelineMapping(template_TAbstractMapping, template_TMessageExtremity):

    def __init__(self, eolVisibleExpression: str, sequence_template_TLifelineMapping: set["TExecutionMapping"] = None, sequence_template_TLifelineMapping52: "style_NodeStyleDescription" = None, sequence_template_TLifelineMapping54: "TLifelineStyle" = None, sequence_template_TLifelineMapping56: "style_NodeStyleDescription" = None, sequence_template_TLifelineMapping59: set["TConditionalLifelineStyle"] = None):
        self.eolVisibleExpression = eolVisibleExpression
        self.sequence_template_TLifelineMapping = sequence_template_TLifelineMapping if sequence_template_TLifelineMapping is not None else set()
        self.sequence_template_TLifelineMapping52 = sequence_template_TLifelineMapping52
        self.sequence_template_TLifelineMapping54 = sequence_template_TLifelineMapping54
        self.sequence_template_TLifelineMapping56 = sequence_template_TLifelineMapping56
        self.sequence_template_TLifelineMapping59 = sequence_template_TLifelineMapping59 if sequence_template_TLifelineMapping59 is not None else set()
        
    @property
    def eolVisibleExpression(self) -> str:
        return self.__eolVisibleExpression

    @eolVisibleExpression.setter
    def eolVisibleExpression(self, eolVisibleExpression: str):
        self.__eolVisibleExpression = eolVisibleExpression

    @property
    def sequence_template_TLifelineMapping52(self):
        return self.__sequence_template_TLifelineMapping52

    @sequence_template_TLifelineMapping52.setter
    def sequence_template_TLifelineMapping52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TLifelineMapping__sequence_template_TLifelineMapping52", None)
        self.__sequence_template_TLifelineMapping52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_NodeStyleDescription"):
                opp_val = getattr(old_value, "style_NodeStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_NodeStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_NodeStyleDescription"):
                opp_val = getattr(value, "style_NodeStyleDescription", None)
                setattr(value, "style_NodeStyleDescription", self)

    @property
    def sequence_template_TLifelineMapping(self):
        return self.__sequence_template_TLifelineMapping

    @sequence_template_TLifelineMapping.setter
    def sequence_template_TLifelineMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TLifelineMapping__sequence_template_TLifelineMapping", None)
        self.__sequence_template_TLifelineMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TExecutionMapping"):
                    opp_val = getattr(item, "TExecutionMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "TExecutionMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TExecutionMapping"):
                    opp_val = getattr(item, "TExecutionMapping", None)
                    
                    setattr(item, "TExecutionMapping", self)
                    

    @property
    def sequence_template_TLifelineMapping54(self):
        return self.__sequence_template_TLifelineMapping54

    @sequence_template_TLifelineMapping54.setter
    def sequence_template_TLifelineMapping54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TLifelineMapping__sequence_template_TLifelineMapping54", None)
        self.__sequence_template_TLifelineMapping54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TLifelineStyle"):
                opp_val = getattr(old_value, "TLifelineStyle", None)
                if opp_val == self:
                    setattr(old_value, "TLifelineStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TLifelineStyle"):
                opp_val = getattr(value, "TLifelineStyle", None)
                setattr(value, "TLifelineStyle", self)

    @property
    def sequence_template_TLifelineMapping56(self):
        return self.__sequence_template_TLifelineMapping56

    @sequence_template_TLifelineMapping56.setter
    def sequence_template_TLifelineMapping56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TLifelineMapping__sequence_template_TLifelineMapping56", None)
        self.__sequence_template_TLifelineMapping56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_NodeStyleDescription57"):
                opp_val = getattr(old_value, "style_NodeStyleDescription57", None)
                if opp_val == self:
                    setattr(old_value, "style_NodeStyleDescription57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_NodeStyleDescription57"):
                opp_val = getattr(value, "style_NodeStyleDescription57", None)
                setattr(value, "style_NodeStyleDescription57", self)

    @property
    def sequence_template_TLifelineMapping59(self):
        return self.__sequence_template_TLifelineMapping59

    @sequence_template_TLifelineMapping59.setter
    def sequence_template_TLifelineMapping59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TLifelineMapping__sequence_template_TLifelineMapping59", None)
        self.__sequence_template_TLifelineMapping59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TConditionalLifelineStyle"):
                    opp_val = getattr(item, "TConditionalLifelineStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "TConditionalLifelineStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TConditionalLifelineStyle"):
                    opp_val = getattr(item, "TConditionalLifelineStyle", None)
                    
                    setattr(item, "TConditionalLifelineStyle", self)
                    

class sequence_template_TExecutionMapping(template_TAbstractMapping, template_TMessageExtremity):

    def __init__(self, startingEndFinderExpression: str, finishingEndFinderExpression: str, recursive: bool, sequence_template_TExecutionMapping: set["TExecutionMapping"] = None, sequence_template_TExecutionMapping66: "TExecutionStyle" = None, sequence_template_TExecutionMapping68: set["TConditionalExecutionStyle"] = None):
        self.startingEndFinderExpression = startingEndFinderExpression
        self.finishingEndFinderExpression = finishingEndFinderExpression
        self.recursive = recursive
        self.sequence_template_TExecutionMapping = sequence_template_TExecutionMapping if sequence_template_TExecutionMapping is not None else set()
        self.sequence_template_TExecutionMapping66 = sequence_template_TExecutionMapping66
        self.sequence_template_TExecutionMapping68 = sequence_template_TExecutionMapping68 if sequence_template_TExecutionMapping68 is not None else set()
        
    @property
    def recursive(self) -> bool:
        return self.__recursive

    @recursive.setter
    def recursive(self, recursive: bool):
        self.__recursive = recursive

    @property
    def startingEndFinderExpression(self) -> str:
        return self.__startingEndFinderExpression

    @startingEndFinderExpression.setter
    def startingEndFinderExpression(self, startingEndFinderExpression: str):
        self.__startingEndFinderExpression = startingEndFinderExpression

    @property
    def finishingEndFinderExpression(self) -> str:
        return self.__finishingEndFinderExpression

    @finishingEndFinderExpression.setter
    def finishingEndFinderExpression(self, finishingEndFinderExpression: str):
        self.__finishingEndFinderExpression = finishingEndFinderExpression

    @property
    def sequence_template_TExecutionMapping68(self):
        return self.__sequence_template_TExecutionMapping68

    @sequence_template_TExecutionMapping68.setter
    def sequence_template_TExecutionMapping68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TExecutionMapping__sequence_template_TExecutionMapping68", None)
        self.__sequence_template_TExecutionMapping68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TConditionalExecutionStyle"):
                    opp_val = getattr(item, "TConditionalExecutionStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "TConditionalExecutionStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TConditionalExecutionStyle"):
                    opp_val = getattr(item, "TConditionalExecutionStyle", None)
                    
                    setattr(item, "TConditionalExecutionStyle", self)
                    

    @property
    def sequence_template_TExecutionMapping66(self):
        return self.__sequence_template_TExecutionMapping66

    @sequence_template_TExecutionMapping66.setter
    def sequence_template_TExecutionMapping66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TExecutionMapping__sequence_template_TExecutionMapping66", None)
        self.__sequence_template_TExecutionMapping66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TExecutionStyle"):
                opp_val = getattr(old_value, "TExecutionStyle", None)
                if opp_val == self:
                    setattr(old_value, "TExecutionStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TExecutionStyle"):
                opp_val = getattr(value, "TExecutionStyle", None)
                setattr(value, "TExecutionStyle", self)

    @property
    def sequence_template_TExecutionMapping(self):
        return self.__sequence_template_TExecutionMapping

    @sequence_template_TExecutionMapping.setter
    def sequence_template_TExecutionMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TExecutionMapping__sequence_template_TExecutionMapping", None)
        self.__sequence_template_TExecutionMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TExecutionMapping64"):
                    opp_val = getattr(item, "TExecutionMapping64", None)
                    
                    if opp_val == self:
                        setattr(item, "TExecutionMapping64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TExecutionMapping64"):
                    opp_val = getattr(item, "TExecutionMapping64", None)
                    
                    setattr(item, "TExecutionMapping64", self)
                    

class TTransformer:

    pass
class sequence_template_TConditionalLifelineStyle(TTransformer):

    def __init__(self, predicateExpression: str, sequence_template_TConditionalLifelineStyle: "TLifelineStyle" = None):
        self.predicateExpression = predicateExpression
        self.sequence_template_TConditionalLifelineStyle = sequence_template_TConditionalLifelineStyle
        
    @property
    def predicateExpression(self) -> str:
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression

    @property
    def sequence_template_TConditionalLifelineStyle(self):
        return self.__sequence_template_TConditionalLifelineStyle

    @sequence_template_TConditionalLifelineStyle.setter
    def sequence_template_TConditionalLifelineStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TConditionalLifelineStyle__sequence_template_TConditionalLifelineStyle", None)
        self.__sequence_template_TConditionalLifelineStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TLifelineStyle62"):
                opp_val = getattr(old_value, "TLifelineStyle62", None)
                if opp_val == self:
                    setattr(old_value, "TLifelineStyle62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TLifelineStyle62"):
                opp_val = getattr(value, "TLifelineStyle62", None)
                setattr(value, "TLifelineStyle62", self)

class sequence_template_TConditionalMessageStyle(TTransformer):

    def __init__(self, predicateExpression: str, sequence_template_TConditionalMessageStyle: "TMessageStyle" = None):
        self.predicateExpression = predicateExpression
        self.sequence_template_TConditionalMessageStyle = sequence_template_TConditionalMessageStyle
        
    @property
    def predicateExpression(self) -> str:
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression

    @property
    def sequence_template_TConditionalMessageStyle(self):
        return self.__sequence_template_TConditionalMessageStyle

    @sequence_template_TConditionalMessageStyle.setter
    def sequence_template_TConditionalMessageStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TConditionalMessageStyle__sequence_template_TConditionalMessageStyle", None)
        self.__sequence_template_TConditionalMessageStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TMessageStyle82"):
                opp_val = getattr(old_value, "TMessageStyle82", None)
                if opp_val == self:
                    setattr(old_value, "TMessageStyle82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TMessageStyle82"):
                opp_val = getattr(value, "TMessageStyle82", None)
                setattr(value, "TMessageStyle82", self)

class sequence_template_TLifelineStyle(TTransformer):

    def __init__(self, lifelineWidthComputationExpression: str, sequence_template_TLifelineStyle: "ColorDescription" = None):
        self.lifelineWidthComputationExpression = lifelineWidthComputationExpression
        self.sequence_template_TLifelineStyle = sequence_template_TLifelineStyle
        
    @property
    def lifelineWidthComputationExpression(self) -> str:
        return self.__lifelineWidthComputationExpression

    @lifelineWidthComputationExpression.setter
    def lifelineWidthComputationExpression(self, lifelineWidthComputationExpression: str):
        self.__lifelineWidthComputationExpression = lifelineWidthComputationExpression

    @property
    def sequence_template_TLifelineStyle(self):
        return self.__sequence_template_TLifelineStyle

    @sequence_template_TLifelineStyle.setter
    def sequence_template_TLifelineStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TLifelineStyle__sequence_template_TLifelineStyle", None)
        self.__sequence_template_TLifelineStyle = value
        
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

class sequence_template_TMessageStyle(TTransformer):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, labelExpression: str, sequence_template_TMessageStyle: "ColorDescription" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.labelExpression = labelExpression
        self.sequence_template_TMessageStyle = sequence_template_TMessageStyle
        
    @property
    def labelExpression(self) -> str:
        return self.__labelExpression

    @labelExpression.setter
    def labelExpression(self, labelExpression: str):
        self.__labelExpression = labelExpression

    @property
    def targetArrow(self) -> str:
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def sourceArrow(self) -> str:
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow

    @property
    def sequence_template_TMessageStyle(self):
        return self.__sequence_template_TMessageStyle

    @sequence_template_TMessageStyle.setter
    def sequence_template_TMessageStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TMessageStyle__sequence_template_TMessageStyle", None)
        self.__sequence_template_TMessageStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription80"):
                opp_val = getattr(old_value, "ColorDescription80", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription80"):
                opp_val = getattr(value, "ColorDescription80", None)
                setattr(value, "ColorDescription80", self)

class sequence_template_TConditionalExecutionStyle(TTransformer):

    def __init__(self, predicateExpression: str, sequence_template_TConditionalExecutionStyle: "TExecutionStyle" = None):
        self.predicateExpression = predicateExpression
        self.sequence_template_TConditionalExecutionStyle = sequence_template_TConditionalExecutionStyle
        
    @property
    def predicateExpression(self) -> str:
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression

    @property
    def sequence_template_TConditionalExecutionStyle(self):
        return self.__sequence_template_TConditionalExecutionStyle

    @sequence_template_TConditionalExecutionStyle.setter
    def sequence_template_TConditionalExecutionStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TConditionalExecutionStyle__sequence_template_TConditionalExecutionStyle", None)
        self.__sequence_template_TConditionalExecutionStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TExecutionStyle75"):
                opp_val = getattr(old_value, "TExecutionStyle75", None)
                if opp_val == self:
                    setattr(old_value, "TExecutionStyle75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TExecutionStyle75"):
                opp_val = getattr(value, "TExecutionStyle75", None)
                setattr(value, "TExecutionStyle75", self)

class sequence_template_TExecutionStyle(TTransformer):

    def __init__(self, borderSizeComputationExpression: str, sequence_template_TExecutionStyle: "ColorDescription" = None, sequence_template_TExecutionStyle72: "ColorDescription" = None):
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.sequence_template_TExecutionStyle = sequence_template_TExecutionStyle
        self.sequence_template_TExecutionStyle72 = sequence_template_TExecutionStyle72
        
    @property
    def borderSizeComputationExpression(self) -> str:
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression

    @property
    def sequence_template_TExecutionStyle(self):
        return self.__sequence_template_TExecutionStyle

    @sequence_template_TExecutionStyle.setter
    def sequence_template_TExecutionStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TExecutionStyle__sequence_template_TExecutionStyle", None)
        self.__sequence_template_TExecutionStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription70"):
                opp_val = getattr(old_value, "ColorDescription70", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription70"):
                opp_val = getattr(value, "ColorDescription70", None)
                setattr(value, "ColorDescription70", self)

    @property
    def sequence_template_TExecutionStyle72(self):
        return self.__sequence_template_TExecutionStyle72

    @sequence_template_TExecutionStyle72.setter
    def sequence_template_TExecutionStyle72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TExecutionStyle__sequence_template_TExecutionStyle72", None)
        self.__sequence_template_TExecutionStyle72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription73"):
                opp_val = getattr(old_value, "ColorDescription73", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription73"):
                opp_val = getattr(value, "ColorDescription73", None)
                setattr(value, "ColorDescription73", self)

class sequence_template_TAbstractMapping(TTransformer):

    def __init__(self, name: str, domainClass: str, semanticCandidatesExpression: str):
        self.name = name
        self.domainClass = domainClass
        self.semanticCandidatesExpression = semanticCandidatesExpression
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class template_sequence_EObject:

    pass
class sequence_template_TTransformer:

    pass
class sequence_ordering_InstanceRolesOrdering:

    pass
class SingleEventEnd:

    pass
class ordering_sequence_EObject:

    pass
class sequence_ordering_EventEnd(ABC):

    pass
class sequence_template_TMessageExtremity(ABC):

    pass
class TMessageMapping:

    pass
class sequence_template_TSourceTargetMessageMapping(TMessageMapping):

    def __init__(self, useDomainElement: bool, sourceFinderExpression: str, targetFinderExpression: str, sequence_template_TSourceTargetMessageMapping: set["TMessageExtremity"] = None, TMessageMapping: "sequence_template_TSequenceDiagram"):
        self.useDomainElement = useDomainElement
        self.sourceFinderExpression = sourceFinderExpression
        self.targetFinderExpression = targetFinderExpression
        self.sequence_template_TSourceTargetMessageMapping = sequence_template_TSourceTargetMessageMapping if sequence_template_TSourceTargetMessageMapping is not None else set()
        
    @property
    def sourceFinderExpression(self) -> str:
        return self.__sourceFinderExpression

    @sourceFinderExpression.setter
    def sourceFinderExpression(self, sourceFinderExpression: str):
        self.__sourceFinderExpression = sourceFinderExpression

    @property
    def targetFinderExpression(self) -> str:
        return self.__targetFinderExpression

    @targetFinderExpression.setter
    def targetFinderExpression(self, targetFinderExpression: str):
        self.__targetFinderExpression = targetFinderExpression

    @property
    def useDomainElement(self) -> bool:
        return self.__useDomainElement

    @useDomainElement.setter
    def useDomainElement(self, useDomainElement: bool):
        self.__useDomainElement = useDomainElement

    @property
    def sequence_template_TSourceTargetMessageMapping(self):
        return self.__sequence_template_TSourceTargetMessageMapping

    @sequence_template_TSourceTargetMessageMapping.setter
    def sequence_template_TSourceTargetMessageMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TSourceTargetMessageMapping__sequence_template_TSourceTargetMessageMapping", None)
        self.__sequence_template_TSourceTargetMessageMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TMessageExtremity85"):
                    opp_val = getattr(item, "TMessageExtremity85", None)
                    
                    if opp_val == self:
                        setattr(item, "TMessageExtremity85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TMessageExtremity85"):
                    opp_val = getattr(item, "TMessageExtremity85", None)
                    
                    setattr(item, "TMessageExtremity85", self)
                    

class sequence_template_TReturnMessageMapping(TMessageMapping):

    def __init__(self, invocationMessageFinderExpression: str, sequence_template_TReturnMessageMapping: "TBasicMessageMapping" = None, TMessageMapping: "sequence_template_TSequenceDiagram"):
        self.invocationMessageFinderExpression = invocationMessageFinderExpression
        self.sequence_template_TReturnMessageMapping = sequence_template_TReturnMessageMapping
        
    @property
    def invocationMessageFinderExpression(self) -> str:
        return self.__invocationMessageFinderExpression

    @invocationMessageFinderExpression.setter
    def invocationMessageFinderExpression(self, invocationMessageFinderExpression: str):
        self.__invocationMessageFinderExpression = invocationMessageFinderExpression

    @property
    def sequence_template_TReturnMessageMapping(self):
        return self.__sequence_template_TReturnMessageMapping

    @sequence_template_TReturnMessageMapping.setter
    def sequence_template_TReturnMessageMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TReturnMessageMapping__sequence_template_TReturnMessageMapping", None)
        self.__sequence_template_TReturnMessageMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TBasicMessageMapping"):
                opp_val = getattr(old_value, "TBasicMessageMapping", None)
                if opp_val == self:
                    setattr(old_value, "TBasicMessageMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TBasicMessageMapping"):
                opp_val = getattr(value, "TBasicMessageMapping", None)
                setattr(value, "TBasicMessageMapping", self)

class TLifelineMapping:

    pass
class template_TTransformer:

    pass
class description_RepresentationTemplate:

    pass
class sequence_template_TSequenceDiagram(description_RepresentationTemplate, template_TTransformer):

    def __init__(self, domainClass: str, endsOrdering: str, sequence_template_TSequenceDiagram: set["TLifelineMapping"] = None, sequence_template_TSequenceDiagram49: set["TMessageMapping"] = None):
        self.domainClass = domainClass
        self.endsOrdering = endsOrdering
        self.sequence_template_TSequenceDiagram = sequence_template_TSequenceDiagram if sequence_template_TSequenceDiagram is not None else set()
        self.sequence_template_TSequenceDiagram49 = sequence_template_TSequenceDiagram49 if sequence_template_TSequenceDiagram49 is not None else set()
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def endsOrdering(self) -> str:
        return self.__endsOrdering

    @endsOrdering.setter
    def endsOrdering(self, endsOrdering: str):
        self.__endsOrdering = endsOrdering

    @property
    def sequence_template_TSequenceDiagram49(self):
        return self.__sequence_template_TSequenceDiagram49

    @sequence_template_TSequenceDiagram49.setter
    def sequence_template_TSequenceDiagram49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TSequenceDiagram__sequence_template_TSequenceDiagram49", None)
        self.__sequence_template_TSequenceDiagram49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TMessageMapping"):
                    opp_val = getattr(item, "TMessageMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "TMessageMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TMessageMapping"):
                    opp_val = getattr(item, "TMessageMapping", None)
                    
                    setattr(item, "TMessageMapping", self)
                    

    @property
    def sequence_template_TSequenceDiagram(self):
        return self.__sequence_template_TSequenceDiagram

    @sequence_template_TSequenceDiagram.setter
    def sequence_template_TSequenceDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_template_TSequenceDiagram__sequence_template_TSequenceDiagram", None)
        self.__sequence_template_TSequenceDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TLifelineMapping"):
                    opp_val = getattr(item, "TLifelineMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "TLifelineMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TLifelineMapping"):
                    opp_val = getattr(item, "TLifelineMapping", None)
                    
                    setattr(item, "TLifelineMapping", self)
                    

class InstanceRoleMapping:

    pass
class tool_InitialOperation:

    pass
class tool_AbstractToolDescription:

    pass
class tool_CoveringElementCreationTool:

    pass
class EventEnd:

    pass
class sequence_ordering_SingleEventEnd(EventEnd):

    def __init__(self, start: bool, sequence_ordering_SingleEventEnd: "ordering_sequence_EObject" = None, EventEnd: "sequence_ordering_EventEndsOrdering"):
        self.start = start
        self.sequence_ordering_SingleEventEnd = sequence_ordering_SingleEventEnd
        
    @property
    def start(self) -> bool:
        return self.__start

    @start.setter
    def start(self, start: bool):
        self.__start = start

    @property
    def sequence_ordering_SingleEventEnd(self):
        return self.__sequence_ordering_SingleEventEnd

    @sequence_ordering_SingleEventEnd.setter
    def sequence_ordering_SingleEventEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_ordering_SingleEventEnd__sequence_ordering_SingleEventEnd", None)
        self.__sequence_ordering_SingleEventEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordering_sequence_EObject42"):
                opp_val = getattr(old_value, "ordering_sequence_EObject42", None)
                if opp_val == self:
                    setattr(old_value, "ordering_sequence_EObject42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordering_sequence_EObject42"):
                opp_val = getattr(value, "ordering_sequence_EObject42", None)
                setattr(value, "ordering_sequence_EObject42", self)

class sequence_ordering_CompoundEventEnd(EventEnd):

    def __init__(self, sequence_ordering_CompoundEventEnd: set["SingleEventEnd"] = None, EventEnd: "sequence_ordering_EventEndsOrdering"):
        self.sequence_ordering_CompoundEventEnd = sequence_ordering_CompoundEventEnd if sequence_ordering_CompoundEventEnd is not None else set()
        
    @property
    def sequence_ordering_CompoundEventEnd(self):
        return self.__sequence_ordering_CompoundEventEnd

    @sequence_ordering_CompoundEventEnd.setter
    def sequence_ordering_CompoundEventEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sequence_ordering_CompoundEventEnd__sequence_ordering_CompoundEventEnd", None)
        self.__sequence_ordering_CompoundEventEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleEventEnd"):
                    opp_val = getattr(item, "SingleEventEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleEventEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleEventEnd"):
                    opp_val = getattr(item, "SingleEventEnd", None)
                    
                    setattr(item, "SingleEventEnd", self)
                    

    def getSemanticEvents(self) -> str:
        # TODO: Implement getSemanticEvents method
        pass

class ordering_sequence_SequenceDDiagram:

    pass
class sequence_ordering_EventEndsOrdering:

    pass
class tool_SequenceDiagramToolDescription:

    pass
class sequence_tool_InstanceRoleReorderTool(tool_AbstractToolDescription, tool_SequenceDiagramToolDescription):

    pass
class sequence_tool_ReorderTool(tool_AbstractToolDescription, tool_SequenceDiagramToolDescription):

    pass
class tool_NodeCreationDescription:

    pass
class sequence_tool_InstanceRoleCreationTool(tool_NodeCreationDescription, tool_SequenceDiagramToolDescription):

    pass
class CoveredLifelinesVariable:

    pass
class sequence_tool_CoveringElementCreationTool(ABC):

    pass
class MessageEndVariable:

    pass
class sequence_tool_OrderedElementCreationTool(ABC):

    pass
class sequence_tool_SequenceDiagramToolDescription:

    pass
class FrameMapping:

    pass
class sequence_description_CombinedFragmentMapping(FrameMapping):

    pass
class sequence_description_InteractionUseMapping(FrameMapping):

    pass
class description_ContainerMapping:

    pass
class tool_OrderedElementCreationTool:

    pass
class sequence_tool_ExecutionCreationTool(tool_NodeCreationDescription, tool_SequenceDiagramToolDescription, tool_OrderedElementCreationTool):

    pass
class sequence_tool_ObservationPointCreationTool(tool_NodeCreationDescription, tool_SequenceDiagramToolDescription, tool_OrderedElementCreationTool):

    pass
class sequence_tool_StateCreationTool(tool_NodeCreationDescription, tool_SequenceDiagramToolDescription, tool_OrderedElementCreationTool):

    pass
class tool_EdgeCreationDescription:

    pass
class sequence_tool_MessageCreationTool(tool_SequenceDiagramToolDescription, tool_EdgeCreationDescription, tool_OrderedElementCreationTool):

    pass
class tool_ContainerCreationDescription:

    pass
class sequence_tool_InteractionUseCreationTool(tool_CoveringElementCreationTool, tool_ContainerCreationDescription, tool_SequenceDiagramToolDescription, tool_OrderedElementCreationTool):

    pass
class sequence_tool_CombinedFragmentCreationTool(tool_CoveringElementCreationTool, tool_ContainerCreationDescription, tool_SequenceDiagramToolDescription, tool_OrderedElementCreationTool):

    pass
class sequence_tool_OperandCreationTool(tool_ContainerCreationDescription, tool_SequenceDiagramToolDescription, tool_OrderedElementCreationTool):

    pass
class sequence_tool_LifelineCreationTool(tool_ContainerCreationDescription, tool_SequenceDiagramToolDescription):

    pass
class tool_ElementVariable:

    pass
class description_EventMapping:

    pass
class description_EdgeMapping:

    pass
class sequence_description_MessageMapping(description_EventMapping, description_EdgeMapping):

    def __init__(self, receivingEndFinderExpression: str, sendingEndFinderExpression: str):
        self.receivingEndFinderExpression = receivingEndFinderExpression
        self.sendingEndFinderExpression = sendingEndFinderExpression
        
    @property
    def receivingEndFinderExpression(self) -> str:
        return self.__receivingEndFinderExpression

    @receivingEndFinderExpression.setter
    def receivingEndFinderExpression(self, receivingEndFinderExpression: str):
        self.__receivingEndFinderExpression = receivingEndFinderExpression

    @property
    def sendingEndFinderExpression(self) -> str:
        return self.__sendingEndFinderExpression

    @sendingEndFinderExpression.setter
    def sendingEndFinderExpression(self, sendingEndFinderExpression: str):
        self.__sendingEndFinderExpression = sendingEndFinderExpression

class description_DelimitedEventMapping:

    pass
class sequence_description_FrameMapping(description_DelimitedEventMapping, description_ContainerMapping):

    def __init__(self, coveredLifelinesExpression: str, centerLabelExpression: str):
        self.coveredLifelinesExpression = coveredLifelinesExpression
        self.centerLabelExpression = centerLabelExpression
        
    @property
    def centerLabelExpression(self) -> str:
        return self.__centerLabelExpression

    @centerLabelExpression.setter
    def centerLabelExpression(self, centerLabelExpression: str):
        self.__centerLabelExpression = centerLabelExpression

    @property
    def coveredLifelinesExpression(self) -> str:
        return self.__coveredLifelinesExpression

    @coveredLifelinesExpression.setter
    def coveredLifelinesExpression(self, coveredLifelinesExpression: str):
        self.__coveredLifelinesExpression = coveredLifelinesExpression

class sequence_description_OperandMapping(description_DelimitedEventMapping, description_ContainerMapping):

    pass
class description_NodeMapping:

    pass
class sequence_description_StateMapping(description_DelimitedEventMapping, description_NodeMapping):

    pass
class sequence_description_ExecutionMapping(description_DelimitedEventMapping, description_NodeMapping):

    pass
class EventMapping:

    pass
class sequence_description_DelimitedEventMapping(EventMapping):

    def __init__(self, startingEndFinderExpression: str, finishingEndFinderExpression: str, EventMapping: "sequence_tool_ReorderTool"):
        self.startingEndFinderExpression = startingEndFinderExpression
        self.finishingEndFinderExpression = finishingEndFinderExpression
        
    @property
    def finishingEndFinderExpression(self) -> str:
        return self.__finishingEndFinderExpression

    @finishingEndFinderExpression.setter
    def finishingEndFinderExpression(self, finishingEndFinderExpression: str):
        self.__finishingEndFinderExpression = finishingEndFinderExpression

    @property
    def startingEndFinderExpression(self) -> str:
        return self.__startingEndFinderExpression

    @startingEndFinderExpression.setter
    def startingEndFinderExpression(self, startingEndFinderExpression: str):
        self.__startingEndFinderExpression = startingEndFinderExpression

class sequence_description_EventMapping(ABC):

    pass
class NodeMapping:

    pass
class sequence_description_EndOfLifeMapping(NodeMapping):

    pass
class sequence_description_ObservationPointMapping(NodeMapping):

    pass
class sequence_description_InstanceRoleMapping(NodeMapping):

    pass
class DiagramDescription:

    pass
class sequence_description_SequenceDiagramDescription(DiagramDescription):

    def __init__(self, endsOrdering: str, instanceRolesOrdering: str):
        self.endsOrdering = endsOrdering
        self.instanceRolesOrdering = instanceRolesOrdering
        
    @property
    def instanceRolesOrdering(self) -> str:
        return self.__instanceRolesOrdering

    @instanceRolesOrdering.setter
    def instanceRolesOrdering(self, instanceRolesOrdering: str):
        self.__instanceRolesOrdering = instanceRolesOrdering

    @property
    def endsOrdering(self) -> str:
        return self.__endsOrdering

    @endsOrdering.setter
    def endsOrdering(self, endsOrdering: str):
        self.__endsOrdering = endsOrdering

class InstanceRolesOrdering:

    pass
class AbstractVariable:

    pass
class sequence_description_CoveredLifelinesVariable(AbstractVariable):

    pass
class sequence_description_MessageEndVariable(AbstractVariable):

    pass
class MessageMapping:

    pass
class sequence_description_DestructionMessageMapping(MessageMapping):

    pass
class sequence_description_CreationMessageMapping(MessageMapping):

    pass
class sequence_description_ReturnMessageMapping(MessageMapping):

    def __init__(self, invocationMessageFinderExpression: str):
        self.invocationMessageFinderExpression = invocationMessageFinderExpression
        
    @property
    def invocationMessageFinderExpression(self) -> str:
        return self.__invocationMessageFinderExpression

    @invocationMessageFinderExpression.setter
    def invocationMessageFinderExpression(self, invocationMessageFinderExpression: str):
        self.__invocationMessageFinderExpression = invocationMessageFinderExpression

class sequence_description_BasicMessageMapping(MessageMapping):

    pass
class EventEndsOrdering:

    pass
class DSemanticDiagram:

    pass
class sequence_SequenceDDiagram(DSemanticDiagram):

    pass