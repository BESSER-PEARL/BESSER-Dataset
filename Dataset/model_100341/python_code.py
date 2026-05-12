from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Constant:

    pass
class AsmL_NullConstant(Constant):

    pass
class AsmL_StringConstant(Constant):

    def __init__(self, val: str):
        self.val = val
        
        pass
    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val


class AsmL_IntegerConstant(Constant):

    def __init__(self, val: str):
        self.val = val
        
        pass
    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val


class AsmL_BooleanConstant(Constant):

    def __init__(self, val: str):
        self.val = val
        
        pass
    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val


class SequenceTerm:

    pass
class AsmL_RangeSequence(SequenceTerm):

    pass
class AsmL_EnumerateSequence(SequenceTerm):

    pass
class SetTerm:

    pass
class AsmL_AlgorithmSet(SetTerm):

    pass
class AsmL_RangeSet(SetTerm):

    pass
class AsmL_EnumerateSet(SetTerm):

    pass
class Class:

    pass
class Enumerator:

    pass
class Structure:

    pass
class VarDeclaration:

    pass
class Type:

    pass
class VarOrMethod:

    pass
class VarOrCase:

    pass
class AsmL_Case(VarOrCase):

    def __init__(self, name: str, AsmL_Case: set["VarDeclaration"] = None, VarOrCase: "AsmL_Structure" = None):
        self.name = name
        self.AsmL_Case = AsmL_Case if AsmL_Case is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def AsmL_Case(self):
        return self.__AsmL_Case

    @AsmL_Case.setter
    def AsmL_Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Case__AsmL_Case", None)
        self.__AsmL_Case = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarDeclaration"):
                    opp_val = getattr(item, "VarDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "VarDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarDeclaration"):
                    opp_val = getattr(item, "VarDeclaration", None)
                    
                    setattr(item, "VarDeclaration", self)
                    

class AsmLFile:

    pass
class Main:

    pass
class AsmLElement:

    pass
class AsmL_Namespace(AsmLElement):

    def __init__(self, name: str, AsmLElement: "AsmL_AsmLFile" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AsmL_Class(AsmLElement):

    def __init__(self, name: str, isAbstract: str, superClassName: str, ownerClass: set["VarOrMethod"] = None, AsmLElement: "AsmL_AsmLFile" = None):
        self.name = name
        self.isAbstract = isAbstract
        self.superClassName = superClassName
        self.ownerClass = ownerClass if ownerClass is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def superClassName(self):
        return self.__superClassName

    @superClassName.setter
    def superClassName(self, superClassName: str):
        self.__superClassName = superClassName


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def ownerClass(self):
        return self.__ownerClass

    @ownerClass.setter
    def ownerClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Class__ownerClass", None)
        self.__ownerClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarOrMethod"):
                    opp_val = getattr(item, "VarOrMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "VarOrMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarOrMethod"):
                    opp_val = getattr(item, "VarOrMethod", None)
                    
                    setattr(item, "VarOrMethod", self)
                    

class AsmL_Structure(AsmLElement):

    def __init__(self, name: str, superStructureName: str, ownerStructure: set["VarOrCase"] = None, AsmLElement: "AsmL_AsmLFile" = None):
        self.name = name
        self.superStructureName = superStructureName
        self.ownerStructure = ownerStructure if ownerStructure is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def superStructureName(self):
        return self.__superStructureName

    @superStructureName.setter
    def superStructureName(self, superStructureName: str):
        self.__superStructureName = superStructureName


    @property
    def ownerStructure(self):
        return self.__ownerStructure

    @ownerStructure.setter
    def ownerStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Structure__ownerStructure", None)
        self.__ownerStructure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarOrCase"):
                    opp_val = getattr(item, "VarOrCase", None)
                    
                    if opp_val == self:
                        setattr(item, "VarOrCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarOrCase"):
                    opp_val = getattr(item, "VarOrCase", None)
                    
                    setattr(item, "VarOrCase", self)
                    

class AsmL_VarDeclaration(VarOrCase, AsmLElement, VarOrMethod):

    def __init__(self, isLocal: str, name: str, isConstant: str, isDeclaration: str, ownerDeclaration: "Type" = None, AsmLElement: "AsmL_AsmLFile" = None, VarOrCase: "AsmL_Structure" = None, VarOrMethod: "AsmL_Class" = None):
        self.isLocal = isLocal
        self.name = name
        self.isConstant = isConstant
        self.isDeclaration = isDeclaration
        self.ownerDeclaration = ownerDeclaration
        
        pass
    @property
    def isConstant(self):
        return self.__isConstant

    @isConstant.setter
    def isConstant(self, isConstant: str):
        self.__isConstant = isConstant


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isDeclaration(self):
        return self.__isDeclaration

    @isDeclaration.setter
    def isDeclaration(self, isDeclaration: str):
        self.__isDeclaration = isDeclaration


    @property
    def isLocal(self):
        return self.__isLocal

    @isLocal.setter
    def isLocal(self, isLocal: str):
        self.__isLocal = isLocal


    @property
    def ownerDeclaration(self):
        return self.__ownerDeclaration

    @ownerDeclaration.setter
    def ownerDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_VarDeclaration__ownerDeclaration", None)
        self.__ownerDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

class AsmL_Function(AsmLElement):

    def __init__(self, name: str, AsmL_Function: "Body" = None, AsmLElement: "AsmL_AsmLFile" = None):
        self.name = name
        self.AsmL_Function = AsmL_Function
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def AsmL_Function(self):
        return self.__AsmL_Function

    @AsmL_Function.setter
    def AsmL_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Function__AsmL_Function", None)
        self.__AsmL_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Body"):
                opp_val = getattr(old_value, "Body", None)
                if opp_val == self:
                    setattr(old_value, "Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Body"):
                opp_val = getattr(value, "Body", None)
                setattr(value, "Body", self)

class AsmL_Enumeration(AsmLElement):

    def __init__(self, name: str, AsmL_Enumeration: set["Enumerator"] = None, AsmLElement: "AsmL_AsmLFile" = None):
        self.name = name
        self.AsmL_Enumeration = AsmL_Enumeration if AsmL_Enumeration is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def AsmL_Enumeration(self):
        return self.__AsmL_Enumeration

    @AsmL_Enumeration.setter
    def AsmL_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Enumeration__AsmL_Enumeration", None)
        self.__AsmL_Enumeration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Enumerator"):
                    opp_val = getattr(item, "Enumerator", None)
                    
                    if opp_val == self:
                        setattr(item, "Enumerator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Enumerator"):
                    opp_val = getattr(item, "Enumerator", None)
                    
                    setattr(item, "Enumerator", self)
                    

class Term:

    pass
class AsmL_PredicateTerm(Term):

    pass
class AsmL_SequenceTerm(Term):

    pass
class AsmL_Constant(Term):

    pass
class Rule:

    pass
class LocatedElement:

    pass
class AsmL_VarOrCase(LocatedElement):

    pass
class AsmL_AsmLFile(LocatedElement):

    pass
class AsmL_AsmLElement(LocatedElement):

    pass
class AsmL_Enumerator(LocatedElement):

    def __init__(self, name: str, AsmL_Enumerator: "Term" = None):
        self.name = name
        self.AsmL_Enumerator = AsmL_Enumerator
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def AsmL_Enumerator(self):
        return self.__AsmL_Enumerator

    @AsmL_Enumerator.setter
    def AsmL_Enumerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Enumerator__AsmL_Enumerator", None)
        self.__AsmL_Enumerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term22"):
                opp_val = getattr(old_value, "Term22", None)
                if opp_val == self:
                    setattr(old_value, "Term22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term22"):
                opp_val = getattr(value, "Term22", None)
                setattr(value, "Term22", self)

class AsmL_InWhereHolds(LocatedElement):

    pass
class AsmL_VarOrMethod(LocatedElement):

    pass
class AsmL_Body(LocatedElement):

    pass
class AsmL_LocatedElement(ABC):

    def __init__(self, commentsAfter: str, location: str, commentsBefore: str):
        self.commentsAfter = commentsAfter
        self.location = location
        self.commentsBefore = commentsBefore
        
        pass
    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


class AsmL_SetTerm(Term):

    pass
class PredicateTerm:

    pass
class AsmL_ExistsTerm(PredicateTerm):

    def __init__(self, isUnique: str):
        self.isUnique = isUnique
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


class AsmL_AnyIn(PredicateTerm):

    pass
class AsmL_ForAllTerm(PredicateTerm):

    pass
class AsmL_MethodCallTerm(Term):

    def __init__(self, name: str, AsmL_MethodCallTerm: set["Term"] = None, Term: "AsmL_InWhereHolds" = None, Term114: "AsmL_MapTerm" = None, Term112: "AsmL_Operator" = None, Term79: "AsmL_ReturnRule" = None, Term136: "AsmL_RangeSequence" = None, Term37: "AsmL_Initially" = None, Term139: "AsmL_RangeSequence" = None, Term45: "AsmL_UpdateRule" = None, Term130: "AsmL_RangeSet" = None, Term4: "AsmL_InWhereHolds" = None, Term22: "AsmL_Enumerator" = None, Term86: "AsmL_RemoveRule" = None, Term10: "AsmL_InWhereHolds" = None, Term117: "AsmL_MapTerm" = None, Term121: "AsmL_MethodCallTerm" = None, Term69: "AsmL_ConditionalRule" = None, Term41: "AsmL_StepExpression" = None, Term7: "AsmL_InWhereHolds" = None, Term119: "AsmL_TulpletTerm" = None, Term125: "AsmL_EnumerateSet" = None, Term54: "AsmL_UpdateMapRule" = None, Term109: "AsmL_Operator" = None, Term81: "AsmL_AddRule" = None, Term134: "AsmL_EnumerateSequence" = None, Term47: "AsmL_UpdateVarRule" = None, Term127: "AsmL_RangeSet" = None):
        self.name = name
        self.AsmL_MethodCallTerm = AsmL_MethodCallTerm if AsmL_MethodCallTerm is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def AsmL_MethodCallTerm(self):
        return self.__AsmL_MethodCallTerm

    @AsmL_MethodCallTerm.setter
    def AsmL_MethodCallTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_MethodCallTerm__AsmL_MethodCallTerm", None)
        self.__AsmL_MethodCallTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Term121"):
                    opp_val = getattr(item, "Term121", None)
                    
                    if opp_val == self:
                        setattr(item, "Term121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Term121"):
                    opp_val = getattr(item, "Term121", None)
                    
                    setattr(item, "Term121", self)
                    

class AsmL_TulpletTerm(Term):

    pass
class AsmL_Operator(Term):

    def __init__(self, opName: str, AsmL_Operator: "Term" = None, AsmL_Operator111: "Term" = None, Term: "AsmL_InWhereHolds" = None, Term114: "AsmL_MapTerm" = None, Term112: "AsmL_Operator" = None, Term79: "AsmL_ReturnRule" = None, Term136: "AsmL_RangeSequence" = None, Term37: "AsmL_Initially" = None, Term139: "AsmL_RangeSequence" = None, Term45: "AsmL_UpdateRule" = None, Term130: "AsmL_RangeSet" = None, Term4: "AsmL_InWhereHolds" = None, Term22: "AsmL_Enumerator" = None, Term86: "AsmL_RemoveRule" = None, Term10: "AsmL_InWhereHolds" = None, Term117: "AsmL_MapTerm" = None, Term121: "AsmL_MethodCallTerm" = None, Term69: "AsmL_ConditionalRule" = None, Term41: "AsmL_StepExpression" = None, Term7: "AsmL_InWhereHolds" = None, Term119: "AsmL_TulpletTerm" = None, Term125: "AsmL_EnumerateSet" = None, Term54: "AsmL_UpdateMapRule" = None, Term109: "AsmL_Operator" = None, Term81: "AsmL_AddRule" = None, Term134: "AsmL_EnumerateSequence" = None, Term47: "AsmL_UpdateVarRule" = None, Term127: "AsmL_RangeSet" = None):
        self.opName = opName
        self.AsmL_Operator = AsmL_Operator
        self.AsmL_Operator111 = AsmL_Operator111
        
        pass
    @property
    def opName(self):
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName


    @property
    def AsmL_Operator111(self):
        return self.__AsmL_Operator111

    @AsmL_Operator111.setter
    def AsmL_Operator111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Operator__AsmL_Operator111", None)
        self.__AsmL_Operator111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term112"):
                opp_val = getattr(old_value, "Term112", None)
                if opp_val == self:
                    setattr(old_value, "Term112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term112"):
                opp_val = getattr(value, "Term112", None)
                setattr(value, "Term112", self)

    @property
    def AsmL_Operator(self):
        return self.__AsmL_Operator

    @AsmL_Operator.setter
    def AsmL_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Operator__AsmL_Operator", None)
        self.__AsmL_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term109"):
                opp_val = getattr(old_value, "Term109", None)
                if opp_val == self:
                    setattr(old_value, "Term109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term109"):
                opp_val = getattr(value, "Term109", None)
                setattr(value, "Term109", self)

class AsmL_MapTerm(Term):

    def __init__(self, separator: str, AsmL_MapTerm: "Term" = None, AsmL_MapTerm116: "Term" = None, Term: "AsmL_InWhereHolds" = None, Term114: "AsmL_MapTerm" = None, Term112: "AsmL_Operator" = None, Term79: "AsmL_ReturnRule" = None, Term136: "AsmL_RangeSequence" = None, Term37: "AsmL_Initially" = None, Term139: "AsmL_RangeSequence" = None, Term45: "AsmL_UpdateRule" = None, Term130: "AsmL_RangeSet" = None, Term4: "AsmL_InWhereHolds" = None, Term22: "AsmL_Enumerator" = None, Term86: "AsmL_RemoveRule" = None, Term10: "AsmL_InWhereHolds" = None, Term117: "AsmL_MapTerm" = None, Term121: "AsmL_MethodCallTerm" = None, Term69: "AsmL_ConditionalRule" = None, Term41: "AsmL_StepExpression" = None, Term7: "AsmL_InWhereHolds" = None, Term119: "AsmL_TulpletTerm" = None, Term125: "AsmL_EnumerateSet" = None, Term54: "AsmL_UpdateMapRule" = None, Term109: "AsmL_Operator" = None, Term81: "AsmL_AddRule" = None, Term134: "AsmL_EnumerateSequence" = None, Term47: "AsmL_UpdateVarRule" = None, Term127: "AsmL_RangeSet" = None):
        self.separator = separator
        self.AsmL_MapTerm = AsmL_MapTerm
        self.AsmL_MapTerm116 = AsmL_MapTerm116
        
        pass
    @property
    def separator(self):
        return self.__separator

    @separator.setter
    def separator(self, separator: str):
        self.__separator = separator


    @property
    def AsmL_MapTerm(self):
        return self.__AsmL_MapTerm

    @AsmL_MapTerm.setter
    def AsmL_MapTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_MapTerm__AsmL_MapTerm", None)
        self.__AsmL_MapTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term114"):
                opp_val = getattr(old_value, "Term114", None)
                if opp_val == self:
                    setattr(old_value, "Term114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term114"):
                opp_val = getattr(value, "Term114", None)
                setattr(value, "Term114", self)

    @property
    def AsmL_MapTerm116(self):
        return self.__AsmL_MapTerm116

    @AsmL_MapTerm116.setter
    def AsmL_MapTerm116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_MapTerm__AsmL_MapTerm116", None)
        self.__AsmL_MapTerm116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term117"):
                opp_val = getattr(old_value, "Term117", None)
                if opp_val == self:
                    setattr(old_value, "Term117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term117"):
                opp_val = getattr(value, "Term117", None)
                setattr(value, "Term117", self)

class AsmL_TupletType(Type):

    pass
class AsmL_VarTerm(Term):

    def __init__(self, name: str, Term: "AsmL_InWhereHolds" = None, Term114: "AsmL_MapTerm" = None, Term112: "AsmL_Operator" = None, Term79: "AsmL_ReturnRule" = None, Term136: "AsmL_RangeSequence" = None, Term37: "AsmL_Initially" = None, Term139: "AsmL_RangeSequence" = None, Term45: "AsmL_UpdateRule" = None, Term130: "AsmL_RangeSet" = None, Term4: "AsmL_InWhereHolds" = None, Term22: "AsmL_Enumerator" = None, Term86: "AsmL_RemoveRule" = None, Term10: "AsmL_InWhereHolds" = None, Term117: "AsmL_MapTerm" = None, Term121: "AsmL_MethodCallTerm" = None, Term69: "AsmL_ConditionalRule" = None, Term41: "AsmL_StepExpression" = None, Term7: "AsmL_InWhereHolds" = None, Term119: "AsmL_TulpletTerm" = None, Term125: "AsmL_EnumerateSet" = None, Term54: "AsmL_UpdateMapRule" = None, Term109: "AsmL_Operator" = None, Term81: "AsmL_AddRule" = None, Term134: "AsmL_EnumerateSequence" = None, Term47: "AsmL_UpdateVarRule" = None, Term127: "AsmL_RangeSet" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AsmL_Term(LocatedElement):

    pass
class AsmL_SequenceType(Type):

    pass
class AsmL_SetType(Type):

    pass
class AsmL_MapType(Type):

    pass
class AsmL_NamedType(Type):

    def __init__(self, name: str, Type98: "AsmL_MapType" = None, Type29: "AsmL_Parameter" = None, Type: "AsmL_VarDeclaration" = None, Type101: "AsmL_MapType" = None, Type105: "AsmL_SetType" = None, Type103: "AsmL_TupletType" = None, Type107: "AsmL_SequenceType" = None, Type25: "AsmL_Method" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AsmL_Type(AsmLElement):

    def __init__(self, withNull: str, type: "VarDeclaration" = None, returnType: "Method" = None, type95: "Parameter" = None, AsmLElement: "AsmL_AsmLFile" = None):
        self.withNull = withNull
        self.type = type
        self.returnType = returnType
        self.type95 = type95
        
        pass
    @property
    def withNull(self):
        return self.__withNull

    @withNull.setter
    def withNull(self, withNull: str):
        self.__withNull = withNull


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Type__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VarDeclaration91"):
                opp_val = getattr(old_value, "VarDeclaration91", None)
                if opp_val == self:
                    setattr(old_value, "VarDeclaration91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VarDeclaration91"):
                opp_val = getattr(value, "VarDeclaration91", None)
                setattr(value, "VarDeclaration91", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Type__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method93"):
                opp_val = getattr(old_value, "Method93", None)
                if opp_val == self:
                    setattr(old_value, "Method93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method93"):
                opp_val = getattr(value, "Method93", None)
                setattr(value, "Method93", self)

    @property
    def type95(self):
        return self.__type95

    @type95.setter
    def type95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Type__type95", None)
        self.__type95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter96"):
                opp_val = getattr(old_value, "Parameter96", None)
                if opp_val == self:
                    setattr(old_value, "Parameter96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter96"):
                opp_val = getattr(value, "Parameter96", None)
                setattr(value, "Parameter96", self)

class AsmL_RemoveRule(Rule):

    pass
class AsmL_AddRule(Rule):

    pass
class AsmL_ReturnRule(Rule):

    pass
class ConditionalRule:

    pass
class AsmL_ElseIf(ConditionalRule):

    pass
class ElseIf:

    pass
class AsmL_ConditionalRule(Rule):

    pass
class AsmL_ForallRule(Rule):

    pass
class AsmL_ChooseRule(Rule):

    pass
class AsmL_MethodInvocation(Rule):

    pass
class UpdateRule:

    pass
class AsmL_UpdateFieldRule(UpdateRule):

    pass
class AsmL_UpdateMapRule(UpdateRule):

    pass
class AsmL_UpdateVarRule(UpdateRule):

    pass
class AsmL_UpdateRule(Rule):

    pass
class MethodCallTerm:

    pass
class AsmL_NewInstance(MethodCallTerm):

    pass
class InWhereHolds:

    pass
class StepExpression:

    pass
class AsmL_StepUntil(StepExpression):

    pass
class AsmL_StepWhile(StepExpression):

    pass
class Step:

    pass
class AsmL_StepForEach(Step):

    pass
class AsmL_StepExpression(Step):

    pass
class AsmL_StepUntilFixPoint(Step):

    pass
class AsmL_Step(Rule):

    def __init__(self, name: str, Rule: "AsmL_Body" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AsmL_SkipRule(Rule):

    pass
class Method:

    pass
class AsmL_Rule(LocatedElement):

    pass
class VarTerm:

    pass
class AsmL_Initially(LocatedElement):

    pass
class Initially:

    pass
class Body:

    pass
class AsmL_Parameter(LocatedElement):

    def __init__(self, name: str, ownerParameter: "Type" = None, parameters: "Method" = None):
        self.name = name
        self.ownerParameter = ownerParameter
        self.parameters = parameters
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ownerParameter(self):
        return self.__ownerParameter

    @ownerParameter.setter
    def ownerParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Parameter__ownerParameter", None)
        self.__ownerParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type29"):
                opp_val = getattr(old_value, "Type29", None)
                if opp_val == self:
                    setattr(old_value, "Type29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type29"):
                opp_val = getattr(value, "Type29", None)
                setattr(value, "Type29", self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Parameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method"):
                opp_val = getattr(old_value, "Method", None)
                if opp_val == self:
                    setattr(old_value, "Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method"):
                opp_val = getattr(value, "Method", None)
                setattr(value, "Method", self)

class Parameter:

    pass
class Function:

    pass
class AsmL_Method(Function, VarOrMethod):

    def __init__(self, isAbstract: str, isShared: str, isEntryPoint: str, isOverride: str, ownerMethod: "Type" = None, ownerMethod27: set["Parameter"] = None, VarOrMethod: "AsmL_Class" = None):
        self.isAbstract = isAbstract
        self.isShared = isShared
        self.isEntryPoint = isEntryPoint
        self.isOverride = isOverride
        self.ownerMethod = ownerMethod
        self.ownerMethod27 = ownerMethod27 if ownerMethod27 is not None else set()
        
        pass
    @property
    def isOverride(self):
        return self.__isOverride

    @isOverride.setter
    def isOverride(self, isOverride: str):
        self.__isOverride = isOverride


    @property
    def isEntryPoint(self):
        return self.__isEntryPoint

    @isEntryPoint.setter
    def isEntryPoint(self, isEntryPoint: str):
        self.__isEntryPoint = isEntryPoint


    @property
    def isShared(self):
        return self.__isShared

    @isShared.setter
    def isShared(self, isShared: str):
        self.__isShared = isShared


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def ownerMethod(self):
        return self.__ownerMethod

    @ownerMethod.setter
    def ownerMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Method__ownerMethod", None)
        self.__ownerMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type25"):
                opp_val = getattr(old_value, "Type25", None)
                if opp_val == self:
                    setattr(old_value, "Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type25"):
                opp_val = getattr(value, "Type25", None)
                setattr(value, "Type25", self)

    @property
    def ownerMethod27(self):
        return self.__ownerMethod27

    @ownerMethod27.setter
    def ownerMethod27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AsmL_Method__ownerMethod27", None)
        self.__ownerMethod27 = value if value is not None else set()
        
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
                    

class AsmL_Main(Function):

    pass