####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
identifications: Enumeration = Enumeration(
    name="identifications",
    literals={
            EnumerationLiteral(name="id"),
			EnumerationLiteral(name="identification")
    }
)

PreprocessingUnitTokens: Enumeration = Enumeration(
    name="PreprocessingUnitTokens",
    literals={
            EnumerationLiteral(name="division"),
			EnumerationLiteral(name="all"),
			EnumerationLiteral(name="end"),
			EnumerationLiteral(name="off"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="procedure"),
			EnumerationLiteral(name="by"),
			EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="of"),
			EnumerationLiteral(name="replacing"),
			EnumerationLiteral(name="suppress"),
			EnumerationLiteral(name="replace"),
			EnumerationLiteral(name="program")
    }
)

ZeroConstants: Enumeration = Enumeration(
    name="ZeroConstants",
    literals={
            EnumerationLiteral(name="zero"),
			EnumerationLiteral(name="zeros"),
			EnumerationLiteral(name="zeroes")
    }
)

QuoteConstants: Enumeration = Enumeration(
    name="QuoteConstants",
    literals={
            EnumerationLiteral(name="quote"),
			EnumerationLiteral(name="quotes")
    }
)

NullConstants: Enumeration = Enumeration(
    name="NullConstants",
    literals={
            EnumerationLiteral(name="null"),
			EnumerationLiteral(name="nulls")
    }
)

SpaceConstants: Enumeration = Enumeration(
    name="SpaceConstants",
    literals={
            EnumerationLiteral(name="space"),
			EnumerationLiteral(name="spaces")
    }
)

HighValueConstants: Enumeration = Enumeration(
    name="HighValueConstants",
    literals={
            EnumerationLiteral(name="highValue"),
			EnumerationLiteral(name="highValues")
    }
)

LowValueConstants: Enumeration = Enumeration(
    name="LowValueConstants",
    literals={
            EnumerationLiteral(name="lowValue"),
			EnumerationLiteral(name="lowValues")
    }
)

CobolSourceFormatTypeEnum: Enumeration = Enumeration(
    name="CobolSourceFormatTypeEnum",
    literals={
            EnumerationLiteral(name="ANSI85")
    }
)

# Classes
preprocess_containers_CobolRoot = Class(name="preprocess_containers_CobolRoot", is_abstract=True)
CobolLine = Class(name="CobolLine")
preprocess_containers_CopyUnit = Class(name="preprocess_containers_CopyUnit", is_abstract=True)
IncompleteElement = Class(name="IncompleteElement")
PreprocessingSentence = Class(name="PreprocessingSentence")
preprocess_containers_Copybook = Class(name="preprocess_containers_Copybook")
containers_CobolRoot = Class(name="containers_CobolRoot")
CopyUnit = Class(name="CopyUnit")
preprocess_Dummy = Class(name="preprocess_Dummy")
preprocess_containers_PreprocessingUnit = Class(name="preprocess_containers_PreprocessingUnit")
commons_NamedElement = Class(name="commons_NamedElement")
water_IncompleteElement = Class(name="water_IncompleteElement")
PreprocessingUnit = Class(name="PreprocessingUnit")
CobolWord = Class(name="CobolWord")
DataSegment = Class(name="DataSegment")
ProcedureSegment = Class(name="ProcedureSegment")
preprocess_containers_PreprocessingGroup = Class(name="preprocess_containers_PreprocessingGroup")
CobolRoot = Class(name="CobolRoot")
preprocess_water_Dot = Class(name="preprocess_water_Dot")
PreprocessingUnitWater = Class(name="PreprocessingUnitWater")
preprocess_water_Water = Class(name="preprocess_water_Water", is_abstract=True)
preprocess_water_IncompleteElement = Class(name="preprocess_water_IncompleteElement", is_abstract=True)
Water = Class(name="Water")
preprocess_water_DataSegmentWater = Class(name="preprocess_water_DataSegmentWater", is_abstract=True)
water_Water = Class(name="water_Water")
water_ProcedureSegmentWater = Class(name="water_ProcedureSegmentWater")
preprocess_containers_DataSegment = Class(name="preprocess_containers_DataSegment")
Segment = Class(name="Segment")
preprocess_containers_ProcedureSegment = Class(name="preprocess_containers_ProcedureSegment")
preprocess_containers_Segment = Class(name="preprocess_containers_Segment", is_abstract=True)
preprocess_containers_DataCopyUnit = Class(name="preprocess_containers_DataCopyUnit")
preprocess_containers_ProcedureCopyUnit = Class(name="preprocess_containers_ProcedureCopyUnit")
preprocess_water_PreprocessingUnitWater = Class(name="preprocess_water_PreprocessingUnitWater", is_abstract=True)
DataSegmentWater = Class(name="DataSegmentWater")
preprocess_commons_LibraryElement = Class(name="preprocess_commons_LibraryElement", is_abstract=True)
Element = Class(name="Element")
preprocess_commons_NamedElement = Class(name="preprocess_commons_NamedElement", is_abstract=True)
preprocess_commons_Element = Class(name="preprocess_commons_Element", is_abstract=True)
preprocess_literals_Literal = Class(name="preprocess_literals_Literal", is_abstract=True)
operands_Operand = Class(name="operands_Operand")
preprocess_water_ProcedureSegmentWater = Class(name="preprocess_water_ProcedureSegmentWater", is_abstract=True)
water_PreprocessingUnitWater = Class(name="water_PreprocessingUnitWater")
preprocess_literals_AlphanumericLiteral = Class(name="preprocess_literals_AlphanumericLiteral")
preprocess_water_By = Class(name="preprocess_water_By")
DataSegmentToken = Class(name="DataSegmentToken")
preprocess_water_In = Class(name="preprocess_water_In")
preprocess_water_Of = Class(name="preprocess_water_Of")
preprocess_water_Replacing = Class(name="preprocess_water_Replacing")
preprocess_water_Suppress = Class(name="preprocess_water_Suppress")
preprocess_water_Replace = Class(name="preprocess_water_Replace")
preprocess_water_Program = Class(name="preprocess_water_Program")
preprocess_water_Division = Class(name="preprocess_water_Division")
preprocess_water_All = Class(name="preprocess_water_All")
preprocess_water_End = Class(name="preprocess_water_End")
preprocess_water_Off = Class(name="preprocess_water_Off")
preprocess_water_On = Class(name="preprocess_water_On")
preprocess_water_Procedure = Class(name="preprocess_water_Procedure")
ProcedureSegmentWater = Class(name="ProcedureSegmentWater")
preprocess_water_DataSegmentToken = Class(name="preprocess_water_DataSegmentToken", is_abstract=True)
preprocess_sentences_CopySentence = Class(name="preprocess_sentences_CopySentence")
commons_LibraryElement = Class(name="commons_LibraryElement")
sentences_PreprocessingSentence = Class(name="sentences_PreprocessingSentence")
preprocess_sentences_Replacing = Class(name="preprocess_sentences_Replacing")
Operand = Class(name="Operand")
preprocess_sentences_PreprocessingSentence = Class(name="preprocess_sentences_PreprocessingSentence", is_abstract=True)
Replacing = Class(name="Replacing")
preprocess_sentences_ReplaceSentence = Class(name="preprocess_sentences_ReplaceSentence")
preprocess_literals_Space = Class(name="preprocess_literals_Space")
SpaceConstant = Class(name="SpaceConstant")
preprocess_literals_Spaces = Class(name="preprocess_literals_Spaces")
preprocess_literals_HighValue = Class(name="preprocess_literals_HighValue")
HighValueConstant = Class(name="HighValueConstant")
preprocess_literals_HighValues = Class(name="preprocess_literals_HighValues")
preprocess_literals_LowValue = Class(name="preprocess_literals_LowValue")
LowValueConstant = Class(name="LowValueConstant")
preprocess_literals_LowValues = Class(name="preprocess_literals_LowValues")
preprocess_literals_Zero = Class(name="preprocess_literals_Zero")
ZeroConstant = Class(name="ZeroConstant")
Literal = Class(name="Literal")
preprocess_literals_AlphanumericHexaDecimalLiteral = Class(name="preprocess_literals_AlphanumericHexaDecimalLiteral")
AlphanumericLiteral = Class(name="AlphanumericLiteral")
preprocess_literals_PseudoLiteral = Class(name="preprocess_literals_PseudoLiteral")
preprocess_literals_NumericLiteral = Class(name="preprocess_literals_NumericLiteral")
preprocess_literals_FigurativeConstantLiteral = Class(name="preprocess_literals_FigurativeConstantLiteral", is_abstract=True)
preprocess_literals_AllLiteral = Class(name="preprocess_literals_AllLiteral")
FigurativeConstantLiteral = Class(name="FigurativeConstantLiteral")
preprocess_literals_ConstantLiteral = Class(name="preprocess_literals_ConstantLiteral", is_abstract=True)
preprocess_literals_SpaceConstant = Class(name="preprocess_literals_SpaceConstant", is_abstract=True)
ConstantLiteral = Class(name="ConstantLiteral")
preprocess_literals_HighValueConstant = Class(name="preprocess_literals_HighValueConstant", is_abstract=True)
preprocess_literals_LowValueConstant = Class(name="preprocess_literals_LowValueConstant", is_abstract=True)
preprocess_literals_ZeroConstant = Class(name="preprocess_literals_ZeroConstant", is_abstract=True)
preprocess_literals_QuoteConstant = Class(name="preprocess_literals_QuoteConstant", is_abstract=True)
preprocess_literals_NullConstant = Class(name="preprocess_literals_NullConstant", is_abstract=True)
preprocess_layouts_ANSI85CobolSourceFormat = Class(name="preprocess_layouts_ANSI85CobolSourceFormat")
preprocess_literals_Zeroes = Class(name="preprocess_literals_Zeroes")
preprocess_literals_Zeros = Class(name="preprocess_literals_Zeros")
preprocess_literals_Quote = Class(name="preprocess_literals_Quote")
QuoteConstant = Class(name="QuoteConstant")
preprocess_literals_Quotes = Class(name="preprocess_literals_Quotes")
preprocess_literals_Null = Class(name="preprocess_literals_Null")
NullConstant = Class(name="NullConstant")
preprocess_literals_Nulls = Class(name="preprocess_literals_Nulls")
preprocess_operands_Operand = Class(name="preprocess_operands_Operand", is_abstract=True)
preprocess_operands_CobolWord = Class(name="preprocess_operands_CobolWord")
preprocess_statements_Statement = Class(name="preprocess_statements_Statement", is_abstract=True)
preprocess_statements_Execute = Class(name="preprocess_statements_Execute")
statements_Statement = Class(name="statements_Statement")
preprocess_layouts_CobolLine = Class(name="preprocess_layouts_CobolLine")
CobolSourceFormat = Class(name="CobolSourceFormat")
preprocess_layouts_CobolSourceFormat = Class(name="preprocess_layouts_CobolSourceFormat", is_abstract=True)

# preprocess_containers_CobolRoot class attributes and methods

# CobolLine class attributes and methods

# preprocess_containers_CopyUnit class attributes and methods

# IncompleteElement class attributes and methods

# PreprocessingSentence class attributes and methods

# preprocess_containers_Copybook class attributes and methods

# containers_CobolRoot class attributes and methods

# CopyUnit class attributes and methods

# preprocess_Dummy class attributes and methods

# preprocess_containers_PreprocessingUnit class attributes and methods
preprocess_containers_PreprocessingUnit_id: Property = Property(name="id", type=StringType)
preprocess_containers_PreprocessingUnit.attributes={preprocess_containers_PreprocessingUnit_id}

# commons_NamedElement class attributes and methods

# water_IncompleteElement class attributes and methods

# PreprocessingUnit class attributes and methods

# CobolWord class attributes and methods

# DataSegment class attributes and methods

# ProcedureSegment class attributes and methods

# preprocess_containers_PreprocessingGroup class attributes and methods

# CobolRoot class attributes and methods

# preprocess_water_Dot class attributes and methods

# PreprocessingUnitWater class attributes and methods

# preprocess_water_Water class attributes and methods

# preprocess_water_IncompleteElement class attributes and methods

# Water class attributes and methods

# preprocess_water_DataSegmentWater class attributes and methods

# water_Water class attributes and methods

# water_ProcedureSegmentWater class attributes and methods

# preprocess_containers_DataSegment class attributes and methods

# Segment class attributes and methods

# preprocess_containers_ProcedureSegment class attributes and methods

# preprocess_containers_Segment class attributes and methods

# preprocess_containers_DataCopyUnit class attributes and methods

# preprocess_containers_ProcedureCopyUnit class attributes and methods

# preprocess_water_PreprocessingUnitWater class attributes and methods

# DataSegmentWater class attributes and methods

# preprocess_commons_LibraryElement class attributes and methods
preprocess_commons_LibraryElement_libraryName: Property = Property(name="libraryName", type=StringType)
preprocess_commons_LibraryElement.attributes={preprocess_commons_LibraryElement_libraryName}

# Element class attributes and methods

# preprocess_commons_NamedElement class attributes and methods
preprocess_commons_NamedElement_name: Property = Property(name="name", type=StringType)
preprocess_commons_NamedElement.attributes={preprocess_commons_NamedElement_name}

# preprocess_commons_Element class attributes and methods

# preprocess_literals_Literal class attributes and methods

# operands_Operand class attributes and methods

# preprocess_water_ProcedureSegmentWater class attributes and methods

# water_PreprocessingUnitWater class attributes and methods

# preprocess_literals_AlphanumericLiteral class attributes and methods
preprocess_literals_AlphanumericLiteral_value: Property = Property(name="value", type=StringType)
preprocess_literals_AlphanumericLiteral.attributes={preprocess_literals_AlphanumericLiteral_value}

# preprocess_water_By class attributes and methods

# DataSegmentToken class attributes and methods

# preprocess_water_In class attributes and methods

# preprocess_water_Of class attributes and methods

# preprocess_water_Replacing class attributes and methods

# preprocess_water_Suppress class attributes and methods

# preprocess_water_Replace class attributes and methods

# preprocess_water_Program class attributes and methods

# preprocess_water_Division class attributes and methods

# preprocess_water_All class attributes and methods

# preprocess_water_End class attributes and methods

# preprocess_water_Off class attributes and methods

# preprocess_water_On class attributes and methods

# preprocess_water_Procedure class attributes and methods

# ProcedureSegmentWater class attributes and methods

# preprocess_water_DataSegmentToken class attributes and methods

# preprocess_sentences_CopySentence class attributes and methods
preprocess_sentences_CopySentence_suppress: Property = Property(name="suppress", type=BooleanType)
preprocess_sentences_CopySentence.attributes={preprocess_sentences_CopySentence_suppress}

# commons_LibraryElement class attributes and methods

# sentences_PreprocessingSentence class attributes and methods

# preprocess_sentences_Replacing class attributes and methods

# Operand class attributes and methods

# preprocess_sentences_PreprocessingSentence class attributes and methods

# Replacing class attributes and methods

# preprocess_sentences_ReplaceSentence class attributes and methods
preprocess_sentences_ReplaceSentence_switch: Property = Property(name="switch", type=BooleanType)
preprocess_sentences_ReplaceSentence.attributes={preprocess_sentences_ReplaceSentence_switch}

# preprocess_literals_Space class attributes and methods

# SpaceConstant class attributes and methods

# preprocess_literals_Spaces class attributes and methods

# preprocess_literals_HighValue class attributes and methods

# HighValueConstant class attributes and methods

# preprocess_literals_HighValues class attributes and methods

# preprocess_literals_LowValue class attributes and methods

# LowValueConstant class attributes and methods

# preprocess_literals_LowValues class attributes and methods

# preprocess_literals_Zero class attributes and methods

# ZeroConstant class attributes and methods

# Literal class attributes and methods

# preprocess_literals_AlphanumericHexaDecimalLiteral class attributes and methods

# AlphanumericLiteral class attributes and methods

# preprocess_literals_PseudoLiteral class attributes and methods
preprocess_literals_PseudoLiteral_value: Property = Property(name="value", type=StringType)
preprocess_literals_PseudoLiteral.attributes={preprocess_literals_PseudoLiteral_value}

# preprocess_literals_NumericLiteral class attributes and methods
preprocess_literals_NumericLiteral_value: Property = Property(name="value", type=StringType)
preprocess_literals_NumericLiteral.attributes={preprocess_literals_NumericLiteral_value}

# preprocess_literals_FigurativeConstantLiteral class attributes and methods

# preprocess_literals_AllLiteral class attributes and methods

# FigurativeConstantLiteral class attributes and methods

# preprocess_literals_ConstantLiteral class attributes and methods

# preprocess_literals_SpaceConstant class attributes and methods

# ConstantLiteral class attributes and methods

# preprocess_literals_HighValueConstant class attributes and methods

# preprocess_literals_LowValueConstant class attributes and methods

# preprocess_literals_ZeroConstant class attributes and methods

# preprocess_literals_QuoteConstant class attributes and methods

# preprocess_literals_NullConstant class attributes and methods

# preprocess_layouts_ANSI85CobolSourceFormat class attributes and methods

# preprocess_literals_Zeroes class attributes and methods

# preprocess_literals_Zeros class attributes and methods

# preprocess_literals_Quote class attributes and methods

# QuoteConstant class attributes and methods

# preprocess_literals_Quotes class attributes and methods

# preprocess_literals_Null class attributes and methods

# NullConstant class attributes and methods

# preprocess_literals_Nulls class attributes and methods

# preprocess_operands_Operand class attributes and methods

# preprocess_operands_CobolWord class attributes and methods
preprocess_operands_CobolWord_value: Property = Property(name="value", type=StringType)
preprocess_operands_CobolWord.attributes={preprocess_operands_CobolWord_value}

# preprocess_statements_Statement class attributes and methods

# preprocess_statements_Execute class attributes and methods
preprocess_statements_Execute_water: Property = Property(name="water", type=StringType)
preprocess_statements_Execute.attributes={preprocess_statements_Execute_water}

# statements_Statement class attributes and methods

# preprocess_layouts_CobolLine class attributes and methods
preprocess_layouts_CobolLine_comment: Property = Property(name="comment", type=StringType)
preprocess_layouts_CobolLine_contentAreaA: Property = Property(name="contentAreaA", type=StringType)
preprocess_layouts_CobolLine_contentAreaB: Property = Property(name="contentAreaB", type=StringType)
preprocess_layouts_CobolLine_indicatorArea: Property = Property(name="indicatorArea", type=StringType)
preprocess_layouts_CobolLine_sequenceArea: Property = Property(name="sequenceArea", type=StringType)
preprocess_layouts_CobolLine.attributes={preprocess_layouts_CobolLine_comment, preprocess_layouts_CobolLine_indicatorArea, preprocess_layouts_CobolLine_contentAreaB, preprocess_layouts_CobolLine_contentAreaA, preprocess_layouts_CobolLine_sequenceArea}

# CobolSourceFormat class attributes and methods

# preprocess_layouts_CobolSourceFormat class attributes and methods
preprocess_layouts_CobolSourceFormat_regex: Property = Property(name="regex", type=StringType)
preprocess_layouts_CobolSourceFormat_pattern: Property = Property(name="pattern", type=StringType)
preprocess_layouts_CobolSourceFormat_type: Property = Property(name="type", type=StringType)
preprocess_layouts_CobolSourceFormat_commentEntryMultiLine: Property = Property(name="commentEntryMultiLine", type=BooleanType)
preprocess_layouts_CobolSourceFormat.attributes={preprocess_layouts_CobolSourceFormat_pattern, preprocess_layouts_CobolSourceFormat_type, preprocess_layouts_CobolSourceFormat_commentEntryMultiLine, preprocess_layouts_CobolSourceFormat_regex}

# Relationships
preprocessingUnits7: BinaryAssociation = BinaryAssociation(
    name="preprocessingUnits7",
    ends={
        Property(name="PreprocessingUnit8", type=preprocess_containers_PreprocessingGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_PreprocessingGroup", type=PreprocessingUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines9: BinaryAssociation = BinaryAssociation(
    name="lines9",
    ends={
        Property(name="CobolLine", type=preprocess_containers_CobolRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_CobolRoot", type=CobolLine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sentence10: BinaryAssociation = BinaryAssociation(
    name="sentence10",
    ends={
        Property(name="PreprocessingSentence", type=preprocess_containers_CopyUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_CopyUnit", type=PreprocessingSentence, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nestedPreprocessingUnits0: BinaryAssociation = BinaryAssociation(
    name="nestedPreprocessingUnits0",
    ends={
        Property(name="PreprocessingUnit", type=preprocess_containers_PreprocessingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_PreprocessingUnit", type=PreprocessingUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ending1: BinaryAssociation = BinaryAssociation(
    name="ending1",
    ends={
        Property(name="CobolWord", type=preprocess_containers_PreprocessingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_PreprocessingUnit2", type=CobolWord, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataSegment3: BinaryAssociation = BinaryAssociation(
    name="dataSegment3",
    ends={
        Property(name="DataSegment", type=preprocess_containers_PreprocessingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_PreprocessingUnit4", type=DataSegment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
procedureSegment5: BinaryAssociation = BinaryAssociation(
    name="procedureSegment5",
    ends={
        Property(name="ProcedureSegment", type=preprocess_containers_PreprocessingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_PreprocessingUnit6", type=ProcedureSegment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
water14: BinaryAssociation = BinaryAssociation(
    name="water14",
    ends={
        Property(name="Water", type=preprocess_water_IncompleteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_water_IncompleteElement", type=Water, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyUnits11: BinaryAssociation = BinaryAssociation(
    name="copyUnits11",
    ends={
        Property(name="CopyUnit", type=preprocess_containers_Copybook, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_Copybook", type=CopyUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyUnits12: BinaryAssociation = BinaryAssociation(
    name="copyUnits12",
    ends={
        Property(name="CopyUnit13", type=preprocess_containers_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_containers_Segment", type=CopyUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location20: BinaryAssociation = BinaryAssociation(
    name="location20",
    ends={
        Property(name="CobolLine21", type=preprocess_commons_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_commons_Element", type=CobolLine, multiplicity=Multiplicity(0, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="Operand", type=preprocess_sentences_Replacing, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_sentences_Replacing", type=Operand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="Operand18", type=preprocess_sentences_Replacing, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_sentences_Replacing17", type=Operand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replacings19: BinaryAssociation = BinaryAssociation(
    name="replacings19",
    ends={
        Property(name="Replacing", type=preprocess_sentences_PreprocessingSentence, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_sentences_PreprocessingSentence", type=Replacing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant22: BinaryAssociation = BinaryAssociation(
    name="constant22",
    ends={
        Property(name="Literal", type=preprocess_literals_AllLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_literals_AllLiteral", type=Literal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lineFormat23: BinaryAssociation = BinaryAssociation(
    name="lineFormat23",
    ends={
        Property(name="CobolSourceFormat", type=preprocess_layouts_CobolLine, multiplicity=Multiplicity(1, 1)),
        Property(name="preprocess_layouts_CobolLine", type=CobolSourceFormat, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_preprocess_containers_CopyUnit_IncompleteElement = Generalization(general=IncompleteElement, specific=preprocess_containers_CopyUnit)
gen_preprocess_containers_Copybook_containers_CobolRoot = Generalization(general=containers_CobolRoot, specific=preprocess_containers_Copybook)
gen_preprocess_containers_Copybook_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=preprocess_containers_Copybook)
gen_preprocess_containers_Copybook_commons_NamedElement = Generalization(general=commons_NamedElement, specific=preprocess_containers_Copybook)
gen_preprocess_containers_PreprocessingUnit_commons_NamedElement = Generalization(general=commons_NamedElement, specific=preprocess_containers_PreprocessingUnit)
gen_preprocess_containers_PreprocessingUnit_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=preprocess_containers_PreprocessingUnit)
gen_preprocess_containers_PreprocessingGroup_CobolRoot = Generalization(general=CobolRoot, specific=preprocess_containers_PreprocessingGroup)
gen_preprocess_water_Dot_PreprocessingUnitWater = Generalization(general=PreprocessingUnitWater, specific=preprocess_water_Dot)
gen_preprocess_water_DataSegmentWater_water_Water = Generalization(general=water_Water, specific=preprocess_water_DataSegmentWater)
gen_preprocess_water_DataSegmentWater_water_ProcedureSegmentWater = Generalization(general=water_ProcedureSegmentWater, specific=preprocess_water_DataSegmentWater)
gen_preprocess_containers_DataSegment_Segment = Generalization(general=Segment, specific=preprocess_containers_DataSegment)
gen_preprocess_containers_ProcedureSegment_Segment = Generalization(general=Segment, specific=preprocess_containers_ProcedureSegment)
gen_preprocess_containers_Segment_IncompleteElement = Generalization(general=IncompleteElement, specific=preprocess_containers_Segment)
gen_preprocess_containers_DataCopyUnit_CopyUnit = Generalization(general=CopyUnit, specific=preprocess_containers_DataCopyUnit)
gen_preprocess_containers_ProcedureCopyUnit_CopyUnit = Generalization(general=CopyUnit, specific=preprocess_containers_ProcedureCopyUnit)
gen_preprocess_water_PreprocessingUnitWater_DataSegmentWater = Generalization(general=DataSegmentWater, specific=preprocess_water_PreprocessingUnitWater)
gen_preprocess_commons_LibraryElement_Element = Generalization(general=Element, specific=preprocess_commons_LibraryElement)
gen_preprocess_commons_NamedElement_Element = Generalization(general=Element, specific=preprocess_commons_NamedElement)
gen_preprocess_literals_Literal_operands_Operand = Generalization(general=operands_Operand, specific=preprocess_literals_Literal)
gen_preprocess_water_ProcedureSegmentWater_Water = Generalization(general=Water, specific=preprocess_water_ProcedureSegmentWater)
gen_preprocess_literals_Literal_water_PreprocessingUnitWater = Generalization(general=water_PreprocessingUnitWater, specific=preprocess_literals_Literal)
gen_preprocess_water_By_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_By)
gen_preprocess_water_In_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_In)
gen_preprocess_water_Of_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Of)
gen_preprocess_water_Replacing_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Replacing)
gen_preprocess_water_Suppress_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Suppress)
gen_preprocess_water_Replace_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Replace)
gen_preprocess_water_Program_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Program)
gen_preprocess_water_Division_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Division)
gen_preprocess_water_All_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_All)
gen_preprocess_water_End_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_End)
gen_preprocess_water_Off_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_Off)
gen_preprocess_water_On_DataSegmentToken = Generalization(general=DataSegmentToken, specific=preprocess_water_On)
gen_preprocess_water_Procedure_ProcedureSegmentWater = Generalization(general=ProcedureSegmentWater, specific=preprocess_water_Procedure)
gen_preprocess_water_DataSegmentToken_DataSegmentWater = Generalization(general=DataSegmentWater, specific=preprocess_water_DataSegmentToken)
gen_preprocess_sentences_CopySentence_commons_LibraryElement = Generalization(general=commons_LibraryElement, specific=preprocess_sentences_CopySentence)
gen_preprocess_sentences_CopySentence_sentences_PreprocessingSentence = Generalization(general=sentences_PreprocessingSentence, specific=preprocess_sentences_CopySentence)
gen_preprocess_sentences_CopySentence_commons_NamedElement = Generalization(general=commons_NamedElement, specific=preprocess_sentences_CopySentence)
gen_preprocess_sentences_ReplaceSentence_PreprocessingSentence = Generalization(general=PreprocessingSentence, specific=preprocess_sentences_ReplaceSentence)
gen_preprocess_literals_Space_SpaceConstant = Generalization(general=SpaceConstant, specific=preprocess_literals_Space)
gen_preprocess_literals_Spaces_SpaceConstant = Generalization(general=SpaceConstant, specific=preprocess_literals_Spaces)
gen_preprocess_literals_HighValue_HighValueConstant = Generalization(general=HighValueConstant, specific=preprocess_literals_HighValue)
gen_preprocess_literals_HighValues_HighValueConstant = Generalization(general=HighValueConstant, specific=preprocess_literals_HighValues)
gen_preprocess_literals_LowValue_LowValueConstant = Generalization(general=LowValueConstant, specific=preprocess_literals_LowValue)
gen_preprocess_literals_LowValues_LowValueConstant = Generalization(general=LowValueConstant, specific=preprocess_literals_LowValues)
gen_preprocess_literals_Zero_ZeroConstant = Generalization(general=ZeroConstant, specific=preprocess_literals_Zero)
gen_preprocess_literals_AlphanumericLiteral_Literal = Generalization(general=Literal, specific=preprocess_literals_AlphanumericLiteral)
gen_preprocess_literals_AlphanumericHexaDecimalLiteral_AlphanumericLiteral = Generalization(general=AlphanumericLiteral, specific=preprocess_literals_AlphanumericHexaDecimalLiteral)
gen_preprocess_literals_PseudoLiteral_Literal = Generalization(general=Literal, specific=preprocess_literals_PseudoLiteral)
gen_preprocess_literals_NumericLiteral_Literal = Generalization(general=Literal, specific=preprocess_literals_NumericLiteral)
gen_preprocess_literals_FigurativeConstantLiteral_Literal = Generalization(general=Literal, specific=preprocess_literals_FigurativeConstantLiteral)
gen_preprocess_literals_AllLiteral_FigurativeConstantLiteral = Generalization(general=FigurativeConstantLiteral, specific=preprocess_literals_AllLiteral)
gen_preprocess_literals_ConstantLiteral_FigurativeConstantLiteral = Generalization(general=FigurativeConstantLiteral, specific=preprocess_literals_ConstantLiteral)
gen_preprocess_literals_SpaceConstant_ConstantLiteral = Generalization(general=ConstantLiteral, specific=preprocess_literals_SpaceConstant)
gen_preprocess_literals_HighValueConstant_ConstantLiteral = Generalization(general=ConstantLiteral, specific=preprocess_literals_HighValueConstant)
gen_preprocess_literals_LowValueConstant_ConstantLiteral = Generalization(general=ConstantLiteral, specific=preprocess_literals_LowValueConstant)
gen_preprocess_literals_ZeroConstant_ConstantLiteral = Generalization(general=ConstantLiteral, specific=preprocess_literals_ZeroConstant)
gen_preprocess_literals_QuoteConstant_ConstantLiteral = Generalization(general=ConstantLiteral, specific=preprocess_literals_QuoteConstant)
gen_preprocess_literals_NullConstant_ConstantLiteral = Generalization(general=ConstantLiteral, specific=preprocess_literals_NullConstant)
gen_preprocess_layouts_ANSI85CobolSourceFormat_CobolSourceFormat = Generalization(general=CobolSourceFormat, specific=preprocess_layouts_ANSI85CobolSourceFormat)
gen_preprocess_literals_Zeroes_ZeroConstant = Generalization(general=ZeroConstant, specific=preprocess_literals_Zeroes)
gen_preprocess_literals_Zeros_ZeroConstant = Generalization(general=ZeroConstant, specific=preprocess_literals_Zeros)
gen_preprocess_literals_Quote_QuoteConstant = Generalization(general=QuoteConstant, specific=preprocess_literals_Quote)
gen_preprocess_literals_Quotes_QuoteConstant = Generalization(general=QuoteConstant, specific=preprocess_literals_Quotes)
gen_preprocess_literals_Null_NullConstant = Generalization(general=NullConstant, specific=preprocess_literals_Null)
gen_preprocess_literals_Nulls_NullConstant = Generalization(general=NullConstant, specific=preprocess_literals_Nulls)
gen_preprocess_operands_CobolWord_operands_Operand = Generalization(general=operands_Operand, specific=preprocess_operands_CobolWord)
gen_preprocess_operands_CobolWord_water_PreprocessingUnitWater = Generalization(general=water_PreprocessingUnitWater, specific=preprocess_operands_CobolWord)
gen_preprocess_statements_Execute_statements_Statement = Generalization(general=statements_Statement, specific=preprocess_statements_Execute)
gen_preprocess_statements_Execute_water_PreprocessingUnitWater = Generalization(general=water_PreprocessingUnitWater, specific=preprocess_statements_Execute)

# Domain Model
domain_model = DomainModel(
    name="preprocess",
    types={preprocess_containers_CobolRoot, CobolLine, preprocess_containers_CopyUnit, IncompleteElement, PreprocessingSentence, preprocess_containers_Copybook, containers_CobolRoot, CopyUnit, preprocess_Dummy, preprocess_containers_PreprocessingUnit, commons_NamedElement, water_IncompleteElement, PreprocessingUnit, CobolWord, DataSegment, ProcedureSegment, preprocess_containers_PreprocessingGroup, CobolRoot, preprocess_water_Dot, PreprocessingUnitWater, preprocess_water_Water, preprocess_water_IncompleteElement, Water, preprocess_water_DataSegmentWater, water_Water, water_ProcedureSegmentWater, preprocess_containers_DataSegment, Segment, preprocess_containers_ProcedureSegment, preprocess_containers_Segment, preprocess_containers_DataCopyUnit, preprocess_containers_ProcedureCopyUnit, preprocess_water_PreprocessingUnitWater, DataSegmentWater, preprocess_commons_LibraryElement, Element, preprocess_commons_NamedElement, preprocess_commons_Element, preprocess_literals_Literal, operands_Operand, preprocess_water_ProcedureSegmentWater, water_PreprocessingUnitWater, preprocess_literals_AlphanumericLiteral, preprocess_water_By, DataSegmentToken, preprocess_water_In, preprocess_water_Of, preprocess_water_Replacing, preprocess_water_Suppress, preprocess_water_Replace, preprocess_water_Program, preprocess_water_Division, preprocess_water_All, preprocess_water_End, preprocess_water_Off, preprocess_water_On, preprocess_water_Procedure, ProcedureSegmentWater, preprocess_water_DataSegmentToken, preprocess_sentences_CopySentence, commons_LibraryElement, sentences_PreprocessingSentence, preprocess_sentences_Replacing, Operand, preprocess_sentences_PreprocessingSentence, Replacing, preprocess_sentences_ReplaceSentence, preprocess_literals_Space, SpaceConstant, preprocess_literals_Spaces, preprocess_literals_HighValue, HighValueConstant, preprocess_literals_HighValues, preprocess_literals_LowValue, LowValueConstant, preprocess_literals_LowValues, preprocess_literals_Zero, ZeroConstant, Literal, preprocess_literals_AlphanumericHexaDecimalLiteral, AlphanumericLiteral, preprocess_literals_PseudoLiteral, preprocess_literals_NumericLiteral, preprocess_literals_FigurativeConstantLiteral, preprocess_literals_AllLiteral, FigurativeConstantLiteral, preprocess_literals_ConstantLiteral, preprocess_literals_SpaceConstant, ConstantLiteral, preprocess_literals_HighValueConstant, preprocess_literals_LowValueConstant, preprocess_literals_ZeroConstant, preprocess_literals_QuoteConstant, preprocess_literals_NullConstant, preprocess_layouts_ANSI85CobolSourceFormat, preprocess_literals_Zeroes, preprocess_literals_Zeros, preprocess_literals_Quote, QuoteConstant, preprocess_literals_Quotes, preprocess_literals_Null, NullConstant, preprocess_literals_Nulls, preprocess_operands_Operand, preprocess_operands_CobolWord, preprocess_statements_Statement, preprocess_statements_Execute, statements_Statement, preprocess_layouts_CobolLine, CobolSourceFormat, preprocess_layouts_CobolSourceFormat, identifications, PreprocessingUnitTokens, ZeroConstants, QuoteConstants, NullConstants, SpaceConstants, HighValueConstants, LowValueConstants, CobolSourceFormatTypeEnum},
    associations={preprocessingUnits7, lines9, sentence10, nestedPreprocessingUnits0, ending1, dataSegment3, procedureSegment5, water14, copyUnits11, copyUnits12, location20, source15, target16, replacings19, constant22, lineFormat23},
    generalizations={gen_preprocess_containers_CopyUnit_IncompleteElement, gen_preprocess_containers_Copybook_containers_CobolRoot, gen_preprocess_containers_Copybook_water_IncompleteElement, gen_preprocess_containers_Copybook_commons_NamedElement, gen_preprocess_containers_PreprocessingUnit_commons_NamedElement, gen_preprocess_containers_PreprocessingUnit_water_IncompleteElement, gen_preprocess_containers_PreprocessingGroup_CobolRoot, gen_preprocess_water_Dot_PreprocessingUnitWater, gen_preprocess_water_DataSegmentWater_water_Water, gen_preprocess_water_DataSegmentWater_water_ProcedureSegmentWater, gen_preprocess_containers_DataSegment_Segment, gen_preprocess_containers_ProcedureSegment_Segment, gen_preprocess_containers_Segment_IncompleteElement, gen_preprocess_containers_DataCopyUnit_CopyUnit, gen_preprocess_containers_ProcedureCopyUnit_CopyUnit, gen_preprocess_water_PreprocessingUnitWater_DataSegmentWater, gen_preprocess_commons_LibraryElement_Element, gen_preprocess_commons_NamedElement_Element, gen_preprocess_literals_Literal_operands_Operand, gen_preprocess_water_ProcedureSegmentWater_Water, gen_preprocess_literals_Literal_water_PreprocessingUnitWater, gen_preprocess_water_By_DataSegmentToken, gen_preprocess_water_In_DataSegmentToken, gen_preprocess_water_Of_DataSegmentToken, gen_preprocess_water_Replacing_DataSegmentToken, gen_preprocess_water_Suppress_DataSegmentToken, gen_preprocess_water_Replace_DataSegmentToken, gen_preprocess_water_Program_DataSegmentToken, gen_preprocess_water_Division_DataSegmentToken, gen_preprocess_water_All_DataSegmentToken, gen_preprocess_water_End_DataSegmentToken, gen_preprocess_water_Off_DataSegmentToken, gen_preprocess_water_On_DataSegmentToken, gen_preprocess_water_Procedure_ProcedureSegmentWater, gen_preprocess_water_DataSegmentToken_DataSegmentWater, gen_preprocess_sentences_CopySentence_commons_LibraryElement, gen_preprocess_sentences_CopySentence_sentences_PreprocessingSentence, gen_preprocess_sentences_CopySentence_commons_NamedElement, gen_preprocess_sentences_ReplaceSentence_PreprocessingSentence, gen_preprocess_literals_Space_SpaceConstant, gen_preprocess_literals_Spaces_SpaceConstant, gen_preprocess_literals_HighValue_HighValueConstant, gen_preprocess_literals_HighValues_HighValueConstant, gen_preprocess_literals_LowValue_LowValueConstant, gen_preprocess_literals_LowValues_LowValueConstant, gen_preprocess_literals_Zero_ZeroConstant, gen_preprocess_literals_AlphanumericLiteral_Literal, gen_preprocess_literals_AlphanumericHexaDecimalLiteral_AlphanumericLiteral, gen_preprocess_literals_PseudoLiteral_Literal, gen_preprocess_literals_NumericLiteral_Literal, gen_preprocess_literals_FigurativeConstantLiteral_Literal, gen_preprocess_literals_AllLiteral_FigurativeConstantLiteral, gen_preprocess_literals_ConstantLiteral_FigurativeConstantLiteral, gen_preprocess_literals_SpaceConstant_ConstantLiteral, gen_preprocess_literals_HighValueConstant_ConstantLiteral, gen_preprocess_literals_LowValueConstant_ConstantLiteral, gen_preprocess_literals_ZeroConstant_ConstantLiteral, gen_preprocess_literals_QuoteConstant_ConstantLiteral, gen_preprocess_literals_NullConstant_ConstantLiteral, gen_preprocess_layouts_ANSI85CobolSourceFormat_CobolSourceFormat, gen_preprocess_literals_Zeroes_ZeroConstant, gen_preprocess_literals_Zeros_ZeroConstant, gen_preprocess_literals_Quote_QuoteConstant, gen_preprocess_literals_Quotes_QuoteConstant, gen_preprocess_literals_Null_NullConstant, gen_preprocess_literals_Nulls_NullConstant, gen_preprocess_operands_CobolWord_operands_Operand, gen_preprocess_operands_CobolWord_water_PreprocessingUnitWater, gen_preprocess_statements_Execute_statements_Statement, gen_preprocess_statements_Execute_water_PreprocessingUnitWater},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)