import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    triplet,
    afpText_IDESize,
    afpText_FontHorizontalScaleFactor,
    afpText_ObjectClassification,
    afpText_FinishingOperation,
    afpText_BandImageData,
    afpText_DeviceAppearance,
    afpText_ColorSpecification,
    afpText_UniversalDateAndTimeStamp,
    afpText_ExtendedResourceLocalIdentifier,
    afpText_ResourceSectionNumber,
    afpText_EndImage,
    afpText_GSCS,
    afpText_GSCP,
    afpText_GCBEZ,
    afpText_LineDataObjectPositionMigration,
    afpText_FontDescriptorSpecification,
    afpText_ObjectOriginIdentifier,
    afpText_GSLT,
    afpText_MediumOrientation,
    afpText_TileSize,
    afpText_EncodingSchemeID,
    afpText_FontFidelity,
    afpText_BeginImage,
    afpText_GCMRK,
    afpText_GSCR,
    afpText_ImageSize,
    afpText_PagePositionInformation,
    afpText_GFLT,
    afpText_ImageData,
    afpText_AttributeValue,
    afpText_EndTransparencyMask,
    afpText_GSPCOL,
    afpText_TBM,
    afpText_GSGCH,
    afpText_ExternalAlgorithm,
    afpText_ObjectOffset,
    afpText_GCPARC,
    afpText_MappingOption,
    afpText_ObjectCount,
    afpText_TonerSaver,
    afpText_GSPT,
    afpText_GSCD,
    afpText_BandImage,
    afpText_RenderingIntent,
    afpText_GSBMX,
    afpText_ImageEncoding,
    afpText_ImageResolution,
    afpText_CharacterRotation,
    afpText_GCFLT,
    afpText_ObjectStructuredFieldExtent,
    afpText_GSMS,
    afpText_ObjectContainerPresentationSpaceSize,
    afpText_ImageSubsampling,
    afpText_GPARC,
    afpText_CGCSGID,
    afpText_ColorManagementResourceDescriptor,
    afpText_MODCAInterchangeSet,
    afpText_EndSegment,
    afpText_GFARC,
    afpText_TextFidelity,
    afpText_IDEStructure,
    afpText_FNNRG2,
    afpText_BeginTransparencyMask,
    afpText_GSCH,
    afpText_GSECOL,
    afpText_ResourceUsageAttribute,
    afpText_IncludeTile,
    afpText_ObjectStructuredFieldOffset,
    afpText_ResourceObjectInclude,
    afpText_ResourceObjectType,
    afpText_LocalDateAndTimeStamp,
    afpText_EndSegmentCommand,
    afpText_GCCHST,
    afpText_ResourceLocalIdentifier,
    afpText_GSAP,
    afpText_GBIMG,
    afpText_GCCBEZ,
    afpText_GSMT,
    afpText_GCFARC,
    afpText_GMRK,
    afpText_BeginSegmentCommand,
    afpText_FullyQualifiedName,
    afpText_SamplingRatios,
    afpText_MetricAdjustment,
    afpText_DataObjectFontDescriptor,
    afpText_MediumMapPageNumber,
    afpText_GEIMG,
    afpText_GSFLW,
    afpText_GNOP1,
    afpText_GCLINE,
    afpText_LocaleSelector,
    afpText_MediaEjectControl,
    afpText_GEAR,
    afpText_MeasurementUnits,
    afpText_DrawingOrderSubset,
    afpText_ObjectByteOffset,
    afpText_GSCA,
    afpText_GCBOX,
    afpText_ExtensionFont,
    afpText_PresentationSpaceResetMixing,
    afpText_TilePosition,
    afpText_GLINE,
    afpText_GSMC,
    afpText_PageOverlayConditionalProcessing,
    afpText_CMRFidelity,
    afpText_GBAR,
    afpText_GIMD,
    afpText_TileTOC,
    afpText_CRCResourceManagement,
    afpText_GSCC,
    afpText_ObjectByteExtent,
    afpText_ObjectFunctionSetSpecification,
    afpText_GCBIMG,
    afpText_GEPROL,
    afpText_MediaFidelity,
    afpText_FinishingFidelity,
    afpText_ImageLUTID,
    afpText_GSCOL,
    afpText_AMI,
    afpText_Comment,
    afpText_WindowSpecification,
    afpText_FontResolution,
    afpText_TextOrientation,
    afpText_UP3iFinishingOperation,
    afpText_BeginSegment,
    afpText_EndTile,
    afpText_PresentationSpaceMixingRules,
    afpText_AttributeQualifier,
    afpText_TRN,
    afpText_GSLE,
    afpText_BSU,
    afpText_FontCodedGraphicCharacterSetGlobalIdentifier,
    afpText_GCOMT,
    afpText_BeginTile,
    afpText_USC,
    afpText_PresentationControl,
    afpText_DescriptorPosition,
    afpText_TileSetColor,
    afpText_GSLJ,
    afpText_IOCAFunctionSetIdentification,
    afpText_GBOX,
    afpText_ColorFidelity,
    afpText_GSLW,
    afpText_GSMX,
    afpText_GCHST,
    afpText_GCRLINE,
    afpText_GRLINE,
    afpText_SetBiLevelImageColor,
    afpText_ObjectAreaSize,
    afpText_BLN,
    afpText_GSMP,
    afpText_GSPS,
    afpText_AMB,
    afpText_SVI,
    afpText_STO,
    afpText_STC,
    afpText_SIM,
    afpText_SIA,
    afpText_SEC,
    afpText_SCFL,
    afpText_SBI,
    afpText_RPS,
    afpText_RMI,
    afpText_RMB,
    afpText_OVS,
    afpText_NOPCS,
    afpText_ESU,
    afpText_DIR,
    afpText_DBR,
    afpText_GCRLINERG,
    afpText_GRLINERG,
    afpText_GCMRKRG,
    afpText_GMRKRG,
    afpText_GCLINERG,
    afpText_GLINERG,
    afpText_GCFLTRG,
    afpText_GFLTRG,
    afpText_GCCBEZRG,
    afpText_GCBEZRG,
    afpText_FNNRG,
    afpText_ExternalAlgorithmRG,
    afpText_SamplingRatiosRG,
    afpText_TileTOCRG,
    afpText_BandImageRG,
    afpText_PPORG,
    afpText_PGPRG,
    afpText_MSURG,
    afpText_MPSRG,
    afpText_MPORG,
    afpText_MPGRG,
    afpText_MMTRG,
    afpText_MMORG,
    afpText_MMDRG,
    afpText_MMCRG,
    afpText_MIORG,
    afpText_MGORG,
    afpText_MCARG,
    afpText_MDRRG,
    afpText_MCF1RG,
    afpText_MCFRG,
    afpText_MCDRG,
    afpText_MCCRG,
    afpText_MBCRG,
    afpText_LLERG,
    afpText_CPIRG,
    afpText_CFIRG,
    afpText_triplet,
    structuredField,
    afpText_PGP1,
    afpText_BPM,
    afpText_MPO,
    afpText_BPF,
    afpText_BRG,
    afpText_EAG,
    afpText_CAT,
    afpText_MCD,
    afpText_BDT,
    afpText_BMM,
    afpText_ECF,
    afpText_BOG,
    afpText_PMC,
    afpText_BFM,
    afpText_BRS,
    afpText_PTX,
    afpText_LNC,
    afpText_MFC,
    afpText_MPS,
    afpText_PTD1,
    afpText_MCF1,
    afpText_LND,
    afpText_BDI,
    afpText_BPG,
    afpText_CFI,
    afpText_NOP,
    afpText_PTD,
    afpText_OCD,
    afpText_LLE,
    afpText_BPS,
    afpText_MDD,
    afpText_MPG,
    afpText_MMT,
    afpText_EDM,
    afpText_PEC,
    afpText_DXD,
    afpText_CPD,
    afpText_ECA,
    afpText_CDD,
    afpText_BFN,
    afpText_BII,
    afpText_PGP,
    afpText_PGD,
    afpText_BOC,
    afpText_TLE,
    afpText_BDG,
    afpText_CFC,
    afpText_MIO,
    afpText_BBC,
    afpText_BAG,
    afpText_PPO,
    afpText_BPT,
    afpText_ECP,
    afpText_MMO,
    afpText_BCP,
    afpText_MGO,
    afpText_PFC,
    afpText_CTC,
    afpText_BSG,
    afpText_BGR,
    afpText_BCF,
    afpText_MBC,
    afpText_BDM,
    afpText_FGD,
    afpText_MDR,
    afpText_MMC,
    afpText_BFG,
    afpText_MSU,
    afpText_EBC,
    afpText_OBD,
    afpText_CPI,
    afpText_BCA,
    afpText_EDG,
    afpText_OBP,
    afpText_BNG,
    afpText_BMO,
    afpText_CPC,
    afpText_MCA,
    afpText_MCC,
    afpText_MCF,
    afpText_EDI,
    afpText_BDD,
    afpText_MMD,
    afpText_BDA,
    afpText_BIM,
    afpText_BDX,
    afpText_LineData,
    afpText_structuredField,
    afpText_Model,
    afpText_IPO,
    afpText_IRD,
    afpText_IPS,
    afpText_IPG,
    afpText_IPD,
    afpText_ICP,
    afpText_IOC,
    afpText_IOB,
    afpText_IMM,
    afpText_IID,
    afpText_IEL,
    afpText_IDD,
    afpText_GDD,
    afpText_GAD,
    afpText_FNPRG,
    afpText_FNP,
    afpText_FNORG,
    afpText_FNO,
    afpText_FNMRG,
    afpText_FNM,
    afpText_FNN,
    afpText_FNIRG,
    afpText_FNI,
    afpText_FNG,
    afpText_EPT,
    afpText_FND,
    afpText_FNC,
    afpText_ESG,
    afpText_ERS,
    afpText_ERG,
    afpText_EIM,
    afpText_EPS,
    afpText_EPM,
    afpText_EPG,
    afpText_EPF,
    afpText_EOG,
    afpText_EOC,
    afpText_ENG,
    afpText_EMO,
    afpText_EMM,
    afpText_EII,
    afpText_EGR,
    afpText_EFN,
    afpText_EFM,
    afpText_EFG,
    afpText_EDX,
    afpText_EDT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_triplet_is_not_abstract():
    assert not inspect.isabstract(triplet)


def test_triplet_constructor_exists():
    assert callable(triplet.__init__)


def test_triplet_constructor_args():
    sig = inspect.signature(triplet.__init__)
    params = list(sig.parameters.keys())



def test_afptext_idesize_is_not_abstract():
    assert not inspect.isabstract(afpText_IDESize)


def test_afptext_idesize_constructor_exists():
    assert callable(afpText_IDESize.__init__)


def test_afptext_idesize_constructor_args():
    sig = inspect.signature(afpText_IDESize.__init__)
    params = list(sig.parameters.keys())
    assert "IDESZ" in params, "Missing parameter 'IDESZ'"

def test_afptext_idesize_has_IDESZ():
    assert hasattr(afpText_IDESize, "IDESZ")
    descriptor = None
    for klass in afpText_IDESize.__mro__:
        if "IDESZ" in klass.__dict__:
            descriptor = klass.__dict__["IDESZ"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fonthorizontalscalefactor_is_not_abstract():
    assert not inspect.isabstract(afpText_FontHorizontalScaleFactor)


def test_afptext_fonthorizontalscalefactor_constructor_exists():
    assert callable(afpText_FontHorizontalScaleFactor.__init__)


def test_afptext_fonthorizontalscalefactor_constructor_args():
    sig = inspect.signature(afpText_FontHorizontalScaleFactor.__init__)
    params = list(sig.parameters.keys())
    assert "Hscale" in params, "Missing parameter 'Hscale'"

def test_afptext_fonthorizontalscalefactor_has_Hscale():
    assert hasattr(afpText_FontHorizontalScaleFactor, "Hscale")
    descriptor = None
    for klass in afpText_FontHorizontalScaleFactor.__mro__:
        if "Hscale" in klass.__dict__:
            descriptor = klass.__dict__["Hscale"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectclassification_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectClassification)


def test_afptext_objectclassification_constructor_exists():
    assert callable(afpText_ObjectClassification.__init__)


def test_afptext_objectclassification_constructor_args():
    sig = inspect.signature(afpText_ObjectClassification.__init__)
    params = list(sig.parameters.keys())
    assert "ObjClass" in params, "Missing parameter 'ObjClass'"
    assert "CompName" in params, "Missing parameter 'CompName'"
    assert "StrucFlgs" in params, "Missing parameter 'StrucFlgs'"
    assert "ObjLev" in params, "Missing parameter 'ObjLev'"
    assert "RegObjId" in params, "Missing parameter 'RegObjId'"
    assert "ObjTpName" in params, "Missing parameter 'ObjTpName'"

def test_afptext_objectclassification_has_ObjClass():
    assert hasattr(afpText_ObjectClassification, "ObjClass")
    descriptor = None
    for klass in afpText_ObjectClassification.__mro__:
        if "ObjClass" in klass.__dict__:
            descriptor = klass.__dict__["ObjClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectclassification_has_CompName():
    assert hasattr(afpText_ObjectClassification, "CompName")
    descriptor = None
    for klass in afpText_ObjectClassification.__mro__:
        if "CompName" in klass.__dict__:
            descriptor = klass.__dict__["CompName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectclassification_has_StrucFlgs():
    assert hasattr(afpText_ObjectClassification, "StrucFlgs")
    descriptor = None
    for klass in afpText_ObjectClassification.__mro__:
        if "StrucFlgs" in klass.__dict__:
            descriptor = klass.__dict__["StrucFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectclassification_has_ObjLev():
    assert hasattr(afpText_ObjectClassification, "ObjLev")
    descriptor = None
    for klass in afpText_ObjectClassification.__mro__:
        if "ObjLev" in klass.__dict__:
            descriptor = klass.__dict__["ObjLev"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectclassification_has_RegObjId():
    assert hasattr(afpText_ObjectClassification, "RegObjId")
    descriptor = None
    for klass in afpText_ObjectClassification.__mro__:
        if "RegObjId" in klass.__dict__:
            descriptor = klass.__dict__["RegObjId"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectclassification_has_ObjTpName():
    assert hasattr(afpText_ObjectClassification, "ObjTpName")
    descriptor = None
    for klass in afpText_ObjectClassification.__mro__:
        if "ObjTpName" in klass.__dict__:
            descriptor = klass.__dict__["ObjTpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_finishingoperation_is_not_abstract():
    assert not inspect.isabstract(afpText_FinishingOperation)


def test_afptext_finishingoperation_constructor_exists():
    assert callable(afpText_FinishingOperation.__init__)


def test_afptext_finishingoperation_constructor_args():
    sig = inspect.signature(afpText_FinishingOperation.__init__)
    params = list(sig.parameters.keys())
    assert "AxOffst" in params, "Missing parameter 'AxOffst'"
    assert "FOpCnt" in params, "Missing parameter 'FOpCnt'"
    assert "FOpType" in params, "Missing parameter 'FOpType'"
    assert "RefEdge" in params, "Missing parameter 'RefEdge'"
    assert "OpPos" in params, "Missing parameter 'OpPos'"

def test_afptext_finishingoperation_has_AxOffst():
    assert hasattr(afpText_FinishingOperation, "AxOffst")
    descriptor = None
    for klass in afpText_FinishingOperation.__mro__:
        if "AxOffst" in klass.__dict__:
            descriptor = klass.__dict__["AxOffst"]
            break
    assert isinstance(descriptor, property)

def test_afptext_finishingoperation_has_FOpCnt():
    assert hasattr(afpText_FinishingOperation, "FOpCnt")
    descriptor = None
    for klass in afpText_FinishingOperation.__mro__:
        if "FOpCnt" in klass.__dict__:
            descriptor = klass.__dict__["FOpCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_finishingoperation_has_FOpType():
    assert hasattr(afpText_FinishingOperation, "FOpType")
    descriptor = None
    for klass in afpText_FinishingOperation.__mro__:
        if "FOpType" in klass.__dict__:
            descriptor = klass.__dict__["FOpType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_finishingoperation_has_RefEdge():
    assert hasattr(afpText_FinishingOperation, "RefEdge")
    descriptor = None
    for klass in afpText_FinishingOperation.__mro__:
        if "RefEdge" in klass.__dict__:
            descriptor = klass.__dict__["RefEdge"]
            break
    assert isinstance(descriptor, property)

def test_afptext_finishingoperation_has_OpPos():
    assert hasattr(afpText_FinishingOperation, "OpPos")
    descriptor = None
    for klass in afpText_FinishingOperation.__mro__:
        if "OpPos" in klass.__dict__:
            descriptor = klass.__dict__["OpPos"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bandimagedata_is_not_abstract():
    assert not inspect.isabstract(afpText_BandImageData)


def test_afptext_bandimagedata_constructor_exists():
    assert callable(afpText_BandImageData.__init__)


def test_afptext_bandimagedata_constructor_args():
    sig = inspect.signature(afpText_BandImageData.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"
    assert "BANDNUM" in params, "Missing parameter 'BANDNUM'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"

def test_afptext_bandimagedata_has_DATA():
    assert hasattr(afpText_BandImageData, "DATA")
    descriptor = None
    for klass in afpText_BandImageData.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bandimagedata_has_BANDNUM():
    assert hasattr(afpText_BandImageData, "BANDNUM")
    descriptor = None
    for klass in afpText_BandImageData.__mro__:
        if "BANDNUM" in klass.__dict__:
            descriptor = klass.__dict__["BANDNUM"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bandimagedata_has_RESERVED():
    assert hasattr(afpText_BandImageData, "RESERVED")
    descriptor = None
    for klass in afpText_BandImageData.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)



def test_afptext_deviceappearance_is_not_abstract():
    assert not inspect.isabstract(afpText_DeviceAppearance)


def test_afptext_deviceappearance_constructor_exists():
    assert callable(afpText_DeviceAppearance.__init__)


def test_afptext_deviceappearance_constructor_args():
    sig = inspect.signature(afpText_DeviceAppearance.__init__)
    params = list(sig.parameters.keys())
    assert "DevApp" in params, "Missing parameter 'DevApp'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_deviceappearance_has_DevApp():
    assert hasattr(afpText_DeviceAppearance, "DevApp")
    descriptor = None
    for klass in afpText_DeviceAppearance.__mro__:
        if "DevApp" in klass.__dict__:
            descriptor = klass.__dict__["DevApp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_deviceappearance_has_Reserved():
    assert hasattr(afpText_DeviceAppearance, "Reserved")
    descriptor = None
    for klass in afpText_DeviceAppearance.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_colorspecification_is_not_abstract():
    assert not inspect.isabstract(afpText_ColorSpecification)


def test_afptext_colorspecification_constructor_exists():
    assert callable(afpText_ColorSpecification.__init__)


def test_afptext_colorspecification_constructor_args():
    sig = inspect.signature(afpText_ColorSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "ColSpce" in params, "Missing parameter 'ColSpce'"
    assert "ColSize2" in params, "Missing parameter 'ColSize2'"
    assert "ColSize4" in params, "Missing parameter 'ColSize4'"
    assert "ColSize1" in params, "Missing parameter 'ColSize1'"
    assert "ColSize3" in params, "Missing parameter 'ColSize3'"
    assert "Color" in params, "Missing parameter 'Color'"

def test_afptext_colorspecification_has_ColSpce():
    assert hasattr(afpText_ColorSpecification, "ColSpce")
    descriptor = None
    for klass in afpText_ColorSpecification.__mro__:
        if "ColSpce" in klass.__dict__:
            descriptor = klass.__dict__["ColSpce"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorspecification_has_ColSize2():
    assert hasattr(afpText_ColorSpecification, "ColSize2")
    descriptor = None
    for klass in afpText_ColorSpecification.__mro__:
        if "ColSize2" in klass.__dict__:
            descriptor = klass.__dict__["ColSize2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorspecification_has_ColSize4():
    assert hasattr(afpText_ColorSpecification, "ColSize4")
    descriptor = None
    for klass in afpText_ColorSpecification.__mro__:
        if "ColSize4" in klass.__dict__:
            descriptor = klass.__dict__["ColSize4"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorspecification_has_ColSize1():
    assert hasattr(afpText_ColorSpecification, "ColSize1")
    descriptor = None
    for klass in afpText_ColorSpecification.__mro__:
        if "ColSize1" in klass.__dict__:
            descriptor = klass.__dict__["ColSize1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorspecification_has_ColSize3():
    assert hasattr(afpText_ColorSpecification, "ColSize3")
    descriptor = None
    for klass in afpText_ColorSpecification.__mro__:
        if "ColSize3" in klass.__dict__:
            descriptor = klass.__dict__["ColSize3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorspecification_has_Color():
    assert hasattr(afpText_ColorSpecification, "Color")
    descriptor = None
    for klass in afpText_ColorSpecification.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)



def test_afptext_universaldateandtimestamp_is_not_abstract():
    assert not inspect.isabstract(afpText_UniversalDateAndTimeStamp)


def test_afptext_universaldateandtimestamp_constructor_exists():
    assert callable(afpText_UniversalDateAndTimeStamp.__init__)


def test_afptext_universaldateandtimestamp_constructor_args():
    sig = inspect.signature(afpText_UniversalDateAndTimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "Second" in params, "Missing parameter 'Second'"
    assert "Hour" in params, "Missing parameter 'Hour'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "YearAD" in params, "Missing parameter 'YearAD'"
    assert "Day" in params, "Missing parameter 'Day'"
    assert "UTCDiffM" in params, "Missing parameter 'UTCDiffM'"
    assert "TimeZone" in params, "Missing parameter 'TimeZone'"
    assert "UTCDiffH" in params, "Missing parameter 'UTCDiffH'"
    assert "Minute" in params, "Missing parameter 'Minute'"
    assert "Month" in params, "Missing parameter 'Month'"

def test_afptext_universaldateandtimestamp_has_Second():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "Second")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "Second" in klass.__dict__:
            descriptor = klass.__dict__["Second"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_Hour():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "Hour")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "Hour" in klass.__dict__:
            descriptor = klass.__dict__["Hour"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_Reserved():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "Reserved")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_YearAD():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "YearAD")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "YearAD" in klass.__dict__:
            descriptor = klass.__dict__["YearAD"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_Day():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "Day")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "Day" in klass.__dict__:
            descriptor = klass.__dict__["Day"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_UTCDiffM():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "UTCDiffM")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "UTCDiffM" in klass.__dict__:
            descriptor = klass.__dict__["UTCDiffM"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_TimeZone():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "TimeZone")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "TimeZone" in klass.__dict__:
            descriptor = klass.__dict__["TimeZone"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_UTCDiffH():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "UTCDiffH")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "UTCDiffH" in klass.__dict__:
            descriptor = klass.__dict__["UTCDiffH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_Minute():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "Minute")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "Minute" in klass.__dict__:
            descriptor = klass.__dict__["Minute"]
            break
    assert isinstance(descriptor, property)

def test_afptext_universaldateandtimestamp_has_Month():
    assert hasattr(afpText_UniversalDateAndTimeStamp, "Month")
    descriptor = None
    for klass in afpText_UniversalDateAndTimeStamp.__mro__:
        if "Month" in klass.__dict__:
            descriptor = klass.__dict__["Month"]
            break
    assert isinstance(descriptor, property)



def test_afptext_extendedresourcelocalidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText_ExtendedResourceLocalIdentifier)


def test_afptext_extendedresourcelocalidentifier_constructor_exists():
    assert callable(afpText_ExtendedResourceLocalIdentifier.__init__)


def test_afptext_extendedresourcelocalidentifier_constructor_args():
    sig = inspect.signature(afpText_ExtendedResourceLocalIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "ResLID" in params, "Missing parameter 'ResLID'"
    assert "ResType" in params, "Missing parameter 'ResType'"

def test_afptext_extendedresourcelocalidentifier_has_ResLID():
    assert hasattr(afpText_ExtendedResourceLocalIdentifier, "ResLID")
    descriptor = None
    for klass in afpText_ExtendedResourceLocalIdentifier.__mro__:
        if "ResLID" in klass.__dict__:
            descriptor = klass.__dict__["ResLID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_extendedresourcelocalidentifier_has_ResType():
    assert hasattr(afpText_ExtendedResourceLocalIdentifier, "ResType")
    descriptor = None
    for klass in afpText_ExtendedResourceLocalIdentifier.__mro__:
        if "ResType" in klass.__dict__:
            descriptor = klass.__dict__["ResType"]
            break
    assert isinstance(descriptor, property)



def test_afptext_resourcesectionnumber_is_not_abstract():
    assert not inspect.isabstract(afpText_ResourceSectionNumber)


def test_afptext_resourcesectionnumber_constructor_exists():
    assert callable(afpText_ResourceSectionNumber.__init__)


def test_afptext_resourcesectionnumber_constructor_args():
    sig = inspect.signature(afpText_ResourceSectionNumber.__init__)
    params = list(sig.parameters.keys())
    assert "ResSNum" in params, "Missing parameter 'ResSNum'"

def test_afptext_resourcesectionnumber_has_ResSNum():
    assert hasattr(afpText_ResourceSectionNumber, "ResSNum")
    descriptor = None
    for klass in afpText_ResourceSectionNumber.__mro__:
        if "ResSNum" in klass.__dict__:
            descriptor = klass.__dict__["ResSNum"]
            break
    assert isinstance(descriptor, property)



def test_afptext_endimage_is_not_abstract():
    assert not inspect.isabstract(afpText_EndImage)


def test_afptext_endimage_constructor_exists():
    assert callable(afpText_EndImage.__init__)


def test_afptext_endimage_constructor_args():
    sig = inspect.signature(afpText_EndImage.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gscs_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCS)


def test_afptext_gscs_constructor_exists():
    assert callable(afpText_GSCS.__init__)


def test_afptext_gscs_constructor_args():
    sig = inspect.signature(afpText_GSCS.__init__)
    params = list(sig.parameters.keys())
    assert "LCID" in params, "Missing parameter 'LCID'"

def test_afptext_gscs_has_LCID():
    assert hasattr(afpText_GSCS, "LCID")
    descriptor = None
    for klass in afpText_GSCS.__mro__:
        if "LCID" in klass.__dict__:
            descriptor = klass.__dict__["LCID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gscp_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCP)


def test_afptext_gscp_constructor_exists():
    assert callable(afpText_GSCP.__init__)


def test_afptext_gscp_constructor_args():
    sig = inspect.signature(afpText_GSCP.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gscp_has_YPOS():
    assert hasattr(afpText_GSCP, "YPOS")
    descriptor = None
    for klass in afpText_GSCP.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gscp_has_XPOS():
    assert hasattr(afpText_GSCP, "XPOS")
    descriptor = None
    for klass in afpText_GSCP.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcbez_is_not_abstract():
    assert not inspect.isabstract(afpText_GCBEZ)


def test_afptext_gcbez_constructor_exists():
    assert callable(afpText_GCBEZ.__init__)


def test_afptext_gcbez_constructor_args():
    sig = inspect.signature(afpText_GCBEZ.__init__)
    params = list(sig.parameters.keys())



def test_afptext_linedataobjectpositionmigration_is_not_abstract():
    assert not inspect.isabstract(afpText_LineDataObjectPositionMigration)


def test_afptext_linedataobjectpositionmigration_constructor_exists():
    assert callable(afpText_LineDataObjectPositionMigration.__init__)


def test_afptext_linedataobjectpositionmigration_constructor_args():
    sig = inspect.signature(afpText_LineDataObjectPositionMigration.__init__)
    params = list(sig.parameters.keys())
    assert "TempOrient" in params, "Missing parameter 'TempOrient'"

def test_afptext_linedataobjectpositionmigration_has_TempOrient():
    assert hasattr(afpText_LineDataObjectPositionMigration, "TempOrient")
    descriptor = None
    for klass in afpText_LineDataObjectPositionMigration.__mro__:
        if "TempOrient" in klass.__dict__:
            descriptor = klass.__dict__["TempOrient"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fontdescriptorspecification_is_not_abstract():
    assert not inspect.isabstract(afpText_FontDescriptorSpecification)


def test_afptext_fontdescriptorspecification_constructor_exists():
    assert callable(afpText_FontDescriptorSpecification.__init__)


def test_afptext_fontdescriptorspecification_constructor_args():
    sig = inspect.signature(afpText_FontDescriptorSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "FtHeight" in params, "Missing parameter 'FtHeight'"
    assert "FtUsFlags" in params, "Missing parameter 'FtUsFlags'"
    assert "FtDsFlags" in params, "Missing parameter 'FtDsFlags'"
    assert "FtWtClass" in params, "Missing parameter 'FtWtClass'"
    assert "FtWidth" in params, "Missing parameter 'FtWidth'"
    assert "FtWdClass" in params, "Missing parameter 'FtWdClass'"

def test_afptext_fontdescriptorspecification_has_FtHeight():
    assert hasattr(afpText_FontDescriptorSpecification, "FtHeight")
    descriptor = None
    for klass in afpText_FontDescriptorSpecification.__mro__:
        if "FtHeight" in klass.__dict__:
            descriptor = klass.__dict__["FtHeight"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontdescriptorspecification_has_FtUsFlags():
    assert hasattr(afpText_FontDescriptorSpecification, "FtUsFlags")
    descriptor = None
    for klass in afpText_FontDescriptorSpecification.__mro__:
        if "FtUsFlags" in klass.__dict__:
            descriptor = klass.__dict__["FtUsFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontdescriptorspecification_has_FtDsFlags():
    assert hasattr(afpText_FontDescriptorSpecification, "FtDsFlags")
    descriptor = None
    for klass in afpText_FontDescriptorSpecification.__mro__:
        if "FtDsFlags" in klass.__dict__:
            descriptor = klass.__dict__["FtDsFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontdescriptorspecification_has_FtWtClass():
    assert hasattr(afpText_FontDescriptorSpecification, "FtWtClass")
    descriptor = None
    for klass in afpText_FontDescriptorSpecification.__mro__:
        if "FtWtClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWtClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontdescriptorspecification_has_FtWidth():
    assert hasattr(afpText_FontDescriptorSpecification, "FtWidth")
    descriptor = None
    for klass in afpText_FontDescriptorSpecification.__mro__:
        if "FtWidth" in klass.__dict__:
            descriptor = klass.__dict__["FtWidth"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontdescriptorspecification_has_FtWdClass():
    assert hasattr(afpText_FontDescriptorSpecification, "FtWdClass")
    descriptor = None
    for klass in afpText_FontDescriptorSpecification.__mro__:
        if "FtWdClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWdClass"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectoriginidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectOriginIdentifier)


def test_afptext_objectoriginidentifier_constructor_exists():
    assert callable(afpText_ObjectOriginIdentifier.__init__)


def test_afptext_objectoriginidentifier_constructor_args():
    sig = inspect.signature(afpText_ObjectOriginIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "SysID" in params, "Missing parameter 'SysID'"
    assert "System" in params, "Missing parameter 'System'"
    assert "MedID" in params, "Missing parameter 'MedID'"
    assert "DSID" in params, "Missing parameter 'DSID'"

def test_afptext_objectoriginidentifier_has_SysID():
    assert hasattr(afpText_ObjectOriginIdentifier, "SysID")
    descriptor = None
    for klass in afpText_ObjectOriginIdentifier.__mro__:
        if "SysID" in klass.__dict__:
            descriptor = klass.__dict__["SysID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectoriginidentifier_has_System():
    assert hasattr(afpText_ObjectOriginIdentifier, "System")
    descriptor = None
    for klass in afpText_ObjectOriginIdentifier.__mro__:
        if "System" in klass.__dict__:
            descriptor = klass.__dict__["System"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectoriginidentifier_has_MedID():
    assert hasattr(afpText_ObjectOriginIdentifier, "MedID")
    descriptor = None
    for klass in afpText_ObjectOriginIdentifier.__mro__:
        if "MedID" in klass.__dict__:
            descriptor = klass.__dict__["MedID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectoriginidentifier_has_DSID():
    assert hasattr(afpText_ObjectOriginIdentifier, "DSID")
    descriptor = None
    for klass in afpText_ObjectOriginIdentifier.__mro__:
        if "DSID" in klass.__dict__:
            descriptor = klass.__dict__["DSID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gslt_is_not_abstract():
    assert not inspect.isabstract(afpText_GSLT)


def test_afptext_gslt_constructor_exists():
    assert callable(afpText_GSLT.__init__)


def test_afptext_gslt_constructor_args():
    sig = inspect.signature(afpText_GSLT.__init__)
    params = list(sig.parameters.keys())
    assert "LINETYPE" in params, "Missing parameter 'LINETYPE'"

def test_afptext_gslt_has_LINETYPE():
    assert hasattr(afpText_GSLT, "LINETYPE")
    descriptor = None
    for klass in afpText_GSLT.__mro__:
        if "LINETYPE" in klass.__dict__:
            descriptor = klass.__dict__["LINETYPE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mediumorientation_is_not_abstract():
    assert not inspect.isabstract(afpText_MediumOrientation)


def test_afptext_mediumorientation_constructor_exists():
    assert callable(afpText_MediumOrientation.__init__)


def test_afptext_mediumorientation_constructor_args():
    sig = inspect.signature(afpText_MediumOrientation.__init__)
    params = list(sig.parameters.keys())
    assert "MedOrient" in params, "Missing parameter 'MedOrient'"

def test_afptext_mediumorientation_has_MedOrient():
    assert hasattr(afpText_MediumOrientation, "MedOrient")
    descriptor = None
    for klass in afpText_MediumOrientation.__mro__:
        if "MedOrient" in klass.__dict__:
            descriptor = klass.__dict__["MedOrient"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tilesize_is_not_abstract():
    assert not inspect.isabstract(afpText_TileSize)


def test_afptext_tilesize_constructor_exists():
    assert callable(afpText_TileSize.__init__)


def test_afptext_tilesize_constructor_args():
    sig = inspect.signature(afpText_TileSize.__init__)
    params = list(sig.parameters.keys())
    assert "RELRES" in params, "Missing parameter 'RELRES'"
    assert "TVSIZE" in params, "Missing parameter 'TVSIZE'"
    assert "THSIZE" in params, "Missing parameter 'THSIZE'"

def test_afptext_tilesize_has_RELRES():
    assert hasattr(afpText_TileSize, "RELRES")
    descriptor = None
    for klass in afpText_TileSize.__mro__:
        if "RELRES" in klass.__dict__:
            descriptor = klass.__dict__["RELRES"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesize_has_TVSIZE():
    assert hasattr(afpText_TileSize, "TVSIZE")
    descriptor = None
    for klass in afpText_TileSize.__mro__:
        if "TVSIZE" in klass.__dict__:
            descriptor = klass.__dict__["TVSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesize_has_THSIZE():
    assert hasattr(afpText_TileSize, "THSIZE")
    descriptor = None
    for klass in afpText_TileSize.__mro__:
        if "THSIZE" in klass.__dict__:
            descriptor = klass.__dict__["THSIZE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_encodingschemeid_is_not_abstract():
    assert not inspect.isabstract(afpText_EncodingSchemeID)


def test_afptext_encodingschemeid_constructor_exists():
    assert callable(afpText_EncodingSchemeID.__init__)


def test_afptext_encodingschemeid_constructor_args():
    sig = inspect.signature(afpText_EncodingSchemeID.__init__)
    params = list(sig.parameters.keys())
    assert "ESidCP" in params, "Missing parameter 'ESidCP'"
    assert "ESidUD" in params, "Missing parameter 'ESidUD'"

def test_afptext_encodingschemeid_has_ESidCP():
    assert hasattr(afpText_EncodingSchemeID, "ESidCP")
    descriptor = None
    for klass in afpText_EncodingSchemeID.__mro__:
        if "ESidCP" in klass.__dict__:
            descriptor = klass.__dict__["ESidCP"]
            break
    assert isinstance(descriptor, property)

def test_afptext_encodingschemeid_has_ESidUD():
    assert hasattr(afpText_EncodingSchemeID, "ESidUD")
    descriptor = None
    for klass in afpText_EncodingSchemeID.__mro__:
        if "ESidUD" in klass.__dict__:
            descriptor = klass.__dict__["ESidUD"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fontfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText_FontFidelity)


def test_afptext_fontfidelity_constructor_exists():
    assert callable(afpText_FontFidelity.__init__)


def test_afptext_fontfidelity_constructor_args():
    sig = inspect.signature(afpText_FontFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "StpFntEx" in params, "Missing parameter 'StpFntEx'"

def test_afptext_fontfidelity_has_StpFntEx():
    assert hasattr(afpText_FontFidelity, "StpFntEx")
    descriptor = None
    for klass in afpText_FontFidelity.__mro__:
        if "StpFntEx" in klass.__dict__:
            descriptor = klass.__dict__["StpFntEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext_beginimage_is_not_abstract():
    assert not inspect.isabstract(afpText_BeginImage)


def test_afptext_beginimage_constructor_exists():
    assert callable(afpText_BeginImage.__init__)


def test_afptext_beginimage_constructor_args():
    sig = inspect.signature(afpText_BeginImage.__init__)
    params = list(sig.parameters.keys())
    assert "OBJTYPE" in params, "Missing parameter 'OBJTYPE'"

def test_afptext_beginimage_has_OBJTYPE():
    assert hasattr(afpText_BeginImage, "OBJTYPE")
    descriptor = None
    for klass in afpText_BeginImage.__mro__:
        if "OBJTYPE" in klass.__dict__:
            descriptor = klass.__dict__["OBJTYPE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcmrk_is_not_abstract():
    assert not inspect.isabstract(afpText_GCMRK)


def test_afptext_gcmrk_constructor_exists():
    assert callable(afpText_GCMRK.__init__)


def test_afptext_gcmrk_constructor_args():
    sig = inspect.signature(afpText_GCMRK.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gscr_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCR)


def test_afptext_gscr_constructor_exists():
    assert callable(afpText_GSCR.__init__)


def test_afptext_gscr_constructor_args():
    sig = inspect.signature(afpText_GSCR.__init__)
    params = list(sig.parameters.keys())
    assert "PREC" in params, "Missing parameter 'PREC'"

def test_afptext_gscr_has_PREC():
    assert hasattr(afpText_GSCR, "PREC")
    descriptor = None
    for klass in afpText_GSCR.__mro__:
        if "PREC" in klass.__dict__:
            descriptor = klass.__dict__["PREC"]
            break
    assert isinstance(descriptor, property)



def test_afptext_imagesize_is_not_abstract():
    assert not inspect.isabstract(afpText_ImageSize)


def test_afptext_imagesize_constructor_exists():
    assert callable(afpText_ImageSize.__init__)


def test_afptext_imagesize_constructor_args():
    sig = inspect.signature(afpText_ImageSize.__init__)
    params = list(sig.parameters.keys())
    assert "VSIZE" in params, "Missing parameter 'VSIZE'"
    assert "HRESOL" in params, "Missing parameter 'HRESOL'"
    assert "VRESOL" in params, "Missing parameter 'VRESOL'"
    assert "HSIZE" in params, "Missing parameter 'HSIZE'"
    assert "UNITBASE" in params, "Missing parameter 'UNITBASE'"

def test_afptext_imagesize_has_VSIZE():
    assert hasattr(afpText_ImageSize, "VSIZE")
    descriptor = None
    for klass in afpText_ImageSize.__mro__:
        if "VSIZE" in klass.__dict__:
            descriptor = klass.__dict__["VSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imagesize_has_HRESOL():
    assert hasattr(afpText_ImageSize, "HRESOL")
    descriptor = None
    for klass in afpText_ImageSize.__mro__:
        if "HRESOL" in klass.__dict__:
            descriptor = klass.__dict__["HRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imagesize_has_VRESOL():
    assert hasattr(afpText_ImageSize, "VRESOL")
    descriptor = None
    for klass in afpText_ImageSize.__mro__:
        if "VRESOL" in klass.__dict__:
            descriptor = klass.__dict__["VRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imagesize_has_HSIZE():
    assert hasattr(afpText_ImageSize, "HSIZE")
    descriptor = None
    for klass in afpText_ImageSize.__mro__:
        if "HSIZE" in klass.__dict__:
            descriptor = klass.__dict__["HSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imagesize_has_UNITBASE():
    assert hasattr(afpText_ImageSize, "UNITBASE")
    descriptor = None
    for klass in afpText_ImageSize.__mro__:
        if "UNITBASE" in klass.__dict__:
            descriptor = klass.__dict__["UNITBASE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pagepositioninformation_is_not_abstract():
    assert not inspect.isabstract(afpText_PagePositionInformation)


def test_afptext_pagepositioninformation_constructor_exists():
    assert callable(afpText_PagePositionInformation.__init__)


def test_afptext_pagepositioninformation_constructor_args():
    sig = inspect.signature(afpText_PagePositionInformation.__init__)
    params = list(sig.parameters.keys())
    assert "PGPRG" in params, "Missing parameter 'PGPRG'"

def test_afptext_pagepositioninformation_has_PGPRG():
    assert hasattr(afpText_PagePositionInformation, "PGPRG")
    descriptor = None
    for klass in afpText_PagePositionInformation.__mro__:
        if "PGPRG" in klass.__dict__:
            descriptor = klass.__dict__["PGPRG"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gflt_is_not_abstract():
    assert not inspect.isabstract(afpText_GFLT)


def test_afptext_gflt_constructor_exists():
    assert callable(afpText_GFLT.__init__)


def test_afptext_gflt_constructor_args():
    sig = inspect.signature(afpText_GFLT.__init__)
    params = list(sig.parameters.keys())



def test_afptext_imagedata_is_not_abstract():
    assert not inspect.isabstract(afpText_ImageData)


def test_afptext_imagedata_constructor_exists():
    assert callable(afpText_ImageData.__init__)


def test_afptext_imagedata_constructor_args():
    sig = inspect.signature(afpText_ImageData.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext_imagedata_has_DATA():
    assert hasattr(afpText_ImageData, "DATA")
    descriptor = None
    for klass in afpText_ImageData.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_attributevalue_is_not_abstract():
    assert not inspect.isabstract(afpText_AttributeValue)


def test_afptext_attributevalue_constructor_exists():
    assert callable(afpText_AttributeValue.__init__)


def test_afptext_attributevalue_constructor_args():
    sig = inspect.signature(afpText_AttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "AttVal" in params, "Missing parameter 'AttVal'"
    assert "Reserved0" in params, "Missing parameter 'Reserved0'"

def test_afptext_attributevalue_has_AttVal():
    assert hasattr(afpText_AttributeValue, "AttVal")
    descriptor = None
    for klass in afpText_AttributeValue.__mro__:
        if "AttVal" in klass.__dict__:
            descriptor = klass.__dict__["AttVal"]
            break
    assert isinstance(descriptor, property)

def test_afptext_attributevalue_has_Reserved0():
    assert hasattr(afpText_AttributeValue, "Reserved0")
    descriptor = None
    for klass in afpText_AttributeValue.__mro__:
        if "Reserved0" in klass.__dict__:
            descriptor = klass.__dict__["Reserved0"]
            break
    assert isinstance(descriptor, property)



def test_afptext_endtransparencymask_is_not_abstract():
    assert not inspect.isabstract(afpText_EndTransparencyMask)


def test_afptext_endtransparencymask_constructor_exists():
    assert callable(afpText_EndTransparencyMask.__init__)


def test_afptext_endtransparencymask_constructor_args():
    sig = inspect.signature(afpText_EndTransparencyMask.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gspcol_is_not_abstract():
    assert not inspect.isabstract(afpText_GSPCOL)


def test_afptext_gspcol_constructor_exists():
    assert callable(afpText_GSPCOL.__init__)


def test_afptext_gspcol_constructor_args():
    sig = inspect.signature(afpText_GSPCOL.__init__)
    params = list(sig.parameters.keys())
    assert "COLSIZE2" in params, "Missing parameter 'COLSIZE2'"
    assert "COLSIZE3" in params, "Missing parameter 'COLSIZE3'"
    assert "COLVALUE" in params, "Missing parameter 'COLVALUE'"
    assert "RES2" in params, "Missing parameter 'RES2'"
    assert "COLSIZE1" in params, "Missing parameter 'COLSIZE1'"
    assert "COLSPCE" in params, "Missing parameter 'COLSPCE'"
    assert "RES1" in params, "Missing parameter 'RES1'"
    assert "COLSIZE4" in params, "Missing parameter 'COLSIZE4'"

def test_afptext_gspcol_has_COLSIZE2():
    assert hasattr(afpText_GSPCOL, "COLSIZE2")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "COLSIZE2" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_COLSIZE3():
    assert hasattr(afpText_GSPCOL, "COLSIZE3")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "COLSIZE3" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_COLVALUE():
    assert hasattr(afpText_GSPCOL, "COLVALUE")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "COLVALUE" in klass.__dict__:
            descriptor = klass.__dict__["COLVALUE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_RES2():
    assert hasattr(afpText_GSPCOL, "RES2")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "RES2" in klass.__dict__:
            descriptor = klass.__dict__["RES2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_COLSIZE1():
    assert hasattr(afpText_GSPCOL, "COLSIZE1")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "COLSIZE1" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_COLSPCE():
    assert hasattr(afpText_GSPCOL, "COLSPCE")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "COLSPCE" in klass.__dict__:
            descriptor = klass.__dict__["COLSPCE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_RES1():
    assert hasattr(afpText_GSPCOL, "RES1")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "RES1" in klass.__dict__:
            descriptor = klass.__dict__["RES1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gspcol_has_COLSIZE4():
    assert hasattr(afpText_GSPCOL, "COLSIZE4")
    descriptor = None
    for klass in afpText_GSPCOL.__mro__:
        if "COLSIZE4" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE4"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tbm_is_not_abstract():
    assert not inspect.isabstract(afpText_TBM)


def test_afptext_tbm_constructor_exists():
    assert callable(afpText_TBM.__init__)


def test_afptext_tbm_constructor_args():
    sig = inspect.signature(afpText_TBM.__init__)
    params = list(sig.parameters.keys())
    assert "PRECSION" in params, "Missing parameter 'PRECSION'"
    assert "DIRCTION" in params, "Missing parameter 'DIRCTION'"
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext_tbm_has_PRECSION():
    assert hasattr(afpText_TBM, "PRECSION")
    descriptor = None
    for klass in afpText_TBM.__mro__:
        if "PRECSION" in klass.__dict__:
            descriptor = klass.__dict__["PRECSION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tbm_has_DIRCTION():
    assert hasattr(afpText_TBM, "DIRCTION")
    descriptor = None
    for klass in afpText_TBM.__mro__:
        if "DIRCTION" in klass.__dict__:
            descriptor = klass.__dict__["DIRCTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tbm_has_INCRMENT():
    assert hasattr(afpText_TBM, "INCRMENT")
    descriptor = None
    for klass in afpText_TBM.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsgch_is_not_abstract():
    assert not inspect.isabstract(afpText_GSGCH)


def test_afptext_gsgch_constructor_exists():
    assert callable(afpText_GSGCH.__init__)


def test_afptext_gsgch_constructor_args():
    sig = inspect.signature(afpText_GSGCH.__init__)
    params = list(sig.parameters.keys())



def test_afptext_externalalgorithm_is_not_abstract():
    assert not inspect.isabstract(afpText_ExternalAlgorithm)


def test_afptext_externalalgorithm_constructor_exists():
    assert callable(afpText_ExternalAlgorithm.__init__)


def test_afptext_externalalgorithm_constructor_args():
    sig = inspect.signature(afpText_ExternalAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "ALGTYPE" in params, "Missing parameter 'ALGTYPE'"

def test_afptext_externalalgorithm_has_ALGTYPE():
    assert hasattr(afpText_ExternalAlgorithm, "ALGTYPE")
    descriptor = None
    for klass in afpText_ExternalAlgorithm.__mro__:
        if "ALGTYPE" in klass.__dict__:
            descriptor = klass.__dict__["ALGTYPE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectoffset_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectOffset)


def test_afptext_objectoffset_constructor_exists():
    assert callable(afpText_ObjectOffset.__init__)


def test_afptext_objectoffset_constructor_args():
    sig = inspect.signature(afpText_ObjectOffset.__init__)
    params = list(sig.parameters.keys())
    assert "ObjOset" in params, "Missing parameter 'ObjOset'"
    assert "ObjTpe" in params, "Missing parameter 'ObjTpe'"
    assert "ObjOstHi" in params, "Missing parameter 'ObjOstHi'"

def test_afptext_objectoffset_has_ObjOset():
    assert hasattr(afpText_ObjectOffset, "ObjOset")
    descriptor = None
    for klass in afpText_ObjectOffset.__mro__:
        if "ObjOset" in klass.__dict__:
            descriptor = klass.__dict__["ObjOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectoffset_has_ObjTpe():
    assert hasattr(afpText_ObjectOffset, "ObjTpe")
    descriptor = None
    for klass in afpText_ObjectOffset.__mro__:
        if "ObjTpe" in klass.__dict__:
            descriptor = klass.__dict__["ObjTpe"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectoffset_has_ObjOstHi():
    assert hasattr(afpText_ObjectOffset, "ObjOstHi")
    descriptor = None
    for klass in afpText_ObjectOffset.__mro__:
        if "ObjOstHi" in klass.__dict__:
            descriptor = klass.__dict__["ObjOstHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcparc_is_not_abstract():
    assert not inspect.isabstract(afpText_GCPARC)


def test_afptext_gcparc_constructor_exists():
    assert callable(afpText_GCPARC.__init__)


def test_afptext_gcparc_constructor_args():
    sig = inspect.signature(afpText_GCPARC.__init__)
    params = list(sig.parameters.keys())
    assert "MH" in params, "Missing parameter 'MH'"
    assert "YCENT" in params, "Missing parameter 'YCENT'"
    assert "SWEEP" in params, "Missing parameter 'SWEEP'"
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "START" in params, "Missing parameter 'START'"
    assert "XCENT" in params, "Missing parameter 'XCENT'"

def test_afptext_gcparc_has_MH():
    assert hasattr(afpText_GCPARC, "MH")
    descriptor = None
    for klass in afpText_GCPARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcparc_has_YCENT():
    assert hasattr(afpText_GCPARC, "YCENT")
    descriptor = None
    for klass in afpText_GCPARC.__mro__:
        if "YCENT" in klass.__dict__:
            descriptor = klass.__dict__["YCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcparc_has_SWEEP():
    assert hasattr(afpText_GCPARC, "SWEEP")
    descriptor = None
    for klass in afpText_GCPARC.__mro__:
        if "SWEEP" in klass.__dict__:
            descriptor = klass.__dict__["SWEEP"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcparc_has_MFR():
    assert hasattr(afpText_GCPARC, "MFR")
    descriptor = None
    for klass in afpText_GCPARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcparc_has_START():
    assert hasattr(afpText_GCPARC, "START")
    descriptor = None
    for klass in afpText_GCPARC.__mro__:
        if "START" in klass.__dict__:
            descriptor = klass.__dict__["START"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcparc_has_XCENT():
    assert hasattr(afpText_GCPARC, "XCENT")
    descriptor = None
    for klass in afpText_GCPARC.__mro__:
        if "XCENT" in klass.__dict__:
            descriptor = klass.__dict__["XCENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mappingoption_is_not_abstract():
    assert not inspect.isabstract(afpText_MappingOption)


def test_afptext_mappingoption_constructor_exists():
    assert callable(afpText_MappingOption.__init__)


def test_afptext_mappingoption_constructor_args():
    sig = inspect.signature(afpText_MappingOption.__init__)
    params = list(sig.parameters.keys())
    assert "MapValue" in params, "Missing parameter 'MapValue'"

def test_afptext_mappingoption_has_MapValue():
    assert hasattr(afpText_MappingOption, "MapValue")
    descriptor = None
    for klass in afpText_MappingOption.__mro__:
        if "MapValue" in klass.__dict__:
            descriptor = klass.__dict__["MapValue"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectcount_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectCount)


def test_afptext_objectcount_constructor_exists():
    assert callable(afpText_ObjectCount.__init__)


def test_afptext_objectcount_constructor_args():
    sig = inspect.signature(afpText_ObjectCount.__init__)
    params = list(sig.parameters.keys())
    assert "SobjNmHi" in params, "Missing parameter 'SobjNmHi'"
    assert "SObjNum" in params, "Missing parameter 'SObjNum'"
    assert "SubObj" in params, "Missing parameter 'SubObj'"

def test_afptext_objectcount_has_SobjNmHi():
    assert hasattr(afpText_ObjectCount, "SobjNmHi")
    descriptor = None
    for klass in afpText_ObjectCount.__mro__:
        if "SobjNmHi" in klass.__dict__:
            descriptor = klass.__dict__["SobjNmHi"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectcount_has_SObjNum():
    assert hasattr(afpText_ObjectCount, "SObjNum")
    descriptor = None
    for klass in afpText_ObjectCount.__mro__:
        if "SObjNum" in klass.__dict__:
            descriptor = klass.__dict__["SObjNum"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectcount_has_SubObj():
    assert hasattr(afpText_ObjectCount, "SubObj")
    descriptor = None
    for klass in afpText_ObjectCount.__mro__:
        if "SubObj" in klass.__dict__:
            descriptor = klass.__dict__["SubObj"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tonersaver_is_not_abstract():
    assert not inspect.isabstract(afpText_TonerSaver)


def test_afptext_tonersaver_constructor_exists():
    assert callable(afpText_TonerSaver.__init__)


def test_afptext_tonersaver_constructor_args():
    sig = inspect.signature(afpText_TonerSaver.__init__)
    params = list(sig.parameters.keys())
    assert "TSvCtrl" in params, "Missing parameter 'TSvCtrl'"

def test_afptext_tonersaver_has_TSvCtrl():
    assert hasattr(afpText_TonerSaver, "TSvCtrl")
    descriptor = None
    for klass in afpText_TonerSaver.__mro__:
        if "TSvCtrl" in klass.__dict__:
            descriptor = klass.__dict__["TSvCtrl"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gspt_is_not_abstract():
    assert not inspect.isabstract(afpText_GSPT)


def test_afptext_gspt_constructor_exists():
    assert callable(afpText_GSPT.__init__)


def test_afptext_gspt_constructor_args():
    sig = inspect.signature(afpText_GSPT.__init__)
    params = list(sig.parameters.keys())
    assert "PATT" in params, "Missing parameter 'PATT'"

def test_afptext_gspt_has_PATT():
    assert hasattr(afpText_GSPT, "PATT")
    descriptor = None
    for klass in afpText_GSPT.__mro__:
        if "PATT" in klass.__dict__:
            descriptor = klass.__dict__["PATT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gscd_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCD)


def test_afptext_gscd_constructor_exists():
    assert callable(afpText_GSCD.__init__)


def test_afptext_gscd_constructor_args():
    sig = inspect.signature(afpText_GSCD.__init__)
    params = list(sig.parameters.keys())
    assert "DIRECTION" in params, "Missing parameter 'DIRECTION'"

def test_afptext_gscd_has_DIRECTION():
    assert hasattr(afpText_GSCD, "DIRECTION")
    descriptor = None
    for klass in afpText_GSCD.__mro__:
        if "DIRECTION" in klass.__dict__:
            descriptor = klass.__dict__["DIRECTION"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bandimage_is_not_abstract():
    assert not inspect.isabstract(afpText_BandImage)


def test_afptext_bandimage_constructor_exists():
    assert callable(afpText_BandImage.__init__)


def test_afptext_bandimage_constructor_args():
    sig = inspect.signature(afpText_BandImage.__init__)
    params = list(sig.parameters.keys())
    assert "BCOUNT" in params, "Missing parameter 'BCOUNT'"

def test_afptext_bandimage_has_BCOUNT():
    assert hasattr(afpText_BandImage, "BCOUNT")
    descriptor = None
    for klass in afpText_BandImage.__mro__:
        if "BCOUNT" in klass.__dict__:
            descriptor = klass.__dict__["BCOUNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_renderingintent_is_not_abstract():
    assert not inspect.isabstract(afpText_RenderingIntent)


def test_afptext_renderingintent_constructor_exists():
    assert callable(afpText_RenderingIntent.__init__)


def test_afptext_renderingintent_constructor_args():
    sig = inspect.signature(afpText_RenderingIntent.__init__)
    params = list(sig.parameters.keys())
    assert "IOCARI" in params, "Missing parameter 'IOCARI'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "OCRI" in params, "Missing parameter 'OCRI'"
    assert "GOCARI" in params, "Missing parameter 'GOCARI'"
    assert "PTOCRI" in params, "Missing parameter 'PTOCRI'"

def test_afptext_renderingintent_has_IOCARI():
    assert hasattr(afpText_RenderingIntent, "IOCARI")
    descriptor = None
    for klass in afpText_RenderingIntent.__mro__:
        if "IOCARI" in klass.__dict__:
            descriptor = klass.__dict__["IOCARI"]
            break
    assert isinstance(descriptor, property)

def test_afptext_renderingintent_has_Reserved():
    assert hasattr(afpText_RenderingIntent, "Reserved")
    descriptor = None
    for klass in afpText_RenderingIntent.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_renderingintent_has_Reserved2():
    assert hasattr(afpText_RenderingIntent, "Reserved2")
    descriptor = None
    for klass in afpText_RenderingIntent.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_renderingintent_has_OCRI():
    assert hasattr(afpText_RenderingIntent, "OCRI")
    descriptor = None
    for klass in afpText_RenderingIntent.__mro__:
        if "OCRI" in klass.__dict__:
            descriptor = klass.__dict__["OCRI"]
            break
    assert isinstance(descriptor, property)

def test_afptext_renderingintent_has_GOCARI():
    assert hasattr(afpText_RenderingIntent, "GOCARI")
    descriptor = None
    for klass in afpText_RenderingIntent.__mro__:
        if "GOCARI" in klass.__dict__:
            descriptor = klass.__dict__["GOCARI"]
            break
    assert isinstance(descriptor, property)

def test_afptext_renderingintent_has_PTOCRI():
    assert hasattr(afpText_RenderingIntent, "PTOCRI")
    descriptor = None
    for klass in afpText_RenderingIntent.__mro__:
        if "PTOCRI" in klass.__dict__:
            descriptor = klass.__dict__["PTOCRI"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsbmx_is_not_abstract():
    assert not inspect.isabstract(afpText_GSBMX)


def test_afptext_gsbmx_constructor_exists():
    assert callable(afpText_GSBMX.__init__)


def test_afptext_gsbmx_constructor_args():
    sig = inspect.signature(afpText_GSBMX.__init__)
    params = list(sig.parameters.keys())
    assert "MODE" in params, "Missing parameter 'MODE'"

def test_afptext_gsbmx_has_MODE():
    assert hasattr(afpText_GSBMX, "MODE")
    descriptor = None
    for klass in afpText_GSBMX.__mro__:
        if "MODE" in klass.__dict__:
            descriptor = klass.__dict__["MODE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_imageencoding_is_not_abstract():
    assert not inspect.isabstract(afpText_ImageEncoding)


def test_afptext_imageencoding_constructor_exists():
    assert callable(afpText_ImageEncoding.__init__)


def test_afptext_imageencoding_constructor_args():
    sig = inspect.signature(afpText_ImageEncoding.__init__)
    params = list(sig.parameters.keys())
    assert "RECID" in params, "Missing parameter 'RECID'"
    assert "COMPRID" in params, "Missing parameter 'COMPRID'"
    assert "BITORDR" in params, "Missing parameter 'BITORDR'"

def test_afptext_imageencoding_has_RECID():
    assert hasattr(afpText_ImageEncoding, "RECID")
    descriptor = None
    for klass in afpText_ImageEncoding.__mro__:
        if "RECID" in klass.__dict__:
            descriptor = klass.__dict__["RECID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imageencoding_has_COMPRID():
    assert hasattr(afpText_ImageEncoding, "COMPRID")
    descriptor = None
    for klass in afpText_ImageEncoding.__mro__:
        if "COMPRID" in klass.__dict__:
            descriptor = klass.__dict__["COMPRID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imageencoding_has_BITORDR():
    assert hasattr(afpText_ImageEncoding, "BITORDR")
    descriptor = None
    for klass in afpText_ImageEncoding.__mro__:
        if "BITORDR" in klass.__dict__:
            descriptor = klass.__dict__["BITORDR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_imageresolution_is_not_abstract():
    assert not inspect.isabstract(afpText_ImageResolution)


def test_afptext_imageresolution_constructor_exists():
    assert callable(afpText_ImageResolution.__init__)


def test_afptext_imageresolution_constructor_args():
    sig = inspect.signature(afpText_ImageResolution.__init__)
    params = list(sig.parameters.keys())
    assert "YBase" in params, "Missing parameter 'YBase'"
    assert "XResol" in params, "Missing parameter 'XResol'"
    assert "YResol" in params, "Missing parameter 'YResol'"
    assert "XBase" in params, "Missing parameter 'XBase'"

def test_afptext_imageresolution_has_YBase():
    assert hasattr(afpText_ImageResolution, "YBase")
    descriptor = None
    for klass in afpText_ImageResolution.__mro__:
        if "YBase" in klass.__dict__:
            descriptor = klass.__dict__["YBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imageresolution_has_XResol():
    assert hasattr(afpText_ImageResolution, "XResol")
    descriptor = None
    for klass in afpText_ImageResolution.__mro__:
        if "XResol" in klass.__dict__:
            descriptor = klass.__dict__["XResol"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imageresolution_has_YResol():
    assert hasattr(afpText_ImageResolution, "YResol")
    descriptor = None
    for klass in afpText_ImageResolution.__mro__:
        if "YResol" in klass.__dict__:
            descriptor = klass.__dict__["YResol"]
            break
    assert isinstance(descriptor, property)

def test_afptext_imageresolution_has_XBase():
    assert hasattr(afpText_ImageResolution, "XBase")
    descriptor = None
    for klass in afpText_ImageResolution.__mro__:
        if "XBase" in klass.__dict__:
            descriptor = klass.__dict__["XBase"]
            break
    assert isinstance(descriptor, property)



def test_afptext_characterrotation_is_not_abstract():
    assert not inspect.isabstract(afpText_CharacterRotation)


def test_afptext_characterrotation_constructor_exists():
    assert callable(afpText_CharacterRotation.__init__)


def test_afptext_characterrotation_constructor_args():
    sig = inspect.signature(afpText_CharacterRotation.__init__)
    params = list(sig.parameters.keys())
    assert "CharRot" in params, "Missing parameter 'CharRot'"

def test_afptext_characterrotation_has_CharRot():
    assert hasattr(afpText_CharacterRotation, "CharRot")
    descriptor = None
    for klass in afpText_CharacterRotation.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcflt_is_not_abstract():
    assert not inspect.isabstract(afpText_GCFLT)


def test_afptext_gcflt_constructor_exists():
    assert callable(afpText_GCFLT.__init__)


def test_afptext_gcflt_constructor_args():
    sig = inspect.signature(afpText_GCFLT.__init__)
    params = list(sig.parameters.keys())



def test_afptext_objectstructuredfieldextent_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectStructuredFieldExtent)


def test_afptext_objectstructuredfieldextent_constructor_exists():
    assert callable(afpText_ObjectStructuredFieldExtent.__init__)


def test_afptext_objectstructuredfieldextent_constructor_args():
    sig = inspect.signature(afpText_ObjectStructuredFieldExtent.__init__)
    params = list(sig.parameters.keys())
    assert "SFExt" in params, "Missing parameter 'SFExt'"
    assert "SFExtHi" in params, "Missing parameter 'SFExtHi'"

def test_afptext_objectstructuredfieldextent_has_SFExt():
    assert hasattr(afpText_ObjectStructuredFieldExtent, "SFExt")
    descriptor = None
    for klass in afpText_ObjectStructuredFieldExtent.__mro__:
        if "SFExt" in klass.__dict__:
            descriptor = klass.__dict__["SFExt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectstructuredfieldextent_has_SFExtHi():
    assert hasattr(afpText_ObjectStructuredFieldExtent, "SFExtHi")
    descriptor = None
    for klass in afpText_ObjectStructuredFieldExtent.__mro__:
        if "SFExtHi" in klass.__dict__:
            descriptor = klass.__dict__["SFExtHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsms_is_not_abstract():
    assert not inspect.isabstract(afpText_GSMS)


def test_afptext_gsms_constructor_exists():
    assert callable(afpText_GSMS.__init__)


def test_afptext_gsms_constructor_args():
    sig = inspect.signature(afpText_GSMS.__init__)
    params = list(sig.parameters.keys())
    assert "LCID" in params, "Missing parameter 'LCID'"

def test_afptext_gsms_has_LCID():
    assert hasattr(afpText_GSMS, "LCID")
    descriptor = None
    for klass in afpText_GSMS.__mro__:
        if "LCID" in klass.__dict__:
            descriptor = klass.__dict__["LCID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectcontainerpresentationspacesize_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectContainerPresentationSpaceSize)


def test_afptext_objectcontainerpresentationspacesize_constructor_exists():
    assert callable(afpText_ObjectContainerPresentationSpaceSize.__init__)


def test_afptext_objectcontainerpresentationspacesize_constructor_args():
    sig = inspect.signature(afpText_ObjectContainerPresentationSpaceSize.__init__)
    params = list(sig.parameters.keys())
    assert "PDFSize" in params, "Missing parameter 'PDFSize'"

def test_afptext_objectcontainerpresentationspacesize_has_PDFSize():
    assert hasattr(afpText_ObjectContainerPresentationSpaceSize, "PDFSize")
    descriptor = None
    for klass in afpText_ObjectContainerPresentationSpaceSize.__mro__:
        if "PDFSize" in klass.__dict__:
            descriptor = klass.__dict__["PDFSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext_imagesubsampling_is_not_abstract():
    assert not inspect.isabstract(afpText_ImageSubsampling)


def test_afptext_imagesubsampling_constructor_exists():
    assert callable(afpText_ImageSubsampling.__init__)


def test_afptext_imagesubsampling_constructor_args():
    sig = inspect.signature(afpText_ImageSubsampling.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gparc_is_not_abstract():
    assert not inspect.isabstract(afpText_GPARC)


def test_afptext_gparc_constructor_exists():
    assert callable(afpText_GPARC.__init__)


def test_afptext_gparc_constructor_args():
    sig = inspect.signature(afpText_GPARC.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XCENT" in params, "Missing parameter 'XCENT'"
    assert "SWEEP" in params, "Missing parameter 'SWEEP'"
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "YCENT" in params, "Missing parameter 'YCENT'"
    assert "MH" in params, "Missing parameter 'MH'"
    assert "START" in params, "Missing parameter 'START'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gparc_has_YPOS():
    assert hasattr(afpText_GPARC, "YPOS")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_XCENT():
    assert hasattr(afpText_GPARC, "XCENT")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "XCENT" in klass.__dict__:
            descriptor = klass.__dict__["XCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_SWEEP():
    assert hasattr(afpText_GPARC, "SWEEP")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "SWEEP" in klass.__dict__:
            descriptor = klass.__dict__["SWEEP"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_MFR():
    assert hasattr(afpText_GPARC, "MFR")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_YCENT():
    assert hasattr(afpText_GPARC, "YCENT")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "YCENT" in klass.__dict__:
            descriptor = klass.__dict__["YCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_MH():
    assert hasattr(afpText_GPARC, "MH")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_START():
    assert hasattr(afpText_GPARC, "START")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "START" in klass.__dict__:
            descriptor = klass.__dict__["START"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gparc_has_XPOS():
    assert hasattr(afpText_GPARC, "XPOS")
    descriptor = None
    for klass in afpText_GPARC.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cgcsgid_is_not_abstract():
    assert not inspect.isabstract(afpText_CGCSGID)


def test_afptext_cgcsgid_constructor_exists():
    assert callable(afpText_CGCSGID.__init__)


def test_afptext_cgcsgid_constructor_args():
    sig = inspect.signature(afpText_CGCSGID.__init__)
    params = list(sig.parameters.keys())
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"
    assert "CPGID" in params, "Missing parameter 'CPGID'"

def test_afptext_cgcsgid_has_GCSGID():
    assert hasattr(afpText_CGCSGID, "GCSGID")
    descriptor = None
    for klass in afpText_CGCSGID.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cgcsgid_has_CPGID():
    assert hasattr(afpText_CGCSGID, "CPGID")
    descriptor = None
    for klass in afpText_CGCSGID.__mro__:
        if "CPGID" in klass.__dict__:
            descriptor = klass.__dict__["CPGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_colormanagementresourcedescriptor_is_not_abstract():
    assert not inspect.isabstract(afpText_ColorManagementResourceDescriptor)


def test_afptext_colormanagementresourcedescriptor_constructor_exists():
    assert callable(afpText_ColorManagementResourceDescriptor.__init__)


def test_afptext_colormanagementresourcedescriptor_constructor_args():
    sig = inspect.signature(afpText_ColorManagementResourceDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "CMRScpe" in params, "Missing parameter 'CMRScpe'"
    assert "ProcMode" in params, "Missing parameter 'ProcMode'"

def test_afptext_colormanagementresourcedescriptor_has_CMRScpe():
    assert hasattr(afpText_ColorManagementResourceDescriptor, "CMRScpe")
    descriptor = None
    for klass in afpText_ColorManagementResourceDescriptor.__mro__:
        if "CMRScpe" in klass.__dict__:
            descriptor = klass.__dict__["CMRScpe"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colormanagementresourcedescriptor_has_ProcMode():
    assert hasattr(afpText_ColorManagementResourceDescriptor, "ProcMode")
    descriptor = None
    for klass in afpText_ColorManagementResourceDescriptor.__mro__:
        if "ProcMode" in klass.__dict__:
            descriptor = klass.__dict__["ProcMode"]
            break
    assert isinstance(descriptor, property)



def test_afptext_modcainterchangeset_is_not_abstract():
    assert not inspect.isabstract(afpText_MODCAInterchangeSet)


def test_afptext_modcainterchangeset_constructor_exists():
    assert callable(afpText_MODCAInterchangeSet.__init__)


def test_afptext_modcainterchangeset_constructor_args():
    sig = inspect.signature(afpText_MODCAInterchangeSet.__init__)
    params = list(sig.parameters.keys())
    assert "IStype" in params, "Missing parameter 'IStype'"
    assert "ISid" in params, "Missing parameter 'ISid'"

def test_afptext_modcainterchangeset_has_IStype():
    assert hasattr(afpText_MODCAInterchangeSet, "IStype")
    descriptor = None
    for klass in afpText_MODCAInterchangeSet.__mro__:
        if "IStype" in klass.__dict__:
            descriptor = klass.__dict__["IStype"]
            break
    assert isinstance(descriptor, property)

def test_afptext_modcainterchangeset_has_ISid():
    assert hasattr(afpText_MODCAInterchangeSet, "ISid")
    descriptor = None
    for klass in afpText_MODCAInterchangeSet.__mro__:
        if "ISid" in klass.__dict__:
            descriptor = klass.__dict__["ISid"]
            break
    assert isinstance(descriptor, property)



def test_afptext_endsegment_is_not_abstract():
    assert not inspect.isabstract(afpText_EndSegment)


def test_afptext_endsegment_constructor_exists():
    assert callable(afpText_EndSegment.__init__)


def test_afptext_endsegment_constructor_args():
    sig = inspect.signature(afpText_EndSegment.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gfarc_is_not_abstract():
    assert not inspect.isabstract(afpText_GFARC)


def test_afptext_gfarc_constructor_exists():
    assert callable(afpText_GFARC.__init__)


def test_afptext_gfarc_constructor_args():
    sig = inspect.signature(afpText_GFARC.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext_gfarc_has_XPOS():
    assert hasattr(afpText_GFARC, "XPOS")
    descriptor = None
    for klass in afpText_GFARC.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gfarc_has_YPOS():
    assert hasattr(afpText_GFARC, "YPOS")
    descriptor = None
    for klass in afpText_GFARC.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gfarc_has_MFR():
    assert hasattr(afpText_GFARC, "MFR")
    descriptor = None
    for klass in afpText_GFARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gfarc_has_MH():
    assert hasattr(afpText_GFARC, "MH")
    descriptor = None
    for klass in afpText_GFARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_textfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText_TextFidelity)


def test_afptext_textfidelity_constructor_exists():
    assert callable(afpText_TextFidelity.__init__)


def test_afptext_textfidelity_constructor_args():
    sig = inspect.signature(afpText_TextFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "RepTxtEx" in params, "Missing parameter 'RepTxtEx'"
    assert "StpTxtEx" in params, "Missing parameter 'StpTxtEx'"

def test_afptext_textfidelity_has_RepTxtEx():
    assert hasattr(afpText_TextFidelity, "RepTxtEx")
    descriptor = None
    for klass in afpText_TextFidelity.__mro__:
        if "RepTxtEx" in klass.__dict__:
            descriptor = klass.__dict__["RepTxtEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext_textfidelity_has_StpTxtEx():
    assert hasattr(afpText_TextFidelity, "StpTxtEx")
    descriptor = None
    for klass in afpText_TextFidelity.__mro__:
        if "StpTxtEx" in klass.__dict__:
            descriptor = klass.__dict__["StpTxtEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext_idestructure_is_not_abstract():
    assert not inspect.isabstract(afpText_IDEStructure)


def test_afptext_idestructure_constructor_exists():
    assert callable(afpText_IDEStructure.__init__)


def test_afptext_idestructure_constructor_args():
    sig = inspect.signature(afpText_IDEStructure.__init__)
    params = list(sig.parameters.keys())
    assert "FORMAT" in params, "Missing parameter 'FORMAT'"
    assert "SIZE2" in params, "Missing parameter 'SIZE2'"
    assert "FLAGS" in params, "Missing parameter 'FLAGS'"
    assert "SIZE4" in params, "Missing parameter 'SIZE4'"
    assert "SIZE1" in params, "Missing parameter 'SIZE1'"
    assert "SIZE3" in params, "Missing parameter 'SIZE3'"

def test_afptext_idestructure_has_FORMAT():
    assert hasattr(afpText_IDEStructure, "FORMAT")
    descriptor = None
    for klass in afpText_IDEStructure.__mro__:
        if "FORMAT" in klass.__dict__:
            descriptor = klass.__dict__["FORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idestructure_has_SIZE2():
    assert hasattr(afpText_IDEStructure, "SIZE2")
    descriptor = None
    for klass in afpText_IDEStructure.__mro__:
        if "SIZE2" in klass.__dict__:
            descriptor = klass.__dict__["SIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idestructure_has_FLAGS():
    assert hasattr(afpText_IDEStructure, "FLAGS")
    descriptor = None
    for klass in afpText_IDEStructure.__mro__:
        if "FLAGS" in klass.__dict__:
            descriptor = klass.__dict__["FLAGS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idestructure_has_SIZE4():
    assert hasattr(afpText_IDEStructure, "SIZE4")
    descriptor = None
    for klass in afpText_IDEStructure.__mro__:
        if "SIZE4" in klass.__dict__:
            descriptor = klass.__dict__["SIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idestructure_has_SIZE1():
    assert hasattr(afpText_IDEStructure, "SIZE1")
    descriptor = None
    for klass in afpText_IDEStructure.__mro__:
        if "SIZE1" in klass.__dict__:
            descriptor = klass.__dict__["SIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idestructure_has_SIZE3():
    assert hasattr(afpText_IDEStructure, "SIZE3")
    descriptor = None
    for klass in afpText_IDEStructure.__mro__:
        if "SIZE3" in klass.__dict__:
            descriptor = klass.__dict__["SIZE3"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnnrg2_is_not_abstract():
    assert not inspect.isabstract(afpText_FNNRG2)


def test_afptext_fnnrg2_constructor_exists():
    assert callable(afpText_FNNRG2.__init__)


def test_afptext_fnnrg2_constructor_args():
    sig = inspect.signature(afpText_FNNRG2.__init__)
    params = list(sig.parameters.keys())
    assert "TSIDLen" in params, "Missing parameter 'TSIDLen'"
    assert "TSID" in params, "Missing parameter 'TSID'"

def test_afptext_fnnrg2_has_TSIDLen():
    assert hasattr(afpText_FNNRG2, "TSIDLen")
    descriptor = None
    for klass in afpText_FNNRG2.__mro__:
        if "TSIDLen" in klass.__dict__:
            descriptor = klass.__dict__["TSIDLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnnrg2_has_TSID():
    assert hasattr(afpText_FNNRG2, "TSID")
    descriptor = None
    for klass in afpText_FNNRG2.__mro__:
        if "TSID" in klass.__dict__:
            descriptor = klass.__dict__["TSID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_begintransparencymask_is_not_abstract():
    assert not inspect.isabstract(afpText_BeginTransparencyMask)


def test_afptext_begintransparencymask_constructor_exists():
    assert callable(afpText_BeginTransparencyMask.__init__)


def test_afptext_begintransparencymask_constructor_args():
    sig = inspect.signature(afpText_BeginTransparencyMask.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gsch_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCH)


def test_afptext_gsch_constructor_exists():
    assert callable(afpText_GSCH.__init__)


def test_afptext_gsch_constructor_args():
    sig = inspect.signature(afpText_GSCH.__init__)
    params = list(sig.parameters.keys())
    assert "HX" in params, "Missing parameter 'HX'"
    assert "HY" in params, "Missing parameter 'HY'"

def test_afptext_gsch_has_HX():
    assert hasattr(afpText_GSCH, "HX")
    descriptor = None
    for klass in afpText_GSCH.__mro__:
        if "HX" in klass.__dict__:
            descriptor = klass.__dict__["HX"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsch_has_HY():
    assert hasattr(afpText_GSCH, "HY")
    descriptor = None
    for klass in afpText_GSCH.__mro__:
        if "HY" in klass.__dict__:
            descriptor = klass.__dict__["HY"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsecol_is_not_abstract():
    assert not inspect.isabstract(afpText_GSECOL)


def test_afptext_gsecol_constructor_exists():
    assert callable(afpText_GSECOL.__init__)


def test_afptext_gsecol_constructor_args():
    sig = inspect.signature(afpText_GSECOL.__init__)
    params = list(sig.parameters.keys())
    assert "COLOR" in params, "Missing parameter 'COLOR'"

def test_afptext_gsecol_has_COLOR():
    assert hasattr(afpText_GSECOL, "COLOR")
    descriptor = None
    for klass in afpText_GSECOL.__mro__:
        if "COLOR" in klass.__dict__:
            descriptor = klass.__dict__["COLOR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_resourceusageattribute_is_not_abstract():
    assert not inspect.isabstract(afpText_ResourceUsageAttribute)


def test_afptext_resourceusageattribute_constructor_exists():
    assert callable(afpText_ResourceUsageAttribute.__init__)


def test_afptext_resourceusageattribute_constructor_args():
    sig = inspect.signature(afpText_ResourceUsageAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "Frequency" in params, "Missing parameter 'Frequency'"

def test_afptext_resourceusageattribute_has_Frequency():
    assert hasattr(afpText_ResourceUsageAttribute, "Frequency")
    descriptor = None
    for klass in afpText_ResourceUsageAttribute.__mro__:
        if "Frequency" in klass.__dict__:
            descriptor = klass.__dict__["Frequency"]
            break
    assert isinstance(descriptor, property)



def test_afptext_includetile_is_not_abstract():
    assert not inspect.isabstract(afpText_IncludeTile)


def test_afptext_includetile_constructor_exists():
    assert callable(afpText_IncludeTile.__init__)


def test_afptext_includetile_constructor_args():
    sig = inspect.signature(afpText_IncludeTile.__init__)
    params = list(sig.parameters.keys())
    assert "TIRID" in params, "Missing parameter 'TIRID'"

def test_afptext_includetile_has_TIRID():
    assert hasattr(afpText_IncludeTile, "TIRID")
    descriptor = None
    for klass in afpText_IncludeTile.__mro__:
        if "TIRID" in klass.__dict__:
            descriptor = klass.__dict__["TIRID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectstructuredfieldoffset_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectStructuredFieldOffset)


def test_afptext_objectstructuredfieldoffset_constructor_exists():
    assert callable(afpText_ObjectStructuredFieldOffset.__init__)


def test_afptext_objectstructuredfieldoffset_constructor_args():
    sig = inspect.signature(afpText_ObjectStructuredFieldOffset.__init__)
    params = list(sig.parameters.keys())
    assert "SFOffHi" in params, "Missing parameter 'SFOffHi'"
    assert "SFOff" in params, "Missing parameter 'SFOff'"

def test_afptext_objectstructuredfieldoffset_has_SFOffHi():
    assert hasattr(afpText_ObjectStructuredFieldOffset, "SFOffHi")
    descriptor = None
    for klass in afpText_ObjectStructuredFieldOffset.__mro__:
        if "SFOffHi" in klass.__dict__:
            descriptor = klass.__dict__["SFOffHi"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectstructuredfieldoffset_has_SFOff():
    assert hasattr(afpText_ObjectStructuredFieldOffset, "SFOff")
    descriptor = None
    for klass in afpText_ObjectStructuredFieldOffset.__mro__:
        if "SFOff" in klass.__dict__:
            descriptor = klass.__dict__["SFOff"]
            break
    assert isinstance(descriptor, property)



def test_afptext_resourceobjectinclude_is_not_abstract():
    assert not inspect.isabstract(afpText_ResourceObjectInclude)


def test_afptext_resourceobjectinclude_constructor_exists():
    assert callable(afpText_ResourceObjectInclude.__init__)


def test_afptext_resourceobjectinclude_constructor_args():
    sig = inspect.signature(afpText_ResourceObjectInclude.__init__)
    params = list(sig.parameters.keys())
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "ObOrent" in params, "Missing parameter 'ObOrent'"
    assert "XobjOset" in params, "Missing parameter 'XobjOset'"
    assert "YobjOset" in params, "Missing parameter 'YobjOset'"
    assert "ObjName" in params, "Missing parameter 'ObjName'"

def test_afptext_resourceobjectinclude_has_ObjType():
    assert hasattr(afpText_ResourceObjectInclude, "ObjType")
    descriptor = None
    for klass in afpText_ResourceObjectInclude.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_resourceobjectinclude_has_ObOrent():
    assert hasattr(afpText_ResourceObjectInclude, "ObOrent")
    descriptor = None
    for klass in afpText_ResourceObjectInclude.__mro__:
        if "ObOrent" in klass.__dict__:
            descriptor = klass.__dict__["ObOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_resourceobjectinclude_has_XobjOset():
    assert hasattr(afpText_ResourceObjectInclude, "XobjOset")
    descriptor = None
    for klass in afpText_ResourceObjectInclude.__mro__:
        if "XobjOset" in klass.__dict__:
            descriptor = klass.__dict__["XobjOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_resourceobjectinclude_has_YobjOset():
    assert hasattr(afpText_ResourceObjectInclude, "YobjOset")
    descriptor = None
    for klass in afpText_ResourceObjectInclude.__mro__:
        if "YobjOset" in klass.__dict__:
            descriptor = klass.__dict__["YobjOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_resourceobjectinclude_has_ObjName():
    assert hasattr(afpText_ResourceObjectInclude, "ObjName")
    descriptor = None
    for klass in afpText_ResourceObjectInclude.__mro__:
        if "ObjName" in klass.__dict__:
            descriptor = klass.__dict__["ObjName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_resourceobjecttype_is_not_abstract():
    assert not inspect.isabstract(afpText_ResourceObjectType)


def test_afptext_resourceobjecttype_constructor_exists():
    assert callable(afpText_ResourceObjectType.__init__)


def test_afptext_resourceobjecttype_constructor_args():
    sig = inspect.signature(afpText_ResourceObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "ConData" in params, "Missing parameter 'ConData'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"

def test_afptext_resourceobjecttype_has_ConData():
    assert hasattr(afpText_ResourceObjectType, "ConData")
    descriptor = None
    for klass in afpText_ResourceObjectType.__mro__:
        if "ConData" in klass.__dict__:
            descriptor = klass.__dict__["ConData"]
            break
    assert isinstance(descriptor, property)

def test_afptext_resourceobjecttype_has_ObjType():
    assert hasattr(afpText_ResourceObjectType, "ObjType")
    descriptor = None
    for klass in afpText_ResourceObjectType.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)



def test_afptext_localdateandtimestamp_is_not_abstract():
    assert not inspect.isabstract(afpText_LocalDateAndTimeStamp)


def test_afptext_localdateandtimestamp_constructor_exists():
    assert callable(afpText_LocalDateAndTimeStamp.__init__)


def test_afptext_localdateandtimestamp_constructor_args():
    sig = inspect.signature(afpText_LocalDateAndTimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "TenYear" in params, "Missing parameter 'TenYear'"
    assert "Day" in params, "Missing parameter 'Day'"
    assert "StampType" in params, "Missing parameter 'StampType'"
    assert "HundSec" in params, "Missing parameter 'HundSec'"
    assert "Hour" in params, "Missing parameter 'Hour'"
    assert "Minute" in params, "Missing parameter 'Minute'"
    assert "THunYear" in params, "Missing parameter 'THunYear'"
    assert "Second" in params, "Missing parameter 'Second'"

def test_afptext_localdateandtimestamp_has_TenYear():
    assert hasattr(afpText_LocalDateAndTimeStamp, "TenYear")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "TenYear" in klass.__dict__:
            descriptor = klass.__dict__["TenYear"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_Day():
    assert hasattr(afpText_LocalDateAndTimeStamp, "Day")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "Day" in klass.__dict__:
            descriptor = klass.__dict__["Day"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_StampType():
    assert hasattr(afpText_LocalDateAndTimeStamp, "StampType")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "StampType" in klass.__dict__:
            descriptor = klass.__dict__["StampType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_HundSec():
    assert hasattr(afpText_LocalDateAndTimeStamp, "HundSec")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "HundSec" in klass.__dict__:
            descriptor = klass.__dict__["HundSec"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_Hour():
    assert hasattr(afpText_LocalDateAndTimeStamp, "Hour")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "Hour" in klass.__dict__:
            descriptor = klass.__dict__["Hour"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_Minute():
    assert hasattr(afpText_LocalDateAndTimeStamp, "Minute")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "Minute" in klass.__dict__:
            descriptor = klass.__dict__["Minute"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_THunYear():
    assert hasattr(afpText_LocalDateAndTimeStamp, "THunYear")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "THunYear" in klass.__dict__:
            descriptor = klass.__dict__["THunYear"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localdateandtimestamp_has_Second():
    assert hasattr(afpText_LocalDateAndTimeStamp, "Second")
    descriptor = None
    for klass in afpText_LocalDateAndTimeStamp.__mro__:
        if "Second" in klass.__dict__:
            descriptor = klass.__dict__["Second"]
            break
    assert isinstance(descriptor, property)



def test_afptext_endsegmentcommand_is_not_abstract():
    assert not inspect.isabstract(afpText_EndSegmentCommand)


def test_afptext_endsegmentcommand_constructor_exists():
    assert callable(afpText_EndSegmentCommand.__init__)


def test_afptext_endsegmentcommand_constructor_args():
    sig = inspect.signature(afpText_EndSegmentCommand.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gcchst_is_not_abstract():
    assert not inspect.isabstract(afpText_GCCHST)


def test_afptext_gcchst_constructor_exists():
    assert callable(afpText_GCCHST.__init__)


def test_afptext_gcchst_constructor_args():
    sig = inspect.signature(afpText_GCCHST.__init__)
    params = list(sig.parameters.keys())
    assert "CP" in params, "Missing parameter 'CP'"

def test_afptext_gcchst_has_CP():
    assert hasattr(afpText_GCCHST, "CP")
    descriptor = None
    for klass in afpText_GCCHST.__mro__:
        if "CP" in klass.__dict__:
            descriptor = klass.__dict__["CP"]
            break
    assert isinstance(descriptor, property)



def test_afptext_resourcelocalidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText_ResourceLocalIdentifier)


def test_afptext_resourcelocalidentifier_constructor_exists():
    assert callable(afpText_ResourceLocalIdentifier.__init__)


def test_afptext_resourcelocalidentifier_constructor_args():
    sig = inspect.signature(afpText_ResourceLocalIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "ResType" in params, "Missing parameter 'ResType'"
    assert "ResLID" in params, "Missing parameter 'ResLID'"

def test_afptext_resourcelocalidentifier_has_ResType():
    assert hasattr(afpText_ResourceLocalIdentifier, "ResType")
    descriptor = None
    for klass in afpText_ResourceLocalIdentifier.__mro__:
        if "ResType" in klass.__dict__:
            descriptor = klass.__dict__["ResType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_resourcelocalidentifier_has_ResLID():
    assert hasattr(afpText_ResourceLocalIdentifier, "ResLID")
    descriptor = None
    for klass in afpText_ResourceLocalIdentifier.__mro__:
        if "ResLID" in klass.__dict__:
            descriptor = klass.__dict__["ResLID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsap_is_not_abstract():
    assert not inspect.isabstract(afpText_GSAP)


def test_afptext_gsap_constructor_exists():
    assert callable(afpText_GSAP.__init__)


def test_afptext_gsap_constructor_args():
    sig = inspect.signature(afpText_GSAP.__init__)
    params = list(sig.parameters.keys())
    assert "P" in params, "Missing parameter 'P'"
    assert "R" in params, "Missing parameter 'R'"
    assert "Q" in params, "Missing parameter 'Q'"
    assert "S" in params, "Missing parameter 'S'"

def test_afptext_gsap_has_P():
    assert hasattr(afpText_GSAP, "P")
    descriptor = None
    for klass in afpText_GSAP.__mro__:
        if "P" in klass.__dict__:
            descriptor = klass.__dict__["P"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsap_has_R():
    assert hasattr(afpText_GSAP, "R")
    descriptor = None
    for klass in afpText_GSAP.__mro__:
        if "R" in klass.__dict__:
            descriptor = klass.__dict__["R"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsap_has_Q():
    assert hasattr(afpText_GSAP, "Q")
    descriptor = None
    for klass in afpText_GSAP.__mro__:
        if "Q" in klass.__dict__:
            descriptor = klass.__dict__["Q"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsap_has_S():
    assert hasattr(afpText_GSAP, "S")
    descriptor = None
    for klass in afpText_GSAP.__mro__:
        if "S" in klass.__dict__:
            descriptor = klass.__dict__["S"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gbimg_is_not_abstract():
    assert not inspect.isabstract(afpText_GBIMG)


def test_afptext_gbimg_constructor_exists():
    assert callable(afpText_GBIMG.__init__)


def test_afptext_gbimg_constructor_args():
    sig = inspect.signature(afpText_GBIMG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "RES" in params, "Missing parameter 'RES'"
    assert "FORMAT" in params, "Missing parameter 'FORMAT'"
    assert "WIDTH" in params, "Missing parameter 'WIDTH'"
    assert "HEIGHT" in params, "Missing parameter 'HEIGHT'"

def test_afptext_gbimg_has_YPOS():
    assert hasattr(afpText_GBIMG, "YPOS")
    descriptor = None
    for klass in afpText_GBIMG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbimg_has_XPOS():
    assert hasattr(afpText_GBIMG, "XPOS")
    descriptor = None
    for klass in afpText_GBIMG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbimg_has_RES():
    assert hasattr(afpText_GBIMG, "RES")
    descriptor = None
    for klass in afpText_GBIMG.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbimg_has_FORMAT():
    assert hasattr(afpText_GBIMG, "FORMAT")
    descriptor = None
    for klass in afpText_GBIMG.__mro__:
        if "FORMAT" in klass.__dict__:
            descriptor = klass.__dict__["FORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbimg_has_WIDTH():
    assert hasattr(afpText_GBIMG, "WIDTH")
    descriptor = None
    for klass in afpText_GBIMG.__mro__:
        if "WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["WIDTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbimg_has_HEIGHT():
    assert hasattr(afpText_GBIMG, "HEIGHT")
    descriptor = None
    for klass in afpText_GBIMG.__mro__:
        if "HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["HEIGHT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gccbez_is_not_abstract():
    assert not inspect.isabstract(afpText_GCCBEZ)


def test_afptext_gccbez_constructor_exists():
    assert callable(afpText_GCCBEZ.__init__)


def test_afptext_gccbez_constructor_args():
    sig = inspect.signature(afpText_GCCBEZ.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gsmt_is_not_abstract():
    assert not inspect.isabstract(afpText_GSMT)


def test_afptext_gsmt_constructor_exists():
    assert callable(afpText_GSMT.__init__)


def test_afptext_gsmt_constructor_args():
    sig = inspect.signature(afpText_GSMT.__init__)
    params = list(sig.parameters.keys())
    assert "MCPT" in params, "Missing parameter 'MCPT'"

def test_afptext_gsmt_has_MCPT():
    assert hasattr(afpText_GSMT, "MCPT")
    descriptor = None
    for klass in afpText_GSMT.__mro__:
        if "MCPT" in klass.__dict__:
            descriptor = klass.__dict__["MCPT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcfarc_is_not_abstract():
    assert not inspect.isabstract(afpText_GCFARC)


def test_afptext_gcfarc_constructor_exists():
    assert callable(afpText_GCFARC.__init__)


def test_afptext_gcfarc_constructor_args():
    sig = inspect.signature(afpText_GCFARC.__init__)
    params = list(sig.parameters.keys())
    assert "MH" in params, "Missing parameter 'MH'"
    assert "MFR" in params, "Missing parameter 'MFR'"

def test_afptext_gcfarc_has_MH():
    assert hasattr(afpText_GCFARC, "MH")
    descriptor = None
    for klass in afpText_GCFARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcfarc_has_MFR():
    assert hasattr(afpText_GCFARC, "MFR")
    descriptor = None
    for klass in afpText_GCFARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gmrk_is_not_abstract():
    assert not inspect.isabstract(afpText_GMRK)


def test_afptext_gmrk_constructor_exists():
    assert callable(afpText_GMRK.__init__)


def test_afptext_gmrk_constructor_args():
    sig = inspect.signature(afpText_GMRK.__init__)
    params = list(sig.parameters.keys())



def test_afptext_beginsegmentcommand_is_not_abstract():
    assert not inspect.isabstract(afpText_BeginSegmentCommand)


def test_afptext_beginsegmentcommand_constructor_exists():
    assert callable(afpText_BeginSegmentCommand.__init__)


def test_afptext_beginsegmentcommand_constructor_args():
    sig = inspect.signature(afpText_BeginSegmentCommand.__init__)
    params = list(sig.parameters.keys())
    assert "NAME" in params, "Missing parameter 'NAME'"
    assert "FLAG1" in params, "Missing parameter 'FLAG1'"
    assert "LENGTH" in params, "Missing parameter 'LENGTH'"
    assert "SEGL" in params, "Missing parameter 'SEGL'"
    assert "FLAG2" in params, "Missing parameter 'FLAG2'"
    assert "PSNAME" in params, "Missing parameter 'PSNAME'"

def test_afptext_beginsegmentcommand_has_NAME():
    assert hasattr(afpText_BeginSegmentCommand, "NAME")
    descriptor = None
    for klass in afpText_BeginSegmentCommand.__mro__:
        if "NAME" in klass.__dict__:
            descriptor = klass.__dict__["NAME"]
            break
    assert isinstance(descriptor, property)

def test_afptext_beginsegmentcommand_has_FLAG1():
    assert hasattr(afpText_BeginSegmentCommand, "FLAG1")
    descriptor = None
    for klass in afpText_BeginSegmentCommand.__mro__:
        if "FLAG1" in klass.__dict__:
            descriptor = klass.__dict__["FLAG1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_beginsegmentcommand_has_LENGTH():
    assert hasattr(afpText_BeginSegmentCommand, "LENGTH")
    descriptor = None
    for klass in afpText_BeginSegmentCommand.__mro__:
        if "LENGTH" in klass.__dict__:
            descriptor = klass.__dict__["LENGTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_beginsegmentcommand_has_SEGL():
    assert hasattr(afpText_BeginSegmentCommand, "SEGL")
    descriptor = None
    for klass in afpText_BeginSegmentCommand.__mro__:
        if "SEGL" in klass.__dict__:
            descriptor = klass.__dict__["SEGL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_beginsegmentcommand_has_FLAG2():
    assert hasattr(afpText_BeginSegmentCommand, "FLAG2")
    descriptor = None
    for klass in afpText_BeginSegmentCommand.__mro__:
        if "FLAG2" in klass.__dict__:
            descriptor = klass.__dict__["FLAG2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_beginsegmentcommand_has_PSNAME():
    assert hasattr(afpText_BeginSegmentCommand, "PSNAME")
    descriptor = None
    for klass in afpText_BeginSegmentCommand.__mro__:
        if "PSNAME" in klass.__dict__:
            descriptor = klass.__dict__["PSNAME"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fullyqualifiedname_is_not_abstract():
    assert not inspect.isabstract(afpText_FullyQualifiedName)


def test_afptext_fullyqualifiedname_constructor_exists():
    assert callable(afpText_FullyQualifiedName.__init__)


def test_afptext_fullyqualifiedname_constructor_args():
    sig = inspect.signature(afpText_FullyQualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "FQName" in params, "Missing parameter 'FQName'"
    assert "FQNFormat" in params, "Missing parameter 'FQNFormat'"
    assert "FQNType" in params, "Missing parameter 'FQNType'"

def test_afptext_fullyqualifiedname_has_FQName():
    assert hasattr(afpText_FullyQualifiedName, "FQName")
    descriptor = None
    for klass in afpText_FullyQualifiedName.__mro__:
        if "FQName" in klass.__dict__:
            descriptor = klass.__dict__["FQName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fullyqualifiedname_has_FQNFormat():
    assert hasattr(afpText_FullyQualifiedName, "FQNFormat")
    descriptor = None
    for klass in afpText_FullyQualifiedName.__mro__:
        if "FQNFormat" in klass.__dict__:
            descriptor = klass.__dict__["FQNFormat"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fullyqualifiedname_has_FQNType():
    assert hasattr(afpText_FullyQualifiedName, "FQNType")
    descriptor = None
    for klass in afpText_FullyQualifiedName.__mro__:
        if "FQNType" in klass.__dict__:
            descriptor = klass.__dict__["FQNType"]
            break
    assert isinstance(descriptor, property)



def test_afptext_samplingratios_is_not_abstract():
    assert not inspect.isabstract(afpText_SamplingRatios)


def test_afptext_samplingratios_constructor_exists():
    assert callable(afpText_SamplingRatios.__init__)


def test_afptext_samplingratios_constructor_args():
    sig = inspect.signature(afpText_SamplingRatios.__init__)
    params = list(sig.parameters.keys())



def test_afptext_metricadjustment_is_not_abstract():
    assert not inspect.isabstract(afpText_MetricAdjustment)


def test_afptext_metricadjustment_constructor_exists():
    assert callable(afpText_MetricAdjustment.__init__)


def test_afptext_metricadjustment_constructor_args():
    sig = inspect.signature(afpText_MetricAdjustment.__init__)
    params = list(sig.parameters.keys())
    assert "YUPUB" in params, "Missing parameter 'YUPUB'"
    assert "HBaselineIncrement" in params, "Missing parameter 'HBaselineIncrement'"
    assert "XUPUB" in params, "Missing parameter 'XUPUB'"
    assert "HUniformIncrement" in params, "Missing parameter 'HUniformIncrement'"
    assert "UnitBase" in params, "Missing parameter 'UnitBase'"
    assert "VBaselineIncrement" in params, "Missing parameter 'VBaselineIncrement'"
    assert "VUniformIncrement" in params, "Missing parameter 'VUniformIncrement'"

def test_afptext_metricadjustment_has_YUPUB():
    assert hasattr(afpText_MetricAdjustment, "YUPUB")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "YUPUB" in klass.__dict__:
            descriptor = klass.__dict__["YUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext_metricadjustment_has_HBaselineIncrement():
    assert hasattr(afpText_MetricAdjustment, "HBaselineIncrement")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "HBaselineIncrement" in klass.__dict__:
            descriptor = klass.__dict__["HBaselineIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext_metricadjustment_has_XUPUB():
    assert hasattr(afpText_MetricAdjustment, "XUPUB")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "XUPUB" in klass.__dict__:
            descriptor = klass.__dict__["XUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext_metricadjustment_has_HUniformIncrement():
    assert hasattr(afpText_MetricAdjustment, "HUniformIncrement")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "HUniformIncrement" in klass.__dict__:
            descriptor = klass.__dict__["HUniformIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext_metricadjustment_has_UnitBase():
    assert hasattr(afpText_MetricAdjustment, "UnitBase")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "UnitBase" in klass.__dict__:
            descriptor = klass.__dict__["UnitBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_metricadjustment_has_VBaselineIncrement():
    assert hasattr(afpText_MetricAdjustment, "VBaselineIncrement")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "VBaselineIncrement" in klass.__dict__:
            descriptor = klass.__dict__["VBaselineIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext_metricadjustment_has_VUniformIncrement():
    assert hasattr(afpText_MetricAdjustment, "VUniformIncrement")
    descriptor = None
    for klass in afpText_MetricAdjustment.__mro__:
        if "VUniformIncrement" in klass.__dict__:
            descriptor = klass.__dict__["VUniformIncrement"]
            break
    assert isinstance(descriptor, property)



def test_afptext_dataobjectfontdescriptor_is_not_abstract():
    assert not inspect.isabstract(afpText_DataObjectFontDescriptor)


def test_afptext_dataobjectfontdescriptor_constructor_exists():
    assert callable(afpText_DataObjectFontDescriptor.__init__)


def test_afptext_dataobjectfontdescriptor_constructor_args():
    sig = inspect.signature(afpText_DataObjectFontDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "EncEnv" in params, "Missing parameter 'EncEnv'"
    assert "VFS" in params, "Missing parameter 'VFS'"
    assert "DOFtFlgs" in params, "Missing parameter 'DOFtFlgs'"
    assert "FontTech" in params, "Missing parameter 'FontTech'"
    assert "CharRot" in params, "Missing parameter 'CharRot'"
    assert "HFS" in params, "Missing parameter 'HFS'"
    assert "EncID" in params, "Missing parameter 'EncID'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_dataobjectfontdescriptor_has_EncEnv():
    assert hasattr(afpText_DataObjectFontDescriptor, "EncEnv")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "EncEnv" in klass.__dict__:
            descriptor = klass.__dict__["EncEnv"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_VFS():
    assert hasattr(afpText_DataObjectFontDescriptor, "VFS")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "VFS" in klass.__dict__:
            descriptor = klass.__dict__["VFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_DOFtFlgs():
    assert hasattr(afpText_DataObjectFontDescriptor, "DOFtFlgs")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "DOFtFlgs" in klass.__dict__:
            descriptor = klass.__dict__["DOFtFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_FontTech():
    assert hasattr(afpText_DataObjectFontDescriptor, "FontTech")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "FontTech" in klass.__dict__:
            descriptor = klass.__dict__["FontTech"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_CharRot():
    assert hasattr(afpText_DataObjectFontDescriptor, "CharRot")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_HFS():
    assert hasattr(afpText_DataObjectFontDescriptor, "HFS")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "HFS" in klass.__dict__:
            descriptor = klass.__dict__["HFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_EncID():
    assert hasattr(afpText_DataObjectFontDescriptor, "EncID")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "EncID" in klass.__dict__:
            descriptor = klass.__dict__["EncID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dataobjectfontdescriptor_has_Reserved():
    assert hasattr(afpText_DataObjectFontDescriptor, "Reserved")
    descriptor = None
    for klass in afpText_DataObjectFontDescriptor.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mediummappagenumber_is_not_abstract():
    assert not inspect.isabstract(afpText_MediumMapPageNumber)


def test_afptext_mediummappagenumber_constructor_exists():
    assert callable(afpText_MediumMapPageNumber.__init__)


def test_afptext_mediummappagenumber_constructor_args():
    sig = inspect.signature(afpText_MediumMapPageNumber.__init__)
    params = list(sig.parameters.keys())
    assert "PageNum" in params, "Missing parameter 'PageNum'"

def test_afptext_mediummappagenumber_has_PageNum():
    assert hasattr(afpText_MediumMapPageNumber, "PageNum")
    descriptor = None
    for klass in afpText_MediumMapPageNumber.__mro__:
        if "PageNum" in klass.__dict__:
            descriptor = klass.__dict__["PageNum"]
            break
    assert isinstance(descriptor, property)



def test_afptext_geimg_is_not_abstract():
    assert not inspect.isabstract(afpText_GEIMG)


def test_afptext_geimg_constructor_exists():
    assert callable(afpText_GEIMG.__init__)


def test_afptext_geimg_constructor_args():
    sig = inspect.signature(afpText_GEIMG.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext_geimg_has_DATA():
    assert hasattr(afpText_GEIMG, "DATA")
    descriptor = None
    for klass in afpText_GEIMG.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsflw_is_not_abstract():
    assert not inspect.isabstract(afpText_GSFLW)


def test_afptext_gsflw_constructor_exists():
    assert callable(afpText_GSFLW.__init__)


def test_afptext_gsflw_constructor_args():
    sig = inspect.signature(afpText_GSFLW.__init__)
    params = list(sig.parameters.keys())
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext_gsflw_has_MFR():
    assert hasattr(afpText_GSFLW, "MFR")
    descriptor = None
    for klass in afpText_GSFLW.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsflw_has_MH():
    assert hasattr(afpText_GSFLW, "MH")
    descriptor = None
    for klass in afpText_GSFLW.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gnop1_is_not_abstract():
    assert not inspect.isabstract(afpText_GNOP1)


def test_afptext_gnop1_constructor_exists():
    assert callable(afpText_GNOP1.__init__)


def test_afptext_gnop1_constructor_args():
    sig = inspect.signature(afpText_GNOP1.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gcline_is_not_abstract():
    assert not inspect.isabstract(afpText_GCLINE)


def test_afptext_gcline_constructor_exists():
    assert callable(afpText_GCLINE.__init__)


def test_afptext_gcline_constructor_args():
    sig = inspect.signature(afpText_GCLINE.__init__)
    params = list(sig.parameters.keys())



def test_afptext_localeselector_is_not_abstract():
    assert not inspect.isabstract(afpText_LocaleSelector)


def test_afptext_localeselector_constructor_exists():
    assert callable(afpText_LocaleSelector.__init__)


def test_afptext_localeselector_constructor_args():
    sig = inspect.signature(afpText_LocaleSelector.__init__)
    params = list(sig.parameters.keys())
    assert "LocFlgs" in params, "Missing parameter 'LocFlgs'"
    assert "LangCode" in params, "Missing parameter 'LangCode'"
    assert "ScrptCde" in params, "Missing parameter 'ScrptCde'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "VarCde" in params, "Missing parameter 'VarCde'"
    assert "RegCde" in params, "Missing parameter 'RegCde'"

def test_afptext_localeselector_has_LocFlgs():
    assert hasattr(afpText_LocaleSelector, "LocFlgs")
    descriptor = None
    for klass in afpText_LocaleSelector.__mro__:
        if "LocFlgs" in klass.__dict__:
            descriptor = klass.__dict__["LocFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localeselector_has_LangCode():
    assert hasattr(afpText_LocaleSelector, "LangCode")
    descriptor = None
    for klass in afpText_LocaleSelector.__mro__:
        if "LangCode" in klass.__dict__:
            descriptor = klass.__dict__["LangCode"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localeselector_has_ScrptCde():
    assert hasattr(afpText_LocaleSelector, "ScrptCde")
    descriptor = None
    for klass in afpText_LocaleSelector.__mro__:
        if "ScrptCde" in klass.__dict__:
            descriptor = klass.__dict__["ScrptCde"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localeselector_has_Reserved():
    assert hasattr(afpText_LocaleSelector, "Reserved")
    descriptor = None
    for klass in afpText_LocaleSelector.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localeselector_has_VarCde():
    assert hasattr(afpText_LocaleSelector, "VarCde")
    descriptor = None
    for klass in afpText_LocaleSelector.__mro__:
        if "VarCde" in klass.__dict__:
            descriptor = klass.__dict__["VarCde"]
            break
    assert isinstance(descriptor, property)

def test_afptext_localeselector_has_RegCde():
    assert hasattr(afpText_LocaleSelector, "RegCde")
    descriptor = None
    for klass in afpText_LocaleSelector.__mro__:
        if "RegCde" in klass.__dict__:
            descriptor = klass.__dict__["RegCde"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mediaejectcontrol_is_not_abstract():
    assert not inspect.isabstract(afpText_MediaEjectControl)


def test_afptext_mediaejectcontrol_constructor_exists():
    assert callable(afpText_MediaEjectControl.__init__)


def test_afptext_mediaejectcontrol_constructor_args():
    sig = inspect.signature(afpText_MediaEjectControl.__init__)
    params = list(sig.parameters.keys())
    assert "EjCtrl" in params, "Missing parameter 'EjCtrl'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_mediaejectcontrol_has_EjCtrl():
    assert hasattr(afpText_MediaEjectControl, "EjCtrl")
    descriptor = None
    for klass in afpText_MediaEjectControl.__mro__:
        if "EjCtrl" in klass.__dict__:
            descriptor = klass.__dict__["EjCtrl"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mediaejectcontrol_has_Reserved():
    assert hasattr(afpText_MediaEjectControl, "Reserved")
    descriptor = None
    for klass in afpText_MediaEjectControl.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gear_is_not_abstract():
    assert not inspect.isabstract(afpText_GEAR)


def test_afptext_gear_constructor_exists():
    assert callable(afpText_GEAR.__init__)


def test_afptext_gear_constructor_args():
    sig = inspect.signature(afpText_GEAR.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext_gear_has_DATA():
    assert hasattr(afpText_GEAR, "DATA")
    descriptor = None
    for klass in afpText_GEAR.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_measurementunits_is_not_abstract():
    assert not inspect.isabstract(afpText_MeasurementUnits)


def test_afptext_measurementunits_constructor_exists():
    assert callable(afpText_MeasurementUnits.__init__)


def test_afptext_measurementunits_constructor_args():
    sig = inspect.signature(afpText_MeasurementUnits.__init__)
    params = list(sig.parameters.keys())
    assert "YoaBase" in params, "Missing parameter 'YoaBase'"
    assert "XoaUnits" in params, "Missing parameter 'XoaUnits'"
    assert "YoaUnits" in params, "Missing parameter 'YoaUnits'"
    assert "XoaBase" in params, "Missing parameter 'XoaBase'"

def test_afptext_measurementunits_has_YoaBase():
    assert hasattr(afpText_MeasurementUnits, "YoaBase")
    descriptor = None
    for klass in afpText_MeasurementUnits.__mro__:
        if "YoaBase" in klass.__dict__:
            descriptor = klass.__dict__["YoaBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_measurementunits_has_XoaUnits():
    assert hasattr(afpText_MeasurementUnits, "XoaUnits")
    descriptor = None
    for klass in afpText_MeasurementUnits.__mro__:
        if "XoaUnits" in klass.__dict__:
            descriptor = klass.__dict__["XoaUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_measurementunits_has_YoaUnits():
    assert hasattr(afpText_MeasurementUnits, "YoaUnits")
    descriptor = None
    for klass in afpText_MeasurementUnits.__mro__:
        if "YoaUnits" in klass.__dict__:
            descriptor = klass.__dict__["YoaUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_measurementunits_has_XoaBase():
    assert hasattr(afpText_MeasurementUnits, "XoaBase")
    descriptor = None
    for klass in afpText_MeasurementUnits.__mro__:
        if "XoaBase" in klass.__dict__:
            descriptor = klass.__dict__["XoaBase"]
            break
    assert isinstance(descriptor, property)



def test_afptext_drawingordersubset_is_not_abstract():
    assert not inspect.isabstract(afpText_DrawingOrderSubset)


def test_afptext_drawingordersubset_constructor_exists():
    assert callable(afpText_DrawingOrderSubset.__init__)


def test_afptext_drawingordersubset_constructor_args():
    sig = inspect.signature(afpText_DrawingOrderSubset.__init__)
    params = list(sig.parameters.keys())



def test_afptext_objectbyteoffset_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectByteOffset)


def test_afptext_objectbyteoffset_constructor_exists():
    assert callable(afpText_ObjectByteOffset.__init__)


def test_afptext_objectbyteoffset_constructor_args():
    sig = inspect.signature(afpText_ObjectByteOffset.__init__)
    params = list(sig.parameters.keys())
    assert "DirByOff" in params, "Missing parameter 'DirByOff'"
    assert "DirByHi" in params, "Missing parameter 'DirByHi'"

def test_afptext_objectbyteoffset_has_DirByOff():
    assert hasattr(afpText_ObjectByteOffset, "DirByOff")
    descriptor = None
    for klass in afpText_ObjectByteOffset.__mro__:
        if "DirByOff" in klass.__dict__:
            descriptor = klass.__dict__["DirByOff"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectbyteoffset_has_DirByHi():
    assert hasattr(afpText_ObjectByteOffset, "DirByHi")
    descriptor = None
    for klass in afpText_ObjectByteOffset.__mro__:
        if "DirByHi" in klass.__dict__:
            descriptor = klass.__dict__["DirByHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsca_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCA)


def test_afptext_gsca_constructor_exists():
    assert callable(afpText_GSCA.__init__)


def test_afptext_gsca_constructor_args():
    sig = inspect.signature(afpText_GSCA.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gsca_has_YPOS():
    assert hasattr(afpText_GSCA, "YPOS")
    descriptor = None
    for klass in afpText_GSCA.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsca_has_XPOS():
    assert hasattr(afpText_GSCA, "XPOS")
    descriptor = None
    for klass in afpText_GSCA.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcbox_is_not_abstract():
    assert not inspect.isabstract(afpText_GCBOX)


def test_afptext_gcbox_constructor_exists():
    assert callable(afpText_GCBOX.__init__)


def test_afptext_gcbox_constructor_args():
    sig = inspect.signature(afpText_GCBOX.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS1" in params, "Missing parameter 'XPOS1'"
    assert "YPOS1" in params, "Missing parameter 'YPOS1'"
    assert "RES" in params, "Missing parameter 'RES'"
    assert "VAXIS" in params, "Missing parameter 'VAXIS'"
    assert "HAXIS" in params, "Missing parameter 'HAXIS'"

def test_afptext_gcbox_has_XPOS1():
    assert hasattr(afpText_GCBOX, "XPOS1")
    descriptor = None
    for klass in afpText_GCBOX.__mro__:
        if "XPOS1" in klass.__dict__:
            descriptor = klass.__dict__["XPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbox_has_YPOS1():
    assert hasattr(afpText_GCBOX, "YPOS1")
    descriptor = None
    for klass in afpText_GCBOX.__mro__:
        if "YPOS1" in klass.__dict__:
            descriptor = klass.__dict__["YPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbox_has_RES():
    assert hasattr(afpText_GCBOX, "RES")
    descriptor = None
    for klass in afpText_GCBOX.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbox_has_VAXIS():
    assert hasattr(afpText_GCBOX, "VAXIS")
    descriptor = None
    for klass in afpText_GCBOX.__mro__:
        if "VAXIS" in klass.__dict__:
            descriptor = klass.__dict__["VAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbox_has_HAXIS():
    assert hasattr(afpText_GCBOX, "HAXIS")
    descriptor = None
    for klass in afpText_GCBOX.__mro__:
        if "HAXIS" in klass.__dict__:
            descriptor = klass.__dict__["HAXIS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_extensionfont_is_not_abstract():
    assert not inspect.isabstract(afpText_ExtensionFont)


def test_afptext_extensionfont_constructor_exists():
    assert callable(afpText_ExtensionFont.__init__)


def test_afptext_extensionfont_constructor_args():
    sig = inspect.signature(afpText_ExtensionFont.__init__)
    params = list(sig.parameters.keys())
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"

def test_afptext_extensionfont_has_GCSGID():
    assert hasattr(afpText_ExtensionFont, "GCSGID")
    descriptor = None
    for klass in afpText_ExtensionFont.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_presentationspaceresetmixing_is_not_abstract():
    assert not inspect.isabstract(afpText_PresentationSpaceResetMixing)


def test_afptext_presentationspaceresetmixing_constructor_exists():
    assert callable(afpText_PresentationSpaceResetMixing.__init__)


def test_afptext_presentationspaceresetmixing_constructor_args():
    sig = inspect.signature(afpText_PresentationSpaceResetMixing.__init__)
    params = list(sig.parameters.keys())
    assert "BgMxFlag" in params, "Missing parameter 'BgMxFlag'"

def test_afptext_presentationspaceresetmixing_has_BgMxFlag():
    assert hasattr(afpText_PresentationSpaceResetMixing, "BgMxFlag")
    descriptor = None
    for klass in afpText_PresentationSpaceResetMixing.__mro__:
        if "BgMxFlag" in klass.__dict__:
            descriptor = klass.__dict__["BgMxFlag"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tileposition_is_not_abstract():
    assert not inspect.isabstract(afpText_TilePosition)


def test_afptext_tileposition_constructor_exists():
    assert callable(afpText_TilePosition.__init__)


def test_afptext_tileposition_constructor_args():
    sig = inspect.signature(afpText_TilePosition.__init__)
    params = list(sig.parameters.keys())
    assert "XOFFSET" in params, "Missing parameter 'XOFFSET'"
    assert "YOFFSET" in params, "Missing parameter 'YOFFSET'"

def test_afptext_tileposition_has_XOFFSET():
    assert hasattr(afpText_TilePosition, "XOFFSET")
    descriptor = None
    for klass in afpText_TilePosition.__mro__:
        if "XOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["XOFFSET"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tileposition_has_YOFFSET():
    assert hasattr(afpText_TilePosition, "YOFFSET")
    descriptor = None
    for klass in afpText_TilePosition.__mro__:
        if "YOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["YOFFSET"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gline_is_not_abstract():
    assert not inspect.isabstract(afpText_GLINE)


def test_afptext_gline_constructor_exists():
    assert callable(afpText_GLINE.__init__)


def test_afptext_gline_constructor_args():
    sig = inspect.signature(afpText_GLINE.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gsmc_is_not_abstract():
    assert not inspect.isabstract(afpText_GSMC)


def test_afptext_gsmc_constructor_exists():
    assert callable(afpText_GSMC.__init__)


def test_afptext_gsmc_constructor_args():
    sig = inspect.signature(afpText_GSMC.__init__)
    params = list(sig.parameters.keys())
    assert "CELLWI" in params, "Missing parameter 'CELLWI'"
    assert "CELLHI" in params, "Missing parameter 'CELLHI'"

def test_afptext_gsmc_has_CELLWI():
    assert hasattr(afpText_GSMC, "CELLWI")
    descriptor = None
    for klass in afpText_GSMC.__mro__:
        if "CELLWI" in klass.__dict__:
            descriptor = klass.__dict__["CELLWI"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gsmc_has_CELLHI():
    assert hasattr(afpText_GSMC, "CELLHI")
    descriptor = None
    for klass in afpText_GSMC.__mro__:
        if "CELLHI" in klass.__dict__:
            descriptor = klass.__dict__["CELLHI"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pageoverlayconditionalprocessing_is_not_abstract():
    assert not inspect.isabstract(afpText_PageOverlayConditionalProcessing)


def test_afptext_pageoverlayconditionalprocessing_constructor_exists():
    assert callable(afpText_PageOverlayConditionalProcessing.__init__)


def test_afptext_pageoverlayconditionalprocessing_constructor_args():
    sig = inspect.signature(afpText_PageOverlayConditionalProcessing.__init__)
    params = list(sig.parameters.keys())
    assert "PgOvType" in params, "Missing parameter 'PgOvType'"
    assert "Level" in params, "Missing parameter 'Level'"

def test_afptext_pageoverlayconditionalprocessing_has_PgOvType():
    assert hasattr(afpText_PageOverlayConditionalProcessing, "PgOvType")
    descriptor = None
    for klass in afpText_PageOverlayConditionalProcessing.__mro__:
        if "PgOvType" in klass.__dict__:
            descriptor = klass.__dict__["PgOvType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pageoverlayconditionalprocessing_has_Level():
    assert hasattr(afpText_PageOverlayConditionalProcessing, "Level")
    descriptor = None
    for klass in afpText_PageOverlayConditionalProcessing.__mro__:
        if "Level" in klass.__dict__:
            descriptor = klass.__dict__["Level"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cmrfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText_CMRFidelity)


def test_afptext_cmrfidelity_constructor_exists():
    assert callable(afpText_CMRFidelity.__init__)


def test_afptext_cmrfidelity_constructor_args():
    sig = inspect.signature(afpText_CMRFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "RepCMREx" in params, "Missing parameter 'RepCMREx'"
    assert "StpCMREx" in params, "Missing parameter 'StpCMREx'"

def test_afptext_cmrfidelity_has_RepCMREx():
    assert hasattr(afpText_CMRFidelity, "RepCMREx")
    descriptor = None
    for klass in afpText_CMRFidelity.__mro__:
        if "RepCMREx" in klass.__dict__:
            descriptor = klass.__dict__["RepCMREx"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cmrfidelity_has_StpCMREx():
    assert hasattr(afpText_CMRFidelity, "StpCMREx")
    descriptor = None
    for klass in afpText_CMRFidelity.__mro__:
        if "StpCMREx" in klass.__dict__:
            descriptor = klass.__dict__["StpCMREx"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gbar_is_not_abstract():
    assert not inspect.isabstract(afpText_GBAR)


def test_afptext_gbar_constructor_exists():
    assert callable(afpText_GBAR.__init__)


def test_afptext_gbar_constructor_args():
    sig = inspect.signature(afpText_GBAR.__init__)
    params = list(sig.parameters.keys())
    assert "FLAGS" in params, "Missing parameter 'FLAGS'"

def test_afptext_gbar_has_FLAGS():
    assert hasattr(afpText_GBAR, "FLAGS")
    descriptor = None
    for klass in afpText_GBAR.__mro__:
        if "FLAGS" in klass.__dict__:
            descriptor = klass.__dict__["FLAGS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gimd_is_not_abstract():
    assert not inspect.isabstract(afpText_GIMD)


def test_afptext_gimd_constructor_exists():
    assert callable(afpText_GIMD.__init__)


def test_afptext_gimd_constructor_args():
    sig = inspect.signature(afpText_GIMD.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext_gimd_has_DATA():
    assert hasattr(afpText_GIMD, "DATA")
    descriptor = None
    for klass in afpText_GIMD.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tiletoc_is_not_abstract():
    assert not inspect.isabstract(afpText_TileTOC)


def test_afptext_tiletoc_constructor_exists():
    assert callable(afpText_TileTOC.__init__)


def test_afptext_tiletoc_constructor_args():
    sig = inspect.signature(afpText_TileTOC.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_tiletoc_has_Reserved():
    assert hasattr(afpText_TileTOC, "Reserved")
    descriptor = None
    for klass in afpText_TileTOC.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_crcresourcemanagement_is_not_abstract():
    assert not inspect.isabstract(afpText_CRCResourceManagement)


def test_afptext_crcresourcemanagement_constructor_exists():
    assert callable(afpText_CRCResourceManagement.__init__)


def test_afptext_crcresourcemanagement_constructor_args():
    sig = inspect.signature(afpText_CRCResourceManagement.__init__)
    params = list(sig.parameters.keys())
    assert "ResClassFlg" in params, "Missing parameter 'ResClassFlg'"
    assert "RMValue" in params, "Missing parameter 'RMValue'"
    assert "FmtQual" in params, "Missing parameter 'FmtQual'"

def test_afptext_crcresourcemanagement_has_ResClassFlg():
    assert hasattr(afpText_CRCResourceManagement, "ResClassFlg")
    descriptor = None
    for klass in afpText_CRCResourceManagement.__mro__:
        if "ResClassFlg" in klass.__dict__:
            descriptor = klass.__dict__["ResClassFlg"]
            break
    assert isinstance(descriptor, property)

def test_afptext_crcresourcemanagement_has_RMValue():
    assert hasattr(afpText_CRCResourceManagement, "RMValue")
    descriptor = None
    for klass in afpText_CRCResourceManagement.__mro__:
        if "RMValue" in klass.__dict__:
            descriptor = klass.__dict__["RMValue"]
            break
    assert isinstance(descriptor, property)

def test_afptext_crcresourcemanagement_has_FmtQual():
    assert hasattr(afpText_CRCResourceManagement, "FmtQual")
    descriptor = None
    for klass in afpText_CRCResourceManagement.__mro__:
        if "FmtQual" in klass.__dict__:
            descriptor = klass.__dict__["FmtQual"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gscc_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCC)


def test_afptext_gscc_constructor_exists():
    assert callable(afpText_GSCC.__init__)


def test_afptext_gscc_constructor_args():
    sig = inspect.signature(afpText_GSCC.__init__)
    params = list(sig.parameters.keys())
    assert "CELLHFR" in params, "Missing parameter 'CELLHFR'"
    assert "CELLHI" in params, "Missing parameter 'CELLHI'"
    assert "CELLWI" in params, "Missing parameter 'CELLWI'"
    assert "CELLWFR" in params, "Missing parameter 'CELLWFR'"

def test_afptext_gscc_has_CELLHFR():
    assert hasattr(afpText_GSCC, "CELLHFR")
    descriptor = None
    for klass in afpText_GSCC.__mro__:
        if "CELLHFR" in klass.__dict__:
            descriptor = klass.__dict__["CELLHFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gscc_has_CELLHI():
    assert hasattr(afpText_GSCC, "CELLHI")
    descriptor = None
    for klass in afpText_GSCC.__mro__:
        if "CELLHI" in klass.__dict__:
            descriptor = klass.__dict__["CELLHI"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gscc_has_CELLWI():
    assert hasattr(afpText_GSCC, "CELLWI")
    descriptor = None
    for klass in afpText_GSCC.__mro__:
        if "CELLWI" in klass.__dict__:
            descriptor = klass.__dict__["CELLWI"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gscc_has_CELLWFR():
    assert hasattr(afpText_GSCC, "CELLWFR")
    descriptor = None
    for klass in afpText_GSCC.__mro__:
        if "CELLWFR" in klass.__dict__:
            descriptor = klass.__dict__["CELLWFR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectbyteextent_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectByteExtent)


def test_afptext_objectbyteextent_constructor_exists():
    assert callable(afpText_ObjectByteExtent.__init__)


def test_afptext_objectbyteextent_constructor_args():
    sig = inspect.signature(afpText_ObjectByteExtent.__init__)
    params = list(sig.parameters.keys())
    assert "ByteExt" in params, "Missing parameter 'ByteExt'"
    assert "ByteExtHi" in params, "Missing parameter 'ByteExtHi'"

def test_afptext_objectbyteextent_has_ByteExt():
    assert hasattr(afpText_ObjectByteExtent, "ByteExt")
    descriptor = None
    for klass in afpText_ObjectByteExtent.__mro__:
        if "ByteExt" in klass.__dict__:
            descriptor = klass.__dict__["ByteExt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectbyteextent_has_ByteExtHi():
    assert hasattr(afpText_ObjectByteExtent, "ByteExtHi")
    descriptor = None
    for klass in afpText_ObjectByteExtent.__mro__:
        if "ByteExtHi" in klass.__dict__:
            descriptor = klass.__dict__["ByteExtHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectfunctionsetspecification_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectFunctionSetSpecification)


def test_afptext_objectfunctionsetspecification_constructor_exists():
    assert callable(afpText_ObjectFunctionSetSpecification.__init__)


def test_afptext_objectfunctionsetspecification_constructor_args():
    sig = inspect.signature(afpText_ObjectFunctionSetSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "DCAFnSet" in params, "Missing parameter 'DCAFnSet'"
    assert "OCAFnSet" in params, "Missing parameter 'OCAFnSet'"
    assert "ArchVrsn" in params, "Missing parameter 'ArchVrsn'"

def test_afptext_objectfunctionsetspecification_has_ObjType():
    assert hasattr(afpText_ObjectFunctionSetSpecification, "ObjType")
    descriptor = None
    for klass in afpText_ObjectFunctionSetSpecification.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectfunctionsetspecification_has_DCAFnSet():
    assert hasattr(afpText_ObjectFunctionSetSpecification, "DCAFnSet")
    descriptor = None
    for klass in afpText_ObjectFunctionSetSpecification.__mro__:
        if "DCAFnSet" in klass.__dict__:
            descriptor = klass.__dict__["DCAFnSet"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectfunctionsetspecification_has_OCAFnSet():
    assert hasattr(afpText_ObjectFunctionSetSpecification, "OCAFnSet")
    descriptor = None
    for klass in afpText_ObjectFunctionSetSpecification.__mro__:
        if "OCAFnSet" in klass.__dict__:
            descriptor = klass.__dict__["OCAFnSet"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectfunctionsetspecification_has_ArchVrsn():
    assert hasattr(afpText_ObjectFunctionSetSpecification, "ArchVrsn")
    descriptor = None
    for klass in afpText_ObjectFunctionSetSpecification.__mro__:
        if "ArchVrsn" in klass.__dict__:
            descriptor = klass.__dict__["ArchVrsn"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcbimg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCBIMG)


def test_afptext_gcbimg_constructor_exists():
    assert callable(afpText_GCBIMG.__init__)


def test_afptext_gcbimg_constructor_args():
    sig = inspect.signature(afpText_GCBIMG.__init__)
    params = list(sig.parameters.keys())
    assert "FORMAT" in params, "Missing parameter 'FORMAT'"
    assert "HEIGHT" in params, "Missing parameter 'HEIGHT'"
    assert "RES" in params, "Missing parameter 'RES'"
    assert "WIDTH" in params, "Missing parameter 'WIDTH'"

def test_afptext_gcbimg_has_FORMAT():
    assert hasattr(afpText_GCBIMG, "FORMAT")
    descriptor = None
    for klass in afpText_GCBIMG.__mro__:
        if "FORMAT" in klass.__dict__:
            descriptor = klass.__dict__["FORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbimg_has_HEIGHT():
    assert hasattr(afpText_GCBIMG, "HEIGHT")
    descriptor = None
    for klass in afpText_GCBIMG.__mro__:
        if "HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["HEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbimg_has_RES():
    assert hasattr(afpText_GCBIMG, "RES")
    descriptor = None
    for klass in afpText_GCBIMG.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbimg_has_WIDTH():
    assert hasattr(afpText_GCBIMG, "WIDTH")
    descriptor = None
    for klass in afpText_GCBIMG.__mro__:
        if "WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["WIDTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_geprol_is_not_abstract():
    assert not inspect.isabstract(afpText_GEPROL)


def test_afptext_geprol_constructor_exists():
    assert callable(afpText_GEPROL.__init__)


def test_afptext_geprol_constructor_args():
    sig = inspect.signature(afpText_GEPROL.__init__)
    params = list(sig.parameters.keys())
    assert "RES" in params, "Missing parameter 'RES'"

def test_afptext_geprol_has_RES():
    assert hasattr(afpText_GEPROL, "RES")
    descriptor = None
    for klass in afpText_GEPROL.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mediafidelity_is_not_abstract():
    assert not inspect.isabstract(afpText_MediaFidelity)


def test_afptext_mediafidelity_constructor_exists():
    assert callable(afpText_MediaFidelity.__init__)


def test_afptext_mediafidelity_constructor_args():
    sig = inspect.signature(afpText_MediaFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "StpMedEx" in params, "Missing parameter 'StpMedEx'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_mediafidelity_has_StpMedEx():
    assert hasattr(afpText_MediaFidelity, "StpMedEx")
    descriptor = None
    for klass in afpText_MediaFidelity.__mro__:
        if "StpMedEx" in klass.__dict__:
            descriptor = klass.__dict__["StpMedEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mediafidelity_has_Reserved():
    assert hasattr(afpText_MediaFidelity, "Reserved")
    descriptor = None
    for klass in afpText_MediaFidelity.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_finishingfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText_FinishingFidelity)


def test_afptext_finishingfidelity_constructor_exists():
    assert callable(afpText_FinishingFidelity.__init__)


def test_afptext_finishingfidelity_constructor_args():
    sig = inspect.signature(afpText_FinishingFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "StpFinEx" in params, "Missing parameter 'StpFinEx'"
    assert "RepFinEx" in params, "Missing parameter 'RepFinEx'"

def test_afptext_finishingfidelity_has_StpFinEx():
    assert hasattr(afpText_FinishingFidelity, "StpFinEx")
    descriptor = None
    for klass in afpText_FinishingFidelity.__mro__:
        if "StpFinEx" in klass.__dict__:
            descriptor = klass.__dict__["StpFinEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext_finishingfidelity_has_RepFinEx():
    assert hasattr(afpText_FinishingFidelity, "RepFinEx")
    descriptor = None
    for klass in afpText_FinishingFidelity.__mro__:
        if "RepFinEx" in klass.__dict__:
            descriptor = klass.__dict__["RepFinEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext_imagelutid_is_not_abstract():
    assert not inspect.isabstract(afpText_ImageLUTID)


def test_afptext_imagelutid_constructor_exists():
    assert callable(afpText_ImageLUTID.__init__)


def test_afptext_imagelutid_constructor_args():
    sig = inspect.signature(afpText_ImageLUTID.__init__)
    params = list(sig.parameters.keys())
    assert "LUTID" in params, "Missing parameter 'LUTID'"

def test_afptext_imagelutid_has_LUTID():
    assert hasattr(afpText_ImageLUTID, "LUTID")
    descriptor = None
    for klass in afpText_ImageLUTID.__mro__:
        if "LUTID" in klass.__dict__:
            descriptor = klass.__dict__["LUTID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gscol_is_not_abstract():
    assert not inspect.isabstract(afpText_GSCOL)


def test_afptext_gscol_constructor_exists():
    assert callable(afpText_GSCOL.__init__)


def test_afptext_gscol_constructor_args():
    sig = inspect.signature(afpText_GSCOL.__init__)
    params = list(sig.parameters.keys())
    assert "COL" in params, "Missing parameter 'COL'"

def test_afptext_gscol_has_COL():
    assert hasattr(afpText_GSCOL, "COL")
    descriptor = None
    for klass in afpText_GSCOL.__mro__:
        if "COL" in klass.__dict__:
            descriptor = klass.__dict__["COL"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ami_is_not_abstract():
    assert not inspect.isabstract(afpText_AMI)


def test_afptext_ami_constructor_exists():
    assert callable(afpText_AMI.__init__)


def test_afptext_ami_constructor_args():
    sig = inspect.signature(afpText_AMI.__init__)
    params = list(sig.parameters.keys())
    assert "DSPLCMNT" in params, "Missing parameter 'DSPLCMNT'"

def test_afptext_ami_has_DSPLCMNT():
    assert hasattr(afpText_AMI, "DSPLCMNT")
    descriptor = None
    for klass in afpText_AMI.__mro__:
        if "DSPLCMNT" in klass.__dict__:
            descriptor = klass.__dict__["DSPLCMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_comment_is_not_abstract():
    assert not inspect.isabstract(afpText_Comment)


def test_afptext_comment_constructor_exists():
    assert callable(afpText_Comment.__init__)


def test_afptext_comment_constructor_args():
    sig = inspect.signature(afpText_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "Comment" in params, "Missing parameter 'Comment'"

def test_afptext_comment_has_Comment():
    assert hasattr(afpText_Comment, "Comment")
    descriptor = None
    for klass in afpText_Comment.__mro__:
        if "Comment" in klass.__dict__:
            descriptor = klass.__dict__["Comment"]
            break
    assert isinstance(descriptor, property)



def test_afptext_windowspecification_is_not_abstract():
    assert not inspect.isabstract(afpText_WindowSpecification)


def test_afptext_windowspecification_constructor_exists():
    assert callable(afpText_WindowSpecification.__init__)


def test_afptext_windowspecification_constructor_args():
    sig = inspect.signature(afpText_WindowSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "RES3" in params, "Missing parameter 'RES3'"
    assert "CFORMAT" in params, "Missing parameter 'CFORMAT'"
    assert "IMGXYRES" in params, "Missing parameter 'IMGXYRES'"
    assert "XRWIND" in params, "Missing parameter 'XRWIND'"
    assert "FLAGS" in params, "Missing parameter 'FLAGS'"
    assert "YRESOL" in params, "Missing parameter 'YRESOL'"
    assert "UBASE" in params, "Missing parameter 'UBASE'"
    assert "XLWIND" in params, "Missing parameter 'XLWIND'"
    assert "XRESOL" in params, "Missing parameter 'XRESOL'"
    assert "YTWIND" in params, "Missing parameter 'YTWIND'"
    assert "YBWIND" in params, "Missing parameter 'YBWIND'"

def test_afptext_windowspecification_has_RES3():
    assert hasattr(afpText_WindowSpecification, "RES3")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "RES3" in klass.__dict__:
            descriptor = klass.__dict__["RES3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_CFORMAT():
    assert hasattr(afpText_WindowSpecification, "CFORMAT")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "CFORMAT" in klass.__dict__:
            descriptor = klass.__dict__["CFORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_IMGXYRES():
    assert hasattr(afpText_WindowSpecification, "IMGXYRES")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "IMGXYRES" in klass.__dict__:
            descriptor = klass.__dict__["IMGXYRES"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_XRWIND():
    assert hasattr(afpText_WindowSpecification, "XRWIND")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "XRWIND" in klass.__dict__:
            descriptor = klass.__dict__["XRWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_FLAGS():
    assert hasattr(afpText_WindowSpecification, "FLAGS")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "FLAGS" in klass.__dict__:
            descriptor = klass.__dict__["FLAGS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_YRESOL():
    assert hasattr(afpText_WindowSpecification, "YRESOL")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "YRESOL" in klass.__dict__:
            descriptor = klass.__dict__["YRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_UBASE():
    assert hasattr(afpText_WindowSpecification, "UBASE")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "UBASE" in klass.__dict__:
            descriptor = klass.__dict__["UBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_XLWIND():
    assert hasattr(afpText_WindowSpecification, "XLWIND")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "XLWIND" in klass.__dict__:
            descriptor = klass.__dict__["XLWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_XRESOL():
    assert hasattr(afpText_WindowSpecification, "XRESOL")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "XRESOL" in klass.__dict__:
            descriptor = klass.__dict__["XRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_YTWIND():
    assert hasattr(afpText_WindowSpecification, "YTWIND")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "YTWIND" in klass.__dict__:
            descriptor = klass.__dict__["YTWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext_windowspecification_has_YBWIND():
    assert hasattr(afpText_WindowSpecification, "YBWIND")
    descriptor = None
    for klass in afpText_WindowSpecification.__mro__:
        if "YBWIND" in klass.__dict__:
            descriptor = klass.__dict__["YBWIND"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fontresolution_is_not_abstract():
    assert not inspect.isabstract(afpText_FontResolution)


def test_afptext_fontresolution_constructor_exists():
    assert callable(afpText_FontResolution.__init__)


def test_afptext_fontresolution_constructor_args():
    sig = inspect.signature(afpText_FontResolution.__init__)
    params = list(sig.parameters.keys())
    assert "RPuBase" in params, "Missing parameter 'RPuBase'"
    assert "RPUnits" in params, "Missing parameter 'RPUnits'"
    assert "MetTech" in params, "Missing parameter 'MetTech'"

def test_afptext_fontresolution_has_RPuBase():
    assert hasattr(afpText_FontResolution, "RPuBase")
    descriptor = None
    for klass in afpText_FontResolution.__mro__:
        if "RPuBase" in klass.__dict__:
            descriptor = klass.__dict__["RPuBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontresolution_has_RPUnits():
    assert hasattr(afpText_FontResolution, "RPUnits")
    descriptor = None
    for klass in afpText_FontResolution.__mro__:
        if "RPUnits" in klass.__dict__:
            descriptor = klass.__dict__["RPUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontresolution_has_MetTech():
    assert hasattr(afpText_FontResolution, "MetTech")
    descriptor = None
    for klass in afpText_FontResolution.__mro__:
        if "MetTech" in klass.__dict__:
            descriptor = klass.__dict__["MetTech"]
            break
    assert isinstance(descriptor, property)



def test_afptext_textorientation_is_not_abstract():
    assert not inspect.isabstract(afpText_TextOrientation)


def test_afptext_textorientation_constructor_exists():
    assert callable(afpText_TextOrientation.__init__)


def test_afptext_textorientation_constructor_args():
    sig = inspect.signature(afpText_TextOrientation.__init__)
    params = list(sig.parameters.keys())
    assert "BAxis" in params, "Missing parameter 'BAxis'"
    assert "IAxis" in params, "Missing parameter 'IAxis'"

def test_afptext_textorientation_has_BAxis():
    assert hasattr(afpText_TextOrientation, "BAxis")
    descriptor = None
    for klass in afpText_TextOrientation.__mro__:
        if "BAxis" in klass.__dict__:
            descriptor = klass.__dict__["BAxis"]
            break
    assert isinstance(descriptor, property)

def test_afptext_textorientation_has_IAxis():
    assert hasattr(afpText_TextOrientation, "IAxis")
    descriptor = None
    for klass in afpText_TextOrientation.__mro__:
        if "IAxis" in klass.__dict__:
            descriptor = klass.__dict__["IAxis"]
            break
    assert isinstance(descriptor, property)



def test_afptext_up3ifinishingoperation_is_not_abstract():
    assert not inspect.isabstract(afpText_UP3iFinishingOperation)


def test_afptext_up3ifinishingoperation_constructor_exists():
    assert callable(afpText_UP3iFinishingOperation.__init__)


def test_afptext_up3ifinishingoperation_constructor_args():
    sig = inspect.signature(afpText_UP3iFinishingOperation.__init__)
    params = list(sig.parameters.keys())
    assert "UP3iDat" in params, "Missing parameter 'UP3iDat'"
    assert "Seqnum" in params, "Missing parameter 'Seqnum'"

def test_afptext_up3ifinishingoperation_has_UP3iDat():
    assert hasattr(afpText_UP3iFinishingOperation, "UP3iDat")
    descriptor = None
    for klass in afpText_UP3iFinishingOperation.__mro__:
        if "UP3iDat" in klass.__dict__:
            descriptor = klass.__dict__["UP3iDat"]
            break
    assert isinstance(descriptor, property)

def test_afptext_up3ifinishingoperation_has_Seqnum():
    assert hasattr(afpText_UP3iFinishingOperation, "Seqnum")
    descriptor = None
    for klass in afpText_UP3iFinishingOperation.__mro__:
        if "Seqnum" in klass.__dict__:
            descriptor = klass.__dict__["Seqnum"]
            break
    assert isinstance(descriptor, property)



def test_afptext_beginsegment_is_not_abstract():
    assert not inspect.isabstract(afpText_BeginSegment)


def test_afptext_beginsegment_constructor_exists():
    assert callable(afpText_BeginSegment.__init__)


def test_afptext_beginsegment_constructor_args():
    sig = inspect.signature(afpText_BeginSegment.__init__)
    params = list(sig.parameters.keys())
    assert "SEGNAME" in params, "Missing parameter 'SEGNAME'"

def test_afptext_beginsegment_has_SEGNAME():
    assert hasattr(afpText_BeginSegment, "SEGNAME")
    descriptor = None
    for klass in afpText_BeginSegment.__mro__:
        if "SEGNAME" in klass.__dict__:
            descriptor = klass.__dict__["SEGNAME"]
            break
    assert isinstance(descriptor, property)



def test_afptext_endtile_is_not_abstract():
    assert not inspect.isabstract(afpText_EndTile)


def test_afptext_endtile_constructor_exists():
    assert callable(afpText_EndTile.__init__)


def test_afptext_endtile_constructor_args():
    sig = inspect.signature(afpText_EndTile.__init__)
    params = list(sig.parameters.keys())



def test_afptext_presentationspacemixingrules_is_not_abstract():
    assert not inspect.isabstract(afpText_PresentationSpaceMixingRules)


def test_afptext_presentationspacemixingrules_constructor_exists():
    assert callable(afpText_PresentationSpaceMixingRules.__init__)


def test_afptext_presentationspacemixingrules_constructor_args():
    sig = inspect.signature(afpText_PresentationSpaceMixingRules.__init__)
    params = list(sig.parameters.keys())



def test_afptext_attributequalifier_is_not_abstract():
    assert not inspect.isabstract(afpText_AttributeQualifier)


def test_afptext_attributequalifier_constructor_exists():
    assert callable(afpText_AttributeQualifier.__init__)


def test_afptext_attributequalifier_constructor_args():
    sig = inspect.signature(afpText_AttributeQualifier.__init__)
    params = list(sig.parameters.keys())
    assert "SeqNum" in params, "Missing parameter 'SeqNum'"
    assert "LevNum" in params, "Missing parameter 'LevNum'"

def test_afptext_attributequalifier_has_SeqNum():
    assert hasattr(afpText_AttributeQualifier, "SeqNum")
    descriptor = None
    for klass in afpText_AttributeQualifier.__mro__:
        if "SeqNum" in klass.__dict__:
            descriptor = klass.__dict__["SeqNum"]
            break
    assert isinstance(descriptor, property)

def test_afptext_attributequalifier_has_LevNum():
    assert hasattr(afpText_AttributeQualifier, "LevNum")
    descriptor = None
    for klass in afpText_AttributeQualifier.__mro__:
        if "LevNum" in klass.__dict__:
            descriptor = klass.__dict__["LevNum"]
            break
    assert isinstance(descriptor, property)



def test_afptext_trn_is_not_abstract():
    assert not inspect.isabstract(afpText_TRN)


def test_afptext_trn_constructor_exists():
    assert callable(afpText_TRN.__init__)


def test_afptext_trn_constructor_args():
    sig = inspect.signature(afpText_TRN.__init__)
    params = list(sig.parameters.keys())
    assert "TRNDATA" in params, "Missing parameter 'TRNDATA'"

def test_afptext_trn_has_TRNDATA():
    assert hasattr(afpText_TRN, "TRNDATA")
    descriptor = None
    for klass in afpText_TRN.__mro__:
        if "TRNDATA" in klass.__dict__:
            descriptor = klass.__dict__["TRNDATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsle_is_not_abstract():
    assert not inspect.isabstract(afpText_GSLE)


def test_afptext_gsle_constructor_exists():
    assert callable(afpText_GSLE.__init__)


def test_afptext_gsle_constructor_args():
    sig = inspect.signature(afpText_GSLE.__init__)
    params = list(sig.parameters.keys())
    assert "LINEEND" in params, "Missing parameter 'LINEEND'"

def test_afptext_gsle_has_LINEEND():
    assert hasattr(afpText_GSLE, "LINEEND")
    descriptor = None
    for klass in afpText_GSLE.__mro__:
        if "LINEEND" in klass.__dict__:
            descriptor = klass.__dict__["LINEEND"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bsu_is_not_abstract():
    assert not inspect.isabstract(afpText_BSU)


def test_afptext_bsu_constructor_exists():
    assert callable(afpText_BSU.__init__)


def test_afptext_bsu_constructor_args():
    sig = inspect.signature(afpText_BSU.__init__)
    params = list(sig.parameters.keys())
    assert "LID" in params, "Missing parameter 'LID'"

def test_afptext_bsu_has_LID():
    assert hasattr(afpText_BSU, "LID")
    descriptor = None
    for klass in afpText_BSU.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fontcodedgraphiccharactersetglobalidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText_FontCodedGraphicCharacterSetGlobalIdentifier)


def test_afptext_fontcodedgraphiccharactersetglobalidentifier_constructor_exists():
    assert callable(afpText_FontCodedGraphicCharacterSetGlobalIdentifier.__init__)


def test_afptext_fontcodedgraphiccharactersetglobalidentifier_constructor_args():
    sig = inspect.signature(afpText_FontCodedGraphicCharacterSetGlobalIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "CPGID" in params, "Missing parameter 'CPGID'"
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"

def test_afptext_fontcodedgraphiccharactersetglobalidentifier_has_CPGID():
    assert hasattr(afpText_FontCodedGraphicCharacterSetGlobalIdentifier, "CPGID")
    descriptor = None
    for klass in afpText_FontCodedGraphicCharacterSetGlobalIdentifier.__mro__:
        if "CPGID" in klass.__dict__:
            descriptor = klass.__dict__["CPGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fontcodedgraphiccharactersetglobalidentifier_has_GCSGID():
    assert hasattr(afpText_FontCodedGraphicCharacterSetGlobalIdentifier, "GCSGID")
    descriptor = None
    for klass in afpText_FontCodedGraphicCharacterSetGlobalIdentifier.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcomt_is_not_abstract():
    assert not inspect.isabstract(afpText_GCOMT)


def test_afptext_gcomt_constructor_exists():
    assert callable(afpText_GCOMT.__init__)


def test_afptext_gcomt_constructor_args():
    sig = inspect.signature(afpText_GCOMT.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext_gcomt_has_DATA():
    assert hasattr(afpText_GCOMT, "DATA")
    descriptor = None
    for klass in afpText_GCOMT.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_begintile_is_not_abstract():
    assert not inspect.isabstract(afpText_BeginTile)


def test_afptext_begintile_constructor_exists():
    assert callable(afpText_BeginTile.__init__)


def test_afptext_begintile_constructor_args():
    sig = inspect.signature(afpText_BeginTile.__init__)
    params = list(sig.parameters.keys())



def test_afptext_usc_is_not_abstract():
    assert not inspect.isabstract(afpText_USC)


def test_afptext_usc_constructor_exists():
    assert callable(afpText_USC.__init__)


def test_afptext_usc_constructor_args():
    sig = inspect.signature(afpText_USC.__init__)
    params = list(sig.parameters.keys())
    assert "BYPSIDEN" in params, "Missing parameter 'BYPSIDEN'"

def test_afptext_usc_has_BYPSIDEN():
    assert hasattr(afpText_USC, "BYPSIDEN")
    descriptor = None
    for klass in afpText_USC.__mro__:
        if "BYPSIDEN" in klass.__dict__:
            descriptor = klass.__dict__["BYPSIDEN"]
            break
    assert isinstance(descriptor, property)



def test_afptext_presentationcontrol_is_not_abstract():
    assert not inspect.isabstract(afpText_PresentationControl)


def test_afptext_presentationcontrol_constructor_exists():
    assert callable(afpText_PresentationControl.__init__)


def test_afptext_presentationcontrol_constructor_args():
    sig = inspect.signature(afpText_PresentationControl.__init__)
    params = list(sig.parameters.keys())
    assert "PRSFlg" in params, "Missing parameter 'PRSFlg'"

def test_afptext_presentationcontrol_has_PRSFlg():
    assert hasattr(afpText_PresentationControl, "PRSFlg")
    descriptor = None
    for klass in afpText_PresentationControl.__mro__:
        if "PRSFlg" in klass.__dict__:
            descriptor = klass.__dict__["PRSFlg"]
            break
    assert isinstance(descriptor, property)



def test_afptext_descriptorposition_is_not_abstract():
    assert not inspect.isabstract(afpText_DescriptorPosition)


def test_afptext_descriptorposition_constructor_exists():
    assert callable(afpText_DescriptorPosition.__init__)


def test_afptext_descriptorposition_constructor_args():
    sig = inspect.signature(afpText_DescriptorPosition.__init__)
    params = list(sig.parameters.keys())
    assert "DesPosID" in params, "Missing parameter 'DesPosID'"

def test_afptext_descriptorposition_has_DesPosID():
    assert hasattr(afpText_DescriptorPosition, "DesPosID")
    descriptor = None
    for klass in afpText_DescriptorPosition.__mro__:
        if "DesPosID" in klass.__dict__:
            descriptor = klass.__dict__["DesPosID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tilesetcolor_is_not_abstract():
    assert not inspect.isabstract(afpText_TileSetColor)


def test_afptext_tilesetcolor_constructor_exists():
    assert callable(afpText_TileSetColor.__init__)


def test_afptext_tilesetcolor_constructor_args():
    sig = inspect.signature(afpText_TileSetColor.__init__)
    params = list(sig.parameters.keys())
    assert "SIZE3" in params, "Missing parameter 'SIZE3'"
    assert "SIZE2" in params, "Missing parameter 'SIZE2'"
    assert "CVAL3" in params, "Missing parameter 'CVAL3'"
    assert "CVAL1" in params, "Missing parameter 'CVAL1'"
    assert "SIZE1" in params, "Missing parameter 'SIZE1'"
    assert "CSPACE" in params, "Missing parameter 'CSPACE'"
    assert "SIZE4" in params, "Missing parameter 'SIZE4'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "CVAL2" in params, "Missing parameter 'CVAL2'"
    assert "CVAL4" in params, "Missing parameter 'CVAL4'"

def test_afptext_tilesetcolor_has_SIZE3():
    assert hasattr(afpText_TileSetColor, "SIZE3")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "SIZE3" in klass.__dict__:
            descriptor = klass.__dict__["SIZE3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_SIZE2():
    assert hasattr(afpText_TileSetColor, "SIZE2")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "SIZE2" in klass.__dict__:
            descriptor = klass.__dict__["SIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_CVAL3():
    assert hasattr(afpText_TileSetColor, "CVAL3")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "CVAL3" in klass.__dict__:
            descriptor = klass.__dict__["CVAL3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_CVAL1():
    assert hasattr(afpText_TileSetColor, "CVAL1")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "CVAL1" in klass.__dict__:
            descriptor = klass.__dict__["CVAL1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_SIZE1():
    assert hasattr(afpText_TileSetColor, "SIZE1")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "SIZE1" in klass.__dict__:
            descriptor = klass.__dict__["SIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_CSPACE():
    assert hasattr(afpText_TileSetColor, "CSPACE")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "CSPACE" in klass.__dict__:
            descriptor = klass.__dict__["CSPACE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_SIZE4():
    assert hasattr(afpText_TileSetColor, "SIZE4")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "SIZE4" in klass.__dict__:
            descriptor = klass.__dict__["SIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_RESERVED():
    assert hasattr(afpText_TileSetColor, "RESERVED")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_CVAL2():
    assert hasattr(afpText_TileSetColor, "CVAL2")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "CVAL2" in klass.__dict__:
            descriptor = klass.__dict__["CVAL2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tilesetcolor_has_CVAL4():
    assert hasattr(afpText_TileSetColor, "CVAL4")
    descriptor = None
    for klass in afpText_TileSetColor.__mro__:
        if "CVAL4" in klass.__dict__:
            descriptor = klass.__dict__["CVAL4"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gslj_is_not_abstract():
    assert not inspect.isabstract(afpText_GSLJ)


def test_afptext_gslj_constructor_exists():
    assert callable(afpText_GSLJ.__init__)


def test_afptext_gslj_constructor_args():
    sig = inspect.signature(afpText_GSLJ.__init__)
    params = list(sig.parameters.keys())
    assert "LINEJOIN" in params, "Missing parameter 'LINEJOIN'"

def test_afptext_gslj_has_LINEJOIN():
    assert hasattr(afpText_GSLJ, "LINEJOIN")
    descriptor = None
    for klass in afpText_GSLJ.__mro__:
        if "LINEJOIN" in klass.__dict__:
            descriptor = klass.__dict__["LINEJOIN"]
            break
    assert isinstance(descriptor, property)



def test_afptext_iocafunctionsetidentification_is_not_abstract():
    assert not inspect.isabstract(afpText_IOCAFunctionSetIdentification)


def test_afptext_iocafunctionsetidentification_constructor_exists():
    assert callable(afpText_IOCAFunctionSetIdentification.__init__)


def test_afptext_iocafunctionsetidentification_constructor_args():
    sig = inspect.signature(afpText_IOCAFunctionSetIdentification.__init__)
    params = list(sig.parameters.keys())
    assert "CATEGORY" in params, "Missing parameter 'CATEGORY'"
    assert "FCNSET" in params, "Missing parameter 'FCNSET'"

def test_afptext_iocafunctionsetidentification_has_CATEGORY():
    assert hasattr(afpText_IOCAFunctionSetIdentification, "CATEGORY")
    descriptor = None
    for klass in afpText_IOCAFunctionSetIdentification.__mro__:
        if "CATEGORY" in klass.__dict__:
            descriptor = klass.__dict__["CATEGORY"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iocafunctionsetidentification_has_FCNSET():
    assert hasattr(afpText_IOCAFunctionSetIdentification, "FCNSET")
    descriptor = None
    for klass in afpText_IOCAFunctionSetIdentification.__mro__:
        if "FCNSET" in klass.__dict__:
            descriptor = klass.__dict__["FCNSET"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gbox_is_not_abstract():
    assert not inspect.isabstract(afpText_GBOX)


def test_afptext_gbox_constructor_exists():
    assert callable(afpText_GBOX.__init__)


def test_afptext_gbox_constructor_args():
    sig = inspect.signature(afpText_GBOX.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS1" in params, "Missing parameter 'XPOS1'"
    assert "XPOS0" in params, "Missing parameter 'XPOS0'"
    assert "HAXIS" in params, "Missing parameter 'HAXIS'"
    assert "YPOS0" in params, "Missing parameter 'YPOS0'"
    assert "YPOS1" in params, "Missing parameter 'YPOS1'"
    assert "VAXIS" in params, "Missing parameter 'VAXIS'"
    assert "RES" in params, "Missing parameter 'RES'"

def test_afptext_gbox_has_XPOS1():
    assert hasattr(afpText_GBOX, "XPOS1")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "XPOS1" in klass.__dict__:
            descriptor = klass.__dict__["XPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbox_has_XPOS0():
    assert hasattr(afpText_GBOX, "XPOS0")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "XPOS0" in klass.__dict__:
            descriptor = klass.__dict__["XPOS0"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbox_has_HAXIS():
    assert hasattr(afpText_GBOX, "HAXIS")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "HAXIS" in klass.__dict__:
            descriptor = klass.__dict__["HAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbox_has_YPOS0():
    assert hasattr(afpText_GBOX, "YPOS0")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "YPOS0" in klass.__dict__:
            descriptor = klass.__dict__["YPOS0"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbox_has_YPOS1():
    assert hasattr(afpText_GBOX, "YPOS1")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "YPOS1" in klass.__dict__:
            descriptor = klass.__dict__["YPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbox_has_VAXIS():
    assert hasattr(afpText_GBOX, "VAXIS")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "VAXIS" in klass.__dict__:
            descriptor = klass.__dict__["VAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gbox_has_RES():
    assert hasattr(afpText_GBOX, "RES")
    descriptor = None
    for klass in afpText_GBOX.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)



def test_afptext_colorfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText_ColorFidelity)


def test_afptext_colorfidelity_constructor_exists():
    assert callable(afpText_ColorFidelity.__init__)


def test_afptext_colorfidelity_constructor_args():
    sig = inspect.signature(afpText_ColorFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "RepCoEx" in params, "Missing parameter 'RepCoEx'"
    assert "StpCoEx" in params, "Missing parameter 'StpCoEx'"
    assert "ColSub" in params, "Missing parameter 'ColSub'"

def test_afptext_colorfidelity_has_RepCoEx():
    assert hasattr(afpText_ColorFidelity, "RepCoEx")
    descriptor = None
    for klass in afpText_ColorFidelity.__mro__:
        if "RepCoEx" in klass.__dict__:
            descriptor = klass.__dict__["RepCoEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorfidelity_has_StpCoEx():
    assert hasattr(afpText_ColorFidelity, "StpCoEx")
    descriptor = None
    for klass in afpText_ColorFidelity.__mro__:
        if "StpCoEx" in klass.__dict__:
            descriptor = klass.__dict__["StpCoEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext_colorfidelity_has_ColSub():
    assert hasattr(afpText_ColorFidelity, "ColSub")
    descriptor = None
    for klass in afpText_ColorFidelity.__mro__:
        if "ColSub" in klass.__dict__:
            descriptor = klass.__dict__["ColSub"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gslw_is_not_abstract():
    assert not inspect.isabstract(afpText_GSLW)


def test_afptext_gslw_constructor_exists():
    assert callable(afpText_GSLW.__init__)


def test_afptext_gslw_constructor_args():
    sig = inspect.signature(afpText_GSLW.__init__)
    params = list(sig.parameters.keys())
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext_gslw_has_MH():
    assert hasattr(afpText_GSLW, "MH")
    descriptor = None
    for klass in afpText_GSLW.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsmx_is_not_abstract():
    assert not inspect.isabstract(afpText_GSMX)


def test_afptext_gsmx_constructor_exists():
    assert callable(afpText_GSMX.__init__)


def test_afptext_gsmx_constructor_args():
    sig = inspect.signature(afpText_GSMX.__init__)
    params = list(sig.parameters.keys())
    assert "MODE" in params, "Missing parameter 'MODE'"

def test_afptext_gsmx_has_MODE():
    assert hasattr(afpText_GSMX, "MODE")
    descriptor = None
    for klass in afpText_GSMX.__mro__:
        if "MODE" in klass.__dict__:
            descriptor = klass.__dict__["MODE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gchst_is_not_abstract():
    assert not inspect.isabstract(afpText_GCHST)


def test_afptext_gchst_constructor_exists():
    assert callable(afpText_GCHST.__init__)


def test_afptext_gchst_constructor_args():
    sig = inspect.signature(afpText_GCHST.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "CP" in params, "Missing parameter 'CP'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gchst_has_YPOS():
    assert hasattr(afpText_GCHST, "YPOS")
    descriptor = None
    for klass in afpText_GCHST.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gchst_has_CP():
    assert hasattr(afpText_GCHST, "CP")
    descriptor = None
    for klass in afpText_GCHST.__mro__:
        if "CP" in klass.__dict__:
            descriptor = klass.__dict__["CP"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gchst_has_XPOS():
    assert hasattr(afpText_GCHST, "XPOS")
    descriptor = None
    for klass in afpText_GCHST.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcrline_is_not_abstract():
    assert not inspect.isabstract(afpText_GCRLINE)


def test_afptext_gcrline_constructor_exists():
    assert callable(afpText_GCRLINE.__init__)


def test_afptext_gcrline_constructor_args():
    sig = inspect.signature(afpText_GCRLINE.__init__)
    params = list(sig.parameters.keys())



def test_afptext_grline_is_not_abstract():
    assert not inspect.isabstract(afpText_GRLINE)


def test_afptext_grline_constructor_exists():
    assert callable(afpText_GRLINE.__init__)


def test_afptext_grline_constructor_args():
    sig = inspect.signature(afpText_GRLINE.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext_grline_has_XPOS():
    assert hasattr(afpText_GRLINE, "XPOS")
    descriptor = None
    for klass in afpText_GRLINE.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_grline_has_YPOS():
    assert hasattr(afpText_GRLINE, "YPOS")
    descriptor = None
    for klass in afpText_GRLINE.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_setbilevelimagecolor_is_not_abstract():
    assert not inspect.isabstract(afpText_SetBiLevelImageColor)


def test_afptext_setbilevelimagecolor_constructor_exists():
    assert callable(afpText_SetBiLevelImageColor.__init__)


def test_afptext_setbilevelimagecolor_constructor_args():
    sig = inspect.signature(afpText_SetBiLevelImageColor.__init__)
    params = list(sig.parameters.keys())
    assert "NAMECOLR" in params, "Missing parameter 'NAMECOLR'"
    assert "AREA" in params, "Missing parameter 'AREA'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_setbilevelimagecolor_has_NAMECOLR():
    assert hasattr(afpText_SetBiLevelImageColor, "NAMECOLR")
    descriptor = None
    for klass in afpText_SetBiLevelImageColor.__mro__:
        if "NAMECOLR" in klass.__dict__:
            descriptor = klass.__dict__["NAMECOLR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_setbilevelimagecolor_has_AREA():
    assert hasattr(afpText_SetBiLevelImageColor, "AREA")
    descriptor = None
    for klass in afpText_SetBiLevelImageColor.__mro__:
        if "AREA" in klass.__dict__:
            descriptor = klass.__dict__["AREA"]
            break
    assert isinstance(descriptor, property)

def test_afptext_setbilevelimagecolor_has_Reserved():
    assert hasattr(afpText_SetBiLevelImageColor, "Reserved")
    descriptor = None
    for klass in afpText_SetBiLevelImageColor.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_objectareasize_is_not_abstract():
    assert not inspect.isabstract(afpText_ObjectAreaSize)


def test_afptext_objectareasize_constructor_exists():
    assert callable(afpText_ObjectAreaSize.__init__)


def test_afptext_objectareasize_constructor_args():
    sig = inspect.signature(afpText_ObjectAreaSize.__init__)
    params = list(sig.parameters.keys())
    assert "XoaSize" in params, "Missing parameter 'XoaSize'"
    assert "SizeType" in params, "Missing parameter 'SizeType'"
    assert "YoaSize" in params, "Missing parameter 'YoaSize'"

def test_afptext_objectareasize_has_XoaSize():
    assert hasattr(afpText_ObjectAreaSize, "XoaSize")
    descriptor = None
    for klass in afpText_ObjectAreaSize.__mro__:
        if "XoaSize" in klass.__dict__:
            descriptor = klass.__dict__["XoaSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectareasize_has_SizeType():
    assert hasattr(afpText_ObjectAreaSize, "SizeType")
    descriptor = None
    for klass in afpText_ObjectAreaSize.__mro__:
        if "SizeType" in klass.__dict__:
            descriptor = klass.__dict__["SizeType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_objectareasize_has_YoaSize():
    assert hasattr(afpText_ObjectAreaSize, "YoaSize")
    descriptor = None
    for klass in afpText_ObjectAreaSize.__mro__:
        if "YoaSize" in klass.__dict__:
            descriptor = klass.__dict__["YoaSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bln_is_not_abstract():
    assert not inspect.isabstract(afpText_BLN)


def test_afptext_bln_constructor_exists():
    assert callable(afpText_BLN.__init__)


def test_afptext_bln_constructor_args():
    sig = inspect.signature(afpText_BLN.__init__)
    params = list(sig.parameters.keys())



def test_afptext_gsmp_is_not_abstract():
    assert not inspect.isabstract(afpText_GSMP)


def test_afptext_gsmp_constructor_exists():
    assert callable(afpText_GSMP.__init__)


def test_afptext_gsmp_constructor_args():
    sig = inspect.signature(afpText_GSMP.__init__)
    params = list(sig.parameters.keys())
    assert "PREC" in params, "Missing parameter 'PREC'"

def test_afptext_gsmp_has_PREC():
    assert hasattr(afpText_GSMP, "PREC")
    descriptor = None
    for klass in afpText_GSMP.__mro__:
        if "PREC" in klass.__dict__:
            descriptor = klass.__dict__["PREC"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gsps_is_not_abstract():
    assert not inspect.isabstract(afpText_GSPS)


def test_afptext_gsps_constructor_exists():
    assert callable(afpText_GSPS.__init__)


def test_afptext_gsps_constructor_args():
    sig = inspect.signature(afpText_GSPS.__init__)
    params = list(sig.parameters.keys())
    assert "LCID" in params, "Missing parameter 'LCID'"

def test_afptext_gsps_has_LCID():
    assert hasattr(afpText_GSPS, "LCID")
    descriptor = None
    for klass in afpText_GSPS.__mro__:
        if "LCID" in klass.__dict__:
            descriptor = klass.__dict__["LCID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_amb_is_not_abstract():
    assert not inspect.isabstract(afpText_AMB)


def test_afptext_amb_constructor_exists():
    assert callable(afpText_AMB.__init__)


def test_afptext_amb_constructor_args():
    sig = inspect.signature(afpText_AMB.__init__)
    params = list(sig.parameters.keys())
    assert "DSPLCMNT" in params, "Missing parameter 'DSPLCMNT'"

def test_afptext_amb_has_DSPLCMNT():
    assert hasattr(afpText_AMB, "DSPLCMNT")
    descriptor = None
    for klass in afpText_AMB.__mro__:
        if "DSPLCMNT" in klass.__dict__:
            descriptor = klass.__dict__["DSPLCMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_svi_is_not_abstract():
    assert not inspect.isabstract(afpText_SVI)


def test_afptext_svi_constructor_exists():
    assert callable(afpText_SVI.__init__)


def test_afptext_svi_constructor_args():
    sig = inspect.signature(afpText_SVI.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext_svi_has_INCRMENT():
    assert hasattr(afpText_SVI, "INCRMENT")
    descriptor = None
    for klass in afpText_SVI.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_sto_is_not_abstract():
    assert not inspect.isabstract(afpText_STO)


def test_afptext_sto_constructor_exists():
    assert callable(afpText_STO.__init__)


def test_afptext_sto_constructor_args():
    sig = inspect.signature(afpText_STO.__init__)
    params = list(sig.parameters.keys())
    assert "IORNTION" in params, "Missing parameter 'IORNTION'"
    assert "BORNTION" in params, "Missing parameter 'BORNTION'"

def test_afptext_sto_has_IORNTION():
    assert hasattr(afpText_STO, "IORNTION")
    descriptor = None
    for klass in afpText_STO.__mro__:
        if "IORNTION" in klass.__dict__:
            descriptor = klass.__dict__["IORNTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sto_has_BORNTION():
    assert hasattr(afpText_STO, "BORNTION")
    descriptor = None
    for klass in afpText_STO.__mro__:
        if "BORNTION" in klass.__dict__:
            descriptor = klass.__dict__["BORNTION"]
            break
    assert isinstance(descriptor, property)



def test_afptext_stc_is_not_abstract():
    assert not inspect.isabstract(afpText_STC)


def test_afptext_stc_constructor_exists():
    assert callable(afpText_STC.__init__)


def test_afptext_stc_constructor_args():
    sig = inspect.signature(afpText_STC.__init__)
    params = list(sig.parameters.keys())
    assert "PRECSION" in params, "Missing parameter 'PRECSION'"
    assert "FRGCOLOR" in params, "Missing parameter 'FRGCOLOR'"

def test_afptext_stc_has_PRECSION():
    assert hasattr(afpText_STC, "PRECSION")
    descriptor = None
    for klass in afpText_STC.__mro__:
        if "PRECSION" in klass.__dict__:
            descriptor = klass.__dict__["PRECSION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_stc_has_FRGCOLOR():
    assert hasattr(afpText_STC, "FRGCOLOR")
    descriptor = None
    for klass in afpText_STC.__mro__:
        if "FRGCOLOR" in klass.__dict__:
            descriptor = klass.__dict__["FRGCOLOR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_sim_is_not_abstract():
    assert not inspect.isabstract(afpText_SIM)


def test_afptext_sim_constructor_exists():
    assert callable(afpText_SIM.__init__)


def test_afptext_sim_constructor_args():
    sig = inspect.signature(afpText_SIM.__init__)
    params = list(sig.parameters.keys())
    assert "DSPLCMNT" in params, "Missing parameter 'DSPLCMNT'"

def test_afptext_sim_has_DSPLCMNT():
    assert hasattr(afpText_SIM, "DSPLCMNT")
    descriptor = None
    for klass in afpText_SIM.__mro__:
        if "DSPLCMNT" in klass.__dict__:
            descriptor = klass.__dict__["DSPLCMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_sia_is_not_abstract():
    assert not inspect.isabstract(afpText_SIA)


def test_afptext_sia_constructor_exists():
    assert callable(afpText_SIA.__init__)


def test_afptext_sia_constructor_args():
    sig = inspect.signature(afpText_SIA.__init__)
    params = list(sig.parameters.keys())
    assert "DIRCTION" in params, "Missing parameter 'DIRCTION'"
    assert "ADJSTMNT" in params, "Missing parameter 'ADJSTMNT'"

def test_afptext_sia_has_DIRCTION():
    assert hasattr(afpText_SIA, "DIRCTION")
    descriptor = None
    for klass in afpText_SIA.__mro__:
        if "DIRCTION" in klass.__dict__:
            descriptor = klass.__dict__["DIRCTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sia_has_ADJSTMNT():
    assert hasattr(afpText_SIA, "ADJSTMNT")
    descriptor = None
    for klass in afpText_SIA.__mro__:
        if "ADJSTMNT" in klass.__dict__:
            descriptor = klass.__dict__["ADJSTMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_sec_is_not_abstract():
    assert not inspect.isabstract(afpText_SEC)


def test_afptext_sec_constructor_exists():
    assert callable(afpText_SEC.__init__)


def test_afptext_sec_constructor_args():
    sig = inspect.signature(afpText_SEC.__init__)
    params = list(sig.parameters.keys())
    assert "COLSIZE2" in params, "Missing parameter 'COLSIZE2'"
    assert "COLSIZE1" in params, "Missing parameter 'COLSIZE1'"
    assert "COLVALUE" in params, "Missing parameter 'COLVALUE'"
    assert "COLSIZE4" in params, "Missing parameter 'COLSIZE4'"
    assert "COLSPCE" in params, "Missing parameter 'COLSPCE'"
    assert "COLSIZE3" in params, "Missing parameter 'COLSIZE3'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"

def test_afptext_sec_has_COLSIZE2():
    assert hasattr(afpText_SEC, "COLSIZE2")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "COLSIZE2" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sec_has_COLSIZE1():
    assert hasattr(afpText_SEC, "COLSIZE1")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "COLSIZE1" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sec_has_COLVALUE():
    assert hasattr(afpText_SEC, "COLVALUE")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "COLVALUE" in klass.__dict__:
            descriptor = klass.__dict__["COLVALUE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sec_has_COLSIZE4():
    assert hasattr(afpText_SEC, "COLSIZE4")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "COLSIZE4" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sec_has_COLSPCE():
    assert hasattr(afpText_SEC, "COLSPCE")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "COLSPCE" in klass.__dict__:
            descriptor = klass.__dict__["COLSPCE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sec_has_COLSIZE3():
    assert hasattr(afpText_SEC, "COLSIZE3")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "COLSIZE3" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_sec_has_RESERVED():
    assert hasattr(afpText_SEC, "RESERVED")
    descriptor = None
    for klass in afpText_SEC.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)



def test_afptext_scfl_is_not_abstract():
    assert not inspect.isabstract(afpText_SCFL)


def test_afptext_scfl_constructor_exists():
    assert callable(afpText_SCFL.__init__)


def test_afptext_scfl_constructor_args():
    sig = inspect.signature(afpText_SCFL.__init__)
    params = list(sig.parameters.keys())
    assert "LID" in params, "Missing parameter 'LID'"

def test_afptext_scfl_has_LID():
    assert hasattr(afpText_SCFL, "LID")
    descriptor = None
    for klass in afpText_SCFL.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_sbi_is_not_abstract():
    assert not inspect.isabstract(afpText_SBI)


def test_afptext_sbi_constructor_exists():
    assert callable(afpText_SBI.__init__)


def test_afptext_sbi_constructor_args():
    sig = inspect.signature(afpText_SBI.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext_sbi_has_INCRMENT():
    assert hasattr(afpText_SBI, "INCRMENT")
    descriptor = None
    for klass in afpText_SBI.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_rps_is_not_abstract():
    assert not inspect.isabstract(afpText_RPS)


def test_afptext_rps_constructor_exists():
    assert callable(afpText_RPS.__init__)


def test_afptext_rps_constructor_args():
    sig = inspect.signature(afpText_RPS.__init__)
    params = list(sig.parameters.keys())
    assert "RPTDATA" in params, "Missing parameter 'RPTDATA'"
    assert "RLENGTH" in params, "Missing parameter 'RLENGTH'"

def test_afptext_rps_has_RPTDATA():
    assert hasattr(afpText_RPS, "RPTDATA")
    descriptor = None
    for klass in afpText_RPS.__mro__:
        if "RPTDATA" in klass.__dict__:
            descriptor = klass.__dict__["RPTDATA"]
            break
    assert isinstance(descriptor, property)

def test_afptext_rps_has_RLENGTH():
    assert hasattr(afpText_RPS, "RLENGTH")
    descriptor = None
    for klass in afpText_RPS.__mro__:
        if "RLENGTH" in klass.__dict__:
            descriptor = klass.__dict__["RLENGTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_rmi_is_not_abstract():
    assert not inspect.isabstract(afpText_RMI)


def test_afptext_rmi_constructor_exists():
    assert callable(afpText_RMI.__init__)


def test_afptext_rmi_constructor_args():
    sig = inspect.signature(afpText_RMI.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext_rmi_has_INCRMENT():
    assert hasattr(afpText_RMI, "INCRMENT")
    descriptor = None
    for klass in afpText_RMI.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_rmb_is_not_abstract():
    assert not inspect.isabstract(afpText_RMB)


def test_afptext_rmb_constructor_exists():
    assert callable(afpText_RMB.__init__)


def test_afptext_rmb_constructor_args():
    sig = inspect.signature(afpText_RMB.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext_rmb_has_INCRMENT():
    assert hasattr(afpText_RMB, "INCRMENT")
    descriptor = None
    for klass in afpText_RMB.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ovs_is_not_abstract():
    assert not inspect.isabstract(afpText_OVS)


def test_afptext_ovs_constructor_exists():
    assert callable(afpText_OVS.__init__)


def test_afptext_ovs_constructor_args():
    sig = inspect.signature(afpText_OVS.__init__)
    params = list(sig.parameters.keys())
    assert "BYPSIDEN" in params, "Missing parameter 'BYPSIDEN'"
    assert "OVERCHAR" in params, "Missing parameter 'OVERCHAR'"

def test_afptext_ovs_has_BYPSIDEN():
    assert hasattr(afpText_OVS, "BYPSIDEN")
    descriptor = None
    for klass in afpText_OVS.__mro__:
        if "BYPSIDEN" in klass.__dict__:
            descriptor = klass.__dict__["BYPSIDEN"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ovs_has_OVERCHAR():
    assert hasattr(afpText_OVS, "OVERCHAR")
    descriptor = None
    for klass in afpText_OVS.__mro__:
        if "OVERCHAR" in klass.__dict__:
            descriptor = klass.__dict__["OVERCHAR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_nopcs_is_not_abstract():
    assert not inspect.isabstract(afpText_NOPCS)


def test_afptext_nopcs_constructor_exists():
    assert callable(afpText_NOPCS.__init__)


def test_afptext_nopcs_constructor_args():
    sig = inspect.signature(afpText_NOPCS.__init__)
    params = list(sig.parameters.keys())
    assert "IGNDATA" in params, "Missing parameter 'IGNDATA'"

def test_afptext_nopcs_has_IGNDATA():
    assert hasattr(afpText_NOPCS, "IGNDATA")
    descriptor = None
    for klass in afpText_NOPCS.__mro__:
        if "IGNDATA" in klass.__dict__:
            descriptor = klass.__dict__["IGNDATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext_esu_is_not_abstract():
    assert not inspect.isabstract(afpText_ESU)


def test_afptext_esu_constructor_exists():
    assert callable(afpText_ESU.__init__)


def test_afptext_esu_constructor_args():
    sig = inspect.signature(afpText_ESU.__init__)
    params = list(sig.parameters.keys())
    assert "LID" in params, "Missing parameter 'LID'"

def test_afptext_esu_has_LID():
    assert hasattr(afpText_ESU, "LID")
    descriptor = None
    for klass in afpText_ESU.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_dir_is_not_abstract():
    assert not inspect.isabstract(afpText_DIR)


def test_afptext_dir_constructor_exists():
    assert callable(afpText_DIR.__init__)


def test_afptext_dir_constructor_args():
    sig = inspect.signature(afpText_DIR.__init__)
    params = list(sig.parameters.keys())
    assert "RWIDTH" in params, "Missing parameter 'RWIDTH'"
    assert "RWIDTHFRACTION" in params, "Missing parameter 'RWIDTHFRACTION'"
    assert "RLENGTH" in params, "Missing parameter 'RLENGTH'"

def test_afptext_dir_has_RWIDTH():
    assert hasattr(afpText_DIR, "RWIDTH")
    descriptor = None
    for klass in afpText_DIR.__mro__:
        if "RWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dir_has_RWIDTHFRACTION():
    assert hasattr(afpText_DIR, "RWIDTHFRACTION")
    descriptor = None
    for klass in afpText_DIR.__mro__:
        if "RWIDTHFRACTION" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTHFRACTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dir_has_RLENGTH():
    assert hasattr(afpText_DIR, "RLENGTH")
    descriptor = None
    for klass in afpText_DIR.__mro__:
        if "RLENGTH" in klass.__dict__:
            descriptor = klass.__dict__["RLENGTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_dbr_is_not_abstract():
    assert not inspect.isabstract(afpText_DBR)


def test_afptext_dbr_constructor_exists():
    assert callable(afpText_DBR.__init__)


def test_afptext_dbr_constructor_args():
    sig = inspect.signature(afpText_DBR.__init__)
    params = list(sig.parameters.keys())
    assert "RWIDTHFRACTION" in params, "Missing parameter 'RWIDTHFRACTION'"
    assert "RLENGTH" in params, "Missing parameter 'RLENGTH'"
    assert "RWIDTH" in params, "Missing parameter 'RWIDTH'"

def test_afptext_dbr_has_RWIDTHFRACTION():
    assert hasattr(afpText_DBR, "RWIDTHFRACTION")
    descriptor = None
    for klass in afpText_DBR.__mro__:
        if "RWIDTHFRACTION" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTHFRACTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dbr_has_RLENGTH():
    assert hasattr(afpText_DBR, "RLENGTH")
    descriptor = None
    for klass in afpText_DBR.__mro__:
        if "RLENGTH" in klass.__dict__:
            descriptor = klass.__dict__["RLENGTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_dbr_has_RWIDTH():
    assert hasattr(afpText_DBR, "RWIDTH")
    descriptor = None
    for klass in afpText_DBR.__mro__:
        if "RWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcrlinerg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCRLINERG)


def test_afptext_gcrlinerg_constructor_exists():
    assert callable(afpText_GCRLINERG.__init__)


def test_afptext_gcrlinerg_constructor_args():
    sig = inspect.signature(afpText_GCRLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YOFFS" in params, "Missing parameter 'YOFFS'"
    assert "XOSSF" in params, "Missing parameter 'XOSSF'"

def test_afptext_gcrlinerg_has_YOFFS():
    assert hasattr(afpText_GCRLINERG, "YOFFS")
    descriptor = None
    for klass in afpText_GCRLINERG.__mro__:
        if "YOFFS" in klass.__dict__:
            descriptor = klass.__dict__["YOFFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcrlinerg_has_XOSSF():
    assert hasattr(afpText_GCRLINERG, "XOSSF")
    descriptor = None
    for klass in afpText_GCRLINERG.__mro__:
        if "XOSSF" in klass.__dict__:
            descriptor = klass.__dict__["XOSSF"]
            break
    assert isinstance(descriptor, property)



def test_afptext_grlinerg_is_not_abstract():
    assert not inspect.isabstract(afpText_GRLINERG)


def test_afptext_grlinerg_constructor_exists():
    assert callable(afpText_GRLINERG.__init__)


def test_afptext_grlinerg_constructor_args():
    sig = inspect.signature(afpText_GRLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YOFFS" in params, "Missing parameter 'YOFFS'"
    assert "XOSSF" in params, "Missing parameter 'XOSSF'"

def test_afptext_grlinerg_has_YOFFS():
    assert hasattr(afpText_GRLINERG, "YOFFS")
    descriptor = None
    for klass in afpText_GRLINERG.__mro__:
        if "YOFFS" in klass.__dict__:
            descriptor = klass.__dict__["YOFFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_grlinerg_has_XOSSF():
    assert hasattr(afpText_GRLINERG, "XOSSF")
    descriptor = None
    for klass in afpText_GRLINERG.__mro__:
        if "XOSSF" in klass.__dict__:
            descriptor = klass.__dict__["XOSSF"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcmrkrg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCMRKRG)


def test_afptext_gcmrkrg_constructor_exists():
    assert callable(afpText_GCMRKRG.__init__)


def test_afptext_gcmrkrg_constructor_args():
    sig = inspect.signature(afpText_GCMRKRG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext_gcmrkrg_has_XPOS():
    assert hasattr(afpText_GCMRKRG, "XPOS")
    descriptor = None
    for klass in afpText_GCMRKRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcmrkrg_has_YPOS():
    assert hasattr(afpText_GCMRKRG, "YPOS")
    descriptor = None
    for klass in afpText_GCMRKRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gmrkrg_is_not_abstract():
    assert not inspect.isabstract(afpText_GMRKRG)


def test_afptext_gmrkrg_constructor_exists():
    assert callable(afpText_GMRKRG.__init__)


def test_afptext_gmrkrg_constructor_args():
    sig = inspect.signature(afpText_GMRKRG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext_gmrkrg_has_XPOS():
    assert hasattr(afpText_GMRKRG, "XPOS")
    descriptor = None
    for klass in afpText_GMRKRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gmrkrg_has_YPOS():
    assert hasattr(afpText_GMRKRG, "YPOS")
    descriptor = None
    for klass in afpText_GMRKRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gclinerg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCLINERG)


def test_afptext_gclinerg_constructor_exists():
    assert callable(afpText_GCLINERG.__init__)


def test_afptext_gclinerg_constructor_args():
    sig = inspect.signature(afpText_GCLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gclinerg_has_YPOS():
    assert hasattr(afpText_GCLINERG, "YPOS")
    descriptor = None
    for klass in afpText_GCLINERG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gclinerg_has_XPOS():
    assert hasattr(afpText_GCLINERG, "XPOS")
    descriptor = None
    for klass in afpText_GCLINERG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_glinerg_is_not_abstract():
    assert not inspect.isabstract(afpText_GLINERG)


def test_afptext_glinerg_constructor_exists():
    assert callable(afpText_GLINERG.__init__)


def test_afptext_glinerg_constructor_args():
    sig = inspect.signature(afpText_GLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_glinerg_has_YPOS():
    assert hasattr(afpText_GLINERG, "YPOS")
    descriptor = None
    for klass in afpText_GLINERG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_glinerg_has_XPOS():
    assert hasattr(afpText_GLINERG, "XPOS")
    descriptor = None
    for klass in afpText_GLINERG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcfltrg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCFLTRG)


def test_afptext_gcfltrg_constructor_exists():
    assert callable(afpText_GCFLTRG.__init__)


def test_afptext_gcfltrg_constructor_args():
    sig = inspect.signature(afpText_GCFLTRG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext_gcfltrg_has_XPOS():
    assert hasattr(afpText_GCFLTRG, "XPOS")
    descriptor = None
    for klass in afpText_GCFLTRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcfltrg_has_YPOS():
    assert hasattr(afpText_GCFLTRG, "YPOS")
    descriptor = None
    for klass in afpText_GCFLTRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gfltrg_is_not_abstract():
    assert not inspect.isabstract(afpText_GFLTRG)


def test_afptext_gfltrg_constructor_exists():
    assert callable(afpText_GFLTRG.__init__)


def test_afptext_gfltrg_constructor_args():
    sig = inspect.signature(afpText_GFLTRG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext_gfltrg_has_XPOS():
    assert hasattr(afpText_GFLTRG, "XPOS")
    descriptor = None
    for klass in afpText_GFLTRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gfltrg_has_YPOS():
    assert hasattr(afpText_GFLTRG, "YPOS")
    descriptor = None
    for klass in afpText_GFLTRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gccbezrg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCCBEZRG)


def test_afptext_gccbezrg_constructor_exists():
    assert callable(afpText_GCCBEZRG.__init__)


def test_afptext_gccbezrg_constructor_args():
    sig = inspect.signature(afpText_GCCBEZRG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gccbezrg_has_YPOS():
    assert hasattr(afpText_GCCBEZRG, "YPOS")
    descriptor = None
    for klass in afpText_GCCBEZRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gccbezrg_has_XPOS():
    assert hasattr(afpText_GCCBEZRG, "XPOS")
    descriptor = None
    for klass in afpText_GCCBEZRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gcbezrg_is_not_abstract():
    assert not inspect.isabstract(afpText_GCBEZRG)


def test_afptext_gcbezrg_constructor_exists():
    assert callable(afpText_GCBEZRG.__init__)


def test_afptext_gcbezrg_constructor_args():
    sig = inspect.signature(afpText_GCBEZRG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext_gcbezrg_has_YPOS():
    assert hasattr(afpText_GCBEZRG, "YPOS")
    descriptor = None
    for klass in afpText_GCBEZRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_gcbezrg_has_XPOS():
    assert hasattr(afpText_GCBEZRG, "XPOS")
    descriptor = None
    for klass in afpText_GCBEZRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnnrg_is_not_abstract():
    assert not inspect.isabstract(afpText_FNNRG)


def test_afptext_fnnrg_constructor_exists():
    assert callable(afpText_FNNRG.__init__)


def test_afptext_fnnrg_constructor_args():
    sig = inspect.signature(afpText_FNNRG.__init__)
    params = list(sig.parameters.keys())
    assert "TSOffset" in params, "Missing parameter 'TSOffset'"
    assert "GCGID" in params, "Missing parameter 'GCGID'"

def test_afptext_fnnrg_has_TSOffset():
    assert hasattr(afpText_FNNRG, "TSOffset")
    descriptor = None
    for klass in afpText_FNNRG.__mro__:
        if "TSOffset" in klass.__dict__:
            descriptor = klass.__dict__["TSOffset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnnrg_has_GCGID():
    assert hasattr(afpText_FNNRG, "GCGID")
    descriptor = None
    for klass in afpText_FNNRG.__mro__:
        if "GCGID" in klass.__dict__:
            descriptor = klass.__dict__["GCGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_externalalgorithmrg_is_not_abstract():
    assert not inspect.isabstract(afpText_ExternalAlgorithmRG)


def test_afptext_externalalgorithmrg_constructor_exists():
    assert callable(afpText_ExternalAlgorithmRG.__init__)


def test_afptext_externalalgorithmrg_constructor_args():
    sig = inspect.signature(afpText_ExternalAlgorithmRG.__init__)
    params = list(sig.parameters.keys())
    assert "DIRCTN" in params, "Missing parameter 'DIRCTN'"
    assert "PADBDRY" in params, "Missing parameter 'PADBDRY'"
    assert "PADALMT" in params, "Missing parameter 'PADALMT'"

def test_afptext_externalalgorithmrg_has_DIRCTN():
    assert hasattr(afpText_ExternalAlgorithmRG, "DIRCTN")
    descriptor = None
    for klass in afpText_ExternalAlgorithmRG.__mro__:
        if "DIRCTN" in klass.__dict__:
            descriptor = klass.__dict__["DIRCTN"]
            break
    assert isinstance(descriptor, property)

def test_afptext_externalalgorithmrg_has_PADBDRY():
    assert hasattr(afpText_ExternalAlgorithmRG, "PADBDRY")
    descriptor = None
    for klass in afpText_ExternalAlgorithmRG.__mro__:
        if "PADBDRY" in klass.__dict__:
            descriptor = klass.__dict__["PADBDRY"]
            break
    assert isinstance(descriptor, property)

def test_afptext_externalalgorithmrg_has_PADALMT():
    assert hasattr(afpText_ExternalAlgorithmRG, "PADALMT")
    descriptor = None
    for klass in afpText_ExternalAlgorithmRG.__mro__:
        if "PADALMT" in klass.__dict__:
            descriptor = klass.__dict__["PADALMT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_samplingratiosrg_is_not_abstract():
    assert not inspect.isabstract(afpText_SamplingRatiosRG)


def test_afptext_samplingratiosrg_constructor_exists():
    assert callable(afpText_SamplingRatiosRG.__init__)


def test_afptext_samplingratiosrg_constructor_args():
    sig = inspect.signature(afpText_SamplingRatiosRG.__init__)
    params = list(sig.parameters.keys())
    assert "HSAMPLE" in params, "Missing parameter 'HSAMPLE'"
    assert "VSAMPLE" in params, "Missing parameter 'VSAMPLE'"

def test_afptext_samplingratiosrg_has_HSAMPLE():
    assert hasattr(afpText_SamplingRatiosRG, "HSAMPLE")
    descriptor = None
    for klass in afpText_SamplingRatiosRG.__mro__:
        if "HSAMPLE" in klass.__dict__:
            descriptor = klass.__dict__["HSAMPLE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_samplingratiosrg_has_VSAMPLE():
    assert hasattr(afpText_SamplingRatiosRG, "VSAMPLE")
    descriptor = None
    for klass in afpText_SamplingRatiosRG.__mro__:
        if "VSAMPLE" in klass.__dict__:
            descriptor = klass.__dict__["VSAMPLE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tiletocrg_is_not_abstract():
    assert not inspect.isabstract(afpText_TileTOCRG)


def test_afptext_tiletocrg_constructor_exists():
    assert callable(afpText_TileTOCRG.__init__)


def test_afptext_tiletocrg_constructor_args():
    sig = inspect.signature(afpText_TileTOCRG.__init__)
    params = list(sig.parameters.keys())
    assert "RELRES" in params, "Missing parameter 'RELRES'"
    assert "YOFFSET" in params, "Missing parameter 'YOFFSET'"
    assert "XOFFSET" in params, "Missing parameter 'XOFFSET'"
    assert "TVSIZE" in params, "Missing parameter 'TVSIZE'"
    assert "COMPR" in params, "Missing parameter 'COMPR'"
    assert "DATAPOS" in params, "Missing parameter 'DATAPOS'"
    assert "THSIZE" in params, "Missing parameter 'THSIZE'"

def test_afptext_tiletocrg_has_RELRES():
    assert hasattr(afpText_TileTOCRG, "RELRES")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "RELRES" in klass.__dict__:
            descriptor = klass.__dict__["RELRES"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tiletocrg_has_YOFFSET():
    assert hasattr(afpText_TileTOCRG, "YOFFSET")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "YOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["YOFFSET"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tiletocrg_has_XOFFSET():
    assert hasattr(afpText_TileTOCRG, "XOFFSET")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "XOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["XOFFSET"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tiletocrg_has_TVSIZE():
    assert hasattr(afpText_TileTOCRG, "TVSIZE")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "TVSIZE" in klass.__dict__:
            descriptor = klass.__dict__["TVSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tiletocrg_has_COMPR():
    assert hasattr(afpText_TileTOCRG, "COMPR")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "COMPR" in klass.__dict__:
            descriptor = klass.__dict__["COMPR"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tiletocrg_has_DATAPOS():
    assert hasattr(afpText_TileTOCRG, "DATAPOS")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "DATAPOS" in klass.__dict__:
            descriptor = klass.__dict__["DATAPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext_tiletocrg_has_THSIZE():
    assert hasattr(afpText_TileTOCRG, "THSIZE")
    descriptor = None
    for klass in afpText_TileTOCRG.__mro__:
        if "THSIZE" in klass.__dict__:
            descriptor = klass.__dict__["THSIZE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bandimagerg_is_not_abstract():
    assert not inspect.isabstract(afpText_BandImageRG)


def test_afptext_bandimagerg_constructor_exists():
    assert callable(afpText_BandImageRG.__init__)


def test_afptext_bandimagerg_constructor_args():
    sig = inspect.signature(afpText_BandImageRG.__init__)
    params = list(sig.parameters.keys())
    assert "BITCNT" in params, "Missing parameter 'BITCNT'"

def test_afptext_bandimagerg_has_BITCNT():
    assert hasattr(afpText_BandImageRG, "BITCNT")
    descriptor = None
    for klass in afpText_BandImageRG.__mro__:
        if "BITCNT" in klass.__dict__:
            descriptor = klass.__dict__["BITCNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pporg_is_not_abstract():
    assert not inspect.isabstract(afpText_PPORG)


def test_afptext_pporg_constructor_exists():
    assert callable(afpText_PPORG.__init__)


def test_afptext_pporg_constructor_args():
    sig = inspect.signature(afpText_PPORG.__init__)
    params = list(sig.parameters.keys())
    assert "XocaOset" in params, "Missing parameter 'XocaOset'"
    assert "YocaOset" in params, "Missing parameter 'YocaOset'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "ProcFlgs" in params, "Missing parameter 'ProcFlgs'"

def test_afptext_pporg_has_XocaOset():
    assert hasattr(afpText_PPORG, "XocaOset")
    descriptor = None
    for klass in afpText_PPORG.__mro__:
        if "XocaOset" in klass.__dict__:
            descriptor = klass.__dict__["XocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pporg_has_YocaOset():
    assert hasattr(afpText_PPORG, "YocaOset")
    descriptor = None
    for klass in afpText_PPORG.__mro__:
        if "YocaOset" in klass.__dict__:
            descriptor = klass.__dict__["YocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pporg_has_ObjType():
    assert hasattr(afpText_PPORG, "ObjType")
    descriptor = None
    for klass in afpText_PPORG.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pporg_has_RGLength():
    assert hasattr(afpText_PPORG, "RGLength")
    descriptor = None
    for klass in afpText_PPORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pporg_has_ProcFlgs():
    assert hasattr(afpText_PPORG, "ProcFlgs")
    descriptor = None
    for klass in afpText_PPORG.__mro__:
        if "ProcFlgs" in klass.__dict__:
            descriptor = klass.__dict__["ProcFlgs"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pgprg_is_not_abstract():
    assert not inspect.isabstract(afpText_PGPRG)


def test_afptext_pgprg_constructor_exists():
    assert callable(afpText_PGPRG.__init__)


def test_afptext_pgprg_constructor_args():
    sig = inspect.signature(afpText_PGPRG.__init__)
    params = list(sig.parameters.keys())
    assert "PGorient" in params, "Missing parameter 'PGorient'"
    assert "PMCid" in params, "Missing parameter 'PMCid'"
    assert "SHside" in params, "Missing parameter 'SHside'"
    assert "PgFlgs" in params, "Missing parameter 'PgFlgs'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "XmOset" in params, "Missing parameter 'XmOset'"
    assert "YmOset" in params, "Missing parameter 'YmOset'"

def test_afptext_pgprg_has_PGorient():
    assert hasattr(afpText_PGPRG, "PGorient")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "PGorient" in klass.__dict__:
            descriptor = klass.__dict__["PGorient"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgprg_has_PMCid():
    assert hasattr(afpText_PGPRG, "PMCid")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "PMCid" in klass.__dict__:
            descriptor = klass.__dict__["PMCid"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgprg_has_SHside():
    assert hasattr(afpText_PGPRG, "SHside")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "SHside" in klass.__dict__:
            descriptor = klass.__dict__["SHside"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgprg_has_PgFlgs():
    assert hasattr(afpText_PGPRG, "PgFlgs")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "PgFlgs" in klass.__dict__:
            descriptor = klass.__dict__["PgFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgprg_has_RGLength():
    assert hasattr(afpText_PGPRG, "RGLength")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgprg_has_XmOset():
    assert hasattr(afpText_PGPRG, "XmOset")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "XmOset" in klass.__dict__:
            descriptor = klass.__dict__["XmOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgprg_has_YmOset():
    assert hasattr(afpText_PGPRG, "YmOset")
    descriptor = None
    for klass in afpText_PGPRG.__mro__:
        if "YmOset" in klass.__dict__:
            descriptor = klass.__dict__["YmOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_msurg_is_not_abstract():
    assert not inspect.isabstract(afpText_MSURG)


def test_afptext_msurg_constructor_exists():
    assert callable(afpText_MSURG.__init__)


def test_afptext_msurg_constructor_args():
    sig = inspect.signature(afpText_MSURG.__init__)
    params = list(sig.parameters.keys())
    assert "SUPid" in params, "Missing parameter 'SUPid'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "SUPname" in params, "Missing parameter 'SUPname'"

def test_afptext_msurg_has_SUPid():
    assert hasattr(afpText_MSURG, "SUPid")
    descriptor = None
    for klass in afpText_MSURG.__mro__:
        if "SUPid" in klass.__dict__:
            descriptor = klass.__dict__["SUPid"]
            break
    assert isinstance(descriptor, property)

def test_afptext_msurg_has_Reserved():
    assert hasattr(afpText_MSURG, "Reserved")
    descriptor = None
    for klass in afpText_MSURG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_msurg_has_SUPname():
    assert hasattr(afpText_MSURG, "SUPname")
    descriptor = None
    for klass in afpText_MSURG.__mro__:
        if "SUPname" in klass.__dict__:
            descriptor = klass.__dict__["SUPname"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mpsrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MPSRG)


def test_afptext_mpsrg_constructor_exists():
    assert callable(afpText_MPSRG.__init__)


def test_afptext_mpsrg_constructor_args():
    sig = inspect.signature(afpText_MPSRG.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext_mpsrg_has_Reserved():
    assert hasattr(afpText_MPSRG, "Reserved")
    descriptor = None
    for klass in afpText_MPSRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mpsrg_has_PsegName():
    assert hasattr(afpText_MPSRG, "PsegName")
    descriptor = None
    for klass in afpText_MPSRG.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mporg_is_not_abstract():
    assert not inspect.isabstract(afpText_MPORG)


def test_afptext_mporg_constructor_exists():
    assert callable(afpText_MPORG.__init__)


def test_afptext_mporg_constructor_args():
    sig = inspect.signature(afpText_MPORG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mporg_has_RGLength():
    assert hasattr(afpText_MPORG, "RGLength")
    descriptor = None
    for klass in afpText_MPORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mpgrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MPGRG)


def test_afptext_mpgrg_constructor_exists():
    assert callable(afpText_MPGRG.__init__)


def test_afptext_mpgrg_constructor_args():
    sig = inspect.signature(afpText_MPGRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mpgrg_has_RGLength():
    assert hasattr(afpText_MPGRG, "RGLength")
    descriptor = None
    for klass in afpText_MPGRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mmtrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MMTRG)


def test_afptext_mmtrg_constructor_exists():
    assert callable(afpText_MMTRG.__init__)


def test_afptext_mmtrg_constructor_args():
    sig = inspect.signature(afpText_MMTRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mmtrg_has_RGLength():
    assert hasattr(afpText_MMTRG, "RGLength")
    descriptor = None
    for klass in afpText_MMTRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mmorg_is_not_abstract():
    assert not inspect.isabstract(afpText_MMORG)


def test_afptext_mmorg_constructor_exists():
    assert callable(afpText_MMORG.__init__)


def test_afptext_mmorg_constructor_args():
    sig = inspect.signature(afpText_MMORG.__init__)
    params = list(sig.parameters.keys())
    assert "OVLid" in params, "Missing parameter 'OVLid'"
    assert "OVLname" in params, "Missing parameter 'OVLname'"
    assert "Flags" in params, "Missing parameter 'Flags'"

def test_afptext_mmorg_has_OVLid():
    assert hasattr(afpText_MMORG, "OVLid")
    descriptor = None
    for klass in afpText_MMORG.__mro__:
        if "OVLid" in klass.__dict__:
            descriptor = klass.__dict__["OVLid"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mmorg_has_OVLname():
    assert hasattr(afpText_MMORG, "OVLname")
    descriptor = None
    for klass in afpText_MMORG.__mro__:
        if "OVLname" in klass.__dict__:
            descriptor = klass.__dict__["OVLname"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mmorg_has_Flags():
    assert hasattr(afpText_MMORG, "Flags")
    descriptor = None
    for klass in afpText_MMORG.__mro__:
        if "Flags" in klass.__dict__:
            descriptor = klass.__dict__["Flags"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mmdrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MMDRG)


def test_afptext_mmdrg_constructor_exists():
    assert callable(afpText_MMDRG.__init__)


def test_afptext_mmdrg_constructor_args():
    sig = inspect.signature(afpText_MMDRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mmdrg_has_RGLength():
    assert hasattr(afpText_MMDRG, "RGLength")
    descriptor = None
    for klass in afpText_MMDRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mmcrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MMCRG)


def test_afptext_mmcrg_constructor_exists():
    assert callable(afpText_MMCRG.__init__)


def test_afptext_mmcrg_constructor_args():
    sig = inspect.signature(afpText_MMCRG.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_afptext_mmcrg_has_key():
    assert hasattr(afpText_MMCRG, "key")
    descriptor = None
    for klass in afpText_MMCRG.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mmcrg_has_value():
    assert hasattr(afpText_MMCRG, "value")
    descriptor = None
    for klass in afpText_MMCRG.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_afptext_miorg_is_not_abstract():
    assert not inspect.isabstract(afpText_MIORG)


def test_afptext_miorg_constructor_exists():
    assert callable(afpText_MIORG.__init__)


def test_afptext_miorg_constructor_args():
    sig = inspect.signature(afpText_MIORG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_miorg_has_RGLength():
    assert hasattr(afpText_MIORG, "RGLength")
    descriptor = None
    for klass in afpText_MIORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mgorg_is_not_abstract():
    assert not inspect.isabstract(afpText_MGORG)


def test_afptext_mgorg_constructor_exists():
    assert callable(afpText_MGORG.__init__)


def test_afptext_mgorg_constructor_args():
    sig = inspect.signature(afpText_MGORG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mgorg_has_RGLength():
    assert hasattr(afpText_MGORG, "RGLength")
    descriptor = None
    for klass in afpText_MGORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mcarg_is_not_abstract():
    assert not inspect.isabstract(afpText_MCARG)


def test_afptext_mcarg_constructor_exists():
    assert callable(afpText_MCARG.__init__)


def test_afptext_mcarg_constructor_args():
    sig = inspect.signature(afpText_MCARG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mcarg_has_RGLength():
    assert hasattr(afpText_MCARG, "RGLength")
    descriptor = None
    for klass in afpText_MCARG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mdrrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MDRRG)


def test_afptext_mdrrg_constructor_exists():
    assert callable(afpText_MDRRG.__init__)


def test_afptext_mdrrg_constructor_args():
    sig = inspect.signature(afpText_MDRRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mdrrg_has_RGLength():
    assert hasattr(afpText_MDRRG, "RGLength")
    descriptor = None
    for klass in afpText_MDRRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mcf1rg_is_not_abstract():
    assert not inspect.isabstract(afpText_MCF1RG)


def test_afptext_mcf1rg_constructor_exists():
    assert callable(afpText_MCF1RG.__init__)


def test_afptext_mcf1rg_constructor_args():
    sig = inspect.signature(afpText_MCF1RG.__init__)
    params = list(sig.parameters.keys())
    assert "FCSName" in params, "Missing parameter 'FCSName'"
    assert "CPName" in params, "Missing parameter 'CPName'"
    assert "CFLid" in params, "Missing parameter 'CFLid'"
    assert "CFName" in params, "Missing parameter 'CFName'"
    assert "CharRot" in params, "Missing parameter 'CharRot'"
    assert "Sectid" in params, "Missing parameter 'Sectid'"

def test_afptext_mcf1rg_has_FCSName():
    assert hasattr(afpText_MCF1RG, "FCSName")
    descriptor = None
    for klass in afpText_MCF1RG.__mro__:
        if "FCSName" in klass.__dict__:
            descriptor = klass.__dict__["FCSName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mcf1rg_has_CPName():
    assert hasattr(afpText_MCF1RG, "CPName")
    descriptor = None
    for klass in afpText_MCF1RG.__mro__:
        if "CPName" in klass.__dict__:
            descriptor = klass.__dict__["CPName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mcf1rg_has_CFLid():
    assert hasattr(afpText_MCF1RG, "CFLid")
    descriptor = None
    for klass in afpText_MCF1RG.__mro__:
        if "CFLid" in klass.__dict__:
            descriptor = klass.__dict__["CFLid"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mcf1rg_has_CFName():
    assert hasattr(afpText_MCF1RG, "CFName")
    descriptor = None
    for klass in afpText_MCF1RG.__mro__:
        if "CFName" in klass.__dict__:
            descriptor = klass.__dict__["CFName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mcf1rg_has_CharRot():
    assert hasattr(afpText_MCF1RG, "CharRot")
    descriptor = None
    for klass in afpText_MCF1RG.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mcf1rg_has_Sectid():
    assert hasattr(afpText_MCF1RG, "Sectid")
    descriptor = None
    for klass in afpText_MCF1RG.__mro__:
        if "Sectid" in klass.__dict__:
            descriptor = klass.__dict__["Sectid"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mcfrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MCFRG)


def test_afptext_mcfrg_constructor_exists():
    assert callable(afpText_MCFRG.__init__)


def test_afptext_mcfrg_constructor_args():
    sig = inspect.signature(afpText_MCFRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mcfrg_has_RGLength():
    assert hasattr(afpText_MCFRG, "RGLength")
    descriptor = None
    for klass in afpText_MCFRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mcdrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MCDRG)


def test_afptext_mcdrg_constructor_exists():
    assert callable(afpText_MCDRG.__init__)


def test_afptext_mcdrg_constructor_args():
    sig = inspect.signature(afpText_MCDRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mcdrg_has_RGLength():
    assert hasattr(afpText_MCDRG, "RGLength")
    descriptor = None
    for klass in afpText_MCDRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mccrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MCCRG)


def test_afptext_mccrg_constructor_exists():
    assert callable(afpText_MCCRG.__init__)


def test_afptext_mccrg_constructor_args():
    sig = inspect.signature(afpText_MCCRG.__init__)
    params = list(sig.parameters.keys())
    assert "MMCid" in params, "Missing parameter 'MMCid'"
    assert "Stopnum" in params, "Missing parameter 'Stopnum'"
    assert "Startnum" in params, "Missing parameter 'Startnum'"

def test_afptext_mccrg_has_MMCid():
    assert hasattr(afpText_MCCRG, "MMCid")
    descriptor = None
    for klass in afpText_MCCRG.__mro__:
        if "MMCid" in klass.__dict__:
            descriptor = klass.__dict__["MMCid"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mccrg_has_Stopnum():
    assert hasattr(afpText_MCCRG, "Stopnum")
    descriptor = None
    for klass in afpText_MCCRG.__mro__:
        if "Stopnum" in klass.__dict__:
            descriptor = klass.__dict__["Stopnum"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mccrg_has_Startnum():
    assert hasattr(afpText_MCCRG, "Startnum")
    descriptor = None
    for klass in afpText_MCCRG.__mro__:
        if "Startnum" in klass.__dict__:
            descriptor = klass.__dict__["Startnum"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mbcrg_is_not_abstract():
    assert not inspect.isabstract(afpText_MBCRG)


def test_afptext_mbcrg_constructor_exists():
    assert callable(afpText_MBCRG.__init__)


def test_afptext_mbcrg_constructor_args():
    sig = inspect.signature(afpText_MBCRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mbcrg_has_RGLength():
    assert hasattr(afpText_MBCRG, "RGLength")
    descriptor = None
    for klass in afpText_MBCRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_llerg_is_not_abstract():
    assert not inspect.isabstract(afpText_LLERG)


def test_afptext_llerg_constructor_exists():
    assert callable(afpText_LLERG.__init__)


def test_afptext_llerg_constructor_args():
    sig = inspect.signature(afpText_LLERG.__init__)
    params = list(sig.parameters.keys())
    assert "RGFunct" in params, "Missing parameter 'RGFunct'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_llerg_has_RGFunct():
    assert hasattr(afpText_LLERG, "RGFunct")
    descriptor = None
    for klass in afpText_LLERG.__mro__:
        if "RGFunct" in klass.__dict__:
            descriptor = klass.__dict__["RGFunct"]
            break
    assert isinstance(descriptor, property)

def test_afptext_llerg_has_RGLength():
    assert hasattr(afpText_LLERG, "RGLength")
    descriptor = None
    for klass in afpText_LLERG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cpirg_is_not_abstract():
    assert not inspect.isabstract(afpText_CPIRG)


def test_afptext_cpirg_constructor_exists():
    assert callable(afpText_CPIRG.__init__)


def test_afptext_cpirg_constructor_args():
    sig = inspect.signature(afpText_CPIRG.__init__)
    params = list(sig.parameters.keys())
    assert "GCGID" in params, "Missing parameter 'GCGID'"
    assert "CodePoint" in params, "Missing parameter 'CodePoint'"
    assert "Count" in params, "Missing parameter 'Count'"
    assert "PrtFlags" in params, "Missing parameter 'PrtFlags'"

def test_afptext_cpirg_has_GCGID():
    assert hasattr(afpText_CPIRG, "GCGID")
    descriptor = None
    for klass in afpText_CPIRG.__mro__:
        if "GCGID" in klass.__dict__:
            descriptor = klass.__dict__["GCGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpirg_has_CodePoint():
    assert hasattr(afpText_CPIRG, "CodePoint")
    descriptor = None
    for klass in afpText_CPIRG.__mro__:
        if "CodePoint" in klass.__dict__:
            descriptor = klass.__dict__["CodePoint"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpirg_has_Count():
    assert hasattr(afpText_CPIRG, "Count")
    descriptor = None
    for klass in afpText_CPIRG.__mro__:
        if "Count" in klass.__dict__:
            descriptor = klass.__dict__["Count"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpirg_has_PrtFlags():
    assert hasattr(afpText_CPIRG, "PrtFlags")
    descriptor = None
    for klass in afpText_CPIRG.__mro__:
        if "PrtFlags" in klass.__dict__:
            descriptor = klass.__dict__["PrtFlags"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cfirg_is_not_abstract():
    assert not inspect.isabstract(afpText_CFIRG)


def test_afptext_cfirg_constructor_exists():
    assert callable(afpText_CFIRG.__init__)


def test_afptext_cfirg_constructor_args():
    sig = inspect.signature(afpText_CFIRG.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "CPName" in params, "Missing parameter 'CPName'"
    assert "SHScale" in params, "Missing parameter 'SHScale'"
    assert "FCSName" in params, "Missing parameter 'FCSName'"
    assert "Section" in params, "Missing parameter 'Section'"
    assert "SVSize" in params, "Missing parameter 'SVSize'"

def test_afptext_cfirg_has_Reserved():
    assert hasattr(afpText_CFIRG, "Reserved")
    descriptor = None
    for klass in afpText_CFIRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cfirg_has_CPName():
    assert hasattr(afpText_CFIRG, "CPName")
    descriptor = None
    for klass in afpText_CFIRG.__mro__:
        if "CPName" in klass.__dict__:
            descriptor = klass.__dict__["CPName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cfirg_has_SHScale():
    assert hasattr(afpText_CFIRG, "SHScale")
    descriptor = None
    for klass in afpText_CFIRG.__mro__:
        if "SHScale" in klass.__dict__:
            descriptor = klass.__dict__["SHScale"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cfirg_has_FCSName():
    assert hasattr(afpText_CFIRG, "FCSName")
    descriptor = None
    for klass in afpText_CFIRG.__mro__:
        if "FCSName" in klass.__dict__:
            descriptor = klass.__dict__["FCSName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cfirg_has_Section():
    assert hasattr(afpText_CFIRG, "Section")
    descriptor = None
    for klass in afpText_CFIRG.__mro__:
        if "Section" in klass.__dict__:
            descriptor = klass.__dict__["Section"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cfirg_has_SVSize():
    assert hasattr(afpText_CFIRG, "SVSize")
    descriptor = None
    for klass in afpText_CFIRG.__mro__:
        if "SVSize" in klass.__dict__:
            descriptor = klass.__dict__["SVSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext_triplet_is_not_abstract():
    assert not inspect.isabstract(afpText_triplet)


def test_afptext_triplet_constructor_exists():
    assert callable(afpText_triplet.__init__)


def test_afptext_triplet_constructor_args():
    sig = inspect.signature(afpText_triplet.__init__)
    params = list(sig.parameters.keys())



def test_structuredfield_is_not_abstract():
    assert not inspect.isabstract(structuredField)


def test_structuredfield_constructor_exists():
    assert callable(structuredField.__init__)


def test_structuredfield_constructor_args():
    sig = inspect.signature(structuredField.__init__)
    params = list(sig.parameters.keys())



def test_afptext_pgp1_is_not_abstract():
    assert not inspect.isabstract(afpText_PGP1)


def test_afptext_pgp1_constructor_exists():
    assert callable(afpText_PGP1.__init__)


def test_afptext_pgp1_constructor_args():
    sig = inspect.signature(afpText_PGP1.__init__)
    params = list(sig.parameters.keys())
    assert "YOset" in params, "Missing parameter 'YOset'"
    assert "XOset" in params, "Missing parameter 'XOset'"

def test_afptext_pgp1_has_YOset():
    assert hasattr(afpText_PGP1, "YOset")
    descriptor = None
    for klass in afpText_PGP1.__mro__:
        if "YOset" in klass.__dict__:
            descriptor = klass.__dict__["YOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgp1_has_XOset():
    assert hasattr(afpText_PGP1, "XOset")
    descriptor = None
    for klass in afpText_PGP1.__mro__:
        if "XOset" in klass.__dict__:
            descriptor = klass.__dict__["XOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bpm_is_not_abstract():
    assert not inspect.isabstract(afpText_BPM)


def test_afptext_bpm_constructor_exists():
    assert callable(afpText_BPM.__init__)


def test_afptext_bpm_constructor_args():
    sig = inspect.signature(afpText_BPM.__init__)
    params = list(sig.parameters.keys())
    assert "PMName" in params, "Missing parameter 'PMName'"

def test_afptext_bpm_has_PMName():
    assert hasattr(afpText_BPM, "PMName")
    descriptor = None
    for klass in afpText_BPM.__mro__:
        if "PMName" in klass.__dict__:
            descriptor = klass.__dict__["PMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mpo_is_not_abstract():
    assert not inspect.isabstract(afpText_MPO)


def test_afptext_mpo_constructor_exists():
    assert callable(afpText_MPO.__init__)


def test_afptext_mpo_constructor_args():
    sig = inspect.signature(afpText_MPO.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bpf_is_not_abstract():
    assert not inspect.isabstract(afpText_BPF)


def test_afptext_bpf_constructor_exists():
    assert callable(afpText_BPF.__init__)


def test_afptext_bpf_constructor_args():
    sig = inspect.signature(afpText_BPF.__init__)
    params = list(sig.parameters.keys())
    assert "PFName" in params, "Missing parameter 'PFName'"

def test_afptext_bpf_has_PFName():
    assert hasattr(afpText_BPF, "PFName")
    descriptor = None
    for klass in afpText_BPF.__mro__:
        if "PFName" in klass.__dict__:
            descriptor = klass.__dict__["PFName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_brg_is_not_abstract():
    assert not inspect.isabstract(afpText_BRG)


def test_afptext_brg_constructor_exists():
    assert callable(afpText_BRG.__init__)


def test_afptext_brg_constructor_args():
    sig = inspect.signature(afpText_BRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGrpName" in params, "Missing parameter 'RGrpName'"

def test_afptext_brg_has_RGrpName():
    assert hasattr(afpText_BRG, "RGrpName")
    descriptor = None
    for klass in afpText_BRG.__mro__:
        if "RGrpName" in klass.__dict__:
            descriptor = klass.__dict__["RGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eag_is_not_abstract():
    assert not inspect.isabstract(afpText_EAG)


def test_afptext_eag_constructor_exists():
    assert callable(afpText_EAG.__init__)


def test_afptext_eag_constructor_args():
    sig = inspect.signature(afpText_EAG.__init__)
    params = list(sig.parameters.keys())
    assert "AEGName" in params, "Missing parameter 'AEGName'"

def test_afptext_eag_has_AEGName():
    assert hasattr(afpText_EAG, "AEGName")
    descriptor = None
    for klass in afpText_EAG.__mro__:
        if "AEGName" in klass.__dict__:
            descriptor = klass.__dict__["AEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cat_is_not_abstract():
    assert not inspect.isabstract(afpText_CAT)


def test_afptext_cat_constructor_exists():
    assert callable(afpText_CAT.__init__)


def test_afptext_cat_constructor_args():
    sig = inspect.signature(afpText_CAT.__init__)
    params = list(sig.parameters.keys())
    assert "CATData" in params, "Missing parameter 'CATData'"

def test_afptext_cat_has_CATData():
    assert hasattr(afpText_CAT, "CATData")
    descriptor = None
    for klass in afpText_CAT.__mro__:
        if "CATData" in klass.__dict__:
            descriptor = klass.__dict__["CATData"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mcd_is_not_abstract():
    assert not inspect.isabstract(afpText_MCD)


def test_afptext_mcd_constructor_exists():
    assert callable(afpText_MCD.__init__)


def test_afptext_mcd_constructor_args():
    sig = inspect.signature(afpText_MCD.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bdt_is_not_abstract():
    assert not inspect.isabstract(afpText_BDT)


def test_afptext_bdt_constructor_exists():
    assert callable(afpText_BDT.__init__)


def test_afptext_bdt_constructor_args():
    sig = inspect.signature(afpText_BDT.__init__)
    params = list(sig.parameters.keys())
    assert "DocName" in params, "Missing parameter 'DocName'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_bdt_has_DocName():
    assert hasattr(afpText_BDT, "DocName")
    descriptor = None
    for klass in afpText_BDT.__mro__:
        if "DocName" in klass.__dict__:
            descriptor = klass.__dict__["DocName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdt_has_Reserved():
    assert hasattr(afpText_BDT, "Reserved")
    descriptor = None
    for klass in afpText_BDT.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bmm_is_not_abstract():
    assert not inspect.isabstract(afpText_BMM)


def test_afptext_bmm_constructor_exists():
    assert callable(afpText_BMM.__init__)


def test_afptext_bmm_constructor_args():
    sig = inspect.signature(afpText_BMM.__init__)
    params = list(sig.parameters.keys())
    assert "MMName" in params, "Missing parameter 'MMName'"

def test_afptext_bmm_has_MMName():
    assert hasattr(afpText_BMM, "MMName")
    descriptor = None
    for klass in afpText_BMM.__mro__:
        if "MMName" in klass.__dict__:
            descriptor = klass.__dict__["MMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ecf_is_not_abstract():
    assert not inspect.isabstract(afpText_ECF)


def test_afptext_ecf_constructor_exists():
    assert callable(afpText_ECF.__init__)


def test_afptext_ecf_constructor_args():
    sig = inspect.signature(afpText_ECF.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_ecf_has_RSName():
    assert hasattr(afpText_ECF, "RSName")
    descriptor = None
    for klass in afpText_ECF.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bog_is_not_abstract():
    assert not inspect.isabstract(afpText_BOG)


def test_afptext_bog_constructor_exists():
    assert callable(afpText_BOG.__init__)


def test_afptext_bog_constructor_args():
    sig = inspect.signature(afpText_BOG.__init__)
    params = list(sig.parameters.keys())
    assert "OEGName" in params, "Missing parameter 'OEGName'"

def test_afptext_bog_has_OEGName():
    assert hasattr(afpText_BOG, "OEGName")
    descriptor = None
    for klass in afpText_BOG.__mro__:
        if "OEGName" in klass.__dict__:
            descriptor = klass.__dict__["OEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pmc_is_not_abstract():
    assert not inspect.isabstract(afpText_PMC)


def test_afptext_pmc_constructor_exists():
    assert callable(afpText_PMC.__init__)


def test_afptext_pmc_constructor_args():
    sig = inspect.signature(afpText_PMC.__init__)
    params = list(sig.parameters.keys())
    assert "PMCid" in params, "Missing parameter 'PMCid'"

def test_afptext_pmc_has_PMCid():
    assert hasattr(afpText_PMC, "PMCid")
    descriptor = None
    for klass in afpText_PMC.__mro__:
        if "PMCid" in klass.__dict__:
            descriptor = klass.__dict__["PMCid"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bfm_is_not_abstract():
    assert not inspect.isabstract(afpText_BFM)


def test_afptext_bfm_constructor_exists():
    assert callable(afpText_BFM.__init__)


def test_afptext_bfm_constructor_args():
    sig = inspect.signature(afpText_BFM.__init__)
    params = list(sig.parameters.keys())
    assert "FMName" in params, "Missing parameter 'FMName'"

def test_afptext_bfm_has_FMName():
    assert hasattr(afpText_BFM, "FMName")
    descriptor = None
    for klass in afpText_BFM.__mro__:
        if "FMName" in klass.__dict__:
            descriptor = klass.__dict__["FMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_brs_is_not_abstract():
    assert not inspect.isabstract(afpText_BRS)


def test_afptext_brs_constructor_exists():
    assert callable(afpText_BRS.__init__)


def test_afptext_brs_constructor_args():
    sig = inspect.signature(afpText_BRS.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_brs_has_RSName():
    assert hasattr(afpText_BRS, "RSName")
    descriptor = None
    for klass in afpText_BRS.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ptx_is_not_abstract():
    assert not inspect.isabstract(afpText_PTX)


def test_afptext_ptx_constructor_exists():
    assert callable(afpText_PTX.__init__)


def test_afptext_ptx_constructor_args():
    sig = inspect.signature(afpText_PTX.__init__)
    params = list(sig.parameters.keys())



def test_afptext_lnc_is_not_abstract():
    assert not inspect.isabstract(afpText_LNC)


def test_afptext_lnc_constructor_exists():
    assert callable(afpText_LNC.__init__)


def test_afptext_lnc_constructor_args():
    sig = inspect.signature(afpText_LNC.__init__)
    params = list(sig.parameters.keys())
    assert "NumDSC" in params, "Missing parameter 'NumDSC'"

def test_afptext_lnc_has_NumDSC():
    assert hasattr(afpText_LNC, "NumDSC")
    descriptor = None
    for klass in afpText_LNC.__mro__:
        if "NumDSC" in klass.__dict__:
            descriptor = klass.__dict__["NumDSC"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mfc_is_not_abstract():
    assert not inspect.isabstract(afpText_MFC)


def test_afptext_mfc_constructor_exists():
    assert callable(afpText_MFC.__init__)


def test_afptext_mfc_constructor_args():
    sig = inspect.signature(afpText_MFC.__init__)
    params = list(sig.parameters.keys())
    assert "MFCFlgs" in params, "Missing parameter 'MFCFlgs'"
    assert "MedColl" in params, "Missing parameter 'MedColl'"
    assert "MFCScpe" in params, "Missing parameter 'MFCScpe'"

def test_afptext_mfc_has_MFCFlgs():
    assert hasattr(afpText_MFC, "MFCFlgs")
    descriptor = None
    for klass in afpText_MFC.__mro__:
        if "MFCFlgs" in klass.__dict__:
            descriptor = klass.__dict__["MFCFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mfc_has_MedColl():
    assert hasattr(afpText_MFC, "MedColl")
    descriptor = None
    for klass in afpText_MFC.__mro__:
        if "MedColl" in klass.__dict__:
            descriptor = klass.__dict__["MedColl"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mfc_has_MFCScpe():
    assert hasattr(afpText_MFC, "MFCScpe")
    descriptor = None
    for klass in afpText_MFC.__mro__:
        if "MFCScpe" in klass.__dict__:
            descriptor = klass.__dict__["MFCScpe"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mps_is_not_abstract():
    assert not inspect.isabstract(afpText_MPS)


def test_afptext_mps_constructor_exists():
    assert callable(afpText_MPS.__init__)


def test_afptext_mps_constructor_args():
    sig = inspect.signature(afpText_MPS.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mps_has_Reserved():
    assert hasattr(afpText_MPS, "Reserved")
    descriptor = None
    for klass in afpText_MPS.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mps_has_RGLength():
    assert hasattr(afpText_MPS, "RGLength")
    descriptor = None
    for klass in afpText_MPS.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ptd1_is_not_abstract():
    assert not inspect.isabstract(afpText_PTD1)


def test_afptext_ptd1_constructor_exists():
    assert callable(afpText_PTD1.__init__)


def test_afptext_ptd1_constructor_args():
    sig = inspect.signature(afpText_PTD1.__init__)
    params = list(sig.parameters.keys())
    assert "YPEXTENT" in params, "Missing parameter 'YPEXTENT'"
    assert "YPUNITVL" in params, "Missing parameter 'YPUNITVL'"
    assert "XPUNITVL" in params, "Missing parameter 'XPUNITVL'"
    assert "XPBASE" in params, "Missing parameter 'XPBASE'"
    assert "XPEXTENT" in params, "Missing parameter 'XPEXTENT'"
    assert "YPBASE" in params, "Missing parameter 'YPBASE'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"

def test_afptext_ptd1_has_YPEXTENT():
    assert hasattr(afpText_PTD1, "YPEXTENT")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "YPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["YPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd1_has_YPUNITVL():
    assert hasattr(afpText_PTD1, "YPUNITVL")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "YPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["YPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd1_has_XPUNITVL():
    assert hasattr(afpText_PTD1, "XPUNITVL")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "XPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["XPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd1_has_XPBASE():
    assert hasattr(afpText_PTD1, "XPBASE")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "XPBASE" in klass.__dict__:
            descriptor = klass.__dict__["XPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd1_has_XPEXTENT():
    assert hasattr(afpText_PTD1, "XPEXTENT")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "XPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["XPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd1_has_YPBASE():
    assert hasattr(afpText_PTD1, "YPBASE")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "YPBASE" in klass.__dict__:
            descriptor = klass.__dict__["YPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd1_has_RESERVED():
    assert hasattr(afpText_PTD1, "RESERVED")
    descriptor = None
    for klass in afpText_PTD1.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mcf1_is_not_abstract():
    assert not inspect.isabstract(afpText_MCF1)


def test_afptext_mcf1_constructor_exists():
    assert callable(afpText_MCF1.__init__)


def test_afptext_mcf1_constructor_args():
    sig = inspect.signature(afpText_MCF1.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mcf1_has_RGLength():
    assert hasattr(afpText_MCF1, "RGLength")
    descriptor = None
    for klass in afpText_MCF1.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_lnd_is_not_abstract():
    assert not inspect.isabstract(afpText_LND)


def test_afptext_lnd_constructor_exists():
    assert callable(afpText_LND.__init__)


def test_afptext_lnd_constructor_args():
    sig = inspect.signature(afpText_LND.__init__)
    params = list(sig.parameters.keys())
    assert "LNDFlgs" in params, "Missing parameter 'LNDFlgs'"
    assert "SupName" in params, "Missing parameter 'SupName'"
    assert "NLNDsp" in params, "Missing parameter 'NLNDsp'"
    assert "CCPID" in params, "Missing parameter 'CCPID'"
    assert "ChnlCde" in params, "Missing parameter 'ChnlCde'"
    assert "TxtOrent" in params, "Missing parameter 'TxtOrent'"
    assert "TxtColor" in params, "Missing parameter 'TxtColor'"
    assert "BPos" in params, "Missing parameter 'BPos'"
    assert "DataLgth" in params, "Missing parameter 'DataLgth'"
    assert "DataStrt" in params, "Missing parameter 'DataStrt'"
    assert "NLNDccp" in params, "Missing parameter 'NLNDccp'"
    assert "FntLID" in params, "Missing parameter 'FntLID'"
    assert "NLNDskp" in params, "Missing parameter 'NLNDskp'"
    assert "SubpgID" in params, "Missing parameter 'SubpgID'"
    assert "NLNDreu" in params, "Missing parameter 'NLNDreu'"
    assert "IPos" in params, "Missing parameter 'IPos'"
    assert "SOLid" in params, "Missing parameter 'SOLid'"

def test_afptext_lnd_has_LNDFlgs():
    assert hasattr(afpText_LND, "LNDFlgs")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "LNDFlgs" in klass.__dict__:
            descriptor = klass.__dict__["LNDFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_SupName():
    assert hasattr(afpText_LND, "SupName")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "SupName" in klass.__dict__:
            descriptor = klass.__dict__["SupName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_NLNDsp():
    assert hasattr(afpText_LND, "NLNDsp")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "NLNDsp" in klass.__dict__:
            descriptor = klass.__dict__["NLNDsp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_CCPID():
    assert hasattr(afpText_LND, "CCPID")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "CCPID" in klass.__dict__:
            descriptor = klass.__dict__["CCPID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_ChnlCde():
    assert hasattr(afpText_LND, "ChnlCde")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "ChnlCde" in klass.__dict__:
            descriptor = klass.__dict__["ChnlCde"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_TxtOrent():
    assert hasattr(afpText_LND, "TxtOrent")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "TxtOrent" in klass.__dict__:
            descriptor = klass.__dict__["TxtOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_TxtColor():
    assert hasattr(afpText_LND, "TxtColor")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "TxtColor" in klass.__dict__:
            descriptor = klass.__dict__["TxtColor"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_BPos():
    assert hasattr(afpText_LND, "BPos")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "BPos" in klass.__dict__:
            descriptor = klass.__dict__["BPos"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_DataLgth():
    assert hasattr(afpText_LND, "DataLgth")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "DataLgth" in klass.__dict__:
            descriptor = klass.__dict__["DataLgth"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_DataStrt():
    assert hasattr(afpText_LND, "DataStrt")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "DataStrt" in klass.__dict__:
            descriptor = klass.__dict__["DataStrt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_NLNDccp():
    assert hasattr(afpText_LND, "NLNDccp")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "NLNDccp" in klass.__dict__:
            descriptor = klass.__dict__["NLNDccp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_FntLID():
    assert hasattr(afpText_LND, "FntLID")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "FntLID" in klass.__dict__:
            descriptor = klass.__dict__["FntLID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_NLNDskp():
    assert hasattr(afpText_LND, "NLNDskp")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "NLNDskp" in klass.__dict__:
            descriptor = klass.__dict__["NLNDskp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_SubpgID():
    assert hasattr(afpText_LND, "SubpgID")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "SubpgID" in klass.__dict__:
            descriptor = klass.__dict__["SubpgID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_NLNDreu():
    assert hasattr(afpText_LND, "NLNDreu")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "NLNDreu" in klass.__dict__:
            descriptor = klass.__dict__["NLNDreu"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_IPos():
    assert hasattr(afpText_LND, "IPos")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "IPos" in klass.__dict__:
            descriptor = klass.__dict__["IPos"]
            break
    assert isinstance(descriptor, property)

def test_afptext_lnd_has_SOLid():
    assert hasattr(afpText_LND, "SOLid")
    descriptor = None
    for klass in afpText_LND.__mro__:
        if "SOLid" in klass.__dict__:
            descriptor = klass.__dict__["SOLid"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bdi_is_not_abstract():
    assert not inspect.isabstract(afpText_BDI)


def test_afptext_bdi_constructor_exists():
    assert callable(afpText_BDI.__init__)


def test_afptext_bdi_constructor_args():
    sig = inspect.signature(afpText_BDI.__init__)
    params = list(sig.parameters.keys())
    assert "IndxName" in params, "Missing parameter 'IndxName'"

def test_afptext_bdi_has_IndxName():
    assert hasattr(afpText_BDI, "IndxName")
    descriptor = None
    for klass in afpText_BDI.__mro__:
        if "IndxName" in klass.__dict__:
            descriptor = klass.__dict__["IndxName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bpg_is_not_abstract():
    assert not inspect.isabstract(afpText_BPG)


def test_afptext_bpg_constructor_exists():
    assert callable(afpText_BPG.__init__)


def test_afptext_bpg_constructor_args():
    sig = inspect.signature(afpText_BPG.__init__)
    params = list(sig.parameters.keys())
    assert "PageName" in params, "Missing parameter 'PageName'"

def test_afptext_bpg_has_PageName():
    assert hasattr(afpText_BPG, "PageName")
    descriptor = None
    for klass in afpText_BPG.__mro__:
        if "PageName" in klass.__dict__:
            descriptor = klass.__dict__["PageName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cfi_is_not_abstract():
    assert not inspect.isabstract(afpText_CFI)


def test_afptext_cfi_constructor_exists():
    assert callable(afpText_CFI.__init__)


def test_afptext_cfi_constructor_args():
    sig = inspect.signature(afpText_CFI.__init__)
    params = list(sig.parameters.keys())



def test_afptext_nop_is_not_abstract():
    assert not inspect.isabstract(afpText_NOP)


def test_afptext_nop_constructor_exists():
    assert callable(afpText_NOP.__init__)


def test_afptext_nop_constructor_args():
    sig = inspect.signature(afpText_NOP.__init__)
    params = list(sig.parameters.keys())
    assert "UndfData" in params, "Missing parameter 'UndfData'"

def test_afptext_nop_has_UndfData():
    assert hasattr(afpText_NOP, "UndfData")
    descriptor = None
    for klass in afpText_NOP.__mro__:
        if "UndfData" in klass.__dict__:
            descriptor = klass.__dict__["UndfData"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ptd_is_not_abstract():
    assert not inspect.isabstract(afpText_PTD)


def test_afptext_ptd_constructor_exists():
    assert callable(afpText_PTD.__init__)


def test_afptext_ptd_constructor_args():
    sig = inspect.signature(afpText_PTD.__init__)
    params = list(sig.parameters.keys())
    assert "XPBASE" in params, "Missing parameter 'XPBASE'"
    assert "XPUNITVL" in params, "Missing parameter 'XPUNITVL'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "YPEXTENT" in params, "Missing parameter 'YPEXTENT'"
    assert "YPUNITVL" in params, "Missing parameter 'YPUNITVL'"
    assert "YPBASE" in params, "Missing parameter 'YPBASE'"
    assert "XPEXTENT" in params, "Missing parameter 'XPEXTENT'"

def test_afptext_ptd_has_XPBASE():
    assert hasattr(afpText_PTD, "XPBASE")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "XPBASE" in klass.__dict__:
            descriptor = klass.__dict__["XPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd_has_XPUNITVL():
    assert hasattr(afpText_PTD, "XPUNITVL")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "XPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["XPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd_has_RESERVED():
    assert hasattr(afpText_PTD, "RESERVED")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd_has_YPEXTENT():
    assert hasattr(afpText_PTD, "YPEXTENT")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "YPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["YPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd_has_YPUNITVL():
    assert hasattr(afpText_PTD, "YPUNITVL")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "YPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["YPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd_has_YPBASE():
    assert hasattr(afpText_PTD, "YPBASE")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "YPBASE" in klass.__dict__:
            descriptor = klass.__dict__["YPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ptd_has_XPEXTENT():
    assert hasattr(afpText_PTD, "XPEXTENT")
    descriptor = None
    for klass in afpText_PTD.__mro__:
        if "XPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["XPEXTENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ocd_is_not_abstract():
    assert not inspect.isabstract(afpText_OCD)


def test_afptext_ocd_constructor_exists():
    assert callable(afpText_OCD.__init__)


def test_afptext_ocd_constructor_args():
    sig = inspect.signature(afpText_OCD.__init__)
    params = list(sig.parameters.keys())
    assert "ObjCdat" in params, "Missing parameter 'ObjCdat'"

def test_afptext_ocd_has_ObjCdat():
    assert hasattr(afpText_OCD, "ObjCdat")
    descriptor = None
    for klass in afpText_OCD.__mro__:
        if "ObjCdat" in klass.__dict__:
            descriptor = klass.__dict__["ObjCdat"]
            break
    assert isinstance(descriptor, property)



def test_afptext_lle_is_not_abstract():
    assert not inspect.isabstract(afpText_LLE)


def test_afptext_lle_constructor_exists():
    assert callable(afpText_LLE.__init__)


def test_afptext_lle_constructor_args():
    sig = inspect.signature(afpText_LLE.__init__)
    params = list(sig.parameters.keys())
    assert "LnkType" in params, "Missing parameter 'LnkType'"

def test_afptext_lle_has_LnkType():
    assert hasattr(afpText_LLE, "LnkType")
    descriptor = None
    for klass in afpText_LLE.__mro__:
        if "LnkType" in klass.__dict__:
            descriptor = klass.__dict__["LnkType"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bps_is_not_abstract():
    assert not inspect.isabstract(afpText_BPS)


def test_afptext_bps_constructor_exists():
    assert callable(afpText_BPS.__init__)


def test_afptext_bps_constructor_args():
    sig = inspect.signature(afpText_BPS.__init__)
    params = list(sig.parameters.keys())
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext_bps_has_PsegName():
    assert hasattr(afpText_BPS, "PsegName")
    descriptor = None
    for klass in afpText_BPS.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mdd_is_not_abstract():
    assert not inspect.isabstract(afpText_MDD)


def test_afptext_mdd_constructor_exists():
    assert callable(afpText_MDD.__init__)


def test_afptext_mdd_constructor_args():
    sig = inspect.signature(afpText_MDD.__init__)
    params = list(sig.parameters.keys())
    assert "MDDFlgs" in params, "Missing parameter 'MDDFlgs'"
    assert "XmBase" in params, "Missing parameter 'XmBase'"
    assert "YmSize" in params, "Missing parameter 'YmSize'"
    assert "YmUnits" in params, "Missing parameter 'YmUnits'"
    assert "XmSize" in params, "Missing parameter 'XmSize'"
    assert "XmUnits" in params, "Missing parameter 'XmUnits'"
    assert "YmBase" in params, "Missing parameter 'YmBase'"

def test_afptext_mdd_has_MDDFlgs():
    assert hasattr(afpText_MDD, "MDDFlgs")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "MDDFlgs" in klass.__dict__:
            descriptor = klass.__dict__["MDDFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mdd_has_XmBase():
    assert hasattr(afpText_MDD, "XmBase")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "XmBase" in klass.__dict__:
            descriptor = klass.__dict__["XmBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mdd_has_YmSize():
    assert hasattr(afpText_MDD, "YmSize")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "YmSize" in klass.__dict__:
            descriptor = klass.__dict__["YmSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mdd_has_YmUnits():
    assert hasattr(afpText_MDD, "YmUnits")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "YmUnits" in klass.__dict__:
            descriptor = klass.__dict__["YmUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mdd_has_XmSize():
    assert hasattr(afpText_MDD, "XmSize")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "XmSize" in klass.__dict__:
            descriptor = klass.__dict__["XmSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mdd_has_XmUnits():
    assert hasattr(afpText_MDD, "XmUnits")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "XmUnits" in klass.__dict__:
            descriptor = klass.__dict__["XmUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mdd_has_YmBase():
    assert hasattr(afpText_MDD, "YmBase")
    descriptor = None
    for klass in afpText_MDD.__mro__:
        if "YmBase" in klass.__dict__:
            descriptor = klass.__dict__["YmBase"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mpg_is_not_abstract():
    assert not inspect.isabstract(afpText_MPG)


def test_afptext_mpg_constructor_exists():
    assert callable(afpText_MPG.__init__)


def test_afptext_mpg_constructor_args():
    sig = inspect.signature(afpText_MPG.__init__)
    params = list(sig.parameters.keys())



def test_afptext_mmt_is_not_abstract():
    assert not inspect.isabstract(afpText_MMT)


def test_afptext_mmt_constructor_exists():
    assert callable(afpText_MMT.__init__)


def test_afptext_mmt_constructor_args():
    sig = inspect.signature(afpText_MMT.__init__)
    params = list(sig.parameters.keys())



def test_afptext_edm_is_not_abstract():
    assert not inspect.isabstract(afpText_EDM)


def test_afptext_edm_constructor_exists():
    assert callable(afpText_EDM.__init__)


def test_afptext_edm_constructor_args():
    sig = inspect.signature(afpText_EDM.__init__)
    params = list(sig.parameters.keys())
    assert "DMName" in params, "Missing parameter 'DMName'"

def test_afptext_edm_has_DMName():
    assert hasattr(afpText_EDM, "DMName")
    descriptor = None
    for klass in afpText_EDM.__mro__:
        if "DMName" in klass.__dict__:
            descriptor = klass.__dict__["DMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pec_is_not_abstract():
    assert not inspect.isabstract(afpText_PEC)


def test_afptext_pec_constructor_exists():
    assert callable(afpText_PEC.__init__)


def test_afptext_pec_constructor_args():
    sig = inspect.signature(afpText_PEC.__init__)
    params = list(sig.parameters.keys())



def test_afptext_dxd_is_not_abstract():
    assert not inspect.isabstract(afpText_DXD)


def test_afptext_dxd_constructor_exists():
    assert callable(afpText_DXD.__init__)


def test_afptext_dxd_constructor_args():
    sig = inspect.signature(afpText_DXD.__init__)
    params = list(sig.parameters.keys())



def test_afptext_cpd_is_not_abstract():
    assert not inspect.isabstract(afpText_CPD)


def test_afptext_cpd_constructor_exists():
    assert callable(afpText_CPD.__init__)


def test_afptext_cpd_constructor_args():
    sig = inspect.signature(afpText_CPD.__init__)
    params = list(sig.parameters.keys())
    assert "GCGIDLen" in params, "Missing parameter 'GCGIDLen'"
    assert "EncScheme" in params, "Missing parameter 'EncScheme'"
    assert "CPDesc" in params, "Missing parameter 'CPDesc'"
    assert "NumCdPts" in params, "Missing parameter 'NumCdPts'"
    assert "CPGID" in params, "Missing parameter 'CPGID'"
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"

def test_afptext_cpd_has_GCGIDLen():
    assert hasattr(afpText_CPD, "GCGIDLen")
    descriptor = None
    for klass in afpText_CPD.__mro__:
        if "GCGIDLen" in klass.__dict__:
            descriptor = klass.__dict__["GCGIDLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpd_has_EncScheme():
    assert hasattr(afpText_CPD, "EncScheme")
    descriptor = None
    for klass in afpText_CPD.__mro__:
        if "EncScheme" in klass.__dict__:
            descriptor = klass.__dict__["EncScheme"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpd_has_CPDesc():
    assert hasattr(afpText_CPD, "CPDesc")
    descriptor = None
    for klass in afpText_CPD.__mro__:
        if "CPDesc" in klass.__dict__:
            descriptor = klass.__dict__["CPDesc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpd_has_NumCdPts():
    assert hasattr(afpText_CPD, "NumCdPts")
    descriptor = None
    for klass in afpText_CPD.__mro__:
        if "NumCdPts" in klass.__dict__:
            descriptor = klass.__dict__["NumCdPts"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpd_has_CPGID():
    assert hasattr(afpText_CPD, "CPGID")
    descriptor = None
    for klass in afpText_CPD.__mro__:
        if "CPGID" in klass.__dict__:
            descriptor = klass.__dict__["CPGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpd_has_GCSGID():
    assert hasattr(afpText_CPD, "GCSGID")
    descriptor = None
    for klass in afpText_CPD.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eca_is_not_abstract():
    assert not inspect.isabstract(afpText_ECA)


def test_afptext_eca_constructor_exists():
    assert callable(afpText_ECA.__init__)


def test_afptext_eca_constructor_args():
    sig = inspect.signature(afpText_ECA.__init__)
    params = list(sig.parameters.keys())
    assert "CATName" in params, "Missing parameter 'CATName'"

def test_afptext_eca_has_CATName():
    assert hasattr(afpText_ECA, "CATName")
    descriptor = None
    for klass in afpText_ECA.__mro__:
        if "CATName" in klass.__dict__:
            descriptor = klass.__dict__["CATName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cdd_is_not_abstract():
    assert not inspect.isabstract(afpText_CDD)


def test_afptext_cdd_constructor_exists():
    assert callable(afpText_CDD.__init__)


def test_afptext_cdd_constructor_args():
    sig = inspect.signature(afpText_CDD.__init__)
    params = list(sig.parameters.keys())
    assert "YocSize" in params, "Missing parameter 'YocSize'"
    assert "YocUnits" in params, "Missing parameter 'YocUnits'"
    assert "XocUnits" in params, "Missing parameter 'XocUnits'"
    assert "XocBase" in params, "Missing parameter 'XocBase'"
    assert "YocBase" in params, "Missing parameter 'YocBase'"
    assert "XocSize" in params, "Missing parameter 'XocSize'"

def test_afptext_cdd_has_YocSize():
    assert hasattr(afpText_CDD, "YocSize")
    descriptor = None
    for klass in afpText_CDD.__mro__:
        if "YocSize" in klass.__dict__:
            descriptor = klass.__dict__["YocSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cdd_has_YocUnits():
    assert hasattr(afpText_CDD, "YocUnits")
    descriptor = None
    for klass in afpText_CDD.__mro__:
        if "YocUnits" in klass.__dict__:
            descriptor = klass.__dict__["YocUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cdd_has_XocUnits():
    assert hasattr(afpText_CDD, "XocUnits")
    descriptor = None
    for klass in afpText_CDD.__mro__:
        if "XocUnits" in klass.__dict__:
            descriptor = klass.__dict__["XocUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cdd_has_XocBase():
    assert hasattr(afpText_CDD, "XocBase")
    descriptor = None
    for klass in afpText_CDD.__mro__:
        if "XocBase" in klass.__dict__:
            descriptor = klass.__dict__["XocBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cdd_has_YocBase():
    assert hasattr(afpText_CDD, "YocBase")
    descriptor = None
    for klass in afpText_CDD.__mro__:
        if "YocBase" in klass.__dict__:
            descriptor = klass.__dict__["YocBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cdd_has_XocSize():
    assert hasattr(afpText_CDD, "XocSize")
    descriptor = None
    for klass in afpText_CDD.__mro__:
        if "XocSize" in klass.__dict__:
            descriptor = klass.__dict__["XocSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bfn_is_not_abstract():
    assert not inspect.isabstract(afpText_BFN)


def test_afptext_bfn_constructor_exists():
    assert callable(afpText_BFN.__init__)


def test_afptext_bfn_constructor_args():
    sig = inspect.signature(afpText_BFN.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_bfn_has_RSName():
    assert hasattr(afpText_BFN, "RSName")
    descriptor = None
    for klass in afpText_BFN.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bii_is_not_abstract():
    assert not inspect.isabstract(afpText_BII)


def test_afptext_bii_constructor_exists():
    assert callable(afpText_BII.__init__)


def test_afptext_bii_constructor_args():
    sig = inspect.signature(afpText_BII.__init__)
    params = list(sig.parameters.keys())
    assert "ImoName" in params, "Missing parameter 'ImoName'"

def test_afptext_bii_has_ImoName():
    assert hasattr(afpText_BII, "ImoName")
    descriptor = None
    for klass in afpText_BII.__mro__:
        if "ImoName" in klass.__dict__:
            descriptor = klass.__dict__["ImoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pgp_is_not_abstract():
    assert not inspect.isabstract(afpText_PGP)


def test_afptext_pgp_constructor_exists():
    assert callable(afpText_PGP.__init__)


def test_afptext_pgp_constructor_args():
    sig = inspect.signature(afpText_PGP.__init__)
    params = list(sig.parameters.keys())
    assert "Constant" in params, "Missing parameter 'Constant'"

def test_afptext_pgp_has_Constant():
    assert hasattr(afpText_PGP, "Constant")
    descriptor = None
    for klass in afpText_PGP.__mro__:
        if "Constant" in klass.__dict__:
            descriptor = klass.__dict__["Constant"]
            break
    assert isinstance(descriptor, property)



def test_afptext_pgd_is_not_abstract():
    assert not inspect.isabstract(afpText_PGD)


def test_afptext_pgd_constructor_exists():
    assert callable(afpText_PGD.__init__)


def test_afptext_pgd_constructor_args():
    sig = inspect.signature(afpText_PGD.__init__)
    params = list(sig.parameters.keys())
    assert "YpgSize" in params, "Missing parameter 'YpgSize'"
    assert "YpgUnits" in params, "Missing parameter 'YpgUnits'"
    assert "XpgUnits" in params, "Missing parameter 'XpgUnits'"
    assert "XpgBase" in params, "Missing parameter 'XpgBase'"
    assert "YpgBase" in params, "Missing parameter 'YpgBase'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "XpgSize" in params, "Missing parameter 'XpgSize'"

def test_afptext_pgd_has_YpgSize():
    assert hasattr(afpText_PGD, "YpgSize")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "YpgSize" in klass.__dict__:
            descriptor = klass.__dict__["YpgSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgd_has_YpgUnits():
    assert hasattr(afpText_PGD, "YpgUnits")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "YpgUnits" in klass.__dict__:
            descriptor = klass.__dict__["YpgUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgd_has_XpgUnits():
    assert hasattr(afpText_PGD, "XpgUnits")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "XpgUnits" in klass.__dict__:
            descriptor = klass.__dict__["XpgUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgd_has_XpgBase():
    assert hasattr(afpText_PGD, "XpgBase")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "XpgBase" in klass.__dict__:
            descriptor = klass.__dict__["XpgBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgd_has_YpgBase():
    assert hasattr(afpText_PGD, "YpgBase")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "YpgBase" in klass.__dict__:
            descriptor = klass.__dict__["YpgBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgd_has_Reserved():
    assert hasattr(afpText_PGD, "Reserved")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_pgd_has_XpgSize():
    assert hasattr(afpText_PGD, "XpgSize")
    descriptor = None
    for klass in afpText_PGD.__mro__:
        if "XpgSize" in klass.__dict__:
            descriptor = klass.__dict__["XpgSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext_boc_is_not_abstract():
    assert not inspect.isabstract(afpText_BOC)


def test_afptext_boc_constructor_exists():
    assert callable(afpText_BOC.__init__)


def test_afptext_boc_constructor_args():
    sig = inspect.signature(afpText_BOC.__init__)
    params = list(sig.parameters.keys())
    assert "ObjCName" in params, "Missing parameter 'ObjCName'"

def test_afptext_boc_has_ObjCName():
    assert hasattr(afpText_BOC, "ObjCName")
    descriptor = None
    for klass in afpText_BOC.__mro__:
        if "ObjCName" in klass.__dict__:
            descriptor = klass.__dict__["ObjCName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_tle_is_not_abstract():
    assert not inspect.isabstract(afpText_TLE)


def test_afptext_tle_constructor_exists():
    assert callable(afpText_TLE.__init__)


def test_afptext_tle_constructor_args():
    sig = inspect.signature(afpText_TLE.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bdg_is_not_abstract():
    assert not inspect.isabstract(afpText_BDG)


def test_afptext_bdg_constructor_exists():
    assert callable(afpText_BDG.__init__)


def test_afptext_bdg_constructor_args():
    sig = inspect.signature(afpText_BDG.__init__)
    params = list(sig.parameters.keys())
    assert "DEGName" in params, "Missing parameter 'DEGName'"

def test_afptext_bdg_has_DEGName():
    assert hasattr(afpText_BDG, "DEGName")
    descriptor = None
    for klass in afpText_BDG.__mro__:
        if "DEGName" in klass.__dict__:
            descriptor = klass.__dict__["DEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cfc_is_not_abstract():
    assert not inspect.isabstract(afpText_CFC)


def test_afptext_cfc_constructor_exists():
    assert callable(afpText_CFC.__init__)


def test_afptext_cfc_constructor_args():
    sig = inspect.signature(afpText_CFC.__init__)
    params = list(sig.parameters.keys())
    assert "CFIRGLen" in params, "Missing parameter 'CFIRGLen'"
    assert "Retired1" in params, "Missing parameter 'Retired1'"

def test_afptext_cfc_has_CFIRGLen():
    assert hasattr(afpText_CFC, "CFIRGLen")
    descriptor = None
    for klass in afpText_CFC.__mro__:
        if "CFIRGLen" in klass.__dict__:
            descriptor = klass.__dict__["CFIRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cfc_has_Retired1():
    assert hasattr(afpText_CFC, "Retired1")
    descriptor = None
    for klass in afpText_CFC.__mro__:
        if "Retired1" in klass.__dict__:
            descriptor = klass.__dict__["Retired1"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mio_is_not_abstract():
    assert not inspect.isabstract(afpText_MIO)


def test_afptext_mio_constructor_exists():
    assert callable(afpText_MIO.__init__)


def test_afptext_mio_constructor_args():
    sig = inspect.signature(afpText_MIO.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bbc_is_not_abstract():
    assert not inspect.isabstract(afpText_BBC)


def test_afptext_bbc_constructor_exists():
    assert callable(afpText_BBC.__init__)


def test_afptext_bbc_constructor_args():
    sig = inspect.signature(afpText_BBC.__init__)
    params = list(sig.parameters.keys())
    assert "BCdoName" in params, "Missing parameter 'BCdoName'"

def test_afptext_bbc_has_BCdoName():
    assert hasattr(afpText_BBC, "BCdoName")
    descriptor = None
    for klass in afpText_BBC.__mro__:
        if "BCdoName" in klass.__dict__:
            descriptor = klass.__dict__["BCdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bag_is_not_abstract():
    assert not inspect.isabstract(afpText_BAG)


def test_afptext_bag_constructor_exists():
    assert callable(afpText_BAG.__init__)


def test_afptext_bag_constructor_args():
    sig = inspect.signature(afpText_BAG.__init__)
    params = list(sig.parameters.keys())
    assert "AEGName" in params, "Missing parameter 'AEGName'"

def test_afptext_bag_has_AEGName():
    assert hasattr(afpText_BAG, "AEGName")
    descriptor = None
    for klass in afpText_BAG.__mro__:
        if "AEGName" in klass.__dict__:
            descriptor = klass.__dict__["AEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ppo_is_not_abstract():
    assert not inspect.isabstract(afpText_PPO)


def test_afptext_ppo_constructor_exists():
    assert callable(afpText_PPO.__init__)


def test_afptext_ppo_constructor_args():
    sig = inspect.signature(afpText_PPO.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bpt_is_not_abstract():
    assert not inspect.isabstract(afpText_BPT)


def test_afptext_bpt_constructor_exists():
    assert callable(afpText_BPT.__init__)


def test_afptext_bpt_constructor_args():
    sig = inspect.signature(afpText_BPT.__init__)
    params = list(sig.parameters.keys())
    assert "PTdoName" in params, "Missing parameter 'PTdoName'"

def test_afptext_bpt_has_PTdoName():
    assert hasattr(afpText_BPT, "PTdoName")
    descriptor = None
    for klass in afpText_BPT.__mro__:
        if "PTdoName" in klass.__dict__:
            descriptor = klass.__dict__["PTdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ecp_is_not_abstract():
    assert not inspect.isabstract(afpText_ECP)


def test_afptext_ecp_constructor_exists():
    assert callable(afpText_ECP.__init__)


def test_afptext_ecp_constructor_args():
    sig = inspect.signature(afpText_ECP.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_ecp_has_RSName():
    assert hasattr(afpText_ECP, "RSName")
    descriptor = None
    for klass in afpText_ECP.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mmo_is_not_abstract():
    assert not inspect.isabstract(afpText_MMO)


def test_afptext_mmo_constructor_exists():
    assert callable(afpText_MMO.__init__)


def test_afptext_mmo_constructor_args():
    sig = inspect.signature(afpText_MMO.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext_mmo_has_RGLength():
    assert hasattr(afpText_MMO, "RGLength")
    descriptor = None
    for klass in afpText_MMO.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bcp_is_not_abstract():
    assert not inspect.isabstract(afpText_BCP)


def test_afptext_bcp_constructor_exists():
    assert callable(afpText_BCP.__init__)


def test_afptext_bcp_constructor_args():
    sig = inspect.signature(afpText_BCP.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_bcp_has_RSName():
    assert hasattr(afpText_BCP, "RSName")
    descriptor = None
    for klass in afpText_BCP.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mgo_is_not_abstract():
    assert not inspect.isabstract(afpText_MGO)


def test_afptext_mgo_constructor_exists():
    assert callable(afpText_MGO.__init__)


def test_afptext_mgo_constructor_args():
    sig = inspect.signature(afpText_MGO.__init__)
    params = list(sig.parameters.keys())



def test_afptext_pfc_is_not_abstract():
    assert not inspect.isabstract(afpText_PFC)


def test_afptext_pfc_constructor_exists():
    assert callable(afpText_PFC.__init__)


def test_afptext_pfc_constructor_args():
    sig = inspect.signature(afpText_PFC.__init__)
    params = list(sig.parameters.keys())
    assert "PFCFlgs" in params, "Missing parameter 'PFCFlgs'"

def test_afptext_pfc_has_PFCFlgs():
    assert hasattr(afpText_PFC, "PFCFlgs")
    descriptor = None
    for klass in afpText_PFC.__mro__:
        if "PFCFlgs" in klass.__dict__:
            descriptor = klass.__dict__["PFCFlgs"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ctc_is_not_abstract():
    assert not inspect.isabstract(afpText_CTC)


def test_afptext_ctc_constructor_exists():
    assert callable(afpText_CTC.__init__)


def test_afptext_ctc_constructor_args():
    sig = inspect.signature(afpText_CTC.__init__)
    params = list(sig.parameters.keys())
    assert "ConData" in params, "Missing parameter 'ConData'"

def test_afptext_ctc_has_ConData():
    assert hasattr(afpText_CTC, "ConData")
    descriptor = None
    for klass in afpText_CTC.__mro__:
        if "ConData" in klass.__dict__:
            descriptor = klass.__dict__["ConData"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bsg_is_not_abstract():
    assert not inspect.isabstract(afpText_BSG)


def test_afptext_bsg_constructor_exists():
    assert callable(afpText_BSG.__init__)


def test_afptext_bsg_constructor_args():
    sig = inspect.signature(afpText_BSG.__init__)
    params = list(sig.parameters.keys())
    assert "REGName" in params, "Missing parameter 'REGName'"

def test_afptext_bsg_has_REGName():
    assert hasattr(afpText_BSG, "REGName")
    descriptor = None
    for klass in afpText_BSG.__mro__:
        if "REGName" in klass.__dict__:
            descriptor = klass.__dict__["REGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bgr_is_not_abstract():
    assert not inspect.isabstract(afpText_BGR)


def test_afptext_bgr_constructor_exists():
    assert callable(afpText_BGR.__init__)


def test_afptext_bgr_constructor_args():
    sig = inspect.signature(afpText_BGR.__init__)
    params = list(sig.parameters.keys())
    assert "GdoName" in params, "Missing parameter 'GdoName'"

def test_afptext_bgr_has_GdoName():
    assert hasattr(afpText_BGR, "GdoName")
    descriptor = None
    for klass in afpText_BGR.__mro__:
        if "GdoName" in klass.__dict__:
            descriptor = klass.__dict__["GdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bcf_is_not_abstract():
    assert not inspect.isabstract(afpText_BCF)


def test_afptext_bcf_constructor_exists():
    assert callable(afpText_BCF.__init__)


def test_afptext_bcf_constructor_args():
    sig = inspect.signature(afpText_BCF.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_bcf_has_RSName():
    assert hasattr(afpText_BCF, "RSName")
    descriptor = None
    for klass in afpText_BCF.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mbc_is_not_abstract():
    assert not inspect.isabstract(afpText_MBC)


def test_afptext_mbc_constructor_exists():
    assert callable(afpText_MBC.__init__)


def test_afptext_mbc_constructor_args():
    sig = inspect.signature(afpText_MBC.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bdm_is_not_abstract():
    assert not inspect.isabstract(afpText_BDM)


def test_afptext_bdm_constructor_exists():
    assert callable(afpText_BDM.__init__)


def test_afptext_bdm_constructor_args():
    sig = inspect.signature(afpText_BDM.__init__)
    params = list(sig.parameters.keys())
    assert "DatFmt" in params, "Missing parameter 'DatFmt'"
    assert "DMName" in params, "Missing parameter 'DMName'"

def test_afptext_bdm_has_DatFmt():
    assert hasattr(afpText_BDM, "DatFmt")
    descriptor = None
    for klass in afpText_BDM.__mro__:
        if "DatFmt" in klass.__dict__:
            descriptor = klass.__dict__["DatFmt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdm_has_DMName():
    assert hasattr(afpText_BDM, "DMName")
    descriptor = None
    for klass in afpText_BDM.__mro__:
        if "DMName" in klass.__dict__:
            descriptor = klass.__dict__["DMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fgd_is_not_abstract():
    assert not inspect.isabstract(afpText_FGD)


def test_afptext_fgd_constructor_exists():
    assert callable(afpText_FGD.__init__)


def test_afptext_fgd_constructor_args():
    sig = inspect.signature(afpText_FGD.__init__)
    params = list(sig.parameters.keys())
    assert "ConData" in params, "Missing parameter 'ConData'"

def test_afptext_fgd_has_ConData():
    assert hasattr(afpText_FGD, "ConData")
    descriptor = None
    for klass in afpText_FGD.__mro__:
        if "ConData" in klass.__dict__:
            descriptor = klass.__dict__["ConData"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mdr_is_not_abstract():
    assert not inspect.isabstract(afpText_MDR)


def test_afptext_mdr_constructor_exists():
    assert callable(afpText_MDR.__init__)


def test_afptext_mdr_constructor_args():
    sig = inspect.signature(afpText_MDR.__init__)
    params = list(sig.parameters.keys())



def test_afptext_mmc_is_not_abstract():
    assert not inspect.isabstract(afpText_MMC)


def test_afptext_mmc_constructor_exists():
    assert callable(afpText_MMC.__init__)


def test_afptext_mmc_constructor_args():
    sig = inspect.signature(afpText_MMC.__init__)
    params = list(sig.parameters.keys())
    assert "MMCid" in params, "Missing parameter 'MMCid'"
    assert "PARAMETER1" in params, "Missing parameter 'PARAMETER1'"

def test_afptext_mmc_has_MMCid():
    assert hasattr(afpText_MMC, "MMCid")
    descriptor = None
    for klass in afpText_MMC.__mro__:
        if "MMCid" in klass.__dict__:
            descriptor = klass.__dict__["MMCid"]
            break
    assert isinstance(descriptor, property)

def test_afptext_mmc_has_PARAMETER1():
    assert hasattr(afpText_MMC, "PARAMETER1")
    descriptor = None
    for klass in afpText_MMC.__mro__:
        if "PARAMETER1" in klass.__dict__:
            descriptor = klass.__dict__["PARAMETER1"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bfg_is_not_abstract():
    assert not inspect.isabstract(afpText_BFG)


def test_afptext_bfg_constructor_exists():
    assert callable(afpText_BFG.__init__)


def test_afptext_bfg_constructor_args():
    sig = inspect.signature(afpText_BFG.__init__)
    params = list(sig.parameters.keys())
    assert "FEGName" in params, "Missing parameter 'FEGName'"

def test_afptext_bfg_has_FEGName():
    assert hasattr(afpText_BFG, "FEGName")
    descriptor = None
    for klass in afpText_BFG.__mro__:
        if "FEGName" in klass.__dict__:
            descriptor = klass.__dict__["FEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_msu_is_not_abstract():
    assert not inspect.isabstract(afpText_MSU)


def test_afptext_msu_constructor_exists():
    assert callable(afpText_MSU.__init__)


def test_afptext_msu_constructor_args():
    sig = inspect.signature(afpText_MSU.__init__)
    params = list(sig.parameters.keys())



def test_afptext_ebc_is_not_abstract():
    assert not inspect.isabstract(afpText_EBC)


def test_afptext_ebc_constructor_exists():
    assert callable(afpText_EBC.__init__)


def test_afptext_ebc_constructor_args():
    sig = inspect.signature(afpText_EBC.__init__)
    params = list(sig.parameters.keys())
    assert "BCdoName" in params, "Missing parameter 'BCdoName'"

def test_afptext_ebc_has_BCdoName():
    assert hasattr(afpText_EBC, "BCdoName")
    descriptor = None
    for klass in afpText_EBC.__mro__:
        if "BCdoName" in klass.__dict__:
            descriptor = klass.__dict__["BCdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_obd_is_not_abstract():
    assert not inspect.isabstract(afpText_OBD)


def test_afptext_obd_constructor_exists():
    assert callable(afpText_OBD.__init__)


def test_afptext_obd_constructor_args():
    sig = inspect.signature(afpText_OBD.__init__)
    params = list(sig.parameters.keys())



def test_afptext_cpi_is_not_abstract():
    assert not inspect.isabstract(afpText_CPI)


def test_afptext_cpi_constructor_exists():
    assert callable(afpText_CPI.__init__)


def test_afptext_cpi_constructor_args():
    sig = inspect.signature(afpText_CPI.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bca_is_not_abstract():
    assert not inspect.isabstract(afpText_BCA)


def test_afptext_bca_constructor_exists():
    assert callable(afpText_BCA.__init__)


def test_afptext_bca_constructor_args():
    sig = inspect.signature(afpText_BCA.__init__)
    params = list(sig.parameters.keys())
    assert "CATName" in params, "Missing parameter 'CATName'"

def test_afptext_bca_has_CATName():
    assert hasattr(afpText_BCA, "CATName")
    descriptor = None
    for klass in afpText_BCA.__mro__:
        if "CATName" in klass.__dict__:
            descriptor = klass.__dict__["CATName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_edg_is_not_abstract():
    assert not inspect.isabstract(afpText_EDG)


def test_afptext_edg_constructor_exists():
    assert callable(afpText_EDG.__init__)


def test_afptext_edg_constructor_args():
    sig = inspect.signature(afpText_EDG.__init__)
    params = list(sig.parameters.keys())
    assert "DEGName" in params, "Missing parameter 'DEGName'"

def test_afptext_edg_has_DEGName():
    assert hasattr(afpText_EDG, "DEGName")
    descriptor = None
    for klass in afpText_EDG.__mro__:
        if "DEGName" in klass.__dict__:
            descriptor = klass.__dict__["DEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_obp_is_not_abstract():
    assert not inspect.isabstract(afpText_OBP)


def test_afptext_obp_constructor_exists():
    assert callable(afpText_OBP.__init__)


def test_afptext_obp_constructor_args():
    sig = inspect.signature(afpText_OBP.__init__)
    params = list(sig.parameters.keys())
    assert "XoaOset" in params, "Missing parameter 'XoaOset'"
    assert "OAPosID" in params, "Missing parameter 'OAPosID'"
    assert "YoaOset" in params, "Missing parameter 'YoaOset'"
    assert "YocaOrent" in params, "Missing parameter 'YocaOrent'"
    assert "YoaOrent" in params, "Missing parameter 'YoaOrent'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "XocaOrent" in params, "Missing parameter 'XocaOrent'"
    assert "XocaOset" in params, "Missing parameter 'XocaOset'"
    assert "XoaOrent" in params, "Missing parameter 'XoaOrent'"
    assert "RefCSys" in params, "Missing parameter 'RefCSys'"
    assert "YocaOset" in params, "Missing parameter 'YocaOset'"

def test_afptext_obp_has_XoaOset():
    assert hasattr(afpText_OBP, "XoaOset")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "XoaOset" in klass.__dict__:
            descriptor = klass.__dict__["XoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_OAPosID():
    assert hasattr(afpText_OBP, "OAPosID")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "OAPosID" in klass.__dict__:
            descriptor = klass.__dict__["OAPosID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_YoaOset():
    assert hasattr(afpText_OBP, "YoaOset")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "YoaOset" in klass.__dict__:
            descriptor = klass.__dict__["YoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_YocaOrent():
    assert hasattr(afpText_OBP, "YocaOrent")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "YocaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YocaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_YoaOrent():
    assert hasattr(afpText_OBP, "YoaOrent")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "YoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_RGLength():
    assert hasattr(afpText_OBP, "RGLength")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_XocaOrent():
    assert hasattr(afpText_OBP, "XocaOrent")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "XocaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XocaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_XocaOset():
    assert hasattr(afpText_OBP, "XocaOset")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "XocaOset" in klass.__dict__:
            descriptor = klass.__dict__["XocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_XoaOrent():
    assert hasattr(afpText_OBP, "XoaOrent")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "XoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_RefCSys():
    assert hasattr(afpText_OBP, "RefCSys")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "RefCSys" in klass.__dict__:
            descriptor = klass.__dict__["RefCSys"]
            break
    assert isinstance(descriptor, property)

def test_afptext_obp_has_YocaOset():
    assert hasattr(afpText_OBP, "YocaOset")
    descriptor = None
    for klass in afpText_OBP.__mro__:
        if "YocaOset" in klass.__dict__:
            descriptor = klass.__dict__["YocaOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bng_is_not_abstract():
    assert not inspect.isabstract(afpText_BNG)


def test_afptext_bng_constructor_exists():
    assert callable(afpText_BNG.__init__)


def test_afptext_bng_constructor_args():
    sig = inspect.signature(afpText_BNG.__init__)
    params = list(sig.parameters.keys())
    assert "PGrpName" in params, "Missing parameter 'PGrpName'"

def test_afptext_bng_has_PGrpName():
    assert hasattr(afpText_BNG, "PGrpName")
    descriptor = None
    for klass in afpText_BNG.__mro__:
        if "PGrpName" in klass.__dict__:
            descriptor = klass.__dict__["PGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bmo_is_not_abstract():
    assert not inspect.isabstract(afpText_BMO)


def test_afptext_bmo_constructor_exists():
    assert callable(afpText_BMO.__init__)


def test_afptext_bmo_constructor_args():
    sig = inspect.signature(afpText_BMO.__init__)
    params = list(sig.parameters.keys())
    assert "OvlyName" in params, "Missing parameter 'OvlyName'"

def test_afptext_bmo_has_OvlyName():
    assert hasattr(afpText_BMO, "OvlyName")
    descriptor = None
    for klass in afpText_BMO.__mro__:
        if "OvlyName" in klass.__dict__:
            descriptor = klass.__dict__["OvlyName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_cpc_is_not_abstract():
    assert not inspect.isabstract(afpText_CPC)


def test_afptext_cpc_constructor_exists():
    assert callable(afpText_CPC.__init__)


def test_afptext_cpc_constructor_args():
    sig = inspect.signature(afpText_CPC.__init__)
    params = list(sig.parameters.keys())
    assert "PrtFlags" in params, "Missing parameter 'PrtFlags'"
    assert "CPIRGLen" in params, "Missing parameter 'CPIRGLen'"
    assert "VSCharSN" in params, "Missing parameter 'VSCharSN'"
    assert "VSChar" in params, "Missing parameter 'VSChar'"
    assert "DefCharID" in params, "Missing parameter 'DefCharID'"
    assert "VSFlags" in params, "Missing parameter 'VSFlags'"

def test_afptext_cpc_has_PrtFlags():
    assert hasattr(afpText_CPC, "PrtFlags")
    descriptor = None
    for klass in afpText_CPC.__mro__:
        if "PrtFlags" in klass.__dict__:
            descriptor = klass.__dict__["PrtFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpc_has_CPIRGLen():
    assert hasattr(afpText_CPC, "CPIRGLen")
    descriptor = None
    for klass in afpText_CPC.__mro__:
        if "CPIRGLen" in klass.__dict__:
            descriptor = klass.__dict__["CPIRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpc_has_VSCharSN():
    assert hasattr(afpText_CPC, "VSCharSN")
    descriptor = None
    for klass in afpText_CPC.__mro__:
        if "VSCharSN" in klass.__dict__:
            descriptor = klass.__dict__["VSCharSN"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpc_has_VSChar():
    assert hasattr(afpText_CPC, "VSChar")
    descriptor = None
    for klass in afpText_CPC.__mro__:
        if "VSChar" in klass.__dict__:
            descriptor = klass.__dict__["VSChar"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpc_has_DefCharID():
    assert hasattr(afpText_CPC, "DefCharID")
    descriptor = None
    for klass in afpText_CPC.__mro__:
        if "DefCharID" in klass.__dict__:
            descriptor = klass.__dict__["DefCharID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_cpc_has_VSFlags():
    assert hasattr(afpText_CPC, "VSFlags")
    descriptor = None
    for klass in afpText_CPC.__mro__:
        if "VSFlags" in klass.__dict__:
            descriptor = klass.__dict__["VSFlags"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mca_is_not_abstract():
    assert not inspect.isabstract(afpText_MCA)


def test_afptext_mca_constructor_exists():
    assert callable(afpText_MCA.__init__)


def test_afptext_mca_constructor_args():
    sig = inspect.signature(afpText_MCA.__init__)
    params = list(sig.parameters.keys())



def test_afptext_mcc_is_not_abstract():
    assert not inspect.isabstract(afpText_MCC)


def test_afptext_mcc_constructor_exists():
    assert callable(afpText_MCC.__init__)


def test_afptext_mcc_constructor_args():
    sig = inspect.signature(afpText_MCC.__init__)
    params = list(sig.parameters.keys())



def test_afptext_mcf_is_not_abstract():
    assert not inspect.isabstract(afpText_MCF)


def test_afptext_mcf_constructor_exists():
    assert callable(afpText_MCF.__init__)


def test_afptext_mcf_constructor_args():
    sig = inspect.signature(afpText_MCF.__init__)
    params = list(sig.parameters.keys())



def test_afptext_edi_is_not_abstract():
    assert not inspect.isabstract(afpText_EDI)


def test_afptext_edi_constructor_exists():
    assert callable(afpText_EDI.__init__)


def test_afptext_edi_constructor_args():
    sig = inspect.signature(afpText_EDI.__init__)
    params = list(sig.parameters.keys())
    assert "IndxName" in params, "Missing parameter 'IndxName'"

def test_afptext_edi_has_IndxName():
    assert hasattr(afpText_EDI, "IndxName")
    descriptor = None
    for klass in afpText_EDI.__mro__:
        if "IndxName" in klass.__dict__:
            descriptor = klass.__dict__["IndxName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bdd_is_not_abstract():
    assert not inspect.isabstract(afpText_BDD)


def test_afptext_bdd_constructor_exists():
    assert callable(afpText_BDD.__init__)


def test_afptext_bdd_constructor_args():
    sig = inspect.signature(afpText_BDD.__init__)
    params = list(sig.parameters.keys())
    assert "MULT" in params, "Missing parameter 'MULT'"
    assert "WENE" in params, "Missing parameter 'WENE'"
    assert "YUPUB" in params, "Missing parameter 'YUPUB'"
    assert "ELEMENTHEIGHT" in params, "Missing parameter 'ELEMENTHEIGHT'"
    assert "YEXTENT" in params, "Missing parameter 'YEXTENT'"
    assert "MOD" in params, "Missing parameter 'MOD'"
    assert "XEXTENT" in params, "Missing parameter 'XEXTENT'"
    assert "LID" in params, "Missing parameter 'LID'"
    assert "MODULEWIDTH" in params, "Missing parameter 'MODULEWIDTH'"
    assert "XUPUB" in params, "Missing parameter 'XUPUB'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "UBASE" in params, "Missing parameter 'UBASE'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "TYPE" in params, "Missing parameter 'TYPE'"
    assert "COLOR" in params, "Missing parameter 'COLOR'"

def test_afptext_bdd_has_MULT():
    assert hasattr(afpText_BDD, "MULT")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "MULT" in klass.__dict__:
            descriptor = klass.__dict__["MULT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_WENE():
    assert hasattr(afpText_BDD, "WENE")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "WENE" in klass.__dict__:
            descriptor = klass.__dict__["WENE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_YUPUB():
    assert hasattr(afpText_BDD, "YUPUB")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "YUPUB" in klass.__dict__:
            descriptor = klass.__dict__["YUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_ELEMENTHEIGHT():
    assert hasattr(afpText_BDD, "ELEMENTHEIGHT")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "ELEMENTHEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["ELEMENTHEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_YEXTENT():
    assert hasattr(afpText_BDD, "YEXTENT")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "YEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["YEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_MOD():
    assert hasattr(afpText_BDD, "MOD")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "MOD" in klass.__dict__:
            descriptor = klass.__dict__["MOD"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_XEXTENT():
    assert hasattr(afpText_BDD, "XEXTENT")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "XEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["XEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_LID():
    assert hasattr(afpText_BDD, "LID")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_MODULEWIDTH():
    assert hasattr(afpText_BDD, "MODULEWIDTH")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "MODULEWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["MODULEWIDTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_XUPUB():
    assert hasattr(afpText_BDD, "XUPUB")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "XUPUB" in klass.__dict__:
            descriptor = klass.__dict__["XUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_Reserved2():
    assert hasattr(afpText_BDD, "Reserved2")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_UBASE():
    assert hasattr(afpText_BDD, "UBASE")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "UBASE" in klass.__dict__:
            descriptor = klass.__dict__["UBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_Reserved():
    assert hasattr(afpText_BDD, "Reserved")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_TYPE():
    assert hasattr(afpText_BDD, "TYPE")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "TYPE" in klass.__dict__:
            descriptor = klass.__dict__["TYPE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bdd_has_COLOR():
    assert hasattr(afpText_BDD, "COLOR")
    descriptor = None
    for klass in afpText_BDD.__mro__:
        if "COLOR" in klass.__dict__:
            descriptor = klass.__dict__["COLOR"]
            break
    assert isinstance(descriptor, property)



def test_afptext_mmd_is_not_abstract():
    assert not inspect.isabstract(afpText_MMD)


def test_afptext_mmd_constructor_exists():
    assert callable(afpText_MMD.__init__)


def test_afptext_mmd_constructor_args():
    sig = inspect.signature(afpText_MMD.__init__)
    params = list(sig.parameters.keys())



def test_afptext_bda_is_not_abstract():
    assert not inspect.isabstract(afpText_BDA)


def test_afptext_bda_constructor_exists():
    assert callable(afpText_BDA.__init__)


def test_afptext_bda_constructor_args():
    sig = inspect.signature(afpText_BDA.__init__)
    params = list(sig.parameters.keys())
    assert "Data" in params, "Missing parameter 'Data'"
    assert "Xoffset" in params, "Missing parameter 'Xoffset'"
    assert "Flags" in params, "Missing parameter 'Flags'"
    assert "Yoffset" in params, "Missing parameter 'Yoffset'"

def test_afptext_bda_has_Data():
    assert hasattr(afpText_BDA, "Data")
    descriptor = None
    for klass in afpText_BDA.__mro__:
        if "Data" in klass.__dict__:
            descriptor = klass.__dict__["Data"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bda_has_Xoffset():
    assert hasattr(afpText_BDA, "Xoffset")
    descriptor = None
    for klass in afpText_BDA.__mro__:
        if "Xoffset" in klass.__dict__:
            descriptor = klass.__dict__["Xoffset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bda_has_Flags():
    assert hasattr(afpText_BDA, "Flags")
    descriptor = None
    for klass in afpText_BDA.__mro__:
        if "Flags" in klass.__dict__:
            descriptor = klass.__dict__["Flags"]
            break
    assert isinstance(descriptor, property)

def test_afptext_bda_has_Yoffset():
    assert hasattr(afpText_BDA, "Yoffset")
    descriptor = None
    for klass in afpText_BDA.__mro__:
        if "Yoffset" in klass.__dict__:
            descriptor = klass.__dict__["Yoffset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bim_is_not_abstract():
    assert not inspect.isabstract(afpText_BIM)


def test_afptext_bim_constructor_exists():
    assert callable(afpText_BIM.__init__)


def test_afptext_bim_constructor_args():
    sig = inspect.signature(afpText_BIM.__init__)
    params = list(sig.parameters.keys())
    assert "IdoName" in params, "Missing parameter 'IdoName'"

def test_afptext_bim_has_IdoName():
    assert hasattr(afpText_BIM, "IdoName")
    descriptor = None
    for klass in afpText_BIM.__mro__:
        if "IdoName" in klass.__dict__:
            descriptor = klass.__dict__["IdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_bdx_is_not_abstract():
    assert not inspect.isabstract(afpText_BDX)


def test_afptext_bdx_constructor_exists():
    assert callable(afpText_BDX.__init__)


def test_afptext_bdx_constructor_args():
    sig = inspect.signature(afpText_BDX.__init__)
    params = list(sig.parameters.keys())
    assert "DMXName" in params, "Missing parameter 'DMXName'"

def test_afptext_bdx_has_DMXName():
    assert hasattr(afpText_BDX, "DMXName")
    descriptor = None
    for klass in afpText_BDX.__mro__:
        if "DMXName" in klass.__dict__:
            descriptor = klass.__dict__["DMXName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_linedata_is_not_abstract():
    assert not inspect.isabstract(afpText_LineData)


def test_afptext_linedata_constructor_exists():
    assert callable(afpText_LineData.__init__)


def test_afptext_linedata_constructor_args():
    sig = inspect.signature(afpText_LineData.__init__)
    params = list(sig.parameters.keys())
    assert "linedata" in params, "Missing parameter 'linedata'"

def test_afptext_linedata_has_linedata():
    assert hasattr(afpText_LineData, "linedata")
    descriptor = None
    for klass in afpText_LineData.__mro__:
        if "linedata" in klass.__dict__:
            descriptor = klass.__dict__["linedata"]
            break
    assert isinstance(descriptor, property)



def test_afptext_structuredfield_is_not_abstract():
    assert not inspect.isabstract(afpText_structuredField)


def test_afptext_structuredfield_constructor_exists():
    assert callable(afpText_structuredField.__init__)


def test_afptext_structuredfield_constructor_args():
    sig = inspect.signature(afpText_structuredField.__init__)
    params = list(sig.parameters.keys())



def test_afptext_model_is_not_abstract():
    assert not inspect.isabstract(afpText_Model)


def test_afptext_model_constructor_exists():
    assert callable(afpText_Model.__init__)


def test_afptext_model_constructor_args():
    sig = inspect.signature(afpText_Model.__init__)
    params = list(sig.parameters.keys())



def test_afptext_ipo_is_not_abstract():
    assert not inspect.isabstract(afpText_IPO)


def test_afptext_ipo_constructor_exists():
    assert callable(afpText_IPO.__init__)


def test_afptext_ipo_constructor_args():
    sig = inspect.signature(afpText_IPO.__init__)
    params = list(sig.parameters.keys())
    assert "OvlyName" in params, "Missing parameter 'OvlyName'"
    assert "YolOset" in params, "Missing parameter 'YolOset'"
    assert "XolOset" in params, "Missing parameter 'XolOset'"
    assert "OvlyOrent" in params, "Missing parameter 'OvlyOrent'"

def test_afptext_ipo_has_OvlyName():
    assert hasattr(afpText_IPO, "OvlyName")
    descriptor = None
    for klass in afpText_IPO.__mro__:
        if "OvlyName" in klass.__dict__:
            descriptor = klass.__dict__["OvlyName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ipo_has_YolOset():
    assert hasattr(afpText_IPO, "YolOset")
    descriptor = None
    for klass in afpText_IPO.__mro__:
        if "YolOset" in klass.__dict__:
            descriptor = klass.__dict__["YolOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ipo_has_XolOset():
    assert hasattr(afpText_IPO, "XolOset")
    descriptor = None
    for klass in afpText_IPO.__mro__:
        if "XolOset" in klass.__dict__:
            descriptor = klass.__dict__["XolOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ipo_has_OvlyOrent():
    assert hasattr(afpText_IPO, "OvlyOrent")
    descriptor = None
    for klass in afpText_IPO.__mro__:
        if "OvlyOrent" in klass.__dict__:
            descriptor = klass.__dict__["OvlyOrent"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ird_is_not_abstract():
    assert not inspect.isabstract(afpText_IRD)


def test_afptext_ird_constructor_exists():
    assert callable(afpText_IRD.__init__)


def test_afptext_ird_constructor_args():
    sig = inspect.signature(afpText_IRD.__init__)
    params = list(sig.parameters.keys())
    assert "IMdata" in params, "Missing parameter 'IMdata'"

def test_afptext_ird_has_IMdata():
    assert hasattr(afpText_IRD, "IMdata")
    descriptor = None
    for klass in afpText_IRD.__mro__:
        if "IMdata" in klass.__dict__:
            descriptor = klass.__dict__["IMdata"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ips_is_not_abstract():
    assert not inspect.isabstract(afpText_IPS)


def test_afptext_ips_constructor_exists():
    assert callable(afpText_IPS.__init__)


def test_afptext_ips_constructor_args():
    sig = inspect.signature(afpText_IPS.__init__)
    params = list(sig.parameters.keys())
    assert "YpsOset" in params, "Missing parameter 'YpsOset'"
    assert "PsegName" in params, "Missing parameter 'PsegName'"
    assert "XpsOset" in params, "Missing parameter 'XpsOset'"

def test_afptext_ips_has_YpsOset():
    assert hasattr(afpText_IPS, "YpsOset")
    descriptor = None
    for klass in afpText_IPS.__mro__:
        if "YpsOset" in klass.__dict__:
            descriptor = klass.__dict__["YpsOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ips_has_PsegName():
    assert hasattr(afpText_IPS, "PsegName")
    descriptor = None
    for klass in afpText_IPS.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ips_has_XpsOset():
    assert hasattr(afpText_IPS, "XpsOset")
    descriptor = None
    for klass in afpText_IPS.__mro__:
        if "XpsOset" in klass.__dict__:
            descriptor = klass.__dict__["XpsOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ipg_is_not_abstract():
    assert not inspect.isabstract(afpText_IPG)


def test_afptext_ipg_constructor_exists():
    assert callable(afpText_IPG.__init__)


def test_afptext_ipg_constructor_args():
    sig = inspect.signature(afpText_IPG.__init__)
    params = list(sig.parameters.keys())
    assert "PgName" in params, "Missing parameter 'PgName'"
    assert "IPgFlgs" in params, "Missing parameter 'IPgFlgs'"

def test_afptext_ipg_has_PgName():
    assert hasattr(afpText_IPG, "PgName")
    descriptor = None
    for klass in afpText_IPG.__mro__:
        if "PgName" in klass.__dict__:
            descriptor = klass.__dict__["PgName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ipg_has_IPgFlgs():
    assert hasattr(afpText_IPG, "IPgFlgs")
    descriptor = None
    for klass in afpText_IPG.__mro__:
        if "IPgFlgs" in klass.__dict__:
            descriptor = klass.__dict__["IPgFlgs"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ipd_is_not_abstract():
    assert not inspect.isabstract(afpText_IPD)


def test_afptext_ipd_constructor_exists():
    assert callable(afpText_IPD.__init__)


def test_afptext_ipd_constructor_args():
    sig = inspect.signature(afpText_IPD.__init__)
    params = list(sig.parameters.keys())
    assert "imageData" in params, "Missing parameter 'imageData'"
    assert "IOCAdat" in params, "Missing parameter 'IOCAdat'"

def test_afptext_ipd_has_imageData():
    assert hasattr(afpText_IPD, "imageData")
    descriptor = None
    for klass in afpText_IPD.__mro__:
        if "imageData" in klass.__dict__:
            descriptor = klass.__dict__["imageData"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ipd_has_IOCAdat():
    assert hasattr(afpText_IPD, "IOCAdat")
    descriptor = None
    for klass in afpText_IPD.__mro__:
        if "IOCAdat" in klass.__dict__:
            descriptor = klass.__dict__["IOCAdat"]
            break
    assert isinstance(descriptor, property)



def test_afptext_icp_is_not_abstract():
    assert not inspect.isabstract(afpText_ICP)


def test_afptext_icp_constructor_exists():
    assert callable(afpText_ICP.__init__)


def test_afptext_icp_constructor_args():
    sig = inspect.signature(afpText_ICP.__init__)
    params = list(sig.parameters.keys())
    assert "XCSize" in params, "Missing parameter 'XCSize'"
    assert "XFilSize" in params, "Missing parameter 'XFilSize'"
    assert "YCSize" in params, "Missing parameter 'YCSize'"
    assert "XCOset" in params, "Missing parameter 'XCOset'"
    assert "YCOset" in params, "Missing parameter 'YCOset'"
    assert "YFilSize" in params, "Missing parameter 'YFilSize'"

def test_afptext_icp_has_XCSize():
    assert hasattr(afpText_ICP, "XCSize")
    descriptor = None
    for klass in afpText_ICP.__mro__:
        if "XCSize" in klass.__dict__:
            descriptor = klass.__dict__["XCSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_icp_has_XFilSize():
    assert hasattr(afpText_ICP, "XFilSize")
    descriptor = None
    for klass in afpText_ICP.__mro__:
        if "XFilSize" in klass.__dict__:
            descriptor = klass.__dict__["XFilSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_icp_has_YCSize():
    assert hasattr(afpText_ICP, "YCSize")
    descriptor = None
    for klass in afpText_ICP.__mro__:
        if "YCSize" in klass.__dict__:
            descriptor = klass.__dict__["YCSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_icp_has_XCOset():
    assert hasattr(afpText_ICP, "XCOset")
    descriptor = None
    for klass in afpText_ICP.__mro__:
        if "XCOset" in klass.__dict__:
            descriptor = klass.__dict__["XCOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_icp_has_YCOset():
    assert hasattr(afpText_ICP, "YCOset")
    descriptor = None
    for klass in afpText_ICP.__mro__:
        if "YCOset" in klass.__dict__:
            descriptor = klass.__dict__["YCOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_icp_has_YFilSize():
    assert hasattr(afpText_ICP, "YFilSize")
    descriptor = None
    for klass in afpText_ICP.__mro__:
        if "YFilSize" in klass.__dict__:
            descriptor = klass.__dict__["YFilSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ioc_is_not_abstract():
    assert not inspect.isabstract(afpText_IOC)


def test_afptext_ioc_constructor_exists():
    assert callable(afpText_IOC.__init__)


def test_afptext_ioc_constructor_args():
    sig = inspect.signature(afpText_IOC.__init__)
    params = list(sig.parameters.keys())
    assert "XMap" in params, "Missing parameter 'XMap'"
    assert "XoaOset" in params, "Missing parameter 'XoaOset'"
    assert "ConData1" in params, "Missing parameter 'ConData1'"
    assert "YMap" in params, "Missing parameter 'YMap'"
    assert "YoaOrent" in params, "Missing parameter 'YoaOrent'"
    assert "ConData2" in params, "Missing parameter 'ConData2'"
    assert "XoaOrent" in params, "Missing parameter 'XoaOrent'"
    assert "YoaOset" in params, "Missing parameter 'YoaOset'"

def test_afptext_ioc_has_XMap():
    assert hasattr(afpText_IOC, "XMap")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "XMap" in klass.__dict__:
            descriptor = klass.__dict__["XMap"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_XoaOset():
    assert hasattr(afpText_IOC, "XoaOset")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "XoaOset" in klass.__dict__:
            descriptor = klass.__dict__["XoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_ConData1():
    assert hasattr(afpText_IOC, "ConData1")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "ConData1" in klass.__dict__:
            descriptor = klass.__dict__["ConData1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_YMap():
    assert hasattr(afpText_IOC, "YMap")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "YMap" in klass.__dict__:
            descriptor = klass.__dict__["YMap"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_YoaOrent():
    assert hasattr(afpText_IOC, "YoaOrent")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "YoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_ConData2():
    assert hasattr(afpText_IOC, "ConData2")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "ConData2" in klass.__dict__:
            descriptor = klass.__dict__["ConData2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_XoaOrent():
    assert hasattr(afpText_IOC, "XoaOrent")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "XoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_ioc_has_YoaOset():
    assert hasattr(afpText_IOC, "YoaOset")
    descriptor = None
    for klass in afpText_IOC.__mro__:
        if "YoaOset" in klass.__dict__:
            descriptor = klass.__dict__["YoaOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_iob_is_not_abstract():
    assert not inspect.isabstract(afpText_IOB)


def test_afptext_iob_constructor_exists():
    assert callable(afpText_IOB.__init__)


def test_afptext_iob_constructor_args():
    sig = inspect.signature(afpText_IOB.__init__)
    params = list(sig.parameters.keys())
    assert "XoaOrent" in params, "Missing parameter 'XoaOrent'"
    assert "YoaOrent" in params, "Missing parameter 'YoaOrent'"
    assert "XoaOset" in params, "Missing parameter 'XoaOset'"
    assert "XocaOset" in params, "Missing parameter 'XocaOset'"
    assert "ObjName" in params, "Missing parameter 'ObjName'"
    assert "YocaOset" in params, "Missing parameter 'YocaOset'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "RefCSys" in params, "Missing parameter 'RefCSys'"
    assert "YoaOset" in params, "Missing parameter 'YoaOset'"

def test_afptext_iob_has_XoaOrent():
    assert hasattr(afpText_IOB, "XoaOrent")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "XoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_YoaOrent():
    assert hasattr(afpText_IOB, "YoaOrent")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "YoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_XoaOset():
    assert hasattr(afpText_IOB, "XoaOset")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "XoaOset" in klass.__dict__:
            descriptor = klass.__dict__["XoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_XocaOset():
    assert hasattr(afpText_IOB, "XocaOset")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "XocaOset" in klass.__dict__:
            descriptor = klass.__dict__["XocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_ObjName():
    assert hasattr(afpText_IOB, "ObjName")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "ObjName" in klass.__dict__:
            descriptor = klass.__dict__["ObjName"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_YocaOset():
    assert hasattr(afpText_IOB, "YocaOset")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "YocaOset" in klass.__dict__:
            descriptor = klass.__dict__["YocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_ObjType():
    assert hasattr(afpText_IOB, "ObjType")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_RefCSys():
    assert hasattr(afpText_IOB, "RefCSys")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "RefCSys" in klass.__dict__:
            descriptor = klass.__dict__["RefCSys"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iob_has_YoaOset():
    assert hasattr(afpText_IOB, "YoaOset")
    descriptor = None
    for klass in afpText_IOB.__mro__:
        if "YoaOset" in klass.__dict__:
            descriptor = klass.__dict__["YoaOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext_imm_is_not_abstract():
    assert not inspect.isabstract(afpText_IMM)


def test_afptext_imm_constructor_exists():
    assert callable(afpText_IMM.__init__)


def test_afptext_imm_constructor_args():
    sig = inspect.signature(afpText_IMM.__init__)
    params = list(sig.parameters.keys())
    assert "MMPName" in params, "Missing parameter 'MMPName'"

def test_afptext_imm_has_MMPName():
    assert hasattr(afpText_IMM, "MMPName")
    descriptor = None
    for klass in afpText_IMM.__mro__:
        if "MMPName" in klass.__dict__:
            descriptor = klass.__dict__["MMPName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_iid_is_not_abstract():
    assert not inspect.isabstract(afpText_IID)


def test_afptext_iid_constructor_exists():
    assert callable(afpText_IID.__init__)


def test_afptext_iid_constructor_args():
    sig = inspect.signature(afpText_IID.__init__)
    params = list(sig.parameters.keys())
    assert "YSize" in params, "Missing parameter 'YSize'"
    assert "YCSizeD" in params, "Missing parameter 'YCSizeD'"
    assert "YBase" in params, "Missing parameter 'YBase'"
    assert "ConData3" in params, "Missing parameter 'ConData3'"
    assert "YUnits" in params, "Missing parameter 'YUnits'"
    assert "XBase" in params, "Missing parameter 'XBase'"
    assert "XCSizeD" in params, "Missing parameter 'XCSizeD'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "XSize" in params, "Missing parameter 'XSize'"
    assert "ConData2" in params, "Missing parameter 'ConData2'"
    assert "ConData1" in params, "Missing parameter 'ConData1'"
    assert "XUnits" in params, "Missing parameter 'XUnits'"

def test_afptext_iid_has_YSize():
    assert hasattr(afpText_IID, "YSize")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "YSize" in klass.__dict__:
            descriptor = klass.__dict__["YSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_YCSizeD():
    assert hasattr(afpText_IID, "YCSizeD")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "YCSizeD" in klass.__dict__:
            descriptor = klass.__dict__["YCSizeD"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_YBase():
    assert hasattr(afpText_IID, "YBase")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "YBase" in klass.__dict__:
            descriptor = klass.__dict__["YBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_ConData3():
    assert hasattr(afpText_IID, "ConData3")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "ConData3" in klass.__dict__:
            descriptor = klass.__dict__["ConData3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_YUnits():
    assert hasattr(afpText_IID, "YUnits")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "YUnits" in klass.__dict__:
            descriptor = klass.__dict__["YUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_XBase():
    assert hasattr(afpText_IID, "XBase")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "XBase" in klass.__dict__:
            descriptor = klass.__dict__["XBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_XCSizeD():
    assert hasattr(afpText_IID, "XCSizeD")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "XCSizeD" in klass.__dict__:
            descriptor = klass.__dict__["XCSizeD"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_Color():
    assert hasattr(afpText_IID, "Color")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_XSize():
    assert hasattr(afpText_IID, "XSize")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "XSize" in klass.__dict__:
            descriptor = klass.__dict__["XSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_ConData2():
    assert hasattr(afpText_IID, "ConData2")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "ConData2" in klass.__dict__:
            descriptor = klass.__dict__["ConData2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_ConData1():
    assert hasattr(afpText_IID, "ConData1")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "ConData1" in klass.__dict__:
            descriptor = klass.__dict__["ConData1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_iid_has_XUnits():
    assert hasattr(afpText_IID, "XUnits")
    descriptor = None
    for klass in afpText_IID.__mro__:
        if "XUnits" in klass.__dict__:
            descriptor = klass.__dict__["XUnits"]
            break
    assert isinstance(descriptor, property)



def test_afptext_iel_is_not_abstract():
    assert not inspect.isabstract(afpText_IEL)


def test_afptext_iel_constructor_exists():
    assert callable(afpText_IEL.__init__)


def test_afptext_iel_constructor_args():
    sig = inspect.signature(afpText_IEL.__init__)
    params = list(sig.parameters.keys())



def test_afptext_idd_is_not_abstract():
    assert not inspect.isabstract(afpText_IDD)


def test_afptext_idd_constructor_exists():
    assert callable(afpText_IDD.__init__)


def test_afptext_idd_constructor_args():
    sig = inspect.signature(afpText_IDD.__init__)
    params = list(sig.parameters.keys())
    assert "YSIZE" in params, "Missing parameter 'YSIZE'"
    assert "YRESOL" in params, "Missing parameter 'YRESOL'"
    assert "XRESOL" in params, "Missing parameter 'XRESOL'"
    assert "XSIZE" in params, "Missing parameter 'XSIZE'"
    assert "UNITBASE" in params, "Missing parameter 'UNITBASE'"

def test_afptext_idd_has_YSIZE():
    assert hasattr(afpText_IDD, "YSIZE")
    descriptor = None
    for klass in afpText_IDD.__mro__:
        if "YSIZE" in klass.__dict__:
            descriptor = klass.__dict__["YSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idd_has_YRESOL():
    assert hasattr(afpText_IDD, "YRESOL")
    descriptor = None
    for klass in afpText_IDD.__mro__:
        if "YRESOL" in klass.__dict__:
            descriptor = klass.__dict__["YRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idd_has_XRESOL():
    assert hasattr(afpText_IDD, "XRESOL")
    descriptor = None
    for klass in afpText_IDD.__mro__:
        if "XRESOL" in klass.__dict__:
            descriptor = klass.__dict__["XRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idd_has_XSIZE():
    assert hasattr(afpText_IDD, "XSIZE")
    descriptor = None
    for klass in afpText_IDD.__mro__:
        if "XSIZE" in klass.__dict__:
            descriptor = klass.__dict__["XSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext_idd_has_UNITBASE():
    assert hasattr(afpText_IDD, "UNITBASE")
    descriptor = None
    for klass in afpText_IDD.__mro__:
        if "UNITBASE" in klass.__dict__:
            descriptor = klass.__dict__["UNITBASE"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gdd_is_not_abstract():
    assert not inspect.isabstract(afpText_GDD)


def test_afptext_gdd_constructor_exists():
    assert callable(afpText_GDD.__init__)


def test_afptext_gdd_constructor_args():
    sig = inspect.signature(afpText_GDD.__init__)
    params = list(sig.parameters.keys())
    assert "GOCAdes" in params, "Missing parameter 'GOCAdes'"

def test_afptext_gdd_has_GOCAdes():
    assert hasattr(afpText_GDD, "GOCAdes")
    descriptor = None
    for klass in afpText_GDD.__mro__:
        if "GOCAdes" in klass.__dict__:
            descriptor = klass.__dict__["GOCAdes"]
            break
    assert isinstance(descriptor, property)



def test_afptext_gad_is_not_abstract():
    assert not inspect.isabstract(afpText_GAD)


def test_afptext_gad_constructor_exists():
    assert callable(afpText_GAD.__init__)


def test_afptext_gad_constructor_args():
    sig = inspect.signature(afpText_GAD.__init__)
    params = list(sig.parameters.keys())
    assert "GOCAdat" in params, "Missing parameter 'GOCAdat'"

def test_afptext_gad_has_GOCAdat():
    assert hasattr(afpText_GAD, "GOCAdat")
    descriptor = None
    for klass in afpText_GAD.__mro__:
        if "GOCAdat" in klass.__dict__:
            descriptor = klass.__dict__["GOCAdat"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnprg_is_not_abstract():
    assert not inspect.isabstract(afpText_FNPRG)


def test_afptext_fnprg_constructor_exists():
    assert callable(afpText_FNPRG.__init__)


def test_afptext_fnprg_constructor_args():
    sig = inspect.signature(afpText_FNPRG.__init__)
    params = list(sig.parameters.keys())
    assert "LcHeight" in params, "Missing parameter 'LcHeight'"
    assert "MaxDesDp" in params, "Missing parameter 'MaxDesDp'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "Reserved3" in params, "Missing parameter 'Reserved3'"
    assert "UscoreWdf" in params, "Missing parameter 'UscoreWdf'"
    assert "Retired" in params, "Missing parameter 'Retired'"
    assert "CapMHt" in params, "Missing parameter 'CapMHt'"
    assert "MaxAscHt" in params, "Missing parameter 'MaxAscHt'"
    assert "UscoreWd" in params, "Missing parameter 'UscoreWd'"
    assert "UscorePos" in params, "Missing parameter 'UscorePos'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext_fnprg_has_LcHeight():
    assert hasattr(afpText_FNPRG, "LcHeight")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "LcHeight" in klass.__dict__:
            descriptor = klass.__dict__["LcHeight"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_MaxDesDp():
    assert hasattr(afpText_FNPRG, "MaxDesDp")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "MaxDesDp" in klass.__dict__:
            descriptor = klass.__dict__["MaxDesDp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_Reserved2():
    assert hasattr(afpText_FNPRG, "Reserved2")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_Reserved3():
    assert hasattr(afpText_FNPRG, "Reserved3")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "Reserved3" in klass.__dict__:
            descriptor = klass.__dict__["Reserved3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_UscoreWdf():
    assert hasattr(afpText_FNPRG, "UscoreWdf")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "UscoreWdf" in klass.__dict__:
            descriptor = klass.__dict__["UscoreWdf"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_Retired():
    assert hasattr(afpText_FNPRG, "Retired")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "Retired" in klass.__dict__:
            descriptor = klass.__dict__["Retired"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_CapMHt():
    assert hasattr(afpText_FNPRG, "CapMHt")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "CapMHt" in klass.__dict__:
            descriptor = klass.__dict__["CapMHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_MaxAscHt():
    assert hasattr(afpText_FNPRG, "MaxAscHt")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "MaxAscHt" in klass.__dict__:
            descriptor = klass.__dict__["MaxAscHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_UscoreWd():
    assert hasattr(afpText_FNPRG, "UscoreWd")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "UscoreWd" in klass.__dict__:
            descriptor = klass.__dict__["UscoreWd"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_UscorePos():
    assert hasattr(afpText_FNPRG, "UscorePos")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "UscorePos" in klass.__dict__:
            descriptor = klass.__dict__["UscorePos"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnprg_has_Reserved():
    assert hasattr(afpText_FNPRG, "Reserved")
    descriptor = None
    for klass in afpText_FNPRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnp_is_not_abstract():
    assert not inspect.isabstract(afpText_FNP)


def test_afptext_fnp_constructor_exists():
    assert callable(afpText_FNP.__init__)


def test_afptext_fnp_constructor_args():
    sig = inspect.signature(afpText_FNP.__init__)
    params = list(sig.parameters.keys())



def test_afptext_fnorg_is_not_abstract():
    assert not inspect.isabstract(afpText_FNORG)


def test_afptext_fnorg_constructor_exists():
    assert callable(afpText_FNORG.__init__)


def test_afptext_fnorg_constructor_args():
    sig = inspect.signature(afpText_FNORG.__init__)
    params = list(sig.parameters.keys())
    assert "MaxCharInc" in params, "Missing parameter 'MaxCharInc'"
    assert "NomCharInc" in params, "Missing parameter 'NomCharInc'"
    assert "MaxBOset" in params, "Missing parameter 'MaxBOset'"
    assert "DefBInc" in params, "Missing parameter 'DefBInc'"
    assert "FigSpInc" in params, "Missing parameter 'FigSpInc'"
    assert "Reserved3" in params, "Missing parameter 'Reserved3'"
    assert "CharRot" in params, "Missing parameter 'CharRot'"
    assert "EmSpInc" in params, "Missing parameter 'EmSpInc'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "OrntFlgs" in params, "Missing parameter 'OrntFlgs'"
    assert "MaxBExt" in params, "Missing parameter 'MaxBExt'"
    assert "SpCharInc" in params, "Missing parameter 'SpCharInc'"
    assert "MinASp" in params, "Missing parameter 'MinASp'"

def test_afptext_fnorg_has_MaxCharInc():
    assert hasattr(afpText_FNORG, "MaxCharInc")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "MaxCharInc" in klass.__dict__:
            descriptor = klass.__dict__["MaxCharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_NomCharInc():
    assert hasattr(afpText_FNORG, "NomCharInc")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "NomCharInc" in klass.__dict__:
            descriptor = klass.__dict__["NomCharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_MaxBOset():
    assert hasattr(afpText_FNORG, "MaxBOset")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "MaxBOset" in klass.__dict__:
            descriptor = klass.__dict__["MaxBOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_DefBInc():
    assert hasattr(afpText_FNORG, "DefBInc")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "DefBInc" in klass.__dict__:
            descriptor = klass.__dict__["DefBInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_FigSpInc():
    assert hasattr(afpText_FNORG, "FigSpInc")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "FigSpInc" in klass.__dict__:
            descriptor = klass.__dict__["FigSpInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_Reserved3():
    assert hasattr(afpText_FNORG, "Reserved3")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "Reserved3" in klass.__dict__:
            descriptor = klass.__dict__["Reserved3"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_CharRot():
    assert hasattr(afpText_FNORG, "CharRot")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_EmSpInc():
    assert hasattr(afpText_FNORG, "EmSpInc")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "EmSpInc" in klass.__dict__:
            descriptor = klass.__dict__["EmSpInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_Reserved():
    assert hasattr(afpText_FNORG, "Reserved")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_Reserved2():
    assert hasattr(afpText_FNORG, "Reserved2")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_OrntFlgs():
    assert hasattr(afpText_FNORG, "OrntFlgs")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "OrntFlgs" in klass.__dict__:
            descriptor = klass.__dict__["OrntFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_MaxBExt():
    assert hasattr(afpText_FNORG, "MaxBExt")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "MaxBExt" in klass.__dict__:
            descriptor = klass.__dict__["MaxBExt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_SpCharInc():
    assert hasattr(afpText_FNORG, "SpCharInc")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "SpCharInc" in klass.__dict__:
            descriptor = klass.__dict__["SpCharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnorg_has_MinASp():
    assert hasattr(afpText_FNORG, "MinASp")
    descriptor = None
    for klass in afpText_FNORG.__mro__:
        if "MinASp" in klass.__dict__:
            descriptor = klass.__dict__["MinASp"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fno_is_not_abstract():
    assert not inspect.isabstract(afpText_FNO)


def test_afptext_fno_constructor_exists():
    assert callable(afpText_FNO.__init__)


def test_afptext_fno_constructor_args():
    sig = inspect.signature(afpText_FNO.__init__)
    params = list(sig.parameters.keys())



def test_afptext_fnmrg_is_not_abstract():
    assert not inspect.isabstract(afpText_FNMRG)


def test_afptext_fnmrg_constructor_exists():
    assert callable(afpText_FNMRG.__init__)


def test_afptext_fnmrg_constructor_args():
    sig = inspect.signature(afpText_FNMRG.__init__)
    params = list(sig.parameters.keys())
    assert "PatDOset" in params, "Missing parameter 'PatDOset'"
    assert "CharBoxHt" in params, "Missing parameter 'CharBoxHt'"
    assert "CharBoxWd" in params, "Missing parameter 'CharBoxWd'"

def test_afptext_fnmrg_has_PatDOset():
    assert hasattr(afpText_FNMRG, "PatDOset")
    descriptor = None
    for klass in afpText_FNMRG.__mro__:
        if "PatDOset" in klass.__dict__:
            descriptor = klass.__dict__["PatDOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnmrg_has_CharBoxHt():
    assert hasattr(afpText_FNMRG, "CharBoxHt")
    descriptor = None
    for klass in afpText_FNMRG.__mro__:
        if "CharBoxHt" in klass.__dict__:
            descriptor = klass.__dict__["CharBoxHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnmrg_has_CharBoxWd():
    assert hasattr(afpText_FNMRG, "CharBoxWd")
    descriptor = None
    for klass in afpText_FNMRG.__mro__:
        if "CharBoxWd" in klass.__dict__:
            descriptor = klass.__dict__["CharBoxWd"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnm_is_not_abstract():
    assert not inspect.isabstract(afpText_FNM)


def test_afptext_fnm_constructor_exists():
    assert callable(afpText_FNM.__init__)


def test_afptext_fnm_constructor_args():
    sig = inspect.signature(afpText_FNM.__init__)
    params = list(sig.parameters.keys())



def test_afptext_fnn_is_not_abstract():
    assert not inspect.isabstract(afpText_FNN)


def test_afptext_fnn_constructor_exists():
    assert callable(afpText_FNN.__init__)


def test_afptext_fnn_constructor_args():
    sig = inspect.signature(afpText_FNN.__init__)
    params = list(sig.parameters.keys())
    assert "FNNData" in params, "Missing parameter 'FNNData'"

def test_afptext_fnn_has_FNNData():
    assert hasattr(afpText_FNN, "FNNData")
    descriptor = None
    for klass in afpText_FNN.__mro__:
        if "FNNData" in klass.__dict__:
            descriptor = klass.__dict__["FNNData"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnirg_is_not_abstract():
    assert not inspect.isabstract(afpText_FNIRG)


def test_afptext_fnirg_constructor_exists():
    assert callable(afpText_FNIRG.__init__)


def test_afptext_fnirg_constructor_args():
    sig = inspect.signature(afpText_FNIRG.__init__)
    params = list(sig.parameters.keys())
    assert "FNMCnt" in params, "Missing parameter 'FNMCnt'"
    assert "CharInc" in params, "Missing parameter 'CharInc'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "BaseOset" in params, "Missing parameter 'BaseOset'"
    assert "CSpace" in params, "Missing parameter 'CSpace'"
    assert "GCGID" in params, "Missing parameter 'GCGID'"
    assert "BSpace" in params, "Missing parameter 'BSpace'"
    assert "ASpace" in params, "Missing parameter 'ASpace'"
    assert "DescendDp" in params, "Missing parameter 'DescendDp'"
    assert "AscendHt" in params, "Missing parameter 'AscendHt'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"

def test_afptext_fnirg_has_FNMCnt():
    assert hasattr(afpText_FNIRG, "FNMCnt")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "FNMCnt" in klass.__dict__:
            descriptor = klass.__dict__["FNMCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_CharInc():
    assert hasattr(afpText_FNIRG, "CharInc")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "CharInc" in klass.__dict__:
            descriptor = klass.__dict__["CharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_Reserved():
    assert hasattr(afpText_FNIRG, "Reserved")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_BaseOset():
    assert hasattr(afpText_FNIRG, "BaseOset")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "BaseOset" in klass.__dict__:
            descriptor = klass.__dict__["BaseOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_CSpace():
    assert hasattr(afpText_FNIRG, "CSpace")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "CSpace" in klass.__dict__:
            descriptor = klass.__dict__["CSpace"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_GCGID():
    assert hasattr(afpText_FNIRG, "GCGID")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "GCGID" in klass.__dict__:
            descriptor = klass.__dict__["GCGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_BSpace():
    assert hasattr(afpText_FNIRG, "BSpace")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "BSpace" in klass.__dict__:
            descriptor = klass.__dict__["BSpace"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_ASpace():
    assert hasattr(afpText_FNIRG, "ASpace")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "ASpace" in klass.__dict__:
            descriptor = klass.__dict__["ASpace"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_DescendDp():
    assert hasattr(afpText_FNIRG, "DescendDp")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "DescendDp" in klass.__dict__:
            descriptor = klass.__dict__["DescendDp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_AscendHt():
    assert hasattr(afpText_FNIRG, "AscendHt")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "AscendHt" in klass.__dict__:
            descriptor = klass.__dict__["AscendHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnirg_has_Reserved2():
    assert hasattr(afpText_FNIRG, "Reserved2")
    descriptor = None
    for klass in afpText_FNIRG.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fni_is_not_abstract():
    assert not inspect.isabstract(afpText_FNI)


def test_afptext_fni_constructor_exists():
    assert callable(afpText_FNI.__init__)


def test_afptext_fni_constructor_args():
    sig = inspect.signature(afpText_FNI.__init__)
    params = list(sig.parameters.keys())



def test_afptext_fng_is_not_abstract():
    assert not inspect.isabstract(afpText_FNG)


def test_afptext_fng_constructor_exists():
    assert callable(afpText_FNG.__init__)


def test_afptext_fng_constructor_args():
    sig = inspect.signature(afpText_FNG.__init__)
    params = list(sig.parameters.keys())
    assert "PatData" in params, "Missing parameter 'PatData'"

def test_afptext_fng_has_PatData():
    assert hasattr(afpText_FNG, "PatData")
    descriptor = None
    for klass in afpText_FNG.__mro__:
        if "PatData" in klass.__dict__:
            descriptor = klass.__dict__["PatData"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ept_is_not_abstract():
    assert not inspect.isabstract(afpText_EPT)


def test_afptext_ept_constructor_exists():
    assert callable(afpText_EPT.__init__)


def test_afptext_ept_constructor_args():
    sig = inspect.signature(afpText_EPT.__init__)
    params = list(sig.parameters.keys())
    assert "PTdoName" in params, "Missing parameter 'PTdoName'"

def test_afptext_ept_has_PTdoName():
    assert hasattr(afpText_EPT, "PTdoName")
    descriptor = None
    for klass in afpText_EPT.__mro__:
        if "PTdoName" in klass.__dict__:
            descriptor = klass.__dict__["PTdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnd_is_not_abstract():
    assert not inspect.isabstract(afpText_FND)


def test_afptext_fnd_constructor_exists():
    assert callable(afpText_FND.__init__)


def test_afptext_fnd_constructor_args():
    sig = inspect.signature(afpText_FND.__init__)
    params = list(sig.parameters.keys())
    assert "MinPtSize" in params, "Missing parameter 'MinPtSize'"
    assert "TypeFcDesc" in params, "Missing parameter 'TypeFcDesc'"
    assert "MaxPtSize" in params, "Missing parameter 'MaxPtSize'"
    assert "DsnGenCls" in params, "Missing parameter 'DsnGenCls'"
    assert "DsnSpcGrp" in params, "Missing parameter 'DsnSpcGrp'"
    assert "FtWdClass" in params, "Missing parameter 'FtWdClass'"
    assert "FtWtClass" in params, "Missing parameter 'FtWtClass'"
    assert "NomHSize" in params, "Missing parameter 'NomHSize'"
    assert "MaxHSize" in params, "Missing parameter 'MaxHSize'"
    assert "Reserved1" in params, "Missing parameter 'Reserved1'"
    assert "DsnSubCls" in params, "Missing parameter 'DsnSubCls'"
    assert "MinHSize" in params, "Missing parameter 'MinHSize'"
    assert "FGID" in params, "Missing parameter 'FGID'"
    assert "GCSID" in params, "Missing parameter 'GCSID'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "NomPtSize" in params, "Missing parameter 'NomPtSize'"
    assert "FtDsFlags" in params, "Missing parameter 'FtDsFlags'"

def test_afptext_fnd_has_MinPtSize():
    assert hasattr(afpText_FND, "MinPtSize")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "MinPtSize" in klass.__dict__:
            descriptor = klass.__dict__["MinPtSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_TypeFcDesc():
    assert hasattr(afpText_FND, "TypeFcDesc")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "TypeFcDesc" in klass.__dict__:
            descriptor = klass.__dict__["TypeFcDesc"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_MaxPtSize():
    assert hasattr(afpText_FND, "MaxPtSize")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "MaxPtSize" in klass.__dict__:
            descriptor = klass.__dict__["MaxPtSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_DsnGenCls():
    assert hasattr(afpText_FND, "DsnGenCls")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "DsnGenCls" in klass.__dict__:
            descriptor = klass.__dict__["DsnGenCls"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_DsnSpcGrp():
    assert hasattr(afpText_FND, "DsnSpcGrp")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "DsnSpcGrp" in klass.__dict__:
            descriptor = klass.__dict__["DsnSpcGrp"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_FtWdClass():
    assert hasattr(afpText_FND, "FtWdClass")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "FtWdClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWdClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_FtWtClass():
    assert hasattr(afpText_FND, "FtWtClass")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "FtWtClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWtClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_NomHSize():
    assert hasattr(afpText_FND, "NomHSize")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "NomHSize" in klass.__dict__:
            descriptor = klass.__dict__["NomHSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_MaxHSize():
    assert hasattr(afpText_FND, "MaxHSize")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "MaxHSize" in klass.__dict__:
            descriptor = klass.__dict__["MaxHSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_Reserved1():
    assert hasattr(afpText_FND, "Reserved1")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "Reserved1" in klass.__dict__:
            descriptor = klass.__dict__["Reserved1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_DsnSubCls():
    assert hasattr(afpText_FND, "DsnSubCls")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "DsnSubCls" in klass.__dict__:
            descriptor = klass.__dict__["DsnSubCls"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_MinHSize():
    assert hasattr(afpText_FND, "MinHSize")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "MinHSize" in klass.__dict__:
            descriptor = klass.__dict__["MinHSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_FGID():
    assert hasattr(afpText_FND, "FGID")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "FGID" in klass.__dict__:
            descriptor = klass.__dict__["FGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_GCSID():
    assert hasattr(afpText_FND, "GCSID")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "GCSID" in klass.__dict__:
            descriptor = klass.__dict__["GCSID"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_Reserved2():
    assert hasattr(afpText_FND, "Reserved2")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_NomPtSize():
    assert hasattr(afpText_FND, "NomPtSize")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "NomPtSize" in klass.__dict__:
            descriptor = klass.__dict__["NomPtSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnd_has_FtDsFlags():
    assert hasattr(afpText_FND, "FtDsFlags")
    descriptor = None
    for klass in afpText_FND.__mro__:
        if "FtDsFlags" in klass.__dict__:
            descriptor = klass.__dict__["FtDsFlags"]
            break
    assert isinstance(descriptor, property)



def test_afptext_fnc_is_not_abstract():
    assert not inspect.isabstract(afpText_FNC)


def test_afptext_fnc_constructor_exists():
    assert callable(afpText_FNC.__init__)


def test_afptext_fnc_constructor_args():
    sig = inspect.signature(afpText_FNC.__init__)
    params = list(sig.parameters.keys())
    assert "XUnitBase" in params, "Missing parameter 'XUnitBase'"
    assert "OPatDCnt" in params, "Missing parameter 'OPatDCnt'"
    assert "XftUnits" in params, "Missing parameter 'XftUnits'"
    assert "FNNMapCnt" in params, "Missing parameter 'FNNMapCnt'"
    assert "FNIRGLen" in params, "Missing parameter 'FNIRGLen'"
    assert "FNNDCnt" in params, "Missing parameter 'FNNDCnt'"
    assert "FNMRGLen" in params, "Missing parameter 'FNMRGLen'"
    assert "FntFlags" in params, "Missing parameter 'FntFlags'"
    assert "ResYUBase" in params, "Missing parameter 'ResYUBase'"
    assert "MaxBoxHt" in params, "Missing parameter 'MaxBoxHt'"
    assert "PatAlign" in params, "Missing parameter 'PatAlign'"
    assert "Retired" in params, "Missing parameter 'Retired'"
    assert "PatTech" in params, "Missing parameter 'PatTech'"
    assert "Reserved1" in params, "Missing parameter 'Reserved1'"
    assert "RPatDCnt" in params, "Missing parameter 'RPatDCnt'"
    assert "MaxBoxWd" in params, "Missing parameter 'MaxBoxWd'"
    assert "ResXUBase" in params, "Missing parameter 'ResXUBase'"
    assert "FNORGLen" in params, "Missing parameter 'FNORGLen'"
    assert "YftUnits" in params, "Missing parameter 'YftUnits'"
    assert "FNNRGLen" in params, "Missing parameter 'FNNRGLen'"
    assert "FNPRGLen" in params, "Missing parameter 'FNPRGLen'"
    assert "XfrUnits" in params, "Missing parameter 'XfrUnits'"
    assert "YfrUnits" in params, "Missing parameter 'YfrUnits'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "YUnitBase" in params, "Missing parameter 'YUnitBase'"

def test_afptext_fnc_has_XUnitBase():
    assert hasattr(afpText_FNC, "XUnitBase")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "XUnitBase" in klass.__dict__:
            descriptor = klass.__dict__["XUnitBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_OPatDCnt():
    assert hasattr(afpText_FNC, "OPatDCnt")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "OPatDCnt" in klass.__dict__:
            descriptor = klass.__dict__["OPatDCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_XftUnits():
    assert hasattr(afpText_FNC, "XftUnits")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "XftUnits" in klass.__dict__:
            descriptor = klass.__dict__["XftUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNNMapCnt():
    assert hasattr(afpText_FNC, "FNNMapCnt")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNNMapCnt" in klass.__dict__:
            descriptor = klass.__dict__["FNNMapCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNIRGLen():
    assert hasattr(afpText_FNC, "FNIRGLen")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNIRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNIRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNNDCnt():
    assert hasattr(afpText_FNC, "FNNDCnt")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNNDCnt" in klass.__dict__:
            descriptor = klass.__dict__["FNNDCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNMRGLen():
    assert hasattr(afpText_FNC, "FNMRGLen")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNMRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNMRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FntFlags():
    assert hasattr(afpText_FNC, "FntFlags")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FntFlags" in klass.__dict__:
            descriptor = klass.__dict__["FntFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_ResYUBase():
    assert hasattr(afpText_FNC, "ResYUBase")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "ResYUBase" in klass.__dict__:
            descriptor = klass.__dict__["ResYUBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_MaxBoxHt():
    assert hasattr(afpText_FNC, "MaxBoxHt")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "MaxBoxHt" in klass.__dict__:
            descriptor = klass.__dict__["MaxBoxHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_PatAlign():
    assert hasattr(afpText_FNC, "PatAlign")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "PatAlign" in klass.__dict__:
            descriptor = klass.__dict__["PatAlign"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_Retired():
    assert hasattr(afpText_FNC, "Retired")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "Retired" in klass.__dict__:
            descriptor = klass.__dict__["Retired"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_PatTech():
    assert hasattr(afpText_FNC, "PatTech")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "PatTech" in klass.__dict__:
            descriptor = klass.__dict__["PatTech"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_Reserved1():
    assert hasattr(afpText_FNC, "Reserved1")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "Reserved1" in klass.__dict__:
            descriptor = klass.__dict__["Reserved1"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_RPatDCnt():
    assert hasattr(afpText_FNC, "RPatDCnt")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "RPatDCnt" in klass.__dict__:
            descriptor = klass.__dict__["RPatDCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_MaxBoxWd():
    assert hasattr(afpText_FNC, "MaxBoxWd")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "MaxBoxWd" in klass.__dict__:
            descriptor = klass.__dict__["MaxBoxWd"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_ResXUBase():
    assert hasattr(afpText_FNC, "ResXUBase")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "ResXUBase" in klass.__dict__:
            descriptor = klass.__dict__["ResXUBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNORGLen():
    assert hasattr(afpText_FNC, "FNORGLen")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNORGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNORGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_YftUnits():
    assert hasattr(afpText_FNC, "YftUnits")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "YftUnits" in klass.__dict__:
            descriptor = klass.__dict__["YftUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNNRGLen():
    assert hasattr(afpText_FNC, "FNNRGLen")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNNRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNNRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_FNPRGLen():
    assert hasattr(afpText_FNC, "FNPRGLen")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "FNPRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNPRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_XfrUnits():
    assert hasattr(afpText_FNC, "XfrUnits")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "XfrUnits" in klass.__dict__:
            descriptor = klass.__dict__["XfrUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_YfrUnits():
    assert hasattr(afpText_FNC, "YfrUnits")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "YfrUnits" in klass.__dict__:
            descriptor = klass.__dict__["YfrUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_Reserved2():
    assert hasattr(afpText_FNC, "Reserved2")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext_fnc_has_YUnitBase():
    assert hasattr(afpText_FNC, "YUnitBase")
    descriptor = None
    for klass in afpText_FNC.__mro__:
        if "YUnitBase" in klass.__dict__:
            descriptor = klass.__dict__["YUnitBase"]
            break
    assert isinstance(descriptor, property)



def test_afptext_esg_is_not_abstract():
    assert not inspect.isabstract(afpText_ESG)


def test_afptext_esg_constructor_exists():
    assert callable(afpText_ESG.__init__)


def test_afptext_esg_constructor_args():
    sig = inspect.signature(afpText_ESG.__init__)
    params = list(sig.parameters.keys())
    assert "REGName" in params, "Missing parameter 'REGName'"

def test_afptext_esg_has_REGName():
    assert hasattr(afpText_ESG, "REGName")
    descriptor = None
    for klass in afpText_ESG.__mro__:
        if "REGName" in klass.__dict__:
            descriptor = klass.__dict__["REGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_ers_is_not_abstract():
    assert not inspect.isabstract(afpText_ERS)


def test_afptext_ers_constructor_exists():
    assert callable(afpText_ERS.__init__)


def test_afptext_ers_constructor_args():
    sig = inspect.signature(afpText_ERS.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_ers_has_RSName():
    assert hasattr(afpText_ERS, "RSName")
    descriptor = None
    for klass in afpText_ERS.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_erg_is_not_abstract():
    assert not inspect.isabstract(afpText_ERG)


def test_afptext_erg_constructor_exists():
    assert callable(afpText_ERG.__init__)


def test_afptext_erg_constructor_args():
    sig = inspect.signature(afpText_ERG.__init__)
    params = list(sig.parameters.keys())
    assert "RGrpName" in params, "Missing parameter 'RGrpName'"

def test_afptext_erg_has_RGrpName():
    assert hasattr(afpText_ERG, "RGrpName")
    descriptor = None
    for klass in afpText_ERG.__mro__:
        if "RGrpName" in klass.__dict__:
            descriptor = klass.__dict__["RGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eim_is_not_abstract():
    assert not inspect.isabstract(afpText_EIM)


def test_afptext_eim_constructor_exists():
    assert callable(afpText_EIM.__init__)


def test_afptext_eim_constructor_args():
    sig = inspect.signature(afpText_EIM.__init__)
    params = list(sig.parameters.keys())
    assert "IdoName" in params, "Missing parameter 'IdoName'"

def test_afptext_eim_has_IdoName():
    assert hasattr(afpText_EIM, "IdoName")
    descriptor = None
    for klass in afpText_EIM.__mro__:
        if "IdoName" in klass.__dict__:
            descriptor = klass.__dict__["IdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eps_is_not_abstract():
    assert not inspect.isabstract(afpText_EPS)


def test_afptext_eps_constructor_exists():
    assert callable(afpText_EPS.__init__)


def test_afptext_eps_constructor_args():
    sig = inspect.signature(afpText_EPS.__init__)
    params = list(sig.parameters.keys())
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext_eps_has_PsegName():
    assert hasattr(afpText_EPS, "PsegName")
    descriptor = None
    for klass in afpText_EPS.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_epm_is_not_abstract():
    assert not inspect.isabstract(afpText_EPM)


def test_afptext_epm_constructor_exists():
    assert callable(afpText_EPM.__init__)


def test_afptext_epm_constructor_args():
    sig = inspect.signature(afpText_EPM.__init__)
    params = list(sig.parameters.keys())
    assert "PMName" in params, "Missing parameter 'PMName'"

def test_afptext_epm_has_PMName():
    assert hasattr(afpText_EPM, "PMName")
    descriptor = None
    for klass in afpText_EPM.__mro__:
        if "PMName" in klass.__dict__:
            descriptor = klass.__dict__["PMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_epg_is_not_abstract():
    assert not inspect.isabstract(afpText_EPG)


def test_afptext_epg_constructor_exists():
    assert callable(afpText_EPG.__init__)


def test_afptext_epg_constructor_args():
    sig = inspect.signature(afpText_EPG.__init__)
    params = list(sig.parameters.keys())
    assert "PageName" in params, "Missing parameter 'PageName'"

def test_afptext_epg_has_PageName():
    assert hasattr(afpText_EPG, "PageName")
    descriptor = None
    for klass in afpText_EPG.__mro__:
        if "PageName" in klass.__dict__:
            descriptor = klass.__dict__["PageName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_epf_is_not_abstract():
    assert not inspect.isabstract(afpText_EPF)


def test_afptext_epf_constructor_exists():
    assert callable(afpText_EPF.__init__)


def test_afptext_epf_constructor_args():
    sig = inspect.signature(afpText_EPF.__init__)
    params = list(sig.parameters.keys())
    assert "PFName" in params, "Missing parameter 'PFName'"

def test_afptext_epf_has_PFName():
    assert hasattr(afpText_EPF, "PFName")
    descriptor = None
    for klass in afpText_EPF.__mro__:
        if "PFName" in klass.__dict__:
            descriptor = klass.__dict__["PFName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eog_is_not_abstract():
    assert not inspect.isabstract(afpText_EOG)


def test_afptext_eog_constructor_exists():
    assert callable(afpText_EOG.__init__)


def test_afptext_eog_constructor_args():
    sig = inspect.signature(afpText_EOG.__init__)
    params = list(sig.parameters.keys())
    assert "OEGName" in params, "Missing parameter 'OEGName'"

def test_afptext_eog_has_OEGName():
    assert hasattr(afpText_EOG, "OEGName")
    descriptor = None
    for klass in afpText_EOG.__mro__:
        if "OEGName" in klass.__dict__:
            descriptor = klass.__dict__["OEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eoc_is_not_abstract():
    assert not inspect.isabstract(afpText_EOC)


def test_afptext_eoc_constructor_exists():
    assert callable(afpText_EOC.__init__)


def test_afptext_eoc_constructor_args():
    sig = inspect.signature(afpText_EOC.__init__)
    params = list(sig.parameters.keys())
    assert "ObjCName" in params, "Missing parameter 'ObjCName'"

def test_afptext_eoc_has_ObjCName():
    assert hasattr(afpText_EOC, "ObjCName")
    descriptor = None
    for klass in afpText_EOC.__mro__:
        if "ObjCName" in klass.__dict__:
            descriptor = klass.__dict__["ObjCName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eng_is_not_abstract():
    assert not inspect.isabstract(afpText_ENG)


def test_afptext_eng_constructor_exists():
    assert callable(afpText_ENG.__init__)


def test_afptext_eng_constructor_args():
    sig = inspect.signature(afpText_ENG.__init__)
    params = list(sig.parameters.keys())
    assert "PGrpName" in params, "Missing parameter 'PGrpName'"

def test_afptext_eng_has_PGrpName():
    assert hasattr(afpText_ENG, "PGrpName")
    descriptor = None
    for klass in afpText_ENG.__mro__:
        if "PGrpName" in klass.__dict__:
            descriptor = klass.__dict__["PGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_emo_is_not_abstract():
    assert not inspect.isabstract(afpText_EMO)


def test_afptext_emo_constructor_exists():
    assert callable(afpText_EMO.__init__)


def test_afptext_emo_constructor_args():
    sig = inspect.signature(afpText_EMO.__init__)
    params = list(sig.parameters.keys())
    assert "OvlyName" in params, "Missing parameter 'OvlyName'"

def test_afptext_emo_has_OvlyName():
    assert hasattr(afpText_EMO, "OvlyName")
    descriptor = None
    for klass in afpText_EMO.__mro__:
        if "OvlyName" in klass.__dict__:
            descriptor = klass.__dict__["OvlyName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_emm_is_not_abstract():
    assert not inspect.isabstract(afpText_EMM)


def test_afptext_emm_constructor_exists():
    assert callable(afpText_EMM.__init__)


def test_afptext_emm_constructor_args():
    sig = inspect.signature(afpText_EMM.__init__)
    params = list(sig.parameters.keys())
    assert "MMName" in params, "Missing parameter 'MMName'"

def test_afptext_emm_has_MMName():
    assert hasattr(afpText_EMM, "MMName")
    descriptor = None
    for klass in afpText_EMM.__mro__:
        if "MMName" in klass.__dict__:
            descriptor = klass.__dict__["MMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_eii_is_not_abstract():
    assert not inspect.isabstract(afpText_EII)


def test_afptext_eii_constructor_exists():
    assert callable(afpText_EII.__init__)


def test_afptext_eii_constructor_args():
    sig = inspect.signature(afpText_EII.__init__)
    params = list(sig.parameters.keys())
    assert "ImoName" in params, "Missing parameter 'ImoName'"

def test_afptext_eii_has_ImoName():
    assert hasattr(afpText_EII, "ImoName")
    descriptor = None
    for klass in afpText_EII.__mro__:
        if "ImoName" in klass.__dict__:
            descriptor = klass.__dict__["ImoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_egr_is_not_abstract():
    assert not inspect.isabstract(afpText_EGR)


def test_afptext_egr_constructor_exists():
    assert callable(afpText_EGR.__init__)


def test_afptext_egr_constructor_args():
    sig = inspect.signature(afpText_EGR.__init__)
    params = list(sig.parameters.keys())
    assert "GdoName" in params, "Missing parameter 'GdoName'"

def test_afptext_egr_has_GdoName():
    assert hasattr(afpText_EGR, "GdoName")
    descriptor = None
    for klass in afpText_EGR.__mro__:
        if "GdoName" in klass.__dict__:
            descriptor = klass.__dict__["GdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_efn_is_not_abstract():
    assert not inspect.isabstract(afpText_EFN)


def test_afptext_efn_constructor_exists():
    assert callable(afpText_EFN.__init__)


def test_afptext_efn_constructor_args():
    sig = inspect.signature(afpText_EFN.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext_efn_has_RSName():
    assert hasattr(afpText_EFN, "RSName")
    descriptor = None
    for klass in afpText_EFN.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_efm_is_not_abstract():
    assert not inspect.isabstract(afpText_EFM)


def test_afptext_efm_constructor_exists():
    assert callable(afpText_EFM.__init__)


def test_afptext_efm_constructor_args():
    sig = inspect.signature(afpText_EFM.__init__)
    params = list(sig.parameters.keys())
    assert "FMName" in params, "Missing parameter 'FMName'"

def test_afptext_efm_has_FMName():
    assert hasattr(afpText_EFM, "FMName")
    descriptor = None
    for klass in afpText_EFM.__mro__:
        if "FMName" in klass.__dict__:
            descriptor = klass.__dict__["FMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_efg_is_not_abstract():
    assert not inspect.isabstract(afpText_EFG)


def test_afptext_efg_constructor_exists():
    assert callable(afpText_EFG.__init__)


def test_afptext_efg_constructor_args():
    sig = inspect.signature(afpText_EFG.__init__)
    params = list(sig.parameters.keys())
    assert "FEGName" in params, "Missing parameter 'FEGName'"

def test_afptext_efg_has_FEGName():
    assert hasattr(afpText_EFG, "FEGName")
    descriptor = None
    for klass in afpText_EFG.__mro__:
        if "FEGName" in klass.__dict__:
            descriptor = klass.__dict__["FEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_edx_is_not_abstract():
    assert not inspect.isabstract(afpText_EDX)


def test_afptext_edx_constructor_exists():
    assert callable(afpText_EDX.__init__)


def test_afptext_edx_constructor_args():
    sig = inspect.signature(afpText_EDX.__init__)
    params = list(sig.parameters.keys())
    assert "DMXName" in params, "Missing parameter 'DMXName'"

def test_afptext_edx_has_DMXName():
    assert hasattr(afpText_EDX, "DMXName")
    descriptor = None
    for klass in afpText_EDX.__mro__:
        if "DMXName" in klass.__dict__:
            descriptor = klass.__dict__["DMXName"]
            break
    assert isinstance(descriptor, property)



def test_afptext_edt_is_not_abstract():
    assert not inspect.isabstract(afpText_EDT)


def test_afptext_edt_constructor_exists():
    assert callable(afpText_EDT.__init__)


def test_afptext_edt_constructor_args():
    sig = inspect.signature(afpText_EDT.__init__)
    params = list(sig.parameters.keys())
    assert "DocName" in params, "Missing parameter 'DocName'"

def test_afptext_edt_has_DocName():
    assert hasattr(afpText_EDT, "DocName")
    descriptor = None
    for klass in afpText_EDT.__mro__:
        if "DocName" in klass.__dict__:
            descriptor = klass.__dict__["DocName"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
triplet_strategy = st.builds(
    triplet,
)
afpText_IDESize_strategy = st.builds(
    afpText_IDESize,
    IDESZ=
        safe_text
)
afpText_FontHorizontalScaleFactor_strategy = st.builds(
    afpText_FontHorizontalScaleFactor,
    Hscale=
        safe_text
)
afpText_ObjectClassification_strategy = st.builds(
    afpText_ObjectClassification,
    ObjClass=
        safe_text,
    CompName=
        safe_text,
    StrucFlgs=
        safe_text,
    ObjLev=
        safe_text,
    RegObjId=
        safe_text,
    ObjTpName=
        safe_text
)
afpText_FinishingOperation_strategy = st.builds(
    afpText_FinishingOperation,
    AxOffst=
        safe_text,
    FOpCnt=
        safe_text,
    FOpType=
        safe_text,
    RefEdge=
        safe_text,
    OpPos=
        safe_text
)
afpText_BandImageData_strategy = st.builds(
    afpText_BandImageData,
    DATA=
        safe_text,
    BANDNUM=
        safe_text,
    RESERVED=
        safe_text
)
afpText_DeviceAppearance_strategy = st.builds(
    afpText_DeviceAppearance,
    DevApp=
        safe_text,
    Reserved=
        safe_text
)
afpText_ColorSpecification_strategy = st.builds(
    afpText_ColorSpecification,
    ColSpce=
        safe_text,
    ColSize2=
        safe_text,
    ColSize4=
        safe_text,
    ColSize1=
        safe_text,
    ColSize3=
        safe_text,
    Color=
        safe_text
)
afpText_UniversalDateAndTimeStamp_strategy = st.builds(
    afpText_UniversalDateAndTimeStamp,
    Second=
        safe_text,
    Hour=
        safe_text,
    Reserved=
        safe_text,
    YearAD=
        safe_text,
    Day=
        safe_text,
    UTCDiffM=
        safe_text,
    TimeZone=
        safe_text,
    UTCDiffH=
        safe_text,
    Minute=
        safe_text,
    Month=
        safe_text
)
afpText_ExtendedResourceLocalIdentifier_strategy = st.builds(
    afpText_ExtendedResourceLocalIdentifier,
    ResLID=
        safe_text,
    ResType=
        safe_text
)
afpText_ResourceSectionNumber_strategy = st.builds(
    afpText_ResourceSectionNumber,
    ResSNum=
        safe_text
)
afpText_EndImage_strategy = st.builds(
    afpText_EndImage,
)
afpText_GSCS_strategy = st.builds(
    afpText_GSCS,
    LCID=
        safe_text
)
afpText_GSCP_strategy = st.builds(
    afpText_GSCP,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText_GCBEZ_strategy = st.builds(
    afpText_GCBEZ,
)
afpText_LineDataObjectPositionMigration_strategy = st.builds(
    afpText_LineDataObjectPositionMigration,
    TempOrient=
        safe_text
)
afpText_FontDescriptorSpecification_strategy = st.builds(
    afpText_FontDescriptorSpecification,
    FtHeight=
        safe_text,
    FtUsFlags=
        safe_text,
    FtDsFlags=
        safe_text,
    FtWtClass=
        safe_text,
    FtWidth=
        safe_text,
    FtWdClass=
        safe_text
)
afpText_ObjectOriginIdentifier_strategy = st.builds(
    afpText_ObjectOriginIdentifier,
    SysID=
        safe_text,
    System=
        safe_text,
    MedID=
        safe_text,
    DSID=
        safe_text
)
afpText_GSLT_strategy = st.builds(
    afpText_GSLT,
    LINETYPE=
        safe_text
)
afpText_MediumOrientation_strategy = st.builds(
    afpText_MediumOrientation,
    MedOrient=
        safe_text
)
afpText_TileSize_strategy = st.builds(
    afpText_TileSize,
    RELRES=
        safe_text,
    TVSIZE=
        safe_text,
    THSIZE=
        safe_text
)
afpText_EncodingSchemeID_strategy = st.builds(
    afpText_EncodingSchemeID,
    ESidCP=
        safe_text,
    ESidUD=
        safe_text
)
afpText_FontFidelity_strategy = st.builds(
    afpText_FontFidelity,
    StpFntEx=
        safe_text
)
afpText_BeginImage_strategy = st.builds(
    afpText_BeginImage,
    OBJTYPE=
        safe_text
)
afpText_GCMRK_strategy = st.builds(
    afpText_GCMRK,
)
afpText_GSCR_strategy = st.builds(
    afpText_GSCR,
    PREC=
        safe_text
)
afpText_ImageSize_strategy = st.builds(
    afpText_ImageSize,
    VSIZE=
        safe_text,
    HRESOL=
        safe_text,
    VRESOL=
        safe_text,
    HSIZE=
        safe_text,
    UNITBASE=
        safe_text
)
afpText_PagePositionInformation_strategy = st.builds(
    afpText_PagePositionInformation,
    PGPRG=
        safe_text
)
afpText_GFLT_strategy = st.builds(
    afpText_GFLT,
)
afpText_ImageData_strategy = st.builds(
    afpText_ImageData,
    DATA=
        safe_text
)
afpText_AttributeValue_strategy = st.builds(
    afpText_AttributeValue,
    AttVal=
        safe_text,
    Reserved0=
        safe_text
)
afpText_EndTransparencyMask_strategy = st.builds(
    afpText_EndTransparencyMask,
)
afpText_GSPCOL_strategy = st.builds(
    afpText_GSPCOL,
    COLSIZE2=
        safe_text,
    COLSIZE3=
        safe_text,
    COLVALUE=
        safe_text,
    RES2=
        safe_text,
    COLSIZE1=
        safe_text,
    COLSPCE=
        safe_text,
    RES1=
        safe_text,
    COLSIZE4=
        safe_text
)
afpText_TBM_strategy = st.builds(
    afpText_TBM,
    PRECSION=
        safe_text,
    DIRCTION=
        safe_text,
    INCRMENT=
        safe_text
)
afpText_GSGCH_strategy = st.builds(
    afpText_GSGCH,
)
afpText_ExternalAlgorithm_strategy = st.builds(
    afpText_ExternalAlgorithm,
    ALGTYPE=
        safe_text
)
afpText_ObjectOffset_strategy = st.builds(
    afpText_ObjectOffset,
    ObjOset=
        safe_text,
    ObjTpe=
        safe_text,
    ObjOstHi=
        safe_text
)
afpText_GCPARC_strategy = st.builds(
    afpText_GCPARC,
    MH=
        safe_text,
    YCENT=
        safe_text,
    SWEEP=
        safe_text,
    MFR=
        safe_text,
    START=
        safe_text,
    XCENT=
        safe_text
)
afpText_MappingOption_strategy = st.builds(
    afpText_MappingOption,
    MapValue=
        safe_text
)
afpText_ObjectCount_strategy = st.builds(
    afpText_ObjectCount,
    SobjNmHi=
        safe_text,
    SObjNum=
        safe_text,
    SubObj=
        safe_text
)
afpText_TonerSaver_strategy = st.builds(
    afpText_TonerSaver,
    TSvCtrl=
        safe_text
)
afpText_GSPT_strategy = st.builds(
    afpText_GSPT,
    PATT=
        safe_text
)
afpText_GSCD_strategy = st.builds(
    afpText_GSCD,
    DIRECTION=
        safe_text
)
afpText_BandImage_strategy = st.builds(
    afpText_BandImage,
    BCOUNT=
        safe_text
)
afpText_RenderingIntent_strategy = st.builds(
    afpText_RenderingIntent,
    IOCARI=
        safe_text,
    Reserved=
        safe_text,
    Reserved2=
        safe_text,
    OCRI=
        safe_text,
    GOCARI=
        safe_text,
    PTOCRI=
        safe_text
)
afpText_GSBMX_strategy = st.builds(
    afpText_GSBMX,
    MODE=
        safe_text
)
afpText_ImageEncoding_strategy = st.builds(
    afpText_ImageEncoding,
    RECID=
        safe_text,
    COMPRID=
        safe_text,
    BITORDR=
        safe_text
)
afpText_ImageResolution_strategy = st.builds(
    afpText_ImageResolution,
    YBase=
        safe_text,
    XResol=
        safe_text,
    YResol=
        safe_text,
    XBase=
        safe_text
)
afpText_CharacterRotation_strategy = st.builds(
    afpText_CharacterRotation,
    CharRot=
        safe_text
)
afpText_GCFLT_strategy = st.builds(
    afpText_GCFLT,
)
afpText_ObjectStructuredFieldExtent_strategy = st.builds(
    afpText_ObjectStructuredFieldExtent,
    SFExt=
        safe_text,
    SFExtHi=
        safe_text
)
afpText_GSMS_strategy = st.builds(
    afpText_GSMS,
    LCID=
        safe_text
)
afpText_ObjectContainerPresentationSpaceSize_strategy = st.builds(
    afpText_ObjectContainerPresentationSpaceSize,
    PDFSize=
        safe_text
)
afpText_ImageSubsampling_strategy = st.builds(
    afpText_ImageSubsampling,
)
afpText_GPARC_strategy = st.builds(
    afpText_GPARC,
    YPOS=
        safe_text,
    XCENT=
        safe_text,
    SWEEP=
        safe_text,
    MFR=
        safe_text,
    YCENT=
        safe_text,
    MH=
        safe_text,
    START=
        safe_text,
    XPOS=
        safe_text
)
afpText_CGCSGID_strategy = st.builds(
    afpText_CGCSGID,
    GCSGID=
        safe_text,
    CPGID=
        safe_text
)
afpText_ColorManagementResourceDescriptor_strategy = st.builds(
    afpText_ColorManagementResourceDescriptor,
    CMRScpe=
        safe_text,
    ProcMode=
        safe_text
)
afpText_MODCAInterchangeSet_strategy = st.builds(
    afpText_MODCAInterchangeSet,
    IStype=
        safe_text,
    ISid=
        safe_text
)
afpText_EndSegment_strategy = st.builds(
    afpText_EndSegment,
)
afpText_GFARC_strategy = st.builds(
    afpText_GFARC,
    XPOS=
        safe_text,
    YPOS=
        safe_text,
    MFR=
        safe_text,
    MH=
        safe_text
)
afpText_TextFidelity_strategy = st.builds(
    afpText_TextFidelity,
    RepTxtEx=
        safe_text,
    StpTxtEx=
        safe_text
)
afpText_IDEStructure_strategy = st.builds(
    afpText_IDEStructure,
    FORMAT=
        safe_text,
    SIZE2=
        safe_text,
    FLAGS=
        safe_text,
    SIZE4=
        safe_text,
    SIZE1=
        safe_text,
    SIZE3=
        safe_text
)
afpText_FNNRG2_strategy = st.builds(
    afpText_FNNRG2,
    TSIDLen=
        safe_text,
    TSID=
        safe_text
)
afpText_BeginTransparencyMask_strategy = st.builds(
    afpText_BeginTransparencyMask,
)
afpText_GSCH_strategy = st.builds(
    afpText_GSCH,
    HX=
        safe_text,
    HY=
        safe_text
)
afpText_GSECOL_strategy = st.builds(
    afpText_GSECOL,
    COLOR=
        safe_text
)
afpText_ResourceUsageAttribute_strategy = st.builds(
    afpText_ResourceUsageAttribute,
    Frequency=
        safe_text
)
afpText_IncludeTile_strategy = st.builds(
    afpText_IncludeTile,
    TIRID=
        safe_text
)
afpText_ObjectStructuredFieldOffset_strategy = st.builds(
    afpText_ObjectStructuredFieldOffset,
    SFOffHi=
        safe_text,
    SFOff=
        safe_text
)
afpText_ResourceObjectInclude_strategy = st.builds(
    afpText_ResourceObjectInclude,
    ObjType=
        safe_text,
    ObOrent=
        safe_text,
    XobjOset=
        safe_text,
    YobjOset=
        safe_text,
    ObjName=
        safe_text
)
afpText_ResourceObjectType_strategy = st.builds(
    afpText_ResourceObjectType,
    ConData=
        safe_text,
    ObjType=
        safe_text
)
afpText_LocalDateAndTimeStamp_strategy = st.builds(
    afpText_LocalDateAndTimeStamp,
    TenYear=
        safe_text,
    Day=
        safe_text,
    StampType=
        safe_text,
    HundSec=
        safe_text,
    Hour=
        safe_text,
    Minute=
        safe_text,
    THunYear=
        safe_text,
    Second=
        safe_text
)
afpText_EndSegmentCommand_strategy = st.builds(
    afpText_EndSegmentCommand,
)
afpText_GCCHST_strategy = st.builds(
    afpText_GCCHST,
    CP=
        safe_text
)
afpText_ResourceLocalIdentifier_strategy = st.builds(
    afpText_ResourceLocalIdentifier,
    ResType=
        safe_text,
    ResLID=
        safe_text
)
afpText_GSAP_strategy = st.builds(
    afpText_GSAP,
    P=
        safe_text,
    R=
        safe_text,
    Q=
        safe_text,
    S=
        safe_text
)
afpText_GBIMG_strategy = st.builds(
    afpText_GBIMG,
    YPOS=
        safe_text,
    XPOS=
        safe_text,
    RES=
        safe_text,
    FORMAT=
        safe_text,
    WIDTH=
        safe_text,
    HEIGHT=
        safe_text
)
afpText_GCCBEZ_strategy = st.builds(
    afpText_GCCBEZ,
)
afpText_GSMT_strategy = st.builds(
    afpText_GSMT,
    MCPT=
        safe_text
)
afpText_GCFARC_strategy = st.builds(
    afpText_GCFARC,
    MH=
        safe_text,
    MFR=
        safe_text
)
afpText_GMRK_strategy = st.builds(
    afpText_GMRK,
)
afpText_BeginSegmentCommand_strategy = st.builds(
    afpText_BeginSegmentCommand,
    NAME=
        safe_text,
    FLAG1=
        safe_text,
    LENGTH=
        safe_text,
    SEGL=
        safe_text,
    FLAG2=
        safe_text,
    PSNAME=
        safe_text
)
afpText_FullyQualifiedName_strategy = st.builds(
    afpText_FullyQualifiedName,
    FQName=
        safe_text,
    FQNFormat=
        safe_text,
    FQNType=
        safe_text
)
afpText_SamplingRatios_strategy = st.builds(
    afpText_SamplingRatios,
)
afpText_MetricAdjustment_strategy = st.builds(
    afpText_MetricAdjustment,
    YUPUB=
        safe_text,
    HBaselineIncrement=
        safe_text,
    XUPUB=
        safe_text,
    HUniformIncrement=
        safe_text,
    UnitBase=
        safe_text,
    VBaselineIncrement=
        safe_text,
    VUniformIncrement=
        safe_text
)
afpText_DataObjectFontDescriptor_strategy = st.builds(
    afpText_DataObjectFontDescriptor,
    EncEnv=
        safe_text,
    VFS=
        safe_text,
    DOFtFlgs=
        safe_text,
    FontTech=
        safe_text,
    CharRot=
        safe_text,
    HFS=
        safe_text,
    EncID=
        safe_text,
    Reserved=
        safe_text
)
afpText_MediumMapPageNumber_strategy = st.builds(
    afpText_MediumMapPageNumber,
    PageNum=
        safe_text
)
afpText_GEIMG_strategy = st.builds(
    afpText_GEIMG,
    DATA=
        safe_text
)
afpText_GSFLW_strategy = st.builds(
    afpText_GSFLW,
    MFR=
        safe_text,
    MH=
        safe_text
)
afpText_GNOP1_strategy = st.builds(
    afpText_GNOP1,
)
afpText_GCLINE_strategy = st.builds(
    afpText_GCLINE,
)
afpText_LocaleSelector_strategy = st.builds(
    afpText_LocaleSelector,
    LocFlgs=
        safe_text,
    LangCode=
        safe_text,
    ScrptCde=
        safe_text,
    Reserved=
        safe_text,
    VarCde=
        safe_text,
    RegCde=
        safe_text
)
afpText_MediaEjectControl_strategy = st.builds(
    afpText_MediaEjectControl,
    EjCtrl=
        safe_text,
    Reserved=
        safe_text
)
afpText_GEAR_strategy = st.builds(
    afpText_GEAR,
    DATA=
        safe_text
)
afpText_MeasurementUnits_strategy = st.builds(
    afpText_MeasurementUnits,
    YoaBase=
        safe_text,
    XoaUnits=
        safe_text,
    YoaUnits=
        safe_text,
    XoaBase=
        safe_text
)
afpText_DrawingOrderSubset_strategy = st.builds(
    afpText_DrawingOrderSubset,
)
afpText_ObjectByteOffset_strategy = st.builds(
    afpText_ObjectByteOffset,
    DirByOff=
        safe_text,
    DirByHi=
        safe_text
)
afpText_GSCA_strategy = st.builds(
    afpText_GSCA,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText_GCBOX_strategy = st.builds(
    afpText_GCBOX,
    XPOS1=
        safe_text,
    YPOS1=
        safe_text,
    RES=
        safe_text,
    VAXIS=
        safe_text,
    HAXIS=
        safe_text
)
afpText_ExtensionFont_strategy = st.builds(
    afpText_ExtensionFont,
    GCSGID=
        safe_text
)
afpText_PresentationSpaceResetMixing_strategy = st.builds(
    afpText_PresentationSpaceResetMixing,
    BgMxFlag=
        safe_text
)
afpText_TilePosition_strategy = st.builds(
    afpText_TilePosition,
    XOFFSET=
        safe_text,
    YOFFSET=
        safe_text
)
afpText_GLINE_strategy = st.builds(
    afpText_GLINE,
)
afpText_GSMC_strategy = st.builds(
    afpText_GSMC,
    CELLWI=
        safe_text,
    CELLHI=
        safe_text
)
afpText_PageOverlayConditionalProcessing_strategy = st.builds(
    afpText_PageOverlayConditionalProcessing,
    PgOvType=
        safe_text,
    Level=
        safe_text
)
afpText_CMRFidelity_strategy = st.builds(
    afpText_CMRFidelity,
    RepCMREx=
        safe_text,
    StpCMREx=
        safe_text
)
afpText_GBAR_strategy = st.builds(
    afpText_GBAR,
    FLAGS=
        safe_text
)
afpText_GIMD_strategy = st.builds(
    afpText_GIMD,
    DATA=
        safe_text
)
afpText_TileTOC_strategy = st.builds(
    afpText_TileTOC,
    Reserved=
        safe_text
)
afpText_CRCResourceManagement_strategy = st.builds(
    afpText_CRCResourceManagement,
    ResClassFlg=
        safe_text,
    RMValue=
        safe_text,
    FmtQual=
        safe_text
)
afpText_GSCC_strategy = st.builds(
    afpText_GSCC,
    CELLHFR=
        safe_text,
    CELLHI=
        safe_text,
    CELLWI=
        safe_text,
    CELLWFR=
        safe_text
)
afpText_ObjectByteExtent_strategy = st.builds(
    afpText_ObjectByteExtent,
    ByteExt=
        safe_text,
    ByteExtHi=
        safe_text
)
afpText_ObjectFunctionSetSpecification_strategy = st.builds(
    afpText_ObjectFunctionSetSpecification,
    ObjType=
        safe_text,
    DCAFnSet=
        safe_text,
    OCAFnSet=
        safe_text,
    ArchVrsn=
        safe_text
)
afpText_GCBIMG_strategy = st.builds(
    afpText_GCBIMG,
    FORMAT=
        safe_text,
    HEIGHT=
        safe_text,
    RES=
        safe_text,
    WIDTH=
        safe_text
)
afpText_GEPROL_strategy = st.builds(
    afpText_GEPROL,
    RES=
        safe_text
)
afpText_MediaFidelity_strategy = st.builds(
    afpText_MediaFidelity,
    StpMedEx=
        safe_text,
    Reserved=
        safe_text
)
afpText_FinishingFidelity_strategy = st.builds(
    afpText_FinishingFidelity,
    StpFinEx=
        safe_text,
    RepFinEx=
        safe_text
)
afpText_ImageLUTID_strategy = st.builds(
    afpText_ImageLUTID,
    LUTID=
        safe_text
)
afpText_GSCOL_strategy = st.builds(
    afpText_GSCOL,
    COL=
        safe_text
)
afpText_AMI_strategy = st.builds(
    afpText_AMI,
    DSPLCMNT=
        safe_text
)
afpText_Comment_strategy = st.builds(
    afpText_Comment,
    Comment=
        safe_text
)
afpText_WindowSpecification_strategy = st.builds(
    afpText_WindowSpecification,
    RES3=
        safe_text,
    CFORMAT=
        safe_text,
    IMGXYRES=
        safe_text,
    XRWIND=
        safe_text,
    FLAGS=
        safe_text,
    YRESOL=
        safe_text,
    UBASE=
        safe_text,
    XLWIND=
        safe_text,
    XRESOL=
        safe_text,
    YTWIND=
        safe_text,
    YBWIND=
        safe_text
)
afpText_FontResolution_strategy = st.builds(
    afpText_FontResolution,
    RPuBase=
        safe_text,
    RPUnits=
        safe_text,
    MetTech=
        safe_text
)
afpText_TextOrientation_strategy = st.builds(
    afpText_TextOrientation,
    BAxis=
        safe_text,
    IAxis=
        safe_text
)
afpText_UP3iFinishingOperation_strategy = st.builds(
    afpText_UP3iFinishingOperation,
    UP3iDat=
        safe_text,
    Seqnum=
        safe_text
)
afpText_BeginSegment_strategy = st.builds(
    afpText_BeginSegment,
    SEGNAME=
        safe_text
)
afpText_EndTile_strategy = st.builds(
    afpText_EndTile,
)
afpText_PresentationSpaceMixingRules_strategy = st.builds(
    afpText_PresentationSpaceMixingRules,
)
afpText_AttributeQualifier_strategy = st.builds(
    afpText_AttributeQualifier,
    SeqNum=
        safe_text,
    LevNum=
        safe_text
)
afpText_TRN_strategy = st.builds(
    afpText_TRN,
    TRNDATA=
        safe_text
)
afpText_GSLE_strategy = st.builds(
    afpText_GSLE,
    LINEEND=
        safe_text
)
afpText_BSU_strategy = st.builds(
    afpText_BSU,
    LID=
        safe_text
)
afpText_FontCodedGraphicCharacterSetGlobalIdentifier_strategy = st.builds(
    afpText_FontCodedGraphicCharacterSetGlobalIdentifier,
    CPGID=
        safe_text,
    GCSGID=
        safe_text
)
afpText_GCOMT_strategy = st.builds(
    afpText_GCOMT,
    DATA=
        safe_text
)
afpText_BeginTile_strategy = st.builds(
    afpText_BeginTile,
)
afpText_USC_strategy = st.builds(
    afpText_USC,
    BYPSIDEN=
        safe_text
)
afpText_PresentationControl_strategy = st.builds(
    afpText_PresentationControl,
    PRSFlg=
        safe_text
)
afpText_DescriptorPosition_strategy = st.builds(
    afpText_DescriptorPosition,
    DesPosID=
        safe_text
)
afpText_TileSetColor_strategy = st.builds(
    afpText_TileSetColor,
    SIZE3=
        safe_text,
    SIZE2=
        safe_text,
    CVAL3=
        safe_text,
    CVAL1=
        safe_text,
    SIZE1=
        safe_text,
    CSPACE=
        safe_text,
    SIZE4=
        safe_text,
    RESERVED=
        safe_text,
    CVAL2=
        safe_text,
    CVAL4=
        safe_text
)
afpText_GSLJ_strategy = st.builds(
    afpText_GSLJ,
    LINEJOIN=
        safe_text
)
afpText_IOCAFunctionSetIdentification_strategy = st.builds(
    afpText_IOCAFunctionSetIdentification,
    CATEGORY=
        safe_text,
    FCNSET=
        safe_text
)
afpText_GBOX_strategy = st.builds(
    afpText_GBOX,
    XPOS1=
        safe_text,
    XPOS0=
        safe_text,
    HAXIS=
        safe_text,
    YPOS0=
        safe_text,
    YPOS1=
        safe_text,
    VAXIS=
        safe_text,
    RES=
        safe_text
)
afpText_ColorFidelity_strategy = st.builds(
    afpText_ColorFidelity,
    RepCoEx=
        safe_text,
    StpCoEx=
        safe_text,
    ColSub=
        safe_text
)
afpText_GSLW_strategy = st.builds(
    afpText_GSLW,
    MH=
        safe_text
)
afpText_GSMX_strategy = st.builds(
    afpText_GSMX,
    MODE=
        safe_text
)
afpText_GCHST_strategy = st.builds(
    afpText_GCHST,
    YPOS=
        safe_text,
    CP=
        safe_text,
    XPOS=
        safe_text
)
afpText_GCRLINE_strategy = st.builds(
    afpText_GCRLINE,
)
afpText_GRLINE_strategy = st.builds(
    afpText_GRLINE,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText_SetBiLevelImageColor_strategy = st.builds(
    afpText_SetBiLevelImageColor,
    NAMECOLR=
        safe_text,
    AREA=
        safe_text,
    Reserved=
        safe_text
)
afpText_ObjectAreaSize_strategy = st.builds(
    afpText_ObjectAreaSize,
    XoaSize=
        safe_text,
    SizeType=
        safe_text,
    YoaSize=
        safe_text
)
afpText_BLN_strategy = st.builds(
    afpText_BLN,
)
afpText_GSMP_strategy = st.builds(
    afpText_GSMP,
    PREC=
        safe_text
)
afpText_GSPS_strategy = st.builds(
    afpText_GSPS,
    LCID=
        safe_text
)
afpText_AMB_strategy = st.builds(
    afpText_AMB,
    DSPLCMNT=
        safe_text
)
afpText_SVI_strategy = st.builds(
    afpText_SVI,
    INCRMENT=
        safe_text
)
afpText_STO_strategy = st.builds(
    afpText_STO,
    IORNTION=
        safe_text,
    BORNTION=
        safe_text
)
afpText_STC_strategy = st.builds(
    afpText_STC,
    PRECSION=
        safe_text,
    FRGCOLOR=
        safe_text
)
afpText_SIM_strategy = st.builds(
    afpText_SIM,
    DSPLCMNT=
        safe_text
)
afpText_SIA_strategy = st.builds(
    afpText_SIA,
    DIRCTION=
        safe_text,
    ADJSTMNT=
        safe_text
)
afpText_SEC_strategy = st.builds(
    afpText_SEC,
    COLSIZE2=
        safe_text,
    COLSIZE1=
        safe_text,
    COLVALUE=
        safe_text,
    COLSIZE4=
        safe_text,
    COLSPCE=
        safe_text,
    COLSIZE3=
        safe_text,
    RESERVED=
        safe_text
)
afpText_SCFL_strategy = st.builds(
    afpText_SCFL,
    LID=
        safe_text
)
afpText_SBI_strategy = st.builds(
    afpText_SBI,
    INCRMENT=
        safe_text
)
afpText_RPS_strategy = st.builds(
    afpText_RPS,
    RPTDATA=
        safe_text,
    RLENGTH=
        safe_text
)
afpText_RMI_strategy = st.builds(
    afpText_RMI,
    INCRMENT=
        safe_text
)
afpText_RMB_strategy = st.builds(
    afpText_RMB,
    INCRMENT=
        safe_text
)
afpText_OVS_strategy = st.builds(
    afpText_OVS,
    BYPSIDEN=
        safe_text,
    OVERCHAR=
        safe_text
)
afpText_NOPCS_strategy = st.builds(
    afpText_NOPCS,
    IGNDATA=
        safe_text
)
afpText_ESU_strategy = st.builds(
    afpText_ESU,
    LID=
        safe_text
)
afpText_DIR_strategy = st.builds(
    afpText_DIR,
    RWIDTH=
        safe_text,
    RWIDTHFRACTION=
        safe_text,
    RLENGTH=
        safe_text
)
afpText_DBR_strategy = st.builds(
    afpText_DBR,
    RWIDTHFRACTION=
        safe_text,
    RLENGTH=
        safe_text,
    RWIDTH=
        safe_text
)
afpText_GCRLINERG_strategy = st.builds(
    afpText_GCRLINERG,
    YOFFS=
        safe_text,
    XOSSF=
        safe_text
)
afpText_GRLINERG_strategy = st.builds(
    afpText_GRLINERG,
    YOFFS=
        safe_text,
    XOSSF=
        safe_text
)
afpText_GCMRKRG_strategy = st.builds(
    afpText_GCMRKRG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText_GMRKRG_strategy = st.builds(
    afpText_GMRKRG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText_GCLINERG_strategy = st.builds(
    afpText_GCLINERG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText_GLINERG_strategy = st.builds(
    afpText_GLINERG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText_GCFLTRG_strategy = st.builds(
    afpText_GCFLTRG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText_GFLTRG_strategy = st.builds(
    afpText_GFLTRG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText_GCCBEZRG_strategy = st.builds(
    afpText_GCCBEZRG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText_GCBEZRG_strategy = st.builds(
    afpText_GCBEZRG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText_FNNRG_strategy = st.builds(
    afpText_FNNRG,
    TSOffset=
        safe_text,
    GCGID=
        safe_text
)
afpText_ExternalAlgorithmRG_strategy = st.builds(
    afpText_ExternalAlgorithmRG,
    DIRCTN=
        safe_text,
    PADBDRY=
        safe_text,
    PADALMT=
        safe_text
)
afpText_SamplingRatiosRG_strategy = st.builds(
    afpText_SamplingRatiosRG,
    HSAMPLE=
        safe_text,
    VSAMPLE=
        safe_text
)
afpText_TileTOCRG_strategy = st.builds(
    afpText_TileTOCRG,
    RELRES=
        safe_text,
    YOFFSET=
        safe_text,
    XOFFSET=
        safe_text,
    TVSIZE=
        safe_text,
    COMPR=
        safe_text,
    DATAPOS=
        safe_text,
    THSIZE=
        safe_text
)
afpText_BandImageRG_strategy = st.builds(
    afpText_BandImageRG,
    BITCNT=
        safe_text
)
afpText_PPORG_strategy = st.builds(
    afpText_PPORG,
    XocaOset=
        safe_text,
    YocaOset=
        safe_text,
    ObjType=
        safe_text,
    RGLength=
        safe_text,
    ProcFlgs=
        safe_text
)
afpText_PGPRG_strategy = st.builds(
    afpText_PGPRG,
    PGorient=
        safe_text,
    PMCid=
        safe_text,
    SHside=
        safe_text,
    PgFlgs=
        safe_text,
    RGLength=
        safe_text,
    XmOset=
        safe_text,
    YmOset=
        safe_text
)
afpText_MSURG_strategy = st.builds(
    afpText_MSURG,
    SUPid=
        safe_text,
    Reserved=
        safe_text,
    SUPname=
        safe_text
)
afpText_MPSRG_strategy = st.builds(
    afpText_MPSRG,
    Reserved=
        safe_text,
    PsegName=
        safe_text
)
afpText_MPORG_strategy = st.builds(
    afpText_MPORG,
    RGLength=
        safe_text
)
afpText_MPGRG_strategy = st.builds(
    afpText_MPGRG,
    RGLength=
        safe_text
)
afpText_MMTRG_strategy = st.builds(
    afpText_MMTRG,
    RGLength=
        safe_text
)
afpText_MMORG_strategy = st.builds(
    afpText_MMORG,
    OVLid=
        safe_text,
    OVLname=
        safe_text,
    Flags=
        safe_text
)
afpText_MMDRG_strategy = st.builds(
    afpText_MMDRG,
    RGLength=
        safe_text
)
afpText_MMCRG_strategy = st.builds(
    afpText_MMCRG,
    key=
        safe_text,
    value=
        safe_text
)
afpText_MIORG_strategy = st.builds(
    afpText_MIORG,
    RGLength=
        safe_text
)
afpText_MGORG_strategy = st.builds(
    afpText_MGORG,
    RGLength=
        safe_text
)
afpText_MCARG_strategy = st.builds(
    afpText_MCARG,
    RGLength=
        safe_text
)
afpText_MDRRG_strategy = st.builds(
    afpText_MDRRG,
    RGLength=
        safe_text
)
afpText_MCF1RG_strategy = st.builds(
    afpText_MCF1RG,
    FCSName=
        safe_text,
    CPName=
        safe_text,
    CFLid=
        safe_text,
    CFName=
        safe_text,
    CharRot=
        safe_text,
    Sectid=
        safe_text
)
afpText_MCFRG_strategy = st.builds(
    afpText_MCFRG,
    RGLength=
        safe_text
)
afpText_MCDRG_strategy = st.builds(
    afpText_MCDRG,
    RGLength=
        safe_text
)
afpText_MCCRG_strategy = st.builds(
    afpText_MCCRG,
    MMCid=
        safe_text,
    Stopnum=
        safe_text,
    Startnum=
        safe_text
)
afpText_MBCRG_strategy = st.builds(
    afpText_MBCRG,
    RGLength=
        safe_text
)
afpText_LLERG_strategy = st.builds(
    afpText_LLERG,
    RGFunct=
        safe_text,
    RGLength=
        safe_text
)
afpText_CPIRG_strategy = st.builds(
    afpText_CPIRG,
    GCGID=
        safe_text,
    CodePoint=
        safe_text,
    Count=
        safe_text,
    PrtFlags=
        safe_text
)
afpText_CFIRG_strategy = st.builds(
    afpText_CFIRG,
    Reserved=
        safe_text,
    CPName=
        safe_text,
    SHScale=
        safe_text,
    FCSName=
        safe_text,
    Section=
        safe_text,
    SVSize=
        safe_text
)
afpText_triplet_strategy = st.builds(
    afpText_triplet,
)
structuredField_strategy = st.builds(
    structuredField,
)
afpText_PGP1_strategy = st.builds(
    afpText_PGP1,
    YOset=
        safe_text,
    XOset=
        safe_text
)
afpText_BPM_strategy = st.builds(
    afpText_BPM,
    PMName=
        safe_text
)
afpText_MPO_strategy = st.builds(
    afpText_MPO,
)
afpText_BPF_strategy = st.builds(
    afpText_BPF,
    PFName=
        safe_text
)
afpText_BRG_strategy = st.builds(
    afpText_BRG,
    RGrpName=
        safe_text
)
afpText_EAG_strategy = st.builds(
    afpText_EAG,
    AEGName=
        safe_text
)
afpText_CAT_strategy = st.builds(
    afpText_CAT,
    CATData=
        safe_text
)
afpText_MCD_strategy = st.builds(
    afpText_MCD,
)
afpText_BDT_strategy = st.builds(
    afpText_BDT,
    DocName=
        safe_text,
    Reserved=
        safe_text
)
afpText_BMM_strategy = st.builds(
    afpText_BMM,
    MMName=
        safe_text
)
afpText_ECF_strategy = st.builds(
    afpText_ECF,
    RSName=
        safe_text
)
afpText_BOG_strategy = st.builds(
    afpText_BOG,
    OEGName=
        safe_text
)
afpText_PMC_strategy = st.builds(
    afpText_PMC,
    PMCid=
        safe_text
)
afpText_BFM_strategy = st.builds(
    afpText_BFM,
    FMName=
        safe_text
)
afpText_BRS_strategy = st.builds(
    afpText_BRS,
    RSName=
        safe_text
)
afpText_PTX_strategy = st.builds(
    afpText_PTX,
)
afpText_LNC_strategy = st.builds(
    afpText_LNC,
    NumDSC=
        safe_text
)
afpText_MFC_strategy = st.builds(
    afpText_MFC,
    MFCFlgs=
        safe_text,
    MedColl=
        safe_text,
    MFCScpe=
        safe_text
)
afpText_MPS_strategy = st.builds(
    afpText_MPS,
    Reserved=
        safe_text,
    RGLength=
        safe_text
)
afpText_PTD1_strategy = st.builds(
    afpText_PTD1,
    YPEXTENT=
        safe_text,
    YPUNITVL=
        safe_text,
    XPUNITVL=
        safe_text,
    XPBASE=
        safe_text,
    XPEXTENT=
        safe_text,
    YPBASE=
        safe_text,
    RESERVED=
        safe_text
)
afpText_MCF1_strategy = st.builds(
    afpText_MCF1,
    RGLength=
        safe_text
)
afpText_LND_strategy = st.builds(
    afpText_LND,
    LNDFlgs=
        safe_text,
    SupName=
        safe_text,
    NLNDsp=
        safe_text,
    CCPID=
        safe_text,
    ChnlCde=
        safe_text,
    TxtOrent=
        safe_text,
    TxtColor=
        safe_text,
    BPos=
        safe_text,
    DataLgth=
        safe_text,
    DataStrt=
        safe_text,
    NLNDccp=
        safe_text,
    FntLID=
        safe_text,
    NLNDskp=
        safe_text,
    SubpgID=
        safe_text,
    NLNDreu=
        safe_text,
    IPos=
        safe_text,
    SOLid=
        safe_text
)
afpText_BDI_strategy = st.builds(
    afpText_BDI,
    IndxName=
        safe_text
)
afpText_BPG_strategy = st.builds(
    afpText_BPG,
    PageName=
        safe_text
)
afpText_CFI_strategy = st.builds(
    afpText_CFI,
)
afpText_NOP_strategy = st.builds(
    afpText_NOP,
    UndfData=
        safe_text
)
afpText_PTD_strategy = st.builds(
    afpText_PTD,
    XPBASE=
        safe_text,
    XPUNITVL=
        safe_text,
    RESERVED=
        safe_text,
    YPEXTENT=
        safe_text,
    YPUNITVL=
        safe_text,
    YPBASE=
        safe_text,
    XPEXTENT=
        safe_text
)
afpText_OCD_strategy = st.builds(
    afpText_OCD,
    ObjCdat=
        safe_text
)
afpText_LLE_strategy = st.builds(
    afpText_LLE,
    LnkType=
        safe_text
)
afpText_BPS_strategy = st.builds(
    afpText_BPS,
    PsegName=
        safe_text
)
afpText_MDD_strategy = st.builds(
    afpText_MDD,
    MDDFlgs=
        safe_text,
    XmBase=
        safe_text,
    YmSize=
        safe_text,
    YmUnits=
        safe_text,
    XmSize=
        safe_text,
    XmUnits=
        safe_text,
    YmBase=
        safe_text
)
afpText_MPG_strategy = st.builds(
    afpText_MPG,
)
afpText_MMT_strategy = st.builds(
    afpText_MMT,
)
afpText_EDM_strategy = st.builds(
    afpText_EDM,
    DMName=
        safe_text
)
afpText_PEC_strategy = st.builds(
    afpText_PEC,
)
afpText_DXD_strategy = st.builds(
    afpText_DXD,
)
afpText_CPD_strategy = st.builds(
    afpText_CPD,
    GCGIDLen=
        safe_text,
    EncScheme=
        safe_text,
    CPDesc=
        safe_text,
    NumCdPts=
        safe_text,
    CPGID=
        safe_text,
    GCSGID=
        safe_text
)
afpText_ECA_strategy = st.builds(
    afpText_ECA,
    CATName=
        safe_text
)
afpText_CDD_strategy = st.builds(
    afpText_CDD,
    YocSize=
        safe_text,
    YocUnits=
        safe_text,
    XocUnits=
        safe_text,
    XocBase=
        safe_text,
    YocBase=
        safe_text,
    XocSize=
        safe_text
)
afpText_BFN_strategy = st.builds(
    afpText_BFN,
    RSName=
        safe_text
)
afpText_BII_strategy = st.builds(
    afpText_BII,
    ImoName=
        safe_text
)
afpText_PGP_strategy = st.builds(
    afpText_PGP,
    Constant=
        safe_text
)
afpText_PGD_strategy = st.builds(
    afpText_PGD,
    YpgSize=
        safe_text,
    YpgUnits=
        safe_text,
    XpgUnits=
        safe_text,
    XpgBase=
        safe_text,
    YpgBase=
        safe_text,
    Reserved=
        safe_text,
    XpgSize=
        safe_text
)
afpText_BOC_strategy = st.builds(
    afpText_BOC,
    ObjCName=
        safe_text
)
afpText_TLE_strategy = st.builds(
    afpText_TLE,
)
afpText_BDG_strategy = st.builds(
    afpText_BDG,
    DEGName=
        safe_text
)
afpText_CFC_strategy = st.builds(
    afpText_CFC,
    CFIRGLen=
        safe_text,
    Retired1=
        safe_text
)
afpText_MIO_strategy = st.builds(
    afpText_MIO,
)
afpText_BBC_strategy = st.builds(
    afpText_BBC,
    BCdoName=
        safe_text
)
afpText_BAG_strategy = st.builds(
    afpText_BAG,
    AEGName=
        safe_text
)
afpText_PPO_strategy = st.builds(
    afpText_PPO,
)
afpText_BPT_strategy = st.builds(
    afpText_BPT,
    PTdoName=
        safe_text
)
afpText_ECP_strategy = st.builds(
    afpText_ECP,
    RSName=
        safe_text
)
afpText_MMO_strategy = st.builds(
    afpText_MMO,
    RGLength=
        safe_text
)
afpText_BCP_strategy = st.builds(
    afpText_BCP,
    RSName=
        safe_text
)
afpText_MGO_strategy = st.builds(
    afpText_MGO,
)
afpText_PFC_strategy = st.builds(
    afpText_PFC,
    PFCFlgs=
        safe_text
)
afpText_CTC_strategy = st.builds(
    afpText_CTC,
    ConData=
        safe_text
)
afpText_BSG_strategy = st.builds(
    afpText_BSG,
    REGName=
        safe_text
)
afpText_BGR_strategy = st.builds(
    afpText_BGR,
    GdoName=
        safe_text
)
afpText_BCF_strategy = st.builds(
    afpText_BCF,
    RSName=
        safe_text
)
afpText_MBC_strategy = st.builds(
    afpText_MBC,
)
afpText_BDM_strategy = st.builds(
    afpText_BDM,
    DatFmt=
        safe_text,
    DMName=
        safe_text
)
afpText_FGD_strategy = st.builds(
    afpText_FGD,
    ConData=
        safe_text
)
afpText_MDR_strategy = st.builds(
    afpText_MDR,
)
afpText_MMC_strategy = st.builds(
    afpText_MMC,
    MMCid=
        safe_text,
    PARAMETER1=
        safe_text
)
afpText_BFG_strategy = st.builds(
    afpText_BFG,
    FEGName=
        safe_text
)
afpText_MSU_strategy = st.builds(
    afpText_MSU,
)
afpText_EBC_strategy = st.builds(
    afpText_EBC,
    BCdoName=
        safe_text
)
afpText_OBD_strategy = st.builds(
    afpText_OBD,
)
afpText_CPI_strategy = st.builds(
    afpText_CPI,
)
afpText_BCA_strategy = st.builds(
    afpText_BCA,
    CATName=
        safe_text
)
afpText_EDG_strategy = st.builds(
    afpText_EDG,
    DEGName=
        safe_text
)
afpText_OBP_strategy = st.builds(
    afpText_OBP,
    XoaOset=
        safe_text,
    OAPosID=
        safe_text,
    YoaOset=
        safe_text,
    YocaOrent=
        safe_text,
    YoaOrent=
        safe_text,
    RGLength=
        safe_text,
    XocaOrent=
        safe_text,
    XocaOset=
        safe_text,
    XoaOrent=
        safe_text,
    RefCSys=
        safe_text,
    YocaOset=
        safe_text
)
afpText_BNG_strategy = st.builds(
    afpText_BNG,
    PGrpName=
        safe_text
)
afpText_BMO_strategy = st.builds(
    afpText_BMO,
    OvlyName=
        safe_text
)
afpText_CPC_strategy = st.builds(
    afpText_CPC,
    PrtFlags=
        safe_text,
    CPIRGLen=
        safe_text,
    VSCharSN=
        safe_text,
    VSChar=
        safe_text,
    DefCharID=
        safe_text,
    VSFlags=
        safe_text
)
afpText_MCA_strategy = st.builds(
    afpText_MCA,
)
afpText_MCC_strategy = st.builds(
    afpText_MCC,
)
afpText_MCF_strategy = st.builds(
    afpText_MCF,
)
afpText_EDI_strategy = st.builds(
    afpText_EDI,
    IndxName=
        safe_text
)
afpText_BDD_strategy = st.builds(
    afpText_BDD,
    MULT=
        safe_text,
    WENE=
        safe_text,
    YUPUB=
        safe_text,
    ELEMENTHEIGHT=
        safe_text,
    YEXTENT=
        safe_text,
    MOD=
        safe_text,
    XEXTENT=
        safe_text,
    LID=
        safe_text,
    MODULEWIDTH=
        safe_text,
    XUPUB=
        safe_text,
    Reserved2=
        safe_text,
    UBASE=
        safe_text,
    Reserved=
        safe_text,
    TYPE=
        safe_text,
    COLOR=
        safe_text
)
afpText_MMD_strategy = st.builds(
    afpText_MMD,
)
afpText_BDA_strategy = st.builds(
    afpText_BDA,
    Data=
        safe_text,
    Xoffset=
        safe_text,
    Flags=
        safe_text,
    Yoffset=
        safe_text
)
afpText_BIM_strategy = st.builds(
    afpText_BIM,
    IdoName=
        safe_text
)
afpText_BDX_strategy = st.builds(
    afpText_BDX,
    DMXName=
        safe_text
)
afpText_LineData_strategy = st.builds(
    afpText_LineData,
    linedata=
        safe_text
)
afpText_structuredField_strategy = st.builds(
    afpText_structuredField,
)
afpText_Model_strategy = st.builds(
    afpText_Model,
)
afpText_IPO_strategy = st.builds(
    afpText_IPO,
    OvlyName=
        safe_text,
    YolOset=
        safe_text,
    XolOset=
        safe_text,
    OvlyOrent=
        safe_text
)
afpText_IRD_strategy = st.builds(
    afpText_IRD,
    IMdata=
        safe_text
)
afpText_IPS_strategy = st.builds(
    afpText_IPS,
    YpsOset=
        safe_text,
    PsegName=
        safe_text,
    XpsOset=
        safe_text
)
afpText_IPG_strategy = st.builds(
    afpText_IPG,
    PgName=
        safe_text,
    IPgFlgs=
        safe_text
)
afpText_IPD_strategy = st.builds(
    afpText_IPD,
    imageData=
        safe_text,
    IOCAdat=
        safe_text
)
afpText_ICP_strategy = st.builds(
    afpText_ICP,
    XCSize=
        safe_text,
    XFilSize=
        safe_text,
    YCSize=
        safe_text,
    XCOset=
        safe_text,
    YCOset=
        safe_text,
    YFilSize=
        safe_text
)
afpText_IOC_strategy = st.builds(
    afpText_IOC,
    XMap=
        safe_text,
    XoaOset=
        safe_text,
    ConData1=
        safe_text,
    YMap=
        safe_text,
    YoaOrent=
        safe_text,
    ConData2=
        safe_text,
    XoaOrent=
        safe_text,
    YoaOset=
        safe_text
)
afpText_IOB_strategy = st.builds(
    afpText_IOB,
    XoaOrent=
        safe_text,
    YoaOrent=
        safe_text,
    XoaOset=
        safe_text,
    XocaOset=
        safe_text,
    ObjName=
        safe_text,
    YocaOset=
        safe_text,
    ObjType=
        safe_text,
    RefCSys=
        safe_text,
    YoaOset=
        safe_text
)
afpText_IMM_strategy = st.builds(
    afpText_IMM,
    MMPName=
        safe_text
)
afpText_IID_strategy = st.builds(
    afpText_IID,
    YSize=
        safe_text,
    YCSizeD=
        safe_text,
    YBase=
        safe_text,
    ConData3=
        safe_text,
    YUnits=
        safe_text,
    XBase=
        safe_text,
    XCSizeD=
        safe_text,
    Color=
        safe_text,
    XSize=
        safe_text,
    ConData2=
        safe_text,
    ConData1=
        safe_text,
    XUnits=
        safe_text
)
afpText_IEL_strategy = st.builds(
    afpText_IEL,
)
afpText_IDD_strategy = st.builds(
    afpText_IDD,
    YSIZE=
        safe_text,
    YRESOL=
        safe_text,
    XRESOL=
        safe_text,
    XSIZE=
        safe_text,
    UNITBASE=
        safe_text
)
afpText_GDD_strategy = st.builds(
    afpText_GDD,
    GOCAdes=
        safe_text
)
afpText_GAD_strategy = st.builds(
    afpText_GAD,
    GOCAdat=
        safe_text
)
afpText_FNPRG_strategy = st.builds(
    afpText_FNPRG,
    LcHeight=
        safe_text,
    MaxDesDp=
        safe_text,
    Reserved2=
        safe_text,
    Reserved3=
        safe_text,
    UscoreWdf=
        safe_text,
    Retired=
        safe_text,
    CapMHt=
        safe_text,
    MaxAscHt=
        safe_text,
    UscoreWd=
        safe_text,
    UscorePos=
        safe_text,
    Reserved=
        safe_text
)
afpText_FNP_strategy = st.builds(
    afpText_FNP,
)
afpText_FNORG_strategy = st.builds(
    afpText_FNORG,
    MaxCharInc=
        safe_text,
    NomCharInc=
        safe_text,
    MaxBOset=
        safe_text,
    DefBInc=
        safe_text,
    FigSpInc=
        safe_text,
    Reserved3=
        safe_text,
    CharRot=
        safe_text,
    EmSpInc=
        safe_text,
    Reserved=
        safe_text,
    Reserved2=
        safe_text,
    OrntFlgs=
        safe_text,
    MaxBExt=
        safe_text,
    SpCharInc=
        safe_text,
    MinASp=
        safe_text
)
afpText_FNO_strategy = st.builds(
    afpText_FNO,
)
afpText_FNMRG_strategy = st.builds(
    afpText_FNMRG,
    PatDOset=
        safe_text,
    CharBoxHt=
        safe_text,
    CharBoxWd=
        safe_text
)
afpText_FNM_strategy = st.builds(
    afpText_FNM,
)
afpText_FNN_strategy = st.builds(
    afpText_FNN,
    FNNData=
        safe_text
)
afpText_FNIRG_strategy = st.builds(
    afpText_FNIRG,
    FNMCnt=
        safe_text,
    CharInc=
        safe_text,
    Reserved=
        safe_text,
    BaseOset=
        safe_text,
    CSpace=
        safe_text,
    GCGID=
        safe_text,
    BSpace=
        safe_text,
    ASpace=
        safe_text,
    DescendDp=
        safe_text,
    AscendHt=
        safe_text,
    Reserved2=
        safe_text
)
afpText_FNI_strategy = st.builds(
    afpText_FNI,
)
afpText_FNG_strategy = st.builds(
    afpText_FNG,
    PatData=
        safe_text
)
afpText_EPT_strategy = st.builds(
    afpText_EPT,
    PTdoName=
        safe_text
)
afpText_FND_strategy = st.builds(
    afpText_FND,
    MinPtSize=
        safe_text,
    TypeFcDesc=
        safe_text,
    MaxPtSize=
        safe_text,
    DsnGenCls=
        safe_text,
    DsnSpcGrp=
        safe_text,
    FtWdClass=
        safe_text,
    FtWtClass=
        safe_text,
    NomHSize=
        safe_text,
    MaxHSize=
        safe_text,
    Reserved1=
        safe_text,
    DsnSubCls=
        safe_text,
    MinHSize=
        safe_text,
    FGID=
        safe_text,
    GCSID=
        safe_text,
    Reserved2=
        safe_text,
    NomPtSize=
        safe_text,
    FtDsFlags=
        safe_text
)
afpText_FNC_strategy = st.builds(
    afpText_FNC,
    XUnitBase=
        safe_text,
    OPatDCnt=
        safe_text,
    XftUnits=
        safe_text,
    FNNMapCnt=
        safe_text,
    FNIRGLen=
        safe_text,
    FNNDCnt=
        safe_text,
    FNMRGLen=
        safe_text,
    FntFlags=
        safe_text,
    ResYUBase=
        safe_text,
    MaxBoxHt=
        safe_text,
    PatAlign=
        safe_text,
    Retired=
        safe_text,
    PatTech=
        safe_text,
    Reserved1=
        safe_text,
    RPatDCnt=
        safe_text,
    MaxBoxWd=
        safe_text,
    ResXUBase=
        safe_text,
    FNORGLen=
        safe_text,
    YftUnits=
        safe_text,
    FNNRGLen=
        safe_text,
    FNPRGLen=
        safe_text,
    XfrUnits=
        safe_text,
    YfrUnits=
        safe_text,
    Reserved2=
        safe_text,
    YUnitBase=
        safe_text
)
afpText_ESG_strategy = st.builds(
    afpText_ESG,
    REGName=
        safe_text
)
afpText_ERS_strategy = st.builds(
    afpText_ERS,
    RSName=
        safe_text
)
afpText_ERG_strategy = st.builds(
    afpText_ERG,
    RGrpName=
        safe_text
)
afpText_EIM_strategy = st.builds(
    afpText_EIM,
    IdoName=
        safe_text
)
afpText_EPS_strategy = st.builds(
    afpText_EPS,
    PsegName=
        safe_text
)
afpText_EPM_strategy = st.builds(
    afpText_EPM,
    PMName=
        safe_text
)
afpText_EPG_strategy = st.builds(
    afpText_EPG,
    PageName=
        safe_text
)
afpText_EPF_strategy = st.builds(
    afpText_EPF,
    PFName=
        safe_text
)
afpText_EOG_strategy = st.builds(
    afpText_EOG,
    OEGName=
        safe_text
)
afpText_EOC_strategy = st.builds(
    afpText_EOC,
    ObjCName=
        safe_text
)
afpText_ENG_strategy = st.builds(
    afpText_ENG,
    PGrpName=
        safe_text
)
afpText_EMO_strategy = st.builds(
    afpText_EMO,
    OvlyName=
        safe_text
)
afpText_EMM_strategy = st.builds(
    afpText_EMM,
    MMName=
        safe_text
)
afpText_EII_strategy = st.builds(
    afpText_EII,
    ImoName=
        safe_text
)
afpText_EGR_strategy = st.builds(
    afpText_EGR,
    GdoName=
        safe_text
)
afpText_EFN_strategy = st.builds(
    afpText_EFN,
    RSName=
        safe_text
)
afpText_EFM_strategy = st.builds(
    afpText_EFM,
    FMName=
        safe_text
)
afpText_EFG_strategy = st.builds(
    afpText_EFG,
    FEGName=
        safe_text
)
afpText_EDX_strategy = st.builds(
    afpText_EDX,
    DMXName=
        safe_text
)
afpText_EDT_strategy = st.builds(
    afpText_EDT,
    DocName=
        safe_text
)

@given(instance=triplet_strategy)
@settings(max_examples=50)
def test_triplet_instantiation(instance):
    assert isinstance(instance, triplet)

@given(instance=afpText_IDESize_strategy)
@settings(max_examples=50)
def test_afptext_idesize_instantiation(instance):
    assert isinstance(instance, afpText_IDESize)



@given(instance=afpText_IDESize_strategy)
def test_afptext_idesize_IDESZ_setter(instance):
    original = instance.IDESZ
    instance.IDESZ = original
    assert instance.IDESZ == original

@given(instance=afpText_FontHorizontalScaleFactor_strategy)
@settings(max_examples=50)
def test_afptext_fonthorizontalscalefactor_instantiation(instance):
    assert isinstance(instance, afpText_FontHorizontalScaleFactor)



@given(instance=afpText_FontHorizontalScaleFactor_strategy)
def test_afptext_fonthorizontalscalefactor_Hscale_setter(instance):
    original = instance.Hscale
    instance.Hscale = original
    assert instance.Hscale == original

@given(instance=afpText_ObjectClassification_strategy)
@settings(max_examples=50)
def test_afptext_objectclassification_instantiation(instance):
    assert isinstance(instance, afpText_ObjectClassification)



@given(instance=afpText_ObjectClassification_strategy)
def test_afptext_objectclassification_ObjClass_setter(instance):
    original = instance.ObjClass
    instance.ObjClass = original
    assert instance.ObjClass == original



@given(instance=afpText_ObjectClassification_strategy)
def test_afptext_objectclassification_CompName_setter(instance):
    original = instance.CompName
    instance.CompName = original
    assert instance.CompName == original



@given(instance=afpText_ObjectClassification_strategy)
def test_afptext_objectclassification_StrucFlgs_setter(instance):
    original = instance.StrucFlgs
    instance.StrucFlgs = original
    assert instance.StrucFlgs == original



@given(instance=afpText_ObjectClassification_strategy)
def test_afptext_objectclassification_ObjLev_setter(instance):
    original = instance.ObjLev
    instance.ObjLev = original
    assert instance.ObjLev == original



@given(instance=afpText_ObjectClassification_strategy)
def test_afptext_objectclassification_RegObjId_setter(instance):
    original = instance.RegObjId
    instance.RegObjId = original
    assert instance.RegObjId == original



@given(instance=afpText_ObjectClassification_strategy)
def test_afptext_objectclassification_ObjTpName_setter(instance):
    original = instance.ObjTpName
    instance.ObjTpName = original
    assert instance.ObjTpName == original

@given(instance=afpText_FinishingOperation_strategy)
@settings(max_examples=50)
def test_afptext_finishingoperation_instantiation(instance):
    assert isinstance(instance, afpText_FinishingOperation)



@given(instance=afpText_FinishingOperation_strategy)
def test_afptext_finishingoperation_AxOffst_setter(instance):
    original = instance.AxOffst
    instance.AxOffst = original
    assert instance.AxOffst == original



@given(instance=afpText_FinishingOperation_strategy)
def test_afptext_finishingoperation_FOpCnt_setter(instance):
    original = instance.FOpCnt
    instance.FOpCnt = original
    assert instance.FOpCnt == original



@given(instance=afpText_FinishingOperation_strategy)
def test_afptext_finishingoperation_FOpType_setter(instance):
    original = instance.FOpType
    instance.FOpType = original
    assert instance.FOpType == original



@given(instance=afpText_FinishingOperation_strategy)
def test_afptext_finishingoperation_RefEdge_setter(instance):
    original = instance.RefEdge
    instance.RefEdge = original
    assert instance.RefEdge == original



@given(instance=afpText_FinishingOperation_strategy)
def test_afptext_finishingoperation_OpPos_setter(instance):
    original = instance.OpPos
    instance.OpPos = original
    assert instance.OpPos == original

@given(instance=afpText_BandImageData_strategy)
@settings(max_examples=50)
def test_afptext_bandimagedata_instantiation(instance):
    assert isinstance(instance, afpText_BandImageData)



@given(instance=afpText_BandImageData_strategy)
def test_afptext_bandimagedata_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original



@given(instance=afpText_BandImageData_strategy)
def test_afptext_bandimagedata_BANDNUM_setter(instance):
    original = instance.BANDNUM
    instance.BANDNUM = original
    assert instance.BANDNUM == original



@given(instance=afpText_BandImageData_strategy)
def test_afptext_bandimagedata_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText_DeviceAppearance_strategy)
@settings(max_examples=50)
def test_afptext_deviceappearance_instantiation(instance):
    assert isinstance(instance, afpText_DeviceAppearance)



@given(instance=afpText_DeviceAppearance_strategy)
def test_afptext_deviceappearance_DevApp_setter(instance):
    original = instance.DevApp
    instance.DevApp = original
    assert instance.DevApp == original



@given(instance=afpText_DeviceAppearance_strategy)
def test_afptext_deviceappearance_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_ColorSpecification_strategy)
@settings(max_examples=50)
def test_afptext_colorspecification_instantiation(instance):
    assert isinstance(instance, afpText_ColorSpecification)



@given(instance=afpText_ColorSpecification_strategy)
def test_afptext_colorspecification_ColSpce_setter(instance):
    original = instance.ColSpce
    instance.ColSpce = original
    assert instance.ColSpce == original



@given(instance=afpText_ColorSpecification_strategy)
def test_afptext_colorspecification_ColSize2_setter(instance):
    original = instance.ColSize2
    instance.ColSize2 = original
    assert instance.ColSize2 == original



@given(instance=afpText_ColorSpecification_strategy)
def test_afptext_colorspecification_ColSize4_setter(instance):
    original = instance.ColSize4
    instance.ColSize4 = original
    assert instance.ColSize4 == original



@given(instance=afpText_ColorSpecification_strategy)
def test_afptext_colorspecification_ColSize1_setter(instance):
    original = instance.ColSize1
    instance.ColSize1 = original
    assert instance.ColSize1 == original



@given(instance=afpText_ColorSpecification_strategy)
def test_afptext_colorspecification_ColSize3_setter(instance):
    original = instance.ColSize3
    instance.ColSize3 = original
    assert instance.ColSize3 == original



@given(instance=afpText_ColorSpecification_strategy)
def test_afptext_colorspecification_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
@settings(max_examples=50)
def test_afptext_universaldateandtimestamp_instantiation(instance):
    assert isinstance(instance, afpText_UniversalDateAndTimeStamp)



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_Second_setter(instance):
    original = instance.Second
    instance.Second = original
    assert instance.Second == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_Hour_setter(instance):
    original = instance.Hour
    instance.Hour = original
    assert instance.Hour == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_YearAD_setter(instance):
    original = instance.YearAD
    instance.YearAD = original
    assert instance.YearAD == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_Day_setter(instance):
    original = instance.Day
    instance.Day = original
    assert instance.Day == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_UTCDiffM_setter(instance):
    original = instance.UTCDiffM
    instance.UTCDiffM = original
    assert instance.UTCDiffM == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_TimeZone_setter(instance):
    original = instance.TimeZone
    instance.TimeZone = original
    assert instance.TimeZone == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_UTCDiffH_setter(instance):
    original = instance.UTCDiffH
    instance.UTCDiffH = original
    assert instance.UTCDiffH == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_Minute_setter(instance):
    original = instance.Minute
    instance.Minute = original
    assert instance.Minute == original



@given(instance=afpText_UniversalDateAndTimeStamp_strategy)
def test_afptext_universaldateandtimestamp_Month_setter(instance):
    original = instance.Month
    instance.Month = original
    assert instance.Month == original

@given(instance=afpText_ExtendedResourceLocalIdentifier_strategy)
@settings(max_examples=50)
def test_afptext_extendedresourcelocalidentifier_instantiation(instance):
    assert isinstance(instance, afpText_ExtendedResourceLocalIdentifier)



@given(instance=afpText_ExtendedResourceLocalIdentifier_strategy)
def test_afptext_extendedresourcelocalidentifier_ResLID_setter(instance):
    original = instance.ResLID
    instance.ResLID = original
    assert instance.ResLID == original



@given(instance=afpText_ExtendedResourceLocalIdentifier_strategy)
def test_afptext_extendedresourcelocalidentifier_ResType_setter(instance):
    original = instance.ResType
    instance.ResType = original
    assert instance.ResType == original

@given(instance=afpText_ResourceSectionNumber_strategy)
@settings(max_examples=50)
def test_afptext_resourcesectionnumber_instantiation(instance):
    assert isinstance(instance, afpText_ResourceSectionNumber)



@given(instance=afpText_ResourceSectionNumber_strategy)
def test_afptext_resourcesectionnumber_ResSNum_setter(instance):
    original = instance.ResSNum
    instance.ResSNum = original
    assert instance.ResSNum == original

@given(instance=afpText_EndImage_strategy)
@settings(max_examples=50)
def test_afptext_endimage_instantiation(instance):
    assert isinstance(instance, afpText_EndImage)

@given(instance=afpText_GSCS_strategy)
@settings(max_examples=50)
def test_afptext_gscs_instantiation(instance):
    assert isinstance(instance, afpText_GSCS)



@given(instance=afpText_GSCS_strategy)
def test_afptext_gscs_LCID_setter(instance):
    original = instance.LCID
    instance.LCID = original
    assert instance.LCID == original

@given(instance=afpText_GSCP_strategy)
@settings(max_examples=50)
def test_afptext_gscp_instantiation(instance):
    assert isinstance(instance, afpText_GSCP)



@given(instance=afpText_GSCP_strategy)
def test_afptext_gscp_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GSCP_strategy)
def test_afptext_gscp_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_GCBEZ_strategy)
@settings(max_examples=50)
def test_afptext_gcbez_instantiation(instance):
    assert isinstance(instance, afpText_GCBEZ)

@given(instance=afpText_LineDataObjectPositionMigration_strategy)
@settings(max_examples=50)
def test_afptext_linedataobjectpositionmigration_instantiation(instance):
    assert isinstance(instance, afpText_LineDataObjectPositionMigration)



@given(instance=afpText_LineDataObjectPositionMigration_strategy)
def test_afptext_linedataobjectpositionmigration_TempOrient_setter(instance):
    original = instance.TempOrient
    instance.TempOrient = original
    assert instance.TempOrient == original

@given(instance=afpText_FontDescriptorSpecification_strategy)
@settings(max_examples=50)
def test_afptext_fontdescriptorspecification_instantiation(instance):
    assert isinstance(instance, afpText_FontDescriptorSpecification)



@given(instance=afpText_FontDescriptorSpecification_strategy)
def test_afptext_fontdescriptorspecification_FtHeight_setter(instance):
    original = instance.FtHeight
    instance.FtHeight = original
    assert instance.FtHeight == original



@given(instance=afpText_FontDescriptorSpecification_strategy)
def test_afptext_fontdescriptorspecification_FtUsFlags_setter(instance):
    original = instance.FtUsFlags
    instance.FtUsFlags = original
    assert instance.FtUsFlags == original



@given(instance=afpText_FontDescriptorSpecification_strategy)
def test_afptext_fontdescriptorspecification_FtDsFlags_setter(instance):
    original = instance.FtDsFlags
    instance.FtDsFlags = original
    assert instance.FtDsFlags == original



@given(instance=afpText_FontDescriptorSpecification_strategy)
def test_afptext_fontdescriptorspecification_FtWtClass_setter(instance):
    original = instance.FtWtClass
    instance.FtWtClass = original
    assert instance.FtWtClass == original



@given(instance=afpText_FontDescriptorSpecification_strategy)
def test_afptext_fontdescriptorspecification_FtWidth_setter(instance):
    original = instance.FtWidth
    instance.FtWidth = original
    assert instance.FtWidth == original



@given(instance=afpText_FontDescriptorSpecification_strategy)
def test_afptext_fontdescriptorspecification_FtWdClass_setter(instance):
    original = instance.FtWdClass
    instance.FtWdClass = original
    assert instance.FtWdClass == original

@given(instance=afpText_ObjectOriginIdentifier_strategy)
@settings(max_examples=50)
def test_afptext_objectoriginidentifier_instantiation(instance):
    assert isinstance(instance, afpText_ObjectOriginIdentifier)



@given(instance=afpText_ObjectOriginIdentifier_strategy)
def test_afptext_objectoriginidentifier_SysID_setter(instance):
    original = instance.SysID
    instance.SysID = original
    assert instance.SysID == original



@given(instance=afpText_ObjectOriginIdentifier_strategy)
def test_afptext_objectoriginidentifier_System_setter(instance):
    original = instance.System
    instance.System = original
    assert instance.System == original



@given(instance=afpText_ObjectOriginIdentifier_strategy)
def test_afptext_objectoriginidentifier_MedID_setter(instance):
    original = instance.MedID
    instance.MedID = original
    assert instance.MedID == original



@given(instance=afpText_ObjectOriginIdentifier_strategy)
def test_afptext_objectoriginidentifier_DSID_setter(instance):
    original = instance.DSID
    instance.DSID = original
    assert instance.DSID == original

@given(instance=afpText_GSLT_strategy)
@settings(max_examples=50)
def test_afptext_gslt_instantiation(instance):
    assert isinstance(instance, afpText_GSLT)



@given(instance=afpText_GSLT_strategy)
def test_afptext_gslt_LINETYPE_setter(instance):
    original = instance.LINETYPE
    instance.LINETYPE = original
    assert instance.LINETYPE == original

@given(instance=afpText_MediumOrientation_strategy)
@settings(max_examples=50)
def test_afptext_mediumorientation_instantiation(instance):
    assert isinstance(instance, afpText_MediumOrientation)



@given(instance=afpText_MediumOrientation_strategy)
def test_afptext_mediumorientation_MedOrient_setter(instance):
    original = instance.MedOrient
    instance.MedOrient = original
    assert instance.MedOrient == original

@given(instance=afpText_TileSize_strategy)
@settings(max_examples=50)
def test_afptext_tilesize_instantiation(instance):
    assert isinstance(instance, afpText_TileSize)



@given(instance=afpText_TileSize_strategy)
def test_afptext_tilesize_RELRES_setter(instance):
    original = instance.RELRES
    instance.RELRES = original
    assert instance.RELRES == original



@given(instance=afpText_TileSize_strategy)
def test_afptext_tilesize_TVSIZE_setter(instance):
    original = instance.TVSIZE
    instance.TVSIZE = original
    assert instance.TVSIZE == original



@given(instance=afpText_TileSize_strategy)
def test_afptext_tilesize_THSIZE_setter(instance):
    original = instance.THSIZE
    instance.THSIZE = original
    assert instance.THSIZE == original

@given(instance=afpText_EncodingSchemeID_strategy)
@settings(max_examples=50)
def test_afptext_encodingschemeid_instantiation(instance):
    assert isinstance(instance, afpText_EncodingSchemeID)



@given(instance=afpText_EncodingSchemeID_strategy)
def test_afptext_encodingschemeid_ESidCP_setter(instance):
    original = instance.ESidCP
    instance.ESidCP = original
    assert instance.ESidCP == original



@given(instance=afpText_EncodingSchemeID_strategy)
def test_afptext_encodingschemeid_ESidUD_setter(instance):
    original = instance.ESidUD
    instance.ESidUD = original
    assert instance.ESidUD == original

@given(instance=afpText_FontFidelity_strategy)
@settings(max_examples=50)
def test_afptext_fontfidelity_instantiation(instance):
    assert isinstance(instance, afpText_FontFidelity)



@given(instance=afpText_FontFidelity_strategy)
def test_afptext_fontfidelity_StpFntEx_setter(instance):
    original = instance.StpFntEx
    instance.StpFntEx = original
    assert instance.StpFntEx == original

@given(instance=afpText_BeginImage_strategy)
@settings(max_examples=50)
def test_afptext_beginimage_instantiation(instance):
    assert isinstance(instance, afpText_BeginImage)



@given(instance=afpText_BeginImage_strategy)
def test_afptext_beginimage_OBJTYPE_setter(instance):
    original = instance.OBJTYPE
    instance.OBJTYPE = original
    assert instance.OBJTYPE == original

@given(instance=afpText_GCMRK_strategy)
@settings(max_examples=50)
def test_afptext_gcmrk_instantiation(instance):
    assert isinstance(instance, afpText_GCMRK)

@given(instance=afpText_GSCR_strategy)
@settings(max_examples=50)
def test_afptext_gscr_instantiation(instance):
    assert isinstance(instance, afpText_GSCR)



@given(instance=afpText_GSCR_strategy)
def test_afptext_gscr_PREC_setter(instance):
    original = instance.PREC
    instance.PREC = original
    assert instance.PREC == original

@given(instance=afpText_ImageSize_strategy)
@settings(max_examples=50)
def test_afptext_imagesize_instantiation(instance):
    assert isinstance(instance, afpText_ImageSize)



@given(instance=afpText_ImageSize_strategy)
def test_afptext_imagesize_VSIZE_setter(instance):
    original = instance.VSIZE
    instance.VSIZE = original
    assert instance.VSIZE == original



@given(instance=afpText_ImageSize_strategy)
def test_afptext_imagesize_HRESOL_setter(instance):
    original = instance.HRESOL
    instance.HRESOL = original
    assert instance.HRESOL == original



@given(instance=afpText_ImageSize_strategy)
def test_afptext_imagesize_VRESOL_setter(instance):
    original = instance.VRESOL
    instance.VRESOL = original
    assert instance.VRESOL == original



@given(instance=afpText_ImageSize_strategy)
def test_afptext_imagesize_HSIZE_setter(instance):
    original = instance.HSIZE
    instance.HSIZE = original
    assert instance.HSIZE == original



@given(instance=afpText_ImageSize_strategy)
def test_afptext_imagesize_UNITBASE_setter(instance):
    original = instance.UNITBASE
    instance.UNITBASE = original
    assert instance.UNITBASE == original

@given(instance=afpText_PagePositionInformation_strategy)
@settings(max_examples=50)
def test_afptext_pagepositioninformation_instantiation(instance):
    assert isinstance(instance, afpText_PagePositionInformation)



@given(instance=afpText_PagePositionInformation_strategy)
def test_afptext_pagepositioninformation_PGPRG_setter(instance):
    original = instance.PGPRG
    instance.PGPRG = original
    assert instance.PGPRG == original

@given(instance=afpText_GFLT_strategy)
@settings(max_examples=50)
def test_afptext_gflt_instantiation(instance):
    assert isinstance(instance, afpText_GFLT)

@given(instance=afpText_ImageData_strategy)
@settings(max_examples=50)
def test_afptext_imagedata_instantiation(instance):
    assert isinstance(instance, afpText_ImageData)



@given(instance=afpText_ImageData_strategy)
def test_afptext_imagedata_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText_AttributeValue_strategy)
@settings(max_examples=50)
def test_afptext_attributevalue_instantiation(instance):
    assert isinstance(instance, afpText_AttributeValue)



@given(instance=afpText_AttributeValue_strategy)
def test_afptext_attributevalue_AttVal_setter(instance):
    original = instance.AttVal
    instance.AttVal = original
    assert instance.AttVal == original



@given(instance=afpText_AttributeValue_strategy)
def test_afptext_attributevalue_Reserved0_setter(instance):
    original = instance.Reserved0
    instance.Reserved0 = original
    assert instance.Reserved0 == original

@given(instance=afpText_EndTransparencyMask_strategy)
@settings(max_examples=50)
def test_afptext_endtransparencymask_instantiation(instance):
    assert isinstance(instance, afpText_EndTransparencyMask)

@given(instance=afpText_GSPCOL_strategy)
@settings(max_examples=50)
def test_afptext_gspcol_instantiation(instance):
    assert isinstance(instance, afpText_GSPCOL)



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_COLSIZE2_setter(instance):
    original = instance.COLSIZE2
    instance.COLSIZE2 = original
    assert instance.COLSIZE2 == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_COLSIZE3_setter(instance):
    original = instance.COLSIZE3
    instance.COLSIZE3 = original
    assert instance.COLSIZE3 == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_COLVALUE_setter(instance):
    original = instance.COLVALUE
    instance.COLVALUE = original
    assert instance.COLVALUE == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_RES2_setter(instance):
    original = instance.RES2
    instance.RES2 = original
    assert instance.RES2 == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_COLSIZE1_setter(instance):
    original = instance.COLSIZE1
    instance.COLSIZE1 = original
    assert instance.COLSIZE1 == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_COLSPCE_setter(instance):
    original = instance.COLSPCE
    instance.COLSPCE = original
    assert instance.COLSPCE == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_RES1_setter(instance):
    original = instance.RES1
    instance.RES1 = original
    assert instance.RES1 == original



@given(instance=afpText_GSPCOL_strategy)
def test_afptext_gspcol_COLSIZE4_setter(instance):
    original = instance.COLSIZE4
    instance.COLSIZE4 = original
    assert instance.COLSIZE4 == original

@given(instance=afpText_TBM_strategy)
@settings(max_examples=50)
def test_afptext_tbm_instantiation(instance):
    assert isinstance(instance, afpText_TBM)



@given(instance=afpText_TBM_strategy)
def test_afptext_tbm_PRECSION_setter(instance):
    original = instance.PRECSION
    instance.PRECSION = original
    assert instance.PRECSION == original



@given(instance=afpText_TBM_strategy)
def test_afptext_tbm_DIRCTION_setter(instance):
    original = instance.DIRCTION
    instance.DIRCTION = original
    assert instance.DIRCTION == original



@given(instance=afpText_TBM_strategy)
def test_afptext_tbm_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText_GSGCH_strategy)
@settings(max_examples=50)
def test_afptext_gsgch_instantiation(instance):
    assert isinstance(instance, afpText_GSGCH)

@given(instance=afpText_ExternalAlgorithm_strategy)
@settings(max_examples=50)
def test_afptext_externalalgorithm_instantiation(instance):
    assert isinstance(instance, afpText_ExternalAlgorithm)



@given(instance=afpText_ExternalAlgorithm_strategy)
def test_afptext_externalalgorithm_ALGTYPE_setter(instance):
    original = instance.ALGTYPE
    instance.ALGTYPE = original
    assert instance.ALGTYPE == original

@given(instance=afpText_ObjectOffset_strategy)
@settings(max_examples=50)
def test_afptext_objectoffset_instantiation(instance):
    assert isinstance(instance, afpText_ObjectOffset)



@given(instance=afpText_ObjectOffset_strategy)
def test_afptext_objectoffset_ObjOset_setter(instance):
    original = instance.ObjOset
    instance.ObjOset = original
    assert instance.ObjOset == original



@given(instance=afpText_ObjectOffset_strategy)
def test_afptext_objectoffset_ObjTpe_setter(instance):
    original = instance.ObjTpe
    instance.ObjTpe = original
    assert instance.ObjTpe == original



@given(instance=afpText_ObjectOffset_strategy)
def test_afptext_objectoffset_ObjOstHi_setter(instance):
    original = instance.ObjOstHi
    instance.ObjOstHi = original
    assert instance.ObjOstHi == original

@given(instance=afpText_GCPARC_strategy)
@settings(max_examples=50)
def test_afptext_gcparc_instantiation(instance):
    assert isinstance(instance, afpText_GCPARC)



@given(instance=afpText_GCPARC_strategy)
def test_afptext_gcparc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original



@given(instance=afpText_GCPARC_strategy)
def test_afptext_gcparc_YCENT_setter(instance):
    original = instance.YCENT
    instance.YCENT = original
    assert instance.YCENT == original



@given(instance=afpText_GCPARC_strategy)
def test_afptext_gcparc_SWEEP_setter(instance):
    original = instance.SWEEP
    instance.SWEEP = original
    assert instance.SWEEP == original



@given(instance=afpText_GCPARC_strategy)
def test_afptext_gcparc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original



@given(instance=afpText_GCPARC_strategy)
def test_afptext_gcparc_START_setter(instance):
    original = instance.START
    instance.START = original
    assert instance.START == original



@given(instance=afpText_GCPARC_strategy)
def test_afptext_gcparc_XCENT_setter(instance):
    original = instance.XCENT
    instance.XCENT = original
    assert instance.XCENT == original

@given(instance=afpText_MappingOption_strategy)
@settings(max_examples=50)
def test_afptext_mappingoption_instantiation(instance):
    assert isinstance(instance, afpText_MappingOption)



@given(instance=afpText_MappingOption_strategy)
def test_afptext_mappingoption_MapValue_setter(instance):
    original = instance.MapValue
    instance.MapValue = original
    assert instance.MapValue == original

@given(instance=afpText_ObjectCount_strategy)
@settings(max_examples=50)
def test_afptext_objectcount_instantiation(instance):
    assert isinstance(instance, afpText_ObjectCount)



@given(instance=afpText_ObjectCount_strategy)
def test_afptext_objectcount_SobjNmHi_setter(instance):
    original = instance.SobjNmHi
    instance.SobjNmHi = original
    assert instance.SobjNmHi == original



@given(instance=afpText_ObjectCount_strategy)
def test_afptext_objectcount_SObjNum_setter(instance):
    original = instance.SObjNum
    instance.SObjNum = original
    assert instance.SObjNum == original



@given(instance=afpText_ObjectCount_strategy)
def test_afptext_objectcount_SubObj_setter(instance):
    original = instance.SubObj
    instance.SubObj = original
    assert instance.SubObj == original

@given(instance=afpText_TonerSaver_strategy)
@settings(max_examples=50)
def test_afptext_tonersaver_instantiation(instance):
    assert isinstance(instance, afpText_TonerSaver)



@given(instance=afpText_TonerSaver_strategy)
def test_afptext_tonersaver_TSvCtrl_setter(instance):
    original = instance.TSvCtrl
    instance.TSvCtrl = original
    assert instance.TSvCtrl == original

@given(instance=afpText_GSPT_strategy)
@settings(max_examples=50)
def test_afptext_gspt_instantiation(instance):
    assert isinstance(instance, afpText_GSPT)



@given(instance=afpText_GSPT_strategy)
def test_afptext_gspt_PATT_setter(instance):
    original = instance.PATT
    instance.PATT = original
    assert instance.PATT == original

@given(instance=afpText_GSCD_strategy)
@settings(max_examples=50)
def test_afptext_gscd_instantiation(instance):
    assert isinstance(instance, afpText_GSCD)



@given(instance=afpText_GSCD_strategy)
def test_afptext_gscd_DIRECTION_setter(instance):
    original = instance.DIRECTION
    instance.DIRECTION = original
    assert instance.DIRECTION == original

@given(instance=afpText_BandImage_strategy)
@settings(max_examples=50)
def test_afptext_bandimage_instantiation(instance):
    assert isinstance(instance, afpText_BandImage)



@given(instance=afpText_BandImage_strategy)
def test_afptext_bandimage_BCOUNT_setter(instance):
    original = instance.BCOUNT
    instance.BCOUNT = original
    assert instance.BCOUNT == original

@given(instance=afpText_RenderingIntent_strategy)
@settings(max_examples=50)
def test_afptext_renderingintent_instantiation(instance):
    assert isinstance(instance, afpText_RenderingIntent)



@given(instance=afpText_RenderingIntent_strategy)
def test_afptext_renderingintent_IOCARI_setter(instance):
    original = instance.IOCARI
    instance.IOCARI = original
    assert instance.IOCARI == original



@given(instance=afpText_RenderingIntent_strategy)
def test_afptext_renderingintent_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_RenderingIntent_strategy)
def test_afptext_renderingintent_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original



@given(instance=afpText_RenderingIntent_strategy)
def test_afptext_renderingintent_OCRI_setter(instance):
    original = instance.OCRI
    instance.OCRI = original
    assert instance.OCRI == original



@given(instance=afpText_RenderingIntent_strategy)
def test_afptext_renderingintent_GOCARI_setter(instance):
    original = instance.GOCARI
    instance.GOCARI = original
    assert instance.GOCARI == original



@given(instance=afpText_RenderingIntent_strategy)
def test_afptext_renderingintent_PTOCRI_setter(instance):
    original = instance.PTOCRI
    instance.PTOCRI = original
    assert instance.PTOCRI == original

@given(instance=afpText_GSBMX_strategy)
@settings(max_examples=50)
def test_afptext_gsbmx_instantiation(instance):
    assert isinstance(instance, afpText_GSBMX)



@given(instance=afpText_GSBMX_strategy)
def test_afptext_gsbmx_MODE_setter(instance):
    original = instance.MODE
    instance.MODE = original
    assert instance.MODE == original

@given(instance=afpText_ImageEncoding_strategy)
@settings(max_examples=50)
def test_afptext_imageencoding_instantiation(instance):
    assert isinstance(instance, afpText_ImageEncoding)



@given(instance=afpText_ImageEncoding_strategy)
def test_afptext_imageencoding_RECID_setter(instance):
    original = instance.RECID
    instance.RECID = original
    assert instance.RECID == original



@given(instance=afpText_ImageEncoding_strategy)
def test_afptext_imageencoding_COMPRID_setter(instance):
    original = instance.COMPRID
    instance.COMPRID = original
    assert instance.COMPRID == original



@given(instance=afpText_ImageEncoding_strategy)
def test_afptext_imageencoding_BITORDR_setter(instance):
    original = instance.BITORDR
    instance.BITORDR = original
    assert instance.BITORDR == original

@given(instance=afpText_ImageResolution_strategy)
@settings(max_examples=50)
def test_afptext_imageresolution_instantiation(instance):
    assert isinstance(instance, afpText_ImageResolution)



@given(instance=afpText_ImageResolution_strategy)
def test_afptext_imageresolution_YBase_setter(instance):
    original = instance.YBase
    instance.YBase = original
    assert instance.YBase == original



@given(instance=afpText_ImageResolution_strategy)
def test_afptext_imageresolution_XResol_setter(instance):
    original = instance.XResol
    instance.XResol = original
    assert instance.XResol == original



@given(instance=afpText_ImageResolution_strategy)
def test_afptext_imageresolution_YResol_setter(instance):
    original = instance.YResol
    instance.YResol = original
    assert instance.YResol == original



@given(instance=afpText_ImageResolution_strategy)
def test_afptext_imageresolution_XBase_setter(instance):
    original = instance.XBase
    instance.XBase = original
    assert instance.XBase == original

@given(instance=afpText_CharacterRotation_strategy)
@settings(max_examples=50)
def test_afptext_characterrotation_instantiation(instance):
    assert isinstance(instance, afpText_CharacterRotation)



@given(instance=afpText_CharacterRotation_strategy)
def test_afptext_characterrotation_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original

@given(instance=afpText_GCFLT_strategy)
@settings(max_examples=50)
def test_afptext_gcflt_instantiation(instance):
    assert isinstance(instance, afpText_GCFLT)

@given(instance=afpText_ObjectStructuredFieldExtent_strategy)
@settings(max_examples=50)
def test_afptext_objectstructuredfieldextent_instantiation(instance):
    assert isinstance(instance, afpText_ObjectStructuredFieldExtent)



@given(instance=afpText_ObjectStructuredFieldExtent_strategy)
def test_afptext_objectstructuredfieldextent_SFExt_setter(instance):
    original = instance.SFExt
    instance.SFExt = original
    assert instance.SFExt == original



@given(instance=afpText_ObjectStructuredFieldExtent_strategy)
def test_afptext_objectstructuredfieldextent_SFExtHi_setter(instance):
    original = instance.SFExtHi
    instance.SFExtHi = original
    assert instance.SFExtHi == original

@given(instance=afpText_GSMS_strategy)
@settings(max_examples=50)
def test_afptext_gsms_instantiation(instance):
    assert isinstance(instance, afpText_GSMS)



@given(instance=afpText_GSMS_strategy)
def test_afptext_gsms_LCID_setter(instance):
    original = instance.LCID
    instance.LCID = original
    assert instance.LCID == original

@given(instance=afpText_ObjectContainerPresentationSpaceSize_strategy)
@settings(max_examples=50)
def test_afptext_objectcontainerpresentationspacesize_instantiation(instance):
    assert isinstance(instance, afpText_ObjectContainerPresentationSpaceSize)



@given(instance=afpText_ObjectContainerPresentationSpaceSize_strategy)
def test_afptext_objectcontainerpresentationspacesize_PDFSize_setter(instance):
    original = instance.PDFSize
    instance.PDFSize = original
    assert instance.PDFSize == original

@given(instance=afpText_ImageSubsampling_strategy)
@settings(max_examples=50)
def test_afptext_imagesubsampling_instantiation(instance):
    assert isinstance(instance, afpText_ImageSubsampling)

@given(instance=afpText_GPARC_strategy)
@settings(max_examples=50)
def test_afptext_gparc_instantiation(instance):
    assert isinstance(instance, afpText_GPARC)



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_XCENT_setter(instance):
    original = instance.XCENT
    instance.XCENT = original
    assert instance.XCENT == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_SWEEP_setter(instance):
    original = instance.SWEEP
    instance.SWEEP = original
    assert instance.SWEEP == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_YCENT_setter(instance):
    original = instance.YCENT
    instance.YCENT = original
    assert instance.YCENT == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_START_setter(instance):
    original = instance.START
    instance.START = original
    assert instance.START == original



@given(instance=afpText_GPARC_strategy)
def test_afptext_gparc_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_CGCSGID_strategy)
@settings(max_examples=50)
def test_afptext_cgcsgid_instantiation(instance):
    assert isinstance(instance, afpText_CGCSGID)



@given(instance=afpText_CGCSGID_strategy)
def test_afptext_cgcsgid_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original



@given(instance=afpText_CGCSGID_strategy)
def test_afptext_cgcsgid_CPGID_setter(instance):
    original = instance.CPGID
    instance.CPGID = original
    assert instance.CPGID == original

@given(instance=afpText_ColorManagementResourceDescriptor_strategy)
@settings(max_examples=50)
def test_afptext_colormanagementresourcedescriptor_instantiation(instance):
    assert isinstance(instance, afpText_ColorManagementResourceDescriptor)



@given(instance=afpText_ColorManagementResourceDescriptor_strategy)
def test_afptext_colormanagementresourcedescriptor_CMRScpe_setter(instance):
    original = instance.CMRScpe
    instance.CMRScpe = original
    assert instance.CMRScpe == original



@given(instance=afpText_ColorManagementResourceDescriptor_strategy)
def test_afptext_colormanagementresourcedescriptor_ProcMode_setter(instance):
    original = instance.ProcMode
    instance.ProcMode = original
    assert instance.ProcMode == original

@given(instance=afpText_MODCAInterchangeSet_strategy)
@settings(max_examples=50)
def test_afptext_modcainterchangeset_instantiation(instance):
    assert isinstance(instance, afpText_MODCAInterchangeSet)



@given(instance=afpText_MODCAInterchangeSet_strategy)
def test_afptext_modcainterchangeset_IStype_setter(instance):
    original = instance.IStype
    instance.IStype = original
    assert instance.IStype == original



@given(instance=afpText_MODCAInterchangeSet_strategy)
def test_afptext_modcainterchangeset_ISid_setter(instance):
    original = instance.ISid
    instance.ISid = original
    assert instance.ISid == original

@given(instance=afpText_EndSegment_strategy)
@settings(max_examples=50)
def test_afptext_endsegment_instantiation(instance):
    assert isinstance(instance, afpText_EndSegment)

@given(instance=afpText_GFARC_strategy)
@settings(max_examples=50)
def test_afptext_gfarc_instantiation(instance):
    assert isinstance(instance, afpText_GFARC)



@given(instance=afpText_GFARC_strategy)
def test_afptext_gfarc_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GFARC_strategy)
def test_afptext_gfarc_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GFARC_strategy)
def test_afptext_gfarc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original



@given(instance=afpText_GFARC_strategy)
def test_afptext_gfarc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText_TextFidelity_strategy)
@settings(max_examples=50)
def test_afptext_textfidelity_instantiation(instance):
    assert isinstance(instance, afpText_TextFidelity)



@given(instance=afpText_TextFidelity_strategy)
def test_afptext_textfidelity_RepTxtEx_setter(instance):
    original = instance.RepTxtEx
    instance.RepTxtEx = original
    assert instance.RepTxtEx == original



@given(instance=afpText_TextFidelity_strategy)
def test_afptext_textfidelity_StpTxtEx_setter(instance):
    original = instance.StpTxtEx
    instance.StpTxtEx = original
    assert instance.StpTxtEx == original

@given(instance=afpText_IDEStructure_strategy)
@settings(max_examples=50)
def test_afptext_idestructure_instantiation(instance):
    assert isinstance(instance, afpText_IDEStructure)



@given(instance=afpText_IDEStructure_strategy)
def test_afptext_idestructure_FORMAT_setter(instance):
    original = instance.FORMAT
    instance.FORMAT = original
    assert instance.FORMAT == original



@given(instance=afpText_IDEStructure_strategy)
def test_afptext_idestructure_SIZE2_setter(instance):
    original = instance.SIZE2
    instance.SIZE2 = original
    assert instance.SIZE2 == original



@given(instance=afpText_IDEStructure_strategy)
def test_afptext_idestructure_FLAGS_setter(instance):
    original = instance.FLAGS
    instance.FLAGS = original
    assert instance.FLAGS == original



@given(instance=afpText_IDEStructure_strategy)
def test_afptext_idestructure_SIZE4_setter(instance):
    original = instance.SIZE4
    instance.SIZE4 = original
    assert instance.SIZE4 == original



@given(instance=afpText_IDEStructure_strategy)
def test_afptext_idestructure_SIZE1_setter(instance):
    original = instance.SIZE1
    instance.SIZE1 = original
    assert instance.SIZE1 == original



@given(instance=afpText_IDEStructure_strategy)
def test_afptext_idestructure_SIZE3_setter(instance):
    original = instance.SIZE3
    instance.SIZE3 = original
    assert instance.SIZE3 == original

@given(instance=afpText_FNNRG2_strategy)
@settings(max_examples=50)
def test_afptext_fnnrg2_instantiation(instance):
    assert isinstance(instance, afpText_FNNRG2)



@given(instance=afpText_FNNRG2_strategy)
def test_afptext_fnnrg2_TSIDLen_setter(instance):
    original = instance.TSIDLen
    instance.TSIDLen = original
    assert instance.TSIDLen == original



@given(instance=afpText_FNNRG2_strategy)
def test_afptext_fnnrg2_TSID_setter(instance):
    original = instance.TSID
    instance.TSID = original
    assert instance.TSID == original

@given(instance=afpText_BeginTransparencyMask_strategy)
@settings(max_examples=50)
def test_afptext_begintransparencymask_instantiation(instance):
    assert isinstance(instance, afpText_BeginTransparencyMask)

@given(instance=afpText_GSCH_strategy)
@settings(max_examples=50)
def test_afptext_gsch_instantiation(instance):
    assert isinstance(instance, afpText_GSCH)



@given(instance=afpText_GSCH_strategy)
def test_afptext_gsch_HX_setter(instance):
    original = instance.HX
    instance.HX = original
    assert instance.HX == original



@given(instance=afpText_GSCH_strategy)
def test_afptext_gsch_HY_setter(instance):
    original = instance.HY
    instance.HY = original
    assert instance.HY == original

@given(instance=afpText_GSECOL_strategy)
@settings(max_examples=50)
def test_afptext_gsecol_instantiation(instance):
    assert isinstance(instance, afpText_GSECOL)



@given(instance=afpText_GSECOL_strategy)
def test_afptext_gsecol_COLOR_setter(instance):
    original = instance.COLOR
    instance.COLOR = original
    assert instance.COLOR == original

@given(instance=afpText_ResourceUsageAttribute_strategy)
@settings(max_examples=50)
def test_afptext_resourceusageattribute_instantiation(instance):
    assert isinstance(instance, afpText_ResourceUsageAttribute)



@given(instance=afpText_ResourceUsageAttribute_strategy)
def test_afptext_resourceusageattribute_Frequency_setter(instance):
    original = instance.Frequency
    instance.Frequency = original
    assert instance.Frequency == original

@given(instance=afpText_IncludeTile_strategy)
@settings(max_examples=50)
def test_afptext_includetile_instantiation(instance):
    assert isinstance(instance, afpText_IncludeTile)



@given(instance=afpText_IncludeTile_strategy)
def test_afptext_includetile_TIRID_setter(instance):
    original = instance.TIRID
    instance.TIRID = original
    assert instance.TIRID == original

@given(instance=afpText_ObjectStructuredFieldOffset_strategy)
@settings(max_examples=50)
def test_afptext_objectstructuredfieldoffset_instantiation(instance):
    assert isinstance(instance, afpText_ObjectStructuredFieldOffset)



@given(instance=afpText_ObjectStructuredFieldOffset_strategy)
def test_afptext_objectstructuredfieldoffset_SFOffHi_setter(instance):
    original = instance.SFOffHi
    instance.SFOffHi = original
    assert instance.SFOffHi == original



@given(instance=afpText_ObjectStructuredFieldOffset_strategy)
def test_afptext_objectstructuredfieldoffset_SFOff_setter(instance):
    original = instance.SFOff
    instance.SFOff = original
    assert instance.SFOff == original

@given(instance=afpText_ResourceObjectInclude_strategy)
@settings(max_examples=50)
def test_afptext_resourceobjectinclude_instantiation(instance):
    assert isinstance(instance, afpText_ResourceObjectInclude)



@given(instance=afpText_ResourceObjectInclude_strategy)
def test_afptext_resourceobjectinclude_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original



@given(instance=afpText_ResourceObjectInclude_strategy)
def test_afptext_resourceobjectinclude_ObOrent_setter(instance):
    original = instance.ObOrent
    instance.ObOrent = original
    assert instance.ObOrent == original



@given(instance=afpText_ResourceObjectInclude_strategy)
def test_afptext_resourceobjectinclude_XobjOset_setter(instance):
    original = instance.XobjOset
    instance.XobjOset = original
    assert instance.XobjOset == original



@given(instance=afpText_ResourceObjectInclude_strategy)
def test_afptext_resourceobjectinclude_YobjOset_setter(instance):
    original = instance.YobjOset
    instance.YobjOset = original
    assert instance.YobjOset == original



@given(instance=afpText_ResourceObjectInclude_strategy)
def test_afptext_resourceobjectinclude_ObjName_setter(instance):
    original = instance.ObjName
    instance.ObjName = original
    assert instance.ObjName == original

@given(instance=afpText_ResourceObjectType_strategy)
@settings(max_examples=50)
def test_afptext_resourceobjecttype_instantiation(instance):
    assert isinstance(instance, afpText_ResourceObjectType)



@given(instance=afpText_ResourceObjectType_strategy)
def test_afptext_resourceobjecttype_ConData_setter(instance):
    original = instance.ConData
    instance.ConData = original
    assert instance.ConData == original



@given(instance=afpText_ResourceObjectType_strategy)
def test_afptext_resourceobjecttype_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original

@given(instance=afpText_LocalDateAndTimeStamp_strategy)
@settings(max_examples=50)
def test_afptext_localdateandtimestamp_instantiation(instance):
    assert isinstance(instance, afpText_LocalDateAndTimeStamp)



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_TenYear_setter(instance):
    original = instance.TenYear
    instance.TenYear = original
    assert instance.TenYear == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_Day_setter(instance):
    original = instance.Day
    instance.Day = original
    assert instance.Day == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_StampType_setter(instance):
    original = instance.StampType
    instance.StampType = original
    assert instance.StampType == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_HundSec_setter(instance):
    original = instance.HundSec
    instance.HundSec = original
    assert instance.HundSec == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_Hour_setter(instance):
    original = instance.Hour
    instance.Hour = original
    assert instance.Hour == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_Minute_setter(instance):
    original = instance.Minute
    instance.Minute = original
    assert instance.Minute == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_THunYear_setter(instance):
    original = instance.THunYear
    instance.THunYear = original
    assert instance.THunYear == original



@given(instance=afpText_LocalDateAndTimeStamp_strategy)
def test_afptext_localdateandtimestamp_Second_setter(instance):
    original = instance.Second
    instance.Second = original
    assert instance.Second == original

@given(instance=afpText_EndSegmentCommand_strategy)
@settings(max_examples=50)
def test_afptext_endsegmentcommand_instantiation(instance):
    assert isinstance(instance, afpText_EndSegmentCommand)

@given(instance=afpText_GCCHST_strategy)
@settings(max_examples=50)
def test_afptext_gcchst_instantiation(instance):
    assert isinstance(instance, afpText_GCCHST)



@given(instance=afpText_GCCHST_strategy)
def test_afptext_gcchst_CP_setter(instance):
    original = instance.CP
    instance.CP = original
    assert instance.CP == original

@given(instance=afpText_ResourceLocalIdentifier_strategy)
@settings(max_examples=50)
def test_afptext_resourcelocalidentifier_instantiation(instance):
    assert isinstance(instance, afpText_ResourceLocalIdentifier)



@given(instance=afpText_ResourceLocalIdentifier_strategy)
def test_afptext_resourcelocalidentifier_ResType_setter(instance):
    original = instance.ResType
    instance.ResType = original
    assert instance.ResType == original



@given(instance=afpText_ResourceLocalIdentifier_strategy)
def test_afptext_resourcelocalidentifier_ResLID_setter(instance):
    original = instance.ResLID
    instance.ResLID = original
    assert instance.ResLID == original

@given(instance=afpText_GSAP_strategy)
@settings(max_examples=50)
def test_afptext_gsap_instantiation(instance):
    assert isinstance(instance, afpText_GSAP)



@given(instance=afpText_GSAP_strategy)
def test_afptext_gsap_P_setter(instance):
    original = instance.P
    instance.P = original
    assert instance.P == original



@given(instance=afpText_GSAP_strategy)
def test_afptext_gsap_R_setter(instance):
    original = instance.R
    instance.R = original
    assert instance.R == original



@given(instance=afpText_GSAP_strategy)
def test_afptext_gsap_Q_setter(instance):
    original = instance.Q
    instance.Q = original
    assert instance.Q == original



@given(instance=afpText_GSAP_strategy)
def test_afptext_gsap_S_setter(instance):
    original = instance.S
    instance.S = original
    assert instance.S == original

@given(instance=afpText_GBIMG_strategy)
@settings(max_examples=50)
def test_afptext_gbimg_instantiation(instance):
    assert isinstance(instance, afpText_GBIMG)



@given(instance=afpText_GBIMG_strategy)
def test_afptext_gbimg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GBIMG_strategy)
def test_afptext_gbimg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GBIMG_strategy)
def test_afptext_gbimg_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original



@given(instance=afpText_GBIMG_strategy)
def test_afptext_gbimg_FORMAT_setter(instance):
    original = instance.FORMAT
    instance.FORMAT = original
    assert instance.FORMAT == original



@given(instance=afpText_GBIMG_strategy)
def test_afptext_gbimg_WIDTH_setter(instance):
    original = instance.WIDTH
    instance.WIDTH = original
    assert instance.WIDTH == original



@given(instance=afpText_GBIMG_strategy)
def test_afptext_gbimg_HEIGHT_setter(instance):
    original = instance.HEIGHT
    instance.HEIGHT = original
    assert instance.HEIGHT == original

@given(instance=afpText_GCCBEZ_strategy)
@settings(max_examples=50)
def test_afptext_gccbez_instantiation(instance):
    assert isinstance(instance, afpText_GCCBEZ)

@given(instance=afpText_GSMT_strategy)
@settings(max_examples=50)
def test_afptext_gsmt_instantiation(instance):
    assert isinstance(instance, afpText_GSMT)



@given(instance=afpText_GSMT_strategy)
def test_afptext_gsmt_MCPT_setter(instance):
    original = instance.MCPT
    instance.MCPT = original
    assert instance.MCPT == original

@given(instance=afpText_GCFARC_strategy)
@settings(max_examples=50)
def test_afptext_gcfarc_instantiation(instance):
    assert isinstance(instance, afpText_GCFARC)



@given(instance=afpText_GCFARC_strategy)
def test_afptext_gcfarc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original



@given(instance=afpText_GCFARC_strategy)
def test_afptext_gcfarc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original

@given(instance=afpText_GMRK_strategy)
@settings(max_examples=50)
def test_afptext_gmrk_instantiation(instance):
    assert isinstance(instance, afpText_GMRK)

@given(instance=afpText_BeginSegmentCommand_strategy)
@settings(max_examples=50)
def test_afptext_beginsegmentcommand_instantiation(instance):
    assert isinstance(instance, afpText_BeginSegmentCommand)



@given(instance=afpText_BeginSegmentCommand_strategy)
def test_afptext_beginsegmentcommand_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original



@given(instance=afpText_BeginSegmentCommand_strategy)
def test_afptext_beginsegmentcommand_FLAG1_setter(instance):
    original = instance.FLAG1
    instance.FLAG1 = original
    assert instance.FLAG1 == original



@given(instance=afpText_BeginSegmentCommand_strategy)
def test_afptext_beginsegmentcommand_LENGTH_setter(instance):
    original = instance.LENGTH
    instance.LENGTH = original
    assert instance.LENGTH == original



@given(instance=afpText_BeginSegmentCommand_strategy)
def test_afptext_beginsegmentcommand_SEGL_setter(instance):
    original = instance.SEGL
    instance.SEGL = original
    assert instance.SEGL == original



@given(instance=afpText_BeginSegmentCommand_strategy)
def test_afptext_beginsegmentcommand_FLAG2_setter(instance):
    original = instance.FLAG2
    instance.FLAG2 = original
    assert instance.FLAG2 == original



@given(instance=afpText_BeginSegmentCommand_strategy)
def test_afptext_beginsegmentcommand_PSNAME_setter(instance):
    original = instance.PSNAME
    instance.PSNAME = original
    assert instance.PSNAME == original

@given(instance=afpText_FullyQualifiedName_strategy)
@settings(max_examples=50)
def test_afptext_fullyqualifiedname_instantiation(instance):
    assert isinstance(instance, afpText_FullyQualifiedName)



@given(instance=afpText_FullyQualifiedName_strategy)
def test_afptext_fullyqualifiedname_FQName_setter(instance):
    original = instance.FQName
    instance.FQName = original
    assert instance.FQName == original



@given(instance=afpText_FullyQualifiedName_strategy)
def test_afptext_fullyqualifiedname_FQNFormat_setter(instance):
    original = instance.FQNFormat
    instance.FQNFormat = original
    assert instance.FQNFormat == original



@given(instance=afpText_FullyQualifiedName_strategy)
def test_afptext_fullyqualifiedname_FQNType_setter(instance):
    original = instance.FQNType
    instance.FQNType = original
    assert instance.FQNType == original

@given(instance=afpText_SamplingRatios_strategy)
@settings(max_examples=50)
def test_afptext_samplingratios_instantiation(instance):
    assert isinstance(instance, afpText_SamplingRatios)

@given(instance=afpText_MetricAdjustment_strategy)
@settings(max_examples=50)
def test_afptext_metricadjustment_instantiation(instance):
    assert isinstance(instance, afpText_MetricAdjustment)



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_YUPUB_setter(instance):
    original = instance.YUPUB
    instance.YUPUB = original
    assert instance.YUPUB == original



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_HBaselineIncrement_setter(instance):
    original = instance.HBaselineIncrement
    instance.HBaselineIncrement = original
    assert instance.HBaselineIncrement == original



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_XUPUB_setter(instance):
    original = instance.XUPUB
    instance.XUPUB = original
    assert instance.XUPUB == original



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_HUniformIncrement_setter(instance):
    original = instance.HUniformIncrement
    instance.HUniformIncrement = original
    assert instance.HUniformIncrement == original



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_UnitBase_setter(instance):
    original = instance.UnitBase
    instance.UnitBase = original
    assert instance.UnitBase == original



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_VBaselineIncrement_setter(instance):
    original = instance.VBaselineIncrement
    instance.VBaselineIncrement = original
    assert instance.VBaselineIncrement == original



@given(instance=afpText_MetricAdjustment_strategy)
def test_afptext_metricadjustment_VUniformIncrement_setter(instance):
    original = instance.VUniformIncrement
    instance.VUniformIncrement = original
    assert instance.VUniformIncrement == original

@given(instance=afpText_DataObjectFontDescriptor_strategy)
@settings(max_examples=50)
def test_afptext_dataobjectfontdescriptor_instantiation(instance):
    assert isinstance(instance, afpText_DataObjectFontDescriptor)



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_EncEnv_setter(instance):
    original = instance.EncEnv
    instance.EncEnv = original
    assert instance.EncEnv == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_VFS_setter(instance):
    original = instance.VFS
    instance.VFS = original
    assert instance.VFS == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_DOFtFlgs_setter(instance):
    original = instance.DOFtFlgs
    instance.DOFtFlgs = original
    assert instance.DOFtFlgs == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_FontTech_setter(instance):
    original = instance.FontTech
    instance.FontTech = original
    assert instance.FontTech == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_HFS_setter(instance):
    original = instance.HFS
    instance.HFS = original
    assert instance.HFS == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_EncID_setter(instance):
    original = instance.EncID
    instance.EncID = original
    assert instance.EncID == original



@given(instance=afpText_DataObjectFontDescriptor_strategy)
def test_afptext_dataobjectfontdescriptor_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_MediumMapPageNumber_strategy)
@settings(max_examples=50)
def test_afptext_mediummappagenumber_instantiation(instance):
    assert isinstance(instance, afpText_MediumMapPageNumber)



@given(instance=afpText_MediumMapPageNumber_strategy)
def test_afptext_mediummappagenumber_PageNum_setter(instance):
    original = instance.PageNum
    instance.PageNum = original
    assert instance.PageNum == original

@given(instance=afpText_GEIMG_strategy)
@settings(max_examples=50)
def test_afptext_geimg_instantiation(instance):
    assert isinstance(instance, afpText_GEIMG)



@given(instance=afpText_GEIMG_strategy)
def test_afptext_geimg_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText_GSFLW_strategy)
@settings(max_examples=50)
def test_afptext_gsflw_instantiation(instance):
    assert isinstance(instance, afpText_GSFLW)



@given(instance=afpText_GSFLW_strategy)
def test_afptext_gsflw_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original



@given(instance=afpText_GSFLW_strategy)
def test_afptext_gsflw_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText_GNOP1_strategy)
@settings(max_examples=50)
def test_afptext_gnop1_instantiation(instance):
    assert isinstance(instance, afpText_GNOP1)

@given(instance=afpText_GCLINE_strategy)
@settings(max_examples=50)
def test_afptext_gcline_instantiation(instance):
    assert isinstance(instance, afpText_GCLINE)

@given(instance=afpText_LocaleSelector_strategy)
@settings(max_examples=50)
def test_afptext_localeselector_instantiation(instance):
    assert isinstance(instance, afpText_LocaleSelector)



@given(instance=afpText_LocaleSelector_strategy)
def test_afptext_localeselector_LocFlgs_setter(instance):
    original = instance.LocFlgs
    instance.LocFlgs = original
    assert instance.LocFlgs == original



@given(instance=afpText_LocaleSelector_strategy)
def test_afptext_localeselector_LangCode_setter(instance):
    original = instance.LangCode
    instance.LangCode = original
    assert instance.LangCode == original



@given(instance=afpText_LocaleSelector_strategy)
def test_afptext_localeselector_ScrptCde_setter(instance):
    original = instance.ScrptCde
    instance.ScrptCde = original
    assert instance.ScrptCde == original



@given(instance=afpText_LocaleSelector_strategy)
def test_afptext_localeselector_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_LocaleSelector_strategy)
def test_afptext_localeselector_VarCde_setter(instance):
    original = instance.VarCde
    instance.VarCde = original
    assert instance.VarCde == original



@given(instance=afpText_LocaleSelector_strategy)
def test_afptext_localeselector_RegCde_setter(instance):
    original = instance.RegCde
    instance.RegCde = original
    assert instance.RegCde == original

@given(instance=afpText_MediaEjectControl_strategy)
@settings(max_examples=50)
def test_afptext_mediaejectcontrol_instantiation(instance):
    assert isinstance(instance, afpText_MediaEjectControl)



@given(instance=afpText_MediaEjectControl_strategy)
def test_afptext_mediaejectcontrol_EjCtrl_setter(instance):
    original = instance.EjCtrl
    instance.EjCtrl = original
    assert instance.EjCtrl == original



@given(instance=afpText_MediaEjectControl_strategy)
def test_afptext_mediaejectcontrol_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_GEAR_strategy)
@settings(max_examples=50)
def test_afptext_gear_instantiation(instance):
    assert isinstance(instance, afpText_GEAR)



@given(instance=afpText_GEAR_strategy)
def test_afptext_gear_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText_MeasurementUnits_strategy)
@settings(max_examples=50)
def test_afptext_measurementunits_instantiation(instance):
    assert isinstance(instance, afpText_MeasurementUnits)



@given(instance=afpText_MeasurementUnits_strategy)
def test_afptext_measurementunits_YoaBase_setter(instance):
    original = instance.YoaBase
    instance.YoaBase = original
    assert instance.YoaBase == original



@given(instance=afpText_MeasurementUnits_strategy)
def test_afptext_measurementunits_XoaUnits_setter(instance):
    original = instance.XoaUnits
    instance.XoaUnits = original
    assert instance.XoaUnits == original



@given(instance=afpText_MeasurementUnits_strategy)
def test_afptext_measurementunits_YoaUnits_setter(instance):
    original = instance.YoaUnits
    instance.YoaUnits = original
    assert instance.YoaUnits == original



@given(instance=afpText_MeasurementUnits_strategy)
def test_afptext_measurementunits_XoaBase_setter(instance):
    original = instance.XoaBase
    instance.XoaBase = original
    assert instance.XoaBase == original

@given(instance=afpText_DrawingOrderSubset_strategy)
@settings(max_examples=50)
def test_afptext_drawingordersubset_instantiation(instance):
    assert isinstance(instance, afpText_DrawingOrderSubset)

@given(instance=afpText_ObjectByteOffset_strategy)
@settings(max_examples=50)
def test_afptext_objectbyteoffset_instantiation(instance):
    assert isinstance(instance, afpText_ObjectByteOffset)



@given(instance=afpText_ObjectByteOffset_strategy)
def test_afptext_objectbyteoffset_DirByOff_setter(instance):
    original = instance.DirByOff
    instance.DirByOff = original
    assert instance.DirByOff == original



@given(instance=afpText_ObjectByteOffset_strategy)
def test_afptext_objectbyteoffset_DirByHi_setter(instance):
    original = instance.DirByHi
    instance.DirByHi = original
    assert instance.DirByHi == original

@given(instance=afpText_GSCA_strategy)
@settings(max_examples=50)
def test_afptext_gsca_instantiation(instance):
    assert isinstance(instance, afpText_GSCA)



@given(instance=afpText_GSCA_strategy)
def test_afptext_gsca_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GSCA_strategy)
def test_afptext_gsca_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_GCBOX_strategy)
@settings(max_examples=50)
def test_afptext_gcbox_instantiation(instance):
    assert isinstance(instance, afpText_GCBOX)



@given(instance=afpText_GCBOX_strategy)
def test_afptext_gcbox_XPOS1_setter(instance):
    original = instance.XPOS1
    instance.XPOS1 = original
    assert instance.XPOS1 == original



@given(instance=afpText_GCBOX_strategy)
def test_afptext_gcbox_YPOS1_setter(instance):
    original = instance.YPOS1
    instance.YPOS1 = original
    assert instance.YPOS1 == original



@given(instance=afpText_GCBOX_strategy)
def test_afptext_gcbox_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original



@given(instance=afpText_GCBOX_strategy)
def test_afptext_gcbox_VAXIS_setter(instance):
    original = instance.VAXIS
    instance.VAXIS = original
    assert instance.VAXIS == original



@given(instance=afpText_GCBOX_strategy)
def test_afptext_gcbox_HAXIS_setter(instance):
    original = instance.HAXIS
    instance.HAXIS = original
    assert instance.HAXIS == original

@given(instance=afpText_ExtensionFont_strategy)
@settings(max_examples=50)
def test_afptext_extensionfont_instantiation(instance):
    assert isinstance(instance, afpText_ExtensionFont)



@given(instance=afpText_ExtensionFont_strategy)
def test_afptext_extensionfont_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText_PresentationSpaceResetMixing_strategy)
@settings(max_examples=50)
def test_afptext_presentationspaceresetmixing_instantiation(instance):
    assert isinstance(instance, afpText_PresentationSpaceResetMixing)



@given(instance=afpText_PresentationSpaceResetMixing_strategy)
def test_afptext_presentationspaceresetmixing_BgMxFlag_setter(instance):
    original = instance.BgMxFlag
    instance.BgMxFlag = original
    assert instance.BgMxFlag == original

@given(instance=afpText_TilePosition_strategy)
@settings(max_examples=50)
def test_afptext_tileposition_instantiation(instance):
    assert isinstance(instance, afpText_TilePosition)



@given(instance=afpText_TilePosition_strategy)
def test_afptext_tileposition_XOFFSET_setter(instance):
    original = instance.XOFFSET
    instance.XOFFSET = original
    assert instance.XOFFSET == original



@given(instance=afpText_TilePosition_strategy)
def test_afptext_tileposition_YOFFSET_setter(instance):
    original = instance.YOFFSET
    instance.YOFFSET = original
    assert instance.YOFFSET == original

@given(instance=afpText_GLINE_strategy)
@settings(max_examples=50)
def test_afptext_gline_instantiation(instance):
    assert isinstance(instance, afpText_GLINE)

@given(instance=afpText_GSMC_strategy)
@settings(max_examples=50)
def test_afptext_gsmc_instantiation(instance):
    assert isinstance(instance, afpText_GSMC)



@given(instance=afpText_GSMC_strategy)
def test_afptext_gsmc_CELLWI_setter(instance):
    original = instance.CELLWI
    instance.CELLWI = original
    assert instance.CELLWI == original



@given(instance=afpText_GSMC_strategy)
def test_afptext_gsmc_CELLHI_setter(instance):
    original = instance.CELLHI
    instance.CELLHI = original
    assert instance.CELLHI == original

@given(instance=afpText_PageOverlayConditionalProcessing_strategy)
@settings(max_examples=50)
def test_afptext_pageoverlayconditionalprocessing_instantiation(instance):
    assert isinstance(instance, afpText_PageOverlayConditionalProcessing)



@given(instance=afpText_PageOverlayConditionalProcessing_strategy)
def test_afptext_pageoverlayconditionalprocessing_PgOvType_setter(instance):
    original = instance.PgOvType
    instance.PgOvType = original
    assert instance.PgOvType == original



@given(instance=afpText_PageOverlayConditionalProcessing_strategy)
def test_afptext_pageoverlayconditionalprocessing_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original

@given(instance=afpText_CMRFidelity_strategy)
@settings(max_examples=50)
def test_afptext_cmrfidelity_instantiation(instance):
    assert isinstance(instance, afpText_CMRFidelity)



@given(instance=afpText_CMRFidelity_strategy)
def test_afptext_cmrfidelity_RepCMREx_setter(instance):
    original = instance.RepCMREx
    instance.RepCMREx = original
    assert instance.RepCMREx == original



@given(instance=afpText_CMRFidelity_strategy)
def test_afptext_cmrfidelity_StpCMREx_setter(instance):
    original = instance.StpCMREx
    instance.StpCMREx = original
    assert instance.StpCMREx == original

@given(instance=afpText_GBAR_strategy)
@settings(max_examples=50)
def test_afptext_gbar_instantiation(instance):
    assert isinstance(instance, afpText_GBAR)



@given(instance=afpText_GBAR_strategy)
def test_afptext_gbar_FLAGS_setter(instance):
    original = instance.FLAGS
    instance.FLAGS = original
    assert instance.FLAGS == original

@given(instance=afpText_GIMD_strategy)
@settings(max_examples=50)
def test_afptext_gimd_instantiation(instance):
    assert isinstance(instance, afpText_GIMD)



@given(instance=afpText_GIMD_strategy)
def test_afptext_gimd_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText_TileTOC_strategy)
@settings(max_examples=50)
def test_afptext_tiletoc_instantiation(instance):
    assert isinstance(instance, afpText_TileTOC)



@given(instance=afpText_TileTOC_strategy)
def test_afptext_tiletoc_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_CRCResourceManagement_strategy)
@settings(max_examples=50)
def test_afptext_crcresourcemanagement_instantiation(instance):
    assert isinstance(instance, afpText_CRCResourceManagement)



@given(instance=afpText_CRCResourceManagement_strategy)
def test_afptext_crcresourcemanagement_ResClassFlg_setter(instance):
    original = instance.ResClassFlg
    instance.ResClassFlg = original
    assert instance.ResClassFlg == original



@given(instance=afpText_CRCResourceManagement_strategy)
def test_afptext_crcresourcemanagement_RMValue_setter(instance):
    original = instance.RMValue
    instance.RMValue = original
    assert instance.RMValue == original



@given(instance=afpText_CRCResourceManagement_strategy)
def test_afptext_crcresourcemanagement_FmtQual_setter(instance):
    original = instance.FmtQual
    instance.FmtQual = original
    assert instance.FmtQual == original

@given(instance=afpText_GSCC_strategy)
@settings(max_examples=50)
def test_afptext_gscc_instantiation(instance):
    assert isinstance(instance, afpText_GSCC)



@given(instance=afpText_GSCC_strategy)
def test_afptext_gscc_CELLHFR_setter(instance):
    original = instance.CELLHFR
    instance.CELLHFR = original
    assert instance.CELLHFR == original



@given(instance=afpText_GSCC_strategy)
def test_afptext_gscc_CELLHI_setter(instance):
    original = instance.CELLHI
    instance.CELLHI = original
    assert instance.CELLHI == original



@given(instance=afpText_GSCC_strategy)
def test_afptext_gscc_CELLWI_setter(instance):
    original = instance.CELLWI
    instance.CELLWI = original
    assert instance.CELLWI == original



@given(instance=afpText_GSCC_strategy)
def test_afptext_gscc_CELLWFR_setter(instance):
    original = instance.CELLWFR
    instance.CELLWFR = original
    assert instance.CELLWFR == original

@given(instance=afpText_ObjectByteExtent_strategy)
@settings(max_examples=50)
def test_afptext_objectbyteextent_instantiation(instance):
    assert isinstance(instance, afpText_ObjectByteExtent)



@given(instance=afpText_ObjectByteExtent_strategy)
def test_afptext_objectbyteextent_ByteExt_setter(instance):
    original = instance.ByteExt
    instance.ByteExt = original
    assert instance.ByteExt == original



@given(instance=afpText_ObjectByteExtent_strategy)
def test_afptext_objectbyteextent_ByteExtHi_setter(instance):
    original = instance.ByteExtHi
    instance.ByteExtHi = original
    assert instance.ByteExtHi == original

@given(instance=afpText_ObjectFunctionSetSpecification_strategy)
@settings(max_examples=50)
def test_afptext_objectfunctionsetspecification_instantiation(instance):
    assert isinstance(instance, afpText_ObjectFunctionSetSpecification)



@given(instance=afpText_ObjectFunctionSetSpecification_strategy)
def test_afptext_objectfunctionsetspecification_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original



@given(instance=afpText_ObjectFunctionSetSpecification_strategy)
def test_afptext_objectfunctionsetspecification_DCAFnSet_setter(instance):
    original = instance.DCAFnSet
    instance.DCAFnSet = original
    assert instance.DCAFnSet == original



@given(instance=afpText_ObjectFunctionSetSpecification_strategy)
def test_afptext_objectfunctionsetspecification_OCAFnSet_setter(instance):
    original = instance.OCAFnSet
    instance.OCAFnSet = original
    assert instance.OCAFnSet == original



@given(instance=afpText_ObjectFunctionSetSpecification_strategy)
def test_afptext_objectfunctionsetspecification_ArchVrsn_setter(instance):
    original = instance.ArchVrsn
    instance.ArchVrsn = original
    assert instance.ArchVrsn == original

@given(instance=afpText_GCBIMG_strategy)
@settings(max_examples=50)
def test_afptext_gcbimg_instantiation(instance):
    assert isinstance(instance, afpText_GCBIMG)



@given(instance=afpText_GCBIMG_strategy)
def test_afptext_gcbimg_FORMAT_setter(instance):
    original = instance.FORMAT
    instance.FORMAT = original
    assert instance.FORMAT == original



@given(instance=afpText_GCBIMG_strategy)
def test_afptext_gcbimg_HEIGHT_setter(instance):
    original = instance.HEIGHT
    instance.HEIGHT = original
    assert instance.HEIGHT == original



@given(instance=afpText_GCBIMG_strategy)
def test_afptext_gcbimg_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original



@given(instance=afpText_GCBIMG_strategy)
def test_afptext_gcbimg_WIDTH_setter(instance):
    original = instance.WIDTH
    instance.WIDTH = original
    assert instance.WIDTH == original

@given(instance=afpText_GEPROL_strategy)
@settings(max_examples=50)
def test_afptext_geprol_instantiation(instance):
    assert isinstance(instance, afpText_GEPROL)



@given(instance=afpText_GEPROL_strategy)
def test_afptext_geprol_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText_MediaFidelity_strategy)
@settings(max_examples=50)
def test_afptext_mediafidelity_instantiation(instance):
    assert isinstance(instance, afpText_MediaFidelity)



@given(instance=afpText_MediaFidelity_strategy)
def test_afptext_mediafidelity_StpMedEx_setter(instance):
    original = instance.StpMedEx
    instance.StpMedEx = original
    assert instance.StpMedEx == original



@given(instance=afpText_MediaFidelity_strategy)
def test_afptext_mediafidelity_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_FinishingFidelity_strategy)
@settings(max_examples=50)
def test_afptext_finishingfidelity_instantiation(instance):
    assert isinstance(instance, afpText_FinishingFidelity)



@given(instance=afpText_FinishingFidelity_strategy)
def test_afptext_finishingfidelity_StpFinEx_setter(instance):
    original = instance.StpFinEx
    instance.StpFinEx = original
    assert instance.StpFinEx == original



@given(instance=afpText_FinishingFidelity_strategy)
def test_afptext_finishingfidelity_RepFinEx_setter(instance):
    original = instance.RepFinEx
    instance.RepFinEx = original
    assert instance.RepFinEx == original

@given(instance=afpText_ImageLUTID_strategy)
@settings(max_examples=50)
def test_afptext_imagelutid_instantiation(instance):
    assert isinstance(instance, afpText_ImageLUTID)



@given(instance=afpText_ImageLUTID_strategy)
def test_afptext_imagelutid_LUTID_setter(instance):
    original = instance.LUTID
    instance.LUTID = original
    assert instance.LUTID == original

@given(instance=afpText_GSCOL_strategy)
@settings(max_examples=50)
def test_afptext_gscol_instantiation(instance):
    assert isinstance(instance, afpText_GSCOL)



@given(instance=afpText_GSCOL_strategy)
def test_afptext_gscol_COL_setter(instance):
    original = instance.COL
    instance.COL = original
    assert instance.COL == original

@given(instance=afpText_AMI_strategy)
@settings(max_examples=50)
def test_afptext_ami_instantiation(instance):
    assert isinstance(instance, afpText_AMI)



@given(instance=afpText_AMI_strategy)
def test_afptext_ami_DSPLCMNT_setter(instance):
    original = instance.DSPLCMNT
    instance.DSPLCMNT = original
    assert instance.DSPLCMNT == original

@given(instance=afpText_Comment_strategy)
@settings(max_examples=50)
def test_afptext_comment_instantiation(instance):
    assert isinstance(instance, afpText_Comment)



@given(instance=afpText_Comment_strategy)
def test_afptext_comment_Comment_setter(instance):
    original = instance.Comment
    instance.Comment = original
    assert instance.Comment == original

@given(instance=afpText_WindowSpecification_strategy)
@settings(max_examples=50)
def test_afptext_windowspecification_instantiation(instance):
    assert isinstance(instance, afpText_WindowSpecification)



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_RES3_setter(instance):
    original = instance.RES3
    instance.RES3 = original
    assert instance.RES3 == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_CFORMAT_setter(instance):
    original = instance.CFORMAT
    instance.CFORMAT = original
    assert instance.CFORMAT == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_IMGXYRES_setter(instance):
    original = instance.IMGXYRES
    instance.IMGXYRES = original
    assert instance.IMGXYRES == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_XRWIND_setter(instance):
    original = instance.XRWIND
    instance.XRWIND = original
    assert instance.XRWIND == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_FLAGS_setter(instance):
    original = instance.FLAGS
    instance.FLAGS = original
    assert instance.FLAGS == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_YRESOL_setter(instance):
    original = instance.YRESOL
    instance.YRESOL = original
    assert instance.YRESOL == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_UBASE_setter(instance):
    original = instance.UBASE
    instance.UBASE = original
    assert instance.UBASE == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_XLWIND_setter(instance):
    original = instance.XLWIND
    instance.XLWIND = original
    assert instance.XLWIND == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_XRESOL_setter(instance):
    original = instance.XRESOL
    instance.XRESOL = original
    assert instance.XRESOL == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_YTWIND_setter(instance):
    original = instance.YTWIND
    instance.YTWIND = original
    assert instance.YTWIND == original



@given(instance=afpText_WindowSpecification_strategy)
def test_afptext_windowspecification_YBWIND_setter(instance):
    original = instance.YBWIND
    instance.YBWIND = original
    assert instance.YBWIND == original

@given(instance=afpText_FontResolution_strategy)
@settings(max_examples=50)
def test_afptext_fontresolution_instantiation(instance):
    assert isinstance(instance, afpText_FontResolution)



@given(instance=afpText_FontResolution_strategy)
def test_afptext_fontresolution_RPuBase_setter(instance):
    original = instance.RPuBase
    instance.RPuBase = original
    assert instance.RPuBase == original



@given(instance=afpText_FontResolution_strategy)
def test_afptext_fontresolution_RPUnits_setter(instance):
    original = instance.RPUnits
    instance.RPUnits = original
    assert instance.RPUnits == original



@given(instance=afpText_FontResolution_strategy)
def test_afptext_fontresolution_MetTech_setter(instance):
    original = instance.MetTech
    instance.MetTech = original
    assert instance.MetTech == original

@given(instance=afpText_TextOrientation_strategy)
@settings(max_examples=50)
def test_afptext_textorientation_instantiation(instance):
    assert isinstance(instance, afpText_TextOrientation)



@given(instance=afpText_TextOrientation_strategy)
def test_afptext_textorientation_BAxis_setter(instance):
    original = instance.BAxis
    instance.BAxis = original
    assert instance.BAxis == original



@given(instance=afpText_TextOrientation_strategy)
def test_afptext_textorientation_IAxis_setter(instance):
    original = instance.IAxis
    instance.IAxis = original
    assert instance.IAxis == original

@given(instance=afpText_UP3iFinishingOperation_strategy)
@settings(max_examples=50)
def test_afptext_up3ifinishingoperation_instantiation(instance):
    assert isinstance(instance, afpText_UP3iFinishingOperation)



@given(instance=afpText_UP3iFinishingOperation_strategy)
def test_afptext_up3ifinishingoperation_UP3iDat_setter(instance):
    original = instance.UP3iDat
    instance.UP3iDat = original
    assert instance.UP3iDat == original



@given(instance=afpText_UP3iFinishingOperation_strategy)
def test_afptext_up3ifinishingoperation_Seqnum_setter(instance):
    original = instance.Seqnum
    instance.Seqnum = original
    assert instance.Seqnum == original

@given(instance=afpText_BeginSegment_strategy)
@settings(max_examples=50)
def test_afptext_beginsegment_instantiation(instance):
    assert isinstance(instance, afpText_BeginSegment)



@given(instance=afpText_BeginSegment_strategy)
def test_afptext_beginsegment_SEGNAME_setter(instance):
    original = instance.SEGNAME
    instance.SEGNAME = original
    assert instance.SEGNAME == original

@given(instance=afpText_EndTile_strategy)
@settings(max_examples=50)
def test_afptext_endtile_instantiation(instance):
    assert isinstance(instance, afpText_EndTile)

@given(instance=afpText_PresentationSpaceMixingRules_strategy)
@settings(max_examples=50)
def test_afptext_presentationspacemixingrules_instantiation(instance):
    assert isinstance(instance, afpText_PresentationSpaceMixingRules)

@given(instance=afpText_AttributeQualifier_strategy)
@settings(max_examples=50)
def test_afptext_attributequalifier_instantiation(instance):
    assert isinstance(instance, afpText_AttributeQualifier)



@given(instance=afpText_AttributeQualifier_strategy)
def test_afptext_attributequalifier_SeqNum_setter(instance):
    original = instance.SeqNum
    instance.SeqNum = original
    assert instance.SeqNum == original



@given(instance=afpText_AttributeQualifier_strategy)
def test_afptext_attributequalifier_LevNum_setter(instance):
    original = instance.LevNum
    instance.LevNum = original
    assert instance.LevNum == original

@given(instance=afpText_TRN_strategy)
@settings(max_examples=50)
def test_afptext_trn_instantiation(instance):
    assert isinstance(instance, afpText_TRN)



@given(instance=afpText_TRN_strategy)
def test_afptext_trn_TRNDATA_setter(instance):
    original = instance.TRNDATA
    instance.TRNDATA = original
    assert instance.TRNDATA == original

@given(instance=afpText_GSLE_strategy)
@settings(max_examples=50)
def test_afptext_gsle_instantiation(instance):
    assert isinstance(instance, afpText_GSLE)



@given(instance=afpText_GSLE_strategy)
def test_afptext_gsle_LINEEND_setter(instance):
    original = instance.LINEEND
    instance.LINEEND = original
    assert instance.LINEEND == original

@given(instance=afpText_BSU_strategy)
@settings(max_examples=50)
def test_afptext_bsu_instantiation(instance):
    assert isinstance(instance, afpText_BSU)



@given(instance=afpText_BSU_strategy)
def test_afptext_bsu_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText_FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
@settings(max_examples=50)
def test_afptext_fontcodedgraphiccharactersetglobalidentifier_instantiation(instance):
    assert isinstance(instance, afpText_FontCodedGraphicCharacterSetGlobalIdentifier)



@given(instance=afpText_FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
def test_afptext_fontcodedgraphiccharactersetglobalidentifier_CPGID_setter(instance):
    original = instance.CPGID
    instance.CPGID = original
    assert instance.CPGID == original



@given(instance=afpText_FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
def test_afptext_fontcodedgraphiccharactersetglobalidentifier_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText_GCOMT_strategy)
@settings(max_examples=50)
def test_afptext_gcomt_instantiation(instance):
    assert isinstance(instance, afpText_GCOMT)



@given(instance=afpText_GCOMT_strategy)
def test_afptext_gcomt_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText_BeginTile_strategy)
@settings(max_examples=50)
def test_afptext_begintile_instantiation(instance):
    assert isinstance(instance, afpText_BeginTile)

@given(instance=afpText_USC_strategy)
@settings(max_examples=50)
def test_afptext_usc_instantiation(instance):
    assert isinstance(instance, afpText_USC)



@given(instance=afpText_USC_strategy)
def test_afptext_usc_BYPSIDEN_setter(instance):
    original = instance.BYPSIDEN
    instance.BYPSIDEN = original
    assert instance.BYPSIDEN == original

@given(instance=afpText_PresentationControl_strategy)
@settings(max_examples=50)
def test_afptext_presentationcontrol_instantiation(instance):
    assert isinstance(instance, afpText_PresentationControl)



@given(instance=afpText_PresentationControl_strategy)
def test_afptext_presentationcontrol_PRSFlg_setter(instance):
    original = instance.PRSFlg
    instance.PRSFlg = original
    assert instance.PRSFlg == original

@given(instance=afpText_DescriptorPosition_strategy)
@settings(max_examples=50)
def test_afptext_descriptorposition_instantiation(instance):
    assert isinstance(instance, afpText_DescriptorPosition)



@given(instance=afpText_DescriptorPosition_strategy)
def test_afptext_descriptorposition_DesPosID_setter(instance):
    original = instance.DesPosID
    instance.DesPosID = original
    assert instance.DesPosID == original

@given(instance=afpText_TileSetColor_strategy)
@settings(max_examples=50)
def test_afptext_tilesetcolor_instantiation(instance):
    assert isinstance(instance, afpText_TileSetColor)



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_SIZE3_setter(instance):
    original = instance.SIZE3
    instance.SIZE3 = original
    assert instance.SIZE3 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_SIZE2_setter(instance):
    original = instance.SIZE2
    instance.SIZE2 = original
    assert instance.SIZE2 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_CVAL3_setter(instance):
    original = instance.CVAL3
    instance.CVAL3 = original
    assert instance.CVAL3 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_CVAL1_setter(instance):
    original = instance.CVAL1
    instance.CVAL1 = original
    assert instance.CVAL1 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_SIZE1_setter(instance):
    original = instance.SIZE1
    instance.SIZE1 = original
    assert instance.SIZE1 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_CSPACE_setter(instance):
    original = instance.CSPACE
    instance.CSPACE = original
    assert instance.CSPACE == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_SIZE4_setter(instance):
    original = instance.SIZE4
    instance.SIZE4 = original
    assert instance.SIZE4 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_CVAL2_setter(instance):
    original = instance.CVAL2
    instance.CVAL2 = original
    assert instance.CVAL2 == original



@given(instance=afpText_TileSetColor_strategy)
def test_afptext_tilesetcolor_CVAL4_setter(instance):
    original = instance.CVAL4
    instance.CVAL4 = original
    assert instance.CVAL4 == original

@given(instance=afpText_GSLJ_strategy)
@settings(max_examples=50)
def test_afptext_gslj_instantiation(instance):
    assert isinstance(instance, afpText_GSLJ)



@given(instance=afpText_GSLJ_strategy)
def test_afptext_gslj_LINEJOIN_setter(instance):
    original = instance.LINEJOIN
    instance.LINEJOIN = original
    assert instance.LINEJOIN == original

@given(instance=afpText_IOCAFunctionSetIdentification_strategy)
@settings(max_examples=50)
def test_afptext_iocafunctionsetidentification_instantiation(instance):
    assert isinstance(instance, afpText_IOCAFunctionSetIdentification)



@given(instance=afpText_IOCAFunctionSetIdentification_strategy)
def test_afptext_iocafunctionsetidentification_CATEGORY_setter(instance):
    original = instance.CATEGORY
    instance.CATEGORY = original
    assert instance.CATEGORY == original



@given(instance=afpText_IOCAFunctionSetIdentification_strategy)
def test_afptext_iocafunctionsetidentification_FCNSET_setter(instance):
    original = instance.FCNSET
    instance.FCNSET = original
    assert instance.FCNSET == original

@given(instance=afpText_GBOX_strategy)
@settings(max_examples=50)
def test_afptext_gbox_instantiation(instance):
    assert isinstance(instance, afpText_GBOX)



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_XPOS1_setter(instance):
    original = instance.XPOS1
    instance.XPOS1 = original
    assert instance.XPOS1 == original



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_XPOS0_setter(instance):
    original = instance.XPOS0
    instance.XPOS0 = original
    assert instance.XPOS0 == original



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_HAXIS_setter(instance):
    original = instance.HAXIS
    instance.HAXIS = original
    assert instance.HAXIS == original



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_YPOS0_setter(instance):
    original = instance.YPOS0
    instance.YPOS0 = original
    assert instance.YPOS0 == original



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_YPOS1_setter(instance):
    original = instance.YPOS1
    instance.YPOS1 = original
    assert instance.YPOS1 == original



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_VAXIS_setter(instance):
    original = instance.VAXIS
    instance.VAXIS = original
    assert instance.VAXIS == original



@given(instance=afpText_GBOX_strategy)
def test_afptext_gbox_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText_ColorFidelity_strategy)
@settings(max_examples=50)
def test_afptext_colorfidelity_instantiation(instance):
    assert isinstance(instance, afpText_ColorFidelity)



@given(instance=afpText_ColorFidelity_strategy)
def test_afptext_colorfidelity_RepCoEx_setter(instance):
    original = instance.RepCoEx
    instance.RepCoEx = original
    assert instance.RepCoEx == original



@given(instance=afpText_ColorFidelity_strategy)
def test_afptext_colorfidelity_StpCoEx_setter(instance):
    original = instance.StpCoEx
    instance.StpCoEx = original
    assert instance.StpCoEx == original



@given(instance=afpText_ColorFidelity_strategy)
def test_afptext_colorfidelity_ColSub_setter(instance):
    original = instance.ColSub
    instance.ColSub = original
    assert instance.ColSub == original

@given(instance=afpText_GSLW_strategy)
@settings(max_examples=50)
def test_afptext_gslw_instantiation(instance):
    assert isinstance(instance, afpText_GSLW)



@given(instance=afpText_GSLW_strategy)
def test_afptext_gslw_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText_GSMX_strategy)
@settings(max_examples=50)
def test_afptext_gsmx_instantiation(instance):
    assert isinstance(instance, afpText_GSMX)



@given(instance=afpText_GSMX_strategy)
def test_afptext_gsmx_MODE_setter(instance):
    original = instance.MODE
    instance.MODE = original
    assert instance.MODE == original

@given(instance=afpText_GCHST_strategy)
@settings(max_examples=50)
def test_afptext_gchst_instantiation(instance):
    assert isinstance(instance, afpText_GCHST)



@given(instance=afpText_GCHST_strategy)
def test_afptext_gchst_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GCHST_strategy)
def test_afptext_gchst_CP_setter(instance):
    original = instance.CP
    instance.CP = original
    assert instance.CP == original



@given(instance=afpText_GCHST_strategy)
def test_afptext_gchst_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_GCRLINE_strategy)
@settings(max_examples=50)
def test_afptext_gcrline_instantiation(instance):
    assert isinstance(instance, afpText_GCRLINE)

@given(instance=afpText_GRLINE_strategy)
@settings(max_examples=50)
def test_afptext_grline_instantiation(instance):
    assert isinstance(instance, afpText_GRLINE)



@given(instance=afpText_GRLINE_strategy)
def test_afptext_grline_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GRLINE_strategy)
def test_afptext_grline_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText_SetBiLevelImageColor_strategy)
@settings(max_examples=50)
def test_afptext_setbilevelimagecolor_instantiation(instance):
    assert isinstance(instance, afpText_SetBiLevelImageColor)



@given(instance=afpText_SetBiLevelImageColor_strategy)
def test_afptext_setbilevelimagecolor_NAMECOLR_setter(instance):
    original = instance.NAMECOLR
    instance.NAMECOLR = original
    assert instance.NAMECOLR == original



@given(instance=afpText_SetBiLevelImageColor_strategy)
def test_afptext_setbilevelimagecolor_AREA_setter(instance):
    original = instance.AREA
    instance.AREA = original
    assert instance.AREA == original



@given(instance=afpText_SetBiLevelImageColor_strategy)
def test_afptext_setbilevelimagecolor_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_ObjectAreaSize_strategy)
@settings(max_examples=50)
def test_afptext_objectareasize_instantiation(instance):
    assert isinstance(instance, afpText_ObjectAreaSize)



@given(instance=afpText_ObjectAreaSize_strategy)
def test_afptext_objectareasize_XoaSize_setter(instance):
    original = instance.XoaSize
    instance.XoaSize = original
    assert instance.XoaSize == original



@given(instance=afpText_ObjectAreaSize_strategy)
def test_afptext_objectareasize_SizeType_setter(instance):
    original = instance.SizeType
    instance.SizeType = original
    assert instance.SizeType == original



@given(instance=afpText_ObjectAreaSize_strategy)
def test_afptext_objectareasize_YoaSize_setter(instance):
    original = instance.YoaSize
    instance.YoaSize = original
    assert instance.YoaSize == original

@given(instance=afpText_BLN_strategy)
@settings(max_examples=50)
def test_afptext_bln_instantiation(instance):
    assert isinstance(instance, afpText_BLN)

@given(instance=afpText_GSMP_strategy)
@settings(max_examples=50)
def test_afptext_gsmp_instantiation(instance):
    assert isinstance(instance, afpText_GSMP)



@given(instance=afpText_GSMP_strategy)
def test_afptext_gsmp_PREC_setter(instance):
    original = instance.PREC
    instance.PREC = original
    assert instance.PREC == original

@given(instance=afpText_GSPS_strategy)
@settings(max_examples=50)
def test_afptext_gsps_instantiation(instance):
    assert isinstance(instance, afpText_GSPS)



@given(instance=afpText_GSPS_strategy)
def test_afptext_gsps_LCID_setter(instance):
    original = instance.LCID
    instance.LCID = original
    assert instance.LCID == original

@given(instance=afpText_AMB_strategy)
@settings(max_examples=50)
def test_afptext_amb_instantiation(instance):
    assert isinstance(instance, afpText_AMB)



@given(instance=afpText_AMB_strategy)
def test_afptext_amb_DSPLCMNT_setter(instance):
    original = instance.DSPLCMNT
    instance.DSPLCMNT = original
    assert instance.DSPLCMNT == original

@given(instance=afpText_SVI_strategy)
@settings(max_examples=50)
def test_afptext_svi_instantiation(instance):
    assert isinstance(instance, afpText_SVI)



@given(instance=afpText_SVI_strategy)
def test_afptext_svi_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText_STO_strategy)
@settings(max_examples=50)
def test_afptext_sto_instantiation(instance):
    assert isinstance(instance, afpText_STO)



@given(instance=afpText_STO_strategy)
def test_afptext_sto_IORNTION_setter(instance):
    original = instance.IORNTION
    instance.IORNTION = original
    assert instance.IORNTION == original



@given(instance=afpText_STO_strategy)
def test_afptext_sto_BORNTION_setter(instance):
    original = instance.BORNTION
    instance.BORNTION = original
    assert instance.BORNTION == original

@given(instance=afpText_STC_strategy)
@settings(max_examples=50)
def test_afptext_stc_instantiation(instance):
    assert isinstance(instance, afpText_STC)



@given(instance=afpText_STC_strategy)
def test_afptext_stc_PRECSION_setter(instance):
    original = instance.PRECSION
    instance.PRECSION = original
    assert instance.PRECSION == original



@given(instance=afpText_STC_strategy)
def test_afptext_stc_FRGCOLOR_setter(instance):
    original = instance.FRGCOLOR
    instance.FRGCOLOR = original
    assert instance.FRGCOLOR == original

@given(instance=afpText_SIM_strategy)
@settings(max_examples=50)
def test_afptext_sim_instantiation(instance):
    assert isinstance(instance, afpText_SIM)



@given(instance=afpText_SIM_strategy)
def test_afptext_sim_DSPLCMNT_setter(instance):
    original = instance.DSPLCMNT
    instance.DSPLCMNT = original
    assert instance.DSPLCMNT == original

@given(instance=afpText_SIA_strategy)
@settings(max_examples=50)
def test_afptext_sia_instantiation(instance):
    assert isinstance(instance, afpText_SIA)



@given(instance=afpText_SIA_strategy)
def test_afptext_sia_DIRCTION_setter(instance):
    original = instance.DIRCTION
    instance.DIRCTION = original
    assert instance.DIRCTION == original



@given(instance=afpText_SIA_strategy)
def test_afptext_sia_ADJSTMNT_setter(instance):
    original = instance.ADJSTMNT
    instance.ADJSTMNT = original
    assert instance.ADJSTMNT == original

@given(instance=afpText_SEC_strategy)
@settings(max_examples=50)
def test_afptext_sec_instantiation(instance):
    assert isinstance(instance, afpText_SEC)



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_COLSIZE2_setter(instance):
    original = instance.COLSIZE2
    instance.COLSIZE2 = original
    assert instance.COLSIZE2 == original



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_COLSIZE1_setter(instance):
    original = instance.COLSIZE1
    instance.COLSIZE1 = original
    assert instance.COLSIZE1 == original



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_COLVALUE_setter(instance):
    original = instance.COLVALUE
    instance.COLVALUE = original
    assert instance.COLVALUE == original



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_COLSIZE4_setter(instance):
    original = instance.COLSIZE4
    instance.COLSIZE4 = original
    assert instance.COLSIZE4 == original



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_COLSPCE_setter(instance):
    original = instance.COLSPCE
    instance.COLSPCE = original
    assert instance.COLSPCE == original



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_COLSIZE3_setter(instance):
    original = instance.COLSIZE3
    instance.COLSIZE3 = original
    assert instance.COLSIZE3 == original



@given(instance=afpText_SEC_strategy)
def test_afptext_sec_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText_SCFL_strategy)
@settings(max_examples=50)
def test_afptext_scfl_instantiation(instance):
    assert isinstance(instance, afpText_SCFL)



@given(instance=afpText_SCFL_strategy)
def test_afptext_scfl_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText_SBI_strategy)
@settings(max_examples=50)
def test_afptext_sbi_instantiation(instance):
    assert isinstance(instance, afpText_SBI)



@given(instance=afpText_SBI_strategy)
def test_afptext_sbi_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText_RPS_strategy)
@settings(max_examples=50)
def test_afptext_rps_instantiation(instance):
    assert isinstance(instance, afpText_RPS)



@given(instance=afpText_RPS_strategy)
def test_afptext_rps_RPTDATA_setter(instance):
    original = instance.RPTDATA
    instance.RPTDATA = original
    assert instance.RPTDATA == original



@given(instance=afpText_RPS_strategy)
def test_afptext_rps_RLENGTH_setter(instance):
    original = instance.RLENGTH
    instance.RLENGTH = original
    assert instance.RLENGTH == original

@given(instance=afpText_RMI_strategy)
@settings(max_examples=50)
def test_afptext_rmi_instantiation(instance):
    assert isinstance(instance, afpText_RMI)



@given(instance=afpText_RMI_strategy)
def test_afptext_rmi_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText_RMB_strategy)
@settings(max_examples=50)
def test_afptext_rmb_instantiation(instance):
    assert isinstance(instance, afpText_RMB)



@given(instance=afpText_RMB_strategy)
def test_afptext_rmb_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText_OVS_strategy)
@settings(max_examples=50)
def test_afptext_ovs_instantiation(instance):
    assert isinstance(instance, afpText_OVS)



@given(instance=afpText_OVS_strategy)
def test_afptext_ovs_BYPSIDEN_setter(instance):
    original = instance.BYPSIDEN
    instance.BYPSIDEN = original
    assert instance.BYPSIDEN == original



@given(instance=afpText_OVS_strategy)
def test_afptext_ovs_OVERCHAR_setter(instance):
    original = instance.OVERCHAR
    instance.OVERCHAR = original
    assert instance.OVERCHAR == original

@given(instance=afpText_NOPCS_strategy)
@settings(max_examples=50)
def test_afptext_nopcs_instantiation(instance):
    assert isinstance(instance, afpText_NOPCS)



@given(instance=afpText_NOPCS_strategy)
def test_afptext_nopcs_IGNDATA_setter(instance):
    original = instance.IGNDATA
    instance.IGNDATA = original
    assert instance.IGNDATA == original

@given(instance=afpText_ESU_strategy)
@settings(max_examples=50)
def test_afptext_esu_instantiation(instance):
    assert isinstance(instance, afpText_ESU)



@given(instance=afpText_ESU_strategy)
def test_afptext_esu_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText_DIR_strategy)
@settings(max_examples=50)
def test_afptext_dir_instantiation(instance):
    assert isinstance(instance, afpText_DIR)



@given(instance=afpText_DIR_strategy)
def test_afptext_dir_RWIDTH_setter(instance):
    original = instance.RWIDTH
    instance.RWIDTH = original
    assert instance.RWIDTH == original



@given(instance=afpText_DIR_strategy)
def test_afptext_dir_RWIDTHFRACTION_setter(instance):
    original = instance.RWIDTHFRACTION
    instance.RWIDTHFRACTION = original
    assert instance.RWIDTHFRACTION == original



@given(instance=afpText_DIR_strategy)
def test_afptext_dir_RLENGTH_setter(instance):
    original = instance.RLENGTH
    instance.RLENGTH = original
    assert instance.RLENGTH == original

@given(instance=afpText_DBR_strategy)
@settings(max_examples=50)
def test_afptext_dbr_instantiation(instance):
    assert isinstance(instance, afpText_DBR)



@given(instance=afpText_DBR_strategy)
def test_afptext_dbr_RWIDTHFRACTION_setter(instance):
    original = instance.RWIDTHFRACTION
    instance.RWIDTHFRACTION = original
    assert instance.RWIDTHFRACTION == original



@given(instance=afpText_DBR_strategy)
def test_afptext_dbr_RLENGTH_setter(instance):
    original = instance.RLENGTH
    instance.RLENGTH = original
    assert instance.RLENGTH == original



@given(instance=afpText_DBR_strategy)
def test_afptext_dbr_RWIDTH_setter(instance):
    original = instance.RWIDTH
    instance.RWIDTH = original
    assert instance.RWIDTH == original

@given(instance=afpText_GCRLINERG_strategy)
@settings(max_examples=50)
def test_afptext_gcrlinerg_instantiation(instance):
    assert isinstance(instance, afpText_GCRLINERG)



@given(instance=afpText_GCRLINERG_strategy)
def test_afptext_gcrlinerg_YOFFS_setter(instance):
    original = instance.YOFFS
    instance.YOFFS = original
    assert instance.YOFFS == original



@given(instance=afpText_GCRLINERG_strategy)
def test_afptext_gcrlinerg_XOSSF_setter(instance):
    original = instance.XOSSF
    instance.XOSSF = original
    assert instance.XOSSF == original

@given(instance=afpText_GRLINERG_strategy)
@settings(max_examples=50)
def test_afptext_grlinerg_instantiation(instance):
    assert isinstance(instance, afpText_GRLINERG)



@given(instance=afpText_GRLINERG_strategy)
def test_afptext_grlinerg_YOFFS_setter(instance):
    original = instance.YOFFS
    instance.YOFFS = original
    assert instance.YOFFS == original



@given(instance=afpText_GRLINERG_strategy)
def test_afptext_grlinerg_XOSSF_setter(instance):
    original = instance.XOSSF
    instance.XOSSF = original
    assert instance.XOSSF == original

@given(instance=afpText_GCMRKRG_strategy)
@settings(max_examples=50)
def test_afptext_gcmrkrg_instantiation(instance):
    assert isinstance(instance, afpText_GCMRKRG)



@given(instance=afpText_GCMRKRG_strategy)
def test_afptext_gcmrkrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GCMRKRG_strategy)
def test_afptext_gcmrkrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText_GMRKRG_strategy)
@settings(max_examples=50)
def test_afptext_gmrkrg_instantiation(instance):
    assert isinstance(instance, afpText_GMRKRG)



@given(instance=afpText_GMRKRG_strategy)
def test_afptext_gmrkrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GMRKRG_strategy)
def test_afptext_gmrkrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText_GCLINERG_strategy)
@settings(max_examples=50)
def test_afptext_gclinerg_instantiation(instance):
    assert isinstance(instance, afpText_GCLINERG)



@given(instance=afpText_GCLINERG_strategy)
def test_afptext_gclinerg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GCLINERG_strategy)
def test_afptext_gclinerg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_GLINERG_strategy)
@settings(max_examples=50)
def test_afptext_glinerg_instantiation(instance):
    assert isinstance(instance, afpText_GLINERG)



@given(instance=afpText_GLINERG_strategy)
def test_afptext_glinerg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GLINERG_strategy)
def test_afptext_glinerg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_GCFLTRG_strategy)
@settings(max_examples=50)
def test_afptext_gcfltrg_instantiation(instance):
    assert isinstance(instance, afpText_GCFLTRG)



@given(instance=afpText_GCFLTRG_strategy)
def test_afptext_gcfltrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GCFLTRG_strategy)
def test_afptext_gcfltrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText_GFLTRG_strategy)
@settings(max_examples=50)
def test_afptext_gfltrg_instantiation(instance):
    assert isinstance(instance, afpText_GFLTRG)



@given(instance=afpText_GFLTRG_strategy)
def test_afptext_gfltrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original



@given(instance=afpText_GFLTRG_strategy)
def test_afptext_gfltrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText_GCCBEZRG_strategy)
@settings(max_examples=50)
def test_afptext_gccbezrg_instantiation(instance):
    assert isinstance(instance, afpText_GCCBEZRG)



@given(instance=afpText_GCCBEZRG_strategy)
def test_afptext_gccbezrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GCCBEZRG_strategy)
def test_afptext_gccbezrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_GCBEZRG_strategy)
@settings(max_examples=50)
def test_afptext_gcbezrg_instantiation(instance):
    assert isinstance(instance, afpText_GCBEZRG)



@given(instance=afpText_GCBEZRG_strategy)
def test_afptext_gcbezrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original



@given(instance=afpText_GCBEZRG_strategy)
def test_afptext_gcbezrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText_FNNRG_strategy)
@settings(max_examples=50)
def test_afptext_fnnrg_instantiation(instance):
    assert isinstance(instance, afpText_FNNRG)



@given(instance=afpText_FNNRG_strategy)
def test_afptext_fnnrg_TSOffset_setter(instance):
    original = instance.TSOffset
    instance.TSOffset = original
    assert instance.TSOffset == original



@given(instance=afpText_FNNRG_strategy)
def test_afptext_fnnrg_GCGID_setter(instance):
    original = instance.GCGID
    instance.GCGID = original
    assert instance.GCGID == original

@given(instance=afpText_ExternalAlgorithmRG_strategy)
@settings(max_examples=50)
def test_afptext_externalalgorithmrg_instantiation(instance):
    assert isinstance(instance, afpText_ExternalAlgorithmRG)



@given(instance=afpText_ExternalAlgorithmRG_strategy)
def test_afptext_externalalgorithmrg_DIRCTN_setter(instance):
    original = instance.DIRCTN
    instance.DIRCTN = original
    assert instance.DIRCTN == original



@given(instance=afpText_ExternalAlgorithmRG_strategy)
def test_afptext_externalalgorithmrg_PADBDRY_setter(instance):
    original = instance.PADBDRY
    instance.PADBDRY = original
    assert instance.PADBDRY == original



@given(instance=afpText_ExternalAlgorithmRG_strategy)
def test_afptext_externalalgorithmrg_PADALMT_setter(instance):
    original = instance.PADALMT
    instance.PADALMT = original
    assert instance.PADALMT == original

@given(instance=afpText_SamplingRatiosRG_strategy)
@settings(max_examples=50)
def test_afptext_samplingratiosrg_instantiation(instance):
    assert isinstance(instance, afpText_SamplingRatiosRG)



@given(instance=afpText_SamplingRatiosRG_strategy)
def test_afptext_samplingratiosrg_HSAMPLE_setter(instance):
    original = instance.HSAMPLE
    instance.HSAMPLE = original
    assert instance.HSAMPLE == original



@given(instance=afpText_SamplingRatiosRG_strategy)
def test_afptext_samplingratiosrg_VSAMPLE_setter(instance):
    original = instance.VSAMPLE
    instance.VSAMPLE = original
    assert instance.VSAMPLE == original

@given(instance=afpText_TileTOCRG_strategy)
@settings(max_examples=50)
def test_afptext_tiletocrg_instantiation(instance):
    assert isinstance(instance, afpText_TileTOCRG)



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_RELRES_setter(instance):
    original = instance.RELRES
    instance.RELRES = original
    assert instance.RELRES == original



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_YOFFSET_setter(instance):
    original = instance.YOFFSET
    instance.YOFFSET = original
    assert instance.YOFFSET == original



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_XOFFSET_setter(instance):
    original = instance.XOFFSET
    instance.XOFFSET = original
    assert instance.XOFFSET == original



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_TVSIZE_setter(instance):
    original = instance.TVSIZE
    instance.TVSIZE = original
    assert instance.TVSIZE == original



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_COMPR_setter(instance):
    original = instance.COMPR
    instance.COMPR = original
    assert instance.COMPR == original



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_DATAPOS_setter(instance):
    original = instance.DATAPOS
    instance.DATAPOS = original
    assert instance.DATAPOS == original



@given(instance=afpText_TileTOCRG_strategy)
def test_afptext_tiletocrg_THSIZE_setter(instance):
    original = instance.THSIZE
    instance.THSIZE = original
    assert instance.THSIZE == original

@given(instance=afpText_BandImageRG_strategy)
@settings(max_examples=50)
def test_afptext_bandimagerg_instantiation(instance):
    assert isinstance(instance, afpText_BandImageRG)



@given(instance=afpText_BandImageRG_strategy)
def test_afptext_bandimagerg_BITCNT_setter(instance):
    original = instance.BITCNT
    instance.BITCNT = original
    assert instance.BITCNT == original

@given(instance=afpText_PPORG_strategy)
@settings(max_examples=50)
def test_afptext_pporg_instantiation(instance):
    assert isinstance(instance, afpText_PPORG)



@given(instance=afpText_PPORG_strategy)
def test_afptext_pporg_XocaOset_setter(instance):
    original = instance.XocaOset
    instance.XocaOset = original
    assert instance.XocaOset == original



@given(instance=afpText_PPORG_strategy)
def test_afptext_pporg_YocaOset_setter(instance):
    original = instance.YocaOset
    instance.YocaOset = original
    assert instance.YocaOset == original



@given(instance=afpText_PPORG_strategy)
def test_afptext_pporg_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original



@given(instance=afpText_PPORG_strategy)
def test_afptext_pporg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original



@given(instance=afpText_PPORG_strategy)
def test_afptext_pporg_ProcFlgs_setter(instance):
    original = instance.ProcFlgs
    instance.ProcFlgs = original
    assert instance.ProcFlgs == original

@given(instance=afpText_PGPRG_strategy)
@settings(max_examples=50)
def test_afptext_pgprg_instantiation(instance):
    assert isinstance(instance, afpText_PGPRG)



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_PGorient_setter(instance):
    original = instance.PGorient
    instance.PGorient = original
    assert instance.PGorient == original



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_PMCid_setter(instance):
    original = instance.PMCid
    instance.PMCid = original
    assert instance.PMCid == original



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_SHside_setter(instance):
    original = instance.SHside
    instance.SHside = original
    assert instance.SHside == original



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_PgFlgs_setter(instance):
    original = instance.PgFlgs
    instance.PgFlgs = original
    assert instance.PgFlgs == original



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_XmOset_setter(instance):
    original = instance.XmOset
    instance.XmOset = original
    assert instance.XmOset == original



@given(instance=afpText_PGPRG_strategy)
def test_afptext_pgprg_YmOset_setter(instance):
    original = instance.YmOset
    instance.YmOset = original
    assert instance.YmOset == original

@given(instance=afpText_MSURG_strategy)
@settings(max_examples=50)
def test_afptext_msurg_instantiation(instance):
    assert isinstance(instance, afpText_MSURG)



@given(instance=afpText_MSURG_strategy)
def test_afptext_msurg_SUPid_setter(instance):
    original = instance.SUPid
    instance.SUPid = original
    assert instance.SUPid == original



@given(instance=afpText_MSURG_strategy)
def test_afptext_msurg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_MSURG_strategy)
def test_afptext_msurg_SUPname_setter(instance):
    original = instance.SUPname
    instance.SUPname = original
    assert instance.SUPname == original

@given(instance=afpText_MPSRG_strategy)
@settings(max_examples=50)
def test_afptext_mpsrg_instantiation(instance):
    assert isinstance(instance, afpText_MPSRG)



@given(instance=afpText_MPSRG_strategy)
def test_afptext_mpsrg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_MPSRG_strategy)
def test_afptext_mpsrg_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText_MPORG_strategy)
@settings(max_examples=50)
def test_afptext_mporg_instantiation(instance):
    assert isinstance(instance, afpText_MPORG)



@given(instance=afpText_MPORG_strategy)
def test_afptext_mporg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MPGRG_strategy)
@settings(max_examples=50)
def test_afptext_mpgrg_instantiation(instance):
    assert isinstance(instance, afpText_MPGRG)



@given(instance=afpText_MPGRG_strategy)
def test_afptext_mpgrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MMTRG_strategy)
@settings(max_examples=50)
def test_afptext_mmtrg_instantiation(instance):
    assert isinstance(instance, afpText_MMTRG)



@given(instance=afpText_MMTRG_strategy)
def test_afptext_mmtrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MMORG_strategy)
@settings(max_examples=50)
def test_afptext_mmorg_instantiation(instance):
    assert isinstance(instance, afpText_MMORG)



@given(instance=afpText_MMORG_strategy)
def test_afptext_mmorg_OVLid_setter(instance):
    original = instance.OVLid
    instance.OVLid = original
    assert instance.OVLid == original



@given(instance=afpText_MMORG_strategy)
def test_afptext_mmorg_OVLname_setter(instance):
    original = instance.OVLname
    instance.OVLname = original
    assert instance.OVLname == original



@given(instance=afpText_MMORG_strategy)
def test_afptext_mmorg_Flags_setter(instance):
    original = instance.Flags
    instance.Flags = original
    assert instance.Flags == original

@given(instance=afpText_MMDRG_strategy)
@settings(max_examples=50)
def test_afptext_mmdrg_instantiation(instance):
    assert isinstance(instance, afpText_MMDRG)



@given(instance=afpText_MMDRG_strategy)
def test_afptext_mmdrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MMCRG_strategy)
@settings(max_examples=50)
def test_afptext_mmcrg_instantiation(instance):
    assert isinstance(instance, afpText_MMCRG)



@given(instance=afpText_MMCRG_strategy)
def test_afptext_mmcrg_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=afpText_MMCRG_strategy)
def test_afptext_mmcrg_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=afpText_MIORG_strategy)
@settings(max_examples=50)
def test_afptext_miorg_instantiation(instance):
    assert isinstance(instance, afpText_MIORG)



@given(instance=afpText_MIORG_strategy)
def test_afptext_miorg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MGORG_strategy)
@settings(max_examples=50)
def test_afptext_mgorg_instantiation(instance):
    assert isinstance(instance, afpText_MGORG)



@given(instance=afpText_MGORG_strategy)
def test_afptext_mgorg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MCARG_strategy)
@settings(max_examples=50)
def test_afptext_mcarg_instantiation(instance):
    assert isinstance(instance, afpText_MCARG)



@given(instance=afpText_MCARG_strategy)
def test_afptext_mcarg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MDRRG_strategy)
@settings(max_examples=50)
def test_afptext_mdrrg_instantiation(instance):
    assert isinstance(instance, afpText_MDRRG)



@given(instance=afpText_MDRRG_strategy)
def test_afptext_mdrrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MCF1RG_strategy)
@settings(max_examples=50)
def test_afptext_mcf1rg_instantiation(instance):
    assert isinstance(instance, afpText_MCF1RG)



@given(instance=afpText_MCF1RG_strategy)
def test_afptext_mcf1rg_FCSName_setter(instance):
    original = instance.FCSName
    instance.FCSName = original
    assert instance.FCSName == original



@given(instance=afpText_MCF1RG_strategy)
def test_afptext_mcf1rg_CPName_setter(instance):
    original = instance.CPName
    instance.CPName = original
    assert instance.CPName == original



@given(instance=afpText_MCF1RG_strategy)
def test_afptext_mcf1rg_CFLid_setter(instance):
    original = instance.CFLid
    instance.CFLid = original
    assert instance.CFLid == original



@given(instance=afpText_MCF1RG_strategy)
def test_afptext_mcf1rg_CFName_setter(instance):
    original = instance.CFName
    instance.CFName = original
    assert instance.CFName == original



@given(instance=afpText_MCF1RG_strategy)
def test_afptext_mcf1rg_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original



@given(instance=afpText_MCF1RG_strategy)
def test_afptext_mcf1rg_Sectid_setter(instance):
    original = instance.Sectid
    instance.Sectid = original
    assert instance.Sectid == original

@given(instance=afpText_MCFRG_strategy)
@settings(max_examples=50)
def test_afptext_mcfrg_instantiation(instance):
    assert isinstance(instance, afpText_MCFRG)



@given(instance=afpText_MCFRG_strategy)
def test_afptext_mcfrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MCDRG_strategy)
@settings(max_examples=50)
def test_afptext_mcdrg_instantiation(instance):
    assert isinstance(instance, afpText_MCDRG)



@given(instance=afpText_MCDRG_strategy)
def test_afptext_mcdrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_MCCRG_strategy)
@settings(max_examples=50)
def test_afptext_mccrg_instantiation(instance):
    assert isinstance(instance, afpText_MCCRG)



@given(instance=afpText_MCCRG_strategy)
def test_afptext_mccrg_MMCid_setter(instance):
    original = instance.MMCid
    instance.MMCid = original
    assert instance.MMCid == original



@given(instance=afpText_MCCRG_strategy)
def test_afptext_mccrg_Stopnum_setter(instance):
    original = instance.Stopnum
    instance.Stopnum = original
    assert instance.Stopnum == original



@given(instance=afpText_MCCRG_strategy)
def test_afptext_mccrg_Startnum_setter(instance):
    original = instance.Startnum
    instance.Startnum = original
    assert instance.Startnum == original

@given(instance=afpText_MBCRG_strategy)
@settings(max_examples=50)
def test_afptext_mbcrg_instantiation(instance):
    assert isinstance(instance, afpText_MBCRG)



@given(instance=afpText_MBCRG_strategy)
def test_afptext_mbcrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_LLERG_strategy)
@settings(max_examples=50)
def test_afptext_llerg_instantiation(instance):
    assert isinstance(instance, afpText_LLERG)



@given(instance=afpText_LLERG_strategy)
def test_afptext_llerg_RGFunct_setter(instance):
    original = instance.RGFunct
    instance.RGFunct = original
    assert instance.RGFunct == original



@given(instance=afpText_LLERG_strategy)
def test_afptext_llerg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_CPIRG_strategy)
@settings(max_examples=50)
def test_afptext_cpirg_instantiation(instance):
    assert isinstance(instance, afpText_CPIRG)



@given(instance=afpText_CPIRG_strategy)
def test_afptext_cpirg_GCGID_setter(instance):
    original = instance.GCGID
    instance.GCGID = original
    assert instance.GCGID == original



@given(instance=afpText_CPIRG_strategy)
def test_afptext_cpirg_CodePoint_setter(instance):
    original = instance.CodePoint
    instance.CodePoint = original
    assert instance.CodePoint == original



@given(instance=afpText_CPIRG_strategy)
def test_afptext_cpirg_Count_setter(instance):
    original = instance.Count
    instance.Count = original
    assert instance.Count == original



@given(instance=afpText_CPIRG_strategy)
def test_afptext_cpirg_PrtFlags_setter(instance):
    original = instance.PrtFlags
    instance.PrtFlags = original
    assert instance.PrtFlags == original

@given(instance=afpText_CFIRG_strategy)
@settings(max_examples=50)
def test_afptext_cfirg_instantiation(instance):
    assert isinstance(instance, afpText_CFIRG)



@given(instance=afpText_CFIRG_strategy)
def test_afptext_cfirg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_CFIRG_strategy)
def test_afptext_cfirg_CPName_setter(instance):
    original = instance.CPName
    instance.CPName = original
    assert instance.CPName == original



@given(instance=afpText_CFIRG_strategy)
def test_afptext_cfirg_SHScale_setter(instance):
    original = instance.SHScale
    instance.SHScale = original
    assert instance.SHScale == original



@given(instance=afpText_CFIRG_strategy)
def test_afptext_cfirg_FCSName_setter(instance):
    original = instance.FCSName
    instance.FCSName = original
    assert instance.FCSName == original



@given(instance=afpText_CFIRG_strategy)
def test_afptext_cfirg_Section_setter(instance):
    original = instance.Section
    instance.Section = original
    assert instance.Section == original



@given(instance=afpText_CFIRG_strategy)
def test_afptext_cfirg_SVSize_setter(instance):
    original = instance.SVSize
    instance.SVSize = original
    assert instance.SVSize == original

@given(instance=afpText_triplet_strategy)
@settings(max_examples=50)
def test_afptext_triplet_instantiation(instance):
    assert isinstance(instance, afpText_triplet)

@given(instance=structuredField_strategy)
@settings(max_examples=50)
def test_structuredfield_instantiation(instance):
    assert isinstance(instance, structuredField)

@given(instance=afpText_PGP1_strategy)
@settings(max_examples=50)
def test_afptext_pgp1_instantiation(instance):
    assert isinstance(instance, afpText_PGP1)



@given(instance=afpText_PGP1_strategy)
def test_afptext_pgp1_YOset_setter(instance):
    original = instance.YOset
    instance.YOset = original
    assert instance.YOset == original



@given(instance=afpText_PGP1_strategy)
def test_afptext_pgp1_XOset_setter(instance):
    original = instance.XOset
    instance.XOset = original
    assert instance.XOset == original

@given(instance=afpText_BPM_strategy)
@settings(max_examples=50)
def test_afptext_bpm_instantiation(instance):
    assert isinstance(instance, afpText_BPM)



@given(instance=afpText_BPM_strategy)
def test_afptext_bpm_PMName_setter(instance):
    original = instance.PMName
    instance.PMName = original
    assert instance.PMName == original

@given(instance=afpText_MPO_strategy)
@settings(max_examples=50)
def test_afptext_mpo_instantiation(instance):
    assert isinstance(instance, afpText_MPO)

@given(instance=afpText_BPF_strategy)
@settings(max_examples=50)
def test_afptext_bpf_instantiation(instance):
    assert isinstance(instance, afpText_BPF)



@given(instance=afpText_BPF_strategy)
def test_afptext_bpf_PFName_setter(instance):
    original = instance.PFName
    instance.PFName = original
    assert instance.PFName == original

@given(instance=afpText_BRG_strategy)
@settings(max_examples=50)
def test_afptext_brg_instantiation(instance):
    assert isinstance(instance, afpText_BRG)



@given(instance=afpText_BRG_strategy)
def test_afptext_brg_RGrpName_setter(instance):
    original = instance.RGrpName
    instance.RGrpName = original
    assert instance.RGrpName == original

@given(instance=afpText_EAG_strategy)
@settings(max_examples=50)
def test_afptext_eag_instantiation(instance):
    assert isinstance(instance, afpText_EAG)



@given(instance=afpText_EAG_strategy)
def test_afptext_eag_AEGName_setter(instance):
    original = instance.AEGName
    instance.AEGName = original
    assert instance.AEGName == original

@given(instance=afpText_CAT_strategy)
@settings(max_examples=50)
def test_afptext_cat_instantiation(instance):
    assert isinstance(instance, afpText_CAT)



@given(instance=afpText_CAT_strategy)
def test_afptext_cat_CATData_setter(instance):
    original = instance.CATData
    instance.CATData = original
    assert instance.CATData == original

@given(instance=afpText_MCD_strategy)
@settings(max_examples=50)
def test_afptext_mcd_instantiation(instance):
    assert isinstance(instance, afpText_MCD)

@given(instance=afpText_BDT_strategy)
@settings(max_examples=50)
def test_afptext_bdt_instantiation(instance):
    assert isinstance(instance, afpText_BDT)



@given(instance=afpText_BDT_strategy)
def test_afptext_bdt_DocName_setter(instance):
    original = instance.DocName
    instance.DocName = original
    assert instance.DocName == original



@given(instance=afpText_BDT_strategy)
def test_afptext_bdt_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_BMM_strategy)
@settings(max_examples=50)
def test_afptext_bmm_instantiation(instance):
    assert isinstance(instance, afpText_BMM)



@given(instance=afpText_BMM_strategy)
def test_afptext_bmm_MMName_setter(instance):
    original = instance.MMName
    instance.MMName = original
    assert instance.MMName == original

@given(instance=afpText_ECF_strategy)
@settings(max_examples=50)
def test_afptext_ecf_instantiation(instance):
    assert isinstance(instance, afpText_ECF)



@given(instance=afpText_ECF_strategy)
def test_afptext_ecf_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_BOG_strategy)
@settings(max_examples=50)
def test_afptext_bog_instantiation(instance):
    assert isinstance(instance, afpText_BOG)



@given(instance=afpText_BOG_strategy)
def test_afptext_bog_OEGName_setter(instance):
    original = instance.OEGName
    instance.OEGName = original
    assert instance.OEGName == original

@given(instance=afpText_PMC_strategy)
@settings(max_examples=50)
def test_afptext_pmc_instantiation(instance):
    assert isinstance(instance, afpText_PMC)



@given(instance=afpText_PMC_strategy)
def test_afptext_pmc_PMCid_setter(instance):
    original = instance.PMCid
    instance.PMCid = original
    assert instance.PMCid == original

@given(instance=afpText_BFM_strategy)
@settings(max_examples=50)
def test_afptext_bfm_instantiation(instance):
    assert isinstance(instance, afpText_BFM)



@given(instance=afpText_BFM_strategy)
def test_afptext_bfm_FMName_setter(instance):
    original = instance.FMName
    instance.FMName = original
    assert instance.FMName == original

@given(instance=afpText_BRS_strategy)
@settings(max_examples=50)
def test_afptext_brs_instantiation(instance):
    assert isinstance(instance, afpText_BRS)



@given(instance=afpText_BRS_strategy)
def test_afptext_brs_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_PTX_strategy)
@settings(max_examples=50)
def test_afptext_ptx_instantiation(instance):
    assert isinstance(instance, afpText_PTX)

@given(instance=afpText_LNC_strategy)
@settings(max_examples=50)
def test_afptext_lnc_instantiation(instance):
    assert isinstance(instance, afpText_LNC)



@given(instance=afpText_LNC_strategy)
def test_afptext_lnc_NumDSC_setter(instance):
    original = instance.NumDSC
    instance.NumDSC = original
    assert instance.NumDSC == original

@given(instance=afpText_MFC_strategy)
@settings(max_examples=50)
def test_afptext_mfc_instantiation(instance):
    assert isinstance(instance, afpText_MFC)



@given(instance=afpText_MFC_strategy)
def test_afptext_mfc_MFCFlgs_setter(instance):
    original = instance.MFCFlgs
    instance.MFCFlgs = original
    assert instance.MFCFlgs == original



@given(instance=afpText_MFC_strategy)
def test_afptext_mfc_MedColl_setter(instance):
    original = instance.MedColl
    instance.MedColl = original
    assert instance.MedColl == original



@given(instance=afpText_MFC_strategy)
def test_afptext_mfc_MFCScpe_setter(instance):
    original = instance.MFCScpe
    instance.MFCScpe = original
    assert instance.MFCScpe == original

@given(instance=afpText_MPS_strategy)
@settings(max_examples=50)
def test_afptext_mps_instantiation(instance):
    assert isinstance(instance, afpText_MPS)



@given(instance=afpText_MPS_strategy)
def test_afptext_mps_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_MPS_strategy)
def test_afptext_mps_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_PTD1_strategy)
@settings(max_examples=50)
def test_afptext_ptd1_instantiation(instance):
    assert isinstance(instance, afpText_PTD1)



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_YPEXTENT_setter(instance):
    original = instance.YPEXTENT
    instance.YPEXTENT = original
    assert instance.YPEXTENT == original



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_YPUNITVL_setter(instance):
    original = instance.YPUNITVL
    instance.YPUNITVL = original
    assert instance.YPUNITVL == original



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_XPUNITVL_setter(instance):
    original = instance.XPUNITVL
    instance.XPUNITVL = original
    assert instance.XPUNITVL == original



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_XPBASE_setter(instance):
    original = instance.XPBASE
    instance.XPBASE = original
    assert instance.XPBASE == original



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_XPEXTENT_setter(instance):
    original = instance.XPEXTENT
    instance.XPEXTENT = original
    assert instance.XPEXTENT == original



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_YPBASE_setter(instance):
    original = instance.YPBASE
    instance.YPBASE = original
    assert instance.YPBASE == original



@given(instance=afpText_PTD1_strategy)
def test_afptext_ptd1_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText_MCF1_strategy)
@settings(max_examples=50)
def test_afptext_mcf1_instantiation(instance):
    assert isinstance(instance, afpText_MCF1)



@given(instance=afpText_MCF1_strategy)
def test_afptext_mcf1_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_LND_strategy)
@settings(max_examples=50)
def test_afptext_lnd_instantiation(instance):
    assert isinstance(instance, afpText_LND)



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_LNDFlgs_setter(instance):
    original = instance.LNDFlgs
    instance.LNDFlgs = original
    assert instance.LNDFlgs == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_SupName_setter(instance):
    original = instance.SupName
    instance.SupName = original
    assert instance.SupName == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_NLNDsp_setter(instance):
    original = instance.NLNDsp
    instance.NLNDsp = original
    assert instance.NLNDsp == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_CCPID_setter(instance):
    original = instance.CCPID
    instance.CCPID = original
    assert instance.CCPID == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_ChnlCde_setter(instance):
    original = instance.ChnlCde
    instance.ChnlCde = original
    assert instance.ChnlCde == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_TxtOrent_setter(instance):
    original = instance.TxtOrent
    instance.TxtOrent = original
    assert instance.TxtOrent == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_TxtColor_setter(instance):
    original = instance.TxtColor
    instance.TxtColor = original
    assert instance.TxtColor == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_BPos_setter(instance):
    original = instance.BPos
    instance.BPos = original
    assert instance.BPos == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_DataLgth_setter(instance):
    original = instance.DataLgth
    instance.DataLgth = original
    assert instance.DataLgth == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_DataStrt_setter(instance):
    original = instance.DataStrt
    instance.DataStrt = original
    assert instance.DataStrt == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_NLNDccp_setter(instance):
    original = instance.NLNDccp
    instance.NLNDccp = original
    assert instance.NLNDccp == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_FntLID_setter(instance):
    original = instance.FntLID
    instance.FntLID = original
    assert instance.FntLID == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_NLNDskp_setter(instance):
    original = instance.NLNDskp
    instance.NLNDskp = original
    assert instance.NLNDskp == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_SubpgID_setter(instance):
    original = instance.SubpgID
    instance.SubpgID = original
    assert instance.SubpgID == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_NLNDreu_setter(instance):
    original = instance.NLNDreu
    instance.NLNDreu = original
    assert instance.NLNDreu == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_IPos_setter(instance):
    original = instance.IPos
    instance.IPos = original
    assert instance.IPos == original



@given(instance=afpText_LND_strategy)
def test_afptext_lnd_SOLid_setter(instance):
    original = instance.SOLid
    instance.SOLid = original
    assert instance.SOLid == original

@given(instance=afpText_BDI_strategy)
@settings(max_examples=50)
def test_afptext_bdi_instantiation(instance):
    assert isinstance(instance, afpText_BDI)



@given(instance=afpText_BDI_strategy)
def test_afptext_bdi_IndxName_setter(instance):
    original = instance.IndxName
    instance.IndxName = original
    assert instance.IndxName == original

@given(instance=afpText_BPG_strategy)
@settings(max_examples=50)
def test_afptext_bpg_instantiation(instance):
    assert isinstance(instance, afpText_BPG)



@given(instance=afpText_BPG_strategy)
def test_afptext_bpg_PageName_setter(instance):
    original = instance.PageName
    instance.PageName = original
    assert instance.PageName == original

@given(instance=afpText_CFI_strategy)
@settings(max_examples=50)
def test_afptext_cfi_instantiation(instance):
    assert isinstance(instance, afpText_CFI)

@given(instance=afpText_NOP_strategy)
@settings(max_examples=50)
def test_afptext_nop_instantiation(instance):
    assert isinstance(instance, afpText_NOP)



@given(instance=afpText_NOP_strategy)
def test_afptext_nop_UndfData_setter(instance):
    original = instance.UndfData
    instance.UndfData = original
    assert instance.UndfData == original

@given(instance=afpText_PTD_strategy)
@settings(max_examples=50)
def test_afptext_ptd_instantiation(instance):
    assert isinstance(instance, afpText_PTD)



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_XPBASE_setter(instance):
    original = instance.XPBASE
    instance.XPBASE = original
    assert instance.XPBASE == original



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_XPUNITVL_setter(instance):
    original = instance.XPUNITVL
    instance.XPUNITVL = original
    assert instance.XPUNITVL == original



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_YPEXTENT_setter(instance):
    original = instance.YPEXTENT
    instance.YPEXTENT = original
    assert instance.YPEXTENT == original



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_YPUNITVL_setter(instance):
    original = instance.YPUNITVL
    instance.YPUNITVL = original
    assert instance.YPUNITVL == original



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_YPBASE_setter(instance):
    original = instance.YPBASE
    instance.YPBASE = original
    assert instance.YPBASE == original



@given(instance=afpText_PTD_strategy)
def test_afptext_ptd_XPEXTENT_setter(instance):
    original = instance.XPEXTENT
    instance.XPEXTENT = original
    assert instance.XPEXTENT == original

@given(instance=afpText_OCD_strategy)
@settings(max_examples=50)
def test_afptext_ocd_instantiation(instance):
    assert isinstance(instance, afpText_OCD)



@given(instance=afpText_OCD_strategy)
def test_afptext_ocd_ObjCdat_setter(instance):
    original = instance.ObjCdat
    instance.ObjCdat = original
    assert instance.ObjCdat == original

@given(instance=afpText_LLE_strategy)
@settings(max_examples=50)
def test_afptext_lle_instantiation(instance):
    assert isinstance(instance, afpText_LLE)



@given(instance=afpText_LLE_strategy)
def test_afptext_lle_LnkType_setter(instance):
    original = instance.LnkType
    instance.LnkType = original
    assert instance.LnkType == original

@given(instance=afpText_BPS_strategy)
@settings(max_examples=50)
def test_afptext_bps_instantiation(instance):
    assert isinstance(instance, afpText_BPS)



@given(instance=afpText_BPS_strategy)
def test_afptext_bps_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText_MDD_strategy)
@settings(max_examples=50)
def test_afptext_mdd_instantiation(instance):
    assert isinstance(instance, afpText_MDD)



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_MDDFlgs_setter(instance):
    original = instance.MDDFlgs
    instance.MDDFlgs = original
    assert instance.MDDFlgs == original



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_XmBase_setter(instance):
    original = instance.XmBase
    instance.XmBase = original
    assert instance.XmBase == original



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_YmSize_setter(instance):
    original = instance.YmSize
    instance.YmSize = original
    assert instance.YmSize == original



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_YmUnits_setter(instance):
    original = instance.YmUnits
    instance.YmUnits = original
    assert instance.YmUnits == original



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_XmSize_setter(instance):
    original = instance.XmSize
    instance.XmSize = original
    assert instance.XmSize == original



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_XmUnits_setter(instance):
    original = instance.XmUnits
    instance.XmUnits = original
    assert instance.XmUnits == original



@given(instance=afpText_MDD_strategy)
def test_afptext_mdd_YmBase_setter(instance):
    original = instance.YmBase
    instance.YmBase = original
    assert instance.YmBase == original

@given(instance=afpText_MPG_strategy)
@settings(max_examples=50)
def test_afptext_mpg_instantiation(instance):
    assert isinstance(instance, afpText_MPG)

@given(instance=afpText_MMT_strategy)
@settings(max_examples=50)
def test_afptext_mmt_instantiation(instance):
    assert isinstance(instance, afpText_MMT)

@given(instance=afpText_EDM_strategy)
@settings(max_examples=50)
def test_afptext_edm_instantiation(instance):
    assert isinstance(instance, afpText_EDM)



@given(instance=afpText_EDM_strategy)
def test_afptext_edm_DMName_setter(instance):
    original = instance.DMName
    instance.DMName = original
    assert instance.DMName == original

@given(instance=afpText_PEC_strategy)
@settings(max_examples=50)
def test_afptext_pec_instantiation(instance):
    assert isinstance(instance, afpText_PEC)

@given(instance=afpText_DXD_strategy)
@settings(max_examples=50)
def test_afptext_dxd_instantiation(instance):
    assert isinstance(instance, afpText_DXD)

@given(instance=afpText_CPD_strategy)
@settings(max_examples=50)
def test_afptext_cpd_instantiation(instance):
    assert isinstance(instance, afpText_CPD)



@given(instance=afpText_CPD_strategy)
def test_afptext_cpd_GCGIDLen_setter(instance):
    original = instance.GCGIDLen
    instance.GCGIDLen = original
    assert instance.GCGIDLen == original



@given(instance=afpText_CPD_strategy)
def test_afptext_cpd_EncScheme_setter(instance):
    original = instance.EncScheme
    instance.EncScheme = original
    assert instance.EncScheme == original



@given(instance=afpText_CPD_strategy)
def test_afptext_cpd_CPDesc_setter(instance):
    original = instance.CPDesc
    instance.CPDesc = original
    assert instance.CPDesc == original



@given(instance=afpText_CPD_strategy)
def test_afptext_cpd_NumCdPts_setter(instance):
    original = instance.NumCdPts
    instance.NumCdPts = original
    assert instance.NumCdPts == original



@given(instance=afpText_CPD_strategy)
def test_afptext_cpd_CPGID_setter(instance):
    original = instance.CPGID
    instance.CPGID = original
    assert instance.CPGID == original



@given(instance=afpText_CPD_strategy)
def test_afptext_cpd_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText_ECA_strategy)
@settings(max_examples=50)
def test_afptext_eca_instantiation(instance):
    assert isinstance(instance, afpText_ECA)



@given(instance=afpText_ECA_strategy)
def test_afptext_eca_CATName_setter(instance):
    original = instance.CATName
    instance.CATName = original
    assert instance.CATName == original

@given(instance=afpText_CDD_strategy)
@settings(max_examples=50)
def test_afptext_cdd_instantiation(instance):
    assert isinstance(instance, afpText_CDD)



@given(instance=afpText_CDD_strategy)
def test_afptext_cdd_YocSize_setter(instance):
    original = instance.YocSize
    instance.YocSize = original
    assert instance.YocSize == original



@given(instance=afpText_CDD_strategy)
def test_afptext_cdd_YocUnits_setter(instance):
    original = instance.YocUnits
    instance.YocUnits = original
    assert instance.YocUnits == original



@given(instance=afpText_CDD_strategy)
def test_afptext_cdd_XocUnits_setter(instance):
    original = instance.XocUnits
    instance.XocUnits = original
    assert instance.XocUnits == original



@given(instance=afpText_CDD_strategy)
def test_afptext_cdd_XocBase_setter(instance):
    original = instance.XocBase
    instance.XocBase = original
    assert instance.XocBase == original



@given(instance=afpText_CDD_strategy)
def test_afptext_cdd_YocBase_setter(instance):
    original = instance.YocBase
    instance.YocBase = original
    assert instance.YocBase == original



@given(instance=afpText_CDD_strategy)
def test_afptext_cdd_XocSize_setter(instance):
    original = instance.XocSize
    instance.XocSize = original
    assert instance.XocSize == original

@given(instance=afpText_BFN_strategy)
@settings(max_examples=50)
def test_afptext_bfn_instantiation(instance):
    assert isinstance(instance, afpText_BFN)



@given(instance=afpText_BFN_strategy)
def test_afptext_bfn_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_BII_strategy)
@settings(max_examples=50)
def test_afptext_bii_instantiation(instance):
    assert isinstance(instance, afpText_BII)



@given(instance=afpText_BII_strategy)
def test_afptext_bii_ImoName_setter(instance):
    original = instance.ImoName
    instance.ImoName = original
    assert instance.ImoName == original

@given(instance=afpText_PGP_strategy)
@settings(max_examples=50)
def test_afptext_pgp_instantiation(instance):
    assert isinstance(instance, afpText_PGP)



@given(instance=afpText_PGP_strategy)
def test_afptext_pgp_Constant_setter(instance):
    original = instance.Constant
    instance.Constant = original
    assert instance.Constant == original

@given(instance=afpText_PGD_strategy)
@settings(max_examples=50)
def test_afptext_pgd_instantiation(instance):
    assert isinstance(instance, afpText_PGD)



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_YpgSize_setter(instance):
    original = instance.YpgSize
    instance.YpgSize = original
    assert instance.YpgSize == original



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_YpgUnits_setter(instance):
    original = instance.YpgUnits
    instance.YpgUnits = original
    assert instance.YpgUnits == original



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_XpgUnits_setter(instance):
    original = instance.XpgUnits
    instance.XpgUnits = original
    assert instance.XpgUnits == original



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_XpgBase_setter(instance):
    original = instance.XpgBase
    instance.XpgBase = original
    assert instance.XpgBase == original



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_YpgBase_setter(instance):
    original = instance.YpgBase
    instance.YpgBase = original
    assert instance.YpgBase == original



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_PGD_strategy)
def test_afptext_pgd_XpgSize_setter(instance):
    original = instance.XpgSize
    instance.XpgSize = original
    assert instance.XpgSize == original

@given(instance=afpText_BOC_strategy)
@settings(max_examples=50)
def test_afptext_boc_instantiation(instance):
    assert isinstance(instance, afpText_BOC)



@given(instance=afpText_BOC_strategy)
def test_afptext_boc_ObjCName_setter(instance):
    original = instance.ObjCName
    instance.ObjCName = original
    assert instance.ObjCName == original

@given(instance=afpText_TLE_strategy)
@settings(max_examples=50)
def test_afptext_tle_instantiation(instance):
    assert isinstance(instance, afpText_TLE)

@given(instance=afpText_BDG_strategy)
@settings(max_examples=50)
def test_afptext_bdg_instantiation(instance):
    assert isinstance(instance, afpText_BDG)



@given(instance=afpText_BDG_strategy)
def test_afptext_bdg_DEGName_setter(instance):
    original = instance.DEGName
    instance.DEGName = original
    assert instance.DEGName == original

@given(instance=afpText_CFC_strategy)
@settings(max_examples=50)
def test_afptext_cfc_instantiation(instance):
    assert isinstance(instance, afpText_CFC)



@given(instance=afpText_CFC_strategy)
def test_afptext_cfc_CFIRGLen_setter(instance):
    original = instance.CFIRGLen
    instance.CFIRGLen = original
    assert instance.CFIRGLen == original



@given(instance=afpText_CFC_strategy)
def test_afptext_cfc_Retired1_setter(instance):
    original = instance.Retired1
    instance.Retired1 = original
    assert instance.Retired1 == original

@given(instance=afpText_MIO_strategy)
@settings(max_examples=50)
def test_afptext_mio_instantiation(instance):
    assert isinstance(instance, afpText_MIO)

@given(instance=afpText_BBC_strategy)
@settings(max_examples=50)
def test_afptext_bbc_instantiation(instance):
    assert isinstance(instance, afpText_BBC)



@given(instance=afpText_BBC_strategy)
def test_afptext_bbc_BCdoName_setter(instance):
    original = instance.BCdoName
    instance.BCdoName = original
    assert instance.BCdoName == original

@given(instance=afpText_BAG_strategy)
@settings(max_examples=50)
def test_afptext_bag_instantiation(instance):
    assert isinstance(instance, afpText_BAG)



@given(instance=afpText_BAG_strategy)
def test_afptext_bag_AEGName_setter(instance):
    original = instance.AEGName
    instance.AEGName = original
    assert instance.AEGName == original

@given(instance=afpText_PPO_strategy)
@settings(max_examples=50)
def test_afptext_ppo_instantiation(instance):
    assert isinstance(instance, afpText_PPO)

@given(instance=afpText_BPT_strategy)
@settings(max_examples=50)
def test_afptext_bpt_instantiation(instance):
    assert isinstance(instance, afpText_BPT)



@given(instance=afpText_BPT_strategy)
def test_afptext_bpt_PTdoName_setter(instance):
    original = instance.PTdoName
    instance.PTdoName = original
    assert instance.PTdoName == original

@given(instance=afpText_ECP_strategy)
@settings(max_examples=50)
def test_afptext_ecp_instantiation(instance):
    assert isinstance(instance, afpText_ECP)



@given(instance=afpText_ECP_strategy)
def test_afptext_ecp_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_MMO_strategy)
@settings(max_examples=50)
def test_afptext_mmo_instantiation(instance):
    assert isinstance(instance, afpText_MMO)



@given(instance=afpText_MMO_strategy)
def test_afptext_mmo_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText_BCP_strategy)
@settings(max_examples=50)
def test_afptext_bcp_instantiation(instance):
    assert isinstance(instance, afpText_BCP)



@given(instance=afpText_BCP_strategy)
def test_afptext_bcp_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_MGO_strategy)
@settings(max_examples=50)
def test_afptext_mgo_instantiation(instance):
    assert isinstance(instance, afpText_MGO)

@given(instance=afpText_PFC_strategy)
@settings(max_examples=50)
def test_afptext_pfc_instantiation(instance):
    assert isinstance(instance, afpText_PFC)



@given(instance=afpText_PFC_strategy)
def test_afptext_pfc_PFCFlgs_setter(instance):
    original = instance.PFCFlgs
    instance.PFCFlgs = original
    assert instance.PFCFlgs == original

@given(instance=afpText_CTC_strategy)
@settings(max_examples=50)
def test_afptext_ctc_instantiation(instance):
    assert isinstance(instance, afpText_CTC)



@given(instance=afpText_CTC_strategy)
def test_afptext_ctc_ConData_setter(instance):
    original = instance.ConData
    instance.ConData = original
    assert instance.ConData == original

@given(instance=afpText_BSG_strategy)
@settings(max_examples=50)
def test_afptext_bsg_instantiation(instance):
    assert isinstance(instance, afpText_BSG)



@given(instance=afpText_BSG_strategy)
def test_afptext_bsg_REGName_setter(instance):
    original = instance.REGName
    instance.REGName = original
    assert instance.REGName == original

@given(instance=afpText_BGR_strategy)
@settings(max_examples=50)
def test_afptext_bgr_instantiation(instance):
    assert isinstance(instance, afpText_BGR)



@given(instance=afpText_BGR_strategy)
def test_afptext_bgr_GdoName_setter(instance):
    original = instance.GdoName
    instance.GdoName = original
    assert instance.GdoName == original

@given(instance=afpText_BCF_strategy)
@settings(max_examples=50)
def test_afptext_bcf_instantiation(instance):
    assert isinstance(instance, afpText_BCF)



@given(instance=afpText_BCF_strategy)
def test_afptext_bcf_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_MBC_strategy)
@settings(max_examples=50)
def test_afptext_mbc_instantiation(instance):
    assert isinstance(instance, afpText_MBC)

@given(instance=afpText_BDM_strategy)
@settings(max_examples=50)
def test_afptext_bdm_instantiation(instance):
    assert isinstance(instance, afpText_BDM)



@given(instance=afpText_BDM_strategy)
def test_afptext_bdm_DatFmt_setter(instance):
    original = instance.DatFmt
    instance.DatFmt = original
    assert instance.DatFmt == original



@given(instance=afpText_BDM_strategy)
def test_afptext_bdm_DMName_setter(instance):
    original = instance.DMName
    instance.DMName = original
    assert instance.DMName == original

@given(instance=afpText_FGD_strategy)
@settings(max_examples=50)
def test_afptext_fgd_instantiation(instance):
    assert isinstance(instance, afpText_FGD)



@given(instance=afpText_FGD_strategy)
def test_afptext_fgd_ConData_setter(instance):
    original = instance.ConData
    instance.ConData = original
    assert instance.ConData == original

@given(instance=afpText_MDR_strategy)
@settings(max_examples=50)
def test_afptext_mdr_instantiation(instance):
    assert isinstance(instance, afpText_MDR)

@given(instance=afpText_MMC_strategy)
@settings(max_examples=50)
def test_afptext_mmc_instantiation(instance):
    assert isinstance(instance, afpText_MMC)



@given(instance=afpText_MMC_strategy)
def test_afptext_mmc_MMCid_setter(instance):
    original = instance.MMCid
    instance.MMCid = original
    assert instance.MMCid == original



@given(instance=afpText_MMC_strategy)
def test_afptext_mmc_PARAMETER1_setter(instance):
    original = instance.PARAMETER1
    instance.PARAMETER1 = original
    assert instance.PARAMETER1 == original

@given(instance=afpText_BFG_strategy)
@settings(max_examples=50)
def test_afptext_bfg_instantiation(instance):
    assert isinstance(instance, afpText_BFG)



@given(instance=afpText_BFG_strategy)
def test_afptext_bfg_FEGName_setter(instance):
    original = instance.FEGName
    instance.FEGName = original
    assert instance.FEGName == original

@given(instance=afpText_MSU_strategy)
@settings(max_examples=50)
def test_afptext_msu_instantiation(instance):
    assert isinstance(instance, afpText_MSU)

@given(instance=afpText_EBC_strategy)
@settings(max_examples=50)
def test_afptext_ebc_instantiation(instance):
    assert isinstance(instance, afpText_EBC)



@given(instance=afpText_EBC_strategy)
def test_afptext_ebc_BCdoName_setter(instance):
    original = instance.BCdoName
    instance.BCdoName = original
    assert instance.BCdoName == original

@given(instance=afpText_OBD_strategy)
@settings(max_examples=50)
def test_afptext_obd_instantiation(instance):
    assert isinstance(instance, afpText_OBD)

@given(instance=afpText_CPI_strategy)
@settings(max_examples=50)
def test_afptext_cpi_instantiation(instance):
    assert isinstance(instance, afpText_CPI)

@given(instance=afpText_BCA_strategy)
@settings(max_examples=50)
def test_afptext_bca_instantiation(instance):
    assert isinstance(instance, afpText_BCA)



@given(instance=afpText_BCA_strategy)
def test_afptext_bca_CATName_setter(instance):
    original = instance.CATName
    instance.CATName = original
    assert instance.CATName == original

@given(instance=afpText_EDG_strategy)
@settings(max_examples=50)
def test_afptext_edg_instantiation(instance):
    assert isinstance(instance, afpText_EDG)



@given(instance=afpText_EDG_strategy)
def test_afptext_edg_DEGName_setter(instance):
    original = instance.DEGName
    instance.DEGName = original
    assert instance.DEGName == original

@given(instance=afpText_OBP_strategy)
@settings(max_examples=50)
def test_afptext_obp_instantiation(instance):
    assert isinstance(instance, afpText_OBP)



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_XoaOset_setter(instance):
    original = instance.XoaOset
    instance.XoaOset = original
    assert instance.XoaOset == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_OAPosID_setter(instance):
    original = instance.OAPosID
    instance.OAPosID = original
    assert instance.OAPosID == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_YoaOset_setter(instance):
    original = instance.YoaOset
    instance.YoaOset = original
    assert instance.YoaOset == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_YocaOrent_setter(instance):
    original = instance.YocaOrent
    instance.YocaOrent = original
    assert instance.YocaOrent == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_YoaOrent_setter(instance):
    original = instance.YoaOrent
    instance.YoaOrent = original
    assert instance.YoaOrent == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_XocaOrent_setter(instance):
    original = instance.XocaOrent
    instance.XocaOrent = original
    assert instance.XocaOrent == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_XocaOset_setter(instance):
    original = instance.XocaOset
    instance.XocaOset = original
    assert instance.XocaOset == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_XoaOrent_setter(instance):
    original = instance.XoaOrent
    instance.XoaOrent = original
    assert instance.XoaOrent == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_RefCSys_setter(instance):
    original = instance.RefCSys
    instance.RefCSys = original
    assert instance.RefCSys == original



@given(instance=afpText_OBP_strategy)
def test_afptext_obp_YocaOset_setter(instance):
    original = instance.YocaOset
    instance.YocaOset = original
    assert instance.YocaOset == original

@given(instance=afpText_BNG_strategy)
@settings(max_examples=50)
def test_afptext_bng_instantiation(instance):
    assert isinstance(instance, afpText_BNG)



@given(instance=afpText_BNG_strategy)
def test_afptext_bng_PGrpName_setter(instance):
    original = instance.PGrpName
    instance.PGrpName = original
    assert instance.PGrpName == original

@given(instance=afpText_BMO_strategy)
@settings(max_examples=50)
def test_afptext_bmo_instantiation(instance):
    assert isinstance(instance, afpText_BMO)



@given(instance=afpText_BMO_strategy)
def test_afptext_bmo_OvlyName_setter(instance):
    original = instance.OvlyName
    instance.OvlyName = original
    assert instance.OvlyName == original

@given(instance=afpText_CPC_strategy)
@settings(max_examples=50)
def test_afptext_cpc_instantiation(instance):
    assert isinstance(instance, afpText_CPC)



@given(instance=afpText_CPC_strategy)
def test_afptext_cpc_PrtFlags_setter(instance):
    original = instance.PrtFlags
    instance.PrtFlags = original
    assert instance.PrtFlags == original



@given(instance=afpText_CPC_strategy)
def test_afptext_cpc_CPIRGLen_setter(instance):
    original = instance.CPIRGLen
    instance.CPIRGLen = original
    assert instance.CPIRGLen == original



@given(instance=afpText_CPC_strategy)
def test_afptext_cpc_VSCharSN_setter(instance):
    original = instance.VSCharSN
    instance.VSCharSN = original
    assert instance.VSCharSN == original



@given(instance=afpText_CPC_strategy)
def test_afptext_cpc_VSChar_setter(instance):
    original = instance.VSChar
    instance.VSChar = original
    assert instance.VSChar == original



@given(instance=afpText_CPC_strategy)
def test_afptext_cpc_DefCharID_setter(instance):
    original = instance.DefCharID
    instance.DefCharID = original
    assert instance.DefCharID == original



@given(instance=afpText_CPC_strategy)
def test_afptext_cpc_VSFlags_setter(instance):
    original = instance.VSFlags
    instance.VSFlags = original
    assert instance.VSFlags == original

@given(instance=afpText_MCA_strategy)
@settings(max_examples=50)
def test_afptext_mca_instantiation(instance):
    assert isinstance(instance, afpText_MCA)

@given(instance=afpText_MCC_strategy)
@settings(max_examples=50)
def test_afptext_mcc_instantiation(instance):
    assert isinstance(instance, afpText_MCC)

@given(instance=afpText_MCF_strategy)
@settings(max_examples=50)
def test_afptext_mcf_instantiation(instance):
    assert isinstance(instance, afpText_MCF)

@given(instance=afpText_EDI_strategy)
@settings(max_examples=50)
def test_afptext_edi_instantiation(instance):
    assert isinstance(instance, afpText_EDI)



@given(instance=afpText_EDI_strategy)
def test_afptext_edi_IndxName_setter(instance):
    original = instance.IndxName
    instance.IndxName = original
    assert instance.IndxName == original

@given(instance=afpText_BDD_strategy)
@settings(max_examples=50)
def test_afptext_bdd_instantiation(instance):
    assert isinstance(instance, afpText_BDD)



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_MULT_setter(instance):
    original = instance.MULT
    instance.MULT = original
    assert instance.MULT == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_WENE_setter(instance):
    original = instance.WENE
    instance.WENE = original
    assert instance.WENE == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_YUPUB_setter(instance):
    original = instance.YUPUB
    instance.YUPUB = original
    assert instance.YUPUB == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_ELEMENTHEIGHT_setter(instance):
    original = instance.ELEMENTHEIGHT
    instance.ELEMENTHEIGHT = original
    assert instance.ELEMENTHEIGHT == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_YEXTENT_setter(instance):
    original = instance.YEXTENT
    instance.YEXTENT = original
    assert instance.YEXTENT == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_MOD_setter(instance):
    original = instance.MOD
    instance.MOD = original
    assert instance.MOD == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_XEXTENT_setter(instance):
    original = instance.XEXTENT
    instance.XEXTENT = original
    assert instance.XEXTENT == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_MODULEWIDTH_setter(instance):
    original = instance.MODULEWIDTH
    instance.MODULEWIDTH = original
    assert instance.MODULEWIDTH == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_XUPUB_setter(instance):
    original = instance.XUPUB
    instance.XUPUB = original
    assert instance.XUPUB == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_UBASE_setter(instance):
    original = instance.UBASE
    instance.UBASE = original
    assert instance.UBASE == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_TYPE_setter(instance):
    original = instance.TYPE
    instance.TYPE = original
    assert instance.TYPE == original



@given(instance=afpText_BDD_strategy)
def test_afptext_bdd_COLOR_setter(instance):
    original = instance.COLOR
    instance.COLOR = original
    assert instance.COLOR == original

@given(instance=afpText_MMD_strategy)
@settings(max_examples=50)
def test_afptext_mmd_instantiation(instance):
    assert isinstance(instance, afpText_MMD)

@given(instance=afpText_BDA_strategy)
@settings(max_examples=50)
def test_afptext_bda_instantiation(instance):
    assert isinstance(instance, afpText_BDA)



@given(instance=afpText_BDA_strategy)
def test_afptext_bda_Data_setter(instance):
    original = instance.Data
    instance.Data = original
    assert instance.Data == original



@given(instance=afpText_BDA_strategy)
def test_afptext_bda_Xoffset_setter(instance):
    original = instance.Xoffset
    instance.Xoffset = original
    assert instance.Xoffset == original



@given(instance=afpText_BDA_strategy)
def test_afptext_bda_Flags_setter(instance):
    original = instance.Flags
    instance.Flags = original
    assert instance.Flags == original



@given(instance=afpText_BDA_strategy)
def test_afptext_bda_Yoffset_setter(instance):
    original = instance.Yoffset
    instance.Yoffset = original
    assert instance.Yoffset == original

@given(instance=afpText_BIM_strategy)
@settings(max_examples=50)
def test_afptext_bim_instantiation(instance):
    assert isinstance(instance, afpText_BIM)



@given(instance=afpText_BIM_strategy)
def test_afptext_bim_IdoName_setter(instance):
    original = instance.IdoName
    instance.IdoName = original
    assert instance.IdoName == original

@given(instance=afpText_BDX_strategy)
@settings(max_examples=50)
def test_afptext_bdx_instantiation(instance):
    assert isinstance(instance, afpText_BDX)



@given(instance=afpText_BDX_strategy)
def test_afptext_bdx_DMXName_setter(instance):
    original = instance.DMXName
    instance.DMXName = original
    assert instance.DMXName == original

@given(instance=afpText_LineData_strategy)
@settings(max_examples=50)
def test_afptext_linedata_instantiation(instance):
    assert isinstance(instance, afpText_LineData)



@given(instance=afpText_LineData_strategy)
def test_afptext_linedata_linedata_setter(instance):
    original = instance.linedata
    instance.linedata = original
    assert instance.linedata == original

@given(instance=afpText_structuredField_strategy)
@settings(max_examples=50)
def test_afptext_structuredfield_instantiation(instance):
    assert isinstance(instance, afpText_structuredField)

@given(instance=afpText_Model_strategy)
@settings(max_examples=50)
def test_afptext_model_instantiation(instance):
    assert isinstance(instance, afpText_Model)

@given(instance=afpText_IPO_strategy)
@settings(max_examples=50)
def test_afptext_ipo_instantiation(instance):
    assert isinstance(instance, afpText_IPO)



@given(instance=afpText_IPO_strategy)
def test_afptext_ipo_OvlyName_setter(instance):
    original = instance.OvlyName
    instance.OvlyName = original
    assert instance.OvlyName == original



@given(instance=afpText_IPO_strategy)
def test_afptext_ipo_YolOset_setter(instance):
    original = instance.YolOset
    instance.YolOset = original
    assert instance.YolOset == original



@given(instance=afpText_IPO_strategy)
def test_afptext_ipo_XolOset_setter(instance):
    original = instance.XolOset
    instance.XolOset = original
    assert instance.XolOset == original



@given(instance=afpText_IPO_strategy)
def test_afptext_ipo_OvlyOrent_setter(instance):
    original = instance.OvlyOrent
    instance.OvlyOrent = original
    assert instance.OvlyOrent == original

@given(instance=afpText_IRD_strategy)
@settings(max_examples=50)
def test_afptext_ird_instantiation(instance):
    assert isinstance(instance, afpText_IRD)



@given(instance=afpText_IRD_strategy)
def test_afptext_ird_IMdata_setter(instance):
    original = instance.IMdata
    instance.IMdata = original
    assert instance.IMdata == original

@given(instance=afpText_IPS_strategy)
@settings(max_examples=50)
def test_afptext_ips_instantiation(instance):
    assert isinstance(instance, afpText_IPS)



@given(instance=afpText_IPS_strategy)
def test_afptext_ips_YpsOset_setter(instance):
    original = instance.YpsOset
    instance.YpsOset = original
    assert instance.YpsOset == original



@given(instance=afpText_IPS_strategy)
def test_afptext_ips_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original



@given(instance=afpText_IPS_strategy)
def test_afptext_ips_XpsOset_setter(instance):
    original = instance.XpsOset
    instance.XpsOset = original
    assert instance.XpsOset == original

@given(instance=afpText_IPG_strategy)
@settings(max_examples=50)
def test_afptext_ipg_instantiation(instance):
    assert isinstance(instance, afpText_IPG)



@given(instance=afpText_IPG_strategy)
def test_afptext_ipg_PgName_setter(instance):
    original = instance.PgName
    instance.PgName = original
    assert instance.PgName == original



@given(instance=afpText_IPG_strategy)
def test_afptext_ipg_IPgFlgs_setter(instance):
    original = instance.IPgFlgs
    instance.IPgFlgs = original
    assert instance.IPgFlgs == original

@given(instance=afpText_IPD_strategy)
@settings(max_examples=50)
def test_afptext_ipd_instantiation(instance):
    assert isinstance(instance, afpText_IPD)



@given(instance=afpText_IPD_strategy)
def test_afptext_ipd_imageData_setter(instance):
    original = instance.imageData
    instance.imageData = original
    assert instance.imageData == original



@given(instance=afpText_IPD_strategy)
def test_afptext_ipd_IOCAdat_setter(instance):
    original = instance.IOCAdat
    instance.IOCAdat = original
    assert instance.IOCAdat == original

@given(instance=afpText_ICP_strategy)
@settings(max_examples=50)
def test_afptext_icp_instantiation(instance):
    assert isinstance(instance, afpText_ICP)



@given(instance=afpText_ICP_strategy)
def test_afptext_icp_XCSize_setter(instance):
    original = instance.XCSize
    instance.XCSize = original
    assert instance.XCSize == original



@given(instance=afpText_ICP_strategy)
def test_afptext_icp_XFilSize_setter(instance):
    original = instance.XFilSize
    instance.XFilSize = original
    assert instance.XFilSize == original



@given(instance=afpText_ICP_strategy)
def test_afptext_icp_YCSize_setter(instance):
    original = instance.YCSize
    instance.YCSize = original
    assert instance.YCSize == original



@given(instance=afpText_ICP_strategy)
def test_afptext_icp_XCOset_setter(instance):
    original = instance.XCOset
    instance.XCOset = original
    assert instance.XCOset == original



@given(instance=afpText_ICP_strategy)
def test_afptext_icp_YCOset_setter(instance):
    original = instance.YCOset
    instance.YCOset = original
    assert instance.YCOset == original



@given(instance=afpText_ICP_strategy)
def test_afptext_icp_YFilSize_setter(instance):
    original = instance.YFilSize
    instance.YFilSize = original
    assert instance.YFilSize == original

@given(instance=afpText_IOC_strategy)
@settings(max_examples=50)
def test_afptext_ioc_instantiation(instance):
    assert isinstance(instance, afpText_IOC)



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_XMap_setter(instance):
    original = instance.XMap
    instance.XMap = original
    assert instance.XMap == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_XoaOset_setter(instance):
    original = instance.XoaOset
    instance.XoaOset = original
    assert instance.XoaOset == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_ConData1_setter(instance):
    original = instance.ConData1
    instance.ConData1 = original
    assert instance.ConData1 == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_YMap_setter(instance):
    original = instance.YMap
    instance.YMap = original
    assert instance.YMap == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_YoaOrent_setter(instance):
    original = instance.YoaOrent
    instance.YoaOrent = original
    assert instance.YoaOrent == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_ConData2_setter(instance):
    original = instance.ConData2
    instance.ConData2 = original
    assert instance.ConData2 == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_XoaOrent_setter(instance):
    original = instance.XoaOrent
    instance.XoaOrent = original
    assert instance.XoaOrent == original



@given(instance=afpText_IOC_strategy)
def test_afptext_ioc_YoaOset_setter(instance):
    original = instance.YoaOset
    instance.YoaOset = original
    assert instance.YoaOset == original

@given(instance=afpText_IOB_strategy)
@settings(max_examples=50)
def test_afptext_iob_instantiation(instance):
    assert isinstance(instance, afpText_IOB)



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_XoaOrent_setter(instance):
    original = instance.XoaOrent
    instance.XoaOrent = original
    assert instance.XoaOrent == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_YoaOrent_setter(instance):
    original = instance.YoaOrent
    instance.YoaOrent = original
    assert instance.YoaOrent == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_XoaOset_setter(instance):
    original = instance.XoaOset
    instance.XoaOset = original
    assert instance.XoaOset == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_XocaOset_setter(instance):
    original = instance.XocaOset
    instance.XocaOset = original
    assert instance.XocaOset == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_ObjName_setter(instance):
    original = instance.ObjName
    instance.ObjName = original
    assert instance.ObjName == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_YocaOset_setter(instance):
    original = instance.YocaOset
    instance.YocaOset = original
    assert instance.YocaOset == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_RefCSys_setter(instance):
    original = instance.RefCSys
    instance.RefCSys = original
    assert instance.RefCSys == original



@given(instance=afpText_IOB_strategy)
def test_afptext_iob_YoaOset_setter(instance):
    original = instance.YoaOset
    instance.YoaOset = original
    assert instance.YoaOset == original

@given(instance=afpText_IMM_strategy)
@settings(max_examples=50)
def test_afptext_imm_instantiation(instance):
    assert isinstance(instance, afpText_IMM)



@given(instance=afpText_IMM_strategy)
def test_afptext_imm_MMPName_setter(instance):
    original = instance.MMPName
    instance.MMPName = original
    assert instance.MMPName == original

@given(instance=afpText_IID_strategy)
@settings(max_examples=50)
def test_afptext_iid_instantiation(instance):
    assert isinstance(instance, afpText_IID)



@given(instance=afpText_IID_strategy)
def test_afptext_iid_YSize_setter(instance):
    original = instance.YSize
    instance.YSize = original
    assert instance.YSize == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_YCSizeD_setter(instance):
    original = instance.YCSizeD
    instance.YCSizeD = original
    assert instance.YCSizeD == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_YBase_setter(instance):
    original = instance.YBase
    instance.YBase = original
    assert instance.YBase == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_ConData3_setter(instance):
    original = instance.ConData3
    instance.ConData3 = original
    assert instance.ConData3 == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_YUnits_setter(instance):
    original = instance.YUnits
    instance.YUnits = original
    assert instance.YUnits == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_XBase_setter(instance):
    original = instance.XBase
    instance.XBase = original
    assert instance.XBase == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_XCSizeD_setter(instance):
    original = instance.XCSizeD
    instance.XCSizeD = original
    assert instance.XCSizeD == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_XSize_setter(instance):
    original = instance.XSize
    instance.XSize = original
    assert instance.XSize == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_ConData2_setter(instance):
    original = instance.ConData2
    instance.ConData2 = original
    assert instance.ConData2 == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_ConData1_setter(instance):
    original = instance.ConData1
    instance.ConData1 = original
    assert instance.ConData1 == original



@given(instance=afpText_IID_strategy)
def test_afptext_iid_XUnits_setter(instance):
    original = instance.XUnits
    instance.XUnits = original
    assert instance.XUnits == original

@given(instance=afpText_IEL_strategy)
@settings(max_examples=50)
def test_afptext_iel_instantiation(instance):
    assert isinstance(instance, afpText_IEL)

@given(instance=afpText_IDD_strategy)
@settings(max_examples=50)
def test_afptext_idd_instantiation(instance):
    assert isinstance(instance, afpText_IDD)



@given(instance=afpText_IDD_strategy)
def test_afptext_idd_YSIZE_setter(instance):
    original = instance.YSIZE
    instance.YSIZE = original
    assert instance.YSIZE == original



@given(instance=afpText_IDD_strategy)
def test_afptext_idd_YRESOL_setter(instance):
    original = instance.YRESOL
    instance.YRESOL = original
    assert instance.YRESOL == original



@given(instance=afpText_IDD_strategy)
def test_afptext_idd_XRESOL_setter(instance):
    original = instance.XRESOL
    instance.XRESOL = original
    assert instance.XRESOL == original



@given(instance=afpText_IDD_strategy)
def test_afptext_idd_XSIZE_setter(instance):
    original = instance.XSIZE
    instance.XSIZE = original
    assert instance.XSIZE == original



@given(instance=afpText_IDD_strategy)
def test_afptext_idd_UNITBASE_setter(instance):
    original = instance.UNITBASE
    instance.UNITBASE = original
    assert instance.UNITBASE == original

@given(instance=afpText_GDD_strategy)
@settings(max_examples=50)
def test_afptext_gdd_instantiation(instance):
    assert isinstance(instance, afpText_GDD)



@given(instance=afpText_GDD_strategy)
def test_afptext_gdd_GOCAdes_setter(instance):
    original = instance.GOCAdes
    instance.GOCAdes = original
    assert instance.GOCAdes == original

@given(instance=afpText_GAD_strategy)
@settings(max_examples=50)
def test_afptext_gad_instantiation(instance):
    assert isinstance(instance, afpText_GAD)



@given(instance=afpText_GAD_strategy)
def test_afptext_gad_GOCAdat_setter(instance):
    original = instance.GOCAdat
    instance.GOCAdat = original
    assert instance.GOCAdat == original

@given(instance=afpText_FNPRG_strategy)
@settings(max_examples=50)
def test_afptext_fnprg_instantiation(instance):
    assert isinstance(instance, afpText_FNPRG)



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_LcHeight_setter(instance):
    original = instance.LcHeight
    instance.LcHeight = original
    assert instance.LcHeight == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_MaxDesDp_setter(instance):
    original = instance.MaxDesDp
    instance.MaxDesDp = original
    assert instance.MaxDesDp == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_Reserved3_setter(instance):
    original = instance.Reserved3
    instance.Reserved3 = original
    assert instance.Reserved3 == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_UscoreWdf_setter(instance):
    original = instance.UscoreWdf
    instance.UscoreWdf = original
    assert instance.UscoreWdf == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_Retired_setter(instance):
    original = instance.Retired
    instance.Retired = original
    assert instance.Retired == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_CapMHt_setter(instance):
    original = instance.CapMHt
    instance.CapMHt = original
    assert instance.CapMHt == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_MaxAscHt_setter(instance):
    original = instance.MaxAscHt
    instance.MaxAscHt = original
    assert instance.MaxAscHt == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_UscoreWd_setter(instance):
    original = instance.UscoreWd
    instance.UscoreWd = original
    assert instance.UscoreWd == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_UscorePos_setter(instance):
    original = instance.UscorePos
    instance.UscorePos = original
    assert instance.UscorePos == original



@given(instance=afpText_FNPRG_strategy)
def test_afptext_fnprg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText_FNP_strategy)
@settings(max_examples=50)
def test_afptext_fnp_instantiation(instance):
    assert isinstance(instance, afpText_FNP)

@given(instance=afpText_FNORG_strategy)
@settings(max_examples=50)
def test_afptext_fnorg_instantiation(instance):
    assert isinstance(instance, afpText_FNORG)



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_MaxCharInc_setter(instance):
    original = instance.MaxCharInc
    instance.MaxCharInc = original
    assert instance.MaxCharInc == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_NomCharInc_setter(instance):
    original = instance.NomCharInc
    instance.NomCharInc = original
    assert instance.NomCharInc == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_MaxBOset_setter(instance):
    original = instance.MaxBOset
    instance.MaxBOset = original
    assert instance.MaxBOset == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_DefBInc_setter(instance):
    original = instance.DefBInc
    instance.DefBInc = original
    assert instance.DefBInc == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_FigSpInc_setter(instance):
    original = instance.FigSpInc
    instance.FigSpInc = original
    assert instance.FigSpInc == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_Reserved3_setter(instance):
    original = instance.Reserved3
    instance.Reserved3 = original
    assert instance.Reserved3 == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_EmSpInc_setter(instance):
    original = instance.EmSpInc
    instance.EmSpInc = original
    assert instance.EmSpInc == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_OrntFlgs_setter(instance):
    original = instance.OrntFlgs
    instance.OrntFlgs = original
    assert instance.OrntFlgs == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_MaxBExt_setter(instance):
    original = instance.MaxBExt
    instance.MaxBExt = original
    assert instance.MaxBExt == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_SpCharInc_setter(instance):
    original = instance.SpCharInc
    instance.SpCharInc = original
    assert instance.SpCharInc == original



@given(instance=afpText_FNORG_strategy)
def test_afptext_fnorg_MinASp_setter(instance):
    original = instance.MinASp
    instance.MinASp = original
    assert instance.MinASp == original

@given(instance=afpText_FNO_strategy)
@settings(max_examples=50)
def test_afptext_fno_instantiation(instance):
    assert isinstance(instance, afpText_FNO)

@given(instance=afpText_FNMRG_strategy)
@settings(max_examples=50)
def test_afptext_fnmrg_instantiation(instance):
    assert isinstance(instance, afpText_FNMRG)



@given(instance=afpText_FNMRG_strategy)
def test_afptext_fnmrg_PatDOset_setter(instance):
    original = instance.PatDOset
    instance.PatDOset = original
    assert instance.PatDOset == original



@given(instance=afpText_FNMRG_strategy)
def test_afptext_fnmrg_CharBoxHt_setter(instance):
    original = instance.CharBoxHt
    instance.CharBoxHt = original
    assert instance.CharBoxHt == original



@given(instance=afpText_FNMRG_strategy)
def test_afptext_fnmrg_CharBoxWd_setter(instance):
    original = instance.CharBoxWd
    instance.CharBoxWd = original
    assert instance.CharBoxWd == original

@given(instance=afpText_FNM_strategy)
@settings(max_examples=50)
def test_afptext_fnm_instantiation(instance):
    assert isinstance(instance, afpText_FNM)

@given(instance=afpText_FNN_strategy)
@settings(max_examples=50)
def test_afptext_fnn_instantiation(instance):
    assert isinstance(instance, afpText_FNN)



@given(instance=afpText_FNN_strategy)
def test_afptext_fnn_FNNData_setter(instance):
    original = instance.FNNData
    instance.FNNData = original
    assert instance.FNNData == original

@given(instance=afpText_FNIRG_strategy)
@settings(max_examples=50)
def test_afptext_fnirg_instantiation(instance):
    assert isinstance(instance, afpText_FNIRG)



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_FNMCnt_setter(instance):
    original = instance.FNMCnt
    instance.FNMCnt = original
    assert instance.FNMCnt == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_CharInc_setter(instance):
    original = instance.CharInc
    instance.CharInc = original
    assert instance.CharInc == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_BaseOset_setter(instance):
    original = instance.BaseOset
    instance.BaseOset = original
    assert instance.BaseOset == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_CSpace_setter(instance):
    original = instance.CSpace
    instance.CSpace = original
    assert instance.CSpace == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_GCGID_setter(instance):
    original = instance.GCGID
    instance.GCGID = original
    assert instance.GCGID == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_BSpace_setter(instance):
    original = instance.BSpace
    instance.BSpace = original
    assert instance.BSpace == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_ASpace_setter(instance):
    original = instance.ASpace
    instance.ASpace = original
    assert instance.ASpace == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_DescendDp_setter(instance):
    original = instance.DescendDp
    instance.DescendDp = original
    assert instance.DescendDp == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_AscendHt_setter(instance):
    original = instance.AscendHt
    instance.AscendHt = original
    assert instance.AscendHt == original



@given(instance=afpText_FNIRG_strategy)
def test_afptext_fnirg_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText_FNI_strategy)
@settings(max_examples=50)
def test_afptext_fni_instantiation(instance):
    assert isinstance(instance, afpText_FNI)

@given(instance=afpText_FNG_strategy)
@settings(max_examples=50)
def test_afptext_fng_instantiation(instance):
    assert isinstance(instance, afpText_FNG)



@given(instance=afpText_FNG_strategy)
def test_afptext_fng_PatData_setter(instance):
    original = instance.PatData
    instance.PatData = original
    assert instance.PatData == original

@given(instance=afpText_EPT_strategy)
@settings(max_examples=50)
def test_afptext_ept_instantiation(instance):
    assert isinstance(instance, afpText_EPT)



@given(instance=afpText_EPT_strategy)
def test_afptext_ept_PTdoName_setter(instance):
    original = instance.PTdoName
    instance.PTdoName = original
    assert instance.PTdoName == original

@given(instance=afpText_FND_strategy)
@settings(max_examples=50)
def test_afptext_fnd_instantiation(instance):
    assert isinstance(instance, afpText_FND)



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_MinPtSize_setter(instance):
    original = instance.MinPtSize
    instance.MinPtSize = original
    assert instance.MinPtSize == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_TypeFcDesc_setter(instance):
    original = instance.TypeFcDesc
    instance.TypeFcDesc = original
    assert instance.TypeFcDesc == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_MaxPtSize_setter(instance):
    original = instance.MaxPtSize
    instance.MaxPtSize = original
    assert instance.MaxPtSize == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_DsnGenCls_setter(instance):
    original = instance.DsnGenCls
    instance.DsnGenCls = original
    assert instance.DsnGenCls == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_DsnSpcGrp_setter(instance):
    original = instance.DsnSpcGrp
    instance.DsnSpcGrp = original
    assert instance.DsnSpcGrp == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_FtWdClass_setter(instance):
    original = instance.FtWdClass
    instance.FtWdClass = original
    assert instance.FtWdClass == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_FtWtClass_setter(instance):
    original = instance.FtWtClass
    instance.FtWtClass = original
    assert instance.FtWtClass == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_NomHSize_setter(instance):
    original = instance.NomHSize
    instance.NomHSize = original
    assert instance.NomHSize == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_MaxHSize_setter(instance):
    original = instance.MaxHSize
    instance.MaxHSize = original
    assert instance.MaxHSize == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_Reserved1_setter(instance):
    original = instance.Reserved1
    instance.Reserved1 = original
    assert instance.Reserved1 == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_DsnSubCls_setter(instance):
    original = instance.DsnSubCls
    instance.DsnSubCls = original
    assert instance.DsnSubCls == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_MinHSize_setter(instance):
    original = instance.MinHSize
    instance.MinHSize = original
    assert instance.MinHSize == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_FGID_setter(instance):
    original = instance.FGID
    instance.FGID = original
    assert instance.FGID == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_GCSID_setter(instance):
    original = instance.GCSID
    instance.GCSID = original
    assert instance.GCSID == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_NomPtSize_setter(instance):
    original = instance.NomPtSize
    instance.NomPtSize = original
    assert instance.NomPtSize == original



@given(instance=afpText_FND_strategy)
def test_afptext_fnd_FtDsFlags_setter(instance):
    original = instance.FtDsFlags
    instance.FtDsFlags = original
    assert instance.FtDsFlags == original

@given(instance=afpText_FNC_strategy)
@settings(max_examples=50)
def test_afptext_fnc_instantiation(instance):
    assert isinstance(instance, afpText_FNC)



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_XUnitBase_setter(instance):
    original = instance.XUnitBase
    instance.XUnitBase = original
    assert instance.XUnitBase == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_OPatDCnt_setter(instance):
    original = instance.OPatDCnt
    instance.OPatDCnt = original
    assert instance.OPatDCnt == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_XftUnits_setter(instance):
    original = instance.XftUnits
    instance.XftUnits = original
    assert instance.XftUnits == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNNMapCnt_setter(instance):
    original = instance.FNNMapCnt
    instance.FNNMapCnt = original
    assert instance.FNNMapCnt == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNIRGLen_setter(instance):
    original = instance.FNIRGLen
    instance.FNIRGLen = original
    assert instance.FNIRGLen == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNNDCnt_setter(instance):
    original = instance.FNNDCnt
    instance.FNNDCnt = original
    assert instance.FNNDCnt == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNMRGLen_setter(instance):
    original = instance.FNMRGLen
    instance.FNMRGLen = original
    assert instance.FNMRGLen == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FntFlags_setter(instance):
    original = instance.FntFlags
    instance.FntFlags = original
    assert instance.FntFlags == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_ResYUBase_setter(instance):
    original = instance.ResYUBase
    instance.ResYUBase = original
    assert instance.ResYUBase == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_MaxBoxHt_setter(instance):
    original = instance.MaxBoxHt
    instance.MaxBoxHt = original
    assert instance.MaxBoxHt == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_PatAlign_setter(instance):
    original = instance.PatAlign
    instance.PatAlign = original
    assert instance.PatAlign == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_Retired_setter(instance):
    original = instance.Retired
    instance.Retired = original
    assert instance.Retired == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_PatTech_setter(instance):
    original = instance.PatTech
    instance.PatTech = original
    assert instance.PatTech == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_Reserved1_setter(instance):
    original = instance.Reserved1
    instance.Reserved1 = original
    assert instance.Reserved1 == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_RPatDCnt_setter(instance):
    original = instance.RPatDCnt
    instance.RPatDCnt = original
    assert instance.RPatDCnt == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_MaxBoxWd_setter(instance):
    original = instance.MaxBoxWd
    instance.MaxBoxWd = original
    assert instance.MaxBoxWd == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_ResXUBase_setter(instance):
    original = instance.ResXUBase
    instance.ResXUBase = original
    assert instance.ResXUBase == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNORGLen_setter(instance):
    original = instance.FNORGLen
    instance.FNORGLen = original
    assert instance.FNORGLen == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_YftUnits_setter(instance):
    original = instance.YftUnits
    instance.YftUnits = original
    assert instance.YftUnits == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNNRGLen_setter(instance):
    original = instance.FNNRGLen
    instance.FNNRGLen = original
    assert instance.FNNRGLen == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_FNPRGLen_setter(instance):
    original = instance.FNPRGLen
    instance.FNPRGLen = original
    assert instance.FNPRGLen == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_XfrUnits_setter(instance):
    original = instance.XfrUnits
    instance.XfrUnits = original
    assert instance.XfrUnits == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_YfrUnits_setter(instance):
    original = instance.YfrUnits
    instance.YfrUnits = original
    assert instance.YfrUnits == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original



@given(instance=afpText_FNC_strategy)
def test_afptext_fnc_YUnitBase_setter(instance):
    original = instance.YUnitBase
    instance.YUnitBase = original
    assert instance.YUnitBase == original

@given(instance=afpText_ESG_strategy)
@settings(max_examples=50)
def test_afptext_esg_instantiation(instance):
    assert isinstance(instance, afpText_ESG)



@given(instance=afpText_ESG_strategy)
def test_afptext_esg_REGName_setter(instance):
    original = instance.REGName
    instance.REGName = original
    assert instance.REGName == original

@given(instance=afpText_ERS_strategy)
@settings(max_examples=50)
def test_afptext_ers_instantiation(instance):
    assert isinstance(instance, afpText_ERS)



@given(instance=afpText_ERS_strategy)
def test_afptext_ers_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_ERG_strategy)
@settings(max_examples=50)
def test_afptext_erg_instantiation(instance):
    assert isinstance(instance, afpText_ERG)



@given(instance=afpText_ERG_strategy)
def test_afptext_erg_RGrpName_setter(instance):
    original = instance.RGrpName
    instance.RGrpName = original
    assert instance.RGrpName == original

@given(instance=afpText_EIM_strategy)
@settings(max_examples=50)
def test_afptext_eim_instantiation(instance):
    assert isinstance(instance, afpText_EIM)



@given(instance=afpText_EIM_strategy)
def test_afptext_eim_IdoName_setter(instance):
    original = instance.IdoName
    instance.IdoName = original
    assert instance.IdoName == original

@given(instance=afpText_EPS_strategy)
@settings(max_examples=50)
def test_afptext_eps_instantiation(instance):
    assert isinstance(instance, afpText_EPS)



@given(instance=afpText_EPS_strategy)
def test_afptext_eps_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText_EPM_strategy)
@settings(max_examples=50)
def test_afptext_epm_instantiation(instance):
    assert isinstance(instance, afpText_EPM)



@given(instance=afpText_EPM_strategy)
def test_afptext_epm_PMName_setter(instance):
    original = instance.PMName
    instance.PMName = original
    assert instance.PMName == original

@given(instance=afpText_EPG_strategy)
@settings(max_examples=50)
def test_afptext_epg_instantiation(instance):
    assert isinstance(instance, afpText_EPG)



@given(instance=afpText_EPG_strategy)
def test_afptext_epg_PageName_setter(instance):
    original = instance.PageName
    instance.PageName = original
    assert instance.PageName == original

@given(instance=afpText_EPF_strategy)
@settings(max_examples=50)
def test_afptext_epf_instantiation(instance):
    assert isinstance(instance, afpText_EPF)



@given(instance=afpText_EPF_strategy)
def test_afptext_epf_PFName_setter(instance):
    original = instance.PFName
    instance.PFName = original
    assert instance.PFName == original

@given(instance=afpText_EOG_strategy)
@settings(max_examples=50)
def test_afptext_eog_instantiation(instance):
    assert isinstance(instance, afpText_EOG)



@given(instance=afpText_EOG_strategy)
def test_afptext_eog_OEGName_setter(instance):
    original = instance.OEGName
    instance.OEGName = original
    assert instance.OEGName == original

@given(instance=afpText_EOC_strategy)
@settings(max_examples=50)
def test_afptext_eoc_instantiation(instance):
    assert isinstance(instance, afpText_EOC)



@given(instance=afpText_EOC_strategy)
def test_afptext_eoc_ObjCName_setter(instance):
    original = instance.ObjCName
    instance.ObjCName = original
    assert instance.ObjCName == original

@given(instance=afpText_ENG_strategy)
@settings(max_examples=50)
def test_afptext_eng_instantiation(instance):
    assert isinstance(instance, afpText_ENG)



@given(instance=afpText_ENG_strategy)
def test_afptext_eng_PGrpName_setter(instance):
    original = instance.PGrpName
    instance.PGrpName = original
    assert instance.PGrpName == original

@given(instance=afpText_EMO_strategy)
@settings(max_examples=50)
def test_afptext_emo_instantiation(instance):
    assert isinstance(instance, afpText_EMO)



@given(instance=afpText_EMO_strategy)
def test_afptext_emo_OvlyName_setter(instance):
    original = instance.OvlyName
    instance.OvlyName = original
    assert instance.OvlyName == original

@given(instance=afpText_EMM_strategy)
@settings(max_examples=50)
def test_afptext_emm_instantiation(instance):
    assert isinstance(instance, afpText_EMM)



@given(instance=afpText_EMM_strategy)
def test_afptext_emm_MMName_setter(instance):
    original = instance.MMName
    instance.MMName = original
    assert instance.MMName == original

@given(instance=afpText_EII_strategy)
@settings(max_examples=50)
def test_afptext_eii_instantiation(instance):
    assert isinstance(instance, afpText_EII)



@given(instance=afpText_EII_strategy)
def test_afptext_eii_ImoName_setter(instance):
    original = instance.ImoName
    instance.ImoName = original
    assert instance.ImoName == original

@given(instance=afpText_EGR_strategy)
@settings(max_examples=50)
def test_afptext_egr_instantiation(instance):
    assert isinstance(instance, afpText_EGR)



@given(instance=afpText_EGR_strategy)
def test_afptext_egr_GdoName_setter(instance):
    original = instance.GdoName
    instance.GdoName = original
    assert instance.GdoName == original

@given(instance=afpText_EFN_strategy)
@settings(max_examples=50)
def test_afptext_efn_instantiation(instance):
    assert isinstance(instance, afpText_EFN)



@given(instance=afpText_EFN_strategy)
def test_afptext_efn_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText_EFM_strategy)
@settings(max_examples=50)
def test_afptext_efm_instantiation(instance):
    assert isinstance(instance, afpText_EFM)



@given(instance=afpText_EFM_strategy)
def test_afptext_efm_FMName_setter(instance):
    original = instance.FMName
    instance.FMName = original
    assert instance.FMName == original

@given(instance=afpText_EFG_strategy)
@settings(max_examples=50)
def test_afptext_efg_instantiation(instance):
    assert isinstance(instance, afpText_EFG)



@given(instance=afpText_EFG_strategy)
def test_afptext_efg_FEGName_setter(instance):
    original = instance.FEGName
    instance.FEGName = original
    assert instance.FEGName == original

@given(instance=afpText_EDX_strategy)
@settings(max_examples=50)
def test_afptext_edx_instantiation(instance):
    assert isinstance(instance, afpText_EDX)



@given(instance=afpText_EDX_strategy)
def test_afptext_edx_DMXName_setter(instance):
    original = instance.DMXName
    instance.DMXName = original
    assert instance.DMXName == original

@given(instance=afpText_EDT_strategy)
@settings(max_examples=50)
def test_afptext_edt_instantiation(instance):
    assert isinstance(instance, afpText_EDT)



@given(instance=afpText_EDT_strategy)
def test_afptext_edt_DocName_setter(instance):
    original = instance.DocName
    instance.DocName = original
    assert instance.DocName == original
