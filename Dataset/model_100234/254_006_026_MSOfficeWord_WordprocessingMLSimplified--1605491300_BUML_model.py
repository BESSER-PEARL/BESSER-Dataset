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
FldCharTypeProperty: Enumeration = Enumeration(
    name="FldCharTypeProperty",
    literals={
            EnumerationLiteral(name="fctp_begin"),
			EnumerationLiteral(name="fctp_separate"),
			EnumerationLiteral(name="fctp_end")
    }
)

BreakType: Enumeration = Enumeration(
    name="BreakType",
    literals={
            EnumerationLiteral(name="bt_page"),
			EnumerationLiteral(name="bt_column"),
			EnumerationLiteral(name="bt_text_wrapping")
    }
)

NoteValue: Enumeration = Enumeration(
    name="NoteValue",
    literals={
            EnumerationLiteral(name="ftn_normal"),
			EnumerationLiteral(name="ftn_separator"),
			EnumerationLiteral(name="ftn_continuation_separator"),
			EnumerationLiteral(name="ftn_continuation_notice")
    }
)

OnOffType: Enumeration = Enumeration(
    name="OnOffType",
    literals={
            EnumerationLiteral(name="oot_off"),
			EnumerationLiteral(name="oot_on")
    }
)

# Classes
WordprocessingMLBasicDef_StringProperty = Class(name="WordprocessingMLBasicDef_StringProperty")
StringType = Class(name="StringType")
WordprocessingMLBasicDef_WordDocument = Class(name="WordprocessingMLBasicDef_WordDocument")
StringProperty = Class(name="StringProperty")
WordprocessingMLBasicDef_StringType = Class(name="WordprocessingMLBasicDef_StringType")
WordprocessingMLBasicDef_BlockLevelElt = Class(name="WordprocessingMLBasicDef_BlockLevelElt", is_abstract=True)
NoteElt = Class(name="NoteElt")
WordprocessingMLBasicDef_BlockLevelChunkElt = Class(name="WordprocessingMLBasicDef_BlockLevelChunkElt", is_abstract=True)
BodyElt = Class(name="BodyElt")
WordprocessingMLBasicDef_BodyElt = Class(name="WordprocessingMLBasicDef_BodyElt")
WordDocument = Class(name="WordDocument")
BlockLevelElt = Class(name="BlockLevelElt")
WordprocessingMLBasicDef_RunContentElt = Class(name="WordprocessingMLBasicDef_RunContentElt", is_abstract=True)
RunElt = Class(name="RunElt")
WordprocessingMLBasicDef_BreakElt = Class(name="WordprocessingMLBasicDef_BreakElt")
WordprocessingMLBasicDef_ParaElt = Class(name="WordprocessingMLBasicDef_ParaElt")
BlockLevelChunkElt = Class(name="BlockLevelChunkElt")
ParaContentElt = Class(name="ParaContentElt")
WordprocessingMLBasicDef_ParaContentElt = Class(name="WordprocessingMLBasicDef_ParaContentElt", is_abstract=True)
ParaElt = Class(name="ParaElt")
WordprocessingMLBasicDef_RunElt = Class(name="WordprocessingMLBasicDef_RunElt")
RunContentElt = Class(name="RunContentElt")
WordprocessingMLBasicDef_FootnoteRef = Class(name="WordprocessingMLBasicDef_FootnoteRef")
WordprocessingMLBasicDef_EndnoteRef = Class(name="WordprocessingMLBasicDef_EndnoteRef")
WordprocessingMLBasicDef_Separator = Class(name="WordprocessingMLBasicDef_Separator")
WordprocessingMLBasicDef_ContinuationSeparator = Class(name="WordprocessingMLBasicDef_ContinuationSeparator")
WordprocessingMLBasicDef_PgNum = Class(name="WordprocessingMLBasicDef_PgNum")
WordprocessingMLBasicDef_Text = Class(name="WordprocessingMLBasicDef_Text")
WordprocessingMLBasicDef_DelText = Class(name="WordprocessingMLBasicDef_DelText")
WordprocessingMLBasicDef_InstrText = Class(name="WordprocessingMLBasicDef_InstrText")
WordprocessingMLBasicDef_DelInstrText = Class(name="WordprocessingMLBasicDef_DelInstrText")
WordprocessingMLBasicDef_NoBreakHyphen = Class(name="WordprocessingMLBasicDef_NoBreakHyphen")
WordprocessingMLBasicDef_SoftHyphen = Class(name="WordprocessingMLBasicDef_SoftHyphen")
WordprocessingMLBasicDef_AnnotationRef = Class(name="WordprocessingMLBasicDef_AnnotationRef")
WordprocessingMLBasicDef_Symbol = Class(name="WordprocessingMLBasicDef_Symbol")
SymElt = Class(name="SymElt")
WordprocessingMLBasicDef_SymElt = Class(name="WordprocessingMLBasicDef_SymElt")
WordprocessingMLBasicDef_Cr = Class(name="WordprocessingMLBasicDef_Cr")
WordprocessingMLBasicDef_Footnote = Class(name="WordprocessingMLBasicDef_Footnote")
WordprocessingMLBasicDef_Tab = Class(name="WordprocessingMLBasicDef_Tab")
WordprocessingMLBasicDef_Endnote = Class(name="WordprocessingMLBasicDef_Endnote")
WordprocessingMLBasicDef_FldChar = Class(name="WordprocessingMLBasicDef_FldChar")
WordprocessingMLBasicDef_NoteElt = Class(name="WordprocessingMLBasicDef_NoteElt", is_abstract=True)
FldCharElt = Class(name="FldCharElt")
WordprocessingMLBasicDef_Picture = Class(name="WordprocessingMLBasicDef_Picture")
WordprocessingMLBasicDef_FldCharElt = Class(name="WordprocessingMLBasicDef_FldCharElt")

# WordprocessingMLBasicDef_StringProperty class attributes and methods

# StringType class attributes and methods

# WordprocessingMLBasicDef_WordDocument class attributes and methods

# StringProperty class attributes and methods

# WordprocessingMLBasicDef_StringType class attributes and methods
WordprocessingMLBasicDef_StringType_val: Property = Property(name="val", type=StringType)
WordprocessingMLBasicDef_StringType.attributes={WordprocessingMLBasicDef_StringType_val}

# WordprocessingMLBasicDef_BlockLevelElt class attributes and methods

# NoteElt class attributes and methods

# WordprocessingMLBasicDef_BlockLevelChunkElt class attributes and methods

# BodyElt class attributes and methods

# WordprocessingMLBasicDef_BodyElt class attributes and methods

# WordDocument class attributes and methods

# BlockLevelElt class attributes and methods

# WordprocessingMLBasicDef_RunContentElt class attributes and methods

# RunElt class attributes and methods

# WordprocessingMLBasicDef_BreakElt class attributes and methods
WordprocessingMLBasicDef_BreakElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLBasicDef_BreakElt.attributes={WordprocessingMLBasicDef_BreakElt_type}

# WordprocessingMLBasicDef_ParaElt class attributes and methods

# BlockLevelChunkElt class attributes and methods

# ParaContentElt class attributes and methods

# WordprocessingMLBasicDef_ParaContentElt class attributes and methods

# ParaElt class attributes and methods

# WordprocessingMLBasicDef_RunElt class attributes and methods

# RunContentElt class attributes and methods

# WordprocessingMLBasicDef_FootnoteRef class attributes and methods

# WordprocessingMLBasicDef_EndnoteRef class attributes and methods

# WordprocessingMLBasicDef_Separator class attributes and methods

# WordprocessingMLBasicDef_ContinuationSeparator class attributes and methods

# WordprocessingMLBasicDef_PgNum class attributes and methods

# WordprocessingMLBasicDef_Text class attributes and methods

# WordprocessingMLBasicDef_DelText class attributes and methods

# WordprocessingMLBasicDef_InstrText class attributes and methods

# WordprocessingMLBasicDef_DelInstrText class attributes and methods

# WordprocessingMLBasicDef_NoBreakHyphen class attributes and methods

# WordprocessingMLBasicDef_SoftHyphen class attributes and methods

# WordprocessingMLBasicDef_AnnotationRef class attributes and methods

# WordprocessingMLBasicDef_Symbol class attributes and methods

# SymElt class attributes and methods

# WordprocessingMLBasicDef_SymElt class attributes and methods

# WordprocessingMLBasicDef_Cr class attributes and methods

# WordprocessingMLBasicDef_Footnote class attributes and methods

# WordprocessingMLBasicDef_Tab class attributes and methods

# WordprocessingMLBasicDef_Endnote class attributes and methods

# WordprocessingMLBasicDef_FldChar class attributes and methods

# WordprocessingMLBasicDef_NoteElt class attributes and methods
WordprocessingMLBasicDef_NoteElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLBasicDef_NoteElt_suppressRef: Property = Property(name="suppressRef", type=StringType)
WordprocessingMLBasicDef_NoteElt.attributes={WordprocessingMLBasicDef_NoteElt_suppressRef, WordprocessingMLBasicDef_NoteElt_type}

# FldCharElt class attributes and methods

# WordprocessingMLBasicDef_Picture class attributes and methods

# WordprocessingMLBasicDef_FldCharElt class attributes and methods
WordprocessingMLBasicDef_FldCharElt_fldLock: Property = Property(name="fldLock", type=StringType)
WordprocessingMLBasicDef_FldCharElt_fldCharType: Property = Property(name="fldCharType", type=StringType)
WordprocessingMLBasicDef_FldCharElt.attributes={WordprocessingMLBasicDef_FldCharElt_fldCharType, WordprocessingMLBasicDef_FldCharElt_fldLock}

# Relationships
ble_bodyElt7: BinaryAssociation = BinaryAssociation(
    name="ble_bodyElt7",
    ends={
        Property(name="BodyElt8", type=WordprocessingMLBasicDef_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="blockLevelElts", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)
ble_note9: BinaryAssociation = BinaryAssociation(
    name="ble_note9",
    ends={
        Property(name="NoteElt", type=WordprocessingMLBasicDef_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="n_blockLevelElts", type=NoteElt, multiplicity=Multiplicity(1, 1))
    }
)
ignoreSubtree0: BinaryAssociation = BinaryAssociation(
    name="ignoreSubtree0",
    ends={
        Property(name="StringProperty", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_WordDocument", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ignoreElements1: BinaryAssociation = BinaryAssociation(
    name="ignoreElements1",
    ends={
        Property(name="StringProperty3", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_WordDocument2", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body4: BinaryAssociation = BinaryAssociation(
    name="body4",
    ends={
        Property(name="BodyElt", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="be_wordDocument", type=BodyElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
be_wordDocument5: BinaryAssociation = BinaryAssociation(
    name="be_wordDocument5",
    ends={
        Property(name="WordDocument", type=WordprocessingMLBasicDef_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
blockLevelElts6: BinaryAssociation = BinaryAssociation(
    name="blockLevelElts6",
    ends={
        Property(name="BlockLevelElt", type=WordprocessingMLBasicDef_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_bodyElt", type=BlockLevelElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rContentElts12: BinaryAssociation = BinaryAssociation(
    name="rContentElts12",
    ends={
        Property(name="rce_rElt", type=RunContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="RunContentElt", type=WordprocessingMLBasicDef_RunElt, multiplicity=Multiplicity(1, 1))
    }
)
rce_rElt13: BinaryAssociation = BinaryAssociation(
    name="rce_rElt13",
    ends={
        Property(name="RunElt", type=WordprocessingMLBasicDef_RunContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rContentElts", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
pContentElts10: BinaryAssociation = BinaryAssociation(
    name="pContentElts10",
    ends={
        Property(name="ParaContentElt", type=WordprocessingMLBasicDef_ParaElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pce_pElt", type=ParaContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pce_pElt11: BinaryAssociation = BinaryAssociation(
    name="pce_pElt11",
    ends={
        Property(name="ParaElt", type=WordprocessingMLBasicDef_ParaContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pContentElts", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
font16: BinaryAssociation = BinaryAssociation(
    name="font16",
    ends={
        Property(name="StringType", type=WordprocessingMLBasicDef_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_SymElt", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
char17: BinaryAssociation = BinaryAssociation(
    name="char17",
    ends={
        Property(name="StringType19", type=WordprocessingMLBasicDef_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_SymElt18", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
n_blockLevelElts14: BinaryAssociation = BinaryAssociation(
    name="n_blockLevelElts14",
    ends={
        Property(name="BlockLevelElt15", type=WordprocessingMLBasicDef_NoteElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_note", type=BlockLevelElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fldData20: BinaryAssociation = BinaryAssociation(
    name="fldData20",
    ends={
        Property(name="StringType21", type=WordprocessingMLBasicDef_FldCharElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_FldCharElt", type=StringType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_WordprocessingMLBasicDef_StringProperty_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_StringProperty)
gen_WordprocessingMLBasicDef_BreakElt_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_BreakElt)
gen_WordprocessingMLBasicDef_BlockLevelChunkElt_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLBasicDef_BlockLevelChunkElt)
gen_WordprocessingMLBasicDef_ParaElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLBasicDef_ParaElt)
gen_WordprocessingMLBasicDef_RunElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLBasicDef_RunElt)
gen_WordprocessingMLBasicDef_FootnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_FootnoteRef)
gen_WordprocessingMLBasicDef_EndnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_EndnoteRef)
gen_WordprocessingMLBasicDef_Separator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Separator)
gen_WordprocessingMLBasicDef_ContinuationSeparator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_ContinuationSeparator)
gen_WordprocessingMLBasicDef_Text_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Text)
gen_WordprocessingMLBasicDef_Text_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_Text)
gen_WordprocessingMLBasicDef_DelText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_DelText)
gen_WordprocessingMLBasicDef_DelText_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_DelText)
gen_WordprocessingMLBasicDef_InstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_InstrText)
gen_WordprocessingMLBasicDef_InstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_InstrText)
gen_WordprocessingMLBasicDef_DelInstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_DelInstrText)
gen_WordprocessingMLBasicDef_DelInstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_DelInstrText)
gen_WordprocessingMLBasicDef_NoBreakHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_NoBreakHyphen)
gen_WordprocessingMLBasicDef_SoftHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_SoftHyphen)
gen_WordprocessingMLBasicDef_AnnotationRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_AnnotationRef)
gen_WordprocessingMLBasicDef_Symbol_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Symbol)
gen_WordprocessingMLBasicDef_Symbol_SymElt = Generalization(general=SymElt, specific=WordprocessingMLBasicDef_Symbol)
gen_WordprocessingMLBasicDef_PgNum_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_PgNum)
gen_WordprocessingMLBasicDef_Cr_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Cr)
gen_WordprocessingMLBasicDef_Footnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Footnote)
gen_WordprocessingMLBasicDef_Footnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLBasicDef_Footnote)
gen_WordprocessingMLBasicDef_Tab_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Tab)
gen_WordprocessingMLBasicDef_Endnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Endnote)
gen_WordprocessingMLBasicDef_Endnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLBasicDef_Endnote)
gen_WordprocessingMLBasicDef_FldChar_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_FldChar)
gen_WordprocessingMLBasicDef_FldChar_FldCharElt = Generalization(general=FldCharElt, specific=WordprocessingMLBasicDef_FldChar)
gen_WordprocessingMLBasicDef_Picture_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Picture)

# Domain Model
domain_model = DomainModel(
    name="WordprocessingMLBasicDef",
    types={WordprocessingMLBasicDef_StringProperty, StringType, WordprocessingMLBasicDef_WordDocument, StringProperty, WordprocessingMLBasicDef_StringType, WordprocessingMLBasicDef_BlockLevelElt, NoteElt, WordprocessingMLBasicDef_BlockLevelChunkElt, BodyElt, WordprocessingMLBasicDef_BodyElt, WordDocument, BlockLevelElt, WordprocessingMLBasicDef_RunContentElt, RunElt, WordprocessingMLBasicDef_BreakElt, WordprocessingMLBasicDef_ParaElt, BlockLevelChunkElt, ParaContentElt, WordprocessingMLBasicDef_ParaContentElt, ParaElt, WordprocessingMLBasicDef_RunElt, RunContentElt, WordprocessingMLBasicDef_FootnoteRef, WordprocessingMLBasicDef_EndnoteRef, WordprocessingMLBasicDef_Separator, WordprocessingMLBasicDef_ContinuationSeparator, WordprocessingMLBasicDef_PgNum, WordprocessingMLBasicDef_Text, WordprocessingMLBasicDef_DelText, WordprocessingMLBasicDef_InstrText, WordprocessingMLBasicDef_DelInstrText, WordprocessingMLBasicDef_NoBreakHyphen, WordprocessingMLBasicDef_SoftHyphen, WordprocessingMLBasicDef_AnnotationRef, WordprocessingMLBasicDef_Symbol, SymElt, WordprocessingMLBasicDef_SymElt, WordprocessingMLBasicDef_Cr, WordprocessingMLBasicDef_Footnote, WordprocessingMLBasicDef_Tab, WordprocessingMLBasicDef_Endnote, WordprocessingMLBasicDef_FldChar, WordprocessingMLBasicDef_NoteElt, FldCharElt, WordprocessingMLBasicDef_Picture, WordprocessingMLBasicDef_FldCharElt, FldCharTypeProperty, BreakType, NoteValue, OnOffType},
    associations={ble_bodyElt7, ble_note9, ignoreSubtree0, ignoreElements1, body4, be_wordDocument5, blockLevelElts6, rContentElts12, rce_rElt13, pContentElts10, pce_pElt11, font16, char17, n_blockLevelElts14, fldData20},
    generalizations={gen_WordprocessingMLBasicDef_StringProperty_StringType, gen_WordprocessingMLBasicDef_BreakElt_RunContentElt, gen_WordprocessingMLBasicDef_BlockLevelChunkElt_BlockLevelElt, gen_WordprocessingMLBasicDef_ParaElt_BlockLevelChunkElt, gen_WordprocessingMLBasicDef_RunElt_ParaContentElt, gen_WordprocessingMLBasicDef_FootnoteRef_RunContentElt, gen_WordprocessingMLBasicDef_EndnoteRef_RunContentElt, gen_WordprocessingMLBasicDef_Separator_RunContentElt, gen_WordprocessingMLBasicDef_ContinuationSeparator_RunContentElt, gen_WordprocessingMLBasicDef_Text_RunContentElt, gen_WordprocessingMLBasicDef_Text_StringType, gen_WordprocessingMLBasicDef_DelText_RunContentElt, gen_WordprocessingMLBasicDef_DelText_StringType, gen_WordprocessingMLBasicDef_InstrText_RunContentElt, gen_WordprocessingMLBasicDef_InstrText_StringType, gen_WordprocessingMLBasicDef_DelInstrText_RunContentElt, gen_WordprocessingMLBasicDef_DelInstrText_StringType, gen_WordprocessingMLBasicDef_NoBreakHyphen_RunContentElt, gen_WordprocessingMLBasicDef_SoftHyphen_RunContentElt, gen_WordprocessingMLBasicDef_AnnotationRef_RunContentElt, gen_WordprocessingMLBasicDef_Symbol_RunContentElt, gen_WordprocessingMLBasicDef_Symbol_SymElt, gen_WordprocessingMLBasicDef_PgNum_RunContentElt, gen_WordprocessingMLBasicDef_Cr_RunContentElt, gen_WordprocessingMLBasicDef_Footnote_RunContentElt, gen_WordprocessingMLBasicDef_Footnote_NoteElt, gen_WordprocessingMLBasicDef_Tab_RunContentElt, gen_WordprocessingMLBasicDef_Endnote_RunContentElt, gen_WordprocessingMLBasicDef_Endnote_NoteElt, gen_WordprocessingMLBasicDef_FldChar_RunContentElt, gen_WordprocessingMLBasicDef_FldChar_FldCharElt, gen_WordprocessingMLBasicDef_Picture_RunContentElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)