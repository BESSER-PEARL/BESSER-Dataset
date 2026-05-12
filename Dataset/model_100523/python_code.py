from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class ObjectNodeOrderingKind(Enum):
    LIFO = "LIFO"
    FIFO = "FIFO"
    unordered = "unordered"
    ordered = "ordered"
class ParameterDirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
    return_ = "return_"
class MessageSort(Enum):
    reply = "reply"
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
class ConnectorKind(Enum):
    assembly = "assembly"
    delegation = "delegation"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class MessageKind(Enum):
    complete = "complete"
    lost = "lost"
    found = "found"
    unknown = "unknown"
class InteractionOperatorKind(Enum):
    opt = "opt"
    break_ = "break_"
    seq = "seq"
    alt = "alt"
    par = "par"
    strict = "strict"
    loop = "loop"
    critical = "critical"
    neg = "neg"
    assert_ = "assert_"
    ignore = "ignore"
    consider = "consider"
class ExpansionKind(Enum):
    stream = "stream"
    parallel = "parallel"
    iterative = "iterative"
class PseudostateKind(Enum):
    terminate = "terminate"
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"


############################################
# Definition of Classes
############################################

class DirectedRelationship:

    pass
class BehavioredClassifier:

    pass
class umluseCases_Actor(BehavioredClassifier):

    def __init__(self):
        
        pass
    def must_have_name(self, umluseCases_diagnostics, umluseCases_context) :
        # TODO: Implement must_have_name method
        pass

    def associations(self, umluseCases_context, umluseCases_diagnostics) :
        # TODO: Implement associations method
        pass

class Classifier:

    pass
class umluseCases_BehavioredClassifier(Classifier):

    pass
class umluseCases_UseCase(BehavioredClassifier):

    def __init__(self, umluseCases_UseCase: "umluseCases_Classifier" = None, UseCase: "umluseCases_Classifier" = None, includingCase: set["umluseCases_Include"] = None, extension: set["umluseCases_Extend"] = None, useCase: set["umluseCases_ExtensionPoint"] = None, useCase36: set["umluseCases_Classifier"] = None, umluseCases_UseCase38: "umluseCases_Include" = None, UseCase46: "umluseCases_Extend" = None, UseCase40: "umluseCases_Include" = None, umluseCases_UseCase42: "umluseCases_Extend" = None, UseCase48: "umluseCases_ExtensionPoint" = None):
        self.umluseCases_UseCase = umluseCases_UseCase
        self.UseCase = UseCase
        self.includingCase = includingCase if includingCase is not None else set()
        self.extension = extension if extension is not None else set()
        self.useCase = useCase if useCase is not None else set()
        self.useCase36 = useCase36 if useCase36 is not None else set()
        self.umluseCases_UseCase38 = umluseCases_UseCase38
        self.UseCase46 = UseCase46
        self.UseCase40 = UseCase40
        self.umluseCases_UseCase42 = umluseCases_UseCase42
        self.UseCase48 = UseCase48
        
        pass
    @property
    def umluseCases_UseCase42(self):
        return self.__umluseCases_UseCase42

    @umluseCases_UseCase42.setter
    def umluseCases_UseCase42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__umluseCases_UseCase42", None)
        self.__umluseCases_UseCase42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Extend"):
                opp_val = getattr(old_value, "umluseCases_Extend", None)
                if opp_val == self:
                    setattr(old_value, "umluseCases_Extend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Extend"):
                opp_val = getattr(value, "umluseCases_Extend", None)
                setattr(value, "umluseCases_Extend", self)

    @property
    def UseCase46(self):
        return self.__UseCase46

    @UseCase46.setter
    def UseCase46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__UseCase46", None)
        self.__UseCase46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extend"):
                opp_val = getattr(old_value, "extend", None)
                if opp_val == self:
                    setattr(old_value, "extend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extend"):
                opp_val = getattr(value, "extend", None)
                setattr(value, "extend", self)

    @property
    def useCase36(self):
        return self.__useCase36

    @useCase36.setter
    def useCase36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__useCase36", None)
        self.__useCase36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

    @property
    def UseCase48(self):
        return self.__UseCase48

    @UseCase48.setter
    def UseCase48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__UseCase48", None)
        self.__UseCase48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensionPoint"):
                opp_val = getattr(old_value, "extensionPoint", None)
                if opp_val == self:
                    setattr(old_value, "extensionPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensionPoint"):
                opp_val = getattr(value, "extensionPoint", None)
                setattr(value, "extensionPoint", self)

    @property
    def UseCase40(self):
        return self.__UseCase40

    @UseCase40.setter
    def UseCase40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__UseCase40", None)
        self.__UseCase40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "include"):
                opp_val = getattr(old_value, "include", None)
                if opp_val == self:
                    setattr(old_value, "include", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "include"):
                opp_val = getattr(value, "include", None)
                setattr(value, "include", self)

    @property
    def umluseCases_UseCase38(self):
        return self.__umluseCases_UseCase38

    @umluseCases_UseCase38.setter
    def umluseCases_UseCase38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__umluseCases_UseCase38", None)
        self.__umluseCases_UseCase38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Include"):
                opp_val = getattr(old_value, "umluseCases_Include", None)
                if opp_val == self:
                    setattr(old_value, "umluseCases_Include", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Include"):
                opp_val = getattr(value, "umluseCases_Include", None)
                setattr(value, "umluseCases_Include", self)

    @property
    def useCase(self):
        return self.__useCase

    @useCase.setter
    def useCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__useCase", None)
        self.__useCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionPoint"):
                    opp_val = getattr(item, "ExtensionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionPoint"):
                    opp_val = getattr(item, "ExtensionPoint", None)
                    
                    setattr(item, "ExtensionPoint", self)
                    

    @property
    def umluseCases_UseCase(self):
        return self.__umluseCases_UseCase

    @umluseCases_UseCase.setter
    def umluseCases_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__umluseCases_UseCase", None)
        self.__umluseCases_UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Classifier25"):
                opp_val = getattr(old_value, "umluseCases_Classifier25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Classifier25"):
                opp_val = getattr(value, "umluseCases_Classifier25", None)
                if opp_val is None:
                    setattr(value, "umluseCases_Classifier25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__extension", None)
        self.__extension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extend"):
                    opp_val = getattr(item, "Extend", None)
                    
                    if opp_val == self:
                        setattr(item, "Extend", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extend"):
                    opp_val = getattr(item, "Extend", None)
                    
                    setattr(item, "Extend", self)
                    

    @property
    def UseCase(self):
        return self.__UseCase

    @UseCase.setter
    def UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__UseCase", None)
        self.__UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subject"):
                opp_val = getattr(old_value, "subject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subject"):
                opp_val = getattr(value, "subject", None)
                if opp_val is None:
                    setattr(value, "subject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def includingCase(self):
        return self.__includingCase

    @includingCase.setter
    def includingCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_UseCase__includingCase", None)
        self.__includingCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Include"):
                    opp_val = getattr(item, "Include", None)
                    
                    if opp_val == self:
                        setattr(item, "Include", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Include"):
                    opp_val = getattr(item, "Include", None)
                    
                    setattr(item, "Include", self)
                    

    def allIncludedUseCases(self) :
        # TODO: Implement allIncludedUseCases method
        pass

    def binary_associations(self, umluseCases_context, umluseCases_diagnostics) :
        # TODO: Implement binary_associations method
        pass

    def must_have_name(self, umluseCases_context, umluseCases_diagnostics) :
        # TODO: Implement must_have_name method
        pass

    def no_association_to_use_case(self, umluseCases_diagnostics, umluseCases_context) :
        # TODO: Implement no_association_to_use_case method
        pass

    def cannot_include_self(self, umluseCases_context, umluseCases_diagnostics) :
        # TODO: Implement cannot_include_self method
        pass

class TemplateableElement:

    pass
class Type:

    pass
class RedefinableElement:

    pass
class umluseCases_ExtensionPoint(RedefinableElement):

    def __init__(self, ExtensionPoint: "umluseCases_UseCase" = None, umluseCases_ExtensionPoint: "umluseCases_Extend" = None, extensionPoint: "umluseCases_UseCase" = None):
        self.ExtensionPoint = ExtensionPoint
        self.umluseCases_ExtensionPoint = umluseCases_ExtensionPoint
        self.extensionPoint = extensionPoint
        
        pass
    @property
    def ExtensionPoint(self):
        return self.__ExtensionPoint

    @ExtensionPoint.setter
    def ExtensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_ExtensionPoint__ExtensionPoint", None)
        self.__ExtensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase"):
                opp_val = getattr(old_value, "useCase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase"):
                opp_val = getattr(value, "useCase", None)
                if opp_val is None:
                    setattr(value, "useCase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_ExtensionPoint(self):
        return self.__umluseCases_ExtensionPoint

    @umluseCases_ExtensionPoint.setter
    def umluseCases_ExtensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_ExtensionPoint__umluseCases_ExtensionPoint", None)
        self.__umluseCases_ExtensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Extend44"):
                opp_val = getattr(old_value, "umluseCases_Extend44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Extend44"):
                opp_val = getattr(value, "umluseCases_Extend44", None)
                if opp_val is None:
                    setattr(value, "umluseCases_Extend44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extensionPoint(self):
        return self.__extensionPoint

    @extensionPoint.setter
    def extensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_ExtensionPoint__extensionPoint", None)
        self.__extensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase48"):
                opp_val = getattr(old_value, "UseCase48", None)
                if opp_val == self:
                    setattr(old_value, "UseCase48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase48"):
                opp_val = getattr(value, "UseCase48", None)
                setattr(value, "UseCase48", self)

    def must_have_name(self, umluseCases_diagnostics, umluseCases_context) :
        # TODO: Implement must_have_name method
        pass

class Namespace:

    pass
class umluseCases_Classifier(Type, TemplateableElement, RedefinableElement, Namespace):

    def __init__(self, isAbstract: str, umluseCases_Classifier: set["umluseCases_NamedElement"] = None, umluseCases_Classifier20: "umluseCases_Classifier" = None, umluseCases_Classifier18: set["umluseCases_Classifier"] = None, umluseCases_Classifier23: "umluseCases_Classifier" = None, umluseCases_Classifier21: set["umluseCases_Classifier"] = None, umluseCases_Classifier25: set["umluseCases_UseCase"] = None, subject: set["umluseCases_UseCase"] = None, umluseCases_Classifier31: "umluseCases_RedefinableElement" = None, Classifier: "umluseCases_UseCase" = None):
        self.isAbstract = isAbstract
        self.umluseCases_Classifier = umluseCases_Classifier if umluseCases_Classifier is not None else set()
        self.umluseCases_Classifier20 = umluseCases_Classifier20
        self.umluseCases_Classifier18 = umluseCases_Classifier18 if umluseCases_Classifier18 is not None else set()
        self.umluseCases_Classifier23 = umluseCases_Classifier23
        self.umluseCases_Classifier21 = umluseCases_Classifier21 if umluseCases_Classifier21 is not None else set()
        self.umluseCases_Classifier25 = umluseCases_Classifier25 if umluseCases_Classifier25 is not None else set()
        self.subject = subject if subject is not None else set()
        self.umluseCases_Classifier31 = umluseCases_Classifier31
        self.Classifier = Classifier
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def umluseCases_Classifier23(self):
        return self.__umluseCases_Classifier23

    @umluseCases_Classifier23.setter
    def umluseCases_Classifier23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier23", None)
        self.__umluseCases_Classifier23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Classifier21"):
                opp_val = getattr(old_value, "umluseCases_Classifier21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Classifier21"):
                opp_val = getattr(value, "umluseCases_Classifier21", None)
                if opp_val is None:
                    setattr(value, "umluseCases_Classifier21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_Classifier25(self):
        return self.__umluseCases_Classifier25

    @umluseCases_Classifier25.setter
    def umluseCases_Classifier25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier25", None)
        self.__umluseCases_Classifier25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_UseCase"):
                    opp_val = getattr(item, "umluseCases_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_UseCase"):
                    opp_val = getattr(item, "umluseCases_UseCase", None)
                    
                    setattr(item, "umluseCases_UseCase", self)
                    

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase36"):
                opp_val = getattr(old_value, "useCase36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase36"):
                opp_val = getattr(value, "useCase36", None)
                if opp_val is None:
                    setattr(value, "useCase36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_Classifier(self):
        return self.__umluseCases_Classifier

    @umluseCases_Classifier.setter
    def umluseCases_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier", None)
        self.__umluseCases_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_NamedElement17"):
                    opp_val = getattr(item, "umluseCases_NamedElement17", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_NamedElement17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_NamedElement17"):
                    opp_val = getattr(item, "umluseCases_NamedElement17", None)
                    
                    setattr(item, "umluseCases_NamedElement17", self)
                    

    @property
    def umluseCases_Classifier21(self):
        return self.__umluseCases_Classifier21

    @umluseCases_Classifier21.setter
    def umluseCases_Classifier21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier21", None)
        self.__umluseCases_Classifier21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_Classifier23"):
                    opp_val = getattr(item, "umluseCases_Classifier23", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_Classifier23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_Classifier23"):
                    opp_val = getattr(item, "umluseCases_Classifier23", None)
                    
                    setattr(item, "umluseCases_Classifier23", self)
                    

    @property
    def umluseCases_Classifier20(self):
        return self.__umluseCases_Classifier20

    @umluseCases_Classifier20.setter
    def umluseCases_Classifier20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier20", None)
        self.__umluseCases_Classifier20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Classifier18"):
                opp_val = getattr(old_value, "umluseCases_Classifier18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Classifier18"):
                opp_val = getattr(value, "umluseCases_Classifier18", None)
                if opp_val is None:
                    setattr(value, "umluseCases_Classifier18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_Classifier18(self):
        return self.__umluseCases_Classifier18

    @umluseCases_Classifier18.setter
    def umluseCases_Classifier18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier18", None)
        self.__umluseCases_Classifier18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_Classifier20"):
                    opp_val = getattr(item, "umluseCases_Classifier20", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_Classifier20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_Classifier20"):
                    opp_val = getattr(item, "umluseCases_Classifier20", None)
                    
                    setattr(item, "umluseCases_Classifier20", self)
                    

    @property
    def umluseCases_Classifier31(self):
        return self.__umluseCases_Classifier31

    @umluseCases_Classifier31.setter
    def umluseCases_Classifier31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__umluseCases_Classifier31", None)
        self.__umluseCases_Classifier31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_RedefinableElement30"):
                opp_val = getattr(old_value, "umluseCases_RedefinableElement30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_RedefinableElement30"):
                opp_val = getattr(value, "umluseCases_RedefinableElement30", None)
                if opp_val is None:
                    setattr(value, "umluseCases_RedefinableElement30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Classifier__subject", None)
        self.__subject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCase"):
                    opp_val = getattr(item, "UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCase"):
                    opp_val = getattr(item, "UseCase", None)
                    
                    setattr(item, "UseCase", self)
                    

class PackageableElement:

    pass
class umluseCases_Type(PackageableElement):

    pass
class Relationship:

    pass
class umluseCases_DirectedRelationship(Relationship):

    pass
class Element:

    pass
class umluseCases_ParameterableElement(Element):

    pass
class umluseCases_Relationship(Element):

    pass
class umluseCases_TemplateableElement(Element):

    pass
class umluseCases_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, umluseCases_NamedElement: "umluseCases_Namespace" = None, NamedElement: "umluseCases_Namespace" = None, umluseCases_NamedElement17: "umluseCases_Classifier" = None, ownedMember: "umluseCases_Namespace" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.umluseCases_NamedElement = umluseCases_NamedElement
        self.NamedElement = NamedElement
        self.umluseCases_NamedElement17 = umluseCases_NamedElement17
        self.ownedMember = ownedMember
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def umluseCases_NamedElement(self):
        return self.__umluseCases_NamedElement

    @umluseCases_NamedElement.setter
    def umluseCases_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_NamedElement__umluseCases_NamedElement", None)
        self.__umluseCases_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Namespace"):
                opp_val = getattr(old_value, "umluseCases_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Namespace"):
                opp_val = getattr(value, "umluseCases_Namespace", None)
                if opp_val is None:
                    setattr(value, "umluseCases_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_NamedElement17(self):
        return self.__umluseCases_NamedElement17

    @umluseCases_NamedElement17.setter
    def umluseCases_NamedElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_NamedElement__umluseCases_NamedElement17", None)
        self.__umluseCases_NamedElement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_Classifier"):
                opp_val = getattr(old_value, "umluseCases_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_Classifier"):
                opp_val = getattr(value, "umluseCases_Classifier", None)
                if opp_val is None:
                    setattr(value, "umluseCases_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_NamedElement__ownedMember", None)
        self.__ownedMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ParameterableElement:

    pass
class NamedElement:

    pass
class umluseCases_Extend(DirectedRelationship, NamedElement):

    def __init__(self, Extend: "umluseCases_UseCase" = None, extend: "umluseCases_UseCase" = None, umluseCases_Extend: "umluseCases_UseCase" = None, umluseCases_Extend44: set["umluseCases_ExtensionPoint"] = None):
        self.Extend = Extend
        self.extend = extend
        self.umluseCases_Extend = umluseCases_Extend
        self.umluseCases_Extend44 = umluseCases_Extend44 if umluseCases_Extend44 is not None else set()
        
        pass
    @property
    def Extend(self):
        return self.__Extend

    @Extend.setter
    def Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Extend__Extend", None)
        self.__Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extension"):
                opp_val = getattr(old_value, "extension", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extension"):
                opp_val = getattr(value, "extension", None)
                if opp_val is None:
                    setattr(value, "extension", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_Extend(self):
        return self.__umluseCases_Extend

    @umluseCases_Extend.setter
    def umluseCases_Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Extend__umluseCases_Extend", None)
        self.__umluseCases_Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_UseCase42"):
                opp_val = getattr(old_value, "umluseCases_UseCase42", None)
                if opp_val == self:
                    setattr(old_value, "umluseCases_UseCase42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_UseCase42"):
                opp_val = getattr(value, "umluseCases_UseCase42", None)
                setattr(value, "umluseCases_UseCase42", self)

    @property
    def extend(self):
        return self.__extend

    @extend.setter
    def extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Extend__extend", None)
        self.__extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase46"):
                opp_val = getattr(old_value, "UseCase46", None)
                if opp_val == self:
                    setattr(old_value, "UseCase46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase46"):
                opp_val = getattr(value, "UseCase46", None)
                setattr(value, "UseCase46", self)

    @property
    def umluseCases_Extend44(self):
        return self.__umluseCases_Extend44

    @umluseCases_Extend44.setter
    def umluseCases_Extend44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_Extend__umluseCases_Extend44", None)
        self.__umluseCases_Extend44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_ExtensionPoint"):
                    opp_val = getattr(item, "umluseCases_ExtensionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_ExtensionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_ExtensionPoint"):
                    opp_val = getattr(item, "umluseCases_ExtensionPoint", None)
                    
                    setattr(item, "umluseCases_ExtensionPoint", self)
                    

    def extension_points(self, umluseCases_diagnostics, umluseCases_context) :
        # TODO: Implement extension_points method
        pass

class umluseCases_Namespace(NamedElement):

    pass
class umluseCases_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, umluseCases_RedefinableElement30: set["umluseCases_Classifier"] = None, umluseCases_RedefinableElement: "umluseCases_RedefinableElement" = None, umluseCases_RedefinableElement27: set["umluseCases_RedefinableElement"] = None):
        self.isLeaf = isLeaf
        self.umluseCases_RedefinableElement30 = umluseCases_RedefinableElement30 if umluseCases_RedefinableElement30 is not None else set()
        self.umluseCases_RedefinableElement = umluseCases_RedefinableElement
        self.umluseCases_RedefinableElement27 = umluseCases_RedefinableElement27 if umluseCases_RedefinableElement27 is not None else set()
        
        pass
    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf


    @property
    def umluseCases_RedefinableElement30(self):
        return self.__umluseCases_RedefinableElement30

    @umluseCases_RedefinableElement30.setter
    def umluseCases_RedefinableElement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_RedefinableElement__umluseCases_RedefinableElement30", None)
        self.__umluseCases_RedefinableElement30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_Classifier31"):
                    opp_val = getattr(item, "umluseCases_Classifier31", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_Classifier31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_Classifier31"):
                    opp_val = getattr(item, "umluseCases_Classifier31", None)
                    
                    setattr(item, "umluseCases_Classifier31", self)
                    

    @property
    def umluseCases_RedefinableElement(self):
        return self.__umluseCases_RedefinableElement

    @umluseCases_RedefinableElement.setter
    def umluseCases_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_RedefinableElement__umluseCases_RedefinableElement", None)
        self.__umluseCases_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umluseCases_RedefinableElement27"):
                opp_val = getattr(old_value, "umluseCases_RedefinableElement27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umluseCases_RedefinableElement27"):
                opp_val = getattr(value, "umluseCases_RedefinableElement27", None)
                if opp_val is None:
                    setattr(value, "umluseCases_RedefinableElement27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umluseCases_RedefinableElement27(self):
        return self.__umluseCases_RedefinableElement27

    @umluseCases_RedefinableElement27.setter
    def umluseCases_RedefinableElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umluseCases_RedefinableElement__umluseCases_RedefinableElement27", None)
        self.__umluseCases_RedefinableElement27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umluseCases_RedefinableElement"):
                    opp_val = getattr(item, "umluseCases_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "umluseCases_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umluseCases_RedefinableElement"):
                    opp_val = getattr(item, "umluseCases_RedefinableElement", None)
                    
                    setattr(item, "umluseCases_RedefinableElement", self)
                    

class umluseCases_Include(DirectedRelationship, NamedElement):

    pass
class umluseCases_PackageableElement(ParameterableElement, NamedElement):

    pass
class EModelElement:

    pass
class umluseCases_Element(EModelElement):

    pass