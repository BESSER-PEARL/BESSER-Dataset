from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class delphi_Visitable:

    pass
class delphi_CSTrace(ABC):

    pass
class ident:

    pass
class delphi_MultipleId(ident):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class parameter:

    pass
class delphi_parameterSimple(parameter):

    pass
class delphi_parameterList(parameter):

    pass
class constExpr:

    pass
class delphi_MultipleConstExp(constExpr):

    pass
class delphi_RecordConstExp(constExpr):

    pass
class delphi_ConstExp(constExpr):

    pass
class delphi_MineID(ident):

    def __init__(self, first: str, second: str):
        self.first = first
        self.second = second
        
    @property
    def second(self) -> str:
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second

    @property
    def first(self) -> str:
        return self.__first

    @first.setter
    def first(self, first: str):
        self.__first = first

class delphi_ReservedId(ident):

    pass
class simpleStatement:

    pass
class delphi_inheritedStamnt(simpleStatement):

    pass
class delphi_gotoStmnt(simpleStatement):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class delphi_callStmnt(simpleStatement):

    pass
class delphi_assignmentStmnt(simpleStatement):

    def __init__(self, operator: str, delphi_assignmentStmnt: "delphi_designator" = None, delphi_assignmentStmnt432: "delphi_expression" = None):
        self.operator = operator
        self.delphi_assignmentStmnt = delphi_assignmentStmnt
        self.delphi_assignmentStmnt432 = delphi_assignmentStmnt432
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def delphi_assignmentStmnt432(self):
        return self.__delphi_assignmentStmnt432

    @delphi_assignmentStmnt432.setter
    def delphi_assignmentStmnt432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_assignmentStmnt__delphi_assignmentStmnt432", None)
        self.__delphi_assignmentStmnt432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_expression433"):
                opp_val = getattr(old_value, "delphi_expression433", None)
                if opp_val == self:
                    setattr(old_value, "delphi_expression433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_expression433"):
                opp_val = getattr(value, "delphi_expression433", None)
                setattr(value, "delphi_expression433", self)

    @property
    def delphi_assignmentStmnt(self):
        return self.__delphi_assignmentStmnt

    @delphi_assignmentStmnt.setter
    def delphi_assignmentStmnt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_assignmentStmnt__delphi_assignmentStmnt", None)
        self.__delphi_assignmentStmnt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_designator430"):
                opp_val = getattr(old_value, "delphi_designator430", None)
                if opp_val == self:
                    setattr(old_value, "delphi_designator430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_designator430"):
                opp_val = getattr(value, "delphi_designator430", None)
                setattr(value, "delphi_designator430", self)

class addOp:

    pass
class delphi_adOp(addOp):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class factor:

    pass
class delphi_simpleFactor(factor):

    pass
class pointerType:

    pass
class classHeritage:

    pass
class objFieldList:

    pass
class restrictedType:

    pass
class delphi_classType(restrictedType):

    def __init__(self, visibility: str, delphi_classType: "delphi_classHeritage" = None, delphi_classType314: "delphi_classFieldList" = None, delphi_classType316: "delphi_classMethodList" = None, delphi_classType318: "delphi_classPropertyList" = None):
        self.visibility = visibility
        self.delphi_classType = delphi_classType
        self.delphi_classType314 = delphi_classType314
        self.delphi_classType316 = delphi_classType316
        self.delphi_classType318 = delphi_classType318
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def delphi_classType318(self):
        return self.__delphi_classType318

    @delphi_classType318.setter
    def delphi_classType318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classType__delphi_classType318", None)
        self.__delphi_classType318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classPropertyList"):
                opp_val = getattr(old_value, "delphi_classPropertyList", None)
                if opp_val == self:
                    setattr(old_value, "delphi_classPropertyList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classPropertyList"):
                opp_val = getattr(value, "delphi_classPropertyList", None)
                setattr(value, "delphi_classPropertyList", self)

    @property
    def delphi_classType(self):
        return self.__delphi_classType

    @delphi_classType.setter
    def delphi_classType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classType__delphi_classType", None)
        self.__delphi_classType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classHeritage"):
                opp_val = getattr(old_value, "delphi_classHeritage", None)
                if opp_val == self:
                    setattr(old_value, "delphi_classHeritage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classHeritage"):
                opp_val = getattr(value, "delphi_classHeritage", None)
                setattr(value, "delphi_classHeritage", self)

    @property
    def delphi_classType314(self):
        return self.__delphi_classType314

    @delphi_classType314.setter
    def delphi_classType314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classType__delphi_classType314", None)
        self.__delphi_classType314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classFieldList"):
                opp_val = getattr(old_value, "delphi_classFieldList", None)
                if opp_val == self:
                    setattr(old_value, "delphi_classFieldList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classFieldList"):
                opp_val = getattr(value, "delphi_classFieldList", None)
                setattr(value, "delphi_classFieldList", self)

    @property
    def delphi_classType316(self):
        return self.__delphi_classType316

    @delphi_classType316.setter
    def delphi_classType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classType__delphi_classType316", None)
        self.__delphi_classType316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classMethodList"):
                opp_val = getattr(old_value, "delphi_classMethodList", None)
                if opp_val == self:
                    setattr(old_value, "delphi_classMethodList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classMethodList"):
                opp_val = getattr(value, "delphi_classMethodList", None)
                setattr(value, "delphi_classMethodList", self)

class delphi_interfaceType(restrictedType):

    pass
class delphi_objectType(restrictedType):

    pass
class methodHeading:

    pass
class delphi_constructorHeading(methodHeading):

    pass
class delphi_destructorHeading(methodHeading):

    pass
class procedureDeclSection:

    pass
class delphi_functionDecl(procedureDeclSection):

    pass
class delphi_procedureDecl(procedureDeclSection):

    pass
class loopStmt:

    pass
class delphi_whileStmt(loopStmt):

    pass
class delphi_forStmt(loopStmt):

    pass
class delphi_repeatStmt(loopStmt):

    pass
class conditionalStmt:

    pass
class delphi_caseStmt(conditionalStmt):

    pass
class delphi_ifStmt(conditionalStmt):

    pass
class structStmt:

    pass
class delphi_conditionalStmt(structStmt):

    pass
class delphi_raiseStmt(structStmt):

    def __init__(self, raise: str, at: str):
        self.raise = raise
        self.at = at
        
    @property
    def at(self) -> str:
        return self.__at

    @at.setter
    def at(self, at: str):
        self.__at = at

    @property
    def raise(self) -> str:
        return self.__raise

    @raise.setter
    def raise(self, raise: str):
        self.__raise = raise

class delphi_withStmt(structStmt):

    pass
class delphi_loopStmt(structStmt):

    pass
class delphi_tryStmt(structStmt):

    pass
class delphi_assemblerStmt(structStmt):

    pass
class unlabelledStatement:

    pass
class delphi_structStmt(unlabelledStatement):

    pass
class delphi_simpleStatement(unlabelledStatement):

    pass
class term:

    pass
class delphi_multExp(term):

    pass
class delphi_factor(term):

    def __init__(self, number: str, string: str, delphi_factor: "delphi_designator" = None, delphi_factor167: "delphi_exprList" = None, delphi_factor174: "delphi_setConstructor" = None, delphi_factor176: "delphi_typeId" = None, delphi_factor169: "delphi_expression" = None, delphi_factor171: "delphi_expression" = None, delphi_factor428: "delphi_multExp" = None):
        self.number = number
        self.string = string
        self.delphi_factor = delphi_factor
        self.delphi_factor167 = delphi_factor167
        self.delphi_factor174 = delphi_factor174
        self.delphi_factor176 = delphi_factor176
        self.delphi_factor169 = delphi_factor169
        self.delphi_factor171 = delphi_factor171
        self.delphi_factor428 = delphi_factor428
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def delphi_factor171(self):
        return self.__delphi_factor171

    @delphi_factor171.setter
    def delphi_factor171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor171", None)
        self.__delphi_factor171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_expression172"):
                opp_val = getattr(old_value, "delphi_expression172", None)
                if opp_val == self:
                    setattr(old_value, "delphi_expression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_expression172"):
                opp_val = getattr(value, "delphi_expression172", None)
                setattr(value, "delphi_expression172", self)

    @property
    def delphi_factor174(self):
        return self.__delphi_factor174

    @delphi_factor174.setter
    def delphi_factor174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor174", None)
        self.__delphi_factor174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_setConstructor"):
                opp_val = getattr(old_value, "delphi_setConstructor", None)
                if opp_val == self:
                    setattr(old_value, "delphi_setConstructor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_setConstructor"):
                opp_val = getattr(value, "delphi_setConstructor", None)
                setattr(value, "delphi_setConstructor", self)

    @property
    def delphi_factor(self):
        return self.__delphi_factor

    @delphi_factor.setter
    def delphi_factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor", None)
        self.__delphi_factor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_designator"):
                opp_val = getattr(old_value, "delphi_designator", None)
                if opp_val == self:
                    setattr(old_value, "delphi_designator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_designator"):
                opp_val = getattr(value, "delphi_designator", None)
                setattr(value, "delphi_designator", self)

    @property
    def delphi_factor167(self):
        return self.__delphi_factor167

    @delphi_factor167.setter
    def delphi_factor167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor167", None)
        self.__delphi_factor167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_exprList"):
                opp_val = getattr(old_value, "delphi_exprList", None)
                if opp_val == self:
                    setattr(old_value, "delphi_exprList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_exprList"):
                opp_val = getattr(value, "delphi_exprList", None)
                setattr(value, "delphi_exprList", self)

    @property
    def delphi_factor176(self):
        return self.__delphi_factor176

    @delphi_factor176.setter
    def delphi_factor176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor176", None)
        self.__delphi_factor176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_typeId177"):
                opp_val = getattr(old_value, "delphi_typeId177", None)
                if opp_val == self:
                    setattr(old_value, "delphi_typeId177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_typeId177"):
                opp_val = getattr(value, "delphi_typeId177", None)
                setattr(value, "delphi_typeId177", self)

    @property
    def delphi_factor169(self):
        return self.__delphi_factor169

    @delphi_factor169.setter
    def delphi_factor169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor169", None)
        self.__delphi_factor169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_expression"):
                opp_val = getattr(old_value, "delphi_expression", None)
                if opp_val == self:
                    setattr(old_value, "delphi_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_expression"):
                opp_val = getattr(value, "delphi_expression", None)
                setattr(value, "delphi_expression", self)

    @property
    def delphi_factor428(self):
        return self.__delphi_factor428

    @delphi_factor428.setter
    def delphi_factor428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_factor__delphi_factor428", None)
        self.__delphi_factor428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_multExp427"):
                opp_val = getattr(old_value, "delphi_multExp427", None)
                if opp_val == self:
                    setattr(old_value, "delphi_multExp427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_multExp427"):
                opp_val = getattr(value, "delphi_multExp427", None)
                setattr(value, "delphi_multExp427", self)

class simpleExpression:

    pass
class delphi_addExp(simpleExpression):

    pass
class delphi_term(simpleExpression):

    pass
class expression:

    pass
class delphi_relExp(expression):

    pass
class delphi_simpleExpression(expression):

    pass
class strucType:

    pass
class delphi_setType(strucType):

    pass
class delphi_fileType(strucType):

    pass
class delphi_arrayType(strucType):

    pass
class delphi_recType(strucType):

    pass
class type:

    pass
class delphi_procedureType(type):

    pass
class delphi_pointerType(type):

    pass
class delphi_strucType(type):

    def __init__(self, port: str):
        self.port = port
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

class delphi_classRefType(type):

    pass
class delphi_stringType(type):

    pass
class delphi_variantType(type):

    pass
class ordinalType:

    pass
class delphi_enumeratedType(ordinalType):

    pass
class delphi_subrangeType(ordinalType):

    pass
class delphi_ordIdent(ordinalType):

    pass
class simpleType:

    pass
class delphi_ordinalType(simpleType):

    pass
class delphi_realType(simpleType):

    pass
class delphi_simpleType(type):

    pass
class delphi_typeId(pointerType, type):

    pass
class declSection:

    pass
class delphi_procedureDeclSection(declSection):

    def __init__(self, port: str, delphi_procedureDeclSection: "delphi_directive" = None, delphi_procedureDeclSection269: "delphi_block" = None):
        self.port = port
        self.delphi_procedureDeclSection = delphi_procedureDeclSection
        self.delphi_procedureDeclSection269 = delphi_procedureDeclSection269
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def delphi_procedureDeclSection269(self):
        return self.__delphi_procedureDeclSection269

    @delphi_procedureDeclSection269.setter
    def delphi_procedureDeclSection269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_procedureDeclSection__delphi_procedureDeclSection269", None)
        self.__delphi_procedureDeclSection269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_block270"):
                opp_val = getattr(old_value, "delphi_block270", None)
                if opp_val == self:
                    setattr(old_value, "delphi_block270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_block270"):
                opp_val = getattr(value, "delphi_block270", None)
                setattr(value, "delphi_block270", self)

    @property
    def delphi_procedureDeclSection(self):
        return self.__delphi_procedureDeclSection

    @delphi_procedureDeclSection.setter
    def delphi_procedureDeclSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_procedureDeclSection__delphi_procedureDeclSection", None)
        self.__delphi_procedureDeclSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_directive267"):
                opp_val = getattr(old_value, "delphi_directive267", None)
                if opp_val == self:
                    setattr(old_value, "delphi_directive267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_directive267"):
                opp_val = getattr(value, "delphi_directive267", None)
                setattr(value, "delphi_directive267", self)

class delphi_labelDeclSection(declSection):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class delphi_compoundStmt(structStmt):

    pass
class delphi_functionHeading(methodHeading):

    pass
class delphi_procedureHeading(methodHeading):

    pass
class interfaceDecl:

    pass
class delphi_typeSection(declSection, interfaceDecl):

    pass
class delphi_varSection(declSection, interfaceDecl):

    pass
class delphi_constSection(declSection, interfaceDecl):

    pass
class delphi_exportedHeading(interfaceDecl):

    pass
class CSTrace:

    pass
class delphi_typedConstant(CSTrace):

    pass
class delphi_objHeritage(CSTrace):

    pass
class delphi_fieldList(CSTrace):

    pass
class delphi_unlabelledStatement(CSTrace):

    pass
class delphi_formalParameters(CSTrace):

    pass
class delphi_interfaceHeritage(CSTrace):

    pass
class delphi_type(CSTrace):

    pass
class delphi_fieldDecl(CSTrace):

    def __init__(self, port: str, delphi_fieldDecl: "delphi_fieldList" = None, delphi_fieldDecl121: "delphi_identList" = None, delphi_fieldDecl124: "delphi_type" = None):
        self.port = port
        self.delphi_fieldDecl = delphi_fieldDecl
        self.delphi_fieldDecl121 = delphi_fieldDecl121
        self.delphi_fieldDecl124 = delphi_fieldDecl124
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def delphi_fieldDecl(self):
        return self.__delphi_fieldDecl

    @delphi_fieldDecl.setter
    def delphi_fieldDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_fieldDecl__delphi_fieldDecl", None)
        self.__delphi_fieldDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_fieldList117"):
                opp_val = getattr(old_value, "delphi_fieldList117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_fieldList117"):
                opp_val = getattr(value, "delphi_fieldList117", None)
                if opp_val is None:
                    setattr(value, "delphi_fieldList117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_fieldDecl121(self):
        return self.__delphi_fieldDecl121

    @delphi_fieldDecl121.setter
    def delphi_fieldDecl121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_fieldDecl__delphi_fieldDecl121", None)
        self.__delphi_fieldDecl121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_identList122"):
                opp_val = getattr(old_value, "delphi_identList122", None)
                if opp_val == self:
                    setattr(old_value, "delphi_identList122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_identList122"):
                opp_val = getattr(value, "delphi_identList122", None)
                setattr(value, "delphi_identList122", self)

    @property
    def delphi_fieldDecl124(self):
        return self.__delphi_fieldDecl124

    @delphi_fieldDecl124.setter
    def delphi_fieldDecl124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_fieldDecl__delphi_fieldDecl124", None)
        self.__delphi_fieldDecl124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_type125"):
                opp_val = getattr(old_value, "delphi_type125", None)
                if opp_val == self:
                    setattr(old_value, "delphi_type125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_type125"):
                opp_val = getattr(value, "delphi_type125", None)
                setattr(value, "delphi_type125", self)

class delphi_typeDecl(CSTrace):

    def __init__(self, port: str, delphi_typeDecl68: "delphi_ident" = None, delphi_typeDecl71: "delphi_type" = None, delphi_typeDecl73: "delphi_restrictedType" = None, delphi_typeDecl: "delphi_typeSection" = None):
        self.port = port
        self.delphi_typeDecl68 = delphi_typeDecl68
        self.delphi_typeDecl71 = delphi_typeDecl71
        self.delphi_typeDecl73 = delphi_typeDecl73
        self.delphi_typeDecl = delphi_typeDecl
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def delphi_typeDecl68(self):
        return self.__delphi_typeDecl68

    @delphi_typeDecl68.setter
    def delphi_typeDecl68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_typeDecl__delphi_typeDecl68", None)
        self.__delphi_typeDecl68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_ident69"):
                opp_val = getattr(old_value, "delphi_ident69", None)
                if opp_val == self:
                    setattr(old_value, "delphi_ident69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_ident69"):
                opp_val = getattr(value, "delphi_ident69", None)
                setattr(value, "delphi_ident69", self)

    @property
    def delphi_typeDecl(self):
        return self.__delphi_typeDecl

    @delphi_typeDecl.setter
    def delphi_typeDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_typeDecl__delphi_typeDecl", None)
        self.__delphi_typeDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_typeSection"):
                opp_val = getattr(old_value, "delphi_typeSection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_typeSection"):
                opp_val = getattr(value, "delphi_typeSection", None)
                if opp_val is None:
                    setattr(value, "delphi_typeSection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_typeDecl73(self):
        return self.__delphi_typeDecl73

    @delphi_typeDecl73.setter
    def delphi_typeDecl73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_typeDecl__delphi_typeDecl73", None)
        self.__delphi_typeDecl73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_restrictedType"):
                opp_val = getattr(old_value, "delphi_restrictedType", None)
                if opp_val == self:
                    setattr(old_value, "delphi_restrictedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_restrictedType"):
                opp_val = getattr(value, "delphi_restrictedType", None)
                setattr(value, "delphi_restrictedType", self)

    @property
    def delphi_typeDecl71(self):
        return self.__delphi_typeDecl71

    @delphi_typeDecl71.setter
    def delphi_typeDecl71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_typeDecl__delphi_typeDecl71", None)
        self.__delphi_typeDecl71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_type"):
                opp_val = getattr(old_value, "delphi_type", None)
                if opp_val == self:
                    setattr(old_value, "delphi_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_type"):
                opp_val = getattr(value, "delphi_type", None)
                setattr(value, "delphi_type", self)

class delphi_arrayConstant(CSTrace):

    pass
class delphi_recordConstExpr(CSTrace):

    pass
class delphi_classMethodList(CSTrace):

    pass
class delphi_relOp(CSTrace):

    def __init__(self, op: str, delphi_relOp: "delphi_relExp" = None):
        self.op = op
        self.delphi_relOp = delphi_relOp
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def delphi_relOp(self):
        return self.__delphi_relOp

    @delphi_relOp.setter
    def delphi_relOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_relOp__delphi_relOp", None)
        self.__delphi_relOp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_relExp413"):
                opp_val = getattr(old_value, "delphi_relExp413", None)
                if opp_val == self:
                    setattr(old_value, "delphi_relExp413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_relExp413"):
                opp_val = getattr(value, "delphi_relExp413", None)
                setattr(value, "delphi_relExp413", self)

class delphi_exceptionBlock(CSTrace):

    pass
class delphi_constantDecl(CSTrace):

    def __init__(self, port: str, delphi_constantDecl: "delphi_constSection" = None, delphi_constantDecl57: "delphi_ident" = None, delphi_constantDecl60: "delphi_constExpr" = None, delphi_constantDecl63: "delphi_typeId" = None, delphi_constantDecl65: "delphi_typedConstant" = None):
        self.port = port
        self.delphi_constantDecl = delphi_constantDecl
        self.delphi_constantDecl57 = delphi_constantDecl57
        self.delphi_constantDecl60 = delphi_constantDecl60
        self.delphi_constantDecl63 = delphi_constantDecl63
        self.delphi_constantDecl65 = delphi_constantDecl65
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def delphi_constantDecl60(self):
        return self.__delphi_constantDecl60

    @delphi_constantDecl60.setter
    def delphi_constantDecl60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_constantDecl__delphi_constantDecl60", None)
        self.__delphi_constantDecl60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_constExpr61"):
                opp_val = getattr(old_value, "delphi_constExpr61", None)
                if opp_val == self:
                    setattr(old_value, "delphi_constExpr61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_constExpr61"):
                opp_val = getattr(value, "delphi_constExpr61", None)
                setattr(value, "delphi_constExpr61", self)

    @property
    def delphi_constantDecl57(self):
        return self.__delphi_constantDecl57

    @delphi_constantDecl57.setter
    def delphi_constantDecl57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_constantDecl__delphi_constantDecl57", None)
        self.__delphi_constantDecl57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_ident58"):
                opp_val = getattr(old_value, "delphi_ident58", None)
                if opp_val == self:
                    setattr(old_value, "delphi_ident58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_ident58"):
                opp_val = getattr(value, "delphi_ident58", None)
                setattr(value, "delphi_ident58", self)

    @property
    def delphi_constantDecl(self):
        return self.__delphi_constantDecl

    @delphi_constantDecl.setter
    def delphi_constantDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_constantDecl__delphi_constantDecl", None)
        self.__delphi_constantDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_constSection"):
                opp_val = getattr(old_value, "delphi_constSection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_constSection"):
                opp_val = getattr(value, "delphi_constSection", None)
                if opp_val is None:
                    setattr(value, "delphi_constSection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_constantDecl63(self):
        return self.__delphi_constantDecl63

    @delphi_constantDecl63.setter
    def delphi_constantDecl63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_constantDecl__delphi_constantDecl63", None)
        self.__delphi_constantDecl63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_typeId"):
                opp_val = getattr(old_value, "delphi_typeId", None)
                if opp_val == self:
                    setattr(old_value, "delphi_typeId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_typeId"):
                opp_val = getattr(value, "delphi_typeId", None)
                setattr(value, "delphi_typeId", self)

    @property
    def delphi_constantDecl65(self):
        return self.__delphi_constantDecl65

    @delphi_constantDecl65.setter
    def delphi_constantDecl65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_constantDecl__delphi_constantDecl65", None)
        self.__delphi_constantDecl65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_typedConstant"):
                opp_val = getattr(old_value, "delphi_typedConstant", None)
                if opp_val == self:
                    setattr(old_value, "delphi_typedConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_typedConstant"):
                opp_val = getattr(value, "delphi_typedConstant", None)
                setattr(value, "delphi_typedConstant", self)

class delphi_propertySpecifiers(CSTrace):

    pass
class delphi_setConstructor(CSTrace):

    pass
class delphi_methodList(CSTrace):

    pass
class delphi_formalParm(CSTrace):

    pass
class delphi_qualId(CSTrace):

    pass
class delphi_addOp(CSTrace):

    pass
class delphi_variantSection(CSTrace):

    pass
class delphi_recVariant(CSTrace):

    pass
class delphi_recordFieldConstant(CSTrace):

    pass
class delphi_block(CSTrace):

    pass
class delphi_exprList(CSTrace):

    pass
class delphi_mulOp(CSTrace):

    def __init__(self, op: str, delphi_mulOp: "delphi_multExp" = None):
        self.op = op
        self.delphi_mulOp = delphi_mulOp
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def delphi_mulOp(self):
        return self.__delphi_mulOp

    @delphi_mulOp.setter
    def delphi_mulOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_mulOp__delphi_mulOp", None)
        self.__delphi_mulOp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_multExp425"):
                opp_val = getattr(old_value, "delphi_multExp425", None)
                if opp_val == self:
                    setattr(old_value, "delphi_multExp425", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_multExp425"):
                opp_val = getattr(value, "delphi_multExp425", None)
                setattr(value, "delphi_multExp425", self)

class delphi_classProperty(CSTrace):

    def __init__(self, visibility: str, delphi_classProperty: "delphi_classPropertyList" = None, delphi_classProperty332: "delphi_propertyList" = None):
        self.visibility = visibility
        self.delphi_classProperty = delphi_classProperty
        self.delphi_classProperty332 = delphi_classProperty332
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def delphi_classProperty(self):
        return self.__delphi_classProperty

    @delphi_classProperty.setter
    def delphi_classProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classProperty__delphi_classProperty", None)
        self.__delphi_classProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classPropertyList330"):
                opp_val = getattr(old_value, "delphi_classPropertyList330", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classPropertyList330"):
                opp_val = getattr(value, "delphi_classPropertyList330", None)
                if opp_val is None:
                    setattr(value, "delphi_classPropertyList330", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_classProperty332(self):
        return self.__delphi_classProperty332

    @delphi_classProperty332.setter
    def delphi_classProperty332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classProperty__delphi_classProperty332", None)
        self.__delphi_classProperty332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_propertyList"):
                opp_val = getattr(old_value, "delphi_propertyList", None)
                if opp_val == self:
                    setattr(old_value, "delphi_propertyList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_propertyList"):
                opp_val = getattr(value, "delphi_propertyList", None)
                setattr(value, "delphi_propertyList", self)

class delphi_designatorPart(CSTrace):

    def __init__(self, id: str, id2: str, delphi_designatorPart: "delphi_designatorSubPart" = None, delphi_designatorPart189: "delphi_reservedWord" = None):
        self.id = id
        self.id2 = id2
        self.delphi_designatorPart = delphi_designatorPart
        self.delphi_designatorPart189 = delphi_designatorPart189
        
    @property
    def id2(self) -> str:
        return self.__id2

    @id2.setter
    def id2(self, id2: str):
        self.__id2 = id2

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def delphi_designatorPart189(self):
        return self.__delphi_designatorPart189

    @delphi_designatorPart189.setter
    def delphi_designatorPart189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_designatorPart__delphi_designatorPart189", None)
        self.__delphi_designatorPart189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_reservedWord"):
                opp_val = getattr(old_value, "delphi_reservedWord", None)
                if opp_val == self:
                    setattr(old_value, "delphi_reservedWord", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_reservedWord"):
                opp_val = getattr(value, "delphi_reservedWord", None)
                setattr(value, "delphi_reservedWord", self)

    @property
    def delphi_designatorPart(self):
        return self.__delphi_designatorPart

    @delphi_designatorPart.setter
    def delphi_designatorPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_designatorPart__delphi_designatorPart", None)
        self.__delphi_designatorPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_designatorSubPart184"):
                opp_val = getattr(old_value, "delphi_designatorSubPart184", None)
                if opp_val == self:
                    setattr(old_value, "delphi_designatorSubPart184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_designatorSubPart184"):
                opp_val = getattr(value, "delphi_designatorSubPart184", None)
                setattr(value, "delphi_designatorSubPart184", self)

class delphi_exportsItem(CSTrace):

    pass
class delphi_declSection(CSTrace):

    pass
class delphi_propertyInterface(CSTrace):

    pass
class delphi_objFieldList(CSTrace):

    pass
class delphi_classHeritage(CSTrace):

    pass
class delphi_recordConstant(CSTrace):

    pass
class delphi_classMethod(CSTrace):

    def __init__(self, visibility: str, delphi_classMethod: "delphi_classMethodList" = None, delphi_classMethod327: "delphi_methodList" = None):
        self.visibility = visibility
        self.delphi_classMethod = delphi_classMethod
        self.delphi_classMethod327 = delphi_classMethod327
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def delphi_classMethod327(self):
        return self.__delphi_classMethod327

    @delphi_classMethod327.setter
    def delphi_classMethod327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classMethod__delphi_classMethod327", None)
        self.__delphi_classMethod327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_methodList328"):
                opp_val = getattr(old_value, "delphi_methodList328", None)
                if opp_val == self:
                    setattr(old_value, "delphi_methodList328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_methodList328"):
                opp_val = getattr(value, "delphi_methodList328", None)
                setattr(value, "delphi_methodList328", self)

    @property
    def delphi_classMethod(self):
        return self.__delphi_classMethod

    @delphi_classMethod.setter
    def delphi_classMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classMethod__delphi_classMethod", None)
        self.__delphi_classMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classMethodList325"):
                opp_val = getattr(old_value, "delphi_classMethodList325", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classMethodList325"):
                opp_val = getattr(value, "delphi_classMethodList325", None)
                if opp_val is None:
                    setattr(value, "delphi_classMethodList325", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class delphi_varDecl(CSTrace):

    pass
class delphi_restrictedType(CSTrace):

    pass
class delphi_classPropertyList(CSTrace):

    pass
class delphi_propertyList(CSTrace):

    def __init__(self, port: str, delphi_propertyList: "delphi_classProperty" = None, delphi_propertyList334: "delphi_ident" = None, delphi_propertyList337: "delphi_propertyInterface" = None, delphi_propertyList339: "delphi_propertySpecifiers" = None):
        self.port = port
        self.delphi_propertyList = delphi_propertyList
        self.delphi_propertyList334 = delphi_propertyList334
        self.delphi_propertyList337 = delphi_propertyList337
        self.delphi_propertyList339 = delphi_propertyList339
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def delphi_propertyList334(self):
        return self.__delphi_propertyList334

    @delphi_propertyList334.setter
    def delphi_propertyList334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_propertyList__delphi_propertyList334", None)
        self.__delphi_propertyList334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_ident335"):
                opp_val = getattr(old_value, "delphi_ident335", None)
                if opp_val == self:
                    setattr(old_value, "delphi_ident335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_ident335"):
                opp_val = getattr(value, "delphi_ident335", None)
                setattr(value, "delphi_ident335", self)

    @property
    def delphi_propertyList339(self):
        return self.__delphi_propertyList339

    @delphi_propertyList339.setter
    def delphi_propertyList339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_propertyList__delphi_propertyList339", None)
        self.__delphi_propertyList339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_propertySpecifiers"):
                opp_val = getattr(old_value, "delphi_propertySpecifiers", None)
                if opp_val == self:
                    setattr(old_value, "delphi_propertySpecifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_propertySpecifiers"):
                opp_val = getattr(value, "delphi_propertySpecifiers", None)
                setattr(value, "delphi_propertySpecifiers", self)

    @property
    def delphi_propertyList337(self):
        return self.__delphi_propertyList337

    @delphi_propertyList337.setter
    def delphi_propertyList337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_propertyList__delphi_propertyList337", None)
        self.__delphi_propertyList337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_propertyInterface"):
                opp_val = getattr(old_value, "delphi_propertyInterface", None)
                if opp_val == self:
                    setattr(old_value, "delphi_propertyInterface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_propertyInterface"):
                opp_val = getattr(value, "delphi_propertyInterface", None)
                setattr(value, "delphi_propertyInterface", self)

    @property
    def delphi_propertyList(self):
        return self.__delphi_propertyList

    @delphi_propertyList.setter
    def delphi_propertyList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_propertyList__delphi_propertyList", None)
        self.__delphi_propertyList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classProperty332"):
                opp_val = getattr(old_value, "delphi_classProperty332", None)
                if opp_val == self:
                    setattr(old_value, "delphi_classProperty332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classProperty332"):
                opp_val = getattr(value, "delphi_classProperty332", None)
                setattr(value, "delphi_classProperty332", self)

class delphi_classFieldList(CSTrace):

    pass
class delphi_propertyParameterList(CSTrace):

    pass
class delphi_directive(CSTrace):

    def __init__(self, dir: str, delphi_directive: "delphi_exportedHeading" = None, delphi_directive267: "delphi_procedureDeclSection" = None, delphi_directive285: "delphi_constExpr" = None, delphi_directive299: "delphi_methodList" = None):
        self.dir = dir
        self.delphi_directive = delphi_directive
        self.delphi_directive267 = delphi_directive267
        self.delphi_directive285 = delphi_directive285
        self.delphi_directive299 = delphi_directive299
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def delphi_directive267(self):
        return self.__delphi_directive267

    @delphi_directive267.setter
    def delphi_directive267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_directive__delphi_directive267", None)
        self.__delphi_directive267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_procedureDeclSection"):
                opp_val = getattr(old_value, "delphi_procedureDeclSection", None)
                if opp_val == self:
                    setattr(old_value, "delphi_procedureDeclSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_procedureDeclSection"):
                opp_val = getattr(value, "delphi_procedureDeclSection", None)
                setattr(value, "delphi_procedureDeclSection", self)

    @property
    def delphi_directive299(self):
        return self.__delphi_directive299

    @delphi_directive299.setter
    def delphi_directive299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_directive__delphi_directive299", None)
        self.__delphi_directive299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_methodList298"):
                opp_val = getattr(old_value, "delphi_methodList298", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_methodList298"):
                opp_val = getattr(value, "delphi_methodList298", None)
                if opp_val is None:
                    setattr(value, "delphi_methodList298", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_directive285(self):
        return self.__delphi_directive285

    @delphi_directive285.setter
    def delphi_directive285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_directive__delphi_directive285", None)
        self.__delphi_directive285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_constExpr286"):
                opp_val = getattr(old_value, "delphi_constExpr286", None)
                if opp_val == self:
                    setattr(old_value, "delphi_constExpr286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_constExpr286"):
                opp_val = getattr(value, "delphi_constExpr286", None)
                setattr(value, "delphi_constExpr286", self)

    @property
    def delphi_directive(self):
        return self.__delphi_directive

    @delphi_directive.setter
    def delphi_directive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_directive__delphi_directive", None)
        self.__delphi_directive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_exportedHeading30"):
                opp_val = getattr(old_value, "delphi_exportedHeading30", None)
                if opp_val == self:
                    setattr(old_value, "delphi_exportedHeading30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_exportedHeading30"):
                opp_val = getattr(value, "delphi_exportedHeading30", None)
                setattr(value, "delphi_exportedHeading30", self)

class delphi_classField(CSTrace):

    def __init__(self, visibility: str, delphi_classField: "delphi_classFieldList" = None, delphi_classField322: "delphi_objFieldList" = None):
        self.visibility = visibility
        self.delphi_classField = delphi_classField
        self.delphi_classField322 = delphi_classField322
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def delphi_classField322(self):
        return self.__delphi_classField322

    @delphi_classField322.setter
    def delphi_classField322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classField__delphi_classField322", None)
        self.__delphi_classField322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_objFieldList323"):
                opp_val = getattr(old_value, "delphi_objFieldList323", None)
                if opp_val == self:
                    setattr(old_value, "delphi_objFieldList323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_objFieldList323"):
                opp_val = getattr(value, "delphi_objFieldList323", None)
                setattr(value, "delphi_objFieldList323", self)

    @property
    def delphi_classField(self):
        return self.__delphi_classField

    @delphi_classField.setter
    def delphi_classField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_classField__delphi_classField", None)
        self.__delphi_classField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_classFieldList320"):
                opp_val = getattr(old_value, "delphi_classFieldList320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_classFieldList320"):
                opp_val = getattr(value, "delphi_classFieldList320", None)
                if opp_val is None:
                    setattr(value, "delphi_classFieldList320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class delphi_file(CSTrace):

    pass
class delphi_constExpr(CSTrace):

    pass
class delphi_expression(CSTrace):

    pass
class delphi_interfaceDecl(CSTrace):

    pass
class delphi_exportsStmt(CSTrace):

    pass
class delphi_caseLabel(CSTrace):

    pass
class delphi_methodHeading(CSTrace):

    pass
class delphi_parameter(CSTrace):

    pass
class delphi_designator(CSTrace):

    pass
class delphi_caseSelector(CSTrace):

    pass
class delphi_enumeratedTypeElement(CSTrace):

    pass
class delphi_reservedWord(CSTrace):

    def __init__(self, id: str, delphi_reservedWord: "delphi_designatorPart" = None, delphi_reservedWord447: "delphi_ReservedId" = None):
        self.id = id
        self.delphi_reservedWord = delphi_reservedWord
        self.delphi_reservedWord447 = delphi_reservedWord447
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def delphi_reservedWord447(self):
        return self.__delphi_reservedWord447

    @delphi_reservedWord447.setter
    def delphi_reservedWord447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_reservedWord__delphi_reservedWord447", None)
        self.__delphi_reservedWord447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_ReservedId"):
                opp_val = getattr(old_value, "delphi_ReservedId", None)
                if opp_val == self:
                    setattr(old_value, "delphi_ReservedId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_ReservedId"):
                opp_val = getattr(value, "delphi_ReservedId", None)
                setattr(value, "delphi_ReservedId", self)

    @property
    def delphi_reservedWord(self):
        return self.__delphi_reservedWord

    @delphi_reservedWord.setter
    def delphi_reservedWord(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_reservedWord__delphi_reservedWord", None)
        self.__delphi_reservedWord = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_designatorPart189"):
                opp_val = getattr(old_value, "delphi_designatorPart189", None)
                if opp_val == self:
                    setattr(old_value, "delphi_designatorPart189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_designatorPart189"):
                opp_val = getattr(value, "delphi_designatorPart189", None)
                setattr(value, "delphi_designatorPart189", self)

class delphi_usesClause(CSTrace):

    pass
class delphi_setElement(CSTrace):

    pass
class delphi_unitId(CSTrace):

    def __init__(self, id: str, delphi_unitId: "delphi_qualId" = None, delphi_unitId401: "delphi_typeId" = None):
        self.id = id
        self.delphi_unitId = delphi_unitId
        self.delphi_unitId401 = delphi_unitId401
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def delphi_unitId(self):
        return self.__delphi_unitId

    @delphi_unitId.setter
    def delphi_unitId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_unitId__delphi_unitId", None)
        self.__delphi_unitId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_qualId395"):
                opp_val = getattr(old_value, "delphi_qualId395", None)
                if opp_val == self:
                    setattr(old_value, "delphi_qualId395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_qualId395"):
                opp_val = getattr(value, "delphi_qualId395", None)
                setattr(value, "delphi_qualId395", self)

    @property
    def delphi_unitId401(self):
        return self.__delphi_unitId401

    @delphi_unitId401.setter
    def delphi_unitId401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_unitId__delphi_unitId401", None)
        self.__delphi_unitId401 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_typeId400"):
                opp_val = getattr(old_value, "delphi_typeId400", None)
                if opp_val == self:
                    setattr(old_value, "delphi_typeId400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_typeId400"):
                opp_val = getattr(value, "delphi_typeId400", None)
                setattr(value, "delphi_typeId400", self)

class delphi_statement(CSTrace):

    def __init__(self, labelId: str, delphi_statement: "delphi_stmtList" = None, delphi_statement203: "delphi_unlabelledStatement" = None, delphi_statement226: "delphi_caseSelector" = None, delphi_statement234: "delphi_loopStmt" = None, delphi_statement211: "delphi_ifStmt" = None, delphi_statement214: "delphi_ifStmt" = None, delphi_statement246: "delphi_withStmt" = None, delphi_statement262: "delphi_exceptionBlock" = None):
        self.labelId = labelId
        self.delphi_statement = delphi_statement
        self.delphi_statement203 = delphi_statement203
        self.delphi_statement226 = delphi_statement226
        self.delphi_statement234 = delphi_statement234
        self.delphi_statement211 = delphi_statement211
        self.delphi_statement214 = delphi_statement214
        self.delphi_statement246 = delphi_statement246
        self.delphi_statement262 = delphi_statement262
        
    @property
    def labelId(self) -> str:
        return self.__labelId

    @labelId.setter
    def labelId(self, labelId: str):
        self.__labelId = labelId

    @property
    def delphi_statement234(self):
        return self.__delphi_statement234

    @delphi_statement234.setter
    def delphi_statement234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement234", None)
        self.__delphi_statement234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_loopStmt"):
                opp_val = getattr(old_value, "delphi_loopStmt", None)
                if opp_val == self:
                    setattr(old_value, "delphi_loopStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_loopStmt"):
                opp_val = getattr(value, "delphi_loopStmt", None)
                setattr(value, "delphi_loopStmt", self)

    @property
    def delphi_statement246(self):
        return self.__delphi_statement246

    @delphi_statement246.setter
    def delphi_statement246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement246", None)
        self.__delphi_statement246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_withStmt245"):
                opp_val = getattr(old_value, "delphi_withStmt245", None)
                if opp_val == self:
                    setattr(old_value, "delphi_withStmt245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_withStmt245"):
                opp_val = getattr(value, "delphi_withStmt245", None)
                setattr(value, "delphi_withStmt245", self)

    @property
    def delphi_statement226(self):
        return self.__delphi_statement226

    @delphi_statement226.setter
    def delphi_statement226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement226", None)
        self.__delphi_statement226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_caseSelector225"):
                opp_val = getattr(old_value, "delphi_caseSelector225", None)
                if opp_val == self:
                    setattr(old_value, "delphi_caseSelector225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_caseSelector225"):
                opp_val = getattr(value, "delphi_caseSelector225", None)
                setattr(value, "delphi_caseSelector225", self)

    @property
    def delphi_statement(self):
        return self.__delphi_statement

    @delphi_statement.setter
    def delphi_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement", None)
        self.__delphi_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_stmtList"):
                opp_val = getattr(old_value, "delphi_stmtList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_stmtList"):
                opp_val = getattr(value, "delphi_stmtList", None)
                if opp_val is None:
                    setattr(value, "delphi_stmtList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_statement211(self):
        return self.__delphi_statement211

    @delphi_statement211.setter
    def delphi_statement211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement211", None)
        self.__delphi_statement211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_ifStmt210"):
                opp_val = getattr(old_value, "delphi_ifStmt210", None)
                if opp_val == self:
                    setattr(old_value, "delphi_ifStmt210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_ifStmt210"):
                opp_val = getattr(value, "delphi_ifStmt210", None)
                setattr(value, "delphi_ifStmt210", self)

    @property
    def delphi_statement203(self):
        return self.__delphi_statement203

    @delphi_statement203.setter
    def delphi_statement203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement203", None)
        self.__delphi_statement203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_unlabelledStatement"):
                opp_val = getattr(old_value, "delphi_unlabelledStatement", None)
                if opp_val == self:
                    setattr(old_value, "delphi_unlabelledStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_unlabelledStatement"):
                opp_val = getattr(value, "delphi_unlabelledStatement", None)
                setattr(value, "delphi_unlabelledStatement", self)

    @property
    def delphi_statement262(self):
        return self.__delphi_statement262

    @delphi_statement262.setter
    def delphi_statement262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement262", None)
        self.__delphi_statement262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_exceptionBlock261"):
                opp_val = getattr(old_value, "delphi_exceptionBlock261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_exceptionBlock261"):
                opp_val = getattr(value, "delphi_exceptionBlock261", None)
                if opp_val is None:
                    setattr(value, "delphi_exceptionBlock261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def delphi_statement214(self):
        return self.__delphi_statement214

    @delphi_statement214.setter
    def delphi_statement214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_statement__delphi_statement214", None)
        self.__delphi_statement214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_ifStmt213"):
                opp_val = getattr(old_value, "delphi_ifStmt213", None)
                if opp_val == self:
                    setattr(old_value, "delphi_ifStmt213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_ifStmt213"):
                opp_val = getattr(value, "delphi_ifStmt213", None)
                setattr(value, "delphi_ifStmt213", self)

class delphi_designatorSubPart(CSTrace):

    pass
class delphi_stmtList(CSTrace):

    pass
class delphi_mainRule(CSTrace):

    pass
class delphi_containsClause(CSTrace):

    pass
class delphi_requiresClause(CSTrace):

    pass
class delphi_initSection(CSTrace):

    pass
class delphi_implementationSection(CSTrace):

    pass
class delphi_interfaceSection(CSTrace):

    pass
class delphi_programBlock(CSTrace):

    pass
class delphi_identList(objFieldList, classHeritage):

    pass
class file:

    pass
class delphi_library(file):

    pass
class delphi_unit(file):

    def __init__(self, port: str, delphi_unit: "delphi_interfaceSection" = None, delphi_unit8: "delphi_implementationSection" = None, delphi_unit10: "delphi_initSection" = None):
        self.port = port
        self.delphi_unit = delphi_unit
        self.delphi_unit8 = delphi_unit8
        self.delphi_unit10 = delphi_unit10
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def delphi_unit(self):
        return self.__delphi_unit

    @delphi_unit.setter
    def delphi_unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_unit__delphi_unit", None)
        self.__delphi_unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_interfaceSection"):
                opp_val = getattr(old_value, "delphi_interfaceSection", None)
                if opp_val == self:
                    setattr(old_value, "delphi_interfaceSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_interfaceSection"):
                opp_val = getattr(value, "delphi_interfaceSection", None)
                setattr(value, "delphi_interfaceSection", self)

    @property
    def delphi_unit10(self):
        return self.__delphi_unit10

    @delphi_unit10.setter
    def delphi_unit10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_unit__delphi_unit10", None)
        self.__delphi_unit10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_initSection"):
                opp_val = getattr(old_value, "delphi_initSection", None)
                if opp_val == self:
                    setattr(old_value, "delphi_initSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_initSection"):
                opp_val = getattr(value, "delphi_initSection", None)
                setattr(value, "delphi_initSection", self)

    @property
    def delphi_unit8(self):
        return self.__delphi_unit8

    @delphi_unit8.setter
    def delphi_unit8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_delphi_unit__delphi_unit8", None)
        self.__delphi_unit8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delphi_implementationSection"):
                opp_val = getattr(old_value, "delphi_implementationSection", None)
                if opp_val == self:
                    setattr(old_value, "delphi_implementationSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delphi_implementationSection"):
                opp_val = getattr(value, "delphi_implementationSection", None)
                setattr(value, "delphi_implementationSection", self)

class delphi_packageDecl(file):

    pass
class delphi_program(file):

    pass
class delphi_ident(CSTrace):

    pass