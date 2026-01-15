from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Declarator:

    pass
class Typed:

    pass
class TemplateType:

    pass
class types_FixedPtType(TemplateType):

    pass
class types_WString(TemplateType):

    pass
class types_IdlString(TemplateType):

    pass
class types_SequenceType(Typed, TemplateType):

    pass
class types_ForwardDcl:

    pass
class MemberContainer:

    pass
class types_Declarator:

    pass
class PrimitiveType:

    pass
class types_IdlChar(PrimitiveType):

    pass
class types_WChar(PrimitiveType):

    pass
class types_Any(PrimitiveType):

    pass
class types_Octet(PrimitiveType):

    pass
class types_Float(PrimitiveType):

    pass
class types_Long(PrimitiveType):

    pass
class types_ULongLong(PrimitiveType):

    pass
class types_UShort(PrimitiveType):

    pass
class types_IdlWChar(PrimitiveType):

    pass
class types_Boolean(PrimitiveType):

    pass
class types_LongLong(PrimitiveType):

    pass
class types_ULong(PrimitiveType):

    pass
class types_IdlObject(PrimitiveType):

    pass
class types_ValueBaseType(PrimitiveType):

    pass
class types_LongDouble(PrimitiveType):

    pass
class types_Double(PrimitiveType):

    pass
class types_Short(PrimitiveType):

    pass
class IdlType:

    pass
class types_PrimitiveType(IdlType):

    pass
class types_TemplateType(IdlType):

    pass
class types_VoidType(IdlType):

    pass
class IdlTypeDcl:

    pass
class types_StructType(IdlTypeDcl, MemberContainer):

    pass
class types_StructForwardDcl(IdlTypeDcl):

    pass
class types_Enumeration(IdlTypeDcl, Declarator):

    pass
class types_UnionType(IdlTypeDcl):

    pass
class types_EnumType(IdlTypeDcl):

    pass
class TypedElement:

    pass
class types_TypeDef(IdlTypeDcl, TypedElement):

    pass
class types_Expression:

    pass
class CaseLabel:

    pass
class types_ExprCaseLabel(CaseLabel):

    pass
class types_DefaultCaseLabel(CaseLabel):

    pass
class types_IdlType:

    pass
class FileRegion:

    pass
class types_Case(FileRegion):

    pass
class types_CaseLabel(FileRegion):

    pass
class types_ElementSpec(FileRegion):

    pass
class types_Switch(FileRegion):

    pass
class types_UnionForwardDcl(IdlTypeDcl):

    pass