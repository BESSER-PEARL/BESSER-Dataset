from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ecore_Transition:

    def __init__(self, input: str, output: str, Transition: "ecore_State" = None, Transition118: "ecore_State" = None, outgoingTransition: "ecore_State" = None, incomingTransition: "ecore_State" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition118 = Transition118
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State125"):
                opp_val = getattr(old_value, "State125", None)
                if opp_val == self:
                    setattr(old_value, "State125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State125"):
                opp_val = getattr(value, "State125", None)
                setattr(value, "State125", self)

    @property
    def Transition118(self):
        return self.__Transition118

    @Transition118.setter
    def Transition118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__Transition118", None)
        self.__Transition118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State123"):
                opp_val = getattr(old_value, "State123", None)
                if opp_val == self:
                    setattr(old_value, "State123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State123"):
                opp_val = getattr(value, "State123", None)
                setattr(value, "State123", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecore_State:

    def __init__(self, name: str, State: "ecore_FSM" = None, ecore_State: "ecore_FSM" = None, ecore_State114: "ecore_FSM" = None, ownedState: "ecore_FSM" = None, source: set["ecore_Transition"] = None, target: set["ecore_Transition"] = None, ecore_State120: set["ecore_EClass"] = None, State123: "ecore_Transition" = None, State125: "ecore_Transition" = None):
        self.name = name
        self.State = State
        self.ecore_State = ecore_State
        self.ecore_State114 = ecore_State114
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.ecore_State120 = ecore_State120 if ecore_State120 is not None else set()
        self.State123 = State123
        self.State125 = State125
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecore_State(self):
        return self.__ecore_State

    @ecore_State.setter
    def ecore_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ecore_State", None)
        self.__ecore_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_FSM111"):
                opp_val = getattr(old_value, "ecore_FSM111", None)
                if opp_val == self:
                    setattr(old_value, "ecore_FSM111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_FSM111"):
                opp_val = getattr(value, "ecore_FSM111", None)
                setattr(value, "ecore_FSM111", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition118"):
                    opp_val = getattr(item, "Transition118", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition118"):
                    opp_val = getattr(item, "Transition118", None)
                    
                    setattr(item, "Transition118", self)
                    

    @property
    def State123(self):
        return self.__State123

    @State123.setter
    def State123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__State123", None)
        self.__State123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransition"):
                opp_val = getattr(old_value, "outgoingTransition", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransition"):
                opp_val = getattr(value, "outgoingTransition", None)
                setattr(value, "outgoingTransition", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_State120(self):
        return self.__ecore_State120

    @ecore_State120.setter
    def ecore_State120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ecore_State120", None)
        self.__ecore_State120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass121"):
                    opp_val = getattr(item, "ecore_EClass121", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass121"):
                    opp_val = getattr(item, "ecore_EClass121", None)
                    
                    setattr(item, "ecore_EClass121", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ownedState", None)
        self.__ownedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

    @property
    def State125(self):
        return self.__State125

    @State125.setter
    def State125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__State125", None)
        self.__State125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransition"):
                opp_val = getattr(old_value, "incomingTransition", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransition"):
                opp_val = getattr(value, "incomingTransition", None)
                setattr(value, "incomingTransition", self)

    @property
    def ecore_State114(self):
        return self.__ecore_State114

    @ecore_State114.setter
    def ecore_State114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ecore_State114", None)
        self.__ecore_State114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_FSM113"):
                opp_val = getattr(old_value, "ecore_FSM113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_FSM113"):
                opp_val = getattr(value, "ecore_FSM113", None)
                if opp_val is None:
                    setattr(value, "ecore_FSM113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ETypedElement:

    pass
class ecore_EParameter(ETypedElement):

    pass
class ecore_FSM:

    pass
class EDataType:

    pass
class ecore_EEnum(EDataType):

    def __init__(self, eEnum: set["ecore_EEnumLiteral"] = None, EEnum: "ecore_EEnumLiteral" = None):
        self.eEnum = eEnum if eEnum is not None else set()
        self.EEnum = EEnum
        
    @property
    def EEnum(self):
        return self.__EEnum

    @EEnum.setter
    def EEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnum__EEnum", None)
        self.__EEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eLiterals"):
                opp_val = getattr(old_value, "eLiterals", None)
                if opp_val == self:
                    setattr(old_value, "eLiterals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eLiterals"):
                opp_val = getattr(value, "eLiterals", None)
                setattr(value, "eLiterals", self)

    @property
    def eEnum(self):
        return self.__eEnum

    @eEnum.setter
    def eEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnum__eEnum", None)
        self.__eEnum = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EEnumLiteral"):
                    opp_val = getattr(item, "EEnumLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "EEnumLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EEnumLiteral"):
                    opp_val = getattr(item, "EEnumLiteral", None)
                    
                    setattr(item, "EEnumLiteral", self)
                    

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class ENamedElement:

    pass
class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, EPackage: "ecore_EClassifier" = None, EPackage47: "ecore_EFactory" = None, ePackage: "ecore_EFactory" = None, ePackage63: set["ecore_EClassifier"] = None, EPackage69: "ecore_EPackage" = None, eSubpackages: "ecore_EPackage" = None, EPackage66: "ecore_EPackage" = None, eSuperPackage: set["ecore_EPackage"] = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.EPackage = EPackage
        self.EPackage47 = EPackage47
        self.ePackage = ePackage
        self.ePackage63 = ePackage63 if ePackage63 is not None else set()
        self.EPackage69 = EPackage69
        self.eSubpackages = eSubpackages
        self.EPackage66 = EPackage66
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        
    @property
    def nsURI(self) -> str:
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI

    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def ePackage63(self):
        return self.__ePackage63

    @ePackage63.setter
    def ePackage63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage63", None)
        self.__ePackage63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "EClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    setattr(item, "EClassifier", self)
                    

    @property
    def EPackage66(self):
        return self.__EPackage66

    @EPackage66.setter
    def EPackage66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage66", None)
        self.__EPackage66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSuperPackage"):
                opp_val = getattr(old_value, "eSuperPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSuperPackage"):
                opp_val = getattr(value, "eSuperPackage", None)
                if opp_val is None:
                    setattr(value, "eSuperPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage69"):
                opp_val = getattr(old_value, "EPackage69", None)
                if opp_val == self:
                    setattr(old_value, "EPackage69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage69"):
                opp_val = getattr(value, "EPackage69", None)
                setattr(value, "EPackage69", self)

    @property
    def EPackage47(self):
        return self.__EPackage47

    @EPackage47.setter
    def EPackage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage47", None)
        self.__EPackage47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eFactoryInstance"):
                opp_val = getattr(old_value, "eFactoryInstance", None)
                if opp_val == self:
                    setattr(old_value, "eFactoryInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eFactoryInstance"):
                opp_val = getattr(value, "eFactoryInstance", None)
                setattr(value, "eFactoryInstance", self)

    @property
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EPackage66"):
                    opp_val = getattr(item, "EPackage66", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage66"):
                    opp_val = getattr(item, "EPackage66", None)
                    
                    setattr(item, "EPackage66", self)
                    

    @property
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage", None)
        self.__EPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eClassifiers"):
                opp_val = getattr(old_value, "eClassifiers", None)
                if opp_val == self:
                    setattr(old_value, "eClassifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eClassifiers"):
                opp_val = getattr(value, "eClassifiers", None)
                setattr(value, "eClassifiers", self)

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage", None)
        self.__ePackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFactory"):
                opp_val = getattr(old_value, "EFactory", None)
                if opp_val == self:
                    setattr(old_value, "EFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFactory"):
                opp_val = getattr(value, "EFactory", None)
                setattr(value, "EFactory", self)

    @property
    def EPackage69(self):
        return self.__EPackage69

    @EPackage69.setter
    def EPackage69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage69", None)
        self.__EPackage69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSubpackages"):
                opp_val = getattr(old_value, "eSubpackages", None)
                if opp_val == self:
                    setattr(old_value, "eSubpackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSubpackages"):
                opp_val = getattr(value, "eSubpackages", None)
                setattr(value, "eSubpackages", self)

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class ecore_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, ecore_ETypedElement: "ecore_EClassifier" = None, ecore_ETypedElement86: "ecore_EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement86 = ecore_ETypedElement86
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def ecore_ETypedElement86(self):
        return self.__ecore_ETypedElement86

    @ecore_ETypedElement86.setter
    def ecore_ETypedElement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement86", None)
        self.__ecore_ETypedElement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType87"):
                opp_val = getattr(old_value, "ecore_EGenericType87", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType87"):
                opp_val = getattr(value, "ecore_EGenericType87", None)
                setattr(value, "ecore_EGenericType87", self)

    @property
    def ecore_ETypedElement(self):
        return self.__ecore_ETypedElement

    @ecore_ETypedElement.setter
    def ecore_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement", None)
        self.__ecore_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClassifier84"):
                opp_val = getattr(old_value, "ecore_EClassifier84", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier84"):
                opp_val = getattr(value, "ecore_EClassifier84", None)
                setattr(value, "ecore_EClassifier84", self)

class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, EEnumLiteral: "ecore_EEnum" = None, eLiterals: "ecore_EEnum" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        
    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnumLiteral__EEnumLiteral", None)
        self.__EEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eEnum"):
                opp_val = getattr(old_value, "eEnum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eEnum"):
                opp_val = getattr(value, "eEnum", None)
                if opp_val is None:
                    setattr(value, "eEnum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eLiterals(self):
        return self.__eLiterals

    @eLiterals.setter
    def eLiterals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnumLiteral__eLiterals", None)
        self.__eLiterals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EEnum"):
                opp_val = getattr(old_value, "EEnum", None)
                if opp_val == self:
                    setattr(old_value, "EEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EEnum"):
                opp_val = getattr(value, "EEnum", None)
                setattr(value, "EEnum", self)

class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, eClassifiers: "ecore_EPackage" = None, ecore_EClassifier: set["ecore_ETypeParameter"] = None, ecore_EClassifier57: "ecore_EOperation" = None, EClassifier: "ecore_EPackage" = None, ecore_EClassifier84: "ecore_ETypedElement" = None, ecore_EClassifier96: "ecore_EGenericType" = None, ecore_EClassifier105: "ecore_EGenericType" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.eClassifiers = eClassifiers
        self.ecore_EClassifier = ecore_EClassifier if ecore_EClassifier is not None else set()
        self.ecore_EClassifier57 = ecore_EClassifier57
        self.EClassifier = EClassifier
        self.ecore_EClassifier84 = ecore_EClassifier84
        self.ecore_EClassifier96 = ecore_EClassifier96
        self.ecore_EClassifier105 = ecore_EClassifier105
        
    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def ecore_EClassifier84(self):
        return self.__ecore_EClassifier84

    @ecore_EClassifier84.setter
    def ecore_EClassifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier84", None)
        self.__ecore_EClassifier84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_ETypedElement"):
                opp_val = getattr(old_value, "ecore_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "ecore_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_ETypedElement"):
                opp_val = getattr(value, "ecore_ETypedElement", None)
                setattr(value, "ecore_ETypedElement", self)

    @property
    def ecore_EClassifier96(self):
        return self.__ecore_EClassifier96

    @ecore_EClassifier96.setter
    def ecore_EClassifier96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier96", None)
        self.__ecore_EClassifier96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType95"):
                opp_val = getattr(old_value, "ecore_EGenericType95", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType95"):
                opp_val = getattr(value, "ecore_EGenericType95", None)
                setattr(value, "ecore_EGenericType95", self)

    @property
    def ecore_EClassifier(self):
        return self.__ecore_EClassifier

    @ecore_EClassifier.setter
    def ecore_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier", None)
        self.__ecore_EClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_ETypeParameter"):
                    opp_val = getattr(item, "ecore_ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_ETypeParameter"):
                    opp_val = getattr(item, "ecore_ETypeParameter", None)
                    
                    setattr(item, "ecore_ETypeParameter", self)
                    

    @property
    def ecore_EClassifier105(self):
        return self.__ecore_EClassifier105

    @ecore_EClassifier105.setter
    def ecore_EClassifier105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier105", None)
        self.__ecore_EClassifier105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType104"):
                opp_val = getattr(old_value, "ecore_EGenericType104", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType104"):
                opp_val = getattr(value, "ecore_EGenericType104", None)
                setattr(value, "ecore_EGenericType104", self)

    @property
    def ecore_EClassifier57(self):
        return self.__ecore_EClassifier57

    @ecore_EClassifier57.setter
    def ecore_EClassifier57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier57", None)
        self.__ecore_EClassifier57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EOperation56"):
                opp_val = getattr(old_value, "ecore_EOperation56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EOperation56"):
                opp_val = getattr(value, "ecore_EOperation56", None)
                if opp_val is None:
                    setattr(value, "ecore_EOperation56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__eClassifiers", None)
        self.__eClassifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage"):
                opp_val = getattr(old_value, "EPackage", None)
                if opp_val == self:
                    setattr(old_value, "EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage"):
                opp_val = getattr(value, "EPackage", None)
                setattr(value, "EPackage", self)

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__EClassifier", None)
        self.__EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage63"):
                opp_val = getattr(old_value, "ePackage63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage63"):
                opp_val = getattr(value, "ePackage63", None)
                if opp_val is None:
                    setattr(value, "ePackage63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

class ecore_EGenericType:

    def __init__(self, ecore_EGenericType: "ecore_EClass" = None, ecore_EGenericType41: "ecore_EClass" = None, ecore_EGenericType60: "ecore_EOperation" = None, ecore_EGenericType87: "ecore_ETypedElement" = None, ecore_EGenericType93: "ecore_EGenericType" = None, ecore_EGenericType91: set["ecore_EGenericType"] = None, ecore_EGenericType95: "ecore_EClassifier" = None, ecore_EGenericType99: "ecore_EGenericType" = None, ecore_EGenericType97: "ecore_EGenericType" = None, ecore_EGenericType101: "ecore_ETypeParameter" = None, ecore_EGenericType104: "ecore_EClassifier" = None, ecore_EGenericType90: "ecore_EGenericType" = None, ecore_EGenericType88: "ecore_EGenericType" = None, ecore_EGenericType108: "ecore_ETypeParameter" = None):
        self.ecore_EGenericType = ecore_EGenericType
        self.ecore_EGenericType41 = ecore_EGenericType41
        self.ecore_EGenericType60 = ecore_EGenericType60
        self.ecore_EGenericType87 = ecore_EGenericType87
        self.ecore_EGenericType93 = ecore_EGenericType93
        self.ecore_EGenericType91 = ecore_EGenericType91 if ecore_EGenericType91 is not None else set()
        self.ecore_EGenericType95 = ecore_EGenericType95
        self.ecore_EGenericType99 = ecore_EGenericType99
        self.ecore_EGenericType97 = ecore_EGenericType97
        self.ecore_EGenericType101 = ecore_EGenericType101
        self.ecore_EGenericType104 = ecore_EGenericType104
        self.ecore_EGenericType90 = ecore_EGenericType90
        self.ecore_EGenericType88 = ecore_EGenericType88
        self.ecore_EGenericType108 = ecore_EGenericType108
        
    @property
    def ecore_EGenericType60(self):
        return self.__ecore_EGenericType60

    @ecore_EGenericType60.setter
    def ecore_EGenericType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType60", None)
        self.__ecore_EGenericType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EOperation59"):
                opp_val = getattr(old_value, "ecore_EOperation59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EOperation59"):
                opp_val = getattr(value, "ecore_EOperation59", None)
                if opp_val is None:
                    setattr(value, "ecore_EOperation59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EGenericType87(self):
        return self.__ecore_EGenericType87

    @ecore_EGenericType87.setter
    def ecore_EGenericType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType87", None)
        self.__ecore_EGenericType87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_ETypedElement86"):
                opp_val = getattr(old_value, "ecore_ETypedElement86", None)
                if opp_val == self:
                    setattr(old_value, "ecore_ETypedElement86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_ETypedElement86"):
                opp_val = getattr(value, "ecore_ETypedElement86", None)
                setattr(value, "ecore_ETypedElement86", self)

    @property
    def ecore_EGenericType101(self):
        return self.__ecore_EGenericType101

    @ecore_EGenericType101.setter
    def ecore_EGenericType101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType101", None)
        self.__ecore_EGenericType101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_ETypeParameter102"):
                opp_val = getattr(old_value, "ecore_ETypeParameter102", None)
                if opp_val == self:
                    setattr(old_value, "ecore_ETypeParameter102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_ETypeParameter102"):
                opp_val = getattr(value, "ecore_ETypeParameter102", None)
                setattr(value, "ecore_ETypeParameter102", self)

    @property
    def ecore_EGenericType91(self):
        return self.__ecore_EGenericType91

    @ecore_EGenericType91.setter
    def ecore_EGenericType91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType91", None)
        self.__ecore_EGenericType91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType93"):
                    opp_val = getattr(item, "ecore_EGenericType93", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType93"):
                    opp_val = getattr(item, "ecore_EGenericType93", None)
                    
                    setattr(item, "ecore_EGenericType93", self)
                    

    @property
    def ecore_EGenericType88(self):
        return self.__ecore_EGenericType88

    @ecore_EGenericType88.setter
    def ecore_EGenericType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType88", None)
        self.__ecore_EGenericType88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType90"):
                opp_val = getattr(old_value, "ecore_EGenericType90", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType90"):
                opp_val = getattr(value, "ecore_EGenericType90", None)
                setattr(value, "ecore_EGenericType90", self)

    @property
    def ecore_EGenericType41(self):
        return self.__ecore_EGenericType41

    @ecore_EGenericType41.setter
    def ecore_EGenericType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType41", None)
        self.__ecore_EGenericType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass40"):
                opp_val = getattr(old_value, "ecore_EClass40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass40"):
                opp_val = getattr(value, "ecore_EClass40", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EGenericType108(self):
        return self.__ecore_EGenericType108

    @ecore_EGenericType108.setter
    def ecore_EGenericType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType108", None)
        self.__ecore_EGenericType108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_ETypeParameter107"):
                opp_val = getattr(old_value, "ecore_ETypeParameter107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_ETypeParameter107"):
                opp_val = getattr(value, "ecore_ETypeParameter107", None)
                if opp_val is None:
                    setattr(value, "ecore_ETypeParameter107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EGenericType93(self):
        return self.__ecore_EGenericType93

    @ecore_EGenericType93.setter
    def ecore_EGenericType93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType93", None)
        self.__ecore_EGenericType93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType91"):
                opp_val = getattr(old_value, "ecore_EGenericType91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType91"):
                opp_val = getattr(value, "ecore_EGenericType91", None)
                if opp_val is None:
                    setattr(value, "ecore_EGenericType91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EGenericType(self):
        return self.__ecore_EGenericType

    @ecore_EGenericType.setter
    def ecore_EGenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType", None)
        self.__ecore_EGenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass38"):
                opp_val = getattr(old_value, "ecore_EClass38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass38"):
                opp_val = getattr(value, "ecore_EClass38", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EGenericType104(self):
        return self.__ecore_EGenericType104

    @ecore_EGenericType104.setter
    def ecore_EGenericType104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType104", None)
        self.__ecore_EGenericType104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClassifier105"):
                opp_val = getattr(old_value, "ecore_EClassifier105", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier105"):
                opp_val = getattr(value, "ecore_EClassifier105", None)
                setattr(value, "ecore_EClassifier105", self)

    @property
    def ecore_EGenericType97(self):
        return self.__ecore_EGenericType97

    @ecore_EGenericType97.setter
    def ecore_EGenericType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType97", None)
        self.__ecore_EGenericType97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType99"):
                opp_val = getattr(old_value, "ecore_EGenericType99", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType99"):
                opp_val = getattr(value, "ecore_EGenericType99", None)
                setattr(value, "ecore_EGenericType99", self)

    @property
    def ecore_EGenericType99(self):
        return self.__ecore_EGenericType99

    @ecore_EGenericType99.setter
    def ecore_EGenericType99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType99", None)
        self.__ecore_EGenericType99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType97"):
                opp_val = getattr(old_value, "ecore_EGenericType97", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType97"):
                opp_val = getattr(value, "ecore_EGenericType97", None)
                setattr(value, "ecore_EGenericType97", self)

    @property
    def ecore_EGenericType95(self):
        return self.__ecore_EGenericType95

    @ecore_EGenericType95.setter
    def ecore_EGenericType95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType95", None)
        self.__ecore_EGenericType95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClassifier96"):
                opp_val = getattr(old_value, "ecore_EClassifier96", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier96"):
                opp_val = getattr(value, "ecore_EClassifier96", None)
                setattr(value, "ecore_EClassifier96", self)

    @property
    def ecore_EGenericType90(self):
        return self.__ecore_EGenericType90

    @ecore_EGenericType90.setter
    def ecore_EGenericType90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType90", None)
        self.__ecore_EGenericType90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType88"):
                opp_val = getattr(old_value, "ecore_EGenericType88", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType88"):
                opp_val = getattr(value, "ecore_EGenericType88", None)
                setattr(value, "ecore_EGenericType88", self)

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, changeable: bool, volatile: bool, ecore_EStructuralFeature: "ecore_EClass" = None, EStructuralFeature: "ecore_EClass" = None, eStructuralFeatures: "ecore_EClass" = None):
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.changeable = changeable
        self.volatile = volatile
        self.ecore_EStructuralFeature = ecore_EStructuralFeature
        self.EStructuralFeature = EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def ecore_EStructuralFeature(self):
        return self.__ecore_EStructuralFeature

    @ecore_EStructuralFeature.setter
    def ecore_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__ecore_EStructuralFeature", None)
        self.__ecore_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass28"):
                opp_val = getattr(old_value, "ecore_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass28"):
                opp_val = getattr(value, "ecore_EClass28", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__EStructuralFeature", None)
        self.__EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass36"):
                opp_val = getattr(old_value, "eContainingClass36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass36"):
                opp_val = getattr(value, "eContainingClass36", None)
                if opp_val is None:
                    setattr(value, "eContainingClass36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eStructuralFeatures(self):
        return self.__eStructuralFeatures

    @eStructuralFeatures.setter
    def eStructuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass82"):
                opp_val = getattr(old_value, "EClass82", None)
                if opp_val == self:
                    setattr(old_value, "EClass82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass82"):
                opp_val = getattr(value, "EClass82", None)
                setattr(value, "EClass82", self)

    def getContainerClass(self):
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class ecore_EOperation(ETypedElement):

    def __init__(self, EOperation: "ecore_EClass" = None, ecore_EOperation: "ecore_EClass" = None, eOperations: "ecore_EClass" = None, eOperation: set["ecore_EParameter"] = None, ecore_EOperation56: set["ecore_EClassifier"] = None, ecore_EOperation59: set["ecore_EGenericType"] = None, ecore_EOperation52: set["ecore_ETypeParameter"] = None, EOperation71: "ecore_EParameter" = None):
        self.EOperation = EOperation
        self.ecore_EOperation = ecore_EOperation
        self.eOperations = eOperations
        self.eOperation = eOperation if eOperation is not None else set()
        self.ecore_EOperation56 = ecore_EOperation56 if ecore_EOperation56 is not None else set()
        self.ecore_EOperation59 = ecore_EOperation59 if ecore_EOperation59 is not None else set()
        self.ecore_EOperation52 = ecore_EOperation52 if ecore_EOperation52 is not None else set()
        self.EOperation71 = EOperation71
        
    @property
    def ecore_EOperation(self):
        return self.__ecore_EOperation

    @ecore_EOperation.setter
    def ecore_EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation", None)
        self.__ecore_EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass26"):
                opp_val = getattr(old_value, "ecore_EClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass26"):
                opp_val = getattr(value, "ecore_EClass26", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EOperation56(self):
        return self.__ecore_EOperation56

    @ecore_EOperation56.setter
    def ecore_EOperation56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation56", None)
        self.__ecore_EOperation56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClassifier57"):
                    opp_val = getattr(item, "ecore_EClassifier57", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClassifier57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClassifier57"):
                    opp_val = getattr(item, "ecore_EClassifier57", None)
                    
                    setattr(item, "ecore_EClassifier57", self)
                    

    @property
    def eOperations(self):
        return self.__eOperations

    @eOperations.setter
    def eOperations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__eOperations", None)
        self.__eOperations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass"):
                opp_val = getattr(old_value, "EClass", None)
                if opp_val == self:
                    setattr(old_value, "EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass"):
                opp_val = getattr(value, "EClass", None)
                setattr(value, "EClass", self)

    @property
    def eOperation(self):
        return self.__eOperation

    @eOperation.setter
    def eOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__eOperation", None)
        self.__eOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EParameter"):
                    opp_val = getattr(item, "EParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "EParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EParameter"):
                    opp_val = getattr(item, "EParameter", None)
                    
                    setattr(item, "EParameter", self)
                    

    @property
    def ecore_EOperation52(self):
        return self.__ecore_EOperation52

    @ecore_EOperation52.setter
    def ecore_EOperation52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation52", None)
        self.__ecore_EOperation52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_ETypeParameter53"):
                    opp_val = getattr(item, "ecore_ETypeParameter53", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_ETypeParameter53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_ETypeParameter53"):
                    opp_val = getattr(item, "ecore_ETypeParameter53", None)
                    
                    setattr(item, "ecore_ETypeParameter53", self)
                    

    @property
    def EOperation(self):
        return self.__EOperation

    @EOperation.setter
    def EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__EOperation", None)
        self.__EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass"):
                opp_val = getattr(old_value, "eContainingClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass"):
                opp_val = getattr(value, "eContainingClass", None)
                if opp_val is None:
                    setattr(value, "eContainingClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EOperation59(self):
        return self.__ecore_EOperation59

    @ecore_EOperation59.setter
    def ecore_EOperation59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation59", None)
        self.__ecore_EOperation59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType60"):
                    opp_val = getattr(item, "ecore_EGenericType60", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType60"):
                    opp_val = getattr(item, "ecore_EGenericType60", None)
                    
                    setattr(item, "ecore_EGenericType60", self)
                    

    @property
    def EOperation71(self):
        return self.__EOperation71

    @EOperation71.setter
    def EOperation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__EOperation71", None)
        self.__EOperation71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eParameters"):
                opp_val = getattr(old_value, "eParameters", None)
                if opp_val == self:
                    setattr(old_value, "eParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eParameters"):
                opp_val = getattr(value, "eParameters", None)
                setattr(value, "eParameters", self)

    def isOverrideOf(self, someOperation: str) -> bool:
        # TODO: Implement isOverrideOf method
        pass

    def getOperationID(self) -> int:
        # TODO: Implement getOperationID method
        pass

class FSM:

    pass
class EClassifier:

    pass
class ecore_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecore_EDataType: "ecore_EAttribute" = None):
        self.serializable = serializable
        self.ecore_EDataType = ecore_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def ecore_EDataType(self):
        return self.__ecore_EDataType

    @ecore_EDataType.setter
    def ecore_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EDataType__ecore_EDataType", None)
        self.__ecore_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAttribute"):
                opp_val = getattr(old_value, "ecore_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute"):
                opp_val = getattr(value, "ecore_EAttribute", None)
                setattr(value, "ecore_EAttribute", self)

class ecore_EClass(EClassifier, FSM):

    def __init__(self, abstract: bool, interface: bool, ecore_EClass: "ecore_EClass" = None, ecore_EClass8: set["ecore_EClass"] = None, eContainingClass: set["ecore_EOperation"] = None, ecore_EClass12: set["ecore_EAttribute"] = None, ecore_EClass15: set["ecore_EReference"] = None, ecore_EClass17: set["ecore_EReference"] = None, ecore_EClass20: set["ecore_EAttribute"] = None, ecore_EClass23: set["ecore_EReference"] = None, ecore_EClass28: set["ecore_EStructuralFeature"] = None, ecore_EClass31: "ecore_EClass" = None, ecore_EClass29: set["ecore_EClass"] = None, ecore_EClass33: "ecore_EAttribute" = None, eContainingClass36: set["ecore_EStructuralFeature"] = None, ecore_EClass38: set["ecore_EGenericType"] = None, ecore_EClass40: set["ecore_EGenericType"] = None, ecore_EClass26: set["ecore_EOperation"] = None, EClass: "ecore_EOperation" = None, ecore_EClass77: "ecore_EReference" = None, EClass82: "ecore_EStructuralFeature" = None, ecore_EClass121: "ecore_State" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecore_EClass = ecore_EClass
        self.ecore_EClass8 = ecore_EClass8 if ecore_EClass8 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecore_EClass12 = ecore_EClass12 if ecore_EClass12 is not None else set()
        self.ecore_EClass15 = ecore_EClass15 if ecore_EClass15 is not None else set()
        self.ecore_EClass17 = ecore_EClass17 if ecore_EClass17 is not None else set()
        self.ecore_EClass20 = ecore_EClass20 if ecore_EClass20 is not None else set()
        self.ecore_EClass23 = ecore_EClass23 if ecore_EClass23 is not None else set()
        self.ecore_EClass28 = ecore_EClass28 if ecore_EClass28 is not None else set()
        self.ecore_EClass31 = ecore_EClass31
        self.ecore_EClass29 = ecore_EClass29 if ecore_EClass29 is not None else set()
        self.ecore_EClass33 = ecore_EClass33
        self.eContainingClass36 = eContainingClass36 if eContainingClass36 is not None else set()
        self.ecore_EClass38 = ecore_EClass38 if ecore_EClass38 is not None else set()
        self.ecore_EClass40 = ecore_EClass40 if ecore_EClass40 is not None else set()
        self.ecore_EClass26 = ecore_EClass26 if ecore_EClass26 is not None else set()
        self.EClass = EClass
        self.ecore_EClass77 = ecore_EClass77
        self.EClass82 = EClass82
        self.ecore_EClass121 = ecore_EClass121
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def ecore_EClass23(self):
        return self.__ecore_EClass23

    @ecore_EClass23.setter
    def ecore_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass23", None)
        self.__ecore_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference24"):
                    opp_val = getattr(item, "ecore_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference24"):
                    opp_val = getattr(item, "ecore_EReference24", None)
                    
                    setattr(item, "ecore_EReference24", self)
                    

    @property
    def ecore_EClass77(self):
        return self.__ecore_EClass77

    @ecore_EClass77.setter
    def ecore_EClass77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass77", None)
        self.__ecore_EClass77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference76"):
                opp_val = getattr(old_value, "ecore_EReference76", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference76"):
                opp_val = getattr(value, "ecore_EReference76", None)
                setattr(value, "ecore_EReference76", self)

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass", None)
        self.__EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eOperations"):
                opp_val = getattr(old_value, "eOperations", None)
                if opp_val == self:
                    setattr(old_value, "eOperations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eOperations"):
                opp_val = getattr(value, "eOperations", None)
                setattr(value, "eOperations", self)

    @property
    def ecore_EClass20(self):
        return self.__ecore_EClass20

    @ecore_EClass20.setter
    def ecore_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass20", None)
        self.__ecore_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute21"):
                    opp_val = getattr(item, "ecore_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute21"):
                    opp_val = getattr(item, "ecore_EAttribute21", None)
                    
                    setattr(item, "ecore_EAttribute21", self)
                    

    @property
    def ecore_EClass28(self):
        return self.__ecore_EClass28

    @ecore_EClass28.setter
    def ecore_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass28", None)
        self.__ecore_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EStructuralFeature"):
                    opp_val = getattr(item, "ecore_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EStructuralFeature"):
                    opp_val = getattr(item, "ecore_EStructuralFeature", None)
                    
                    setattr(item, "ecore_EStructuralFeature", self)
                    

    @property
    def eContainingClass36(self):
        return self.__eContainingClass36

    @eContainingClass36.setter
    def eContainingClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass36", None)
        self.__eContainingClass36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    setattr(item, "EStructuralFeature", self)
                    

    @property
    def ecore_EClass29(self):
        return self.__ecore_EClass29

    @ecore_EClass29.setter
    def ecore_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass29", None)
        self.__ecore_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass31"):
                    opp_val = getattr(item, "ecore_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass31"):
                    opp_val = getattr(item, "ecore_EClass31", None)
                    
                    setattr(item, "ecore_EClass31", self)
                    

    @property
    def ecore_EClass15(self):
        return self.__ecore_EClass15

    @ecore_EClass15.setter
    def ecore_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass15", None)
        self.__ecore_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference"):
                    opp_val = getattr(item, "ecore_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference"):
                    opp_val = getattr(item, "ecore_EReference", None)
                    
                    setattr(item, "ecore_EReference", self)
                    

    @property
    def ecore_EClass12(self):
        return self.__ecore_EClass12

    @ecore_EClass12.setter
    def ecore_EClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass12", None)
        self.__ecore_EClass12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute13"):
                    opp_val = getattr(item, "ecore_EAttribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute13"):
                    opp_val = getattr(item, "ecore_EAttribute13", None)
                    
                    setattr(item, "ecore_EAttribute13", self)
                    

    @property
    def ecore_EClass(self):
        return self.__ecore_EClass

    @ecore_EClass.setter
    def ecore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass", None)
        self.__ecore_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass8"):
                opp_val = getattr(old_value, "ecore_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass8"):
                opp_val = getattr(value, "ecore_EClass8", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClass17(self):
        return self.__ecore_EClass17

    @ecore_EClass17.setter
    def ecore_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass17", None)
        self.__ecore_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference18"):
                    opp_val = getattr(item, "ecore_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference18"):
                    opp_val = getattr(item, "ecore_EReference18", None)
                    
                    setattr(item, "ecore_EReference18", self)
                    

    @property
    def ecore_EClass8(self):
        return self.__ecore_EClass8

    @ecore_EClass8.setter
    def ecore_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass8", None)
        self.__ecore_EClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass"):
                    opp_val = getattr(item, "ecore_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass"):
                    opp_val = getattr(item, "ecore_EClass", None)
                    
                    setattr(item, "ecore_EClass", self)
                    

    @property
    def ecore_EClass38(self):
        return self.__ecore_EClass38

    @ecore_EClass38.setter
    def ecore_EClass38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass38", None)
        self.__ecore_EClass38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType"):
                    opp_val = getattr(item, "ecore_EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType"):
                    opp_val = getattr(item, "ecore_EGenericType", None)
                    
                    setattr(item, "ecore_EGenericType", self)
                    

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass", None)
        self.__eContainingClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    setattr(item, "EOperation", self)
                    

    @property
    def EClass82(self):
        return self.__EClass82

    @EClass82.setter
    def EClass82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass82", None)
        self.__EClass82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eStructuralFeatures"):
                opp_val = getattr(old_value, "eStructuralFeatures", None)
                if opp_val == self:
                    setattr(old_value, "eStructuralFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eStructuralFeatures"):
                opp_val = getattr(value, "eStructuralFeatures", None)
                setattr(value, "eStructuralFeatures", self)

    @property
    def ecore_EClass31(self):
        return self.__ecore_EClass31

    @ecore_EClass31.setter
    def ecore_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass31", None)
        self.__ecore_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass29"):
                opp_val = getattr(old_value, "ecore_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass29"):
                opp_val = getattr(value, "ecore_EClass29", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClass26(self):
        return self.__ecore_EClass26

    @ecore_EClass26.setter
    def ecore_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass26", None)
        self.__ecore_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EOperation"):
                    opp_val = getattr(item, "ecore_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EOperation"):
                    opp_val = getattr(item, "ecore_EOperation", None)
                    
                    setattr(item, "ecore_EOperation", self)
                    

    @property
    def ecore_EClass33(self):
        return self.__ecore_EClass33

    @ecore_EClass33.setter
    def ecore_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass33", None)
        self.__ecore_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAttribute34"):
                opp_val = getattr(old_value, "ecore_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute34"):
                opp_val = getattr(value, "ecore_EAttribute34", None)
                setattr(value, "ecore_EAttribute34", self)

    @property
    def ecore_EClass121(self):
        return self.__ecore_EClass121

    @ecore_EClass121.setter
    def ecore_EClass121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass121", None)
        self.__ecore_EClass121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_State120"):
                opp_val = getattr(old_value, "ecore_State120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_State120"):
                opp_val = getattr(value, "ecore_State120", None)
                if opp_val is None:
                    setattr(value, "ecore_State120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClass40(self):
        return self.__ecore_EClass40

    @ecore_EClass40.setter
    def ecore_EClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass40", None)
        self.__ecore_EClass40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType41"):
                    opp_val = getattr(item, "ecore_EGenericType41", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType41"):
                    opp_val = getattr(item, "ecore_EGenericType41", None)
                    
                    setattr(item, "ecore_EGenericType41", self)
                    

    def getFeatureType(self, feature: EStructuralFeature) -> str:
        # TODO: Implement getFeatureType method
        pass

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

    def getEOperation(self, operationID: int) -> str:
        # TODO: Implement getEOperation method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getOperationID(self, operation: str) -> int:
        # TODO: Implement getOperationID method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getOverride(self, operation: str) -> str:
        # TODO: Implement getOverride method
        pass

    def getOperationCount(self) -> int:
        # TODO: Implement getOperationCount method
        pass

class ecore_EObject:

    def __init__(self, ecore_EObject: "ecore_EAnnotation" = None, ecore_EObject7: "ecore_EAnnotation" = None):
        self.ecore_EObject = ecore_EObject
        self.ecore_EObject7 = ecore_EObject7
        
    @property
    def ecore_EObject7(self):
        return self.__ecore_EObject7

    @ecore_EObject7.setter
    def ecore_EObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject7", None)
        self.__ecore_EObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation6"):
                opp_val = getattr(old_value, "ecore_EAnnotation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation6"):
                opp_val = getattr(value, "ecore_EAnnotation6", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EObject(self):
        return self.__ecore_EObject

    @ecore_EObject.setter
    def ecore_EObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject", None)
        self.__ecore_EObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation4"):
                opp_val = getattr(old_value, "ecore_EAnnotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation4"):
                opp_val = getattr(value, "ecore_EAnnotation4", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

    def eInvoke(self, operation: str, arguments: str) -> str:
        # TODO: Implement eInvoke method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eSet(self, newValue: str, feature: EStructuralFeature):
        # TODO: Implement eSet method
        pass

    def eCrossReferences(self):
        # TODO: Implement eCrossReferences method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eAllContents(self):
        # TODO: Implement eAllContents method
        pass

    def eContainer(self) -> str:
        # TODO: Implement eContainer method
        pass

    def eContents(self):
        # TODO: Implement eContents method
        pass

    def eGet(self, resolve: bool, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

class ecore_EModelElement(ABC):

    def __init__(self, EModelElement: "ecore_EAnnotation" = None, eModelElement: set["ecore_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
    @property
    def EModelElement(self):
        return self.__EModelElement

    @EModelElement.setter
    def EModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EModelElement__EModelElement", None)
        self.__EModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eAnnotations"):
                opp_val = getattr(old_value, "eAnnotations", None)
                if opp_val == self:
                    setattr(old_value, "eAnnotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eAnnotations"):
                opp_val = getattr(value, "eAnnotations", None)
                setattr(value, "eAnnotations", self)

    @property
    def eModelElement(self):
        return self.__eModelElement

    @eModelElement.setter
    def eModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EModelElement__eModelElement", None)
        self.__eModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAnnotation"):
                    opp_val = getattr(item, "EAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "EAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAnnotation"):
                    opp_val = getattr(item, "EAnnotation", None)
                    
                    setattr(item, "EAnnotation", self)
                    

    def getEAnnotation(self, source: str) -> str:
        # TODO: Implement getEAnnotation method
        pass

class ecore_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecore_EStringToStringMapEntry: "ecore_EAnnotation" = None):
        self.key = key
        self.value = value
        self.ecore_EStringToStringMapEntry = ecore_EStringToStringMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def ecore_EStringToStringMapEntry(self):
        return self.__ecore_EStringToStringMapEntry

    @ecore_EStringToStringMapEntry.setter
    def ecore_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStringToStringMapEntry__ecore_EStringToStringMapEntry", None)
        self.__ecore_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation"):
                opp_val = getattr(old_value, "ecore_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation"):
                opp_val = getattr(value, "ecore_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class ecore_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "ecore_EPackage" = None, EFactory: "ecore_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
    @property
    def EFactory(self):
        return self.__EFactory

    @EFactory.setter
    def EFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EFactory__EFactory", None)
        self.__EFactory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage"):
                opp_val = getattr(old_value, "ePackage", None)
                if opp_val == self:
                    setattr(old_value, "ePackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage"):
                opp_val = getattr(value, "ePackage", None)
                setattr(value, "ePackage", self)

    @property
    def eFactoryInstance(self):
        return self.__eFactoryInstance

    @eFactoryInstance.setter
    def eFactoryInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EFactory__eFactoryInstance", None)
        self.__eFactoryInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage47"):
                opp_val = getattr(old_value, "EPackage47", None)
                if opp_val == self:
                    setattr(old_value, "EPackage47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage47"):
                opp_val = getattr(value, "EPackage47", None)
                setattr(value, "EPackage47", self)

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

    def convertToString(self, eDataType: EDataType, instanceValue: str) -> str:
        # TODO: Implement convertToString method
        pass

    def createFromString(self, literalValue: str, eDataType: EDataType) -> str:
        # TODO: Implement createFromString method
        pass

class ecore_ENamedElement(EModelElement):

    def __init__(self, name: str, ecore_ENamedElement: set["ecore_FSM"] = None):
        self.name = name
        self.ecore_ENamedElement = ecore_ENamedElement if ecore_ENamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecore_ENamedElement(self):
        return self.__ecore_ENamedElement

    @ecore_ENamedElement.setter
    def ecore_ENamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ENamedElement__ecore_ENamedElement", None)
        self.__ecore_ENamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_FSM"):
                    opp_val = getattr(item, "ecore_FSM", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_FSM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_FSM"):
                    opp_val = getattr(item, "ecore_FSM", None)
                    
                    setattr(item, "ecore_FSM", self)
                    

class ecore_EAnnotation(EModelElement):

    def __init__(self, source: str, ecore_EAnnotation: set["ecore_EStringToStringMapEntry"] = None, eAnnotations: "ecore_EModelElement" = None, ecore_EAnnotation4: set["ecore_EObject"] = None, ecore_EAnnotation6: set["ecore_EObject"] = None, EAnnotation: "ecore_EModelElement" = None):
        self.source = source
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.ecore_EAnnotation4 = ecore_EAnnotation4 if ecore_EAnnotation4 is not None else set()
        self.ecore_EAnnotation6 = ecore_EAnnotation6 if ecore_EAnnotation6 is not None else set()
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecore_EAnnotation(self):
        return self.__ecore_EAnnotation

    @ecore_EAnnotation.setter
    def ecore_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation", None)
        self.__ecore_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecore_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecore_EStringToStringMapEntry", None)
                    
                    setattr(item, "ecore_EStringToStringMapEntry", self)
                    

    @property
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__eAnnotations", None)
        self.__eAnnotations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EModelElement"):
                opp_val = getattr(old_value, "EModelElement", None)
                if opp_val == self:
                    setattr(old_value, "EModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EModelElement"):
                opp_val = getattr(value, "EModelElement", None)
                setattr(value, "EModelElement", self)

    @property
    def ecore_EAnnotation6(self):
        return self.__ecore_EAnnotation6

    @ecore_EAnnotation6.setter
    def ecore_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation6", None)
        self.__ecore_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EObject7"):
                    opp_val = getattr(item, "ecore_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject7"):
                    opp_val = getattr(item, "ecore_EObject7", None)
                    
                    setattr(item, "ecore_EObject7", self)
                    

    @property
    def ecore_EAnnotation4(self):
        return self.__ecore_EAnnotation4

    @ecore_EAnnotation4.setter
    def ecore_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation4", None)
        self.__ecore_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EObject"):
                    opp_val = getattr(item, "ecore_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject"):
                    opp_val = getattr(item, "ecore_EObject", None)
                    
                    setattr(item, "ecore_EObject", self)
                    

    @property
    def EAnnotation(self):
        return self.__EAnnotation

    @EAnnotation.setter
    def EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__EAnnotation", None)
        self.__EAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eModelElement"):
                opp_val = getattr(old_value, "eModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eModelElement"):
                opp_val = getattr(value, "eModelElement", None)
                if opp_val is None:
                    setattr(value, "eModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EStructuralFeature:

    pass
class ecore_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecore_EReference: "ecore_EClass" = None, ecore_EReference18: "ecore_EClass" = None, ecore_EReference24: "ecore_EClass" = None, ecore_EReference74: "ecore_EReference" = None, ecore_EReference72: "ecore_EReference" = None, ecore_EReference76: "ecore_EClass" = None, ecore_EReference79: set["ecore_EAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference18 = ecore_EReference18
        self.ecore_EReference24 = ecore_EReference24
        self.ecore_EReference74 = ecore_EReference74
        self.ecore_EReference72 = ecore_EReference72
        self.ecore_EReference76 = ecore_EReference76
        self.ecore_EReference79 = ecore_EReference79 if ecore_EReference79 is not None else set()
        
    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def ecore_EReference18(self):
        return self.__ecore_EReference18

    @ecore_EReference18.setter
    def ecore_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference18", None)
        self.__ecore_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass17"):
                opp_val = getattr(old_value, "ecore_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass17"):
                opp_val = getattr(value, "ecore_EClass17", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference24(self):
        return self.__ecore_EReference24

    @ecore_EReference24.setter
    def ecore_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference24", None)
        self.__ecore_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass23"):
                opp_val = getattr(old_value, "ecore_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass23"):
                opp_val = getattr(value, "ecore_EClass23", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference76(self):
        return self.__ecore_EReference76

    @ecore_EReference76.setter
    def ecore_EReference76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference76", None)
        self.__ecore_EReference76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass77"):
                opp_val = getattr(old_value, "ecore_EClass77", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass77"):
                opp_val = getattr(value, "ecore_EClass77", None)
                setattr(value, "ecore_EClass77", self)

    @property
    def ecore_EReference79(self):
        return self.__ecore_EReference79

    @ecore_EReference79.setter
    def ecore_EReference79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference79", None)
        self.__ecore_EReference79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute80"):
                    opp_val = getattr(item, "ecore_EAttribute80", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute80"):
                    opp_val = getattr(item, "ecore_EAttribute80", None)
                    
                    setattr(item, "ecore_EAttribute80", self)
                    

    @property
    def ecore_EReference72(self):
        return self.__ecore_EReference72

    @ecore_EReference72.setter
    def ecore_EReference72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference72", None)
        self.__ecore_EReference72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference74"):
                opp_val = getattr(old_value, "ecore_EReference74", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference74"):
                opp_val = getattr(value, "ecore_EReference74", None)
                setattr(value, "ecore_EReference74", self)

    @property
    def ecore_EReference(self):
        return self.__ecore_EReference

    @ecore_EReference.setter
    def ecore_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference", None)
        self.__ecore_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass15"):
                opp_val = getattr(old_value, "ecore_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass15"):
                opp_val = getattr(value, "ecore_EClass15", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference74(self):
        return self.__ecore_EReference74

    @ecore_EReference74.setter
    def ecore_EReference74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference74", None)
        self.__ecore_EReference74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference72"):
                opp_val = getattr(old_value, "ecore_EReference72", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference72"):
                opp_val = getattr(value, "ecore_EReference72", None)
                setattr(value, "ecore_EReference72", self)

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecore_EAttribute: "ecore_EDataType" = None, ecore_EAttribute13: "ecore_EClass" = None, ecore_EAttribute21: "ecore_EClass" = None, ecore_EAttribute34: "ecore_EClass" = None, ecore_EAttribute80: "ecore_EReference" = None):
        self.iD = iD
        self.ecore_EAttribute = ecore_EAttribute
        self.ecore_EAttribute13 = ecore_EAttribute13
        self.ecore_EAttribute21 = ecore_EAttribute21
        self.ecore_EAttribute34 = ecore_EAttribute34
        self.ecore_EAttribute80 = ecore_EAttribute80
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecore_EAttribute(self):
        return self.__ecore_EAttribute

    @ecore_EAttribute.setter
    def ecore_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute", None)
        self.__ecore_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EDataType"):
                opp_val = getattr(old_value, "ecore_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EDataType"):
                opp_val = getattr(value, "ecore_EDataType", None)
                setattr(value, "ecore_EDataType", self)

    @property
    def ecore_EAttribute80(self):
        return self.__ecore_EAttribute80

    @ecore_EAttribute80.setter
    def ecore_EAttribute80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute80", None)
        self.__ecore_EAttribute80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference79"):
                opp_val = getattr(old_value, "ecore_EReference79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference79"):
                opp_val = getattr(value, "ecore_EReference79", None)
                if opp_val is None:
                    setattr(value, "ecore_EReference79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute21(self):
        return self.__ecore_EAttribute21

    @ecore_EAttribute21.setter
    def ecore_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute21", None)
        self.__ecore_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass20"):
                opp_val = getattr(old_value, "ecore_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass20"):
                opp_val = getattr(value, "ecore_EClass20", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute13(self):
        return self.__ecore_EAttribute13

    @ecore_EAttribute13.setter
    def ecore_EAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute13", None)
        self.__ecore_EAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass12"):
                opp_val = getattr(old_value, "ecore_EClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass12"):
                opp_val = getattr(value, "ecore_EClass12", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute34(self):
        return self.__ecore_EAttribute34

    @ecore_EAttribute34.setter
    def ecore_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute34", None)
        self.__ecore_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass33"):
                opp_val = getattr(old_value, "ecore_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass33"):
                opp_val = getattr(value, "ecore_EClass33", None)
                setattr(value, "ecore_EClass33", self)
