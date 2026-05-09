from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class QuoteConstants(Enum):
    quote = "quote"
    quotes = "quotes"
class identifications(Enum):
    id = "id"
    identification = "identification"
class SpaceConstants(Enum):
    space = "space"
    spaces = "spaces"
class CobolSourceFormatTypeEnum(Enum):
    ANSI85 = "ANSI85"
class NullConstants(Enum):
    null = "null"
    nulls = "nulls"
class LowValueConstants(Enum):
    lowValue = "lowValue"
    lowValues = "lowValues"
class PreprocessingUnitTokens(Enum):
    division = "division"
    all = "all"
    end = "end"
    off = "off"
    on = "on"
    procedure = "procedure"
    by = "by"
    in_ = "in_"
    of = "of"
    replacing = "replacing"
    suppress = "suppress"
    replace = "replace"
    program = "program"
class ZeroConstants(Enum):
    zero = "zero"
    zeros = "zeros"
    zeroes = "zeroes"
class HighValueConstants(Enum):
    highValue = "highValue"
    highValues = "highValues"


############################################
# Definition of Classes
############################################

class preprocess_layouts_CobolSourceFormat(ABC):

    def __init__(self, regex: str, pattern: str, type: str, commentEntryMultiLine: bool):
        self.regex = regex
        self.pattern = pattern
        self.type = type
        self.commentEntryMultiLine = commentEntryMultiLine
        
        pass
    @property
    def commentEntryMultiLine(self):
        return self.__commentEntryMultiLine

    @commentEntryMultiLine.setter
    def commentEntryMultiLine(self, commentEntryMultiLine: bool):
        self.__commentEntryMultiLine = commentEntryMultiLine


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def regex(self):
        return self.__regex

    @regex.setter
    def regex(self, regex: str):
        self.__regex = regex


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class CobolSourceFormat:

    pass
class preprocess_layouts_CobolLine:

    def __init__(self, comment: str, contentAreaA: str, contentAreaB: str, indicatorArea: str, sequenceArea: str, preprocess_layouts_CobolLine: "CobolSourceFormat" = None):
        self.comment = comment
        self.contentAreaA = contentAreaA
        self.contentAreaB = contentAreaB
        self.indicatorArea = indicatorArea
        self.sequenceArea = sequenceArea
        self.preprocess_layouts_CobolLine = preprocess_layouts_CobolLine
        
        pass
    @property
    def sequenceArea(self):
        return self.__sequenceArea

    @sequenceArea.setter
    def sequenceArea(self, sequenceArea: str):
        self.__sequenceArea = sequenceArea


    @property
    def contentAreaB(self):
        return self.__contentAreaB

    @contentAreaB.setter
    def contentAreaB(self, contentAreaB: str):
        self.__contentAreaB = contentAreaB


    @property
    def indicatorArea(self):
        return self.__indicatorArea

    @indicatorArea.setter
    def indicatorArea(self, indicatorArea: str):
        self.__indicatorArea = indicatorArea


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def contentAreaA(self):
        return self.__contentAreaA

    @contentAreaA.setter
    def contentAreaA(self, contentAreaA: str):
        self.__contentAreaA = contentAreaA


    @property
    def preprocess_layouts_CobolLine(self):
        return self.__preprocess_layouts_CobolLine

    @preprocess_layouts_CobolLine.setter
    def preprocess_layouts_CobolLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_preprocess_layouts_CobolLine__preprocess_layouts_CobolLine", None)
        self.__preprocess_layouts_CobolLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CobolSourceFormat"):
                opp_val = getattr(old_value, "CobolSourceFormat", None)
                if opp_val == self:
                    setattr(old_value, "CobolSourceFormat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CobolSourceFormat"):
                opp_val = getattr(value, "CobolSourceFormat", None)
                setattr(value, "CobolSourceFormat", self)

class statements_Statement:

    pass
class preprocess_statements_Statement(ABC):

    pass
class preprocess_operands_Operand(ABC):

    pass
class NullConstant:

    pass
class preprocess_literals_Nulls(NullConstant):

    pass
class preprocess_literals_Null(NullConstant):

    pass
class QuoteConstant:

    pass
class preprocess_literals_Quotes(QuoteConstant):

    pass
class preprocess_literals_Quote(QuoteConstant):

    pass
class preprocess_layouts_ANSI85CobolSourceFormat(CobolSourceFormat):

    pass
class ConstantLiteral:

    pass
class preprocess_literals_ZeroConstant(ConstantLiteral):

    pass
class preprocess_literals_HighValueConstant(ConstantLiteral):

    pass
class preprocess_literals_LowValueConstant(ConstantLiteral):

    pass
class preprocess_literals_NullConstant(ConstantLiteral):

    pass
class preprocess_literals_QuoteConstant(ConstantLiteral):

    pass
class preprocess_literals_SpaceConstant(ConstantLiteral):

    pass
class FigurativeConstantLiteral:

    pass
class preprocess_literals_ConstantLiteral(FigurativeConstantLiteral):

    pass
class preprocess_literals_AllLiteral(FigurativeConstantLiteral):

    pass
class AlphanumericLiteral:

    pass
class preprocess_literals_AlphanumericHexaDecimalLiteral(AlphanumericLiteral):

    pass
class Literal:

    pass
class preprocess_literals_PseudoLiteral(Literal):

    def __init__(self, value: str, Literal: "preprocess_literals_AllLiteral" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class preprocess_literals_NumericLiteral(Literal):

    def __init__(self, value: str, Literal: "preprocess_literals_AllLiteral" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class preprocess_literals_FigurativeConstantLiteral(Literal):

    pass
class ZeroConstant:

    pass
class preprocess_literals_Zeroes(ZeroConstant):

    pass
class preprocess_literals_Zeros(ZeroConstant):

    pass
class preprocess_literals_Zero(ZeroConstant):

    pass
class LowValueConstant:

    pass
class preprocess_literals_LowValues(LowValueConstant):

    pass
class preprocess_literals_LowValue(LowValueConstant):

    pass
class HighValueConstant:

    pass
class preprocess_literals_HighValues(HighValueConstant):

    pass
class preprocess_literals_HighValue(HighValueConstant):

    pass
class SpaceConstant:

    pass
class preprocess_literals_Spaces(SpaceConstant):

    pass
class preprocess_literals_Space(SpaceConstant):

    pass
class Replacing:

    pass
class preprocess_sentences_PreprocessingSentence(ABC):

    pass
class Operand:

    pass
class preprocess_sentences_Replacing:

    pass
class sentences_PreprocessingSentence:

    pass
class commons_LibraryElement:

    pass
class ProcedureSegmentWater:

    pass
class preprocess_water_Procedure(ProcedureSegmentWater):

    pass
class DataSegmentToken:

    pass
class preprocess_water_Replacing(DataSegmentToken):

    pass
class preprocess_water_On(DataSegmentToken):

    pass
class preprocess_water_In(DataSegmentToken):

    pass
class preprocess_water_Off(DataSegmentToken):

    pass
class preprocess_water_All(DataSegmentToken):

    pass
class preprocess_water_Suppress(DataSegmentToken):

    pass
class preprocess_water_Replace(DataSegmentToken):

    pass
class preprocess_water_Of(DataSegmentToken):

    pass
class preprocess_water_End(DataSegmentToken):

    pass
class preprocess_water_Program(DataSegmentToken):

    pass
class preprocess_water_Division(DataSegmentToken):

    pass
class preprocess_water_By(DataSegmentToken):

    pass
class preprocess_literals_AlphanumericLiteral(Literal):

    def __init__(self, value: str, Literal: "preprocess_literals_AllLiteral" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class water_PreprocessingUnitWater:

    pass
class preprocess_statements_Execute(statements_Statement, water_PreprocessingUnitWater):

    def __init__(self, water: str):
        self.water = water
        
        pass
    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, water: str):
        self.__water = water


class operands_Operand:

    pass
class preprocess_operands_CobolWord(operands_Operand, water_PreprocessingUnitWater):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class preprocess_literals_Literal(operands_Operand, water_PreprocessingUnitWater):

    pass
class preprocess_commons_Element(ABC):

    pass
class Element:

    pass
class preprocess_commons_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class preprocess_commons_LibraryElement(Element):

    def __init__(self, libraryName: str):
        self.libraryName = libraryName
        
        pass
    @property
    def libraryName(self):
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName


class DataSegmentWater:

    pass
class preprocess_water_DataSegmentToken(DataSegmentWater):

    pass
class preprocess_water_PreprocessingUnitWater(DataSegmentWater):

    pass
class Segment:

    pass
class preprocess_containers_ProcedureSegment(Segment):

    pass
class preprocess_containers_DataSegment(Segment):

    pass
class water_ProcedureSegmentWater:

    pass
class water_Water:

    pass
class preprocess_water_DataSegmentWater(water_Water, water_ProcedureSegmentWater):

    pass
class Water:

    pass
class preprocess_water_ProcedureSegmentWater(Water):

    pass
class preprocess_water_IncompleteElement(ABC):

    pass
class preprocess_water_Water(ABC):

    pass
class PreprocessingUnitWater:

    pass
class preprocess_water_Dot(PreprocessingUnitWater):

    pass
class CobolRoot:

    pass
class preprocess_containers_PreprocessingGroup(CobolRoot):

    pass
class ProcedureSegment:

    pass
class DataSegment:

    pass
class CobolWord:

    pass
class PreprocessingUnit:

    pass
class water_IncompleteElement:

    pass
class commons_NamedElement:

    pass
class preprocess_sentences_CopySentence(sentences_PreprocessingSentence, commons_LibraryElement, commons_NamedElement):

    def __init__(self, suppress: bool):
        self.suppress = suppress
        
        pass
    @property
    def suppress(self):
        return self.__suppress

    @suppress.setter
    def suppress(self, suppress: bool):
        self.__suppress = suppress


class preprocess_containers_PreprocessingUnit(water_IncompleteElement, commons_NamedElement):

    def __init__(self, id: str, preprocess_containers_PreprocessingUnit: set["PreprocessingUnit"] = None, preprocess_containers_PreprocessingUnit2: "CobolWord" = None, preprocess_containers_PreprocessingUnit4: "DataSegment" = None, preprocess_containers_PreprocessingUnit6: "ProcedureSegment" = None):
        self.id = id
        self.preprocess_containers_PreprocessingUnit = preprocess_containers_PreprocessingUnit if preprocess_containers_PreprocessingUnit is not None else set()
        self.preprocess_containers_PreprocessingUnit2 = preprocess_containers_PreprocessingUnit2
        self.preprocess_containers_PreprocessingUnit4 = preprocess_containers_PreprocessingUnit4
        self.preprocess_containers_PreprocessingUnit6 = preprocess_containers_PreprocessingUnit6
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def preprocess_containers_PreprocessingUnit4(self):
        return self.__preprocess_containers_PreprocessingUnit4

    @preprocess_containers_PreprocessingUnit4.setter
    def preprocess_containers_PreprocessingUnit4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_preprocess_containers_PreprocessingUnit__preprocess_containers_PreprocessingUnit4", None)
        self.__preprocess_containers_PreprocessingUnit4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataSegment"):
                opp_val = getattr(old_value, "DataSegment", None)
                if opp_val == self:
                    setattr(old_value, "DataSegment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataSegment"):
                opp_val = getattr(value, "DataSegment", None)
                setattr(value, "DataSegment", self)

    @property
    def preprocess_containers_PreprocessingUnit6(self):
        return self.__preprocess_containers_PreprocessingUnit6

    @preprocess_containers_PreprocessingUnit6.setter
    def preprocess_containers_PreprocessingUnit6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_preprocess_containers_PreprocessingUnit__preprocess_containers_PreprocessingUnit6", None)
        self.__preprocess_containers_PreprocessingUnit6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcedureSegment"):
                opp_val = getattr(old_value, "ProcedureSegment", None)
                if opp_val == self:
                    setattr(old_value, "ProcedureSegment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcedureSegment"):
                opp_val = getattr(value, "ProcedureSegment", None)
                setattr(value, "ProcedureSegment", self)

    @property
    def preprocess_containers_PreprocessingUnit(self):
        return self.__preprocess_containers_PreprocessingUnit

    @preprocess_containers_PreprocessingUnit.setter
    def preprocess_containers_PreprocessingUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_preprocess_containers_PreprocessingUnit__preprocess_containers_PreprocessingUnit", None)
        self.__preprocess_containers_PreprocessingUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PreprocessingUnit"):
                    opp_val = getattr(item, "PreprocessingUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "PreprocessingUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PreprocessingUnit"):
                    opp_val = getattr(item, "PreprocessingUnit", None)
                    
                    setattr(item, "PreprocessingUnit", self)
                    

    @property
    def preprocess_containers_PreprocessingUnit2(self):
        return self.__preprocess_containers_PreprocessingUnit2

    @preprocess_containers_PreprocessingUnit2.setter
    def preprocess_containers_PreprocessingUnit2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_preprocess_containers_PreprocessingUnit__preprocess_containers_PreprocessingUnit2", None)
        self.__preprocess_containers_PreprocessingUnit2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CobolWord"):
                opp_val = getattr(old_value, "CobolWord", None)
                if opp_val == self:
                    setattr(old_value, "CobolWord", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CobolWord"):
                opp_val = getattr(value, "CobolWord", None)
                setattr(value, "CobolWord", self)

class preprocess_Dummy:

    pass
class CopyUnit:

    pass
class preprocess_containers_ProcedureCopyUnit(CopyUnit):

    pass
class preprocess_containers_DataCopyUnit(CopyUnit):

    pass
class containers_CobolRoot:

    pass
class preprocess_containers_Copybook(water_IncompleteElement, commons_NamedElement, containers_CobolRoot):

    pass
class PreprocessingSentence:

    pass
class preprocess_sentences_ReplaceSentence(PreprocessingSentence):

    def __init__(self, switch: bool, PreprocessingSentence: "preprocess_containers_CopyUnit" = None):
        self.switch = switch
        
        pass
    @property
    def switch(self):
        return self.__switch

    @switch.setter
    def switch(self, switch: bool):
        self.__switch = switch


class IncompleteElement:

    pass
class preprocess_containers_Segment(IncompleteElement):

    pass
class preprocess_containers_CopyUnit(IncompleteElement):

    pass
class CobolLine:

    pass
class preprocess_containers_CobolRoot(ABC):

    pass