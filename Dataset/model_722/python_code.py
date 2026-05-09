from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConstraintLanguage(Enum):
    kermeta = "kermeta"
    ocl = "ocl"
class ConstraintType(Enum):
    inv = "inv"
    pre = "pre"
    post = "post"


############################################
# Definition of Classes
############################################

class CallFeature:

    pass
class org_behavior_CallOperation(CallFeature):

    pass
class structure_UnresolvedOperation:

    pass
class structure_Using:

    pass
class structure_UnresolvedReference:

    pass
class Literal:

    pass
class org_behavior_VoidLiteral(Literal):

    pass
class org_behavior_IntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class behavior_LambdaParameter:

    pass
class MultiplicityElement:

    pass
class org_behavior_TypeReference(MultiplicityElement):

    pass
class org_behavior_CallTypeLiteral(Literal):

    pass
class org_behavior_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class org_behavior_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class CallVariable:

    pass
class org_behavior_CallResult(CallVariable):

    pass
class CallOperation:

    pass
class org_behavior_CallSuperOperation(CallOperation):

    pass
class behavior_TypeReference:

    pass
class KermetaModelElement:

    pass
class org_behavior_LambdaParameter(KermetaModelElement):

    def __init__(self, name: str, org_behavior_LambdaParameter: "behavior_TypeReference" = None):
        self.name = name
        self.org_behavior_LambdaParameter = org_behavior_LambdaParameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def org_behavior_LambdaParameter(self):
        return self.__org_behavior_LambdaParameter

    @org_behavior_LambdaParameter.setter
    def org_behavior_LambdaParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_LambdaParameter__org_behavior_LambdaParameter", None)
        self.__org_behavior_LambdaParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference38"):
                opp_val = getattr(old_value, "behavior_TypeReference38", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference38"):
                opp_val = getattr(value, "behavior_TypeReference38", None)
                setattr(value, "behavior_TypeReference38", self)

class org_behavior_Rescue(KermetaModelElement):

    def __init__(self, exceptionName: str, org_behavior_Rescue: set["behavior_Expression"] = None, org_behavior_Rescue30: "behavior_TypeReference" = None):
        self.exceptionName = exceptionName
        self.org_behavior_Rescue = org_behavior_Rescue if org_behavior_Rescue is not None else set()
        self.org_behavior_Rescue30 = org_behavior_Rescue30
        
        pass
    @property
    def exceptionName(self):
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName


    @property
    def org_behavior_Rescue(self):
        return self.__org_behavior_Rescue

    @org_behavior_Rescue.setter
    def org_behavior_Rescue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Rescue__org_behavior_Rescue", None)
        self.__org_behavior_Rescue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression28"):
                    opp_val = getattr(item, "behavior_Expression28", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression28"):
                    opp_val = getattr(item, "behavior_Expression28", None)
                    
                    setattr(item, "behavior_Expression28", self)
                    

    @property
    def org_behavior_Rescue30(self):
        return self.__org_behavior_Rescue30

    @org_behavior_Rescue30.setter
    def org_behavior_Rescue30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Rescue__org_behavior_Rescue30", None)
        self.__org_behavior_Rescue30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference"):
                opp_val = getattr(old_value, "behavior_TypeReference", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference"):
                opp_val = getattr(value, "behavior_TypeReference", None)
                setattr(value, "behavior_TypeReference", self)

class structure_Type:

    pass
class structure_TypeContainer:

    pass
class structure_KermetaModelElement:

    pass
class org_behavior_Expression(structure_TypeContainer, structure_KermetaModelElement):

    pass
class behavior_Expression:

    pass
class behavior_CallExpression:

    pass
class org_behavior_UnresolvedCall(structure_UnresolvedReference, structure_TypeContainer, behavior_CallExpression):

    def __init__(self, isAtpre: str, isCalledWithParenthesis: str, org_behavior_UnresolvedCall59: "structure_Type" = None, org_behavior_UnresolvedCall62: set["structure_Type"] = None, org_behavior_UnresolvedCall: set["structure_Using"] = None, org_behavior_UnresolvedCall56: "behavior_Expression" = None, behavior_CallExpression: "org_behavior_Assignment" = None, TypeContainer: "org_structure_Type" = None, structure_UnresolvedReference: "org_structure_UseAdaptationOperator" = None):
        self.isAtpre = isAtpre
        self.isCalledWithParenthesis = isCalledWithParenthesis
        self.org_behavior_UnresolvedCall59 = org_behavior_UnresolvedCall59
        self.org_behavior_UnresolvedCall62 = org_behavior_UnresolvedCall62 if org_behavior_UnresolvedCall62 is not None else set()
        self.org_behavior_UnresolvedCall = org_behavior_UnresolvedCall if org_behavior_UnresolvedCall is not None else set()
        self.org_behavior_UnresolvedCall56 = org_behavior_UnresolvedCall56
        
        pass
    @property
    def isCalledWithParenthesis(self):
        return self.__isCalledWithParenthesis

    @isCalledWithParenthesis.setter
    def isCalledWithParenthesis(self, isCalledWithParenthesis: str):
        self.__isCalledWithParenthesis = isCalledWithParenthesis


    @property
    def isAtpre(self):
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre


    @property
    def org_behavior_UnresolvedCall62(self):
        return self.__org_behavior_UnresolvedCall62

    @org_behavior_UnresolvedCall62.setter
    def org_behavior_UnresolvedCall62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall62", None)
        self.__org_behavior_UnresolvedCall62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type63"):
                    opp_val = getattr(item, "structure_Type63", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type63"):
                    opp_val = getattr(item, "structure_Type63", None)
                    
                    setattr(item, "structure_Type63", self)
                    

    @property
    def org_behavior_UnresolvedCall56(self):
        return self.__org_behavior_UnresolvedCall56

    @org_behavior_UnresolvedCall56.setter
    def org_behavior_UnresolvedCall56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall56", None)
        self.__org_behavior_UnresolvedCall56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression57"):
                opp_val = getattr(old_value, "behavior_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression57"):
                opp_val = getattr(value, "behavior_Expression57", None)
                setattr(value, "behavior_Expression57", self)

    @property
    def org_behavior_UnresolvedCall(self):
        return self.__org_behavior_UnresolvedCall

    @org_behavior_UnresolvedCall.setter
    def org_behavior_UnresolvedCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall", None)
        self.__org_behavior_UnresolvedCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Using"):
                    opp_val = getattr(item, "structure_Using", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Using", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Using"):
                    opp_val = getattr(item, "structure_Using", None)
                    
                    setattr(item, "structure_Using", self)
                    

    @property
    def org_behavior_UnresolvedCall59(self):
        return self.__org_behavior_UnresolvedCall59

    @org_behavior_UnresolvedCall59.setter
    def org_behavior_UnresolvedCall59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall59", None)
        self.__org_behavior_UnresolvedCall59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Type60"):
                opp_val = getattr(old_value, "structure_Type60", None)
                if opp_val == self:
                    setattr(old_value, "structure_Type60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Type60"):
                opp_val = getattr(value, "structure_Type60", None)
                setattr(value, "structure_Type60", self)

class CallExpression:

    pass
class org_behavior_CallFeature(CallExpression):

    def __init__(self, isAtpre: str, org_behavior_CallFeature: "behavior_Expression" = None):
        self.isAtpre = isAtpre
        self.org_behavior_CallFeature = org_behavior_CallFeature
        
        pass
    @property
    def isAtpre(self):
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre


    @property
    def org_behavior_CallFeature(self):
        return self.__org_behavior_CallFeature

    @org_behavior_CallFeature.setter
    def org_behavior_CallFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_CallFeature__org_behavior_CallFeature", None)
        self.__org_behavior_CallFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression14"):
                opp_val = getattr(old_value, "behavior_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression14"):
                opp_val = getattr(value, "behavior_Expression14", None)
                setattr(value, "behavior_Expression14", self)

class org_behavior_CallValue(CallExpression):

    pass
class org_behavior_CallVariable(CallExpression):

    def __init__(self, isAtpre: str):
        self.isAtpre = isAtpre
        
        pass
    @property
    def isAtpre(self):
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre


class behavior_Rescue:

    pass
class Expression:

    pass
class org_behavior_Block(Expression):

    pass
class org_behavior_VariableDecl(Expression):

    def __init__(self, identifier: str, org_behavior_VariableDecl: "behavior_Expression" = None, org_behavior_VariableDecl52: "behavior_TypeReference" = None):
        self.identifier = identifier
        self.org_behavior_VariableDecl = org_behavior_VariableDecl
        self.org_behavior_VariableDecl52 = org_behavior_VariableDecl52
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def org_behavior_VariableDecl(self):
        return self.__org_behavior_VariableDecl

    @org_behavior_VariableDecl.setter
    def org_behavior_VariableDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_VariableDecl__org_behavior_VariableDecl", None)
        self.__org_behavior_VariableDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression50"):
                opp_val = getattr(old_value, "behavior_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression50"):
                opp_val = getattr(value, "behavior_Expression50", None)
                setattr(value, "behavior_Expression50", self)

    @property
    def org_behavior_VariableDecl52(self):
        return self.__org_behavior_VariableDecl52

    @org_behavior_VariableDecl52.setter
    def org_behavior_VariableDecl52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_VariableDecl__org_behavior_VariableDecl52", None)
        self.__org_behavior_VariableDecl52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference53"):
                opp_val = getattr(old_value, "behavior_TypeReference53", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference53"):
                opp_val = getattr(value, "behavior_TypeReference53", None)
                setattr(value, "behavior_TypeReference53", self)

class org_behavior_LambdaExpression(Expression):

    pass
class org_behavior_Conditional(Expression):

    pass
class org_behavior_CallExpression(Expression):

    def __init__(self, name: str, org_behavior_CallExpression: set["behavior_Expression"] = None, org_behavior_CallExpression7: set["structure_Type"] = None):
        self.name = name
        self.org_behavior_CallExpression = org_behavior_CallExpression if org_behavior_CallExpression is not None else set()
        self.org_behavior_CallExpression7 = org_behavior_CallExpression7 if org_behavior_CallExpression7 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def org_behavior_CallExpression7(self):
        return self.__org_behavior_CallExpression7

    @org_behavior_CallExpression7.setter
    def org_behavior_CallExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_CallExpression__org_behavior_CallExpression7", None)
        self.__org_behavior_CallExpression7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type8"):
                    opp_val = getattr(item, "structure_Type8", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type8"):
                    opp_val = getattr(item, "structure_Type8", None)
                    
                    setattr(item, "structure_Type8", self)
                    

    @property
    def org_behavior_CallExpression(self):
        return self.__org_behavior_CallExpression

    @org_behavior_CallExpression.setter
    def org_behavior_CallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_CallExpression__org_behavior_CallExpression", None)
        self.__org_behavior_CallExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression5"):
                    opp_val = getattr(item, "behavior_Expression5", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression5"):
                    opp_val = getattr(item, "behavior_Expression5", None)
                    
                    setattr(item, "behavior_Expression5", self)
                    

class org_behavior_Loop(Expression):

    pass
class org_behavior_EmptyExpression(Expression):

    pass
class org_behavior_JavaStaticCall(Expression):

    def __init__(self, jclass: str, jmethod: str, org_behavior_JavaStaticCall: set["behavior_Expression"] = None):
        self.jclass = jclass
        self.jmethod = jmethod
        self.org_behavior_JavaStaticCall = org_behavior_JavaStaticCall if org_behavior_JavaStaticCall is not None else set()
        
        pass
    @property
    def jclass(self):
        return self.__jclass

    @jclass.setter
    def jclass(self, jclass: str):
        self.__jclass = jclass


    @property
    def jmethod(self):
        return self.__jmethod

    @jmethod.setter
    def jmethod(self, jmethod: str):
        self.__jmethod = jmethod


    @property
    def org_behavior_JavaStaticCall(self):
        return self.__org_behavior_JavaStaticCall

    @org_behavior_JavaStaticCall.setter
    def org_behavior_JavaStaticCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_JavaStaticCall__org_behavior_JavaStaticCall", None)
        self.__org_behavior_JavaStaticCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression32"):
                    opp_val = getattr(item, "behavior_Expression32", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression32"):
                    opp_val = getattr(item, "behavior_Expression32", None)
                    
                    setattr(item, "behavior_Expression32", self)
                    

class org_behavior_Raise(Expression):

    pass
class org_behavior_Literal(Expression):

    pass
class org_behavior_SelfExpression(Expression):

    pass
class org_behavior_Assignment(Expression):

    def __init__(self, isCast: str, org_behavior_Assignment: "behavior_CallExpression" = None, org_behavior_Assignment2: "behavior_Expression" = None):
        self.isCast = isCast
        self.org_behavior_Assignment = org_behavior_Assignment
        self.org_behavior_Assignment2 = org_behavior_Assignment2
        
        pass
    @property
    def isCast(self):
        return self.__isCast

    @isCast.setter
    def isCast(self, isCast: str):
        self.__isCast = isCast


    @property
    def org_behavior_Assignment(self):
        return self.__org_behavior_Assignment

    @org_behavior_Assignment.setter
    def org_behavior_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Assignment__org_behavior_Assignment", None)
        self.__org_behavior_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_CallExpression"):
                opp_val = getattr(old_value, "behavior_CallExpression", None)
                if opp_val == self:
                    setattr(old_value, "behavior_CallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_CallExpression"):
                opp_val = getattr(value, "behavior_CallExpression", None)
                setattr(value, "behavior_CallExpression", self)

    @property
    def org_behavior_Assignment2(self):
        return self.__org_behavior_Assignment2

    @org_behavior_Assignment2.setter
    def org_behavior_Assignment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Assignment__org_behavior_Assignment2", None)
        self.__org_behavior_Assignment2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression"):
                opp_val = getattr(old_value, "behavior_Expression", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression"):
                opp_val = getattr(value, "behavior_Expression", None)
                setattr(value, "behavior_Expression", self)

class org_structure_ModelTransformation(MultiplicityElement):

    def __init__(self, isAbstract: str, org_structure_ModelTransformation: set["structure_ModelTypeVariable"] = None, org_structure_ModelTransformation228: "behavior_Expression" = None, org_structure_ModelTransformation231: set["structure_Operation"] = None, ownedTransformations: "structure_ModelTypeDefinition" = None, org_structure_ModelTransformation235: set["structure_Parameter"] = None):
        self.isAbstract = isAbstract
        self.org_structure_ModelTransformation = org_structure_ModelTransformation if org_structure_ModelTransformation is not None else set()
        self.org_structure_ModelTransformation228 = org_structure_ModelTransformation228
        self.org_structure_ModelTransformation231 = org_structure_ModelTransformation231 if org_structure_ModelTransformation231 is not None else set()
        self.ownedTransformations = ownedTransformations
        self.org_structure_ModelTransformation235 = org_structure_ModelTransformation235 if org_structure_ModelTransformation235 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def org_structure_ModelTransformation235(self):
        return self.__org_structure_ModelTransformation235

    @org_structure_ModelTransformation235.setter
    def org_structure_ModelTransformation235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation235", None)
        self.__org_structure_ModelTransformation235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Parameter"):
                    opp_val = getattr(item, "structure_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Parameter"):
                    opp_val = getattr(item, "structure_Parameter", None)
                    
                    setattr(item, "structure_Parameter", self)
                    

    @property
    def org_structure_ModelTransformation231(self):
        return self.__org_structure_ModelTransformation231

    @org_structure_ModelTransformation231.setter
    def org_structure_ModelTransformation231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation231", None)
        self.__org_structure_ModelTransformation231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Operation232"):
                    opp_val = getattr(item, "structure_Operation232", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Operation232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Operation232"):
                    opp_val = getattr(item, "structure_Operation232", None)
                    
                    setattr(item, "structure_Operation232", self)
                    

    @property
    def org_structure_ModelTransformation(self):
        return self.__org_structure_ModelTransformation

    @org_structure_ModelTransformation.setter
    def org_structure_ModelTransformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation", None)
        self.__org_structure_ModelTransformation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_ModelTypeVariable"):
                    opp_val = getattr(item, "structure_ModelTypeVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_ModelTypeVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_ModelTypeVariable"):
                    opp_val = getattr(item, "structure_ModelTypeVariable", None)
                    
                    setattr(item, "structure_ModelTypeVariable", self)
                    

    @property
    def org_structure_ModelTransformation228(self):
        return self.__org_structure_ModelTransformation228

    @org_structure_ModelTransformation228.setter
    def org_structure_ModelTransformation228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation228", None)
        self.__org_structure_ModelTransformation228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression229"):
                opp_val = getattr(old_value, "behavior_Expression229", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression229"):
                opp_val = getattr(value, "behavior_Expression229", None)
                setattr(value, "behavior_Expression229", self)

    @property
    def ownedTransformations(self):
        return self.__ownedTransformations

    @ownedTransformations.setter
    def ownedTransformations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__ownedTransformations", None)
        self.__ownedTransformations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelTypeDefinition"):
                opp_val = getattr(old_value, "ModelTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ModelTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelTypeDefinition"):
                opp_val = getattr(value, "ModelTypeDefinition", None)
                setattr(value, "ModelTypeDefinition", self)

class structure_ModelTypeDefinitionBinding:

    pass
class structure_Metamodel:

    pass
class org_structure_FilteredMetamodelReference(KermetaModelElement):

    pass
class TypeDefinition:

    pass
class org_structure_ModelTypeDefinition(TypeDefinition):

    pass
class org_structure_ModelElementTypeDefinition(TypeDefinition):

    pass
class org_structure_ModelTypeDefinitionContainer(KermetaModelElement):

    pass
class org_structure_UseAdaptationOperator(KermetaModelElement):

    pass
class structure_AdaptationParameter:

    pass
class org_structure_OperationBinding(KermetaModelElement):

    pass
class org_structure_PropertyBinding(KermetaModelElement):

    pass
class org_structure_EnumerationBinding(KermetaModelElement):

    pass
class structure_OperationBinding:

    pass
class structure_PropertyBinding:

    pass
class org_structure_ClassDefinitionBinding(KermetaModelElement):

    pass
class structure_ModelTypeDefinition:

    pass
class org_structure_UnresolvedModelTypeDefinition(structure_UnresolvedReference, structure_ModelTypeDefinition):

    pass
class structure_EnumerationBinding:

    pass
class structure_UseAdaptationOperator:

    pass
class structure_ClassDefinitionBinding:

    pass
class AdaptationOperator:

    pass
class org_structure_OperationAdaptationOperator(AdaptationOperator):

    def __init__(self, body: str, org_structure_OperationAdaptationOperator: "structure_Operation" = None):
        self.body = body
        self.org_structure_OperationAdaptationOperator = org_structure_OperationAdaptationOperator
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def org_structure_OperationAdaptationOperator(self):
        return self.__org_structure_OperationAdaptationOperator

    @org_structure_OperationAdaptationOperator.setter
    def org_structure_OperationAdaptationOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_OperationAdaptationOperator__org_structure_OperationAdaptationOperator", None)
        self.__org_structure_OperationAdaptationOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Operation214"):
                opp_val = getattr(old_value, "structure_Operation214", None)
                if opp_val == self:
                    setattr(old_value, "structure_Operation214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Operation214"):
                opp_val = getattr(value, "structure_Operation214", None)
                setattr(value, "structure_Operation214", self)

class org_structure_PropertyAdaptationOperator(AdaptationOperator):

    def __init__(self, getter: str, setter: str, adder: str, remover: str, org_structure_PropertyAdaptationOperator: "structure_Property" = None):
        self.getter = getter
        self.setter = setter
        self.adder = adder
        self.remover = remover
        self.org_structure_PropertyAdaptationOperator = org_structure_PropertyAdaptationOperator
        
        pass
    @property
    def adder(self):
        return self.__adder

    @adder.setter
    def adder(self, adder: str):
        self.__adder = adder


    @property
    def setter(self):
        return self.__setter

    @setter.setter
    def setter(self, setter: str):
        self.__setter = setter


    @property
    def getter(self):
        return self.__getter

    @getter.setter
    def getter(self, getter: str):
        self.__getter = getter


    @property
    def remover(self):
        return self.__remover

    @remover.setter
    def remover(self, remover: str):
        self.__remover = remover


    @property
    def org_structure_PropertyAdaptationOperator(self):
        return self.__org_structure_PropertyAdaptationOperator

    @org_structure_PropertyAdaptationOperator.setter
    def org_structure_PropertyAdaptationOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_PropertyAdaptationOperator__org_structure_PropertyAdaptationOperator", None)
        self.__org_structure_PropertyAdaptationOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Property212"):
                opp_val = getattr(old_value, "structure_Property212", None)
                if opp_val == self:
                    setattr(old_value, "structure_Property212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Property212"):
                opp_val = getattr(value, "structure_Property212", None)
                setattr(value, "structure_Property212", self)

class org_structure_FunctionType(structure_TypeContainer, structure_Type):

    pass
class org_structure_ProductType(structure_TypeContainer, structure_Type):

    pass
class org_structure_Using(KermetaModelElement):

    def __init__(self, fromQName: str, toName: str):
        self.fromQName = fromQName
        self.toName = toName
        
        pass
    @property
    def toName(self):
        return self.__toName

    @toName.setter
    def toName(self, toName: str):
        self.__toName = toName


    @property
    def fromQName(self):
        return self.__fromQName

    @fromQName.setter
    def fromQName(self, fromQName: str):
        self.__fromQName = fromQName


class org_structure_UnresolvedReference(KermetaModelElement):

    pass
class org_structure_UnresolvedInferredType(structure_UnresolvedReference, structure_Type):

    pass
class structure_ModelTypeVariable:

    pass
class ObjectTypeVariable:

    pass
class org_structure_VirtualType(ObjectTypeVariable):

    pass
class structure_VirtualType:

    pass
class TypeVariable:

    pass
class org_structure_ModelTypeVariable(TypeVariable):

    pass
class org_structure_ObjectTypeVariable(TypeVariable):

    pass
class structure_GenericTypeDefinition:

    pass
class structure_TypeVariableBinding:

    pass
class Type:

    pass
class org_structure_ModelType(Type):

    pass
class org_structure_VoidType(Type):

    pass
class org_structure_ParameterizedType(Type):

    pass
class org_structure_UnresolvedType(structure_UnresolvedReference, structure_TypeContainer, structure_Type):

    def __init__(self, typeIdentifier: str, org_structure_UnresolvedType: set["structure_Using"] = None, org_structure_UnresolvedType162: set["structure_Type"] = None, TypeContainer: "org_structure_Type" = None, structure_Type102: "org_structure_TypeVariableBinding" = None, structure_Type119: "org_structure_PrimitiveType" = None, structure_Type63: "org_behavior_UnresolvedCall" = None, structure_Type121: "org_structure_TypedElement" = None, structure_Type71: "org_structure_Operation" = None, structure_Type: "org_behavior_Expression" = None, structure_Type165: "org_structure_ProductType" = None, structure_Type167: "org_structure_FunctionType" = None, Type: "org_structure_TypeContainer" = None, structure_Type60: "org_behavior_UnresolvedCall" = None, structure_Type150: "org_structure_TypeVariable" = None, structure_Type16: "org_behavior_CallSuperOperation" = None, structure_Type8: "org_behavior_CallExpression" = None, structure_Type104: "org_structure_TypeDefinition" = None, structure_Type170: "org_structure_FunctionType" = None, structure_Type163: "org_structure_UnresolvedType" = None, structure_UnresolvedReference: "org_structure_UseAdaptationOperator" = None):
        self.typeIdentifier = typeIdentifier
        self.org_structure_UnresolvedType = org_structure_UnresolvedType if org_structure_UnresolvedType is not None else set()
        self.org_structure_UnresolvedType162 = org_structure_UnresolvedType162 if org_structure_UnresolvedType162 is not None else set()
        
        pass
    @property
    def typeIdentifier(self):
        return self.__typeIdentifier

    @typeIdentifier.setter
    def typeIdentifier(self, typeIdentifier: str):
        self.__typeIdentifier = typeIdentifier


    @property
    def org_structure_UnresolvedType162(self):
        return self.__org_structure_UnresolvedType162

    @org_structure_UnresolvedType162.setter
    def org_structure_UnresolvedType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_UnresolvedType__org_structure_UnresolvedType162", None)
        self.__org_structure_UnresolvedType162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type163"):
                    opp_val = getattr(item, "structure_Type163", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type163"):
                    opp_val = getattr(item, "structure_Type163", None)
                    
                    setattr(item, "structure_Type163", self)
                    

    @property
    def org_structure_UnresolvedType(self):
        return self.__org_structure_UnresolvedType

    @org_structure_UnresolvedType.setter
    def org_structure_UnresolvedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_UnresolvedType__org_structure_UnresolvedType", None)
        self.__org_structure_UnresolvedType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Using160"):
                    opp_val = getattr(item, "structure_Using160", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Using160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Using160"):
                    opp_val = getattr(item, "structure_Using160", None)
                    
                    setattr(item, "structure_Using160", self)
                    

class org_structure_AbstractOperation(KermetaModelElement):

    pass
class org_structure_Model(KermetaModelElement):

    pass
class structure_FilteredMetamodelReference:

    pass
class structure_ModelTypeDefinitionContainer:

    pass
class org_structure_ModelTypeDefinitionBinding(structure_KermetaModelElement, structure_ModelTypeDefinitionContainer):

    pass
class GenericTypeDefinition:

    pass
class org_structure_ClassDefinition(GenericTypeDefinition):

    def __init__(self, isAbstract: str, isSingleton: str, isFinal: str, invOwner: set["structure_Constraint"] = None, owningClass: set["structure_Property"] = None, owningClass135: set["structure_Operation"] = None):
        self.isAbstract = isAbstract
        self.isSingleton = isSingleton
        self.isFinal = isFinal
        self.invOwner = invOwner if invOwner is not None else set()
        self.owningClass = owningClass if owningClass is not None else set()
        self.owningClass135 = owningClass135 if owningClass135 is not None else set()
        
        pass
    @property
    def isFinal(self):
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: str):
        self.__isFinal = isFinal


    @property
    def isSingleton(self):
        return self.__isSingleton

    @isSingleton.setter
    def isSingleton(self, isSingleton: str):
        self.__isSingleton = isSingleton


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def invOwner(self):
        return self.__invOwner

    @invOwner.setter
    def invOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ClassDefinition__invOwner", None)
        self.__invOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint132"):
                    opp_val = getattr(item, "Constraint132", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint132"):
                    opp_val = getattr(item, "Constraint132", None)
                    
                    setattr(item, "Constraint132", self)
                    

    @property
    def owningClass135(self):
        return self.__owningClass135

    @owningClass135.setter
    def owningClass135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ClassDefinition__owningClass135", None)
        self.__owningClass135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation136"):
                    opp_val = getattr(item, "Operation136", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation136"):
                    opp_val = getattr(item, "Operation136", None)
                    
                    setattr(item, "Operation136", self)
                    

    @property
    def owningClass(self):
        return self.__owningClass

    @owningClass.setter
    def owningClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ClassDefinition__owningClass", None)
        self.__owningClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

class ModelElementTypeDefinition:

    pass
class org_structure_GenericTypeDefinition(ModelElementTypeDefinition):

    pass
class org_structure_AbstractProperty(KermetaModelElement):

    pass
class org_structure_Tag(KermetaModelElement):

    def __init__(self, name: str, value: str, kTag: set["structure_KermetaModelElement"] = None):
        self.name = name
        self.value = value
        self.kTag = kTag if kTag is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kTag(self):
        return self.__kTag

    @kTag.setter
    def kTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Tag__kTag", None)
        self.__kTag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KermetaModelElement"):
                    opp_val = getattr(item, "KermetaModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "KermetaModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KermetaModelElement"):
                    opp_val = getattr(item, "KermetaModelElement", None)
                    
                    setattr(item, "KermetaModelElement", self)
                    

class org_structure_Parameter(MultiplicityElement):

    pass
class structure_Package:

    pass
class structure_ModelElementTypeDefinitionContainer:

    pass
class org_structure_NamedElement(KermetaModelElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class DataType:

    pass
class org_structure_PrimitiveType(DataType):

    pass
class org_structure_Enumeration(DataType):

    pass
class structure_ModelElementTypeDefinition:

    pass
class org_structure_DataType(structure_ModelElementTypeDefinition, structure_Type):

    pass
class structure_Class:

    pass
class structure_AdaptationOperator:

    pass
class org_structure_UnresolvedAdaptationOperator(structure_AdaptationOperator, structure_UnresolvedReference):

    pass
class structure_NamedElement:

    pass
class org_structure_Package(structure_NamedElement, structure_ModelElementTypeDefinitionContainer):

    def __init__(self, uri: str, nestedPackage: "structure_Package" = None, org_structure_Package: set["structure_AdaptationOperator"] = None, nestingPackage: set["structure_Package"] = None):
        self.uri = uri
        self.nestedPackage = nestedPackage
        self.org_structure_Package = org_structure_Package if org_structure_Package is not None else set()
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package115"):
                opp_val = getattr(old_value, "Package115", None)
                if opp_val == self:
                    setattr(old_value, "Package115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package115"):
                opp_val = getattr(value, "Package115", None)
                setattr(value, "Package115", self)

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def org_structure_Package(self):
        return self.__org_structure_Package

    @org_structure_Package.setter
    def org_structure_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Package__org_structure_Package", None)
        self.__org_structure_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_AdaptationOperator"):
                    opp_val = getattr(item, "structure_AdaptationOperator", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_AdaptationOperator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_AdaptationOperator"):
                    opp_val = getattr(item, "structure_AdaptationOperator", None)
                    
                    setattr(item, "structure_AdaptationOperator", self)
                    

class org_structure_TypeVariable(structure_TypeContainer, structure_NamedElement, structure_Type):

    pass
class org_structure_TypedElement(structure_TypeContainer, structure_NamedElement):

    pass
class org_structure_Metamodel(structure_KermetaModelElement, structure_NamedElement, structure_ModelTypeDefinitionContainer):

    def __init__(self, uri: str, isResolved: bool, org_structure_Metamodel: set["structure_Package"] = None, org_structure_Metamodel139: set["structure_FilteredMetamodelReference"] = None, structure_KermetaModelElement205: "org_structure_UseAdaptationOperator" = None, KermetaModelElement: "org_structure_Tag" = None, structure_KermetaModelElement: "org_structure_Model" = None):
        self.uri = uri
        self.isResolved = isResolved
        self.org_structure_Metamodel = org_structure_Metamodel if org_structure_Metamodel is not None else set()
        self.org_structure_Metamodel139 = org_structure_Metamodel139 if org_structure_Metamodel139 is not None else set()
        
        pass
    @property
    def isResolved(self):
        return self.__isResolved

    @isResolved.setter
    def isResolved(self, isResolved: bool):
        self.__isResolved = isResolved


    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def org_structure_Metamodel(self):
        return self.__org_structure_Metamodel

    @org_structure_Metamodel.setter
    def org_structure_Metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Metamodel__org_structure_Metamodel", None)
        self.__org_structure_Metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Package"):
                    opp_val = getattr(item, "structure_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Package"):
                    opp_val = getattr(item, "structure_Package", None)
                    
                    setattr(item, "structure_Package", self)
                    

    @property
    def org_structure_Metamodel139(self):
        return self.__org_structure_Metamodel139

    @org_structure_Metamodel139.setter
    def org_structure_Metamodel139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Metamodel__org_structure_Metamodel139", None)
        self.__org_structure_Metamodel139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_FilteredMetamodelReference"):
                    opp_val = getattr(item, "structure_FilteredMetamodelReference", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_FilteredMetamodelReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_FilteredMetamodelReference"):
                    opp_val = getattr(item, "structure_FilteredMetamodelReference", None)
                    
                    setattr(item, "structure_FilteredMetamodelReference", self)
                    

class org_structure_TypeDefinition(structure_TypeContainer, structure_NamedElement):

    def __init__(self, isAspect: str, org_structure_TypeDefinition: set["structure_Type"] = None, TypeContainer: "org_structure_Type" = None):
        self.isAspect = isAspect
        self.org_structure_TypeDefinition = org_structure_TypeDefinition if org_structure_TypeDefinition is not None else set()
        
        pass
    @property
    def isAspect(self):
        return self.__isAspect

    @isAspect.setter
    def isAspect(self, isAspect: str):
        self.__isAspect = isAspect


    @property
    def org_structure_TypeDefinition(self):
        return self.__org_structure_TypeDefinition

    @org_structure_TypeDefinition.setter
    def org_structure_TypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_TypeDefinition__org_structure_TypeDefinition", None)
        self.__org_structure_TypeDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type104"):
                    opp_val = getattr(item, "structure_Type104", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type104"):
                    opp_val = getattr(item, "structure_Type104", None)
                    
                    setattr(item, "structure_Type104", self)
                    

class TypedElement:

    pass
class org_structure_AdaptationParameter(TypedElement):

    pass
class org_structure_MultiplicityElement(TypedElement):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


class org_structure_TypeVariableBinding(structure_TypeContainer, structure_KermetaModelElement):

    pass
class structure_Enumeration:

    pass
class NamedElement:

    pass
class org_structure_Constraint(NamedElement):

    def __init__(self, stereotype: str, language: str, org_structure_Constraint: "behavior_Expression" = None, inv: "structure_ClassDefinition" = None, pre: "structure_Operation" = None, post: "structure_Operation" = None):
        self.stereotype = stereotype
        self.language = language
        self.org_structure_Constraint = org_structure_Constraint
        self.inv = inv
        self.pre = pre
        self.post = post
        
        pass
    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def pre(self):
        return self.__pre

    @pre.setter
    def pre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__pre", None)
        self.__pre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation128"):
                opp_val = getattr(old_value, "Operation128", None)
                if opp_val == self:
                    setattr(old_value, "Operation128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation128"):
                opp_val = getattr(value, "Operation128", None)
                setattr(value, "Operation128", self)

    @property
    def post(self):
        return self.__post

    @post.setter
    def post(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__post", None)
        self.__post = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation130"):
                opp_val = getattr(old_value, "Operation130", None)
                if opp_val == self:
                    setattr(old_value, "Operation130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation130"):
                opp_val = getattr(value, "Operation130", None)
                setattr(value, "Operation130", self)

    @property
    def inv(self):
        return self.__inv

    @inv.setter
    def inv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__inv", None)
        self.__inv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDefinition126"):
                opp_val = getattr(old_value, "ClassDefinition126", None)
                if opp_val == self:
                    setattr(old_value, "ClassDefinition126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDefinition126"):
                opp_val = getattr(value, "ClassDefinition126", None)
                setattr(value, "ClassDefinition126", self)

    @property
    def org_structure_Constraint(self):
        return self.__org_structure_Constraint

    @org_structure_Constraint.setter
    def org_structure_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__org_structure_Constraint", None)
        self.__org_structure_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression124"):
                opp_val = getattr(old_value, "behavior_Expression124", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression124"):
                opp_val = getattr(value, "behavior_Expression124", None)
                setattr(value, "behavior_Expression124", self)

class org_structure_AdaptationOperator(NamedElement):

    pass
class org_structure_ModelElementTypeDefinitionContainer(NamedElement):

    pass
class org_structure_EnumerationLiteral(NamedElement):

    pass
class org_structure_TypeContainer(KermetaModelElement):

    pass
class ParameterizedType:

    pass
class org_structure_Class(ParameterizedType):

    def __init__(self, isAbstract: str, name: str, org_structure_Class: set["structure_Property"] = None, org_structure_Class108: set["structure_Operation"] = None, org_structure_Class111: set["structure_Class"] = None):
        self.isAbstract = isAbstract
        self.name = name
        self.org_structure_Class = org_structure_Class if org_structure_Class is not None else set()
        self.org_structure_Class108 = org_structure_Class108 if org_structure_Class108 is not None else set()
        self.org_structure_Class111 = org_structure_Class111 if org_structure_Class111 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def org_structure_Class108(self):
        return self.__org_structure_Class108

    @org_structure_Class108.setter
    def org_structure_Class108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Class__org_structure_Class108", None)
        self.__org_structure_Class108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Operation109"):
                    opp_val = getattr(item, "structure_Operation109", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Operation109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Operation109"):
                    opp_val = getattr(item, "structure_Operation109", None)
                    
                    setattr(item, "structure_Operation109", self)
                    

    @property
    def org_structure_Class111(self):
        return self.__org_structure_Class111

    @org_structure_Class111.setter
    def org_structure_Class111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Class__org_structure_Class111", None)
        self.__org_structure_Class111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Class"):
                    opp_val = getattr(item, "structure_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Class"):
                    opp_val = getattr(item, "structure_Class", None)
                    
                    setattr(item, "structure_Class", self)
                    

    @property
    def org_structure_Class(self):
        return self.__org_structure_Class

    @org_structure_Class.setter
    def org_structure_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Class__org_structure_Class", None)
        self.__org_structure_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Property106"):
                    opp_val = getattr(item, "structure_Property106", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Property106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Property106"):
                    opp_val = getattr(item, "structure_Property106", None)
                    
                    setattr(item, "structure_Property106", self)
                    

class structure_UnresolvedProperty:

    pass
class structure_AbstractProperty:

    pass
class org_structure_UnresolvedProperty(structure_UnresolvedReference, structure_AbstractProperty):

    def __init__(self, propertyIdentifier: str, structure_AbstractProperty: "org_structure_Property" = None, structure_UnresolvedReference: "org_structure_UseAdaptationOperator" = None):
        self.propertyIdentifier = propertyIdentifier
        
        pass
    @property
    def propertyIdentifier(self):
        return self.__propertyIdentifier

    @propertyIdentifier.setter
    def propertyIdentifier(self, propertyIdentifier: str):
        self.__propertyIdentifier = propertyIdentifier


class structure_TypeVariable:

    pass
class org_structure_UnresolvedTypeVariable(structure_UnresolvedReference, structure_TypeVariable):

    pass
class structure_ClassDefinition:

    pass
class org_structure_Type(KermetaModelElement):

    pass
class structure_Constraint:

    pass
class structure_Parameter:

    pass
class structure_AbstractOperation:

    pass
class org_structure_UnresolvedOperation(structure_UnresolvedReference, structure_TypeContainer, structure_AbstractOperation):

    def __init__(self, operationIdentifier: str, TypeContainer: "org_structure_Type" = None, structure_UnresolvedReference: "org_structure_UseAdaptationOperator" = None):
        self.operationIdentifier = operationIdentifier
        
        pass
    @property
    def operationIdentifier(self):
        return self.__operationIdentifier

    @operationIdentifier.setter
    def operationIdentifier(self, operationIdentifier: str):
        self.__operationIdentifier = operationIdentifier


class structure_MultiplicityElement:

    pass
class org_structure_Property(structure_AbstractProperty, structure_MultiplicityElement):

    def __init__(self, isReadOnly: str, default: str, isComposite: str, isDerived: str, isID: str, isGetterAbstract: str, isSetterAbstract: str, org_structure_Property: "structure_AbstractProperty" = None, org_structure_Property86: "behavior_Expression" = None, org_structure_Property89: "behavior_Expression" = None, org_structure_Property92: set["structure_UnresolvedProperty"] = None, ownedAttribute: "structure_ClassDefinition" = None, structure_AbstractProperty: "org_structure_Property" = None):
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isGetterAbstract = isGetterAbstract
        self.isSetterAbstract = isSetterAbstract
        self.org_structure_Property = org_structure_Property
        self.org_structure_Property86 = org_structure_Property86
        self.org_structure_Property89 = org_structure_Property89
        self.org_structure_Property92 = org_structure_Property92 if org_structure_Property92 is not None else set()
        self.ownedAttribute = ownedAttribute
        
        pass
    @property
    def isSetterAbstract(self):
        return self.__isSetterAbstract

    @isSetterAbstract.setter
    def isSetterAbstract(self, isSetterAbstract: str):
        self.__isSetterAbstract = isSetterAbstract


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


    @property
    def isGetterAbstract(self):
        return self.__isGetterAbstract

    @isGetterAbstract.setter
    def isGetterAbstract(self, isGetterAbstract: str):
        self.__isGetterAbstract = isGetterAbstract


    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def org_structure_Property86(self):
        return self.__org_structure_Property86

    @org_structure_Property86.setter
    def org_structure_Property86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property86", None)
        self.__org_structure_Property86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression87"):
                opp_val = getattr(old_value, "behavior_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression87"):
                opp_val = getattr(value, "behavior_Expression87", None)
                setattr(value, "behavior_Expression87", self)

    @property
    def org_structure_Property(self):
        return self.__org_structure_Property

    @org_structure_Property.setter
    def org_structure_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property", None)
        self.__org_structure_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_AbstractProperty"):
                opp_val = getattr(old_value, "structure_AbstractProperty", None)
                if opp_val == self:
                    setattr(old_value, "structure_AbstractProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_AbstractProperty"):
                opp_val = getattr(value, "structure_AbstractProperty", None)
                setattr(value, "structure_AbstractProperty", self)

    @property
    def org_structure_Property89(self):
        return self.__org_structure_Property89

    @org_structure_Property89.setter
    def org_structure_Property89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property89", None)
        self.__org_structure_Property89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression90"):
                opp_val = getattr(old_value, "behavior_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression90"):
                opp_val = getattr(value, "behavior_Expression90", None)
                setattr(value, "behavior_Expression90", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDefinition94"):
                opp_val = getattr(old_value, "ClassDefinition94", None)
                if opp_val == self:
                    setattr(old_value, "ClassDefinition94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDefinition94"):
                opp_val = getattr(value, "ClassDefinition94", None)
                setattr(value, "ClassDefinition94", self)

    @property
    def org_structure_Property92(self):
        return self.__org_structure_Property92

    @org_structure_Property92.setter
    def org_structure_Property92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property92", None)
        self.__org_structure_Property92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_UnresolvedProperty"):
                    opp_val = getattr(item, "structure_UnresolvedProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_UnresolvedProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_UnresolvedProperty"):
                    opp_val = getattr(item, "structure_UnresolvedProperty", None)
                    
                    setattr(item, "structure_UnresolvedProperty", self)
                    

class org_structure_Operation(structure_AbstractOperation, structure_MultiplicityElement):

    def __init__(self, isAbstract: str, uniqueName: str, postOwner: set["structure_Constraint"] = None, org_structure_Operation77: "behavior_Expression" = None, org_structure_Operation80: set["structure_UnresolvedOperation"] = None, org_structure_Operation: set["structure_Type"] = None, operation: set["structure_Parameter"] = None, preOwner: set["structure_Constraint"] = None, ownedOperation: "structure_ClassDefinition" = None, org_structure_Operation83: set["structure_TypeVariable"] = None):
        self.isAbstract = isAbstract
        self.uniqueName = uniqueName
        self.postOwner = postOwner if postOwner is not None else set()
        self.org_structure_Operation77 = org_structure_Operation77
        self.org_structure_Operation80 = org_structure_Operation80 if org_structure_Operation80 is not None else set()
        self.org_structure_Operation = org_structure_Operation if org_structure_Operation is not None else set()
        self.operation = operation if operation is not None else set()
        self.preOwner = preOwner if preOwner is not None else set()
        self.ownedOperation = ownedOperation
        self.org_structure_Operation83 = org_structure_Operation83 if org_structure_Operation83 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def uniqueName(self):
        return self.__uniqueName

    @uniqueName.setter
    def uniqueName(self, uniqueName: str):
        self.__uniqueName = uniqueName


    @property
    def preOwner(self):
        return self.__preOwner

    @preOwner.setter
    def preOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__preOwner", None)
        self.__preOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def org_structure_Operation(self):
        return self.__org_structure_Operation

    @org_structure_Operation.setter
    def org_structure_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation", None)
        self.__org_structure_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type71"):
                    opp_val = getattr(item, "structure_Type71", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type71"):
                    opp_val = getattr(item, "structure_Type71", None)
                    
                    setattr(item, "structure_Type71", self)
                    

    @property
    def org_structure_Operation80(self):
        return self.__org_structure_Operation80

    @org_structure_Operation80.setter
    def org_structure_Operation80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation80", None)
        self.__org_structure_Operation80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_UnresolvedOperation"):
                    opp_val = getattr(item, "structure_UnresolvedOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_UnresolvedOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_UnresolvedOperation"):
                    opp_val = getattr(item, "structure_UnresolvedOperation", None)
                    
                    setattr(item, "structure_UnresolvedOperation", self)
                    

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDefinition"):
                opp_val = getattr(old_value, "ClassDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ClassDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDefinition"):
                opp_val = getattr(value, "ClassDefinition", None)
                setattr(value, "ClassDefinition", self)

    @property
    def postOwner(self):
        return self.__postOwner

    @postOwner.setter
    def postOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__postOwner", None)
        self.__postOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint75"):
                    opp_val = getattr(item, "Constraint75", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint75"):
                    opp_val = getattr(item, "Constraint75", None)
                    
                    setattr(item, "Constraint75", self)
                    

    @property
    def org_structure_Operation83(self):
        return self.__org_structure_Operation83

    @org_structure_Operation83.setter
    def org_structure_Operation83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation83", None)
        self.__org_structure_Operation83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_TypeVariable"):
                    opp_val = getattr(item, "structure_TypeVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_TypeVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_TypeVariable"):
                    opp_val = getattr(item, "structure_TypeVariable", None)
                    
                    setattr(item, "structure_TypeVariable", self)
                    

    @property
    def org_structure_Operation77(self):
        return self.__org_structure_Operation77

    @org_structure_Operation77.setter
    def org_structure_Operation77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation77", None)
        self.__org_structure_Operation77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression78"):
                opp_val = getattr(old_value, "behavior_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression78"):
                opp_val = getattr(value, "behavior_Expression78", None)
                setattr(value, "behavior_Expression78", self)

class structure_Tag:

    pass
class org_structure_KermetaModelElement(ABC):

    pass
class structure_ModelTransformation:

    pass
class org_structure_UnresolvedModelTransformation(structure_UnresolvedReference, structure_ModelTransformation):

    pass
class org_behavior_CallModelTransformation(CallFeature):

    pass
class structure_EnumerationLiteral:

    pass
class org_behavior_CallEnumLiteral(CallExpression):

    pass
class structure_Property:

    pass
class org_behavior_CallProperty(CallFeature):

    pass
class structure_Operation:

    pass